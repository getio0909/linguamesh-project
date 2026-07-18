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
contract before provider work begins.
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
| Rust core checkpoint | Validated locally and remotely | Functional revision `031b20cd6f4ddc7635057d1b2d949db4ac7d1f39` uses Core `0.1.0-alpha.2`, ABI 1, protocol 1, and `protected_spans_v1`; it passed rustfmt, strict Clippy, 60 tests, locked build, cargo-deny policy, native SDK checks, credential scans, and CI run `29632565728`. Core head `c1406eb60c56cc4bebdf130f0cc6ee6602046c83` also passed Native SDK run `29632565726`; its delta is test-only HTTP header robustness. Canonical profiles, SQLite schema 2 migration, the bounded typed host-secret broker, Linux default-VFS SQLite no-follow protection, and streamed protected-span restoration are implemented without credential-value persistence. |
| Localization bundle | Validated locally and remotely | l10n evidence revision `dc9a9d48a38dfeb8f6b2020417960023678d8252` contains 208 canonical messages, including Linux-only status, partial-output, text-import/export, provider-profile, source-target, onboarding-stage, active-provider, notification, draft-note, locale selector language names, fixed provider/file/worker errors, reducer-state/category guidance, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control copy, and Core/loopback startup plus profile-storage error copy, 12 official locale packs, two pseudo-locales, 59 generated artifacts including paired Linux PO/MO resources, 26 passing tests, platform-format checks, and deterministic bundle ZIP SHA-256 `a8c5535b23eb27f02ff5fd3bb4c4c1c6948718f1233321305c173b1741b27e6f`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `79de8d9e01bebdb4be666ef7a1aed6309ef25970` negotiates Core `protected_spans_v1`, starts disconnected, derives provider setup from authoritative state, manages multiple profiles with independent models, preserves authenticated A/B routing without credential crossover, exposes baseline GTK accessibility semantics, uses a GIO Secret Service adapter with a corrected single-layer plain-string OpenSession Variant plus isolated real-daemon CRUD/cleanup, persistent daemon-restart restoration, locked-item fail-closed verification, secure persistent-credential onboarding, a no-credential OpenAI-compatible loopback path, and session fallback, exposes twelve official Linux PO/MO packs with runtime action-label, workspace-widget, active-provider, active-provider transition/mode, status summary/partial-output, text-file import/export, provider-profile, source/target language, locale selector language names, onboarding-stage, draft-note, fixed provider/file/worker and reducer-state/category error messages, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control copy, Core/loopback startup and profile-storage error copy, and theme-option switching plus Arabic RTL root direction, preserves the source editor buffer across a Simplified Chinese-to-Arabic locale switch, emits generic completion notifications without source or translated content, imports bounded UTF-8 TXT/Markdown through GTK FileDialog/GIO or single-file source-editor drag-and-drop, and asynchronously exports UTF-8 translated output with source-file overwrite protection. Post-startup persistent Connect, model-update, and deletion `ENOSPC` failures reject before success, preserve the prior session, and restore only pre-fault state. Local suites passed 52 portable tests and 5 localization tests; source-level GUI checks passed locally while the binary GUI test is CI-only on this host. Native run `29632530497` (job `88048916214`), Foundation run `29632530524` (job `88048916265`), and Flatpak run `29632530485` (job `88048916150`) passed; the native gate includes GTK locale/widget/theme/status/text-import/export/construction-stage/provider-profile/source-target/locale-name/onboarding-stage/active-provider/notification/error assertions, source-buffer preservation, runtime MO lookup, PO/MO syntax/readability checks, real GTK locale/RTL code, Secret Service prompted-flow store/delete rejection, real portal backend, application FileDialog, source-editor URI-list drag/drop, dunst delivery, and visible viewable Dunst desktop-shell window fixtures. End-user prompt approval, complete visible-string gettext coverage, physical compositor/GPU rendering, and signing/distributable release remain unverified. |
| Linux Flatpak packaging scaffold | GNOME 49 SDK build and bounded sandbox startup validated | Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` publishes the pinned GNOME 49 manifest, immutable Core/Linux source pins, generated Cargo archive hashes, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; latest `Flatpak Linux` run `29625778180` (job `88029765322`) is the current remote packaging gate. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | l10n revision `dc9a9d48a38dfeb8f6b2020417960023678d8252` passed Localization run `29631551712` and Foundation run `29631551720`. Core functional revision `031b20cd6f4ddc7635057d1b2d949db4ac7d1f39` passed Native SDK run `29632398136`; Core head `c1406eb60c56cc4bebdf130f0cc6ee6602046c83` passed CI run `29632565728` and Native SDK run `29632565726`. Linux revision `79de8d9e01bebdb4be666ef7a1aed6309ef25970` passed Native run `29632530497` (job `88048916214`), Foundation run `29632530524` (job `88048916265`), and Flatpak run `29632530485` (job `88048916150`). Central coordination revision `30cb91557d96fbff82bea242ae8a9a722f93f9eb` passed run `29632016228` with Linux job `88047478552` and PowerShell job `88047478559`; protected-span integration revision `a662fd53209730d552bc3c2869b7a5f98e537023` passed run `29632758636` with Linux job `88049553494` and PowerShell job `88049553476`. |
| Non-functional repository heads | Passed | Core head `c1406eb60c56cc4bebdf130f0cc6ee6602046c83` is a test-only descendant of functional pin `031b20cd6f4ddc7635057d1b2d949db4ac7d1f39`; its CI and Native SDK gates passed. Linux revision `79de8d9e01bebdb4be666ef7a1aed6309ef25970` is the published compatibility/docs head over the reviewed Core pin; latest Native, Foundation, and Flatpak gates are recorded above. The release manifest intentionally pins functional revisions and lists no release artifact. |
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
