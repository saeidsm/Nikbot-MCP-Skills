#!/usr/bin/env bash
# claude-gpt — Claude Code via the LOCAL CLIProxyAPI bridge (ChatGPT/Codex
# subscription; no OpenAI API billing). Installed by
# /root/.claude-gpt-bridge/activate.sh — remove with rollback.sh.
# Only backend/model variables are overridden here; everything else in your
# environment is preserved. Absolute path on purpose: with --wrap-claude a
# wrapper dir precedes this on PATH and a bare `claude` would recurse.
#
# Model mapping (Claude Code documented behavior):
#   ANTHROPIC_MODEL               -> main model
#   ANTHROPIC_DEFAULT_SONNET_MODEL -> what the `sonnet` alias resolves to (also subagents)
#   ANTHROPIC_DEFAULT_OPUS_MODEL   -> what the `opus` alias resolves to (also Plan Mode)
#   ANTHROPIC_DEFAULT_FABLE_MODEL  -> Fable resolves to gpt-6-astra
#   ANTHROPIC_DEFAULT_HAIKU_MODEL  -> what the `haiku` alias resolves to + background/fast tasks
#   ANTHROPIC_SMALL_FAST_MODEL     -> deprecated; unset so nothing stale leaks in
#   CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY -> /model picker lists the bridge's /v1/models
set -euo pipefail
. /root/.claude-gpt-bridge/bridge.env
exec env \
  -u ANTHROPIC_API_KEY \
  -u ANTHROPIC_DEFAULT_MODEL \
  -u ANTHROPIC_DEFAULT_OPUS_MODEL \
  -u ANTHROPIC_DEFAULT_OPUS_MODEL_DESCRIPTION \
  -u ANTHROPIC_DEFAULT_FABLE_MODEL_SUPPORTED_CAPABILITIES \
  -u ANTHROPIC_DEFAULT_SONNET_MODEL \
  -u ANTHROPIC_DEFAULT_SONNET_MODEL_DESCRIPTION \
  -u ANTHROPIC_DEFAULT_HAIKU_MODEL \
  -u ANTHROPIC_DEFAULT_HAIKU_MODEL_DESCRIPTION \
  -u ANTHROPIC_SMALL_FAST_MODEL \
  -u OPENROUTER_API_KEY \
  ANTHROPIC_BASE_URL="http://127.0.0.1:${BRIDGE_PORT}" \
  ANTHROPIC_AUTH_TOKEN="$BRIDGE_API_KEY" \
  ANTHROPIC_MODEL="gpt-6.1-sol" \
  ANTHROPIC_DEFAULT_SONNET_MODEL="$BRIDGE_MODEL" \
  ANTHROPIC_DEFAULT_OPUS_MODEL="gpt-6.1-sol" \
  ANTHROPIC_DEFAULT_FABLE_MODEL=gpt-6-astra \
  ANTHROPIC_DEFAULT_FABLE_MODEL_NAME='Fable (GPT-6 Astra)' \
  ANTHROPIC_DEFAULT_FABLE_MODEL_DESCRIPTION='ChatGPT subscription via local CLIProxyAPI' \
  ANTHROPIC_DEFAULT_HAIKU_MODEL="$BRIDGE_FAST_MODEL" \
  CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1 \
  API_TIMEOUT_MS=600000 \
  DISABLE_TELEMETRY=1 \
  /root/.local/bin/claude "$@"
