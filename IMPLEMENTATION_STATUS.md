# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` non-secret profile persistence/restart slice are implemented, committed, published
to the canonical public repositories owned by `getio0909`, and verified by applicable local and
GitHub Actions gates. The active Linux secure-provider checkpoint remains incomplete because native
Secret Service credential create/read/update/delete, onboarding, and active switching among
multiple saved profiles are not implemented. No stable product release, completed native client,
released SDK artifact, or supported document codec is claimed here.

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
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `c58a54c2479045773358bd9c456b45a958e98e1e` starts disconnected, requires explicit connection and model selection, resolves one-shot session secrets, and persists one credential-free profile/model preference in private XDG Core storage. Restart restores the form without network access or auto-connect; credentials require re-entry. Local suites passed 29 and 50 tests, including secret-canary scans, unsafe-path rejection, session fallback, and persistence rollback. Native Ubuntu CI passed 50 library tests, the real GTK test, strict all-feature Clippy, and the all-target build under D-Bus/Xvfb. Persistent secrets still fail closed. |
| GitHub Actions | Passed | Core run `29572377637` (Rust job `87858924329`) and Native SDK run `29572377631` (Linux job `87858924315`) passed for the functional Core source. Linux foundation run `29574265553` (job `87865028745`) and Native Linux run `29574265570` (job `87865028892`) passed for the functional client source. Central runs `29551747796` and `29552361617` passed Linux and Windows validation; prior repository and localization evidence remains recorded in component status files. |
| Documentation-only repository heads | Passed | Core head `b8ce1fda3a2a20ea2bc99bb6abff70e1a7a95383` is a documentation-only descendant of the functional pin; Core run `29573340721` and Native SDK run `29573340735` passed. Linux head `90977fdd019b14f151ee3aef56af81eb238a41b3` changes only implementation/testing/release evidence from the functional pin; foundation run `29574386265` (job `87865409337`) and Native Linux run `29574386318` (job `87865409285`) passed. The release manifest intentionally pins functional revisions. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not passed | Scenarios 2–20 do not yet have complete reproducible passing evidence. The Linux alpha.2 slice is partial implementation evidence and does not complete Scenario 3 or the secure-provider checkpoint. |

## Validation limitations

PowerShell validation was not executed locally because `pwsh` is unavailable on this Linux host;
central GitHub Actions run `29551747796` executed it successfully on Windows. Native GTK headers
are also unavailable locally; Linux run `29574265570` supplies the native compile, link, X11,
D-Bus, and GTK test evidence. Full third-party JSON Schema validation was not run locally because
the Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator
independently checked the manifest's required repository, component, version, status, source,
checksum, owner, and remote invariants. Native Secret Service, multiple saved-profile lifecycle,
runtime database I/O fault injection, packaging, accessibility, Wayland, and third-party
local-server interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until the native
Secret Service-backed credential lifecycle, multiple-profile management, compatible stable
components, checksummed artifacts, and all required acceptance evidence are recorded.
