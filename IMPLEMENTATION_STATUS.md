# Implementation Status

Last updated: 2026-07-19

## Current checkpoint

Linux routing configuration revision `cd9df9fff290fa2f3ebaf64fcf8e5819039eaf7f` now exposes
Core's `Manual`, `Ordered`, and `Automatic` modes, explicit fallback consent defaulting off, and
focusable candidate checkboxes for saved provider/model pairs. Local Linux validation passed with
131 tests (`129 passed; 2 ignored`), GUI all-target check, strict Clippy, formatting, localization
sync/audit, Flatpak metadata, and diff checks. Push Native/Flatpak/Foundation runs
`29697021191`/`29697021176`/`29697021171` and PR Native/Flatpak/Foundation runs
`29697022738`/`29697022740`/`29697022751` all passed after one PR Native AT-SPI cleanup rerun. This is a Linux
configuration slice only and does not claim complete candidate management, other clients, visual or
Orca review, distributable artifacts, or a stable release.

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
pause, cancel, or export binary DOCX/PPTX/XLSX/EPUB/PDF output; pixel-identical PDF reconstruction,
image-only page translation beyond the opt-in OCR path, and remaining archive codecs remain open. Core now
exposes structured PDF warnings for image-only pages, uncertain reading order, and limited
reconstruction; Linux renders fixed, page-number-only warning text without source content.
Linux standard-text translation now has an explicit approved-fallback control: one different saved
provider may receive a retry after a network or timeout failure, partial output is preserved, and the
selection is surfaced; document jobs, cancellation, authentication/model failures, unapproved
profiles, and session-only profiles never fall back.
Core now also exposes the non-secret `routing_planner_v1` contract for deterministic Manual,
Ordered, and Automatic candidate selection with explainable rejection/ranking data and explicit
fallback ordering; Linux negotiates this feature before provider work. Linux persists and edits
validated non-secret routing profiles through the worker/storage boundary and executes ordinary text
requests through a selected saved routing profile, resolving candidates through the host secret
broker. Ordered/Automatic chains now skip unavailable saved providers, retry retryable stream
failures across remaining candidates, preserve partial output, remap event sequences, and emit
typed fallback notices without endpoints, credentials, or source content. Linux document jobs now
select a saved document-capable routing candidate, persist the selected provider/model options,
and emit a typed non-secret decision; document jobs never auto-fallback. Core schema 16 now stores
the optional non-secret routing-profile ID, so Linux Resume and Retry reconnect the saved profile
after worker restart; legacy schema-15 snapshots without that ID retain their persisted provider/
model resume path. Other client controls remain unimplemented.
The document-job queue now renders source, technical format, lifecycle state, and completed/total
metadata through catalog templates and stable state labels rather than Rust debug formatting. Linux
source-referenced localization keys are now statically audited against the canonical catalog in
Native and Foundation CI. Linux now exposes localized OpenAI-compatible and native Ollama provider
presets in GTK, preserving user-entered endpoint edits while switching protocol defaults.
Linux file-import regression coverage now exercises bounded DOCX package reconstruction with tables,
headers, and retained image parts, plus XLSX shared-string selection while preserving unselected
values, formulas, numbers, and image parts. The same native wrapper now rejects DOCX ZIP path
traversal and oversized uncompressed entries before import.
The worker queue now has a native regression proving that multiple pending jobs are listed together
for explicit queue selection. Linux worker regressions now also drive persisted DOCX and XLSX jobs
through fake-provider translation and inspect reconstructed OOXML while preserving binary resources,
formulas, and numeric cells.
The reviewed Core archive boundary now also rejects suspicious OOXML compression ratios before XML
inspection, and Linux consumes that guard through an immutable Core pin.
No stable product release, completed native client, or released SDK artifact is claimed here.

## 2026-07-19 — Linux routed document restart checkpoint

Assumption: a routed document job must persist only its non-secret routing-profile ID so restart can
re-run deterministic candidate selection; legacy jobs without that ID continue using saved
provider/model options. Document fallback remains disabled.

- Core `9926d0f9bf6394c6011c6cc886d142bfeb54e10f` adds schema 16 and the transactional migration
  for `document_job_options.routing_profile_id`.
- Linux `202f565f65738345d23c3e19b428a99494ad7cfe` reconnects the saved profile through the host
  secret broker for Resume and Retry, emits a zero-fallback decision, and translates remaining
  segments after restart. Regression `document_job_resume_reconnects_saved_routing_profile_after_restart`
  verifies complete reconstruction.
- Local Core storage/workspace validation, Linux formatting/checks/tests/Clippy, localization and
  Flatpak audits, and diff checks passed. Core remote CI/Native SDK passed (`29694632345`,
  `29694632350`); Linux Native/Foundation push and PR gates passed (`29694926451`, `29694926454`,
  `29694927642`, `29694927681`). Final Linux push Native/Flatpak/Foundation
  `29695388000`/`29695388015`/`29695387996` and PR Native/Flatpak/Foundation
  `29695389589`/`29695389588`/`29695389602` also passed.

## 2026-07-19 — Linux ordinary-text routing execution checkpoint

Assumption: applying a saved routing profile to ordinary text is the smallest complete vertical
slice; document jobs and the existing explicit single-provider fallback retain their boundaries
until their multi-candidate semantics are specified.

- Linux `128a03ef82a031d69ad55597467d501d0415522d` adds `TranslateWithRouting`: it builds a
  non-secret `RoutingContext`, asks Core to select a candidate, reconnects the selected saved
  provider through the host secret broker when needed, and emits a typed decision summary before
  streaming the ordinary text result. The GTK routing dialog adds an explicit Use action.
- l10n `fade545ec14793893de2603c62e0994689d9c4df` contains 352 messages and the Linux pin now
  consumes the regenerated PO/MO resources.
- Local Linux validation passed 124 tests with 2 ignored, GUI all-target check, strict Clippy,
  localization sync and 228-key audit, Flatpak metadata, and diff checks. Remote push Native/
  Foundation/Flatpak runs `29692401405`/`29692401396`/`29692401402` passed; duplicate PR-triggered
  runs `29692402861`/`29692402845`/`29692402867` also passed. l10n Foundation/Localization runs
  `29691938103`/`29691938112` passed.

This checkpoint does not claim complete automatic/ordered fallback chains, document-job routing,
other clients, visual/Orca review, distributable artifacts, or a stable release.

## 2026-07-19 — Linux ordered/automatic routing fallback checkpoint

Assumption: routing fallback remains ordinary-text-only until document-job provider selection and
resume semantics are independently specified and independently verified.

- Linux `8a3b806490191f858411c802070ccaea6af606b8` executes remaining Core planner candidates for
  ordinary text. Ordered/Automatic profiles skip unavailable saved providers during initial
  dispatch; retryable network/timeout stream failures reconnect the next candidate, preserve
  partial output, remap event sequences, and emit a typed non-sensitive fallback event.
