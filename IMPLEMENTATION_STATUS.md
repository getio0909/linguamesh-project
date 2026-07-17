# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` multi-profile/session-onboarding, runtime-`ENOSPC` rollback, GIO Secret Service
adapter, runtime PO action-label slice, generic completion desktop notification, and bounded
native text-file import are
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
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `b0da3819d97ae24f8c85147da5e7e1c65fe2d6fc` starts disconnected, derives provider setup from authoritative state, manages multiple profiles with independent models, preserves authenticated A/B routing without credential crossover, exposes baseline GTK accessibility semantics, uses a GIO Secret Service adapter for persistent SecretRef values with fail-closed session fallback, loads pinned English/Simplified Chinese PO catalogs for runtime Translate/Stop labels, emits generic completion notifications without source or translated content, and imports bounded UTF-8 TXT/Markdown text through GTK FileDialog/GIO or single-file source-editor drag-and-drop. Post-startup persistent Connect, model-update, and deletion `ENOSPC` failures reject before success, preserve the prior session, and restore only pre-fault state. Local suites passed 44 and 70 tests plus one exact fault test. Validation revision `b0da3819d97ae24f8c85147da5e7e1c65fe2d6fc` passed Native Linux run `29597016894` (job `87939785693`) with both display gates, strict Clippy, storage-fault test, text-import and DropTarget assertions, and the native build. Real desktop keyring CRUD, notification-server delivery, interactive portal leases, and complete UI gettext coverage remain unverified. |
| GitHub Actions | Passed | Drag-and-drop validation run `29597016894` (job `87939785693`) and evidence-head run `29597182692` (job `87940328074`) passed the exact fault test, GTK assertions, both display gates, bounded import path, and the all-feature build; Foundation runs `29597016893` and `29597182729` also passed. Central integration commit `18fc69e0eea5431bf82c767b8d90ce48fef38d01` passed coordination run `29597565696`, Linux job `87941565049`, and PowerShell job `87941565102`. |
| Non-functional repository heads | Passed | Core head `b8ce1fda3a2a20ea2bc99bb6abff70e1a7a95383` is a documentation-only descendant of the functional pin; Core run `29573340721` and Native SDK run `29573340735` passed. Linux evidence head `cdc711320c284eae1f1376635e0d84234d8863a1` changes only evidence documentation relative to functional source `b0da3819d97ae24f8c85147da5e7e1c65fe2d6fc`; foundation run `29597182729` and Native Linux run `29597182692` (job `87940328074`) passed. The release manifest intentionally pins functional revisions. |
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
coverage, secure persistent-credential onboarding, notification-server delivery, interactive portal leases, drag-and-drop, database faults beyond the verified `ENOSPC` transaction boundary, packaging,
AT-SPI/Orca, physical-keyboard, physical-compositor and GPU-backed Wayland, a broader desktop matrix, and third-party
local-server interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until the real desktop
Secret Service-backed credential lifecycle, secure persistent-credential onboarding, compatible
stable components, checksummed artifacts, and all required acceptance evidence are recorded.
