# Implementation Status

Last updated: 2026-07-18

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` multi-profile/session-onboarding, runtime-`ENOSPC` rollback, GIO Secret Service
adapter, runtime official Linux locale-pack switching with Arabic RTL direction, generic completion
desktop notification, bounded
native text-file import, bounded Linux glossary CSV import/export, bounded Linux JSON/HTML/EPUB/PDF document import with subtitle readability warnings, private notification-service transport validation, headless real
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
compositor/GPU rendering and release artifacts remain open. Core schema 9 and the Linux worker now
persist bounded TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX job snapshots, preserve CSV delimiters/quotes,
selected-column boundaries, JSON structure/path selection, and HTML text-node structure, and restore pending/running segment progress after restart without source
paths or credentials. Core schema 10 now persists bounded DOCX package bytes, schema 11 adds
bounded PPTX package persistence, schema 12 adds bounded XLSX persistence, schema 13 adds bounded
EPUB persistence, and schema 14 adds bounded text-PDF persistence while retaining
non-text package parts and
reconstructing supported OOXML text nodes with ZIP path, XML, entry, and size limits. The Linux GTK
client now lists persisted jobs in a modal queue and lets the user select a job to resume, retry,
pause, cancel, or export binary DOCX/PPTX/XLSX/EPUB/PDF output; PDF OCR, pixel-identical PDF
reconstruction, image-only page translation, and remaining archive codecs remain open. Core now
exposes structured PDF warnings for image-only pages, uncertain reading order, and limited
reconstruction; Linux renders fixed, page-number-only warning text without source content.
Linux standard-text translation now has an explicit approved-fallback control: one different saved
provider may receive a retry after a network or timeout failure, partial output is preserved, and the
selection is surfaced; document jobs, cancellation, authentication/model failures, unapproved
profiles, and session-only profiles never fall back.
No stable product release, completed native client, or released SDK artifact is claimed here.

## 2026-07-18 — Linux JSON document checkpoint

Assumption: JSON include/exclude rules use exact RFC 6901 JSON Pointer paths; object keys,
numbers, booleans, `null`, whitespace, and original string escapes remain protected, while
selected string values are decoded before translation and safely re-encoded on reconstruction.

- Core `ae8e437ff51fb045a6961604db6a19ebe488e0ba` adds bounded JSON syntax validation, raw-token
  preservation, array/object path tracking, default string-value segmentation, exact include/exclude
  path selection, safe JSON string decoding/encoding, and schema-9 `json` persistence mapping.
- Linux `3f6d7e577afacb3aa3b7ad8c9825a243c9a0f13f` adds `.json` chooser support, worker integration,
  malformed-input mapping, and regression coverage for path selection, primitive/key protection,
  escaping, persistence, and reconstruction. Local Linux tests: 60 passed; locked all-target checks,
  strict Clippy, and diff checks passed.
- Core CI `29647639604`, Native SDK `29647639577`, Linux Native `29647794016` (job `88088841342`),
  Foundation `29647793982`, and Flatpak `29647794021` (job `88088841323`) passed. This checkpoint
  remains unreleased; HTML and remaining archive/subtitle formats are still open.

## 2026-07-18 — Linux HTML document checkpoint

Assumption: the bounded HTML codec validates tag nesting with a stack, treats script/style bodies
as protected raw text, preserves original tags/attributes/links and whitespace, and translates only
non-whitespace text nodes. Translated text is escaped before reconstruction so provider output cannot
inject markup; external entities and remote resources are never resolved.

- Core `912780f21d8dbb19571c9b991879778a053272f8` adds bounded HTML tag-stack validation, void-tag
  handling, raw script/style protection, visible text-node segmentation, safe text escaping, and
  schema-9 `html` persistence mapping.
- Linux `2a04c096594f5358638fc9e5b1610c78c1051a13` accepts `.html`/`.htm` in the native chooser,
  routes visible text nodes through the worker, and covers malformed nesting, attributes, links,
  scripts, styles, and encoded reconstruction. Local Linux tests: 61 passed; locked all-target
  checks, strict Clippy, and diff checks passed.
- Core CI `29648352547`, Native SDK `29648352548`, Linux Native `29648437605` (job `88090534144`),
  Foundation `29648437590`, and Flatpak `29648437562` (job `88090534114`) passed. This checkpoint
  remains unreleased; DOCX, publication formats, PDF, and OCR remain open.

## 2026-07-18 — Linux DOCX package checkpoint

Assumption: Linux-first DOCX support is limited to ZIP packages of at most 4 MiB and 512 entries.
Only `word/document.xml`, headers/footers, footnotes, endnotes, comments, and glossary XML text
nodes are translated; resources remain unchanged. Encrypted, traversal, duplicate, malformed,
DTD-bearing, oversized, and incomplete packages are rejected, and package bytes never contain source
paths or credentials.

- Core `08eb64cb87d9cf6df624225819818d8287063c4c` adds bounded DOCX inspection, XML-safe text-node
  reconstruction, binary reconstruction, and schema-10 package persistence. Core CI `29650212367`
  and Native SDK `29650212378` passed, with 19 document and 25 storage tests included in the full
  workspace run.
- Linux functional revision `96c22dd1a5ac964b79124b790117b0b5dd16f2ae` adds DOCX chooser/import,
  worker reconstruction, and binary export. Packaging revision `3725ef97584b30ee34e7807e35cddc16df6ad8ae`
  pins the final Linux source and vendored DOCX dependencies. Native `29650642852` (job
  `88096278936`), Foundation `29650642855`, and Flatpak `29650642850` (job `88096278936`) passed.
- The checkpoint remains unreleased; PPTX/XLSX, EPUB, PDF/OCR, remaining archive codecs, full
  cross-platform clients, and acceptance scenarios 2–20 remain open.

## 2026-07-18 — Linux PPTX package checkpoint

Assumption: Linux-first PPTX support uses the same 4 MiB/512-entry bounded OOXML package limits as
DOCX. Only presentation slides, notes, masters, layouts, handouts, and comments XML text nodes are
translated; media, relationships, themes, and other package resources remain unchanged. Encrypted,
traversal, duplicate, malformed, DTD-bearing, oversized, and incomplete packages are rejected.

- Core `0f71a652a536753f48bb8c852fd38e97740c23ce` adds bounded PPTX inspection/reconstruction,
  resource preservation, and schema-11 package persistence. Core CI `29651206485` and Native SDK
  `29651206487` passed, with 20 document and 26 storage tests included in the full workspace run.
- Linux functional revision `ce08d1232889522bead58e6056d296f0fc8d56e1` adds PPTX chooser/import,
  worker reconstruction, and binary export. Packaging revision
  `766b78e4b236f15ee7a6f1d6e61ebd828415da82` pins the final Linux source. Native `29651317600`,
  Foundation `29651317621`, and Flatpak `29651317679` are the current gates; all three passed.
- The checkpoint remains unreleased; XLSX, EPUB, PDF/OCR, remaining archive codecs, full
  cross-platform clients, and acceptance scenarios 2–20 remain open.

## 2026-07-18 — Linux XLSX package checkpoint

Assumption: Linux-first XLSX support reuses the 4 MiB/512-entry bounded OOXML package limits.
Only shared-string and worksheet text nodes are translated; workbook relationships, styles,
formulas, numbers, and media resources remain unchanged. Encrypted, traversal, duplicate,
malformed, DTD-bearing, oversized, and incomplete packages are rejected.

- Core `36f256637236636889b0933cc5fe6a70bffff02c` adds bounded XLSX inspection/reconstruction,
  resource preservation, and schema-12 package persistence. Core CI `29651848624` and Native SDK
  `29651848606` passed, with 21 document and 27 storage tests included in the full workspace run.
- Linux functional revision `731072eb3d9b29a43fe0e238084290cd5c253e59` adds XLSX chooser/import,
  worker reconstruction, and binary export. Native `29651990077`, Foundation `29651990067`, and
  Flatpak `29651990064` passed.
- The checkpoint remains unreleased; EPUB, PDF/OCR, remaining archive codecs, full cross-platform
  clients, and acceptance scenarios 2–20 remain open.

## 2026-07-18 — Linux text-PDF checkpoint

Assumption: PDF support is bounded to text-based files and does not perform OCR or promise
pixel-identical layout reconstruction. The Core parser preserves page association, basic text
coordinates, and uncertain reading-order boundaries; encrypted PDFs, unsupported filters, malformed
objects, and over-limit inputs are rejected. Image-only pages remain explicit limitations.

- Core `7275c5ec195946ea20a2d65e5f42790b2d631ff2` adds page-aware PDF extraction, literal/hex text
  rewriting with Flate stream support, schema-14 persistence, and a structured HTML alternative for
  target text that cannot be safely encoded. Core CI `29653737299` and Native SDK `29653737293`
  passed, with 23 document and 29 storage tests in the full workspace run.
- Linux `a64e3751bdab9e6f21901f1d3bc8a7eb8004d0f0` adds PDF chooser/MIME filtering, worker export
  fallback from `.pdf` to page-aware `.html`, and documentation. Native `29653900764`, Foundation
  `29653900780`, and Flatpak `29653900782` all passed.
- This checkpoint remains unreleased; PDF OCR, pixel-identical reconstruction, image-only page
  translation, remaining archive codecs, complete cross-platform clients, and acceptance scenarios
  2–20 remain open.

## 2026-07-18 — Linux PDF fidelity-warning checkpoint

Assumption: PDF fidelity warnings are advisory structured metadata, not OCR output or a promise of
pixel-identical reconstruction. They must never include source text or credentials.

- Core `4f03618ffb1f37f27fb1edcf2de5a80e3bec540d` adds `DocumentWarning` values for limited PDF
  reconstruction, image-only pages, and uncertain reading order. Local Core workspace tests and
  strict Clippy passed; CI `29654538722` and Native SDK `29654538670` passed.
- Linux `edbfad1a8e443d86f39c782f4ad991a029cb8e76` stores warnings on imported/restored jobs,
  renders bounded page-number-only UI text, updates the Core pin, and documents the behavior. Local
  no-default and demo-provider suites passed (61 and 99 tests; one existing environment-dependent
  ignore); locked check/Clippy passed. Native `29654651108`, Foundation `29654651074`, and Flatpak
  `29654651067` passed.
- This checkpoint remains unreleased; OCR, pixel-identical reconstruction, remaining archive codecs,
  complete cross-platform clients, and acceptance scenarios 2–20 remain open.

## 2026-07-18 — Linux subtitle readability-warning checkpoint

Assumption: subtitle readability warnings are advisory, cue-level metadata only; they never expose
source text, rewrite timestamps, or change translation behavior. The default guidance is 42 Unicode
characters per line and 17 non-whitespace characters per second, and Core callers may provide custom
limits.

- Core `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` adds `DocumentWarning` values for line-length and
  reading-speed limits, stores 1-based cue numbers, and exposes `warnings_with_subtitle_limits`.
  Local document tests (25), full workspace tests, format, and strict Clippy passed; CI
  `29655212117` and Native SDK `29655212149` passed.
- Linux `60b560383e53bf4cf9ccc5ecf3821fe735206446` persists warnings on imported/restored jobs and
  renders cue-number-only English fallback text without subtitle source content. Local no-default
  and demo-provider suites passed (61 and 99 tests; one existing environment-dependent ignore),
  locked checks and strict Clippy passed; Native `29656158543`, Foundation `29656158527`, and
  Flatpak `29656158526` passed. The host-only GTK targeted test remained unavailable because the
  installed GTK linker lacks required symbols; the remote GTK gate is authoritative.
- This checkpoint remains unreleased; OCR, remaining archive formats, complete acceptance scenarios,
  non-Linux clients, and stable-release evidence remain open.

## 2026-07-18 — Linux persisted document queue checkpoint

Assumption: the queue window exposes only the bounded, non-secret job snapshot already returned by
Core storage. Selecting a row replaces the editor source and current job binding; provider
credentials and filesystem paths remain outside the persisted snapshot.

- Linux `ba7d4a3ad9d1cc152d5c52e5acf84633ae46ef92` adds a non-blocking queue-list command, a
  localized GTK “Document jobs” action, an empty-state/list dialog, progress/state metadata, and
  selection back into the existing resume/retry/pause/cancel/export controls.
- Linux packaging revision `71e8b24dd6f233c4667c705066524489b065e49a` pins the Flatpak source to the
  queue implementation. Local format, 61-test library suite, all-target checks, strict Clippy, and
  diff checks passed; Native `29649067477` (job `88092162300`), Foundation `29649067457`, and
  Flatpak `29649067473` (job `88092162266`) passed.
- This checkpoint remains unreleased; DOCX, PPTX/XLSX, EPUB, PDF/OCR, archive codecs, complete
  gettext coverage, cross-platform clients, and the remaining acceptance scenarios remain open.

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

## 2026-07-18 — Linux CSV document checkpoint

Assumption: the Linux-first document boundary remains bounded to 4 MiB input/output, 10,000
records, 1,024 fields per record, and 10,000 persisted segments. CSV detection accepts comma,
semicolon, tab, and pipe delimiters; quoted fields, escaped quotes, variable-width rows, record
line endings, and selected-column verbatim boundaries are preserved. Android, Windows, and macOS
remain deferred under the explicit Linux-first scope.

Core `5feaa3700764e3f174a69a4b490ae67b2d5cd8c9` adds `DocumentFormat::Csv`, bounded structural
parsing, decoded provider text, safe field re-encoding, selected-column segmentation, and schema-9
storage migration. Linux `f198aa539d51f21e2e29b8e366884013ea436360` accepts `.csv` in the native
chooser, maps malformed records to a generic document error, and routes decoded fields through the
worker before persistence re-encodes completed translations.

Local Core workspace tests (11 document tests, 22 storage tests), strict all-target/all-feature
Clippy, Linux all-target/all-feature check and Clippy, Linux 59-test library suite, formatting, and
diff checks passed. Remote Core and Linux gates are recorded below after completion; HTML, JSON,
archive formats, Android, Windows, and macOS remain open.

## 2026-07-18 — Linux subtitle document checkpoint

Assumption: SRT and WebVTT preserve cue IDs, headers, timestamps, ordering, and original line
endings verbatim. Only cue text is translatable; timing and subtitle line-length policy are not
rewritten automatically. Android, Windows, and macOS remain deferred under the Linux-first scope.

Core `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` extends `bounded_text_document_v1` with bounded
UTF-8 SRT/WebVTT detection, timestamp/cue-order validation, subtitle structural segmentation,
reconstruction validation, and inter-cue WebVTT metadata handling. Linux
`33b47852f3bd3a0a4a8997cd6592c756a0b254a3` accepts `.srt` and `.vtt` in the native chooser and maps
malformed structures to a safe import error. TXT/Markdown and schema-8 restart option reuse remain
unchanged at that checkpoint; HTML and archive formats remained open.

Local validation passed Core fmt/check/Clippy/offline workspace tests and the 7-test document suite;
Linux fmt/check/Clippy/offline library tests passed with 94 tests passing and 1 intentional
environment-dependent ignore. Core CI `29645385353` passed; Native SDK `29645385324`, Linux Native
`29645547013` (job `88083068099`), Foundation `29645547036` (job `88083068179`), and Flatpak
`29645547024` (job `88083068088`) passed; Core CI and Native SDK also passed.

## 2026-07-18 — Linux exported-output open checkpoint

Assumption: opening an exported result is limited to the most recent successfully written GIO URI;
the client never reconstructs or logs a filesystem path and delegates URI handling to the desktop's
default GIO application.

- l10n `4be0401a09ce26e65c8fd3c921e333d6011e8706` adds localized open-output and open-failure
  messages, producing 280 canonical messages, 59 generated artifacts, and bundle checksum
  `61fe261fb62e996b637745913bb89e5a5e0c0a16a82c5d2fe536a254cf61b6ee`; Localization `29657734947`
  and Foundation `29657734951` passed.
- Linux `45d9365eaba0b25d58c65a09e4a5dcfa2bae0840` adds a focusable Open exported output action,
  stores a destination only after asynchronous text/binary export succeeds, clears stale output
  destinations on new imports/translations, delegates to `gio::AppInfo::launch_default_for_uri`,
  and reports a fixed localized error without URI details. Local no-default/demo-provider suites
  passed (61/99 tests, one existing environment skip), GUI `cargo check`, strict Clippy, format,
  l10n sync, and diff checks passed; host GTK test linking remains unavailable because the installed
  GTK libraries lack required symbols. Native `29657811742`, Foundation `29657811734`, and Flatpak
  `29657811738` passed all remote GTK/portal/Wayland/build and sandbox gates.
- This checkpoint remains unreleased; routing fallback, OCR, screen-reader narration, physical
  keyboard traversal, complete acceptance scenarios, non-Linux clients, and stable-release evidence
  remain open.

## 2026-07-18 — Linux approved text fallback checkpoint

Assumption: one explicitly selected saved fallback profile is the smallest complete Linux Scenario 7
slice; automatic routing and ordered multi-provider chains remain future work.

- l10n `273be8a4e9c3b1084f393ce0086cdf2c42fcd4e9` adds six Linux-only fallback messages, producing
  286 canonical messages and bundle checksum `ee7c269571beca22cdbd7bea971ae266975b8004490b02ead4b71305e3a93872`.
- Linux `878a9c015d29ce49633046d435f48f5fee4c9a47` adds an opt-in saved-provider selector and worker
  routing limited to ordinary text. Only network/timeout failures retry once; cancellation,
  authentication/model failures, document jobs, incognito, unapproved profiles, and session-only
  profiles do not fall back. Partial output is retained and a localized selection notice records the
  decision without endpoint or content details. Local no-default/demo-provider suites passed
  (61/100 tests, one existing environment skip), strict Clippy, GUI check, l10n sync, and diff checks.
- Native `29659054771` (job `88118395199`), Foundation `29659054755` (job `88118395124`), and Flatpak
  `29659054756` (job `88118395046`) passed the current-head GTK, portal, Wayland, packaging, and
  foundation gates. This remains an unreleased implementation checkpoint, not stable-release evidence.
- This checkpoint remains unreleased; OCR, screen-reader narration, physical keyboard traversal,
  complete acceptance scenarios, non-Linux clients, and stable-release evidence remain open.

## 2026-07-18 — Linux AT-SPI semantic export checkpoint

Assumption: the smallest reproducible Linux screen-reader slice is live AT-SPI tree export for the
primary translation controls. Linux revision `7480579e4ae305758397082b7456715939666a9e` adds an
isolated Xvfb/xfwm4 fixture that starts the AT-SPI bus and reads the running GTK tree with
`python3-pyatspi`, verifying the named `Stop translation` push button and two text-editor roles;
existing GTK helper assertions continue to cover label relations, editor properties, and state
changes. Native `29664478686` (job `88132499067`), Foundation `29664478672`, and Flatpak
  `29664478670` passed. Central coordination `29664611878` (Linux job `88132835095`, PowerShell
  job `88132835104`) also passed. Orca speech, provider-form default Tab-chain review, physical
  desktop accessibility, OCR, other clients, and stable-release evidence remain open.

## 2026-07-18 — Linux dialog field localization checkpoint

Assumption: existing catalog keys `field.source_text` and `field.translation` are the canonical
labels for source and translated content in history and translation-memory dialogs. Linux revision
`1b68cef85d89324baba20689ce246486ab28c49b` replaces those fixed English prefixes without changing
stored content or adding locale-pack keys. Native `29664934283` (job `88133657483`), Foundation
`29664934298`, and Flatpak `29664934279` passed. Dynamic `Job` and `Identity` metadata, complete
visible-string gettext coverage, and the remaining Linux/release boundaries remain open.

## 2026-07-18 — Linux dialog metadata localization checkpoint

Assumption: the existing catalog titles `dialog.document_jobs` and `dialog.memory` are the
canonical Linux labels for the corresponding job and translation-memory metadata rows. Linux
revision `c19192fbd78b30aa55a5bac94c133c7400c78642` routes those identifier prefixes through the
active catalog without changing stored content or locale packs.

- Local `cargo fmt --all -- --check`, strict all-target/all-feature Clippy, the locked no-default
  61-test suite, and `git diff --check` passed.
- Native `29665343100` (job `88134735908`), Foundation `29665343120`, and Flatpak `29665343145`
  passed for the pushed Linux revision.

Complete visible-string gettext coverage, Orca speech, physical desktop review, OCR, other
platform clients, and stable-release evidence remain open.

## 2026-07-18 — Linux multi-job queue controls checkpoint

Assumption: the existing persisted `DocumentJobSnapshot` list is the source of truth for a
multi-job GTK queue; queue-row controls reuse the worker's existing pause, resume, and retry
commands and do not introduce a second task state machine. Linux revision
`014a79a19cb72b4eceba3d7c0c592b7655e1cdd0` adds those catalog-backed row actions while retaining
Select as the source-editor binding action.

- Local strict Clippy, the locked no-default 61-test suite, demo-provider 99-test suite (99 passed,
  1 existing environment-dependent ignore), formatting, and diff checks passed.
- Native `29665725241`, Foundation `29665725238`, and Flatpak `29665725434` passed for the pushed
  Linux revision.

Orca speech, physical desktop review, OCR, complete visible-string gettext coverage, other
platform clients, and stable-release evidence remain open.

## 2026-07-19 — Linux glossary validation localization checkpoint

Assumption: request-level glossary syntax, credential-like data rejection, and conflicting-rule
errors are stable user-facing Linux messages and require dedicated catalog keys. l10n revision
`ede66149c501a1680ed050d76b8b78e7b565ba01` adds the three Linux-only messages, producing 289
canonical entries and bundle checksum `c8bd6b0464ebbfa015988a4fc0cfd30b1f9e28d9e1aad19b8c50d36976128e8f`.
Linux revision `cb22b2052362ce7b4990cc4be99e26a152b07800` synchronizes the PO/MO resources and
maps the validation errors through the runtime catalog.

- Local l10n `make check`, targeted localization regression, strict Clippy, locked no-default
  61-test suite, l10n sync check, and diff checks passed.
- Native `29666379600`, Foundation `29666379579`, and Flatpak `29666379586` passed.

Complete visible-string gettext coverage, Orca speech, physical desktop review, OCR, other
platform clients, and stable-release evidence remain open.

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
| Rust core checkpoint | Validated locally and remotely | Functional revision `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` includes schema 5 optional translation memory, schema 6 bounded document-job/segment snapshots, schema 7 paused-job state, schema 8 non-secret document options, schema 9 subtitle/CSV/JSON/HTML format constraints, schema 10 bounded DOCX, schema 11 bounded PPTX, schema 12 bounded XLSX, schema 13 bounded EPUB, and schema 14 bounded PDF package persistence plus structured PDF fidelity and subtitle readability warnings, with the negotiated `bounded_text_document_v1` contract for bounded UTF-8 TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT, DOCX/PPTX/XLSX/EPUB packages, and text-based PDF page inspection with page association, coordinates where available, structured HTML fallback, preserved line endings, Markdown fences, subtitle cue IDs/headers/timestamps and cue-level limits, CSV delimiters/quotes/variable-width rows/selected-column boundaries, JSON keys/primitives/paths/escaping, HTML tags/attributes/scripts/styles/text nodes, OOXML/EPUB package resources and supported text nodes, inter-cue WebVTT metadata, serializable segments, and fail-closed reconstruction; local fmt, strict Clippy, workspace tests, Core CI `29655212117`, and Native SDK `29655212149` passed. |
| Localization bundle | Validated locally and remotely | l10n evidence revision `ede66149c501a1680ed050d76b8b78e7b565ba01` contains 289 canonical messages, including approved-fallback, translation-memory, glossary rule-validation, PDF/subtitle warnings, document queue actions/dialog/status/progress/tooltip controls, and exported-output open/failure actions, 12 official locale packs, two pseudo-locales, 59 generated artifacts including paired Linux PO/MO resources, 26 passing tests, platform-format checks, and deterministic bundle ZIP SHA-256 `c8bd6b0464ebbfa015988a4fc0cfd30b1f9e28d9e1aad19b8c50d36976128e8f`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Linux head `cb22b20` negotiates `bounded_text_document_v1`, converts bounded TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB/PDF imports into Core jobs, preserves subtitle cue IDs/headers/timestamps and surfaces configurable cue-level line-length/reading-speed warnings plus localized PDF fidelity warnings and document queue controls without source content, CSV delimiters/quotes/variable-width rows/selected-column boundaries, JSON structure/path selection/escaping, HTML tags/attributes/links/scripts/styles/text nodes, OOXML/EPUB non-text resources and supported text nodes, PDF page association/coordinates and structured HTML fallback, sequentially translates pending prose segments with persisted progress, lists persisted jobs in the GTK queue, supports selection plus pause/resume/retry/cancel/export, records successful asynchronous export URIs and opens them through the default GIO handler with localized path-safe failure handling, adds opt-in ordinary-text fallback to one different approved saved provider after network/timeout failure while preserving partial output, and restores schema-14 snapshots without paths or credentials while retaining secure-provider, glossary, history, policy, and translation-memory behavior. A headless Xvfb/xfwm4 fixture now verifies the provider form's explicit Tab/Shift+Tab chain plus tested onboarding/workspace controls from a real GTK focus path, while preserving Ctrl+Tab traversal. Local 61/100-test suites, strict Clippy, Rust checks, diff checks, GUI `cargo check`, fallback and focusability assertions passed; Native `29666379600`, Foundation `29666379579`, and Flatpak `29666379586` passed. |
| Linux Flatpak packaging scaffold | Static validation passed; remote passed | Linux packaging revision `8f2cba0` publishes the pinned GNOME 49 manifest, immutable Core/Linux/l10n source pins including DOCX/PPTX/XLSX/EPUB/PDF warning UI, document queue/export-open/fallback controls, headless keyboard fixture dependency, generated Cargo archive hashes for the current lockfile, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; Flatpak job `88129285461` passed. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | Core revision `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` passed CI `29655212117` and Native SDK `29655212149`; l10n revision `ede66149c501a1680ed050d76b8b78e7b565ba01` passed local and repository validation; Linux default branch head `cb22b20` passed Native `29666379600`, Foundation `29666379579`, and Flatpak `29666379586`; the AT-SPI fixture passed in Native job `88134735908`; central coordination `29665943305` passed the previous central documentation head. |
| Non-functional repository heads | Published | Core head `81be0b8be9d7115b98eae3f134b4fd0f25411bbb`, l10n head `ede66149c501a1680ed050d76b8b78e7b565ba01`, and Linux head `cb22b2052362ce7b4990cc4be99e26a152b07800` are published; current-head Linux Native/Flatpak/Foundation gates passed. The release manifest remains unreleased with no artifacts. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not passed | Scenarios 2–20 do not yet have complete cross-platform reproducible passing evidence. Linux now has complete secure-provider Scenario 3 and ordinary-text fallback Scenario 7 implementation/remote gate evidence plus partial Scenario 5 evidence; the global scenarios and stable-release evidence remain incomplete. |

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
physical desktop keyboard, physical-compositor and GPU-backed Wayland, a broader desktop matrix, and third-party
local-server interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until prompted desktop
Secret Service interaction, compatible
stable components, checksummed artifacts, and all required acceptance evidence are recorded.