- Local Linux evidence: 125 tests passed with 2 ignored; GUI all-target check, strict Clippy,
  formatting, and diff checks passed. The regression
  `ordered_routing_skips_unavailable_primary_candidate` covers the unavailable-first-candidate
  path and translated output.
- Linux push and PR Native/Flatpak/Foundation gates passed: Native
  `29693117355`/`29693118757`, Flatpak `29693117348`/`29693118741`, Foundation
  `29693117351`/`29693118742`.

This closes ordinary-text multi-candidate routing execution only. Document-job routing, other
clients, visual/Orca review, distributable artifacts, and a stable release remain open.

## 2026-07-19 — Linux document-job saved routing checkpoint

Assumption: the smallest complete Linux document-routing slice selects one saved document-capable
candidate, records the actual provider/model options in the existing schema-15 snapshot, and keeps
automatic fallback disabled; persisting the routing-profile ID is deferred to a future migration.

- Linux `08a85653b303345bc54e242405a537a03fb1ad32` adds a routed document-job command. It loads the
  saved profile, selects a document-capable candidate through `routing_planner_v1`, resolves that
  provider through the host secret broker, and emits `RoutingDecisionSelected` with only profile,
  provider/model, and eligible/rejected/fallback counts. The selected manager is reused for segment
  continuation and same-process pause/resume; failed starts reset the job to Pending.
- The GTK document-job action prefers the selected saved routing profile over the explicit fallback
  checkbox. Document jobs reject Incognito persistence and never switch to another candidate after
  a start or stream failure, even if the profile allows explicit fallback.
- Local Linux evidence: 126 demo-provider tests passed with 2 ignored; GUI all-target check, strict
  Clippy, formatting, localization sync and 228-key audit, Flatpak metadata, and diff checks passed.
- Linux push and PR Native/Flatpak/Foundation gates passed: Native `29693935010`/`29693936875`,
  Flatpak `29693934970`/`29693936887`, and Foundation `29693934974`/`29693936881`.

This advances Linux document-routing evidence without claiming persisted profile-ID recovery,
concurrent document execution, other clients, visual/Orca review, distributable artifacts, or a
stable release.

## 2026-07-19 — Linux visible-string gettext coverage checkpoint

Assumption: compound summaries visible to users must localize their complete template rather than
concatenating an English prefix with data. Technical identifiers, filenames, model IDs, and
translation content remain data and are not translated.

- Linux `5fe8d20cd0970e8ddb0ded0fdb207c9bc7360a36` routes history and translation-memory metadata
  through `status.translation_entry_metadata`, document queue identifiers through
  `status.document_job_id`, and active-provider persistence mode through
  `provider.active_with_mode`; missing provider/model values use catalog-backed
  `status.unavailable`.
- l10n `bd06a76bcd498748b520143c61964a92727d1b51` contains 339 messages and all 59 deterministic
  native resources plus both pseudo-locales. Non-English values remain explicit machine-generated
  drafts.
- Local l10n `make check`, Linux formatting, 121 demo-provider tests with 2 ignored, GUI check,
  strict Clippy, l10n synchronization, 219-key audit, Flatpak metadata, and diff checks passed.
  The host GTK all-target test-link limitation remains unchanged.
- Linux push Native/Foundation/Flatpak runs `29690203426`/`29690203419`/`29690203422` passed;
  duplicate PR-triggered Native/Flatpak runs `29690201544`/`29690201545` also passed. l10n
  Foundation/Localization runs `29690127881`/`29690127894` passed. Central coordination run
  `29690453908` passed for the updated release and workspace manifests.

This closes the current Linux source-level compound-summary localization gap without claiming
human translated-copy review, Orca speech, automatic/ordered routing controls, other clients,
release artifacts, or a stable release.

## 2026-07-19 — Linux routing profile persistence checkpoint

Assumption: the first Linux routing slice should persist only validated planner metadata; provider
endpoints, credentials, and translation content remain outside the saved record.

- Linux `9cbd4d5a270a004eff8e71c0e813d7648f74068d` adds a catalog-backed Routing profiles action.
  The worker saves, lists, and deletes Core `routing_planner_v1` profiles through the storage
  boundary and rejects mutations while a translation is active.
- The GTK dialog creates a bounded `linux-default` automatic, local-preferred profile from saved
  provider/model selections, displays mode and candidate counts, and provides explicit deletion.
- l10n `5f98f8bf760bb552c5d9e6cc7ace575e427bae10` contains 350 messages, including the 11 Linux
  routing-profile labels and mode strings. Local l10n checks, Linux tests (122 passed, 2 ignored),
  GUI check, strict Clippy, localization sync/audit, Flatpak metadata, and diff checks passed.

This establishes routing-profile persistence and editing only. Actual translation dispatch through
automatic or ordered routing, human copy review, other clients, release artifacts, and a stable
release remain open.

Remote evidence for this head passed: Linux push Native `29691040234`, Foundation `29691040260`,
and Flatpak `29691040243`; duplicate PR-triggered Native `29691041454`, Foundation `29691041501`,
and Flatpak `29691041451`. The corresponding jobs were `88203697224`, `88203697367`,
`88203697248`, `88203700980`, `88203701027`, and `88203700779`. Central coordination commit
`bcff9b563df6f72d8a285ba4a29e8ec799d666a0` passed workflow `29691253266`.

## 2026-07-19 — Linux text translation retry checkpoint

Assumption: a failed or cancelled ordinary text request must be explicitly retryable without
creating a document job or changing the confirmed provider/model selection.

- Linux `9c19083aa87304ffb3fcc9cd3bfb276503d38a00` adds an accessible, catalog-backed Retry
  translation action that reuses the existing real worker command path. The action is disabled for
  completed/busy/document-job states and enabled only after a failed or cancelled text request.
- Linux local evidence: 121 demo-provider tests passed with 2 ignored; formatting, GUI check,
  strict Clippy, l10n synchronization, 217-key audit, Flatpak metadata, and diff checks passed.
  The host cannot link the GUI all-target test binary because its system GTK libraries do not
  export the GTK 4 symbols required by the installed gtk-rs version; this is recorded as an
  environment limitation and not treated as a passing GUI runtime test.
- l10n `50688449ab16a8007f0edebabed2f8d6f0d3a90a` adds the two Linux-only retry messages to all
  official packs and pseudo-locales; its 26 tests and deterministic generated-resource checks pass.
- Linux push Native 29689432043, Foundation 29689432053, and Flatpak 29689432045 passed for the
  new head; duplicate push-triggered Native/Foundation/Flatpak runs 29689431072/29689431028/
  29689431052 also passed. l10n Localization/Foundation runs 29689387482/29689387493 and
  central coordination run 29689497792 passed. Stable release, human copy/visual/Orca review,
  other clients, artifacts, and automatic/ordered routing UI remain open.

## 2026-07-19 — Core OOXML compression-ratio and Linux pin checkpoint

Assumption: the shared Core archive boundary is the authoritative security control for DOCX/PPTX/XLSX
imports; Linux must consume it through the exact Native/Flatpak pin rather than duplicating parser
logic.

