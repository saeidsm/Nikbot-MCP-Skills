"""Offline publication checks: never contact or invoke an MCP server."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location('validate_pack', ROOT / 'scripts/validate_pack.py')
        cls.validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.validator)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('skills', 'protocol'):
            shutil.copytree(ROOT / name, self.root / name)

    def change(self, relative, mutate):
        path = self.root / relative
        data = json.loads(path.read_text())
        mutate(data)
        path.write_text(json.dumps(data))

    def test_current_pack_has_all_actual_tools_and_counterexamples(self):
        self.assertEqual(self.validator.validate_pack(self.root), (17, 13, 13))

    def test_bad_example_is_rejected(self):
        self.change('skills/using-nikbot-mcp/examples.json',
                    lambda d: d['cases'][1]['request']['params']['arguments'].update(owner='forged'))
        with self.assertRaises(ValueError):
            self.validator.validate_pack(self.root)

    def test_lost_tool_coverage_is_rejected(self):
        self.change('skills/using-nikbot-mcp/examples.json',
                    lambda d: d.update(cases=[c for c in d['cases'] if c['id'] != 'discover']))
        with self.assertRaises(ValueError):
            self.validator.validate_pack(self.root)

    def test_version_mismatch_is_rejected(self):
        self.change('protocol/tool-input-schemas.json', lambda d: d.update(pack_version='99.0.0'))
        with self.assertRaises(ValueError):
            self.validator.validate_pack(self.root)

    def test_duplicate_case_is_rejected(self):
        self.change('skills/using-nikbot-mcp/examples.json', lambda d: d['cases'].append(d['cases'][0]))
        with self.assertRaises(ValueError):
            self.validator.validate_pack(self.root)

    def test_duplicate_tool_is_rejected(self):
        self.change('protocol/tool-input-schemas.json', lambda d: d['tools'].append(d['tools'][0]))
        with self.assertRaises(ValueError):
            self.validator.validate_pack(self.root)

    def test_invalid_rpc_envelope_is_rejected(self):
        self.change('skills/using-nikbot-mcp/examples.json',
                    lambda d: d['cases'][0]['request'].update(method='invented/call'))
        with self.assertRaises(ValueError):
            self.validator.validate_pack(self.root)


if __name__ == '__main__':
    unittest.main()
