"""Offline request-example validation against a source-derived schema snapshot.

Requires jsonschema; no source checkout, credentials, network or MCP handlers.
A passing input schema does not establish authorization or execution success.
"""
from pathlib import Path
import json
import re

from jsonschema import Draft202012Validator


def validate_pack(root: Path) -> tuple[int, int, int]:
    pack = json.loads((root / 'skills/using-nikbot-mcp/examples.json').read_text())
    snapshot = json.loads((root / 'protocol/tool-input-schemas.json').read_text())
    if pack['pack_version'] != snapshot['pack_version'] or pack['pack_version'] != '0.2.0':
        raise ValueError('Pack/schema version mismatch')
    if not re.fullmatch(r'[a-f0-9]{40}', snapshot['source_commit']):
        raise ValueError('Missing exact source commit')
    tools = snapshot['tools']
    registry = {tool['name']: tool['inputSchema'] for tool in tools}
    if len(registry) != len(tools) or not registry:
        raise ValueError('Duplicate or missing tools')
    for schema in registry.values():
        Draft202012Validator.check_schema(schema)
    cases = pack['cases']
    if not cases or len({case['id'] for case in cases}) != len(cases):
        raise ValueError('Duplicate or missing examples')
    covered, accepted, rejected = set(), 0, 0
    for case in cases:
        request = case['request']
        if (set(request) != {'jsonrpc', 'id', 'method', 'params'}
                or request['jsonrpc'] != '2.0' or request['method'] != 'tools/call'
                or request['id'] != case['id']):
            raise ValueError('Invalid example request envelope')
        params = request['params']
        if set(params) != {'name', 'arguments'} or params['name'] not in registry:
            raise ValueError('Unknown tool or arguments envelope')
        expected = case['schema_valid']
        valid = Draft202012Validator(registry[params['name']]).is_valid(params['arguments'])
        if type(expected) is not bool or valid != expected:
            raise ValueError(f'Unexpected schema result for {case["id"]}')
        if expected:
            covered.add(params['name'])
            accepted += 1
        else:
            rejected += 1
    if covered != set(registry) or rejected < 5:
        raise ValueError('Incomplete tool or negative-example coverage')
    return accepted, rejected, len(registry)


if __name__ == '__main__':
    accepted, rejected, tools = validate_pack(Path(__file__).resolve().parents[1])
    print(f'PASS: {accepted} valid, {rejected} invalid examples; {tools} tools. '
          'Offline input schemas only; no tool handlers invoked.')