- Core `14cee83a650610b3a9a79a460c7c6f54ae9d21d4` rejects encrypted, symlinked, duplicate, traversal,
  over-limit, suspiciously compressed, macro-bearing, and digitally signed OOXML entries before XML
  inspection. Core workspace formatting, strict Clippy, all-feature offline tests, and locked build
  passed; Core CI `29685742893` and Native SDK `29685742897` passed all jobs.
- Linux `e03a6afb93fc4d2a8d04e5feefe31e1de9935e7e` records that Core revision in Native CI and Flatpak
  metadata, maps the unsupported macro/signature boundary through the native import wrapper, and
  keeps the worker DOCX/XLSX/PPTX end-to-end regressions intact. Local Linux validation passed 119
  tests with 2 ignored, GUI check, strict Clippy, formatting, 215-key audit, l10n synchronization,
  Flatpak metadata, and diff checks.
- Linux push Native `29686220611` (job `88190803342`), Foundation `29686220631` (job `88190803382`),
  and Flatpak `29686220605` (job `88190803207`) passed. PR Native `29686222024` (job `88190807513`),
  Foundation `29686222035` (job `88190807556`), and Flatpak `29686222028` (job `88190807563`) passed.

This strengthens mandatory Scenario 15 archive safety, records explicit macro/signature rejection, and
keeps the release train unreleased; physical visual review, other clients, signing, and distributable
artifacts remain open.

## 2026-07-19 — Linux image-only PDF OCR toolchain revalidation

Assumption: the current Linux checkout must re-run the real optional OCR fixture before its image-only
PDF evidence is reused in a later checkpoint.

- Linux `e03a6afb93fc4d2a8d04e5feefe31e1de9935e7e` passed `bash tools/run-ocr-test.sh` locally.
  ImageMagick generated the private image-only PDF, Poppler rendered it, and Tesseract recognized
  the expected English fixture text through the bounded plugin.
- The OCR path remains explicitly opt-in; malformed-PDF, unavailable-tool, timeout, and output-limit
  guards remain covered by the ordinary Linux test suite.

This revalidates Linux OCR only and does not claim pixel-identical reconstruction, non-English OCR
quality, physical visual review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux cancelled document-job retry checkpoint

Assumption: an interrupted document job must retain all pending segments and reuse its persisted
provider/model options when the user explicitly retries it.

- Linux `1e92fa3f145e61469f221c862584478dff95ae46` adds
  `cancelled_document_job_can_be_retried_without_losing_pending_segments`. The test cancels after
  a streamed partial event, verifies the cancelled snapshot still has two pending segments, then
  retries through saved options and reconstructs both translated lines.
- Local Linux validation passed with 120 tests and 2 ignored, including GUI check, strict Clippy,
  formatting, localization synchronization, 215-key audit, Flatpak metadata, and diff checks.
- Current-head Linux push and PR Native/Flatpak/Foundation gates passed in the subsequent routing
  planner compatibility checkpoint below.

This strengthens Linux Scenario 12 recovery evidence without claiming concurrent document execution,
physical interruption recovery, other clients, release artifacts, or a stable release.

## 2026-07-19 — Shared routing planner compatibility checkpoint

Assumption: routing policy must be defined once in Core and negotiated by Linux before provider work;
the current checkpoint does not claim a GTK UI for automatic or ordered chains.

- Core `d1c03ba84362c0c672c57045a59fc8092db470be` adds stricter routing-profile constraint
  validation on schema 15 persistence and advertises `routing_planner_v1` with Manual, Ordered,
  and Automatic modes, bounded non-secret constraints, stable rejection reasons, deterministic
  ranking, and explicit fallback ordering.
- Linux `eba4b036649cdb1fb4b466844b5c0429d3ff4de5` requires that feature in its exact alpha.2
  compatibility gate and pins Native/Flatpak builds to the same Core revision.
- Core CI `29688550094` and Native SDK `29688550109` passed. Linux push Native `29688581267`,
  Foundation `29688581251`, and Flatpak `29688581258` passed; PR Native `29688582602`, Foundation
  `29688582637`, and Flatpak `29688582608` passed.

This records a shared routing contract and compatibility evidence without claiming complete automatic
routing UI, ordered multi-provider chains, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux worker OOXML end-to-end checkpoint

Assumption: mandatory DOCX/XLSX evidence must exercise the persisted Linux worker command path, not
only native wrapper or shared Core reconstruction fixtures; the test packages are bounded in-memory
fixtures and contain no user paths or credentials.

- Linux `9ed0557a87b5c042d38e05cad5abf4a2afe487f9` adds worker regressions that create persisted
  DOCX and XLSX jobs, translate all pending segments through the fake provider, reconstruct the
  completed packages, and verify translated text while preserving binary resources, formulas, and
  numeric cells. Documentation revisions `468b915f050864bddff31001669ec80123263ac3` and
  `541d7cac307dfb4d63b61568cdc4ff441ed17c62` record the test names, validation boundary, and actual
  local checks.
- Local Linux validation passed: formatting, GUI all-target check, strict Clippy, localization
  audit, l10n synchronization, diff check, and `cargo test --features demo-provider --offline`
  with 115 passed and 2 ignored.
- Linux push Native `29682266701` (job `88180407003`), Foundation `29682266727` (job
  `88180407046`), and Flatpak `29682266698` (job `88180407090`) passed. PR Native
  `29682268238` (job `88180411020`), Foundation `29682268236` (job `88180411096`), and Flatpak
  `29682268234` (job `88180411062`) also passed.

This strengthens Linux evidence for mandatory Scenarios 10 and 11 without claiming macro/signature
coverage, visual review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux multi-job queue listing checkpoint

Assumption: queue selection must expose more than one resumable job in a single worker listing before
the GTK modal can claim multi-job coverage; the test uses two bounded TXT jobs in isolated storage.

- Linux `be10088904be1ae2ebb833180df43b0a1c6295b8` retains the worker regression from
  `5b7d0d51f189412f92f722345e8dc6b4ec78314b` creating two pending jobs,
  listing them through `ListDocumentJobs`, and asserting both stable IDs and pending states are
  returned together for selection; the testing guide now documents that gate and its concurrent-
  translation boundary.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (113 passed, 2 ignored),
  l10n synchronization, 215-key audit, and diff checks passed.
- Linux push Native `29681283021` (job `88177797814`), Foundation `29681282976` (job `88177797694`),
  and Flatpak `29681282978` (job `88177797688`) passed. PR Native `29681283843` (job `88177800339`),
  Foundation `29681283852` (job `88177800356`), and Flatpak `29681283837` (job `88177800299`) also passed.

This strengthens Linux document queue evidence without claiming multi-job concurrent translation,
end-user visual review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux archive path-safety checkpoint

Assumption: the Linux import boundary must reject unsafe OOXML archive entry names before any
translation or reconstruction work; the regression fixture is in-memory and contains no user path.

