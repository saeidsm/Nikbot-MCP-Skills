import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import time
import unittest
import uuid

spec = importlib.util.spec_from_file_location("sam_menu", Path(__file__).with_name("sam_menu.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class Integration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.tmux = ["tmux", "-L", "sam-test-" + uuid.uuid4().hex]
        bridge = self.base / "fake-bridge"
        bridge.write_text("#!/bin/sh\nprintf '%s\\n' \"$@\"\nsleep 60\n")
        bridge.chmod(0o700)
        self.menu = m.Menu(self.base / "state", self.tmux, str(bridge))
        self.repo = self.base / "repo"
        self.repo.mkdir()
        self.git("init")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        (self.repo / "hello").write_text("baseline")
        self.git("add", "hello")
        self.git("commit", "-m", "fixture")

    def git(self, *args):
        return m.run(["git", "-C", str(self.repo), *args])

    def tearDown(self):
        m.run(self.tmux + ["kill-server"], False)
        self.tmp.cleanup()

    def test_three_parallel_independent_and_fourth_rejected(self):
        names = [self.menu.create(self.repo, "task " + str(i)) for i in range(3)]
        self.assertEqual(sorted(names), self.menu.sessions())
        paths = [self.menu.tm("display-message", "-p", "-t", n,
                             "#{pane_current_path}").stdout.strip() for n in names]
        self.assertEqual(len(set(paths)), 3)
        for p in paths:
            self.assertNotEqual(Path(p), self.repo)
            self.assertTrue((Path(p) / "hello").exists())
        with self.assertRaisesRegex(ValueError, "Three"):
            self.menu.create(self.repo, "fourth")
        self.assertEqual(len(self.menu.sessions()), 3)

    def test_dirty_project_rejected_without_launch(self):
        (self.repo / "hello").write_text("uncommitted")
        with self.assertRaisesRegex(ValueError, "uncommitted"):
            self.menu.create(self.repo, "task")
        self.assertEqual(self.menu.sessions(), [])
        self.assertEqual((self.repo / "hello").read_text(), "uncommitted")

    def test_task_is_data_not_shell(self):
        marker = self.base / "SHOULD_NOT_EXIST"
        name = self.menu.create(self.repo, "$(touch " + str(marker) + "); 'quoted' & --help")
        time.sleep(0.3)
        self.assertFalse(marker.exists())
        pane = self.menu.tm("capture-pane", "-p", "-t", name).stdout
        self.assertIn("SHOULD_NOT_EXIST", pane)
        self.assertIn(name, self.menu.sessions())

    def test_non_git_private_workspace(self):
        source = self.base / "documents"
        source.mkdir()
        name = self.menu.create(source, "report")
        cwd = self.menu.tm("display-message", "-p", "-t", name,
                           "#{pane_current_path}").stdout.strip()
        self.assertNotEqual(Path(cwd), source)
        self.assertTrue(Path(cwd).is_relative_to(self.menu.state))

    def test_existing_sessions_count_and_survive(self):
        for name in ["sam-mcp-existing", "sam-rag-existing"]:
            self.menu.tm("new-session", "-d", "-s", name, "sleep 60")
        self.menu.create(self.repo, "third")
        with self.assertRaisesRegex(ValueError, "Three"):
            self.menu.create(self.repo, "fourth")
        self.assertIn("sam-mcp-existing", self.menu.sessions())

    def test_finished_session_preserved_not_capacity(self):
        name = self.menu.create(self.repo, "done")
        job = self.menu.tm("show-options", "-qv", "-t", name, "@sam_job").stdout.strip()
        # Simulate runner completion after process exits; record stays visible.
        (self.menu.state / job / "exit.status").write_text("0\n")
        self.assertIn(name, self.menu.sessions())
        self.assertNotIn(name, self.menu.active_sessions())
        self.assertIn("exited", self.menu.describe(name))

    def test_role_model_is_explicit(self):
        name = self.menu.create(self.repo, "planning", "plan")
        time.sleep(0.2)
        pane = self.menu.tm("capture-pane", "-p", "-t", name).stdout
        self.assertIn("fable", pane)
        self.assertIn("gpt-6-astra", self.menu.describe(name))
        with self.assertRaises(ValueError):
            self.menu.create(self.repo, "invalid", "bad")

if __name__ == "__main__":
    unittest.main(verbosity=2)
