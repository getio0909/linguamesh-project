# Repository Guidelines

## Project Structure & Module Organization

This is LinguaMesh's central coordination repository, not an application source repository. `PROJECT_GOAL.md` is the authoritative product, architecture, security, and release specification. Keep cross-repository material here: architecture notes in `docs/architecture/`, decisions in `docs/adr/`, proposals in `docs/rfc/`, release records in `docs/releases/`, and workspace automation in `tools/` as those paths are introduced. Product code belongs in sibling repositories such as `linguamesh-core`, `linguamesh-android`, `linguamesh-windows`, `linguamesh-macos`, `linguamesh-linux`, and `linguamesh-l10n`.

## Build, Test, and Development Commands

No build system or test runner exists in this repository yet. Do not claim validation from planned scripts. After Git is initialized, inspect documentation patches and whitespace with:

```sh
git diff --check
git diff -- PROJECT_GOAL.md docs/
```

When implemented, use `tools/bootstrap.sh` (or `tools/bootstrap.ps1`) to prepare sibling repositories and `tools/check-workspace.sh` (or `.ps1`) to validate manifests, compatibility, links, and release metadata. Record the exact commands and results in the pull request.

## Coding Style & Naming Conventions

Write concise Markdown with descriptive headings and relative links. Use uppercase names for top-level policy files (`SECURITY.md`) and lowercase directories. Name ADRs with a zero-padded sequence and short kebab-case summary, for example `docs/adr/0001-core-abi.md`. Keep TOML deterministic and easy to review. Shell scripts should use `set -euo pipefail`, quote expansions, and have equivalent PowerShell behavior when they are cross-platform workspace tools.

## Testing Guidelines

Project-repository checks must cover workspace and release manifests, the known repository set, global-goal revisions, compatibility data, documentation links, checksums, and cross-repository status. Add focused fixtures for manifest validation and name shell checks `check-*.sh`. Tests requiring paid provider credentials do not belong in default CI.

## Commit & Pull Request Guidelines

There is no local Git history from which to infer a convention. Until one is documented, use short imperative subjects with an optional scope, such as `docs: clarify release compatibility`. Pull requests should explain scope, affected sibling repositories, compatibility or rollback impact, linked issues or ADRs, and all validation run. Include screenshots only for user-visible documentation or client changes.

## Security & Configuration

Never commit API keys, tokens, translation content, or production credentials. Keep local integration credentials in environment variables, including settings referenced by `.codex/config.toml`. Redact diagnostics and treat provider, document, locale, and model output as untrusted input.

# LinguaMesh Project Instructions

## Authoritative specification

Read `PROJECT_GOAL.md` completely before performing project work.

`PROJECT_GOAL.md` defines the global architecture, repository topology,
security requirements, delivery milestones, acceptance scenarios, and
completion conditions.

## Repository role

This repository coordinates all LinguaMesh repositories, architecture,
compatibility, roadmaps, release manifests, and cross-repository work.

## Required workflow

1. Inspect Git status and preserve existing user changes.
2. Read `PROJECT_GOAL.md`.
3. Read or update `PLANS.md` for multi-stage work.
4. Record assumptions using `Assumption:`.
5. Implement the smallest complete vertical slice.
6. Run all relevant validation commands.
7. Update `IMPLEMENTATION_STATUS.md` with actual evidence.
8. Keep `workspace-manifest.toml` and `release-manifest.toml` consistent.

## GitHub authorization

Normal creation, initialization, commit, and push operations for the
canonical LinguaMesh repositories are permitted when an active Goal
explicitly authorizes them.

Never delete repositories, force-push, rewrite published history, expose
credentials, or publish an unverified stable release.

## Git safety

Never use destructive Git cleanup or history-rewriting commands without
separate explicit authorization.

Do not discard unrelated user changes.

## Communication

All code comments must be in Simplified Chinese and placed on separate
lines above the code they describe.

All console, log, diagnostic, and command-line output strings must be in
English.

## Definition of done

Do not claim completion without implementation, tests, documentation,
compatibility records, and reproducible evidence.