- Linux `8e057640f9e299335c0b0d60c3881ed7c4a84346` extends the native `file_import` tests with a DOCX
  ZIP entry containing `../outside.txt` and a deflated entry whose uncompressed size exceeds the
  bounded package limit. Core validation rejects them as `InvalidStructure` and `TooLarge`, so no
  source text is exposed to the worker and no output path is touched.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (112 passed, 2 ignored),
  l10n synchronization, 215-key audit, and diff checks passed.
- Linux push Native `29680662802` (job `88176123267`), Foundation `29680662805` (job `88176123266`),
  and Flatpak `29680662821` (job `88176123246`) passed. PR Native `29680663901` (job `88176126198`),
  Foundation `29680663898` (job `88176126183`), and Flatpak `29680663922` (job `88176126247`) also passed.

This strengthens Linux Scenario 15 evidence for traversal and bounded uncompressed-size rejection
without claiming full decompression-bomb coverage, end-user visual review, other clients, release
artifacts, or a stable release.

## 2026-07-19 — Linux office-package import checkpoint

Assumption: Linux's bounded OOXML import contract should be proven through the native wrapper as well
as Core codec tests; the fixture uses only in-memory ZIP packages and never writes to a user path.

- Linux `258f4b3d2537e3920f63dbea561649483489d036` adds native `file_import` regression fixtures for
  DOCX and XLSX. DOCX coverage translates paragraph, table, and header text while checking that the
  package's image part survives reconstruction. XLSX coverage translates one selected shared string,
  preserves an unselected string and inline value, and checks that formula, numeric, and image parts
  remain intact. The source byte buffers are never modified.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (110 passed, 2 ignored),
  l10n synchronization, 215-key audit, and diff checks passed.
- Linux push Native `29680097142` (job `88174572577`), Foundation `29680097156` (job `88174572714`),
  and Flatpak `29680097153` (job `88174572545`) passed. PR Native `29680098361` (job `88174576163`),
  Foundation `29680098362` (job `88174576126`), and Flatpak `29680098380` (job `88174576268`) also passed.

This strengthens Linux evidence for Scenarios 10 and 11 without claiming end-user visual review,
macro/signature coverage, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux GTK fixture localization checkpoint

Assumption: the automated GTK drag-and-drop fixture button is still user-visible UI and must
resolve through the canonical catalog, even though it is only enabled for interaction-test runs.

- Linux `ce1672ec3905d0c8fcc3b8f773bad64e5923158a` resolves the drag-fixture button through the
  new `fixture.drag_file` catalog key and raises the static source audit from 213 to 214 keys.
- l10n `3aa86232974f9a9ece8d3a45e6760dee294fca81` contains 333 catalog messages and bundle SHA-256
  `61a054d99935b256e79d5be7feb4d929fc8cf61af663a02b8fd10475745d70bd`.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (108 passed, 2
  ignored), l10n synchronization, and diff checks passed. l10n Foundation `29678032701` and
  Localization `29678032702` passed.
- Linux push Native `29678132379` (job `88169252095`), Foundation `29678132390` (job
  `88169251984`), and Flatpak `29678132392` (job `88169252009`) passed. PR Native `29678130604`
  (job `88169256356`), Foundation `29678130600` (job `88169256394`), and Flatpak `29678130605`
  (job `88169256366`) also passed.

This closes the currently identified literal Linux production/fixture string gap without claiming
human translated-copy review, visual/RTL review, Orca speech, physical corruption recovery, other
clients, release artifacts, or a stable release.

## 2026-07-19 — Linux built-in Ollama profile-name localization checkpoint

Assumption: built-in provider display names are user-visible Linux form values, so both the
OpenAI-compatible and native Ollama defaults must resolve through the canonical catalog while
user-edited names remain untouched.

- Linux `1153e0053b5f8e9d19dbb9ed46e9d79f9df9760a` routes new-profile initialization and untouched
  preset switching through localized default-name helpers for both built-in providers, raising
  the static source audit from 214 to 215 keys.
- l10n `85b9d45569ce840c17dc0acc7d7366d6810be48e` contains 334 catalog messages and bundle SHA-256
  `028d25b3637fbc19d41d497a860b414353615b9576db6f852a9f236bcbe770ce`.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (108 passed, 2
  ignored), l10n synchronization, and diff checks passed. l10n Localization `29678498771` and
  Foundation `29678498778` passed.
- Linux push Native `29678586553` (job `88170464148`), Foundation `29678586556` (job
  `88170464122`), and Flatpak `29678586562` (job `88170464199`) passed. PR Native `29678588077`
  (job `88170468404`), Foundation `29678588076` (job `88170468473`), and Flatpak `29678588073`
  (job `88170468469`) also passed.

This closes the currently identified built-in provider-name localization gap without claiming human
translated-copy review, visual/RTL review, Orca speech, physical corruption recovery, other
clients, release artifacts, or a stable release.

## 2026-07-19 — Linux localized preset regression-test checkpoint

Assumption: the GTK regression must exercise the same locale dropdown and preset-notification path
as production, while proving that user-edited provider names are preserved.

- Linux `f14fc89f3aecb20b3ac9611642de15d1a670ebf6` drives the real locale dropdown, verifies
  localized OpenAI/Ollama defaults and untouched-name preservation, and restores the demo endpoint
  before the existing GTK flow. This is test evidence only; production behavior remains at the
  localized-provider implementation checkpoint.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (108 passed, 2
  ignored), l10n synchronization, 215-key audit, and diff checks passed.
- Linux push Native `29679490910` (job `88172935950`), Foundation `29679490922` (job
  `88172935926`), and Flatpak `29679490960` (job `88172936097`) passed. PR Native `29679492044`
  (job `88172939088`), Foundation `29679492018` (job `88172939087`), and Flatpak `29679492030`
  (job `88172939072`) also passed.

This strengthens reproducible Linux evidence without claiming human translated-copy review,
visual/RTL review, Orca speech, physical corruption recovery, other clients, release artifacts,
or a stable release.

## 2026-07-19 — Linux corrupt-database fail-closed checkpoint

Assumption: a corrupted local SQLite file must not be repaired or overwritten implicitly; the
client should report persistence failure, preserve the bytes for recovery, and keep session-only
translation available.

- Linux `10cc4e7414efa3f55058c5748e887c5a96481641` adds a worker regression with a private malformed
  SQLite file. Startup emits typed `Persistence` storage-unavailable evidence, the demo provider
  remains available, a session-only translation completes, saved-profile deletion is rejected, and
  the malformed bytes remain unchanged after shutdown.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (108 passed, 2
  ignored), the 213-key localization audit, l10n synchronization, and diff checks passed.
- Push Native `29677532670` (job `88167639832`), Foundation `29677532645` (job `88167639590`), and
  Flatpak `29677532656` (job `88167639662`) passed. PR Native `29677534287` (job `88167644162`),
  Foundation `29677534288` (job `88167644068`), and Flatpak `29677534304` (job `88167644121`) also
  passed.

This strengthens Linux persistence-fault evidence without claiming physical corruption recovery,
desktop accessibility review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux output-safety alias checkpoint

