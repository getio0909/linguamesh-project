# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` multi-profile/session-onboarding, runtime-`ENOSPC` rollback, GIO Secret Service
adapter, runtime PO action-label slice, generic completion desktop notification, bounded
native text-file import, and private notification-service transport validation are
implemented, committed, published to the canonical public repositories owned by `getio0909`, and
verified by applicable local and GitHub Actions gates. The same real GTK flow passes under
X11/Xvfb and forced Wayland/headless Weston. The active Linux secure-provider checkpoint is complete;
prompted interactive flows remain a separately documented fail-closed boundary. A pinned Linux
Flatpak manifest now has a remotely verified GNOME 49 SDK build, prerelease CI bundle, and bounded
sandbox startup smoke; portal leases, desktop-shell notification delivery, and release artifacts remain open. No stable product
release, completed native
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
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `7d7eba9960b657f0460fb0daaaaebaaa609f39b1` starts disconnected, derives provider setup from authoritative state, manages multiple profiles with independent models, preserves authenticated A/B routing without credential crossover, exposes baseline GTK accessibility semantics, uses a GIO Secret Service adapter with a corrected single-layer plain-string OpenSession Variant plus isolated real-daemon CRUD/cleanup, persistent daemon-restart restoration, locked-item fail-closed verification, secure persistent-credential onboarding, a no-credential OpenAI-compatible loopback path, and session fallback, loads pinned English/Simplified Chinese PO catalogs for runtime Translate/Stop labels, emits generic completion notifications without source or translated content, and imports bounded UTF-8 TXT/Markdown text through GTK FileDialog/GIO or single-file source-editor drag-and-drop. Post-startup persistent Connect, model-update, and deletion `ENOSPC` failures reject before success, preserve the prior session, and restore only pre-fault state. Local suites passed 44 and 71 tests plus one exact fault test. Evidence head `ae44102ae90f70d543c001869557a8965dba2074` passed Foundation run `29610044117` (job `87982316925`) and Native Linux run `29610044120` (job `87982316767`), including the private `org.freedesktop.Notifications` service transport fixture that verifies fixed generic title/body text without source or translated content. Prompted interactive flows, desktop-shell notification rendering, interactive portal leases, and complete UI gettext coverage remain unverified. |
| Linux Flatpak packaging scaffold | GNOME 49 SDK build and bounded sandbox startup validated | Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` publishes the pinned GNOME 49 manifest, immutable Core/Linux source pins, generated Cargo archive hashes, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; `Flatpak Linux` run `29608245156` (job `87976563401`) built `linguamesh-linux-x86_64-x86_64.flatpak`, uploaded artifact `8417803048` (2,395,628 bytes), installed it under Xvfb/private D-Bus, confirmed runtime `org.gnome.Platform/x86_64/49`, and passed the bounded startup smoke. Portal leases, desktop-shell notification delivery, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | Linux functional run `29604269568` (job `87963611054`) and foundation run `29604269516` passed the exact fault test, persistent Secret Service lifecycle and secure-onboarding fixtures, no-credential loopback regression, GTK assertions, both display gates, bounded import path, and the all-feature build. Linux notification transport evidence head `ae44102` passed Native Linux run `29610044120` (job `87982316767`) and Foundation run `29610044117` (job `87982316925`); the same head's Flatpak run `29610044088` built and smoke-tested the GNOME 49 bundle. The GNOME 49 packaging revision `fd1f400` passed `Flatpak Linux` run `29608245156` with job `87976563401`, including the sandbox startup smoke. Central integration commit `a7ca1f84eef3f98647a4383dc931c11049171b63` passed coordination run `29604649153` with Linux job `87964871597` and PowerShell job `87964871588`; the packaging documentation checkpoint passed coordination run `29605424763` with Linux job `87967368496` and PowerShell job `87967368478`; the current notification-evidence sync commit `5ea07eb` passed coordination run `29610616057` with Linux job `87984136976` and PowerShell job `87984136992`. |
| Non-functional repository heads | Passed | Core head `b8ce1fda3a2a20ea2bc99bb6abff70e1a7a95383` is a documentation-only descendant of the functional pin; Core run `29573340721` and Native SDK run `29573340735` passed. Linux evidence head `a255b039ce37bcb2b362cfeb3d34a6283ed2aad5` changes only evidence documentation relative to functional source `7d7eba9960b657f0460fb0daaaaebaaa609f39b1`; foundation run `29604459891` and Native Linux run `29604459967` (job `87964249312`) passed. Packaging revision `fd1f400` passed the GNOME 49 SDK build and bounded sandbox startup smoke; the release manifest intentionally pins functional revisions and lists no release artifact. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not passed | Scenarios 2–20 do not yet have complete cross-platform reproducible passing evidence. Linux now has complete secure-provider Scenario 3 implementation evidence and partial Scenario 5 evidence; the global scenarios and stable-release evidence remain incomplete. |

## Validation limitations

PowerShell validation was not executed locally because `pwsh` is unavailable on this Linux host;
central GitHub Actions run `29587437567` executed it successfully on Windows. Native GTK headers
and Weston are also unavailable locally; Linux run `29589332282` supplies the native compile, link,
X11/Xvfb, forced headless Wayland, D-Bus, GTK, accessibility, persistent Secret Service lifecycle,
and controlled `ENOSPC` fault-test
evidence. Full
third-party JSON Schema
validation was not run locally because
the Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator
independently checked the manifest's required repository, component, version, status, source,
checksum, owner, and remote invariants. Prompted Secret Service interaction, complete UI gettext
coverage, desktop-shell notification rendering, interactive portal leases,
database faults beyond the verified `ENOSPC` transaction boundary,
release signing and distributable artifacts, AT-SPI/Orca,
physical-keyboard, physical-compositor and GPU-backed Wayland, a broader desktop matrix, and third-party
local-server interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until prompted desktop
Secret Service interaction, compatible
stable components, checksummed artifacts, and all required acceptance evidence are recorded.
