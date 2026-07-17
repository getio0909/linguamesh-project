#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARGUMENTS=(--project-root "$PROJECT_ROOT")

if [[ "${1:-}" == "--require-repositories" ]]; then
  ARGUMENTS+=(--require-repositories)
elif [[ -n "${1:-}" ]]; then
  echo "Usage: tools/check-workspace.sh [--require-repositories]" >&2
  exit 2
fi

PYTHON_COMMAND="${PYTHON_COMMAND:-python3}"
if ! command -v "$PYTHON_COMMAND" >/dev/null 2>&1; then
  echo "Validation failed: Python 3.11 or newer is required." >&2
  exit 1
fi

"$PYTHON_COMMAND" "$PROJECT_ROOT/tools/check_workspace.py" "${ARGUMENTS[@]}"

if git -C "$PROJECT_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git -C "$PROJECT_ROOT" diff --check
fi

