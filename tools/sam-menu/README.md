# Sam parallel menu

Run `sam` or `sam --menu` in an interactive terminal. Existing sam-* tmux
sessions are listed, including legacy workers. Enter a number to reconnect, N
to create a task, R to refresh, or Q to leave. Ctrl+B then D detaches without
stopping the worker. Run sam again to open another task. Maximum: three sessions
created through this menu, including existing sam-* sessions. Direct tmux/legacy
invocations are outside this admission limit.

Each new Git task starts on a fresh Codex/sam-* branch and worktree at the
selected checkout's HEAD. Dirty sources are refused to avoid silently omitting
uncommitted work. No full repository clone is made. A non-Git task gets an empty
private output directory and a read-only instruction for its reference directory.
Worktree separation is not an OS security sandbox; model permissions and the
existing bridge are unchanged. Shared services still require coordination.
New sessions do not inherit another worker's conversation or resume ID.

The model bridge remains /root/.local/bin/claude-gpt; context remains 200000.
Commands with Claude options (including --print, --help, --version) keep the
previous launcher behavior. --list shows sessions without starting a model.
The menu does not classify whether Claude is thinking or waiting for input:
it shows the foreground command, workspace, and task label.

When Claude exits, press Enter to close its tmux session and free the slot.
Workspaces, branches and task metadata remain on disk. There is no automatic
deletion of work. Review/commit/merge a completed task before using ordinary
git worktree remove on its recorded worktree; never force-remove dirty work.
Closing the menu or SSH does not cancel the workers.

Tests use real tmux on private sockets and a fake executable, with no model
calls: three concurrent sessions, fourth rejected, legacy sessions preserved,
dirty source refusal, shell-metacharacter safety and private non-Git workspaces.
Run: python3 tools/sam-menu/test_sam_menu.py

Installed launcher has a timestamped backup under /root/.local/share/sam-menu/
backups/. Restore that sam.sh backup to /root/sam.sh to roll back. No running
session needs restarting. Do not include task.json or credentials in source control.
