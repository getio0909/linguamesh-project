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
compositor/GPU rendering and release artifacts remain open. Core schema 6 and the Linux worker now
persist bounded TXT/Markdown/SRT/WebVTT job snapshots and restore pending/running segment progress after
restart without source paths or credentials; GUI queue presentation and archive codecs remain open.
No stable product release, completed native client, or released SDK artifact is claimed here.

## 2026-07-18 — Linux document job recovery checkpoint

Assumption: this slice persists only an opaque job ID, source basename, format, ordered bounded
segments, and lifecycle state. Pending/running jobs are restored automatically; completed, cancelled,
and failed snapshots remain inspectable until deletion. Provider credentials, session secrets,
filesystem paths, and archive payloads are excluded.

Core revision `6c54f329e9a62ffa1d2f9503087e59d4b9e9d6e9` adds schema 6 document-job/segment tables,
transactional snapshot replacement, bounds, state transitions, and restart-safe recovery APIs. Linux
revision `ec7a12c649c03c20d7a9665a6499fe8eece6023e` exposes worker create/list/update/resume/cancel
commands, sequential TranslateDocumentJob execution, per-segment events, native import persistence,
and startup restoration events. Core tests (19 storage tests plus full workspace suite) and Linux tests
(91 passed, 1 intentional environment skip) cover migration, segment reconstruction, queue bounds,
structure protection, cancellation, and absence of paths/credentials. Core CI `29641613390`, Native
SDK `29641613407`, Linux Native `29642622311` (job `88075537969`), Foundation `29642623263` (job
`88075540141`), and Flatpak `29642624183` (job `88075542529`) passed.

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

## 2026-07-18 — Linux TXT/Markdown document checkpoint

Assumption: the first Linux document slice is limited to bounded UTF-8 TXT and Markdown imports;
Core preserves BOM/line endings and Markdown fenced structure, while persistent document queues,
interrupted-job recovery, archive codecs, and stable release support remain future work.

- Core `e207754a35d9e29b8716420e1d19f755c9e27682` adds `linguamesh-document` and negotiates
  `bounded_text_document_v1` for format detection, bounded inspection, serializable segments, and
  fail-closed reconstruction. Local fmt, strict Clippy, locked build, full offline workspace tests,
  and diff checks passed; CI `29640818611` and Native SDK `29640818595` passed.
- Linux `07065259f84dac09618627fda1b0f3c90f8bc9d0` routes native TXT/Markdown import through the
  Core contract and localizes invalid UTF-8/size/import failures. Local 87-test, Clippy, GUI Rust,
  l10n-sync, and diff checks passed; Native `29640999127` (job `88071403342`), Foundation
  `29640999121`, and Flatpak `29640999145` (job `88071403518`) passed.
- The first Linux attempt, run `29640946521`, failed at shared-Core checkout because the workflow
  contained an incorrect full SHA; the pin was corrected and rerun successfully above. This failure
  did not execute product validation steps.

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

## 2026-07-18 — Linux document pause checkpoint

Assumption: the current Linux-first slice prioritizes durable TXT/Markdown job lifecycle controls;
Android, Windows, and macOS remain deferred. Core schema 8 (`31e7d3d06abbbf32199432bdedfcaf9a46dbed38`)
adds validated non-secret document translation options on top of transactional paused-job persistence.
Linux (`d5e9bb13e75e172e8698d5227e4ac27a7e70dd35`) reuses those options after restart only when the
active provider/model match. Local Core workspace tests and Linux 94-test library suite pass; Core
CI `29644499145`, Native SDK `29644499158`, Linux Native `29644639413`, Foundation `29644639392`,
and Flatpak `29644639396` are the current remote evidence.
No stable release or cross-platform completion claim is made.

## 2026-07-18 — Linux subtitle document checkpoint

Assumption: SRT and WebVTT preserve cue IDs, headers, timestamps, ordering, and original line
endings verbatim. Only cue text is translatable; timing and subtitle line-length policy are not
rewritten automatically. Android, Windows, and macOS remain deferred under the Linux-first scope.

