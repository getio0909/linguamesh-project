# Implementation Status

Last updated: 2026-07-18

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` multi-profile/session-onboarding, runtime-`ENOSPC` rollback, GIO Secret Service
adapter, runtime official Linux locale-pack switching with Arabic RTL direction, generic completion
desktop notification, bounded
native text-file import, private notification-service transport validation, headless real
notification-daemon delivery, a real XDG document-portal lease lifecycle fixture, a real
interactive portal FileChooser backend fixture, application-level GTK FileDialog callback
verification, and a real GTK source-editor drag/drop gesture fixture are
implemented, committed, published to the canonical public repositories owned by `getio0909`, and
verified by applicable local and GitHub Actions gates. The same real GTK flow passes under
X11/Xvfb and forced Wayland/headless Weston. The active Linux secure-provider checkpoint is complete;
prompted store/delete flows now have a separately verified fail-closed boundary, while end-user
prompt approval remains open. A pinned Linux
Flatpak manifest now has a remotely verified GNOME 49 SDK build, prerelease CI bundle, and bounded
sandbox startup smoke; X11 desktop-shell notification rendering is now verified, while physical
compositor/GPU rendering and release artifacts remain open. No stable product
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
| Localization bundle | Validated locally and remotely | l10n revision `14a4d6bcd556d735dee2d7ed022650fbcc8593b8` contains 57 canonical messages, including Linux-only status, partial-output, and text-import controls, 12 official locale packs, two pseudo-locales, 50 generated artifacts, 25 passing tests, platform-format checks, and deterministic bundle SHA-256 `40655730a4d07d522901e3b9ac0a76978d3208d379bad0bf219623ac3a04ae06`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `7d7eba9960b657f0460fb0daaaaebaaa609f39b1` starts disconnected, derives provider setup from authoritative state, manages multiple profiles with independent models, preserves authenticated A/B routing without credential crossover, exposes baseline GTK accessibility semantics, uses a GIO Secret Service adapter with a corrected single-layer plain-string OpenSession Variant plus isolated real-daemon CRUD/cleanup, persistent daemon-restart restoration, locked-item fail-closed verification, secure persistent-credential onboarding, a no-credential OpenAI-compatible loopback path, and session fallback, exposes twelve official Linux PO packs with runtime action-label, workspace-widget, active-provider, status summary/partial-output, text-file import, and theme-option switching plus Arabic RTL root direction, preserves the source editor buffer across a Simplified Chinese-to-Arabic locale switch, emits generic completion notifications without source or translated content, and imports bounded UTF-8 TXT/Markdown text through GTK FileDialog/GIO or single-file source-editor drag-and-drop. Post-startup persistent Connect, model-update, and deletion `ENOSPC` failures reject before success, preserve the prior session, and restore only pre-fault state. Local suites passed 45 portable tests, 4 localization tests, and one exact fault test. Evidence head `d563bc28ef6a08fd90c7a4eba3bf71ae8b07d57b` passed Native Linux run `29625054878` (job `88027678296`), Foundation run `29625054875`, and Flatpak run `29625054911` (job `88027678198`); the native gate includes GTK locale/widget/theme/status/text-import assertions, source-buffer preservation, real GTK locale/RTL code, Secret Service prompted-flow store/delete rejection, real portal backend, application FileDialog, source-editor URI-list drag/drop, dunst delivery, and visible viewable Dunst desktop-shell window fixtures. End-user prompt approval, physical compositor/GPU rendering, and complete visible-string gettext coverage remain unverified. |
| Linux Flatpak packaging scaffold | GNOME 49 SDK build and bounded sandbox startup validated | Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` publishes the pinned GNOME 49 manifest, immutable Core/Linux source pins, generated Cargo archive hashes, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; latest `Flatpak Linux` run `29625054911` (job `88027678198`) is the current remote packaging gate. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | Linux functional run `29604269568` (job `87963611054`) and foundation run `29604269516` passed the exact fault test, persistent Secret Service lifecycle and secure-onboarding fixtures, no-credential loopback regression, GTK assertions, both display gates, bounded import path, and the all-feature build. Linux evidence head `d563bc28ef6a08fd90c7a4eba3bf71ae8b07d57b` passed Native Linux run `29625054878` (job `88027678296`), Foundation run `29625054875`, and Flatpak run `29625054911` (job `88027678198`); the native job also verified the pinned 57-message localization snapshot, Arabic RTL direction, source-buffer preservation, localized workspace widgets, active-provider/status-summary/partial-output/text-import/theme-option localization, prompted-flow store/delete rejection, real portal backend, application FileDialog callback, source-editor drag/drop gesture, dunst delivery, and visible viewable Dunst window. Central integration commit `79bf11e` passed coordination run `29625308528` with Linux job `88028407855` and PowerShell job `88028407843`. The first status-localization attempt `4d3cfdb` failed before tests because the workflow still checked out the old l10n pin; `edb9cd2` corrected that pin. |
| Non-functional repository heads | Passed | Core head `b8ce1fda3a2a20ea2bc99bb6abff70e1a7a95383` is a documentation-only descendant of the functional pin; Core run `29573340721` and Native SDK run `29573340735` passed. Linux evidence head `d563bc28ef6a08fd90c7a4eba3bf71ae8b07d57b` adds status-summary/partial-output/text-import localization relative to functional source `7d7eba9960b657f0460fb0daaaaebaaa609f39b1`; latest Native, Foundation, and Flatpak gates are recorded above. The release manifest intentionally pins functional revisions and lists no release artifact. |
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
checksum, owner, and remote invariants. End-user prompted Secret Service approval, complete UI gettext
coverage, physical desktop compositor/GPU rendering,
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