Assumption: comparing only byte-for-byte equal destination URIs is insufficient for Scenario 18,
because a save target may be a symbolic link or hard link to the imported source file.

- Linux `c7b7599b118fa54baefe32e2063f57a890dc0f52` compares GIO identity, canonical native paths,
  and Unix device/inode metadata before both text and binary export writes. Source aliases are
  rejected before asynchronous replacement begins.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (107 passed, 2
  ignored), the 213-key localization audit, l10n synchronization, and diff checks passed.
- Push Native `29677149812` (job `88166548121`), Foundation `29677149807` (job `88166548172`), and
  Flatpak `29677149811` (job `88166548143`) passed. PR Native `29677151266` (job `88166552547`),
  Foundation `29677151263` (job `88166552516`), and Flatpak `29677151268` (job `88166552504`) also
  passed.

This strengthens Linux Scenario 18 evidence but does not claim a physical desktop review, Orca
speech review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux plural UI and provider-preservation checkpoint

Assumption: the GTK document queue's visible file count and model-discovery placeholder are
user-facing strings, so both must resolve through the canonical localization catalog while the
last confirmed provider remains usable after a bounded offline failure.

- Linux `8d84636636c969e70943b534deba3818381daed6` wires the document-jobs dialog to a localized
  plural file count and resolves the model selector's discovery placeholder from the catalog.
  The same revision retains the offline-provider regression from `b09f474`, which requires a typed
  `Network` failure under five seconds and a successful translation through the prior confirmed
  provider/model.
- Local `cargo fmt --all -- --check`, GUI all-target checks, strict Clippy, demo-provider tests
  (107 passed, 2 ignored), the 213-key localization audit, l10n synchronization, and diff checks
  passed. l10n `d3d838198027e2104583296eb3e0f6fadc283e4e` remains synchronized at 332 messages with
  bundle SHA-256 `0650b68a49daf27b56c95ae149cd5c29621d890ba4c7554c7c79d5690e38a05b`.
- Push Native `29676780532`, Foundation `29676780527`, and Flatpak `29676780531` passed. PR
  Native `29676781353`, Foundation `29676781358`, and Flatpak `29676781369` also passed.

This advances Linux evidence for localization and Scenario 17, but translated-copy, visual/RTL,
Orca speech, physical offline conditions, other clients, signing, distributable artifacts, and
stable-release evidence remain open.

## 2026-07-19 — Native Ollama GTK preset checkpoint

Assumption: the verified native Ollama worker path is ready for explicit Linux user selection, while
an independently installed daemon remains an external interoperability gate.

Linux `75d5ded3d6ab25e9a35c8614899b8ccc3cf94535` adds localized OpenAI-compatible and native Ollama
presets to the GTK provider form. The native selection maps to the stable `ollama`/`ollama_chat`
pair, restores with saved profiles, updates only untouched default name/endpoint fields, and uses
the native `/api/` endpoint tooltip. The GTK regression connects to the deterministic `/api/`
fixture, discovers `llama3.2:latest`, streams `你好，Ollama！` without a credential, and checks
Simplified Chinese labels and accessible label relations.

Local `cargo check --features gui --all-targets --offline`, test-source checking, the 105-test
demo-provider suite, l10n sync, and documentation/manifest checks passed. The host cannot link the
GTK binary because installed GTK/libadwaita symbols are older than the gtk-rs headers. Remote push
Native `29675743173` (job `88162744428`), Foundation `29675743166` (job `88162744434`), and Flatpak
`29675743159` (job `88162744336`) passed; PR Native `29675744738` (job `88162748418`), Foundation
`29675744785` (job `88162748481`), and Flatpak `29675744821` (job `88162748719`) also passed. l10n revision
`d3d838198027e2104583296eb3e0f6fadc283e4e` contains 332 messages and bundle SHA-256
`0650b68a49daf27b56c95ae149cd5c29621d890ba4c7554c7c79d5690e38a05b`.

The fixture still does not claim third-party daemon interoperability, GPU/desktop rendering, Orca,
visual copy review, stable release artifacts, or other clients.

## 2026-07-19 — Native Ollama `/api` Linux checkpoint

Assumption: Linux-first local-model support requires both Ollama's native `/api` contract and its
OpenAI-compatible `/v1/` surface; a running third-party daemon remains an external runtime gate.

Core `123d5c4d7a76873e597895763ca5d78e1ea42ea0` adds the loopback-only `ollama` provider catalog
preset and native `/api/tags` model discovery plus `/api/chat` NDJSON streaming. The adapter owns
endpoint validation, cancellation, bounded responses, fragmented UTF-8, protected-span restoration,
and completion-marker validation. Linux `a45ad953738766dc9fba5d9a6bd9e3b3280c62fa` creates an
explicit `ollama_chat` worker profile, deliberately selects `llama3.2:latest`, and verifies
`你好，Ollama！` streaming without a secret. The GTK form remains a generic endpoint form, so
end-user native-Ollama preset selection is not claimed.

Local Core format/check/Clippy/workspace tests and Linux format/check/Clippy, 105-test worker suite,
208-key localization audit, and l10n synchronization passed. Core CI `29674653973` and Native SDK
`29674653960` passed. Linux push Native `29674767565` (job `88160007604`), Foundation
`29674767554` (job `88160007526`), and Flatpak `29674767552` (job `88160007533`) passed. The
pull-request reruns also passed: Native `29674768361` (job `88160009796`), Foundation
`29674768357` (job `88160010009`), and Flatpak `29674768359` (job `88160009822`).

The fixture proves the native wire contract only; third-party daemon interoperability, GPU/desktop
rendering, Orca, visual review, other clients, and stable release artifacts remain open.

Central coordination run `29674950216` passed Linux validation job `88160536390` and PowerShell
validation job `88160536391` for the manifest, documentation, and credential-hygiene update.

## 2026-07-19 — Linux Ollama-compatible local endpoint checkpoint

Assumption: the Linux-first local-model acceptance path may use Ollama's OpenAI-compatible `/v1/`
surface. Native Ollama `/api` behavior and interoperability with a running third-party daemon remain
separate work.

Core `0d0d475d22129e8211333ee8f664a7669948ce3a` now provides a deterministic testkit fixture that
returns `llama3.2:latest` from `/v1/models` and streams `/v1/chat/completions` without a credential.
Linux `c1e701b4b0ad35eb6cd2823d19ae83cdb235b30d` uses the existing `local-loopback` preset to
connect, require deliberate model selection, and verify `你好，Ollama！` streaming end to end.

Local Core validation passed formatting, workspace check, strict Clippy, and all workspace tests;
Linux passed 65 no-default tests, 104 demo-provider tests, strict Clippy, localization-key audit,
and synchronized catalog checks. Remote Linux push Native `29673888541` (job `88157552503`) and
Flatpak `29673888548` (job `88157552511`) passed; PR Native `29673889609` (job `88157555098`) and
Flatpak `29673889576` (job `88157554910`) also passed. Android, Windows, and macOS remain deferred.

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

