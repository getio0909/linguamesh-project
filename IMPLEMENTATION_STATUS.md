# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` multi-profile/session-onboarding, runtime-`ENOSPC` rollback, GIO Secret Service
adapter, runtime PO action-label slice, and generic completion desktop notification are
implemented, committed, published to the canonical public repositories owned by `getio0909`, and
verified by applicable local and GitHub Actions gates. The same real GTK flow passes under
X11/Xvfb and forced Wayland/headless Weston. The active Linux secure-provider checkpoint remains
incomplete because real desktop Secret Service credential lifecycle evidence and secure
persistent-credential onboarding are not complete. No stable product release, completed native
client, released SDK artifact, or supported document codec is claimed here.

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
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `07b89f36269155469a488ab830e8f485b3a1323b` starts disconnected, derives provider setup from authoritative state, manages multiple profiles with independent models, preserves authenticated A/B routing without credential crossover, exposes baseline GTK accessibility semantics, uses a GIO Secret Service adapter for persistent SecretRef values with fail-closed session fallback, loads pinned English/Simplified Chinese PO catalogs for runtime Translate/Stop labels, and emits generic completion notifications without source or translated content. Post-startup persistent Connect, model-update, and deletion `ENOSPC` failures reject before success, preserve the prior session, and restore only pre-fault state. Local suites passed 41 and 67 tests plus one exact fault test. Validation revision `07b89f36269155469a488ab830e8f485b3a1323b` passed Native Linux run `29594795691` (job `87932451631`) with both display gates, strict Clippy, storage-fault test, notification path, and the native build. Real desktop keyring CRUD, notification-server delivery, and complete UI gettext coverage remain unverified. |
| GitHub Actions | Passed | Notification validation run `29594795691` (job `87932451631`) and evidence-head run `29594948933` (job `87932966303`) passed the exact fault test, GTK assertions, both display gates, generic notification path, and the all-feature build; Foundation runs `29594795681` and `29594948857` also passed. Central integration commit `a964ac060c51665793ed455763137ee30bd22a26` passed coordination run `29594286528`, Linux job `87930776189`, and PowerShell job `87930776107`. |
| Non-functional repository heads | Passed | Core head `b8ce1fda3a2a20ea2bc99bb6abff70e1a7a95383` is a documentation-only descendant of the functional pin; Core run `29573340721` and Native SDK run `29573340735` passed. Linux evidence head `a7554e81c40b7d92d29a0eb8ab4fa22b1517648f` changes only evidence documentation relative to functional source `07b89f36269155469a488ab830e8f485b3a1323b`; foundation run `29594948857` and Native Linux run `29594948933` (job `87932966303`) passed. The release manifest intentionally pins functional revisions. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not passed | Scenarios 2–20 do not yet have complete reproducible passing evidence. Linux session onboarding and authenticated A/B next-request counters are partial Scenario 3/5 implementation evidence; they do not complete either scenario or the active secure-provider checkpoint. |

## Validation limitations

PowerShell validation was not executed locally because `pwsh` is unavailable on this Linux host;
central GitHub Actions run `29587437567` executed it successfully on Windows. Native GTK headers
and Weston are also unavailable locally; Linux run `29589332282` supplies the native compile, link,
X11/Xvfb, forced headless Wayland, D-Bus, GTK, accessibility, and controlled `ENOSPC` fault-test
evidence. Full
third-party JSON Schema
validation was not run locally because
the Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator
independently checked the manifest's required repository, component, version, status, source,
checksum, owner, and remote invariants. Real desktop Secret Service CRUD/cleanup, complete UI gettext
coverage, secure persistent-credential onboarding, notification-server delivery, database faults beyond the verified `ENOSPC` transaction boundary, packaging,
AT-SPI/Orca, physical-keyboard, physical-compositor and GPU-backed Wayland, a broader desktop matrix, and third-party
local-server interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until the real desktop
Secret Service-backed credential lifecycle, secure persistent-credential onboarding, compatible
stable components, checksummed artifacts, and all required acceptance evidence are recorded.
