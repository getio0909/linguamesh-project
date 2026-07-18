# Implementation Status

Last updated: 2026-07-18

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` multi-profile/session-onboarding, runtime-`ENOSPC` rollback, GIO Secret Service
adapter, runtime official Linux locale-pack switching with Arabic RTL direction, generic completion
desktop notification, bounded
native text-file import, bounded Linux glossary CSV import/export, private notification-service transport validation, headless real
notification-daemon delivery, a real XDG document-portal lease lifecycle fixture, a real
interactive portal FileChooser backend fixture, application-level GTK FileDialog callback
verification, and a real GTK source-editor drag/drop gesture fixture are
implemented, committed, published to the canonical public repositories owned by `getio0909`, and
verified by applicable local and GitHub Actions gates. The same real GTK flow passes under
X11/Xvfb and forced Wayland/headless Weston. The active Linux secure-provider checkpoint is complete;
Core now protects common structured spans across streamed translation, and Linux negotiates that
contract before provider work begins. Core now also provides bounded semantic long-text chunking with
ordered sequential streaming and cancellation propagation; the current Linux slice negotiates that
feature and carries a bounded request-level glossary through Core, protects matching terms before
provider calls, and restores required target terms or immutable names without persistence. Linux
also imports and exports a fixed-schema UTF-8 glossary CSV through native GTK dialogs with Core-
enforced 4 MiB and 256-row bounds. The Linux workspace now exposes an explicit Incognito toggle that
carries `TranslationPrivacyMode::Incognito` into the next Core request. Core schema 3 and the Linux
worker persist completed standard translations in bounded history (100 entries, 4 MiB source/output
limit), restore only the count at startup, and expose a localized clear-all action; Incognito
completions skip history writes. The latest Linux history-policy slice adds a persisted enable/disable
toggle that preserves existing rows while blocking future standard writes, alongside bounded
inspection, exact per-entry deletion, and deterministic escaped UTF-8 TSV export. Core schema 5 and
the Linux worker now add optional bounded translation memory with versioned request identity,
Incognito bypass, persisted policy, cache reuse, inspection, export, exact deletion, and clear-all.
prompted store/delete flows now have a separately verified fail-closed boundary, while end-user
prompt approval remains open. A pinned Linux
Flatpak manifest now has a remotely verified GNOME 49 SDK build, prerelease CI bundle, and bounded
sandbox startup smoke; X11 desktop-shell notification rendering is now verified, while physical
compositor/GPU rendering and release artifacts remain open. No stable product
release, completed native
client, released SDK artifact, or supported document codec is claimed here.

## 2026-07-18 — Linux translation memory checkpoint

Assumption: translation-memory identity is versioned JSON over normalized source text, locale pair,
request limits, glossary/protected-span policy, prompt-template and quality versions, and confirmed
provider identity/model; Incognito requests never read or write the cache.

- Core `b5fb19cf2123b70587775cd6e4a68515a5790575` adds schema 5 bounded translation-memory storage,
  persisted enable/disable policy, deterministic identity matching, cache lookup/write, bounded
  listing, exact deletion, and clear-all. Local rustfmt, strict Clippy, offline build, full tests,
  and diff checks passed; CI `29640169852` and Native SDK `29640169834` passed.
- l10n `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995` adds Linux Save/View/Export/Delete/Clear memory
  messages, bringing the catalog to 262. Local format/lint/generate/test/build checks passed;
  Localization `29640108992` and Foundation `29640108969` passed with bundle SHA-256
  `a3de4b0bf4afd710a01d15e0426f0d163b56910c0b04f26c411870eae9eea368`.
- Linux `2cd9cdc2dfb423e5d9da56f3a235efba8727da53` adds worker cache reuse and GTK controls for
  policy, inspection, export, exact deletion, and clear-all. Local format, strict Clippy, offline
  GUI check, 87 library tests, localization sync, and diff checks passed. Native `29640319555`
  (job `88069646252`), Foundation `29640319563`, and Flatpak `29640319593` (job `88069646300`)
  passed.

Translation-memory behavior is now implemented for the Linux-first slice; end-user prompt approval,
complete visible-string gettext coverage, physical compositor/GPU rendering, signing, distributable
artifacts, stable release, and the remaining acceptance scenarios remain open.

## 2026-07-18 — Linux history controls checkpoint

Assumption: the Linux history window is a bounded view over Core schema 3; export serializes the
displayed snapshot only, while translation-memory storage and history enable/disable policy remain
separate future work.

- Core `6079138348f3182b19c017f50db768df05da62cb` adds newest-first listing and exact operation-ID
  deletion APIs, with storage tests; Core CI `29638085207` and Native SDK `29638085241` passed.
- l10n `971d1691a4eff396c71216b898e30fcfb23e72fa` adds ten Linux history-window/export/delete
  messages, bringing the catalog to 240 messages; Localization `29638057493` and Foundation
  `29638057470` passed.
- Linux `9ff8f3fb9cf61e1f51c3fc5e042e5fc8f601b837` adds the GTK history window, exact per-entry
  deletion, escaped UTF-8 TSV export, worker commands/events, and regression coverage. Local
  formatting, strict Clippy, GUI source check, 83 passing demo-provider tests plus one intentional
  ignore, and localization sync passed. Native `29638278667` passed; Flatpak `29638278677` (job
  `88064320034`) also passed.

History inspection/export/per-entry deletion and history enable/disable policy are no longer open
boundaries for the Linux slice; translation-memory stores and end-user prompt approval remain open.

## 2026-07-18 — Linux history policy checkpoint

Assumption: disabling history affects only future standard completions; existing rows remain
available for inspection, export, and deletion, while Incognito remains an unconditional request
opt-out.

- Core `fb00f3dd6b62a8a3a47350acc85831e60e266929` adds schema 4 persisted history policy APIs and
  storage coverage; CI `29638960182` and Native SDK `29638960230` passed.
- l10n `40f3914e1b28fddd8f38d287fa121010f5192f1c` adds four policy messages, bringing the catalog to
  244 messages; Localization `29639069395` and Foundation `29639069371` passed with bundle SHA-256
  `f3e49113ed85e7e4fadeef6b872ccfe5a2e4fa67548028db5f4524479aedeeb4`.
- Linux functional revision `7173d4a4217d6211c7dc92c368d9f033874198f5` adds the GTK policy toggle,
  worker policy commands/events, and regression coverage. Native `29639139698` (job `88066556152`),
  Foundation `29639139712`, and Flatpak `29639139725` (job `88066556256`) passed.

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
| Rust core checkpoint | Validated locally and remotely | Functional revision `b5fb19cf2123b70587775cd6e4a68515a5790575` uses Core `0.1.0-alpha.2`, ABI 1, protocol 1, `protected_spans_v1`, `long_text_chunking_v1`, bounded request-level glossary protection, deterministic bounded glossary CSV interchange, SQLite schema 3 bounded translation history with newest-first listing and exact per-entry deletion, schema 4 persisted history policy, and schema 5 optional translation memory with versioned identity and exact controls; it passed rustfmt, strict Clippy, full workspace tests, offline build, native SDK checks, CI run `29640169852`, and Native SDK run `29640169834`. |
| Localization bundle | Validated locally and remotely | l10n evidence revision `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995` contains 262 canonical messages, including Linux translation-memory controls/status, 12 official locale packs, two pseudo-locales, 59 generated artifacts including paired Linux PO/MO resources, 26 passing tests, platform-format checks, and deterministic bundle ZIP SHA-256 `a3de4b0bf4afd710a01d15e0426f0d163b56910c0b04f26c411870eae9eea368`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `2cd9cdc2dfb423e5d9da56f3a235efba8727da53` includes the prior secure-provider, glossary, history, and policy behavior plus optional translation-memory cache reuse with confirmed provider identity, Incognito bypass, startup policy/count restore, localized GTK policy/list/export/delete/clear controls, and persistence-failure guards. Local suites passed 87 library tests with one controlled ignore; Native run `29640319555` (job `88069646252`), Foundation run `29640319563`, and Flatpak run `29640319593` (job `88069646300`) passed. |
| Linux Flatpak packaging scaffold | GNOME 49 SDK build and bounded sandbox startup validated | Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` publishes the pinned GNOME 49 manifest, immutable Core/Linux source pins, generated Cargo archive hashes, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; latest `Flatpak Linux` run `29625778180` (job `88029765322`) is the current remote packaging gate. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | l10n revision `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995` passed Localization run `29640108992` and Foundation run `29640108969`; Core revision `b5fb19cf2123b70587775cd6e4a68515a5790575` passed CI run `29640169852` and Native SDK run `29640169834`; Linux revision `2cd9cdc2dfb423e5d9da56f3a235efba8727da53` passed Native run `29640319555` (job `88069646252`), Foundation run `29640319563`, and Flatpak run `29640319593` (job `88069646300`). |
| Non-functional repository heads | Passed | Core head `b5fb19cf2123b70587775cd6e4a68515a5790575`, l10n head `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995`, and Linux head `2cd9cdc2dfb423e5d9da56f3a235efba8727da53` are the current functional pins and passed their CI gates. The release manifest intentionally pins these revisions and lists no release artifact. |
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