## 2026-07-19 — Linux provider-form Tab-chain evidence checkpoint

Assumption: provider onboarding controls require a deterministic application-window Tab/Shift+Tab
order, while Ctrl/Alt/Super-modified Tab remains native workspace navigation. Linux revision
`713c86b3da9b057cc25e72c687dc6c4c265f6439` documents the existing Capture-phase handler and the
real Xvfb/xfwm4 fixture evidence for provider and workspace controls.

- Native `29666820550`, Foundation `29666820602`, and Flatpak `29666820579` passed for the current
  Linux head.
- The local GTK fixture remains unavailable because the host linker lacks the GTK 4 symbols used
  by the current build; this is distinguished from the successful remote executable gate.

Orca speech, physical desktop review, OCR, complete visible-string gettext coverage, other clients,
and stable-release evidence remain open.

## 2026-07-19 — Linux document-job metadata localization checkpoint

Assumption: document-job row metadata is user-visible Linux UI and must use stable technical format
labels plus catalog-backed lifecycle labels; Rust `Debug` output is not an acceptable presentation
contract. l10n revision `c81728faf8679e7a5e9854537ad7c70c046c7800` adds seven Linux-only messages,
bringing the catalog to 296 messages with deterministic bundle SHA-256
`d2f4fd439b5fbc8fc6d48f1be0a91ee92f558c70b851271d643829cfe8590e9b`. Linux revision
`76b5f632fee62dc8e323e0cfec5d420e6fcc6992` localizes the row template and pending/running/paused/
completed/cancelled/failed state labels while preserving source and progress values.

- Local l10n `make check`, deterministic build, Linux formatting, strict all-target/all-feature
  Clippy, locked no-default 61-test suite, demo-provider 99-test suite (one existing
  environment-dependent ignore), l10n sync, and diff checks passed.
- Native `29667553178` (job `88140593951`), Foundation `29667553139`, and Flatpak `29667553149`
  (job `88140593974`) passed, including GTK AT-SPI/Wayland and Flatpak sandbox smoke gates.
- The first Native run for the implementation commit failed only because the workflow pinned the
  previous l10n revision; CI pin fix `fd30017b8d59df8daed3c18cef47e8741f42d904` was pushed before
  the current passing head.

Orca speech, physical desktop review, OCR, complete visible-string gettext coverage, other clients,
and stable-release evidence remain open.

## Evidence

## 2026-07-19 — Linux optional image-only PDF OCR checkpoint

Assumption: OCR is an explicitly enabled Linux capability. Linux invokes `pdftoppm` and
`tesseract` without a shell in a private temporary directory, with bounded input/pages/images/text,
output limits, and a process deadline. Recognition becomes page-marked TXT document-job text; the
source PDF is never rewritten and no pixel-identical reconstruction claim is made.

- l10n `3f3c1a1154b66d25f2936a02b8a08d2a8fc8a878` adds ten Linux-only OCR toggle/progress/error
  messages, producing 306 canonical messages and deterministic bundle SHA-256
  `6fc6839fce3a449eaf37d2efb9a52fa0ede1eab3a39fecdaff68682a79d8a4f8`. Localization run
  `29668388983` and Foundation run `29668388992` passed.
- Linux `d18e8dfa3dd98d56dbe0d5d1eabc536d38b96f1c` adds the optional plugin, worker persistence,
  page-marked import, localized GTK toggle/status/errors, and a generated external fixture.
  Native run `29668688201` (job `88143670012`) passed the OCR fixture with ImageMagick, Poppler,
  and Tesseract installed; Repository Foundation `29668688202` and Flatpak `29668688223` (job
  `88143670073`) also passed.
- Local Linux formatting, all-target/all-feature check and Clippy, locked no-default (64 passed,
  1 ignored) and demo-provider (102 passed, 2 ignored) suites, OCR fixture, localization sync,
  shell syntax, and diff checks passed.

## 2026-07-19 — Linux canonical localization-key audit checkpoint

Assumption: every literal key passed to the Linux UI localization helpers must exist in the
canonical catalog; dynamic keys remain covered by the existing runtime localization tests.

- Linux `a26ee1855e6d46ac1c174f1388bae5eb09420588` adds the dependency-free
  `tools/check-localization-keys.py` audit for literal keys in `src/main.rs` and `src/model.rs`.
  It checks the sibling l10n catalog and fails on any missing key.
- Native run `29669448961` (job `88145739138`), Foundation `29669448991`, and Flatpak
  `29669448995` (job `88145739200`) passed. The corresponding pull-request runs
  `29669459291`, `29669459309`, and `29669459312` also passed.
- Local Linux `python3 -B tools/check-localization-keys.py` covered 187 keys against the pinned
  306-message catalog; Rust checks, both locked test suites, OCR fixture, l10n sync, and diff checks
  passed.

The audit makes source-to-catalog coverage reproducible but does not replace translated-copy,
plural, visual locale/RTL, or Orca speech review.

## 2026-07-19 — Linux accessible document-progress checkpoint

Assumption: persisted document-job progress is user-visible state and must be exposed through a
native GTK progress-bar role with a bounded completed/total fraction.

- Linux `ca040585db0baaced263d438714110ddfdb315b0` adds localized completed/total progress text,
  a clamped fraction, and regression coverage for the role, 2/4 fraction, localized text, and
  hidden reset state.
- Local Linux formatting, locked no-default and demo-provider tests, strict Clippy, OCR fixture,
  localization sync, shell syntax, and diff checks passed. The host GTK libraries cannot link the
  binary GUI test; the remote Native gate executes it.
- Linux push runs Native `29670131311`, Foundation `29670131313`, and Flatpak `29670131281` passed;
  PR reruns Native `29670131967`, Foundation `29670131969`, and Flatpak `29670131964` also passed.
  The preceding code-head runs `29669977294`/`29669977297`/`29669977295` and PR reruns
  `29669978352`/`29669978350`/`29669978371` passed as well.

Orca speech, manual high-contrast/RTL/reduced-motion review, end-user Secret Service prompt
approval, translated-copy/plural/visual review, other clients, and release artifacts remain open.

## 2026-07-19 — Linux localized diagnostics checkpoint

Assumption: the non-sensitive diagnostics panel is user-visible UI and its compatibility summary
must follow runtime locale changes without exposing source text, endpoints, or secret references.

- Linux `3a135bf86d3627dafb48d53164e4568a9c9e5c03` routes the Core ABI/protocol diagnostics header
  through the canonical `diagnostics.summary` template and tests Simplified Chinese rendering plus
  source-content exclusion. The existing redacted state fields remain intact.
- Local formatting, locked all-target checks, strict Clippy, no-default tests (65 passed, 1 ignored),
  demo-provider tests (103 passed, 2 ignored), 188-key localization audit, l10n sync, shell syntax,
  and diff checks passed. The host GTK libraries cannot link the binary GUI test; CI executes it.
