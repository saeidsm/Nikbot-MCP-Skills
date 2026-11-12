# Nikbot-MCP-Skills

Versioned caller guidance for the existing NikBot MCP service. Product implementation remains in [Codex-Cli-MCP](https://github.com/saeidsm/Codex-Cli-MCP); this repository contains reusable documentation, input schemas, synthetic examples and offline validation—not copied service code or private project state.

## Caller pack 0.2.0

Start with [using-nikbot-mcp](skills/using-nikbot-mcp/SKILL.md). It covers discovery, configured route selection, durable submission/idempotency, status/results, supplemental human-approval boundaries, questions/resume, artifact verification and a safe handoff. It explicitly identifies unsupported cancellation, event streams, Swarm, memory APIs, metrics and cleanup rather than inventing tools.

- [Request examples and invalid counterexamples](skills/using-nikbot-mcp/examples.json)
- [Source-advertised tool input schemas](protocol/tool-input-schemas.json)
- [Verification and limitations](docs/VERIFICATION.md)
- [Versioning and compatibility](protocol/versioning.md)

The schema snapshot was exported without dispatching tool handlers from source commit [`9e7b8d9100f07d092f6460bd06760a95af71778f`](https://github.com/saeidsm/Codex-Cli-MCP/commit/9e7b8d9100f07d092f6460bd06760a95af71778f). It is not a live deployment attestation. The connected server's authenticated `tools/list` and actual capability response remain authoritative; a snapshot does not grant execution permission.

## Use or install

1. Review this pack at a specific commit. Obtain an already-authorized MCP connection and granted project ID through the operator's existing flow. The pack supplies neither credentials nor permission.
2. For a client supporting `SKILL.md`, copy the **whole** `skills/using-nikbot-mcp/` directory into that client's approved project-local skill location, preserving `examples.json`. Inspect the destination first; never overwrite an existing skill without reviewing its differences. For Claude Code, a supported project location is `.claude/skills/using-nikbot-mcp/`. Other clients may load the Markdown as reference through their supported attachment/instruction mechanism.
3. Keep this checkout as the maintainer reference: links outside the installed skill directory point into this repository and are not installation prerequisites. No automatic edits to global settings, hooks, permissions or server configuration are required or performed.
4. Discover actual tools before sending requests. Example IDs, model names, project IDs and signatures are placeholders—not executable jobs or consent. Never run the example collection as a workflow.

## Offline checks

With Python 3.10+ and an existing environment providing `jsonschema`:

```sh
python -B scripts/validate_pack.py
python -B -m unittest discover -s tests -v
```

These tests use only packaged input schemas and synthetic examples. They make no network, model, live authentication or MCP tool calls. They do not prove backend acceptance, deployment health or native permission enforcement.

## Publication and implementation status

This increment prepares a reviewed **feature-branch publication**, not a release on `main`. A push does not imply merge, installation or server deployment. No package installer, autoupdater or credential bootstrap is included. See verification evidence for the actual completed checks; do not infer missing checks from these instructions.

The historical [implementation directive](prompts/NIKBOT_MCP_UNIFIED_EXECUTION_DIRECTIVE_2026-11-11.md) is retained unchanged as project history, not a record that its requested features exist, nor authority to bypass current owner policy. Its aspirational protocol fields must not be inserted into current tool arguments.
