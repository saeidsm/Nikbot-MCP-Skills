#!/usr/bin/env python3
"""Three independent Sam terminals; the existing model bridge stays unchanged."""
import fcntl
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import uuid

STATE = Path("/root/.local/share/sam-menu")
BRIDGE = "/root/.local/bin/claude-gpt"
GUARD = """Work only on the assigned task in this workspace. Other Sam sessions may be active.
Do not modify another worktree, shared deployment, service, database or global configuration
unless this task explicitly authorizes it. Do not merge, deploy or clean other sessions.
Read applicable project instructions. Preserve existing changes. Report tests and changed files.
"""
def run(args, check=True):
    return subprocess.run(args, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=check)

class Menu:
    def __init__(self, state=STATE, tmux=None, bridge=BRIDGE):
        self.state = Path(state)
        self.tmux = tmux or ["tmux"]
        self.bridge = bridge
        self.state.mkdir(mode=0o700, parents=True, exist_ok=True)

    def tm(self, *args, check=True):
        return run(self.tmux + list(args), check)

    def sessions(self):
        result = self.tm("list-sessions", "-F", "#{session_name}", check=False)
        if result.returncode:
            if "no server running" in result.stderr or "No such file" in result.stderr:
                return []
            raise RuntimeError(result.stderr.strip())
        return sorted(n for n in result.stdout.splitlines()
                      if n == "sam" or n.startswith("sam-"))

    def create(self, directory, task):
        directory = Path(directory).expanduser().resolve(strict=True)
        if not directory.is_dir() or not task.strip():
            raise ValueError("Choose a directory and enter a nonempty task.")
        with (self.state / "launch.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            if len(self.sessions()) >= 3:
                raise ValueError("Three Sam sessions already exist. Reconnect or close a finished session first.")
            ident = uuid.uuid4().hex[:12]
            name = "sam-" + ident
            job = self.state / ident
            job.mkdir(mode=0o700)
            work = directory
            repo = run(["git", "-C", str(directory), "rev-parse", "--show-toplevel"], False)
            branch = None
            if repo.returncode == 0:
                root = Path(repo.stdout.strip()).resolve()
                if run(["git", "-C", str(root), "status", "--porcelain"]).stdout:
                    raise ValueError("Project has uncommitted changes. Commit/review them first; nothing was copied or changed.")
                branch = "Codex/sam-" + ident
                work = job / "worktree"
                run(["git", "-C", str(root), "worktree", "add", "-b", branch, str(work), "HEAD"])
                work = work / directory.relative_to(root)
            else:
                # Non-Git tasks get a private workspace too, never a shared cwd.
                work = job / "workspace"
                work.mkdir()
                task = "Reference directory: " + str(directory) + "\nUse it read-only; write outputs in your private workspace.\n\n" + task
            meta = {"session": name, "task": task, "source": str(directory),
                    "workspace": str(work), "branch": branch}
            (job / "task.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))
            # Script is quoted as data; arbitrary task text never becomes shell code.
            script = "#!/usr/bin/env bash\nset -uo pipefail\n"
            script += "export CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000\n"
            script += "cd -- " + shlex.quote(str(work)) + "\n"
            script += shlex.join([self.bridge, "--append-system-prompt", GUARD, "--", task]) + "\n"
            script += "status=$?\nprintf '\\nSam exited (%s). Workspace preserved. Press Enter to close.\\n' \"$status\"\nread -r _\n"
            runner = job / "run.sh"
            runner.write_text(script)
            runner.chmod(0o700)
            self.tm("new-session", "-d", "-s", name, "-c", str(work),
                    shlex.join(["/bin/bash", str(runner)]))
            self.tm("set-option", "-t", name, "@sam_managed", "2")
            self.tm("set-option", "-t", name, "@sam_job", ident)
            return name

    def attach(self, name):
        if name not in self.sessions():
            raise ValueError("Session no longer exists.")
        cmd = "switch-client" if os.environ.get("TMUX") else "attach-session"
        subprocess.run(self.tmux + [cmd, "-t", name], check=True)

    def describe(self, name):
        p = self.tm("list-panes", "-t", name, "-F",
                    "#{pane_current_command} | #{pane_current_path}", check=False)
        label = ""
        job = self.tm("show-options", "-qv", "-t", name, "@sam_job", check=False).stdout.strip()
        if re.fullmatch(r"[0-9a-f]{12}", job):
            try:
                label = json.loads((self.state / job / "task.json").read_text())["task"]
                label = " | Task: " + label.splitlines()[-1][:100]
            except (OSError, ValueError, KeyError, IndexError):
                pass
        return p.stdout.strip() + label

def clean_display(value):
    return "".join(c for c in value if c.isprintable())

def main():
    menu = Menu()
    if sys.argv[1:] == ["--list"]:
        for name in menu.sessions():
            print(name + " | " + clean_display(menu.describe(name)))
        return
    if sys.argv[1:] not in ([], ["--menu"]):
        raise ValueError("Use sam, sam --menu, or sam --list.")
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        raise ValueError("Interactive terminal required. Use sam --list or sam --print.")
    while True:
        sessions = menu.sessions()
        print("\n=== SAM | Parallel tasks | " + str(len(sessions)) + "/3 ===")
        for i, name in enumerate(sessions, 1):
            print(str(i) + ") " + name + " | " + clean_display(menu.describe(name)))
        print("\nN) New task   R) Refresh   Q) Exit")
        print("Select a number to reconnect. Detach: Ctrl+B, then D (task keeps running).")
        choice = input("> ").strip().lower()
        if choice == "q":
            return
        try:
            if choice == "n":
                if len(sessions) >= 3:
                    print("All three slots are occupied.")
                    continue
                directory = input("Project directory [" + os.getcwd() + "]: ").strip() or os.getcwd()
                task = input("Task (one line; details can be added after opening): ").strip()
                name = menu.create(directory, task)
                print("Created " + name + ". Workspace preserved after exit.")
                menu.attach(name)
                if os.environ.get("TMUX"):
                    return
            elif choice.isdigit() and 1 <= int(choice) <= len(sessions):
                menu.attach(sessions[int(choice) - 1])
                if os.environ.get("TMUX"):
                    return
        except (ValueError, OSError, subprocess.CalledProcessError, RuntimeError) as exc:
            print("Sam: " + str(exc))
            if isinstance(exc, subprocess.CalledProcessError):
                print(clean_display(exc.stderr or ""))

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nMenu closed; running sessions are unchanged.")
    except (ValueError, OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        print("Sam: " + str(exc), file=sys.stderr)
        sys.exit(1)