- Linux push runs Native `29670658430`, Foundation `29670658434`, and Flatpak `29670658437` passed;
  PR reruns Native `29670659495`, Foundation `29670659502`, and Flatpak `29670659509` also passed.

Complete visible-string gettext coverage, translated-copy/plural review, Orca speech, manual
high-contrast/RTL/reduced-motion review, end-user Secret Service prompt approval, other clients,
and release artifacts remain open.

## 2026-07-19 — Linux diagnostics-label localization checkpoint

Assumption: the Linux diagnostics panel is user-visible UI, so fixed labels, boolean values,
onboarding/status/theme/locale values, and profile-storage states must use the canonical catalog;
provider identifiers, paths, endpoints, and output content remain excluded.

- Linux `355481d937b3722e509dbd05cc1575c4e71be143` routes the complete fixed diagnostics field set
  through 20 new Linux-only catalog keys. l10n `32bef261f5f0deb9f6a0426231e365d0bae72b62`
  contains 326 messages and bundle SHA-256
  `054d6749397cbbf652e099784f2c7d0e3650779a3c17c98e68d25560d286b2d3`; non-English values remain
  explicitly unreviewed drafts.
- Local Linux formatting, locked all-target checks, strict Clippy, no-default tests (65 passed,
  1 ignored), demo-provider tests (103 passed, 2 ignored), 208-key localization audit, l10n sync,
  shell syntax, and diff checks passed. Host GTK binary linking remains unavailable because the
  installed GTK symbols do not match the required surface; Native CI executes the GUI gate.
- l10n Foundation `29671276786` and Localization `29671276797` passed. Linux push Native
  `29671444706`, Foundation `29671444731`, and Flatpak `29671444733` passed; PR reruns
  `29671445475`, `29671445499`, and `29671445495` also passed.

Complete visible-string gettext coverage beyond this diagnostics slice, translated-copy/plural
review, Orca speech, manual high-contrast/RTL/reduced-motion review, end-user Secret Service prompt
approval, other clients, and release artifacts remain open.

## 2026-07-19 — Linux document-pause error localization checkpoint

Assumption: a document-pause command rejected by the bounded worker queue is user-visible UI and
must use the same catalog-backed error rendering as other worker failures.

- Linux `1d96c9825b83cdc1cd6a2783b61fdd678b89e510` routes Pause queue-send failures through the
  reducer's client-error path, applying the existing `error.worker.command_queue_unavailable`
  catalog mapping instead of writing raw English directly into the error label.
- Linux local formatting, locked all-target checks, strict Clippy, no-default tests (65 passed,
  1 ignored), and demo-provider tests (103 passed, 2 ignored) passed. Push Native `29672046465`
  (job `88152770602`), Foundation `29672046491` (job `88152770643`), and Flatpak `29672046488`
  (job `88152770610`) passed; PR reruns `29672047299`/`29672047295`/`29672047296` also passed.

Complete visible-string gettext coverage beyond this error path, translated-copy/plural review,
Orca speech, manual high-contrast/RTL/reduced-motion review, end-user Secret Service prompt
approval, other clients, and release artifacts remain open.

## 2026-07-19 — Linux Secret Service prompted-flow checkpoint

Assumption: Secret Service `CreateItem` and `Delete` prompt paths are explicit Linux security
interactions. The client must call `org.freedesktop.Secret.Prompt.Prompt`, wait for `Completed`,
accept only an approved result, localize dismissal, and fail closed on prompt-call or timeout
failures.

- Linux behavioral revision `739538cb27bdcdc4b4f8530da6dcd5110550a310` implements the bounded
  prompted store/delete flow and keeps credentials and prompt results out of diagnostics.
  The isolated D-Bus fixture covers accepted and dismissed store/delete cases.
- l10n revision `f00b00fda307660000b0e4068c5ca1072d266df1` adds the Linux-only
  `error.storage.prompt_dismissed` key to the 327-message bundle with checksum
  `53821e2397e6697b7551693c6f5787cc1f88e24d96b3077ac590645a848f1977`.
- Local Linux formatting, locked checks, strict Clippy, 65/103 test suites, 208-key audit,
  localization sync, and all four prompted-flow fixture tests passed. l10n Foundation
  `29672618359` and Localization `29672618363` passed.
- Linux push Native `29672741665`, Foundation `29672741666`, and Flatpak `29672741675` passed;
  pull-request reruns Native `29672743058`, Foundation `29672742959`, and Flatpak `29672742990`
  also passed. Evidence is recorded in Linux docs head `6915655ea0ff7bee75a30f84063aefcd385e651c`.

End-user prompt approval UX, broader storage-fault coverage, complete gettext/plural/visual/Orca
review, other clients, signing, distributable artifacts, and stable-release evidence remain open.

## 2026-07-19 — Linux gettext plural runtime checkpoint

Assumption: the pinned gettext catalogs are the runtime source of truth for plural selection, so
the Linux client must retain every generated translation slot and apply the locale-specific rule
before replacing non-sensitive placeholders.

- Linux `29e613a806b1eb096cabab2374c494ea6a07e807` retains all NUL-separated MO plural slots and
  adds `text_plural` selection for English, French, Russian, Arabic, Hindi, Brazilian Portuguese,
  and one-form Chinese/Japanese/Korean catalogs, with safe incomplete-translation fallback.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (106 passed, 2
  ignored), 213-key localization audit, l10n synchronization, and diff checks passed.
- Push Native `29676132263` (job `88163825783`), Foundation `29676132239`, and Flatpak
  `29676132247` (job `88163825792`) passed. PR Native `29676133164`, Foundation `29676133154`,
  and Flatpak `29676133165` (job `88163828359`) also passed.

Translated-copy and visual locale review, Orca speech, end-user prompt approval, other clients,
signing, distributable artifacts, and stable-release evidence remain open.

## 2026-07-19 — Linux offline-provider preservation checkpoint

Assumption: an offline provider attempt must fail within a bounded interval while preserving the
last confirmed provider, model, and request path; the regression uses a just-released loopback port
and does not claim a physical network outage.

- Linux `b09f47415e33c84981f0d6da6fbfc6a0e00c4a53` adds a worker regression that connects a confirmed
  fake provider, rejects a session-only connection to the released loopback port as `Network` in
  under five seconds, and completes the next translation through the previous provider.
- Local formatting, GUI all-target checks, strict Clippy, demo-provider tests (107 passed, 2
  ignored), 213-key localization audit, l10n synchronization, and diff checks passed.
- Push Native `29676519123` (job `88164823336`), Foundation `29676519162`, and Flatpak
  `29676519121` (job `88164823343`) passed. PR Native `29676520477`, Foundation `29676520497`,
  and Flatpak `29676520498` (job `88164827465`) also passed.

This strengthens Linux evidence for mandatory Scenario 17; actual physical offline conditions,
Orca/visual review, other clients, signing, distributable artifacts, and stable release remain open.

