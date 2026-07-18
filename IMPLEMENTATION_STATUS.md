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
Core now protects common structured spans across streamed translation, and Linux negotiates that
contract before provider work begins. The current Linux slice also carries a bounded request-level
glossary through Core, protects matching terms before provider calls, and restores required target
terms or immutable names without persistence.
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
| Rust core checkpoint | Validated locally and remotely | Functional revision `3f96de03eb4ff04add09473fc1473c2c49d67a51` uses Core `0.1.0-alpha.2`, ABI 1, protocol 1, `protected_spans_v1`, and bounded request-level glossary protection; it passed rustfmt, strict Clippy, full workspace tests, locked build, cargo-deny policy, native SDK checks, and Native SDK run `29633431920`. Test-only descendant `da83df8effa9611e496e1c288e6a1f08e1560d2c` passed CI run `29633611719` and Native SDK run `29633611665` (Linux job `88051859910`; Windows `88051859876`; Apple `88051859877`; Android `88051859887`). Canonical profiles, SQLite schema 2 migration, the bounded typed host-secret broker, Linux default-VFS SQLite no-follow protection, streamed protected-span restoration, and glossary validation without credential-value persistence are implemented. |
| Localization bundle | Validated locally and remotely | l10n evidence revision `2e5e3033f453aa2882cf71217f9514dce8501269` contains 211 canonical messages, including Linux-only status, partial-output, text-import/export, provider-profile, source-target, onboarding-stage, active-provider, notification, draft-note, locale selector language names, fixed provider/file/worker errors, reducer-state/category guidance, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, and Core/loopback startup plus profile-storage error copy, 12 official locale packs, two pseudo-locales, 59 generated artifacts including paired Linux PO/MO resources, 26 passing tests, platform-format checks, and deterministic bundle ZIP SHA-256 `116a9cdedd8b0a3d31171b365969b745681e50257e183b40aa2c37c77f1e6d91`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `3affedb1cc95d9ec57823459f7cf8c91f3eb16bb` negotiates Core `protected_spans_v1`, carries bounded request-level glossary rules into translation requests, starts disconnected, derives provider setup from authoritative state, manages multiple profiles with independent models, preserves authenticated A/B routing without credential crossover, exposes baseline GTK accessibility semantics, uses a GIO Secret Service adapter with a corrected single-layer plain-string OpenSession Variant plus isolated real-daemon CRUD/cleanup, persistent daemon-restart restoration, locked-item fail-closed verification, secure persistent-credential onboarding, a no-credential OpenAI-compatible loopback path, and session fallback, exposes twelve official Linux PO/MO packs with runtime action-label, workspace-widget, active-provider, active-provider transition/mode, status summary/partial-output, text-file import/export, provider-profile, source/target language, locale selector language names, onboarding-stage, draft-note, fixed provider/file/worker and reducer-state/category error messages, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, Core/loopback startup and profile-storage error copy, and theme-option switching plus Arabic RTL root direction, preserves the source editor buffer across a Simplified Chinese-to-Arabic locale switch, emits generic completion notifications without source or translated content, imports bounded UTF-8 TXT/Markdown through GTK FileDialog/GIO or single-file source-editor drag-and-drop, and asynchronously exports UTF-8 translated output with source-file overwrite protection. Post-startup persistent Connect, model-update, and deletion `ENOSPC` failures reject before success, preserve the prior session, and restore only pre-fault state. Local suites passed 53 portable tests and 80 demo-provider tests with one controlled ignore; source-level GUI checks passed locally while the binary GUI test is CI-only on this host. Native run `29633550137` (job `88051695699`), Foundation run `29633550177` (job `88051695826`), and Flatpak run `29633550134` (job `88051695714`) passed. |
| Linux Flatpak packaging scaffold | GNOME 49 SDK build and bounded sandbox startup validated | Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` publishes the pinned GNOME 49 manifest, immutable Core/Linux source pins, generated Cargo archive hashes, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; latest `Flatpak Linux` run `29625778180` (job `88029765322`) is the current remote packaging gate. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | l10n revision `2e5e3033f453aa2882cf71217f9514dce8501269` passed Localization run `29633267666` and Foundation run `29633267674`; Core functional revision `3f96de03eb4ff04add09473fc1473c2c49d67a51` passed Native SDK run `29633431920`; test-only descendant `da83df8effa9611e496e1c288e6a1f08e1560d2c` passed CI run `29633611719` and Native SDK run `29633611665`. Linux revision `3affedb1cc95d9ec57823459f7cf8c91f3eb16bb` passed Native run `29633550137` (job `88051695699`), Foundation run `29633550177` (job `88051695826`), and Flatpak run `29633550134` (job `88051695714`). |
| Non-functional repository heads | Passed | Core head `da83df8effa9611e496e1c288e6a1f08e1560d2c` is a test-only descendant of functional pin `3f96de03eb4ff04add09473fc1473c2c49d67a51`; its CI and Native SDK gates passed. Linux revision `3affedb1cc95d9ec57823459f7cf8c91f3eb16bb` is the published compatibility/docs head over the reviewed Core pin; latest Native, Foundation, and Flatpak gates passed. The release manifest intentionally pins functional revisions and lists no release artifact. |
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
