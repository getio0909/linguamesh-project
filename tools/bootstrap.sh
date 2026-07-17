#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORKSPACE_ROOT="$(dirname "$PROJECT_ROOT")"
GITHUB_OWNER_VALUE="${GITHUB_OWNER:-}"
CHECK_ONLY=false
FETCH_EXISTING=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --owner)
      GITHUB_OWNER_VALUE="${2:-}"
      shift 2
      ;;
    --check-only)
      CHECK_ONLY=true
      shift
      ;;
    --fetch-existing)
      FETCH_EXISTING=true
      shift
      ;;
    *)
      echo "Usage: tools/bootstrap.sh [--owner OWNER] [--check-only] [--fetch-existing]" >&2
      exit 2
      ;;
  esac
done

REPOSITORIES=(
  linguamesh-project
  linguamesh-core
  linguamesh-l10n
  linguamesh-android
  linguamesh-windows
  linguamesh-macos
  linguamesh-linux
)
MISSING=0

for repository in "${REPOSITORIES[@]}"; do
  target="$WORKSPACE_ROOT/$repository"
  if [[ -d "$target" ]]; then
    echo "Existing repository preserved: $target"
    if [[ "$FETCH_EXISTING" == true && -d "$target/.git" ]]; then
      git -C "$target" fetch --prune
      echo "Fetched remote references: $repository"
    fi
    continue
  fi

  MISSING=$((MISSING + 1))
  if [[ "$CHECK_ONLY" == true ]]; then
    echo "Missing repository: $target"
    continue
  fi
  if [[ -z "$GITHUB_OWNER_VALUE" ]]; then
    echo "Bootstrap failed: --owner or GITHUB_OWNER is required to clone $repository." >&2
    exit 1
  fi
  if ! command -v gh >/dev/null 2>&1; then
    echo "Bootstrap failed: GitHub CLI is required to clone missing repositories." >&2
    exit 1
  fi
  if ! gh repo view "$GITHUB_OWNER_VALUE/$repository" >/dev/null 2>&1; then
    echo "Bootstrap failed: remote repository is unavailable: $GITHUB_OWNER_VALUE/$repository" >&2
    echo "Review docs/GITHUB_BOOTSTRAP.md before authorized repository creation." >&2
    exit 1
  fi
  gh repo clone "$GITHUB_OWNER_VALUE/$repository" "$target"
  echo "Cloned repository: $repository"
done

if [[ "$CHECK_ONLY" == true && "$MISSING" -gt 0 ]]; then
  echo "Bootstrap check failed: $MISSING canonical repositories are missing." >&2
  exit 1
fi

"$PROJECT_ROOT/tools/check-workspace.sh" --require-repositories
echo "Workspace bootstrap completed."
