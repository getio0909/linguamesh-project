# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` non-secret multi-profile slice are implemented, committed, published to the
canonical public repositories owned by `getio0909`, and verified by applicable local and GitHub
Actions gates. The active Linux secure-provider checkpoint remains incomplete because native
Secret Service credential create/read/update/delete and complete onboarding are not implemented.
No stable product release, completed native client, released SDK artifact, or supported document
codec is claimed here.

## Evidence

| Area | Status | Evidence |
| --- | --- | --- |
| Authoritative goal and plan | Present | `PROJECT_GOAL.md`, `AGENTS.md`, and `PLANS.md` were read before implementation. |
| Central policies and documentation | Validated locally | `bash tools/check-workspace.sh` passed required-file and Markdown-link checks. |
| Workspace and release manifests | Validated locally | Default and strict Bash checks parsed both TOML files, enforced the canonical set and release invariants, parsed the JSON schema, and passed. |
| Workspace automation | Bash validated | `bash -n tools/bootstrap.sh tools/check-workspace.sh` and `bash tools/bootstrap.sh --check-only` passed. The check-only run preserved all seven existing directories. |
| GitHub repositories | Published and verified | All seven repositories are public, use `main` as the default branch, have Issues and Actions enabled, have Wiki disabled, and initially matched their local committed HEAD. Canonical remotes are recorded in `workspace-manifest.toml`. |
| GitHub metadata | Validated | The repository Python 3.13 environment parsed all workflow and issue-template YAML files successfully; remote run evidence is listed below. |
| Canonical sibling repositories | Layout validated | `bash tools/check-workspace.sh --require-repositories` found all seven canonical directories and their minimum policy files. This does not verify sibling application behavior. |
| Rust core checkpoint | Validated locally and remotely | Functional revision `fbf3e9b5927049dccaa19f8c36013495ffebba12` uses Core `0.1.0-alpha.2`, ABI 1, and protocol 1. It passed rustfmt, strict Clippy, 57 tests, locked build, cargo-deny policy, native SDK checks, credential scans, and CI. Canonical profiles, SQLite schema 2 migration, the bounded typed host-secret broker, and Linux default-VFS SQLite no-follow protection are implemented without credential-value persistence. |
| Localization bundle | Validated locally and remotely | l10n revision `4b36889116eba037721cb31827342409e8836168` contains 41 canonical messages, 12 official locale packs, two pseudo-locales, 45 generated artifacts, 25 passing tests, platform-format checks, and deterministic bundle SHA-256 `47bc84bd7562fb6ada7f88fd07490e79843c5c4e9d9b747f87a206dbecd0394a`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `c88d37a5de2f03c2ae5d2940c4d25e5d998c301d` starts disconnected, requires explicit connection and model selection, resolves isolated one-shot session secrets, and manages multiple credential-free profiles with exact stable IDs in private XDG Core storage. It restores the full list/default without network access, keeps browsing separate from activation, preserves per-profile models, and supports create/update/switch/delete while a deleted connected row continues as session-only. Local suites passed 38 and 62 tests. Native run `29577918335` (job `87876528763`) passed 62 library tests, the real GTK multi-profile test, strict all-feature Clippy, and the all-target build under D-Bus/Xvfb. Persistent secrets still fail closed. |
| GitHub Actions | Passed | Core run `29572377637` (Rust job `87858924329`) and Native SDK run `29572377631` (Linux job `87858924315`) passed for the functional Core source. Linux foundation run `29577918346` and Native Linux run `29577918335` (job `87876528763`) passed for the functional multi-profile client source. Central revision `f2c3a5532fed81ebe056c0d6de33d81b404b15cf` passed integration run `29578424525`, Linux job `87878121729`, and PowerShell job `87878121792`; prior repository and localization evidence remains recorded in component status files. |
| Documentation-only repository heads | Passed | Core head `b8ce1fda3a2a20ea2bc99bb6abff70e1a7a95383` is a documentation-only descendant of the functional pin; Core run `29573340721` and Native SDK run `29573340735` passed. Linux head `7ba8909bd05a168e328af027e1308d23f257f0f9` changes only implementation/testing/release evidence from the functional pin; foundation run `29578055430` and Native Linux run `29578055393` (job `87876964652`) passed. The release manifest intentionally pins functional revisions. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not passed | Scenarios 2–20 do not yet have complete reproducible passing evidence. The Linux multi-profile slice is partial implementation evidence and does not complete Scenario 3, Scenario 5, or the active secure-provider checkpoint. |

## Validation limitations

PowerShell validation was not executed locally because `pwsh` is unavailable on this Linux host;
central GitHub Actions run `29578424525` executed it successfully on Windows. Native GTK headers
are also unavailable locally; Linux run `29577918335` supplies the native compile, link, X11,
D-Bus, and GTK test evidence. Full third-party JSON Schema validation was not run locally because
the Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator
independently checked the manifest's required repository, component, version, status, source,
checksum, owner, and remote invariants. Native Secret Service, complete onboarding, runtime
database I/O fault injection, packaging, accessibility, Wayland, and third-party local-server
interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until the native
Secret Service-backed credential lifecycle, complete onboarding, compatible stable components,
checksummed artifacts, and all required acceptance evidence are recorded.