Core `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` extends `bounded_text_document_v1` with bounded
UTF-8 SRT/WebVTT detection, timestamp/cue-order validation, subtitle structural segmentation,
reconstruction validation, and inter-cue WebVTT metadata handling. Linux
`33b47852f3bd3a0a4a8997cd6592c756a0b254a3` accepts `.srt` and `.vtt` in the native chooser and maps
malformed structures to a safe import error. TXT/Markdown and schema-8 restart option reuse remain
unchanged; HTML/JSON/CSV, archive formats, and multi-job queue presentation remain open.

Local validation passed Core fmt/check/Clippy/offline workspace tests and the 7-test document suite;
Linux fmt/check/Clippy/offline library tests passed with 94 tests passing and 1 intentional
environment-dependent ignore. Core CI `29645385353` passed; Native SDK `29645385324`, Linux Native
`29645547013` (job `88083068099`), Foundation `29645547036` (job `88083068179`), and Flatpak
`29645547024` (job `88083068088`) passed; Core CI and Native SDK also passed.

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
| Rust core checkpoint | Validated locally and remotely | Functional revision `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` includes schema 5 optional translation memory, schema 6 bounded document-job/segment snapshots, schema 7 paused-job state, schema 8 non-secret document options, and the negotiated `bounded_text_document_v1` contract for bounded UTF-8 TXT/Markdown/SRT/WebVTT inspection, preserved line endings, Markdown fences, subtitle cue IDs/headers/timestamps, inter-cue WebVTT metadata, serializable segments, and fail-closed reconstruction; local fmt, strict Clippy, offline workspace tests, CI `29645385353`, and Native SDK `29645385324` passed. |
| Localization bundle | Validated locally and remotely | l10n evidence revision `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995` contains 262 canonical messages, including Linux translation-memory controls/status, 12 official locale packs, two pseudo-locales, 59 generated artifacts including paired Linux PO/MO resources, 26 passing tests, platform-format checks, and deterministic bundle ZIP SHA-256 `a3de4b0bf4afd710a01d15e0426f0d163b56910c0b04f26c411870eae9eea368`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `33b47852f3bd3a0a4a8997cd6592c756a0b254a3` negotiates `bounded_text_document_v1`, converts bounded TXT/Markdown/SRT/WebVTT imports into Core jobs, preserves subtitle cue IDs/headers/timestamps, sequentially translates pending prose segments with persisted progress, supports cancellation/reconstruction, and restores schema-8 snapshots without paths or credentials while retaining secure-provider, glossary, history, policy, and translation-memory behavior. Local 94-test suite (1 intentional ignore), strict Clippy, Rust checks, and diff checks passed; Native `29645547013` (job `88083068099`), Foundation `29645547036` (job `88083068179`), and Flatpak `29645547024` (job `88083068088`) passed. |
| Linux Flatpak packaging scaffold | GNOME 49 SDK build and bounded sandbox startup validated | Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` publishes the pinned GNOME 49 manifest, immutable Core/Linux source pins, generated Cargo archive hashes, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; latest `Flatpak Linux` run `29645547024` (job `88083068088`) passed. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | Core revision `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` passed CI `29645385353` and Native SDK `29645385324`; Linux revision `33b47852f3bd3a0a4a8997cd6592c756a0b254a3` passed Native `29645547013` (job `88083068099`), Foundation `29645547036` (job `88083068179`), and Flatpak `29645547024` (job `88083068088`); l10n revision `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995` remains CI-verified. Central coordination `29645763887` passed Linux job `88083632226` and PowerShell job `88083632209`. |
| Non-functional repository heads | Published | Core head `e4962fc19dd09ca2ef45d4841ffb617cb25a1342`, l10n head `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995`, and Linux head `33b47852f3bd3a0a4a8997cd6592c756a0b254a3` are the current functional pins and passed their remote gates. The release manifest remains unreleased with no artifacts. |
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