| Area | Status | Evidence |
| --- | --- | --- |
| Current Linux document-job metadata, OCR, localization-key audit, accessible progress, diagnostics, pause-error localization, Secret Service prompted flows, plural UI, offline-provider preservation, output alias protection, corrupt-database fail-closed behavior, GTK fixture localization, built-in provider-name localization, OOXML archive safety, cancelled-job retry, and shared routing compatibility | Validated locally and remotely | l10n `85b9d45569ce840c17dc0acc7d7366d6810be48e` contains 334 canonical messages and bundle SHA-256 `028d25b3637fbc19d41d497a860b414353615b9576db6f852a9f236bcbe770ce`; Core `d1c03ba84362c0c672c57045a59fc8092db470be` and Linux `eba4b036649cdb1fb4b466844b5c0429d3ff4de5` are published. Linux audits 215 source keys, revalidates the real optional OCR fixture, verifies cancelled-job retry with pending-segment preservation, negotiates `routing_planner_v1`, preserves the confirmed provider after bounded offline failure, rejects source aliases during export, preserves malformed database bytes while falling back to session mode, drives the locale-dropdown preset regression path, translates persisted DOCX/XLSX/PPTX jobs end to end, reconstructs PPTX slides/notes while retaining binary resources, consumes the Core 200:1 OOXML compression-ratio guard through the native import wrapper, rejects unsupported macro/signature parts before import, and bounds AT-SPI fixture cleanup. Push Native `29688581267`, Foundation `29688581251`, and Flatpak `29688581258` passed; PR Native `29688582602`, Foundation `29688582637`, and Flatpak `29688582608` also passed. |
| Authoritative goal and plan | Present | `PROJECT_GOAL.md`, `AGENTS.md`, and `PLANS.md` were read before implementation. |
| Central policies and documentation | Validated locally | `bash tools/check-workspace.sh` passed required-file and Markdown-link checks. |
| Workspace and release manifests | Validated locally | Default and strict Bash checks parsed both TOML files, enforced the canonical set and release invariants, parsed the JSON schema, and passed. |
| Workspace automation | Bash validated | `bash -n tools/bootstrap.sh tools/check-workspace.sh` and `bash tools/bootstrap.sh --check-only` passed. The check-only run preserved all seven existing directories. |
| GitHub repositories | Published and verified | All seven repositories are public, use `main` as the default branch, have Issues and Actions enabled, have Wiki disabled, and initially matched their local committed HEAD. Canonical remotes are recorded in `workspace-manifest.toml`. |
| GitHub metadata | Validated | The repository Python 3.13 environment parsed all workflow and issue-template YAML files successfully; remote run evidence is listed below. |
| Canonical sibling repositories | Layout validated | `bash tools/check-workspace.sh --require-repositories` found all seven canonical directories and their minimum policy files. This does not verify sibling application behavior. |
| Rust core checkpoint | Validated locally and remotely | Functional revision `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` includes schema 5 optional translation memory, schema 6 bounded document-job/segment snapshots, schema 7 paused-job state, schema 8 non-secret document options, schema 9 subtitle/CSV/JSON/HTML format constraints, schema 10 bounded DOCX, schema 11 bounded PPTX, schema 12 bounded XLSX, schema 13 bounded EPUB, and schema 14 bounded PDF package persistence plus structured PDF fidelity and subtitle readability warnings, with the negotiated `bounded_text_document_v1` contract for bounded UTF-8 TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT, DOCX/PPTX/XLSX/EPUB packages, and text-based PDF page inspection with page association, coordinates where available, structured HTML fallback, preserved line endings, Markdown fences, subtitle cue IDs/headers/timestamps and cue-level limits, CSV delimiters/quotes/variable-width rows/selected-column boundaries, JSON keys/primitives/paths/escaping, HTML tags/attributes/scripts/styles/text nodes, OOXML/EPUB package resources and supported text nodes, inter-cue WebVTT metadata, serializable segments, and fail-closed reconstruction; local fmt, strict Clippy, workspace tests, Core CI `29655212117`, and Native SDK `29655212149` passed. |
| Localization bundle | Validated locally and remotely | l10n revision `f00b00fda307660000b0e4068c5ca1072d266df1` contains 327 canonical messages, including opt-in image-only PDF OCR controls/errors, Linux diagnostics labels, Secret Service prompt-dismissal guidance, 12 official locale packs, two pseudo-locales, 59 generated artifacts including paired Linux PO/MO resources, 26 passing tests, platform-format checks, and deterministic bundle ZIP SHA-256 `53821e2397e6697b7551693c6f5787cc1f88e24d96b3077ac590645a848f1977`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Linux head `739538c` negotiates `bounded_text_document_v1`, converts bounded TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB/PDF imports into Core jobs, preserves structured document metadata, provides queue actions and safe reconstruction, routes ordinary-text fallback only after explicit approval, accepts or dismisses Secret Service prompts for persistent store/delete operations, offers explicit bounded image-only PDF OCR to page-marked TXT while keeping the source PDF unchanged, and enforces source-referenced localization-key coverage against the canonical catalog. Local 65/103-test suites, strict Clippy, Rust checks, OCR and prompted-flow fixtures, localization sync, and the 208-key audit passed; push Native `29672741665`, Foundation `29672741666`, and Flatpak `29672741675` passed, as did PR reruns `29672743058`, `29672742959`, and `29672742990`. |
| Linux Flatpak packaging scaffold | Static validation passed; remote passed | Linux packaging revision `8f2cba0` publishes the pinned GNOME 49 manifest, immutable Core/Linux/l10n source pins including DOCX/PPTX/XLSX/EPUB/PDF warning UI, document queue/export-open/fallback controls, headless keyboard fixture dependency, generated Cargo archive hashes for the current lockfile, desktop entry, AppStream metadata, icon, and constrained runtime permissions. `bash tools/validate-flatpak-metadata.sh` passed locally; Flatpak job `88129285461` passed. Physical compositor/GPU rendering, signing, and distributable release remain unverified. |
| GitHub Actions | Passed | Core revision `123d5c4d7a76873e597895763ca5d78e1ea42ea0` remains validated; l10n revision `85b9d45569ce840c17dc0acc7d7366d6810be48e` passed Localization/Foundation gates; Linux head `f14fc89f3aecb20b3ac9611642de15d1a670ebf6` passed push Native `29679490910`, Foundation `29679490922`, and Flatpak `29679490960`, plus PR Native `29679492044`, Foundation `29679492018`, and Flatpak `29679492030`; the corrupt-database, offline-provider, aliased-export, 215-key audit, GTK fixture localization, built-in provider-name localization, locale-dropdown preset regression, plural-count UI, and model-placeholder localization checks passed in Native; central coordination remains separately tracked. |
| Non-functional repository heads | Published | Core head `d1c03ba84362c0c672c57045a59fc8092db470be`, l10n head `bd06a76bcd498748b520143c61964a92727d1b51`, and Linux behavioral/evidence head `5fe8d20cd0970e8ddb0ded0fdb207c9bc7360a36` are published. Current-head Linux Native/Flatpak/Foundation push and PR gates passed; the release manifest remains unreleased with no artifacts. |
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
