#!/usr/bin/env bash
# Launch Claude via the local ChatGPT bridge, in a managed tmux session.
# Inside tmux, run in the current pane instead. No provider fallback.
set -euo pipefail
claude_gpt=/root/.local/bin/claude-gpt
session=sam-claude
# Keep a conservative session-wide context assumption for gateway models.
: "${CLAUDE_CODE_MAX_CONTEXT_TOKENS:=200000}"
export CLAUDE_CODE_MAX_CONTEXT_TOKENS

# Noninteractive and informational CLI modes must retain their normal behavior.
for arg in "$@"; do
  case "$arg" in
    -p|--print|--help|--version|-h|-v) exec "$claude_gpt" "$@" ;;
  esac
done
if [[ -n "${TMUX:-}" ]]; then
  exec "$claude_gpt" "$@"
fi
if ! command -v tmux >/dev/null 2>&1; then
  echo 'sam: tmux is required for an interactive session.' >&2
  exit 1
fi
if [[ ! -t 0 || ! -t 1 ]]; then
  echo 'sam: an interactive terminal is required; use --print for noninteractive mode.' >&2
  exit 1
fi
if tmux list-sessions -F "#{session_name}" 2>/dev/null | grep -Fxq -- "$session"; then
  managed=$(tmux show-options -qv -t "$session" @sam_managed || true)
  if [[ "$managed" != 1 ]]; then
    echo "sam: tmux session '$session' already exists and is not managed by sam; leaving it untouched." >&2
    exit 1
  fi
  if (( $# )); then
    echo "sam: an existing session will be reused, so launch options cannot be applied; re-run sam without options." >&2
    exit 1
  fi
else
  tmux new-session -d -s "$session" -c "$PWD" env "CLAUDE_CODE_MAX_CONTEXT_TOKENS=$CLAUDE_CODE_MAX_CONTEXT_TOKENS" "$claude_gpt" "$@"
  tmux set-option -t "$session" @sam_managed 1
fi
exec tmux attach-session -t "$session"
