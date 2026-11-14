#!/usr/bin/env bash
set -euo pipefail
case "${1:-}" in
  --menu|--list)
    exec python3 /root/.local/lib/sam-menu/sam_menu.py "$@" ;;
esac
if (( $# == 0 )); then
  exec python3 /root/.local/lib/sam-menu/sam_menu.py
fi
exec /root/.local/lib/sam-menu/sam-legacy.sh "$@"
