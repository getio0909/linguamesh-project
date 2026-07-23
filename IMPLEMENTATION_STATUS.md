# Implementation Status

Last updated: 2026-07-23

## 2026-07-23 — Linux localized language swap action

Assumption: Linux remains the active implementation priority; language swapping is a local,
request-free action for the supported English/Chinese pair, while Auto-source and Japanese-target
combinations remain intentionally disabled.

- Linux code `4e5a94feef09bbe382a0b6690dc8e8f7b138656f` adds the localized, focusable **Swap languages**
  control, safe sensitivity gating, runtime locale refresh, and GTK/unit regressions. It exchanges
  only the supported selector pair and preserves editor contents.
- Localization `c2526bfb3f6ff57895bdc3eeed743e26c8783613` adds the action and tooltip to all twelve
  official packs and generated pseudo-locales; `make check` passed 506 messages and 26 tests.
  Linux resources and the Native workflow pin consume that exact revision.
- Linux packaging/docs head `6a9adf472c6ca7afb26311dd0bbe06de2a0f1c05` pins Flatpak source `d6c1c51c3707bf367d4b6b1a06e9cf8faa37ebc5`. Local format, GUI/all-target checks, strict Clippy,
  163 demo-provider library tests with three documented ignores, localization audits, sync checks,
  Flatpak metadata, and diff checks passed. The local GTK binary could not link because the host's
  GTK symbols are incomplete; Native CI is authoritative for that boundary.
- PR #1 Native/Flatpak/Foundation runs `30030245422`/`30030245461`/`30030245538` passed. Push
  Flatpak/Foundation runs `30030242763`/`30030242764` passed; push Native `30030243332` remains
  pending in dependency installation and is not treated as passing. PR #1 remains Draft/Open and
  Issue #1 remains Open; release stays `unreleased`.

## 2026-07-23 — Linux explicit Clear workspace action

Assumption: Linux remains the active implementation priority; the text workspace `clear` action
must be local and network-free, while provider, locale, glossary, history, and cross-client work
remain outside this checkpoint.

- Linux code `38275fd96f0b9ed00b7d3269974780fd61874936` adds a localized, focusable **Clear workspace**
  button and reducer operation. It clears source/output text, partial usage/error/routing diagnostics,
  transient export and document notices, and file URIs without sending a worker command; it stays
  disabled during active work or a persisted document job. The GTK regression verifies Simplified
  Chinese labels, focusability, sensitivity, state reset, and empty editors after completion.
- l10n `99e0e04d200a03b2de79a8dd4a8d018847519ea2` adds the action and tooltip to all twelve official
  packs and generated pseudo-locales; `make check` passed 504 messages and 26 tests. Linux resources
  are synchronized at the same revision, and the Native workflow pin is updated.
- Local Linux formatting, GUI/all-target checks, strict Clippy, 163 demo-provider tests with 3
  documented environment-gated ignores, three localization audits, l10n synchronization, Flatpak
  metadata, and diff checks passed. Linux final packaging/workflow head is
  `54b9a29b6a72db38ae8eabcb91e1cf98dd73ecab` with Flatpak source pin
  `f832a2a04b502c06b6df606d5d6eb4d99b8cbf15`.
- Current-head Linux push Native/Flatpak/Foundation runs `30027666940`/`30027665976`/`30027665616`
  and PR Native/Flatpak/Foundation runs `30027667935`/`30027667025`/`30027666925` all passed. An
  earlier run was superseded after it exposed a stale workflow l10n pin; no failed run is used as
  evidence. Release remains `unreleased` and human visual/Orca review, cross-client parity, signing,
  rollback, and stable-release authorization remain open.

## 2026-07-23 — Linux native clipboard copy action

Assumption: Linux remains the active implementation priority; completed translation output needs an
explicit native clipboard action, while clipboard bytes must never enter Core persistence,
diagnostics, notifications, or logs. Other clients and stable-release evidence remain deferred.

- Linux `e56e56bec0bcea9fe963ca326e3918da54f50790` adds the localized, focusable **Copy translation**
  action. It stays disabled for empty output, copies only the read-only GTK output buffer through
  `GdkClipboard`, and its GTK regression reads the clipboard asynchronously after a completed fake
  translation.
- l10n `0ee87720a8613d3dc130dfb379ab4dc7bc1e1f62` adds the action and tooltip to all official packs
  and generated pseudo-locales; `make check` passed 502 messages and 26 tests.
- Local Linux formatting, GUI/all-target checks, strict Clippy, 162 demo-provider tests with 3
  documented environment-gated ignores, localization audits, Flatpak metadata, and diff checks
  passed. Native CI remains authoritative for display-backed clipboard execution on this host.
- Current-head Linux push Native/Flatpak/Foundation runs `30024453944`/`30024454262`/`30024454369`
  and PR Native/Flatpak/Foundation runs `30024457039`/`30024457175`/`30024457027` all passed for
  Linux `89f0f2d4fe9f748f34ea388daf91c52228b92b74` (documentation/Flatpak pin head).
- Central commit `555c83e00b5556101d95465771c23617cb909192` synchronized the evidence; coordination
  workflow `30025928902` passed both Linux and PowerShell validation.
- Release remains `unreleased`; this checkpoint does not claim cross-client parity, human review,
  signing, rollback, or stable-release authorization.

## 2026-07-23 — Linux typed provider rate-limit handling

Assumption: Linux remains the active implementation priority; HTTP 429 is the stable provider
signal for temporary throttling, while quota/billing semantics, other clients, and stable release
remain open.

- Core `8623b2c8829e4d9cf7299c74440dcfabb4e320db` adds shared `RateLimited` normalization for the
  OpenAI-compatible, Anthropic, Gemini, and Ollama adapters, preserves bounded `Retry-After`, and
  round-trips the category through storage and ABI serialization. Core formatting, locked workspace
  tests, and strict Clippy passed locally.
- l10n `630a8f36d96be358d81b72e2efc87cd527e66974` adds the Linux category to all official packs and
  regenerated PO/MO resources; `make check` passed with 500 messages and 26 tests.
- Linux `a7ac73d6fe8707519dd02698c26ebf8ca78a4246` renders localized plural retry guidance from the
  bounded hint. Local Linux checks passed with 162 demo-provider tests, 3 documented ignores,
  localization audits, Flatpak validation, and diff checks. Current-head Push Native/Flatpak/
  Foundation runs `30022122318`/`30022122787`/`30022122379` and PR Native/Flatpak/Foundation runs
  `30022125925`/`30022125926`/`30022126939` all passed after the workflow pin refresh in Linux
  `c19a7872823af6b7b6da022e0acfba63a0ab2ac9`.
- Release remains `unreleased`; live quota behavior, human visual/Orca review, cross-client parity,
  signing, rollback, and stable-release authorization are not claimed.

## 2026-07-23 — Linux manual model discovery fallback

Assumption: Linux remains the active implementation priority; this checkpoint closes only the
manual-model discovery fallback and does not claim Android, Windows, macOS, stable-release, or
human acceptance evidence.

- Core `7d0f61ee528d32a5671c65d3c253c12368cf40c4` now preserves a validated selected model as a
  `Manual` descriptor when native/protocol discovery is empty or returns typed `ModelUnavailable`
  (including a 404). Authentication, network, and timeout failures remain typed failures.
- Linux `9bda4c64263167cba271fbf70abec546aa68b3fc` (functional code `871c2da4e5f41cfb8197c7688ee0dd9f11b245fe`) exposes an optional
  manual-model field for every preset, forwards non-empty values for session and saved-profile
  connection tests, and keeps mandatory validation only for deployment/model presets that require it.
  Flatpak pins Core `7d0f61ee528d32a5671c65d3c253c12368cf40c4` and Linux `871c2da4e5f41cfb8197c7688ee0dd9f11b245fe`.
- Local Core strict Clippy/all-workspace tests passed; Linux GUI/all-target checks, 161 demo-provider
  library tests (3 documented ignores), localization audits, Flatpak validation, and diff checks
  passed. The exact GTK binary remains compile-verified but host linking lacks GTK/GDK/Graphene
  symbols; Native CI is authoritative. Release remains `unreleased`.

## 2026-07-23 — Linux Provider Hub health label GTK lifecycle

Assumption: Linux remains the active implementation priority; this checkpoint covers persisted,
non-secret Provider Hub health metadata and does not claim Android, Windows, macOS, stable-release,
or human/physical acceptance evidence.

- Linux `c39a5566ae0c87ef892cf9ba38f446b3a16429e5` adds a serialized GTK fixture covering hidden,
  successful UTC timestamp, normalized failure, cleared health, and no-selected-profile states.
  The fixture verifies localized output without exposing credentials or raw provider diagnostics.
- The Flatpak manifest now pins this Linux head with Core
  `460728d79b0e2373445c3d8994793d069b8057b9` and l10n
  `74f773774bdf01ca5d2ab61ce199dbd76cdadb04`. Push Native/Flatpak/Foundation runs
  `30016302142`/`30016302028`/`30016302180` passed; PR Native/Flatpak/Foundation runs
  `30016306021`/`30016305892`/`30016305878` also completed successfully.
- Local formatting, GUI/all-target compilation, demo-provider library tests (`161 passed; 0 failed;
  3 ignored`), localization audits, Flatpak metadata validation, and diff checks passed. The exact
  GTK binary test is compile-verified but cannot link on this host because GTK/GDK/Graphene symbols
  are unavailable; Native CI is authoritative for display-backed execution. Release remains
  `unreleased`. Central coordination workflow `30017427553` passed Linux and PowerShell validation.

## 2026-07-23 — Linux Provider Hub health status

Assumption: Linux remains the active implementation priority; this slice exposes only persisted,
non-secret health metadata and does not claim Android, Windows, macOS, stable-release, or
human/physical acceptance evidence.

- Localization `74f773774bdf01ca5d2ab61ce199dbd76cdadb04` adds localized success/failure templates
  across all 12 packs and regenerates the 499-message Linux resource bundle. Its Foundation and
  Localization workflows `30013122894`/`30013123046` passed.
- Linux code `8a913b263475bec70639c55550bdf9717ded4012` adds the Provider Hub label for the selected
  saved or active profile, showing a UTC ISO-8601 success timestamp or normalized failure category;
  raw provider diagnostics and credentials remain excluded. Documentation/Flatpak head is
  `c75508f887a76e46782a6176e61b560888983c13`, with the Flatpak source manifest pinned to the
  functional code head. Push Native/Flatpak/Foundation `30013497323`/`30013497315`/`30013497291`
  and PR Native/Flatpak/Foundation `30013503182`/`30013503000`/`30013502922` all passed.
- Local Linux formatting, strict all-feature Clippy, GUI cargo check, 163 all-feature library
  tests with 12 documented environment-gated ignores, localization synchronization/audits,
  Flatpak metadata, and diff checks passed. The host cannot link GTK/GDK/Graphene test binaries;
  Native CI is authoritative for display-backed UI. Central coordination workflow `30014149373`
  passed on Linux and PowerShell. Release remains `unreleased`.

## 2026-07-23 — Linux provider health persistence

Assumption: Linux is the active implementation scope; Android, Windows, macOS, stable release,
and human/physical evidence remain deferred.

- Core `460728d79b0e2373445c3d8994793d069b8057b9` adds schema-34 `ProviderProfile` health fields
  for the last successful Unix-second check and last normalized `ErrorKind`, with no raw provider
  error text or credentials persisted. The Core compatibility feature is
  `provider_health_status_v1`.
- Linux `fb9b1e6c9bb3703ade5c4b8e4c1993f716d3126c` records these fields after explicit cancellable
  connection tests, refreshes saved-profile state, and verifies success/failure/restart behavior
  in the worker fixture. Flatpak packaging `4784764b50b4362833e26a1e88b3792a811ae768` pins the
  health-aware Core and Linux sources.
- Local Core workspace tests and Linux all-feature library tests passed (163 Linux tests passed,
  12 documented environment-gated ignores). Push Native/Flatpak/Foundation
  `30010795356`/`30010795221`/`30010795318` and PR Native/Flatpak/Foundation
  `30010798544`/`30010798478`/`30010798760` passed; release remains `unreleased`.

## 2026-07-23 — Linux release-document pin alignment

Assumption: the Linux release guide must describe the same functional and localization pins that
the verified Native/Flatpak workflows consume; this is a documentation-only follow-up and does not
promote the prerelease.

- Linux `99ae05daa82d8317b4fcf7f6de792d10d349d3bc` corrects `docs/releasing.md` to l10n
  `7c2cb9fd71835ea0f9c6605d82dac87c0df012f0` (497 messages), Linux code
  `00186c29fc4e3e6682114ee29cd587d31610a1d6`, and functional packaging pin
  `73051b70028359c56654e1260621ada77def67e9`, matching the central release manifest.
- Local `git diff --check`, `bash tools/validate-flatpak-metadata.sh`, `bash tools/sync-l10n.sh
  --check`, and `cargo fmt --all -- --check` passed. Push and PR Native/Flatpak/Foundation runs
  `30008592951`/`30008592908`/`30008592945` and `30008596468`/`30008596531`/`30008596470`
  all completed successfully; the Native job ran the full GTK, portal, accessibility, release-
  evidence, and performance steps.
- GitHub PR #1 remains Draft/Open and mergeable; central Issue #1 remains Open. Their descriptions
  now reflect the current Linux-first pins and explicit cross-client, human/physical, signing,
  rollback, and stable-release boundaries. Release remains `unreleased`.

## 2026-07-23 — Linux model provenance labels

Assumption: Linux remains the active client priority; Core's existing `ModelSource` contract is
authoritative, and this slice closes the Linux selector's source-identification gap without
claiming cross-client or human-review completion.

- Core `dffa07eca2b006279f99673edff5bd0ae1b24a0f` already exposes `Discovered`, `Catalog`, and
  `Manual` model sources. Linux code `00186c29fc4e3e6682114ee29cd587d31610a1d6` now renders the
  localized source beside every GTK model name and adds a regression test; packaging pin
  `73051b70028359c56654e1260621ada77def67e9` points at that implementation.
- Localization `7c2cb9fd71835ea0f9c6605d82dac87c0df012f0` adds the three source labels and keeps
  all 12 generated packs at 497 catalog messages. Its full `make check` passed (26 tests).
- Linux local validation passed synchronization, formatting, 163 library tests (160 passed, 3
  documented ignores), strict Clippy, GUI cargo check, localization audits, Flatpak metadata,
  and diff checks. The host could not link the full GTK binary because required GTK/GDK/Graphene
  symbols are unavailable; Native CI is authoritative for that GUI test.
- Linux push Native/Flatpak/Foundation `30006418545`/`30006418485`/`30006418554` and PR
  Native/Flatpak/Foundation `30006415855`/`30006415873`/`30006415861` all passed. PR #1 remains
  Draft/Open, Issue #1 remains Open, and release status stays `unreleased`; other clients,
  display-backed/human accessibility review, live providers, signing, rollback, and stable
  authorization remain open.

## 2026-07-23 — Linux model-provenance documentation head

Assumption: Linux documentation head `99c5c5e` is a non-functional follow-up to the verified
model-provenance implementation; the release-manifest Linux pin remains `73051b70028359c56654e1260621ada77def67e9`.

- Linux `99c5c5e` synchronizes `IMPLEMENTATION_STATUS.md`, `README.md`, and `docs/architecture.md`
  with the localized `Discovered`/`Catalog`/`Manual` selector behavior and l10n revision
  `7c2cb9fd71835ea0f9c6605d82dac87c0df012f0`.
- Push Native/Flatpak/Foundation `30007622306`/`30007622052`/`30007622063` and PR
  Native/Flatpak/Foundation `30007624889`/`30007624904`/`30007625187` all passed. The Linux PR
  remains Draft/Open and mergeable; no merge or stable promotion was performed.

## 2026-07-23 — Linux/Core bounded TBX glossary import

Assumption: Linux is the active implementation priority; this checkpoint completes the bounded
Core/Linux glossary-import slice without claiming Android, Windows, macOS, or physical-device
parity.

- Core `dffa07eca2b006279f99673edff5bd0ae1b24a0f` adds restricted UTF-8 TBX parsing with 4 MiB and
  256-entry bounds, first-source/subsequent-target language mapping, locale/note preservation,
  XML entity decoding, and fail-closed DTD, unknown-entity, malformed, missing-term, conflict,
  credential-shape, and oversized-input handling. Its locked workspace suite passed 228 tests and
  strict all-feature Clippy passed.
- Linux `d61a96f` adds GTK CSV/TBX MIME/suffix filters, bounded partial reads, extension-based TBX
  dispatch, and the matching Flatpak source pin. Localization `d8d9084cdf0448039ad0aa7612e8725c6c875036`
  updates revision-62 chooser/error copy and regenerated PO/MO resources; `make check` passed 494
  messages, 12 official packs, 26 tests, deterministic generation, bundle, and Foundation checks.
- Central manifests now pin these exact revisions. Linux local validation passed 160 tests/3
  documented ignores, strict Clippy, audits, sync, Flatpak metadata, and diff checks. Linux push
  Native/Flatpak/Foundation `30004896060`/`30004896007`/`30004896045` and PR
  Native/Flatpak/Foundation `30004893289`/`30004893240`/`30004893064` passed. Release stays
  `unreleased`; PR #1 and Issue #1 remain open, while display-backed chooser review, cross-client
  parity, physical VFS/power-loss, signing, rollback, and stable authorization remain open.

## 2026-07-23 — Current pinned regression rerun

Assumption: this is a verification-only checkpoint; the functional Core, Linux, and localization
pins remain unchanged, and ignored tests still require their documented external fixtures.

- Core `53eee86ce0862bcb0b86f86da5e91257b07fe6d7` passed `cargo test --workspace --locked
  --all-targets` (226 tests passed, 0 failed, 0 ignored) and
  `cargo clippy --workspace --all-targets --all-features --locked -- -D warnings`.
- Linux `3eb710ee35c6aa626714a4c8618e37cc831661c3` passed
  `cargo test --features demo-provider --lib --locked -- --nocapture` (160 passed, 3 ignored;
  OCR, third-party Ollama, and private storage-fault fixtures remain explicitly gated).
- Localization `1de68c9568b5c380845089efc9282ff6edd04bc1` passed `make check`: 494 messages, 12
  official locale packs, 26 tests, deterministic generated resources, bundle creation, and
  Foundation validation.
- Central `bash tools/check-workspace.sh` and `git diff --check` passed; coordination workflow
  `30002603575` passed on Linux and PowerShell. Release remains `unreleased`; no component pin or
  stable-release claim changed.

## 2026-07-23 — Linux regional-locale and script translation presets

Assumption: Linux remains the active implementation scope; Core's bounded regional-locale and
script fields are exposed through the existing GTK translation-preset selector, while parity and
human review on other clients remain open.

- Core `53eee86ce0862bcb0b86f86da5e91257b07fe6d7` adds validated `english_us` and
  `chinese_simplified` presets carrying `en-US`/`Latn` and `zh-CN`/`Hans` metadata. Linux
  `52a9eb7fc579fff07627c55d7ce0f49eac5048ad` exposes both choices and preserves them for text and
  document requests; localization `1de68c9568b5c380845089efc9282ff6edd04bc1` supplies the
  catalog-backed labels in a 494-message bundle.
- Local Linux tests passed `160 passed; 0 failed; 3 ignored`, with strict Clippy, l10n `make
  check`, synchronization, Flatpak metadata, formatting, and diff checks passing. Core CI/Fuzz/
  Native SDK `30000596855`/`30000596731`/`30000596716`, l10n Localization/Foundation
  `30000492370`/`30000492390`, Linux push Native/Flatpak/Foundation
  `30000751775`/`30000751755`/`30000751799`, and Linux PR Native/Flatpak/Foundation
  `30000748043`/`30000747816`/`30000747915` all completed successfully. Central coordination
  commit `781dc286d9cbc86e75d954bfe09653f2b6891b61` passed workflow `30001370175`.
- Release remains `unreleased`; cross-client parity, qualified human accessibility/translation
  review, signing, rollback, and stable-release authorization remain open.

## 2026-07-23 — Linux GTK glossary-library selector and localized resources

Assumption: Linux remains the active implementation scope; a bounded GTK selector is the smallest
complete client slice for Core schema 33, while TBX and other-client parity remain open.

- Core schema 33 remains pinned at `1bd150b3063b6471dbf8a279db1fccb03d2c916c`. Linux worker/UI
  implementation is `cb17d52254db03614929db38228c5f482716f6c0`; packaging/source-pin head is
  `e21629584394fb313c8af8bc95d1fb6ddf885508`. The GTK workspace now saves, lists, loads, and
  deletes bounded glossary libraries through the Core-owned validation path.
- Localization `c4173bf52a5f44ebcf387de2d5dc6fcccc07338e` supplies 492 canonical messages, including
  twelve Linux glossary-library labels, tooltips, dialog strings, and empty-state copy. Linux
  resources are synchronized and the Native workflow pins this exact l10n revision.
- Local Linux `cargo test --features demo-provider --lib --locked -- --nocapture` passed `160
  passed; 0 failed; 3 ignored`; strict Clippy, format, sync, Flatpak metadata, and diff checks
  passed. l10n `make check` passed all 26 tests, generation, bundle, and Foundation validation.
- Final Linux push and PR Native/Flatpak/Foundation gates all passed: `29999190331`, `29999193186`,
  `29999193181`, `29999190239`, `29999193188`, and `29999190245`. PR #1 remains Draft/Open and
  release remains `unreleased`; TBX import, other clients, manual accessibility review, signing,
  rollback, and stable release evidence remain open.

## 2026-07-23 — Linux persistent glossary-library vertical slice

Assumption: bounded Core-owned glossary storage plus a Linux worker CRUD path is the smallest
complete persistence slice; a GTK library selector and TBX import remain separate requirements.

- Core `1bd150b3063b6471dbf8a279db1fccb03d2c916c` adds schema 33 normalized `glossaries` and
  `glossary_terms` tables, 32-library and validated-ID bounds, atomic term replacement, revalidated
  reads, cascading deletion, and no credential/endpoint storage. Linux `cc74e61` exposes save/list/
  delete commands and the restart/delete worker regression; packaging/status head is `35fea77`.
- Local Core workspace tests and strict Clippy passed; Linux demo-provider tests passed (`159
  passed; 3 ignored`) and strict Clippy passed. Core CI/Fuzz/Native SDK
  `29995295648`/`29995295576`/`29995295577` passed. Linux Push Native/Flatpak/Foundation
  `29996102525`/`29996102475`/`29996102477` and PR Native/Flatpak/Foundation
  `29996105093`/`29996105285`/`29996105371` passed. Release remains `unreleased`.

## 2026-07-23 — Linux normalized usage-record persistence

Assumption: usage metadata is safe to retain only as bounded, non-secret accounting metadata; the
history policy and Incognito mode are the persistence controls, and no provider pricing is inferred.

- Core `e48d1040a992b2fd3daaa27af2ae6bd700b25fc5` adds schema 32 `usage_records`, atomic history
  plus usage writes, bounded token counts, source labels, sanitized provider IDs, and cleanup on
  trim/delete/clear. It never stores source/output text, endpoints, credentials, or prices.
- Linux `064a6f17e37030351ef27a7bb047db2910167fe3` persists provider-reported completion usage and
  local translation-memory estimates, while Incognito and disabled-history requests persist nothing.
- Core CI/Fuzz/Native SDK `29992377731`/`29992376984`/`29992377385` passed. Linux push
  Native/Flatpak/Foundation `29992795496`/`29992795837`/`29992795547` and PR
  `29992800736`/`29992800675`/`29992800292` passed. Local Core workspace tests and Linux
  `cargo test --features demo-provider --lib --locked -- --nocapture` passed (159 passed, 3
  ignored). Release remains `unreleased`.

## 2026-07-23 — Linux usage persistence documentation-head gates

Assumption: the documentation-only head does not change the functional source pin; its completed
workflow jobs are recorded separately from the pinned implementation evidence above.

- Linux docs/status head `c4966caa37213225c52e7b0ee8a357c5e85becd7` passed push
  Native/Flatpak/Foundation `29993630277`/`29993630247`/`29993631103` and PR
  Native/Flatpak/Foundation `29993633187`/`29993633058`/`29993633663`. `gh pr checks` reports all
  six checks passing; the PR remains Draft/Open and release remains `unreleased`.

## 2026-07-23 — Linux PR gate result for status head `90a2753`

Assumption: completed Linux workflow jobs are authoritative for this documentation head; GitHub
check aggregation is recorded separately when it lags.

- Push Native `29990602946`, Flatpak `29990602971`, and Repository Foundation `29990602947`
  completed successfully.
- PR Native `29990604854`, Flatpak `29990604856`, and Repository Foundation `29990604877`
  completed successfully. The PR summary may briefly retain a pending Native check during
  propagation.
- The Linux PR remains Draft/Open; no merge or release promotion was performed. Release remains
  `unreleased`.

## 2026-07-23 — Linux PR documentation-head gate refresh

Assumption: Linux documentation head `18c019f49965a9e758a0b292748dd38adeafb0e7` is the current
review target; GitHub check-run propagation is recorded as observed rather than treated as a
source failure.

- Linux PR Native `29990141179` and Repository Foundation `29990141145` completed successfully.
- Linux PR Flatpak `29990141186` completed its build, checksum, SBOM, sandbox-smoke, and cleanup
  steps successfully, while the corresponding check run still reports `in_progress`.
- The Linux PR remains Draft/Open and no merge or release promotion is inferred. Release remains
  `unreleased`.

## 2026-07-23 — Linux demo-provider regression rerun

Assumption: the current Linux documentation head is the authoritative target for this portable
regression; environment-gated GUI, OCR, storage-fault, and third-party-daemon fixtures remain
separately evidenced and are not inferred from this suite.

- Linux documentation/status `40091f78f1aca3b13f1f8efda11d359e00fe97ae` passed
  `cargo test --features demo-provider --lib --locked -- --nocapture`: 159 passed, 0 failed, and
  3 ignored (OCR, third-party Ollama, and private storage-fault runners).
- The same head passed Linux Native, Flatpak, and Repository Foundation workflow dispatch runs
  `29988891946`, `29988892002`, and `29988891951` respectively.
- Automatic push gates also passed Native/Flatpak/Foundation runs `29989088159`, the rerun of
  `29989088223`, and `29989088163`; PR Native/Foundation runs `29989286385` and `29989286425`
  passed. PR Flatpak run `29989286410` completed successfully after its sandbox smoke, although
  GitHub check aggregation was still reporting that one check as `in_progress` during this update.
- The first push Flatpak smoke failure was an external Flathub connection error; its rerun passed,
  so no source or documentation failure is inferred.
- This is a documentation-only Linux checkpoint; the functional release-manifest pin remains
  unchanged, the Linux PR remains Draft/Open, and release status stays `unreleased`.

## 2026-07-23 — Current Core/Linux regression rerun

Assumption: the exact commands run against the currently pinned Core and Linux checkouts are the
authoritative regression evidence for this checkpoint; earlier test totals are retained as
historical records rather than rewritten.

- Core `2f91f313025b189df237294485fd47bafc1f1f53` passed
  `cargo test --workspace --locked --all-targets`: 222 tests passed, with no failures or ignored
  tests, including storage WAL replay, FileLease, ABI, provider, document, and protocol suites.
- Linux `dffc87f4e1499ce7adcc803123db4dfdac4eec1e` passed
  `cargo test --no-default-features --lib`: 83 passed, 1 environment-gated OCR test ignored, and
  no failures. The central `bash tools/check-workspace.sh` and `git diff --check` gates also passed.
- This rerun changes no functional pins or release-manifest values. Linux CI remains green at the
  published head, while physical/human, cross-client, signing, rollback, and stable-release
  evidence remain open; release stays `unreleased`.

## 2026-07-23 — Linux/Core crash-recovery and portable test refresh

Assumption: a Unix child-process abort after a committed SQLite WAL transaction is an automatable
crash-recovery boundary; it strengthens the Linux hardening record but does not emulate physical
power loss or every alternate SQLite VFS.

- Core `2f91f313025b189df237294485fd47bafc1f1f53` passed the focused
  `wal_replay_survives_process_termination_after_commit` test (`1 passed`) and the locked workspace
  test suite (`227 passed`, no failures). The regression commits a provider profile with
  `synchronous=FULL`, aborts the child process, and verifies that the parent reopens the model and
  persistent `SecretRef` from the WAL.
- Linux runtime implementation remains `04478701e3b0192cc7f90228c47badd9f6bb2d2b`; current
  documentation/status head `dffc87f4e1499ce7adcc803123db4dfdac4eec1e` passed the no-default library
  suite (`83 passed; 1 ignored`). The ignored unit case is environment-gated, and the explicit
  image-only PDF OCR fixture `bash tools/run-ocr-test.sh` passed (`1 passed`) with system
  `pdftoppm` and `tesseract`. Push Native/Flatpak/Foundation runs
  `29987023670`/`29987023696`/`29987023655` and PR runs `29987026057`/`29987026021`/`29987026006`
  all passed.
- The same Linux checkout passed `cargo fmt --all --check`, GUI `cargo check`, strict Clippy,
  `cargo-deny check` (advisories, bans, licenses, and sources), localization synchronization against
  l10n `552d87e88a8df42055b1ac76e4dfbaadca92e291`, the 436-key/537-placeholder/visible-string
  audits, and Flatpak metadata validation. The l10n sibling worktree itself remains on its user's
  clean `main` branch and was not modified.
- The private mount storage-fault runner also passed the exact ENOSPC regression (`1 passed`),
  confirming the Linux session-only degradation and false-commit guard under a bounded write fault.
  This is controlled ENOSPC evidence, not physical power-loss or broad VFS coverage.
- The same Linux documentation head also records a temporary host-network
  `ollama/ollama:0.11.10` daemon pulling `smollm:135m`; the real third-party `/api/tags` and
  `/api/chat` regression passed once without credentials. This does not claim live account, quota,
  GPU, or distribution behavior.
- This refresh strengthens reproducible process-crash evidence only. Physical power-loss and
  alternate-VFS behavior, cross-client parity, human review, signing, rollback, and stable-release
  authorization remain open; release stays `unreleased`.

## 2026-07-23 — Linux GTK candidate-chain and fallback-consent evidence audit

Assumption: the Linux routing-profile editor is the authoritative UI for user-approved candidate
chains; this coordination record covers deterministic Linux evidence only and does not promote the
release train.

- Linux implementation `b218c814c21b6e6a2f4ad691b5f6f09bf33d7bc0` (documentation head
  `04478701e3b0192cc7f90228c47badd9f6bb2d2b`) records the production GTK
  candidate-chain lifecycle: Manual/Ordered/Automatic mode, candidate selection/order, Edit/Save,
  Use, Delete cleanup, and localized accessible controls. The same serialized Native workflow
  reports one passing `gtk_routing_profile_candidate_controls_have_accessible_lifecycle` fixture
  and one passing `gtk_fallback_approval_dialog_requires_an_explicit_one_shot_action` fixture.
- Linux push Native/Flatpak/Foundation runs `29984727975`/`29984727998`/`29984727932` passed;
  the corresponding PR runs `29984730138`/`29984730127`/`29984730117` also passed. This closes
  the Linux deterministic candidate-chain/fallback-consent evidence gap only.
- Cross-client parity, live provider interoperability, human visual/copy/Orca review, physical
  VFS/power-loss evidence, signing, rollback, and stable-release authorization remain open;
  release stays `unreleased`.

## 2026-07-23 — Linux GTK Anthropic Messages preset transport evidence

Assumption: Linux is the active client scope; a deterministic loopback Messages service is the
smallest complete evidence for the production Anthropic preset, while live account, quota, model,
and external-network interoperability remain unverified.

- Core `2f91f313025b189df237294485fd47bafc1f1f53` adds `FakeProviderServer::start_anthropic()` with
  `/v1/messages`, `x-api-key` authentication, usage events, fragmented content deltas, and
  `message_stop`. Core CI/Fuzz/Native SDK `29982822450`/`29982822441`/`29982822462` passed.
- Linux implementation `2f12c7482a4d0376bbdd7ea86fd7f25557fea75f` drives Anthropic, Gemini, and
  Azure through the real GTK Connect, manual/discovered model selection, and streamed Translate
  handlers. Packaging head `0a77a14d35fad42d66c812398827b2ca50edb51c` and final status head
  `b218c814c21b6e6a2f4ad691b5f6f09bf33d7bc0` pin the exact Core source and record evidence.
  Linux push Native/Flatpak/Foundation `29983438263`/`29983438252`/`29983438279` and PR
  `29983440294`/`29983440326`/`29983440348` passed; the protocol-preset fixture reported `1 passed`.
- This closes only the Linux deterministic Anthropic protocol-preset evidence gap. Other native
  clients, live providers, human review, signing, rollback, and stable release remain open;
  release stays `unreleased`.

## 2026-07-23 — Linux GTK Gemini and Azure preset transport evidence

Assumption: Linux remains the active client scope; deterministic loopback providers prove
production GTK request shaping and lifecycle without claiming live account, quota, or deployment
interoperability.

- Linux implementation `8006f7a37b81db7c547be717b72860ee610ca7d7` adds the serialized ignored
  fixture `gtk_provider_protocol_presets_use_native_transports`. It drives Gemini discovery and
  streaming through `/v1beta/`, and Azure manual deployment discovery/streaming through the
  resource endpoint with a one-shot `api-key`; both flows require deliberate model selection and
  clear the GTK credential field immediately after capture.
- Final packaging head `5f1634c615f9e1a7ca3de8e37a99e4efc1f02b9e` repins the Flatpak source; Linux
  status head `d0e188f1018dc2f004edf2b1332469625c876913` records the final gates. Push
  Native/Flatpak/Foundation `29981441794`/`29981441765`/`29981441767` and PR
  `29981443146`/`29981443162`/`29981443177` all passed, including the Xvfb/DBus serialized
  fixture. Local formatting, GUI source check, strict Clippy, core-library tests (`83 passed;
  1 ignored`), and diff checks passed; full GTK linking is host-limited by missing GTK symbols.
- This closes only the Linux deterministic protocol-preset evidence gap. Other native clients,
  live providers, human review, signing, rollback, and stable release remain open; release stays
  `unreleased`.

## 2026-07-23 — Linux GTK one-click provider switch evidence

Assumption: Linux remains the active client scope; the production switch fixture uses one-shot
session credentials so CI proves isolation without relying on a developer keyring.

- Linux `988be0ce1f97634b8957fbcc83ca8832173ae86f` adds the serialized GTK fixture
  `gtk_one_click_provider_switch_uses_new_session_and_isolates_credentials`. It restores two saved
  rows, connects/translates through A, deliberately selects B, and proves that selection alone sends
  no inference, B becomes active only after validation, the next request reaches only B, and both
  credential fields are cleared.
- Linux push Native/Flatpak/Foundation runs `29980182737`/`29980182712`/`29980182800` and PR
  Native/Flatpak/Foundation runs `29980184753`/`29980184796`/`29980184751` all passed. The direct
  GTK fixture passed 1/1 in the Native run; local `cargo check`, strict Clippy, core-library tests,
  formatting, and Flatpak metadata checks passed. Release remains `unreleased`; Android, Windows,
  macOS, live-provider, signing, rollback, and human-review evidence remain open.
- Central coordination commit `4c128a6e692d6c3dd8f1615fc4300fa561dc4c14` passed Linux and
  PowerShell validation run `29980627136`.

## 2026-07-23 — In-scope policy documentation compliance

Assumption: the current Linux-first scope includes the shared Core, localization, and Linux
repositories; Android and Windows policy-document additions remain deferred with their platform
implementation work.

- Core `5a5a4cb89985083d02aac9d9aa226184992f3774`, l10n
  `538a15f7917f991b4995d3675f3becba1b5008e2`, and Linux
  `0ffb1c1132bbff9534f54354e0e71230963363d0` add concise `PRIVACY.md` and `CHANGELOG.md` files
  covering secret handling, content flow, draft translations, and the unreleased posture.
- Core CI/Fuzz/Native SDK `29979348220`/`29979348138`/`29979348170`, l10n
  Localization/Foundation `29979357957`/`29979357930`, and Linux push/PR Native, Flatpak, and
  Foundation `29979370911`/`29979370877`/`29979370915` and
  `29979372688`/`29979372682`/`29979372622` passed. The release remains `unreleased`.

## 2026-07-23 — Linux client-certificate TLS identity checkpoint

Assumption: Linux is the active client scope; mutual-TLS material is handled as one bounded
combined PEM identity behind a persistent or session `SecretRef`, never as a profile value.

- Core `2a3534faa9a2531cbbc6cc06d325ad7c82c69394` adds schema 31 identity-reference storage,
  bounded certificate/private-key parsing with redacted diagnostics, one-shot host-broker
  resolution, and reqwest rustls identity wiring across Chat/Responses/Azure, Anthropic, Gemini,
  and Ollama while preserving system roots and TLS verification.
- l10n `552d87e88a8df42055b1ac76e4dfbaadca92e291` adds source revision 59 and the 480-message
  generated Linux bundle. Linux implementation `b4bd13c1ec778e62ef466b7fa9d106de87731f29` adds
  masked GTK capture/clear, Secret Service or session-only handling, restore semantics, and
  exact pins; final status head is `bf5398de6b747841d779b72a9ac51752a19047ef`.
- Local Core workspace tests/strict Clippy/secret-pattern scan, Linux 162-test demo-provider
  suite (159 passed, 3 ignored), strict Clippy, GUI check, l10n checks/audits/sync, and Flatpak
  metadata validation passed. Core CI/Fuzz/Native SDK `29978060455`/`29978060459`/`29978060500`,
  l10n `29977582751`/`29977582767`, and Linux push Native/Flatpak/Foundation
  `29978367171`/`29978367181`/`29978367167` plus PR
  `29978368905`/`29978368870`/`29978368862` passed for the implementation head, and the final
  status-head push Native/Flatpak/Foundation `29978696500`/`29978696556`/`29978696510` plus PR
  `29978698516`/`29978698538`/`29978698523` also passed. Central coordination commit
  `dfcecee8fde665d1cc6e4d9f0d2b1681072e100f` passed run `29978472198`; release remains
  `unreleased`.

## 2026-07-23 — Linux provider proxy authentication SecretRef settings

Assumption: Linux is the active client scope; proxy URLs remain credential-free and proxy
credentials are supplied only as a bounded host-secret value.

- Core `cee5bd8abc5b35a50640c484bc4fbeedeb426745` adds schema 30 `proxy_auth_ref`, bounded
  `username:password` parsing/redaction, one-time host-broker resolution, and HTTP proxy
  Basic-auth forwarding for OpenAI Chat/Responses/Azure, Anthropic, Gemini, and Ollama. Storage
  persists only persistent SecretRefs and rejects session references.
- l10n `f0b1c507d73f540f298a534303d0e6e63d44e87b` adds three Linux strings at source revision 58
  and regenerates the native catalogs. Linux `34b3194c5445f640141de8ad57195768aaa6c3d0`
  adds masked GTK input, immediate clearing, explicit Secret Service persistence, session-only
  fallback, restore behavior, localization synchronization, and Flatpak/source pins.
- Local Core workspace tests/Clippy, Linux demo-provider tests/Clippy plus GUI check, localization
  `make check`, audits, sync, and Flatpak metadata validation passed. Linux push Native/Flatpak/
  Foundation `29976201970`/`29976201964`/`29976201962` and PR Native/Flatpak/Foundation
  `29976204361`/`29976204358`/`29976204331` passed for the exact documentation head; release remains
  `unreleased`.

## 2026-07-23 — Linux provider custom trusted certificate settings

Assumption: the Linux-first TLS slice accepts one bounded PEM trust bundle that augments system
roots; verification remains enabled, private-key material is rejected, and malformed/control-heavy
input fails before any provider client is built.

- Core `913be49da8bc44f9c53baab7b918f2bb002fd64f` adds schema 29 persistence, validation, and
  additive root-certificate wiring across OpenAI Chat/Responses/Azure, Anthropic, Gemini, and
  Ollama. Core `cargo check --workspace` and `cargo test --workspace` passed.
- l10n `d315efe808e05ce2fb0ee24c0247076298d57947` adds three Linux messages and regenerates 474
  messages; `make check` passed.
- Linux `e8f0bcf2c55032cae59f40dba505c6e66a2fdd89` adds the GTK field, saved-profile restore,
  Test connection/Connect forwarding, and Flatpak/source pins. Local no-default tests (83 passed,
  1 ignored), strict Clippy, localization sync, and Flatpak metadata validation passed. Full GTK
  test linking remains host-limited by missing GTK symbols. Core CI/Fuzz/Native SDK
  `29973111006`/`29973111045`/`29973111016`, l10n Localization/Foundation
  `29972855206`/`29972855181`, and Linux push Native/Flatpak/Foundation
  `29973126765`/`29973126853`/`29973126883` plus PR
  `29973129042`/`29973129135`/`29973129087` passed. Central coordination commit
  `b431d626ca3ce04b6d06f65d2e2d8973e7c65708` and run `29973194356` passed.
- Release remains `unreleased`; client certificates, proxy authentication, other clients, human
  review, signing, rollback, and stable-release authorization remain open.

## 2026-07-23 — Linux provider streaming idle timeout settings

Assumption: a bounded streaming idle timeout of 1–300 seconds (default 60) is the smallest
complete follow-up to connection timeout; the budget resets after each received response chunk,
while TLS policy remains separate.

- Core `b247155ad429639fdb65d3b063c3efc580ce46a4` adds schema 28 persistence, domain/storage range
  coverage, and typed per-chunk timeout handling for OpenAI Chat/Responses/Azure, Anthropic,
  Gemini, and Ollama. l10n `2e223f9a416f4b461b72224f12c31cbf7981dae3` regenerates the 471-message
  bundle. Linux `24b69a646a9463b13710502ce35a1bd0d15ee427` adds the localized GTK control,
  saved-profile restore/default behavior, exact source pins, and documentation.
- Local Core `cargo check --workspace` and `cargo test --workspace`, Linux `cargo test
  --no-default-features --lib` and strict Clippy, l10n `make check`, synchronization, Flatpak
  metadata, and diff checks passed. Full-feature local binary linking remains blocked by missing
  GTK symbols on this host; Linux push Native/Flatpak/Foundation
  `29971755022`/`29971755009`/`29971755012` and PR `29971756513`/`29971756522`/`29971756554`
  passed for final head `24b69a646a9463b13710502ce35a1bd0d15ee427`. Release remains `unreleased`.

## 2026-07-23 — Linux provider connection timeout settings

Assumption: a bounded connection-establishment timeout of 1–120 seconds (default 10) is persisted
and applied independently of the existing total request timeout; streaming-idle and TLS policy
remain follow-up work.

- Core `e9a569f8bb6d66db4fdb1c9bd1d6834e93d10f39` adds schema 27 persistence, domain/storage range
  coverage, and connection-timeout wiring for OpenAI Chat/Responses/Azure, Anthropic, Gemini, and
  Ollama. l10n `46ca70b2863fa951b417eda7ce5848e152c46605` regenerates the 469-message bundle.
- Linux `6fbf53da024bd37d64f93025222a57f7b0296d47` adds the localized GTK control, saved-profile
  restore/default behavior, validation before Test connection/Connect, and exact Core/l10n/Flatpak
  pins. Local Core, Linux, l10n, synchronization, localization-audit, Flatpak metadata, and diff
  checks passed. Core CI/Fuzz/Native SDK `29969609373`/`29969609372`/`29969609379`, l10n
  Localization/Foundation `29969625867`/`29969625942`, Linux push Native/Flatpak/Foundation
  `29970072910`/`29970072901`/`29970072923`, and PR `29970070485`/`29970070480`/`29970070516`
  passed for the exact revisions. Release remains `unreleased`.

## 2026-07-23 — Linux provider request timeout settings

Assumption: this checkpoint implements only a bounded total request timeout; connection timeout,
streaming-idle timeout, and TLS policy fields remain separate follow-up work.

- Core `7e78cb0086d85eb5c218d8863b7f11f506bae016` adds schema 26 persistence, 1–600 second
  validation, and request-timeout wiring for OpenAI Chat/Responses/Azure, Anthropic, Gemini, and
  Ollama. l10n `65bf0c8772f75649b2be2e2f9cea610772657c93` regenerates the 467-message bundle.
- Linux `c5db93676128e84a577f628906aad2980f919909` adds the localized GTK control, profile
  restore/default behavior, exact Core/l10n pins, and Flatpak source-head pin. Local Core,
  Linux, l10n, synchronization, localization-audit, Flatpak metadata, and diff checks passed.
- Core CI/Fuzz/Native SDK `29967953180`/`29967953114`/`29967953129` and l10n
  Localization/Foundation `29967968439`/`29967968461` passed for the exact revisions. Linux
  push Native/Flatpak/Foundation `29968376701`/`29968376654`/`29968376661` and PR
  `29968379682`/`29968379660`/`29968379655` passed for the exact head. Release remains
  `unreleased`; cross-client parity, human review, signing, rollback, and stable-release
  authorization remain open.

## 2026-07-22 — Linux provider proxy settings

Assumption: proxy authentication is intentionally out of scope; only bounded non-secret proxy
URLs without embedded credentials are supported in the Linux-first slice.

- Core `7a9da3f467c5dec539dd8f7850b90b54ae712331` adds schema 25 `proxy_url` validation,
  persistence, and transport wiring for OpenAI Chat/Responses/Azure, Anthropic, Gemini, and
  Ollama. Debug output exposes only whether a proxy is configured.
- l10n `bba90a89089c954bdfe1dcda19c210e6ea230b9e` regenerates the 465-message bundle. Linux
  `c03535f82f07ed10c273fb250654c984540ed935` adds the localized GTK field and repins Native and
  Flatpak inputs. Local Linux checks passed formatting, locked all-target check, strict Clippy,
  `159 passed; 3 ignored` demo-provider tests, localization audits, l10n synchronization,
  Flatpak metadata validation, and `git diff --check`.
- Core CI/Fuzz/Native SDK runs `29966758398`/`29966758388`/`29966758389` passed. Linux
  push Native/Flatpak/Foundation runs `29966869662`/`29966869643`/`29966869658` and PR
  Native/Flatpak/Foundation runs `29966872082`/`29966872046`/`29966872048` all passed for the
  exact head.
  Release remains `unreleased`; proxy authentication, other clients, human review, signing,
  rollback, stable artifacts, and PR/Issue closure remain open.

## 2026-07-22 — Linux secret custom-header GTK onboarding

Assumption: Linux remains the active implementation scope; the masked secret-header field follows
the existing credential boundary and never restores Secret Service contents into the form.

- l10n `32397a72c267677f04419a5084514f025f94a0bc` adds the three Linux-only messages and regenerates
  the 462-message PO/MO bundle. Linux `e52a43cb361c5a395aa4e8ecd4d8d5252192d384` adds the
  `PasswordEntry`, clears it after Test connection/Connect, preserves only persistent references,
  and routes session-only secret headers through `WorkerCommand` into the existing host-secret
  broker. A focused worker regression proves malformed session header JSON reaches Core validation.
- Local Linux evidence passed `cargo fmt --all -- --check`, all-target locked check, strict all-feature
  Clippy, full demo-provider tests (`159 passed; 3 ignored`), localization key/placeholder audits,
  l10n synchronization, Flatpak metadata validation, and `git diff --check`. The GUI test binary
  remains linker-limited on this host by missing GTK/GDK/Graphene symbols; source compilation passed.
- Linux push Native/Flatpak/Foundation runs `29965156891`/`29965156910`/`29965156886` and PR runs
  `29965159879`/`29965159874`/`29965159952` passed for the exact head. The release remains
  `unreleased`; other clients, human visual/copy/Orca review, signing, rollback, stable artifacts,
  and PR/Issue closure remain open. Central coordination validation `29965562185` passed for the
  synchronized manifest and documentation head.

## 2026-07-22 — Cross-repository completion gap audit

Assumption: Linux remains the active implementation scope for this checkpoint; deterministic
Linux evidence must not be promoted to global acceptance evidence for the other native clients.

- Added [`docs/GAP_ANALYSIS.md`](docs/GAP_ANALYSIS.md), a milestone and mandatory-scenario matrix
  grounded in the current repository heads and release manifest.
- The audit confirms that the release remains `unreleased`: Linux has substantial runtime and CI
  evidence, while cross-client conformance, qualified human accessibility/visual review, physical
  VFS/power-loss evidence, signing, rollback, and stable-release authorization remain open.
- No implementation, compatibility pin, or release artifact is being claimed from an indirect or
  unavailable validation result.

## 2026-07-22 — Linux secret custom-header SecretRef slice

Assumption: secret custom headers use a separate persistent `SecretRef` whose one-shot resolved
value is a bounded JSON object; the existing API credential reference remains independent, and
GTK editing/onboarding for the second secret is a follow-up surface.

- Core `28baaa2f85bb70b4fc6ecc4c07566e7004a659c5` adds schema 24 persistence for
  `ProviderProfile.secret_custom_headers_ref`, resolves the reference through the host secret
  broker, and applies the in-memory JSON only to OpenAI-compatible Chat, Responses, and Azure
  requests. Secret values are never persisted or included in debug output; reserved header names
  remain rejected, while secret values are not copied into non-secret metadata.
- Linux `9d0ffc10a5ee9dd114e40b95db277679969d2593` preserves persistent secret-header references
  across runtime/storage transforms, rejects session-only references during persistence, and
  removes both credential and secret-header Secret Service entries when deleting a profile.
- Local Core evidence passed full workspace tests, strict Clippy, provider/application/storage
  regressions, C/C++ Native SDK smoke, and `git diff --check`. Local Linux evidence passed
  formatting, GUI/all-target check, strict Clippy, `158 passed; 3 ignored` demo-provider tests,
  the secret-reference persistence regression, Flatpak metadata validation, and diff checks.
- Core CI/Fuzz/Native SDK runs `29963034872`/`29963034867`/`29963034863` passed. Linux push
  Native/Flatpak/Foundation runs `29963506897`/`29963506924`/`29963506877` and PR runs
  `29963509821`/`29963509808`/`29963509782` all passed for the exact heads above. Central
  coordination `29963944562` passed on Linux and PowerShell. The separate GTK secret-header
  editor/onboarding, other clients, human review, signing, rollback, and stable release remain
  open.

## 2026-07-22 — ABI 1 provider metadata projection

Assumption: optional `TranslateTextCommand` fields are backward-compatible under protocol 1;
older clients omit them, while native clients validate bounded metadata before any secret request.

- Core `530e6ea75ef3ccba5defd264227fb6dd6802e17a` adds optional non-secret `organization`,
  `project`, and `custom_headers_json` fields, shared credential-shape validation, C ABI forwarding,
  and source-compatible Android wrapper parameters. Domain/protocol/FFI tests, strict Clippy, full
  workspace tests, C/C++ SDK smoke, and reproducible Linux SDK packaging passed.
- Linux `5cf0fcd133c7df823d4c33f934786a1c940670bb` pins the exact Core revision in Native and
  Flatpak inputs and records the direct typed-Rust integration boundary. Local formatting, GUI
  check, strict Clippy, `158 passed; 3 ignored` demo-provider tests, localization audits, l10n
  synchronization, Flatpak metadata, and diff checks passed.
- Core CI/Fuzz/Native SDK `29961301539`/`29961301501`/`29961301583` and Linux push/PR
  Native/Flatpak/Foundation `29961456792`/`29961456832`/`29961456791` and
  `29961459180`/`29961459196`/`29961459185` passed. Other-client integration, human review,
  signing, rollback, and stable release remain open. Central coordination workflows
  `29961593831` and `29961793515` passed the synchronized manifest and documentation head.

## 2026-07-22 — Linux Azure custom-header application wiring

Assumption: custom request headers are optional, bounded, non-secret ProviderProfile metadata;
proxy settings and secret custom headers remain outside this slice. Azure OpenAI may reuse the
same safe header application path, while OpenAI organization/project headers remain limited to
Chat Completions and Responses.

- Core `cf08384c829ca1b95ecfc79d23bc5b0feb3a701f` adds `AzureOpenAiConfig.custom_headers` and
  forwards it through `ProviderManager` into the existing Azure Chat adapter. Provider-level
  and application-level loopback regressions prove safe headers are applied without replacing the
  Azure `api-key`; Core workspace tests and strict all-feature Clippy passed locally.
- l10n `294e593ab2c71b9ab0ea3475c35ebc61bca2bbc6` remains the source-revision-51, 459-message
  bundle. Linux `61a7317746adea35f35a88f948a94f7e8223bac1` pins the exact Core/l10n inputs in
  Native and Flatpak metadata and
  updates the architecture/testing records.
- Linux local evidence passed: GUI all-target check, strict Clippy, locked demo-provider tests
  (`158 passed; 3 ignored`), localization key/visible/placeholder audits, l10n synchronization,
  Flatpak metadata validation, and `git diff --check`.
- Remote Core CI/Fuzz/Native SDK `29958775964`/`29958776018`/`29958776042` and Linux
  Native/Flatpak/Foundation push gates `29959014144`/`29959014132`/`29959014154` plus PR gates
  `29959016415`/`29959016426`/`29959016416` all passed. Central coordination workflow
  `29959537603` passed the synchronized manifest/document head. No release artifact or stable
  promotion is claimed; manual visual/copy/Orca review, live provider interoperability, other
  clients, signing, rollback, and stable-release acceptance remain open; release remains
  `unreleased`.

## 2026-07-22 — Linux provider-project application wiring correction

Assumption: persisted non-secret `project` metadata must reach both OpenAI-compatible Chat
Completions and Responses requests; storage and adapter-level support alone are insufficient.

- Core correction `8717251375290cc3f825cee86d467ab1c60dd508` forwards
  `ProviderProfile.project` through `ProviderManager` into both adapter configurations. Core's
  header-enforced Chat and Responses regressions passed locally; workspace tests and strict
  all-feature Clippy passed. Remote CI/Fuzz/Native SDK runs
  `29953260332`/`29953260318`/`29953260372` passed.
- Linux code head `69b2d4510c51e9f34d7807687e6536ec411b1611` repins Core and retains l10n
  `ec538de57c1edc198fa13d3dfc1de576ee9b2c12`. Local formatting, GUI checks, strict Clippy,
  demo-provider tests (`158 passed; 3 ignored`), l10n synchronization, Flatpak metadata, and
  diff checks passed. Final status head `ec4b32d7dd0efd6d00d27d3a60750307b9c6ff31` passed push
  Native/Flatpak/Foundation `29954097684`/`29954097694`/`29954097748` and pull-request
  Native/Flatpak/Foundation `29954100960`/`29954102119`/`29954100976`. Release remains
  `unreleased`; PR #1 stays Draft/Open and Issue #1 stays Open.

## 2026-07-22 — Linux provider region/account checkpoint

Assumption: `region` and `account_identifier` are optional bounded, non-secret provider metadata;
Core persists and restores them, while Linux keeps them adapter-neutral until provider-specific
semantics are defined.

- Core revision `158ade12cf1e3284d4b8a0883e771dd62abcff97` adds schema 22 migration,
  validation, storage round-trip coverage, and redacted debug presence reporting.
- l10n revision `ec538de57c1edc198fa13d3dfc1de576ee9b2c12` adds six Linux form messages and
  generated resources; the catalog is source revision 50 with 456 messages.
- Linux runtime/packaging head `761a931538fc49c30d759089185cdf21cf2015ab` binds, restores, clears,
  and preserves both fields through Test connection and Connect; status head
  `69fb128b92a0683434d6978c038c7c2ebc48d6ad` records the final gate evidence. Local Linux/Core/l10n
  checks, synchronization, and Flatpak metadata validation passed. Push Native/Flatpak/Foundation
  runs `29952240768`/`29952240852`/`29952240819` and pull-request Native/Flatpak/Foundation runs
  `29952245004`/`29952244151`/`29952244148` all passed. Earlier stale-pin Flatpak runs
  `29951517923`/`29951520086` were superseded; release remains `unreleased`.

## 2026-07-22 — Linux provider project checkpoint

Assumption: `project` is an optional bounded non-secret OpenAI-compatible identifier. Core sends
it only as `OpenAI-Project` for Chat Completions and Responses; other adapters ignore it until a
provider-specific contract is defined.

- Core `17342ba0bf19dd4978707a7875bc7dbe85efae54` adds schema 21 persistence, validation, storage
  round-trip coverage, redacted debug metadata, and OpenAI request-header coverage. Core local
  targeted tests, formatting, and strict Clippy passed; push CI/Fuzz/Native SDK runs
  `29948435070`/`29948435168`/`29948435159` passed.
- l10n `fea84439f035f30b009532b40d7f67a30049846c` adds `label/placeholder/tooltip.provider_project`
  and generated Linux resources; the 450-message bundle passed 26 tests, generation checks,
  build, Localization `29948338448`, and Foundation `29948337065`.
- Linux status head `108cba3e5b1cb128cf77003fc0cb530e822bd7f7` binds/restores/clears the localized
  GTK field, preserves it through runtime/session profiles, and pins the exact Core/l10n/Flatpak
  inputs. Local GUI check, strict Clippy, 158 passing demo-provider tests with 3 ignored, l10n
  sync, Flatpak metadata, and diff checks passed. Push Native/Flatpak/Foundation
  `29949462141`/`29949462126`/`29949462107` and PR Native/Flatpak/Foundation
  `29949468527`/`29949466704`/`29949468689` all passed. Release remains `unreleased` pending
  cross-client compatibility, human review, signing, rollback, and mandatory acceptance evidence.

## 2026-07-22 — Linux provider organization checkpoint

Assumption: `organization` is an optional bounded non-secret OpenAI-compatible routing/account
identifier. Core forwards it only as `OpenAI-Organization` for Chat Completions and Responses;
other adapters ignore it until their own contract is specified.

- Core `1b8737bbad3d1bb6df7cd5c852d51838f72b9ca1` adds schema 20 persistence, validation, storage
  round-trip coverage, and redacted debug metadata; CI/Fuzz/Native SDK runs
  `29945917593`/`29945917625`/`29945917579` passed.
- Linux head `88114a7a08e814e6b75ee0fe0a5814573104fd08` binds the localized GTK field, preserves it
  through saved/runtime profiles, and pins Core/l10n/Flatpak inputs. l10n
  `94438a6a9ff8148cadad605c4760f88110d78984` contains 447 messages; Localization/Foundation runs
  `29945592293`/`29945590422` passed. Linux push Native/Flatpak/Foundation
  `29946828234`/`29946829779`/`29946829000` and PR
  `29946831489`/`29946831590`/`29946832071` are the final status-head gates.
- PR #1 remains Draft/Open/mergeable and Issue #1 remains Open. Human visual/copy/Orca review,
  physical VFS/power-loss, other clients, signing, rollback, and stable release remain open;
  release status stays `unreleased`.

## 2026-07-22 — Linux provider profile notes checkpoint

Assumption: the optional profile note is a bounded non-secret Linux-first slice of the global
ProviderProfile contract; region, proxy, and custom-header metadata remain separate follow-up work.

- Core `072d6b92df875153a60a9d1256ab814891fe775b` adds schema 19 `user_notes` persistence with
  2 KiB and credential-shaped-value validation, redacted debug behavior, and round-trip tests.
- Linux runtime/packaging `eaa9dc3e6bf07222fe3b2da5c078d39e9419b88d` adds the localized GTK Profile
  notes field, restores/clears it with saved/new profiles, and preserves it through runtime session
  transforms; final status head `3c1a4ad5e9f8d8ae613c5b2f8aa447d057212de0` records the evidence.
- l10n `6aa074e48058bb411d09b2783cd27ba415dc7c55` contains 444 messages; Core CI/Fuzz/Native SDK
  runs `29941753725`/`29941753413`/`29941753631` and l10n Localization/Foundation
  `29941762786`/`29941762915` passed. Linux status-head push Native/Flatpak/Foundation
  `29942842016`/`29942841964`/`29942842049` and PR Native/Flatpak/Foundation
  `29942844853`/`29942844878`/`29942848089` passed. Central coordination run
  `29943525316` passed Linux and PowerShell validation for this record.
- Release status remains `unreleased`; PR #1 remains Draft/Open and Issue #1 remains Open. Human
  visual/copy/Orca review, prompted desktop approval, physical VFS/power-loss, other clients,
  signing, rollback authorization, and the remaining acceptance scenarios remain open.

## 2026-07-22 — Linux About compatibility dialog

Assumption: the primary Linux About surface is localized, read-only, and limited to application
and shared-Core compatibility fields; it does not expose endpoints, credentials, model identifiers,
or translation content.

- Linux runtime/packaging head `0d7b3927fb98e461317feaefeb4c806676e6acc0` adds the About action,
  modal, bounded Core semantic version/ABI/protocol display, pure formatter regression, and
  serialized GTK lifecycle fixture. l10n revision `a65a327a8418332e50d9ab302fca24508e7266ef`
  supplies four catalog-backed messages across 441 synchronized messages.
- Local formatting, GUI all-target check, strict locked offline Clippy, demo-provider tests
  (`158 passed; 3 ignored`), localization audits, Flatpak metadata, and `git diff --check` passed.
  The host full-feature GUI link remains limited by missing GTK4/GDK/Graphene symbols; CI supplies
  the executable GUI evidence.
- Final status head `b71e209` passed push Native/Flatpak/Foundation
  `29939876568`/`29939877021`/`29939876501` and PR Native/Flatpak/Foundation
  `29939879474`/`29939879969`/`29939879856`, including About, accessibility, release,
  checksum/SBOM, performance, Flatpak sandbox, and localization checks. The earlier l10n-pin
  failure `29937178278`, GTK mnemonic assertion failure `29937509002`, and stale-pin Flatpak
  failure `29937961470` are superseded by corrected commits `c0a989f`, `b2627ae`, and `0d7b392`.
- Linux PR #1 remains Draft/Open/mergeable with no submitted reviews or unresolved threads;
  Central Issue #1 remains Open. Human visual/copy/Orca review, physical VFS/power-loss evidence,
  signing, rollback authorization, and stable-release acceptance remain open; release status stays
  `unreleased`.

## 2026-07-22 — Linux current-head regression refresh

Assumption: the Linux status-only checkpoint records reproducible evidence for the published
source head without promoting an unsigned artifact or changing the draft PR/release posture.

- Linux runtime/packaging head `4154aaef160a0578624f581063dbd62a29cadb79` and status head
  `3ef694d97caab7de8f98eac177d77ed29fe2a40c` record local `cargo fmt --check`,
  GUI all-target checks, locked offline demo-provider tests (`158 passed; 3 ignored`), strict
  Clippy, l10n synchronization, Flatpak metadata validation, and `git diff --check` results.
- Push Native/Flatpak/Foundation runs `29935017464`/`29935017253`/`29935017458` passed. PR
  Native/Flatpak/Foundation runs `29935021969`/`29935020280`/`29935020571` also passed, including
  the full GTK, portal, accessibility, release, checksum/SBOM, and performance suites.
- Linux PR #1 remains Draft/Open/mergeable; Central Issue #1 remains Open. Human visual/copy/Orca
  review, physical VFS and power-loss evidence, signing, rollback authorization, and stable
  release acceptance remain open; release status stays `unreleased`.

## 2026-07-22 — Android native foundation slice

Assumption: Android is being advanced as a prerelease preparation slice while Linux remains the
priority client; no device or stable-release evidence is implied.

- Android source `afe7a566bac77a16243f70295d17a4d9cab1151f` pins Core
  `8837e59395742b5385af5037aa36a2596af3b025` and l10n
  `3724cc9d436ebdbac3b8ebf0df9bce9af1b41b15`. The native Kotlin/Compose slice includes the
  application-scoped gateway, Keystore credential broker, generated resources, cancellation and
  event-sequence guards, and release adapter source.
- Android workflow `29932649692` (job `88966082464`) passed clean Core AAR build plus metadata,
  checksum, generated-wrapper, and JNI verification; debug/release builds, 16 JVM tests per
  variant, instrumentation compilation, and debug/release lint also passed. The prior run
  `29931908407` failed only on a stale `alpha.1` metadata assertion and was corrected before the
  authoritative run. The status-head rerun `29933216517` (job `88968007647`) also passed.
- Android remains unreleased. Device instrumentation, real Core/provider credential flow, document
  and history workflows, routing/background work, signing, and distribution are not verified.

This is an Android compatibility-preparation checkpoint; it does not change the Linux-first release
posture or imply cross-client acceptance-scenario completion.

## 2026-07-22 — GitHub PR and issue triage

Assumption: draft PRs with green checks remain open while their documented manual, signing, and
release boundaries are incomplete.

- Linux PR #1 remains Draft/Open/mergeable with no submitted reviews or inline review threads; its
  six current-head Native, Flatpak, and Foundation push/PR checks pass.
- macOS PR #1 remains Draft/Open/mergeable with no submitted reviews or inline review threads;
  foundation checks and Native run `29765906044` pass. A triage comment was added at
  [macOS PR comment](https://github.com/getio0909/linguamesh-macos/pull/1#issuecomment-5048104677).
- Central Issue #1 remains Open. Android evidence and the current PR state were recorded in the
  [coordination issue comment](https://github.com/getio0909/linguamesh-project/issues/1#issuecomment-5048106840).
  No merge, force-push, or stable-release action was taken.

## 2026-07-22 — Linux LM Studio-style compatibility checkpoint

Assumption: LM Studio-style local servers satisfy the required generic OpenAI-compatible `/v1/`
Chat Completions contract; the Linux fixture proves protocol behavior without claiming a desktop
installation or GUI integration.

- Linux runtime commit `74e817f07b5d386706999fdc66a21a357286af6c` adds
  `lm_studio_style_openai_compatible_provider_translates_without_secret`, covering model discovery,
  deliberate selection, streaming translation, and credential-free loopback operation.
- Linux packaging/status commit `4154aaef160a0578624f581063dbd62a29cadb79` pins the Flatpak source
  to that runtime checkpoint and records the protocol boundary in `README.md` and `docs/testing.md`.
- Final push Native/Flatpak/Foundation runs `29930209615`/`29930209070`/`29930209231` and PR
  Native/Flatpak/Foundation runs `29930217543`/`29930215088`/`29930217498` all passed. PR #1
  remains Draft/Open/mergeable; Issue #1 remains Open; no merge, release, signing, or stable
  artifact promotion occurred.
- Central synchronization commit `78f4724e6ccd976ded93765723013f02d8d4f847` passed coordination
  workflow `29930966325` on Linux and PowerShell.

## 2026-07-22 — Linux bundled open-source notices checkpoint

Assumption: the bundled `THIRD_PARTY_NOTICES.md` file is the authoritative legal text for this
Linux prerelease surface; rendering it must not fetch network content or expose privileged state.

- Linux runtime commit `909083dee4c436d0f343785a4c95f1cda4207e35` adds a catalog-backed
  **Open-source licenses** action and a focusable, read-only GTK dialog backed by the bundled notice
  file. The regression requires representative `GTK 4`, `LGPL-2.1-or-later`, `MIT`, and `LinguaMesh
  Core` entries; l10n revision `3724cc9d436ebdbac3b8ebf0df9bce9af1b41b15` supplies the action/dialog/
  tooltip labels.
- Linux status/packaging head `c2c1f24c872fdc7a314986376e399ce24788df68` records the corrected
  Flatpak source pin and the superseded stale-hash attempt. Local format, GUI check, localization
  key/placeholder/visible audits, l10n synchronization, Flatpak metadata, and diff checks passed.
- Final push Native/Flatpak/Foundation runs `29928729926`/`29928727256`/`29928727822` and PR
  Native/Flatpak/Foundation runs `29928731491`/`29928731735`/`29928730487` all passed. PR #1
  remains Draft/Open/mergeable; Issue #1 remains Open; no merge, release, signing, or stable
  artifact promotion occurred.
- Central synchronization commit `c9495526d46af65cd800cacd47883a6abd69f017` passed coordination
  workflow `29929324598` on Linux and PowerShell validation jobs.

This is unreleased Linux-first evidence. Human visual/copy/Orca review, end-user Secret Service
approval, remote VFS/power-loss evidence, other clients, signing, rollback authorization, and
stable-release acceptance remain open.

## 2026-07-22 — GitHub Linux-first PR and issue triage

Assumption: an open draft PR with green gates should remain open when the remaining release
boundaries require manual or external evidence.

- Linux PR #1 has no submitted reviews, change requests, or unresolved review threads. Its six
  current-head Native, Flatpak, and Foundation push/PR checks pass, and the PR remains Draft/Open
  with a clean merge state.
- Central Issue #1 remains the single open coordination issue. It records the outstanding manual
  Secret Service/desktop review, physical VFS and power-loss coverage, cross-client work, signing,
  rollback authorization, and stable-release evidence. Triage comments were added to both records;
  coordination workflow `29905044867` passed Linux and PowerShell validation; no merge, force-push,
  or release action was taken.

This checkpoint records GitHub state only and does not promote the unreleased Linux evidence.

## 2026-07-22 — Linux CI evidence integrity verification

Assumption: prerelease evidence is useful only when uploaded checksum and SBOM sidecars are
validated in the same job that produced them; this does not replace signing or release approval.

- Linux workflow head `48ccbca9523fb4c633e3d806c23104c34b5fa623` verifies every `SHA256SUMS` entry
  and parses `SBOM.spdx.json` before Native or Flatpak evidence upload. The Native source archive
  checksum is written with an evidence-directory-relative name.
- Documentation/status head `3bd2c7a0b9cae2e7de55b700e7863b9fcf3805ff` records the initial path
  failures and correction. Final push Native/Flatpak/Foundation `29903015347`/`29903015532`/
  `29903015352` and PR `29903018444`/`29903018422`/`29903018395` all passed; Native completed the
  full GTK, accessibility, release, checksum/SBOM, and performance suites.

This strengthens unreleased Linux Milestone 8 artifact evidence. Sidecars remain unsigned CI
prerelease evidence; signing, distributable promotion, rollback authorization, and stable release
approval remain open. PR #1 remains Draft/Open and Issue #1 remains Open.

## 2026-07-22 — Linux document-report body redaction regression

Assumption: report redaction must be protected against future changes that accidentally serialize
persisted segment bodies, even though the usage field is derived from those lengths.

- Linux runtime regression `89de426c6fcfce77a395fc066017c01a5bb7c247` asserts that translated and
  pending source-segment bodies are absent from the deterministic report, while the local usage JSON
  remains present. Packaging/docs head `b50a69a61436535e196e2d8f5c997f491e726c74` pins this head.
- Local formatting, locked all-target/all-feature check, strict Clippy, localization audits, Flatpak
  metadata, and diff checks passed. Push Native/Flatpak/Foundation `29901156887`/`29901156926`/
  `29901156939` and PR `29901160007`/`29901159988`/`29901160074` all passed; Native completed the
  full GTK, accessibility, release, checksum/SBOM, and performance suites.

This strengthens unreleased Linux Milestone 3/6 report evidence. Provider-reported usage, retry
history, human visual/copy/Orca review, other clients, signed artifacts, rollback authorization, and
stable release approval remain open. PR #1 remains Draft/Open and Issue #1 remains Open.

## 2026-07-22 — Linux document report usage estimate

Assumption: persisted document segments are the only local, non-sensitive source available for a
report usage field; retry attempt history remains unavailable and is not inferred.

- Linux runtime `ae4750beec1d9aa1c2d53c96754a6ca5a4e55c66` serializes a bounded
  `UsageRecord::locally_estimated` JSON object from persisted source and translated segment lengths.
  The report contains only a source marker and token counts; document text, credentials, and paths
  remain excluded, while `retried_count` remains explicit `unknown`.
- Linux packaging/docs head `130dc051e61250ff6c029afedb490f4eea4863b9` pins the runtime and records
  the regression `document_translation_report_is_redacted_and_counts_segments`.
- Local formatting, locked all-target/all-feature check, strict Clippy, localization audits, Flatpak
  metadata, and diff checks passed. Push Native/Flatpak/Foundation `29899915398`/`29899915416`/
  `29899915427` and PR `29899917681`/`29899917650`/`29899917663` all passed; Native completed the
  full GTK, accessibility, release, checksum/SBOM, and performance suites.

This advances unreleased Linux Milestone 3/6 report evidence. Provider-reported usage, retry history,
human visual/copy/Orca review, other clients, signed artifacts, rollback authorization, and stable
release approval remain open. PR #1 remains Draft/Open and Issue #1 remains Open.

## 2026-07-22 — Linux non-local source-alias protection

Assumption: source-preservation checks must reject an identical non-local URI before export even
when the GIO backend cannot expose a local path, inode, or hard-link identity.

- Linux runtime `dc5304c679feedce407981ea67d832979d81157e` adds
  `non_local_source_alias_is_rejected_by_uri_identity`, proving the production guard rejects the
  same SMB URI and allows a distinct sibling URI. Packaging/docs head
  `6de5e2eb89e493c770376e6c55721f429024f651` pins that runtime and documents the boundary.
- Local formatting, locked all-target/all-feature check, strict Clippy, localization audits,
  Flatpak metadata, and diff checks passed. The focused GUI test target remains linker-limited on
  this host; Native CI is authoritative for display-backed tests.
- Push Native/Flatpak/Foundation `29898746678`/`29898746646`/`29898746643` and PR
  `29898749118`/`29898749101`/`29898749056` all passed. Native completed the full GTK, release,
  checksum/SBOM, and performance suites.

This strengthens unreleased Linux Scenario 18 evidence without claiming remote VFS atomicity,
physical power-loss recovery, human visual/copy/Orca review, other clients, signing, rollback
authorization, or stable-release evidence. PR #1 remains Draft/Open and Issue #1 remains Open.

## 2026-07-22 — Linux non-local GIO export policy guard

Assumption: a non-local destination URI must retain the exclusive-create safety boundary because
the Linux client cannot verify a local parent directory or atomic rename-capable VFS.

- Linux runtime `54003159107919f5c9c55b4637aa45054d457c4d` makes the `ExportWriteStrategy` split
  explicit. Local paths with a parent use same-directory temporary finalization; non-local or
  parentless URIs use GIO exclusive creation, and collision selection preserves the URI. The
  `non_local_export_uses_exclusive_create_fallback` regression covers this policy.
- Linux packaging/docs head `e8d301694709ef2737ad92383300018e7c4a5e24` pins the runtime. Local
  formatting, locked all-target/all-feature check, strict Clippy, localization key/placeholder/
  visible audits, Flatpak metadata, and diff checks passed. The focused GUI test target reaches the
  linker but cannot run on this host because installed GTK/GDK/Graphene libraries lack symbols
  required by the current Rust bindings; Native CI is authoritative for the display-backed suite.
- Push Native/Flatpak/Foundation `29897680877`/`29897680772`/`29897680880` and PR
  `29897682852`/`29897682904`/`29897682859` all passed. Native completed the full GTK, release,
  checksum/SBOM, and performance suites.

This narrows unreleased Linux Scenario 18 evidence without claiming remote VFS atomicity, physical
power-loss recovery, human visual/copy/Orca review, other clients, signing, rollback authorization,
or stable-release evidence. PR #1 remains Draft/Open and Issue #1 remains Open.

## 2026-07-22 — Linux Secret Service session-only recovery UX

Assumption: a failed persistent Secret Service write must preserve the user's Remember intent
until an explicit recovery action is selected; closing the warning cannot silently downgrade the
connection to session-only mode.

- Linux runtime test commit `64909399aa55de6b3dc70b69b46e01ae34bc0606` adds the serialized GTK
  fixture `gtk_secret_storage_fallback_dialog_requires_explicit_session_only_action`. It verifies
  the localized warning, focusable recovery controls, explicit Remember clearing on the
  session-only action, and unchanged Remember state when the dialog is closed. The production
  callback requests focus on the credential field; the exact active-window focus owner remains a
  window-manager concern.
- Linux status/docs head `804c72ac39bcfa1bdc4ba0127c9352db3bb2f396` records the evidence and pins
  Flatpak to the runtime lineage. Local formatting, locked all-target check, strict Clippy, three
  localization audits, Flatpak metadata, and diff checks passed; `xvfb-run` is unavailable on the
  development host, so the display-backed fixture is CI evidence.
- Push Native/Flatpak/Foundation runs `29896626177`/`29896626188`/`29896626170` and PR
  Native/Flatpak/Foundation runs `29896629236`/`29896629228`/`29896629219` all passed. Native
  executed the exact fixture and the complete GTK, Secret Service, accessibility, release, and
  evidence suites.

This closes the automatable Linux session-only recovery UX boundary without claiming real end-user
Secret Service prompt approval or visual review. Human translated-copy/visual/Orca review,
non-local VFS and power-loss evidence, other clients, signing, rollback authorization, and stable
release remain open; release status is `unreleased`.

## 2026-07-22 — Linux source-level visible-string gettext coverage

Assumption: source-level gettext coverage is a reproducible CI gate, while translated-copy, plural,
and visual review remain human acceptance boundaries.

- Linux head `31f3a874918aaf867b8d2434385157bff4a62877` passes all three dependency-free audits:
  `check-localization-keys.py` finds 390 catalog-backed source keys,
  `check-localization-placeholders.py` checks 448 literal fallback calls, and
  `check-visible-localization.py` finds no non-empty hard-coded GTK strings across `src/**/*.rs`
  (three intentional empty/reset call sites).
- The generated official and pseudo-locale catalogs remain pinned to l10n
  `88765d3358450ccfac12f396caf5290230a83577`; the existing runtime localization suite and Native
  accessibility fixtures provide the corresponding CI evidence. This closes the source-level
  visible-string gap without claiming human translated-copy or plural quality.

Source-level Linux gettext coverage is now verified for the unreleased checkpoint. Human translated
copy, plural, visual/Orca review, other clients, signed artifacts, rollback authorization, and
stable release approval remain open; release status is `unreleased`.

## 2026-07-22 — Linux atomic export finalization

Assumption: the canonical document pipeline's temporary-output and atomic-finalization steps apply
to every local user-visible export, while non-local URI destinations retain an exclusive-create
fallback because GIO cannot provide a same-directory local rename there.

- Runtime commit `6e6bc31c7d9d584e9357d272f55132bd02ee367d` writes local exports to a same-directory
  UUID temporary file, closes the stream, and finalizes with GIO `move_async` and
  `FileCopyFlags::NONE`; a destination occupied during the race remains unchanged and failed moves
  asynchronously delete the temporary artifact. Non-local URIs continue through the exclusive
  create/write/close helper. The shared path covers translated output, document reports, glossary
  CSV, routing-profile JSON, translation-history TSV, and translation-memory TSV.
- The ignored GTK fixture `gtk_atomic_output_writer_never_replaces_existing_file` verifies occupied
  destinations preserve their sentinel and leave no temporary artifact, while a new destination is
  created successfully. Local formatting, locked all-target/all-feature checks, strict Clippy,
  demo-provider tests (`157 passed; 3 ignored`), Flatpak metadata, and diff checks passed; full GTK
  linking remains unavailable on this host.
- Packaging/workflow commit `31f3a874918aaf867b8d2434385157bff4a62877` updates the Flatpak source
  pin and dedicated Native fixture name. Push Native/Flatpak/Foundation runs
  `29894536354`/`29894536297`/`29894536351` and PR runs
  `29894538235`/`29894538243`/`29894538211` all passed; Native completed the exact fixture, full
  GTK suite, release build, performance baseline, and checksum/SBOM evidence.

This closes the Linux temporary-output/atomic-finalization evidence for unreleased Scenario 18.
Human visual/copy/Orca review, non-local VFS atomicity, other clients, signed artifacts, rollback
authorization, and stable release approval remain open; release status is `unreleased`.

## 2026-07-22 — Linux auxiliary export overwrite protection

Assumption: every user-visible export must fail closed on an occupied destination, not only
translated document and report output.

- Runtime commit `c11e80bbb69b869b1d021d07e1f97247cf0ae7b4` routes glossary CSV, routing-profile
  JSON, translation-history TSV, and translation-memory TSV exports through the same GIO exclusive
  create, asynchronous write, and close helper used by translated output and reports. No
  `replace_contents_bytes_async` export call sites remain.
- The ignored GTK fixture `gtk_exclusive_output_writer_never_replaces_existing_file` covers both
  occupied-file failure with preserved sentinel contents and successful creation of a new file.
  Local formatting, locked all-target/all-feature checks, strict Clippy, demo-provider tests
  (`157 passed; 3 ignored`), localization audits, Flatpak metadata, diff checks, and static audit
  passed; full GTK linking remains unavailable on this host.
- Packaging/docs commit `c7afb4c351b5a092318dda3ea93f1a1c1043c097` pins Flatpak and documents all
  protected export paths. Code-head push Native/Flatpak/Foundation runs
  `29892239963`/`29892239946`/`29892239987` and PR runs
  `29892242173`/`29892242176`/`29892242188` all passed; Native executed the exclusive fixture and
  completed release, checksum/SBOM, performance, and accessibility suites. Final status head
  `831fcf276010419359fb7bf983be1d47de8d3767` then passed push Native/Flatpak/Foundation
  `29892566477`/`29892566480`/`29892566481` and PR
  `29892568592`/`29892568596`/`29892568579`.

This closes the Linux user-visible export overwrite call-site gap for unreleased Scenario 18
evidence. Human visual/copy/Orca review, other clients, signed artifacts, rollback authorization,
and stable release approval remain open; release status is `unreleased`.

## 2026-07-22 — Linux exclusive translation output writer

Assumption: collision-safe output naming must remain safe if another process creates the selected
destination after the deterministic sibling-path check but before the asynchronous write starts.

- Runtime commit `a48dafe259b794211ed2d1bec0a858b647dcd3d3` replaces export replacement writes for
  plain text, document reports, and binary document outputs with GIO exclusive creation,
  asynchronous `write_all`, and explicit stream close. A race that occupies the path now reports a
  localized save error while leaving the existing file unchanged; no overwrite fallback is used.
- The ignored GTK regression `gtk_exclusive_output_writer_never_replaces_existing_file` proves
  the occupied-file boundary and preserves the sentinel contents. Native CI runs it as a dedicated
  serialized DBus/Xvfb step. Local formatting, locked all-target/all-feature checks, strict Clippy,
  demo-provider tests (`157 passed; 3 ignored`), Flatpak metadata, and diff checks passed; the full
  GTK binary remains linker-limited on this host by incomplete GTK/GDK/Graphene symbols.
- Packaging/workflow commit `95a47ef6dcec45bb55feb967076cc2bfcb5f5919` pins the runtime input.
  Push Native/Flatpak/Foundation runs `29891347377`/`29891347329`/`29891347335` and PR
  Native/Flatpak/Foundation runs `29891349140`/`29891349152`/`29891349162` all passed; Native
  completed the exclusive fixture, full GTK suite, release build, checksum/SBOM, and performance
  baseline.

This strengthens unreleased Linux Milestones 3 and 6 export safety. Human visual/copy/Orca review,
other clients, signed artifacts, rollback authorization, and stable release approval remain open;
release status is `unreleased`.

## 2026-07-22 — Linux collision-safe translation output naming

Assumption: the output contract applies to plain-text and persisted document exports, while the
report export uses the same source/target stem with a `.report.tsv` suffix.

- Runtime commits `c8ff5be178d4f85709d8f6e4efe991dd180b3837` and
  `193ca90b94302f7ae42e2b919576d2ffd68f0aae` derive
  `<original-base-name>.<target-bcp47-tag>.<extension>`, sanitize control characters and path
  separators, carry the persisted document target locale through the worker event, and expose a
  stable report output identifier with `und` fallback. Existing local destinations choose the
  first deterministic `-1`, `-2`, ... sibling path instead of replacing any file; focused tests
  cover multi-dot stems, hidden-file fallback, invalid names, unknown locales, and occupied
  collision slots.
- Linux status/packaging head `56c71b21aedcefbf91ad64c85672d5436ca91a6f` records the evidence.
  Local formatting, locked checks, strict Clippy, demo-provider tests (`157 passed; 3 ignored`),
  localization audits, l10n synchronization at `88765d3358450ccfac12f396caf5290230a83577`,
  Flatpak metadata, and diff checks passed. The full-feature binary target is linker-limited on
  this host by incomplete GTK/GDK/Graphene symbols; Native CI is authoritative for those fixtures.
  Final push Native/Flatpak/Foundation runs `29890568417`/`29890568416`/`29890568445` and PR runs
  `29890570161`/`29890570133`/`29890570165` all passed, with Native completing the full GTK,
  release-build, checksum/SBOM, and performance-baseline suite.

This advances unreleased Linux Milestones 3 and 6. Human visual/copy/Orca review, other clients,
signed artifacts, rollback authorization, and stable release approval remain open; release status
is `unreleased`.

## 2026-07-22 — Linux GTK document report action fixture

Assumption: every persisted queue row must expose the same safe report action at the production
GTK boundary, not only through the report-builder unit test.

- Linux runtime/docs commit `e28981870563970549ca88c4faa691451ed710e7` extends
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` to require exactly one focusable
  **Export translation report** button per pending, paused, and cancelled row, with the
  catalog-backed redacted-TSV tooltip. Formatting commit `07208e1b09e42ecec4a184efa69336570f6243dc`
  and Flatpak pin `ad3012fd0fdf34e81e6cc6bb2e4571e94a324dfc` keep the tested source synchronized.
- Local formatting, locked all-target/all-feature checks, strict Clippy, demo-provider tests
  (`157 passed; 3 ignored`), localization audits, l10n synchronization at
  `88765d3358450ccfac12f396caf5290230a83577`, Flatpak metadata, and diff checks passed. The full
  GTK fixture binary cannot link on this host because installed GTK/GDK/Graphene symbols are
  incomplete; Native CI is authoritative. Final head `ad3012fd0fdf34e81e6cc6bb2e4571e94a324dfc`
  passed push Native/Flatpak/Foundation `29889128173`/`29889128185`/`29889128176` and PR
  Native/Flatpak/Foundation `29889129723`/`29889129750`/`29889129727`; Native completed the full
  fixture, release-build, checksum/SBOM, and performance-baseline suite.

This strengthens unreleased Linux Milestones 3 and 6 report evidence. Native chooser interaction,
visual/copy/Orca review, physical interruption behavior, other clients, signed artifacts, rollback
authorization, and stable release approval remain open; release status is `unreleased`.

## 2026-07-22 — Linux document translation report export

Assumption: the first report surface is a Linux-only, redacted TSV snapshot; persisted
document jobs do not retain provider usage or retry counts, so those fields stay explicitly
unknown instead of being inferred.

- Linux runtime commit `cc5beeea530e500ee2d42b6d05d26dc34a26c7ab` adds a localized Export
  translation report action to each production Document jobs row. The deterministic report
  includes stable identifiers, locales, provider/model, routing/preset/glossary metadata,
  application/Core/prompt versions, segment counts, warnings, state, and Unix timestamps while
  excluding credentials, source/translated text, and local paths; source-alias protection prevents
  overwriting the imported source file.
- Flatpak/workflow commits `4407ce947f86af070f986e4c4ee0fee6b2305683` and
  `c14760c4c14fe26681c2f11a22a5dd8e9af6b1e9` pin the tested Linux/l10n inputs. Canonical l10n
  revision `88765d3358450ccfac12f396caf5290230a83577` passed its full 26-test/generated-resource
  validation. Local Linux formatting, locked all-target/all-feature checks, strict Clippy,
  demo-provider tests (`157 passed; 3 ignored`), localization audits, Flatpak metadata, and diff
  checks passed. After correcting the stale workflow pin (old Native run `29887678331`), push
  Native/Flatpak/Foundation runs `29887890227`/`29887890202`/`29887890226` and PR runs
  `29887892891`/`29887892948`/`29887892894` all passed; Native completed the full GTK fixture,
  release-build, checksum/SBOM, and performance-baseline suite.

This advances the Linux document-workspace report requirement for Milestone 3. Final status head
`a3af4c40a01db6256e5549cdd08ecf78be3ad1d1` passed push Native/Flatpak/Foundation runs
`29888261417`/`29888261423`/`29888261426` and PR runs `29888264002`/`29888263976`/`29888263981`.
Output identifiers remain `<not-exported>` until an output is persisted. Human visual/copy/Orca
review, physical interruption behavior, other clients, signed artifacts, rollback authorization,
and stable release approval remain open; release status is `unreleased`.

## 2026-07-22 — Linux GTK pending document-job Pause action

Assumption: a pending row in the production document queue must dispatch Pause for that exact
snapshot, not merely expose a visually identical button or select a different job.

- Linux runtime commit `8c05797011a04cdc11988cfbe9c35c2d05d2269b` extends
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` so pending, paused, and cancelled
  snapshots each expose their single queue action. The fixture activates `Pause document` for
  `gtk-queue-first` and proves the pending job remains selected with `Pending` state while the
  dialog closes after sending the command.
- Linux packaging pin commit `4bc6da51ac6510503e41234bfb3eea5e794fe1e7` pins Flatpak to the
  runtime head. Local formatting, locked all-target/all-feature checks, strict Clippy,
  demo-provider tests (`157 passed; 3 ignored`), localization audits, l10n synchronization,
  Flatpak metadata, and diff checks passed.
- Code-head push/PR Native/Flatpak/Foundation runs
  `29885792891`/`29885792900`/`29885792902` and `29885795224`/`29885795226`/`29885795242` all
  passed. Final Linux status/docs head is `3fa224a1047a30826ce1c62b45bc8138a02b6e8f`; its
  push/PR Native/Flatpak/Foundation runs `29886174310`/`29886174217`/`29886174265` and
  `29886176680`/`29886176559`/`29886176546` also passed, with Native executing the exact queue
  fixture and reporting `1 passed`.

This advances unreleased Linux document queue evidence for Milestones 3 and 6. Human visual/copy/
Orca review, physical interruption behavior, other clients, signed artifacts, rollback authorization,
and stable release approval remain open.

## 2026-07-22 — Linux GTK cancelled document-job Retry action

Assumption: a cancelled row in the production document queue must dispatch Retry for that exact
snapshot, not merely expose a visually identical button or select a different job.

- Linux runtime commit `819eff7cff79b8e6514120d550f72658ff276bf9` extends
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` with a cancelled third snapshot. The
  fixture verifies the localized three-file count, requires exactly one `Retry document` action,
  activates it, and proves `gtk-queue-cancelled` remains selected with `Cancelled` state while the
  dialog closes after sending the command.
- Linux packaging/docs commit `8fae49ee451c5df22ec766eabe14c1ad0dc71ee2` pins Flatpak to the
  runtime head and documents the Retry assertion. Local formatting, locked all-target/all-feature
  checks, strict Clippy, demo-provider tests (`157 passed; 3 ignored`), localization audits, l10n
  synchronization, Flatpak metadata, and diff checks passed.
- Final Linux status/docs head is `5432b021d3073a703d3d8824dd3fbd00118ba66d`. Final Linux
  status-head push Native/Flatpak/Foundation runs
  `29884616494`/`29884616511`/`29884616504`; PR runs
  `29884618885`/`29884618826`/`29884618821`; all passed. Native executed the exact serialized queue
  fixture and reported `1 passed`.

This advances unreleased Linux document queue evidence for Milestones 3 and 6. Human visual/copy/
Orca review, physical interruption behavior, other clients, signed artifacts, rollback authorization,
and stable release approval remain open.

## 2026-07-22 — Linux GTK paused document-job Resume action

Assumption: a paused row in the production document queue must dispatch Resume for that exact
snapshot, not merely expose a visually identical button or select a different job.

- Linux runtime `7b92bd43915ebefde3e29463252aacb94d064691` extends
  `gtk_document_jobs_dialog_selects_between_multiple_jobs`: after selecting the paused second
  snapshot, the fixture reopens the production queue, requires exactly one `Resume document`
  action, activates it, and verifies the same job ID/state remains selected while the dialog closes
  after sending the command.
- Packaging/docs `ea5bf4768a9f8b40fd04fbc929d8ea788ead32bc` pins Flatpak to the runtime head and
  documents the Resume assertion. Final Linux status head is
  `755ed9a87ee3034c282ef655915a8ad0ec4fe941`. Local formatting, locked checks, strict Clippy,
  157-pass demo-provider tests (3 ignored), localization audits, l10n synchronization, Flatpak
  metadata, and diff checks passed. Final status-head push/PR Native, Flatpak, and Foundation runs
  `29883868226`/`29883868326`/`29883868256` and `29883870536`/`29883870487`/`29883870484` all
  passed; Native reports the exact queue fixture as `1 passed`.

This advances unreleased Linux document queue evidence for Milestones 3 and 6. Human visual/copy/
Orca review, physical interruption behavior, other clients, signed artifacts, rollback authorization,
and stable release approval remain open.

## 2026-07-22 — Linux GTK multi-document queue selection boundary

Assumption: the production document-jobs dialog must expose each persisted job's identity and
source metadata, and selecting one row must return that exact snapshot without cross-row state.

- Linux runtime commit `c652232196f09ee9a2cbf69f7eaa9e01ca7672e7` adds the serialized ignored
  fixture `gtk_document_jobs_dialog_selects_between_multiple_jobs`. It creates two persisted
  snapshots (`first.txt` pending and `second.md` paused), opens the production dialog, asserts the
  `2 files` summary and both filenames, clicks the second Select action, and verifies the selected
  job ID, paused state, and source text before shutdown.
- Packaging/CI commit `e21cd11e5d3518a8248bf95712cad55c6bef57ec` adds the dedicated DBus/Xvfb
  Native step so this fixture is not merely ignored in the general test suite. Local formatting,
  locked all-target/all-feature checks, strict Clippy, 157-pass demo-provider tests (3 ignored),
  localization audits, l10n sync, Flatpak metadata, and diff checks passed. Push/PR Native,
  Flatpak, and Foundation runs `29882794626`/`29882794606`/`29882794617` and
  `29882796272`/`29882796303`/`29882796264` all passed; Native executed the exact fixture
  successfully.

This advances unreleased Linux queue evidence for Milestones 3 and 6. Human visual/copy/Orca
review, other clients, signed artifacts, rollback authorization, and stable release remain open.

## 2026-07-22 — Linux GTK OOXML macro and signature import boundary

Assumption: production GTK/GIO import must reject unsupported OOXML macro and digital-signature
parts before document-job creation, not only through Core unit coverage.

- Linux commit `ed1d419e4c13e614d5470f500e5d0736390449c6` extends
  `gtk_malicious_archive_import_fails_closed_before_document_job` with `word/vbaProject.bin` and
  `_xmlsignatures/sig1.xml` DOCX fixtures alongside traversal and suspicious compression. Every
  case requires a fixed import error, no document-job ID, an empty source editor, and no forbidden
  extracted path. The Flatpak source pin is synchronized to this commit.
- Local formatting, locked all-target/all-feature checks, strict Clippy, 157-pass demo-provider
  tests (3 ignored), localization audits, l10n sync, Flatpak metadata, and diff checks passed.
  Display-backed execution is host-limited and CI-authoritative.
- Final push Native/Flatpak/Foundation runs `29881709701`/`29881709736`/`29881709671` and PR
  runs `29881711799`/`29881711798`/`29881711800` all passed; Native ran the exact fixture.

This advances unreleased Linux Scenario 15/Milestone 6 evidence. Human macro/signature, visual,
copy, Orca, other-client, signing, rollback, and stable-release review remain open.

## 2026-07-22 — Linux GTK malicious archive import boundary

Assumption: Scenario 15 requires the production asynchronous GTK/GIO import path to reject
traversal and suspicious compression while keeping a fixed error visible after UI refresh and before
any document job or extracted content is created.

- Linux runtime code `acb15c2b17bc58f311a31edd57f8793fb7f90e7f` adds
  `gtk_malicious_archive_import_fails_closed_before_document_job`. The serialized fixture drives
  DOCX archives containing `../outside.txt` and a highly compressed repetitive entry through
  `load_source_file`, and verifies fixed rejection, no document-job ID, an empty source editor, and
  no forbidden extracted filename. The loader fix preserves the visible error instead of clearing it
  during the final UI refresh.
- Local formatting, locked all-target/all-feature checks, strict Clippy, no-default/demo-provider
  suites (`83 passed; 1 ignored` and `157 passed; 3 ignored`), localization audits, l10n sync,
  Flatpak metadata, diff checks, and cargo-deny passed. The host lacks `xvfb-run` and matching GTK
  development symbols, so display-backed execution is CI-authoritative.
- Final Linux status/docs head `2900f19c1fe70b184e2d5fd2de1c40627c26a80f` passed push
  Native/Flatpak/Foundation `29880789834`/`29880789824`/`29880789819` and PR
  Native/Flatpak/Foundation `29880792162`/`29880792135`/`29880792142`; Native reports the exact
  malicious-archive fixture successful.

This advances unreleased Linux evidence for Scenario 15. Macro/signature review, human desktop and
Orca review, other clients, signed artifacts, rollback authorization, and stable release remain
open.

## 2026-07-21 — Linux GTK Incognito privacy boundary

Assumption: Scenario 14 is evidenced at the production GTK boundary when a standard translation
creates local history and translation-memory rows, an identical Incognito request reaches the
provider again, and the reopened database contains no additional private rows.

- Linux runtime code `47bbe58bf16ecac11976828575c5964f511198fb` adds the serialized fixture
  `gtk_incognito_translation_bypasses_memory_and_persistence`. It drives the GTK Incognito toggle,
  authenticated connection, deliberate model selection, standard Translate action, repeated
  Incognito Translate action, and direct Storage reopen assertions. The provider request counter
  increases for the private repeat; history and translation-memory counts remain exactly one each.
- Final Linux status/docs head `ca130eec9643c4bf08d9a5877a921d26ef20e9cb` pins the Flatpak runtime
  source and records local formatting, all-target/all-feature checks, strict Clippy, no-default and
  demo-provider suites (`83 passed; 1 ignored` and `157 passed; 3 ignored`), localization audits,
  l10n synchronization, Flatpak metadata, and diff checks.
- Final status-head push Native/Flatpak/Foundation runs `29878453604`/`29878453311`/`29878453609`
  and PR runs `29878456310`/`29878456278`/`29878456340` passed; Native explicitly ran the GTK
  Incognito fixture. Release status remains `unreleased`.

This advances unreleased Linux evidence for mandatory Scenario 14. Human privacy review, other
clients, signed artifacts, rollback authorization, and stable-release approval remain open.

## 2026-07-21 — Linux Incognito translation-memory isolation

Assumption: Incognito means a request must neither consult existing translation memory nor write
history or memory, while standard translation keeps the existing persistence behavior.

- Linux runtime and packaging head `0203b2183ee79d3ba4d836cddeb714ad64091231` guards the worker's
  translation-memory lookup with the request privacy mode. The regression
  `incognito_translation_bypasses_existing_memory_and_persists_nothing` performs a standard
  translation, repeats the same source in Incognito, proves the provider receives a second request,
  and reopens the database to confirm exactly one history row and one memory row.
- Local formatting, locked all-target/all-feature checks, strict Clippy, no-default/demo-provider
  suites (`83 passed; 1 ignored` and `160 passed; 3 ignored`), localization key/placeholder/visible
  audits, l10n synchronization, Flatpak metadata, and diff checks passed.
- Push Native/Flatpak/Foundation runs `29876038029`/`29876038007`/`29876038060` and PR runs
  `29876035413`/`29876035445`/`29876035433` passed. Release status remains `unreleased`.

This advances unreleased Linux evidence for mandatory Scenario 14. Human privacy review, other
clients, signed artifacts, rollback authorization, and stable-release approval remain open.

## 2026-07-21 — Linux GTK interrupted document-job restart/resume lifecycle

Assumption: Linux Scenario 12 is evidenced at the production GTK boundary when a persisted
multi-segment document pauses after committed progress, a second worker restores the same database,
and Resume completes only the remaining segments without duplicating output.

- Runtime code `ca67c8b6b50cd79700c6be505bd7a950c73ed870` adds the serialized ignored fixture
  `gtk_interrupted_document_job_restores_and_resumes`. It drives real GTK Translate/Pause controls
  on a two-segment TXT job, verifies one committed segment and an unchanged source buffer, shuts
  down the first worker, restores the private database in a second GTK worker, reconnects the same
  non-secret provider identity with a fresh session credential, and completes the remaining segment
  through the production Resume action. Linux final evidence head
  `1be587b2d910690cb3fdc07c0342fd0bb9c55ef4` keeps the Flatpak source pin synchronized.
- Local formatting, all-target/all-feature check, strict Clippy, no-default/demo-provider tests
  (`83 passed; 1 ignored` and `156 passed; 3 ignored`), localization key/placeholder/visible audits,
  l10n synchronization, Flatpak metadata, and diff checks passed. Display-backed execution is
  CI-authoritative on this host.
- Code-head push/PR Native, Flatpak, and Foundation gates
  `29873822240`/`29873822363`/`29873822338` and `29873825162`/`29873825141`/`29873825142` passed.
  Evidence-head gates `29874337974`/`29874337743`/`29874337869` and
  `29874339972`/`29874339969`/`29874339977` passed. Final documentation-head gates
  `29874798901`/`29874798855`/`29874798868` and
  `29874801196`/`29874801209`/`29874801193` passed; Native explicitly reports the exact fixture
  successful.

This advances unreleased Linux evidence for mandatory Scenario 12. Physical power-loss recovery,
live-provider interoperability, human visual/copy/Orca review, other clients, signing, rollback,
and stable-release approval remain open.

## 2026-07-21 — Linux GTK glossary and protected-span lifecycle

Assumption: Linux Scenario 9 is evidenced at the production GTK boundary when a request-level
glossary entry protects a source term before dispatch, the provider receives only the opaque
protected marker, and the reducer restores the glossary translation even when that marker is split
across streamed deltas.

- Linux runtime `aa0e0206c20e325bf0dd340dab039eea400a9ab0` adds the serialized ignored fixture
  `gtk_glossary_and_protected_terms_preserve_translation`. It enters a real glossary mapping through
  the GTK form, inspects the loopback request to confirm `LinguaMesh` is replaced by a protected
  marker, streams that marker in two fragments, and verifies the completed output is `你好，凌瓦网！`.
  Flatpak source pin `aa0e0206c20e325bf0dd340dab039eea400a9ab0` remains synchronized in final
  Linux status/docs head `b6f4fbebc9daf928edccf05ee4b401be2a945658`.
- Local Linux `cargo test --all-targets --features demo-provider --locked` passed (`156 passed; 3
  ignored`), alongside formatting, all-target/all-feature checks, strict Clippy, no-default tests
  (`83 passed; 1 ignored`), localization audits, l10n synchronization, Flatpak metadata, and diff
  checks. Display-backed execution remains CI-authoritative on the host.
- Code-head push Native/Flatpak/Foundation gates `29868747478`/`29868747474`/`29868747461` and PR
  gates `29868750361`/`29868750281`/`29868750341` passed. Final status-head push
  Native/Flatpak/Foundation gates `29869815247`/`29869815332`/`29869815462` and PR gates
  `29869819086`/`29869818840`/`29869819166` also passed; Native explicitly reports the exact
  serialized glossary/protected-span fixture successful.

This advances unreleased Linux evidence for mandatory Scenario 9. Provider-specific glossary
semantics, human visual/copy/Orca review, other clients, signed artifacts, rollback authorization,
and stable release remain open.

## 2026-07-21 — Linux GTK translation cancellation lifecycle

Assumption: Linux Scenario 6 is evidenced at the GTK boundary when the production Stop action
cancels a streamed request after a confirmed delta, preserves that partial output, reaches the
`Cancelled` state without an automatic retry, and leaves Retry available for an explicit action.

- Linux runtime `2730a24bc67f9c424b3cce845ced895d9f2710b2` adds the serialized
  `gtk_cancel_translation_preserves_partial_output` fixture. It drives the production GTK form
  against the bearer-token loopback provider, selects `fake-slow-translator`, clicks Stop after
  the first `你好` delta, and verifies retained output, `Cancelled`, disabled Stop, enabled Retry,
  and no error. Packaging pin `2730a24bc67f9c424b3cce845ced895d9f2710b2` is synchronized at
  final Linux status head `5e74f79a2b2af049b84c010632aa979a064f9b1c`.
- Linux local formatting, all-target/all-feature check, strict Clippy, no-default/demo-provider
  suites (`83/1` and `156/3` ignored), localization audits, l10n sync, Flatpak metadata, and diff
  checks passed. The host's installed GTK symbols are older than the Rust bindings, so display-
  backed execution remains CI-authoritative.
- Final code-head push Native/Flatpak/Foundation `29866519789`/`29866519798`/`29866519885` and
  PR gates `29866523643`/`29866523637`/`29866523644` passed. Final status-head push
  Native/Flatpak/Foundation `29867517962`/`29867519068`/`29867518348` and PR gates
  `29867521905`/`29867521950`/`29867521920` also passed.

This advances unreleased Linux evidence for mandatory Scenario 6. Physical provider transport
cancellation, human visual/copy/Orca review, other clients, signed artifacts, rollback, and
stable release remain open.

## 2026-07-21 — Linux GTK provider connection-test lifecycle

Assumption: the explicit GTK Test connection action must validate a provider without committing an
active session, clear entered credentials immediately, and preserve typed authentication errors for
localized redacted presentation.

- Linux runtime code `2d5f625067fb84af260b664e5e2d9c027095e6d8` adds the serialized ignored fixture
  `gtk_connection_test_reports_models_and_redacts_credential`. It drives the production GTK button
  through a bearer-token loopback provider, reports a bounded discovered-model count, clears the
  credential field, and then rejects a wrong canary without exposing the canary or HTTP 401/403
  details. `ConnectionTestRejected` now retains the full `TranslationError` category instead of
  collapsing it into an internal client error.
- Linux final status head `ef83869df4901adbdcb3baaa7ade27c8ad685dd3` records local formatting,
  all-target/all-feature check, strict Clippy, no-default/demo-provider suites (`83/1` and `156/3`
  ignored), localization audits, l10n sync, Flatpak metadata, and diff checks. The host cannot
  link the GTK test binary against its older installed GTK symbols; display-backed execution is
  CI-authoritative.
- Final push Native/Flatpak/Foundation gates `29864753592`/`29864753479`/`29864753370` and PR
  gates `29864757307`/`29864757739`/`29864757412` passed. Native explicitly ran the new provider
  connection-test fixture before the remaining accessibility and release matrix.

This advances unreleased Linux Provider Hub and Scenario 8 evidence. Live-provider interoperability,
human visual/copy/Orca review, other clients, signed artifacts, rollback authorization, and stable
release remain open.

## 2026-07-21 — Linux GTK offline session preservation

Assumption: Linux Scenario 17 needs the real GTK connection lifecycle to preserve a confirmed
provider/model session after an unavailable-provider attempt; worker-only offline tests do not
cover that presentation boundary.

- Linux code `3242133acbf77a7e72374ab680a83f4ff676ff0c` adds the ignored serialized fixture
  `gtk_offline_connection_failure_preserves_confirmed_session`. It connects the deterministic
  bearer-token provider, selects `fake-translator`, captures the active provider/models/source,
  releases a loopback port, and submits a second connection attempt with an unavailable endpoint.
  The fixture asserts the credential field is cleared, the localized network `Alert` contains no
  canary, status returns to Ready, and the confirmed provider, model, and source text remain.
- Local Linux formatting, all-target/all-feature check, no-default/demo-provider suites
  (`83 passed; 1 ignored` and `156 passed; 3 ignored`), localization audits, Flatpak metadata, and
  diff checks passed. The host lacks `xvfb-run`, so the display-backed fixture is CI-authoritative.
- Final Linux status head `97c1f6f9d4e2af9e19193e606b2449dc66161247` passed push
  Native/Flatpak/Foundation gates `29861846026`/`29861846105`/`29861845971` and PR gates
  `29861848727`/`29861848911`/`29861848713`. Native explicitly ran the exact offline GTK fixture
  successfully before the remaining GTK, Wayland, AT-SPI, Orca, portal, and release matrix.

This advances unreleased Linux evidence for Scenario 17. Human offline/visual/copy/Orca review,
physical outage simulation, other clients, live-provider interoperability, signing, rollback, and
stable release remain open.

## 2026-07-21 — Linux GTK authentication-failure presentation

Assumption: Linux Scenario 8 needs evidence across the actual GTK Connect button, worker rejection
event, localized alert rendering, and credential redaction; a pure model test is not sufficient for
that boundary.

- Linux code `bd3487461e725ec5718636b3c2057aa1edd3315b` adds the ignored serialized fixture
  `gtk_authentication_failure_shows_localized_redacted_error`. It starts the deterministic bearer-
  token provider, enters a wrong session credential through the production form, waits for the
  401/403 worker rejection, switches to Simplified Chinese, and asserts the visible `Alert` has
  catalog-backed actionable copy while excluding the wrong credential and backend status numbers.
  The credential field is cleared immediately and no active provider is committed after failure.
- Local Linux formatting, all-target/all-feature check, strict Clippy, no-default/demo-provider
  suites (`83 passed; 1 ignored` and `156 passed; 3 ignored`), localization audits, synchronization,
  Flatpak metadata, and diff checks passed. The display-backed fixture remains CI-authoritative on
  this host.
- Linux packaging/docs/status head `9e45b2a8b721cf0f316d94009d66390677dac480` passed push
  Native/Flatpak/Foundation gates `29859661736`/`29859661796`/`29859661669` and PR gates
  `29859664966`/`29859664991`/`29859665005`. Native explicitly ran the exact authentication-
  failure GTK fixture before the remaining GTK, Wayland, AT-SPI, Orca, Secret Service, portal,
  and release-evidence matrix.

This advances unreleased Linux evidence for Scenario 8. Human translated-copy/visual/Orca review,
live-provider interoperability, other clients, signing, rollback, and stable release remain open.

## 2026-07-21 — Linux actionable authentication-error localization

Assumption: provider HTTP 401/403 responses are authentication failures; Linux should replace
backend status detail with catalog-backed retry guidance before GTK renders the error, without
exposing credentials or backend status numbers.

- Linux code `c66f6df42fd03c67b3991c5b7fb4229dccadce97` maps HTTP 401/403 messages to
  `error.authentication`; `http_authentication_failures_use_localized_actionable_copy` verifies
  Simplified Chinese `身份验证: 请检查提供商凭据，然后重试。` for both statuses and confirms the
  numeric status detail is absent. The corrected Flatpak source/status head is
  `5a18ba9bc04b2430b7d07a30fdb2c64d82df8a26`.
- Local Linux no-default/demo-provider suites passed (`83 passed; 1 ignored` and `156 passed; 3
  ignored`), along with formatting, checks, strict Clippy, localization key/placeholder/visible
  audits, synchronization, Flatpak metadata, and diff checks.
- The first c66f6df Flatpak push/PR runs `29856562427`/`29856565472` failed only because the
  manifest still referenced the old `5d59646` source pin. Corrected push Native/Flatpak/Foundation
  runs `29856805455`/`29856805550`/`29856805478` and PR runs
  `29856808412`/`29856808321`/`29856808250` passed.

This advances unreleased Linux evidence for Scenario 8. Human translated-copy/visual/Orca review,
live-provider interoperability, other clients, signing, rollback, and stable release remain open.

## 2026-07-21 — Linux WAL process-crash recovery

Assumption: abrupt Unix process termination after a committed WAL transaction is an automatable
crash-recovery boundary; it does not emulate physical power loss or every SQLite VFS failure mode.

- Core `8837e59395742b5385af5037aa36a2596af3b025` adds
  `wal_replay_survives_process_termination_after_commit`: a child process holds a reader snapshot,
  commits a provider profile with SQLite `synchronous=FULL`, terminates abruptly, and the parent
  reopens the database to verify the model and persistent `SecretRef`.
- Linux docs/status head `b9c1c0e2c337eef609656aa1e62bf718068382e1` consumes that exact Core pin.
  Local Core/Linux validation passed, including full Core tests, strict Clippy, Linux no-default/
  demo-provider suites (`82/1` and `155/3` ignored), localization audits, synchronization, Flatpak
  metadata, and diff checks.
- Core CI/Fuzz/Native SDK runs `29854340447`/`29854339357`/`29854340140` passed. Linux code-head
  push/PR Native/Flatpak/Foundation runs `29854770351`/`29854770380`/`29854770404` and
  `29854773408`/`29854773406`/`29854773414` passed; final status-head runs
  `29855336417`/`29855336358`/`29855336333` and `29855339737`/`29855339709`/`29855339713` passed.

This remains unreleased Linux crash-recovery evidence. Physical power-loss simulation, alternate
SQLite VFS behavior, other clients, human visual/copy/Orca review, signing, rollback, and stable
release remain open.

## 2026-07-21 — Linux SQLite WAL durability hardening

Assumption: `synchronous=FULL` is the smallest safe storage hardening step for Linux WAL commits;
physical power-loss simulation and alternate SQLite VFS coverage remain separate acceptance work.

- Core `cfecf17802f022b3dc49cff2917de5a77382aefa` configures SQLite with WAL,
  `synchronous=FULL`, foreign-key enforcement, and secure deletion. The storage regression now
  asserts SQLite synchronous mode `2`, while WAL replay and schema checks remain covered.
- Linux docs/status head `94d57f61c16be45dd18e9a0519d7296cebefcb8f` consumes the exact Core pin.
  Local Linux formatting, checks, Clippy, no-default/demo-provider tests, localization audits,
  l10n synchronization, Flatpak metadata, and diff checks passed.
- Core CI/fuzz/native SDK runs `29852245672`/`29852245746`/`29852246017` passed. Linux push
  Native/Flatpak/Foundation runs `29853359722`/`29853359731`/`29853360059` and PR runs
  `29853364106`/`29853364378`/`29853364352` passed.

This remains unreleased Linux durability evidence. Physical power-loss recovery, alternate VFS,
other clients, human visual/copy/Orca review, signing, rollback, and stable release remain open.

## 2026-07-21 — provider-reported usage normalization

Assumption: provider usage metadata is advisory and non-sensitive; missing or partial wire values
must fall back safely without becoming a pricing claim.

- Core `117a72ea80f40258a0abf582ffe1fae93c155786` carries typed usage events through the provider
  stream and normalizes OpenAI Chat/Responses, Anthropic, Gemini, and Ollama metadata into the
  existing `UsageRecord`. Partial records are merged; absent metadata retains bounded local
  estimation. The stable C ABI/protobuf projection remains unchanged.
- Linux docs/status and pin head `507e028d10d2c360053d7b06389ceae910dd5fe9` consumes that Core
  revision; Flatpak keeps the existing Linux code pin `5d59646adeed72750964fa628eb0a3088911ac24`.
- Core fmt/check/Clippy/full workspace tests passed; Linux no-default/demo-provider suites passed
  (`82/1` and `155/3` ignored), localization/placeholder/visible audits, l10n sync, and Flatpak
  metadata validation passed. Core push CI/Native SDK/Fuzz runs `29850220180`/`29850220219`/
  `29850220238` passed. Linux push Native/Flatpak/Foundation runs
  `29850547006`/`29850546971`/`29850548756` and PR runs
  `29850550865`/`29850550890`/`29850550591` passed. Central coordination implementation
  checkpoint `c60b1752dc969f270a40d857895f028b789c7d86` and documentation alignment commit
  `7efe0ebf1981b3930628ad0c6aa0fc33447d53b1` passed workflows `29851043287`/`29851347134`.

This is unreleased provider-wire evidence. Billing equivalence, pricing, stable ABI projection,
other clients, human visual/copy/Orca review, signing, rollback, and stable release remain open.

## 2026-07-21 — Linux normalized usage metadata

Assumption: usage counts are non-sensitive metadata and must remain explicitly categorized as
provider-reported, locally estimated, or unknown; no pricing is inferred.

- Core `117a72ea80f40258a0abf582ffe1fae93c155786` adds the backward-compatible Rust `UsageRecord`
  completion field, provider wire normalization, and `usage_records_v1`; l10n
  `b817ba911c2ffafb35b7a29755681ab39e950368` adds five Linux usage/source labels.
- Linux docs/status head `507e028d10d2c360053d7b06389ceae910dd5fe9` stores and renders the source-
  marked usage line, with Flatpak pin `5d59646adeed72750964fa628eb0a3088911ac24`.
- Local Core workspace checks, Linux no-default/demo-provider suites (`82/1` and `155/3` ignored),
  localization audits, Flatpak metadata, synchronization, and diff validation passed. Remote push
  Native/Flatpak/Foundation `29848267826`/`29848267890`/`29848267931` and PR
  `29848272071`/`29848272079`/`29848272053` passed.

This is unreleased Linux/Rust-host evidence. Billing equivalence, pricing, stable ABI projection,
other clients, human visual/copy/Orca review, signed artifacts, rollback, and stable release remain
open.

## 2026-07-21 — Linux GTK routing profile deletion cleanup lifecycle

Assumption: deleting the currently selected routing profile must clear the GTK selection and
refresh the persisted list through the existing worker event boundary before another profile can
be used.

- Linux code `7f3ed8dcbed3f6e2eeda72b1c271992e36af65e5` extends the serialized
  `gtk_routing_profile_candidate_controls_have_accessible_lifecycle` fixture through Use, Delete,
  `RoutingProfileDeleted`, selected-ID cleanup, and an empty worker list refresh. The fixture keeps
  its private temporary database and worker shutdown boundary; it remains ignored locally because
  this host lacks the full GTK/Xvfb runtime.
- Flatpak pin `e4682e4ce4c8bd1d0b1874939b2a00fe698ea469` and Linux docs/status head
  `a4a17ae62132c62884e88ffdd47f76d17bf7c31f` record the exact lineage. Code-head push/PR
  Native/Flatpak/Foundation runs `29844751533`/`29844750810`/`29844750926` and
  `29844754143`/`29844754151`/`29844754090` passed; final status-head push/PR runs
  `29845371082`/`29845371250`/`29845370967` and `29845374385`/`29845374215`/`29845374014` passed.
- Local formatting, locked all-target/all-feature checks, strict GUI Clippy, demo-provider tests
  (`155 passed; 3 ignored`), no-default tests (`82 passed; 1 ignored`), localization audits,
  l10n synchronization, Flatpak metadata, and diff checks passed.

This is unreleased Linux candidate-management automation evidence only. Human visual, translated-
copy, and end-user Orca review; broader candidate-management release criteria; other clients;
signed artifacts; rollback authorization; and stable-release approval remain open.

## 2026-07-21 — Linux GTK routing candidate edit persistence lifecycle

Assumption: the existing Linux GTK routing-profile editor is the smallest complete slice for
proving candidate deselection and stable-ID editing without expanding the shared Core protocol or
other clients.

- Linux code `dda682d0690be77e93d551fcd31d9318f9c741bd` extends the serialized GTK lifecycle test
  `gtk_routing_profile_candidate_controls_have_accessible_lifecycle`: edit mode locks the profile
  ID, Candidate B is deselected, the same profile is saved, `RoutingProfileSaved` is observed, the
  worker lists the record, and the editor reload confirms only Candidate A remains selected.
- Flatpak pin `70e6074242f58385207884ac8966d4be89a2fa9f` and Linux docs/status head
  `9cab5ba7d9763df4a63dfe09c9a6519048c33bdd` record the exact source and documentation lineage.
  Corrected code-head push Native/Flatpak/Foundation runs `29842604602`/`29842604156`/`29842607411`
  and PR runs `29842605446`/`29842605764`/`29842605418` all passed. Final status-head push
  Native/Flatpak/Foundation runs `29843266745`/`29843267871`/`29843267747` and PR runs
  `29843272666`/`29843272809`/`29843272670` also passed.
- Local formatting, locked all-target/all-feature checks, strict GUI Clippy, demo-provider tests
  (`155 passed; 3 ignored`), no-default tests (`82 passed; 1 ignored`), localization audits,
  l10n synchronization, Flatpak metadata, and diff checks passed.

This is unreleased Linux candidate-management automation evidence only. Human visual, translated-
copy, and end-user Orca review; broader candidate-management release criteria; other clients;
signed artifacts; rollback authorization; and stable-release approval remain open.

## 2026-07-21 — Linux SQLite sidecar identity recheck after Core open

Assumption: checking SQLite `-wal` and `-shm` sidecar identities only before Core opens leaves a
residual replacement window, so the pinned parent descriptor and any pre-existing sidecar
identities must remain available for a second check after Core migration/open.

- Linux code `c6c5528314ddef98f2ac5f24aac8202b0e0d62d1` retains the parent descriptor and sidecar
  identity snapshot through `Storage::open_from_trusted_descriptor`, then fails closed when an
  existing sidecar changes identity or becomes an invalid alias. Sidecars absent at preflight may
  be created by SQLite, but the post-open inspection still rejects non-regular or hard-linked files.
  `replaced_database_sidecar_is_rejected_after_snapshot` uses an atomic rename from a pre-existing
  different inode so the race regression is deterministic; the earlier CI attempt
  `29839491260` exposed inode reuse in the test and was corrected rather than counted as evidence.
- Flatpak pin `1432242c96fad806094bf295703dc0df992d882a` and Linux docs/status head
  `49ea6212eba69c614403edf90d1e5ad9f044c26f` record the exact build and boundary. Corrected push
  Native/Flatpak/Foundation runs `29839920685`/`29839920594`/`29839920501` and PR runs
  `29839923879`/`29839924044`/`29839923994` passed; final status-head push Native/Flatpak/
  Foundation runs `29840468206`/`29840467826`/`29840468229` and PR runs
  `29840473167`/`29840473177`/`29840473045` also passed.
- Local formatting, locked all-target/all-feature checks, strict GUI Clippy, demo-provider tests
  (`155 passed; 3 ignored`), no-default tests (`82 passed; 1 ignored`), both sidecar regressions,
  localization audits, l10n synchronization, Flatpak metadata, and diff checks passed.

This is unreleased Linux storage hardening evidence only. Replacement after the second inspection,
broader filesystem/VFS behavior, abrupt power-loss recovery, other clients, signed artifacts,
rollback authorization, and stable-release approval remain outside the claim.

## 2026-07-21 — Linux SQLite WAL/SHM sidecar hard-link guard

Assumption: pre-existing SQLite `-wal` and `-shm` sidecars are part of the trusted profile
database boundary and must be private regular files before Core opens the database.

- Linux code `2077efb3349505b1125c8f0c686fd707ba439628` inspects both sidecars through the pinned
  parent descriptor with `O_PATH|O_NOFOLLOW`, ignoring only missing sidecars and rejecting
  non-regular or hard-linked aliases. The regression covers both suffixes and verifies that an
  external hard-link target is unchanged; an isolated pre-fix probe demonstrated that SQLite
  otherwise follows these same-UID hard-link sidecars and writes the external inode.
- Flatpak packaging pin `a220b18cfadffdcc39d40b9739cc510c66d45880` and Linux status/docs head
  `2362a5f213098c4cfc0a44580c17ae08dad20094` record the exact lineage. The first code-head
  push/PR Flatpak runs `29837248939`/`29837255929` failed only on the stale pin; corrected
  source-pin push Native/Flatpak/Foundation runs `29837460916`/`29837461045`/`29837460822` and
  PR runs `29837463776`/`29837464358`/`29837464171` passed. Status-head push Native/Flatpak/
  Foundation runs `29838016659`/`29838016535`/`29838016509` and PR runs
  `29838022061`/`29838022446`/`29838022044` passed.
- Local formatting, locked all-target/all-feature checks, strict GUI Clippy, demo-provider tests
  (`154 passed; 3 ignored`), no-default tests (`82 passed; 1 ignored`), the focused sidecar
  regression, localization audits, l10n synchronization, Flatpak metadata, and diff checks
  passed.

This is unreleased Linux storage hardening evidence only. Replacement after sidecar inspection,
broader filesystem/VFS behavior, abrupt power-loss recovery, other clients, signed artifacts,
rollback authorization, and stable-release approval remain outside the claim.

## 2026-07-21 — Linux final database-leaf identity and creation race hardening

Assumption: the final profile-database leaf must remain the exact preflight inode, and a missing
leaf must be created exclusively so a same-UID replacement cannot be accepted between validation
and descriptor open.

- Linux code `a7cee699bd973c8f05893c37b5583dd8c4998471` records the parent and existing-leaf
  device/inode, opens an existing leaf without creation flags, rejects distinct regular-file
  replacement after `fstat`, and uses `O_CREAT|O_EXCL|O_NOFOLLOW` when the leaf was absent.
  Packaging pin `87361ec9fbe37417dbf83f64b181cb834a5a4aa7` and status/docs head
  `5ae3b579d7393511d1a8fbdeedbdc86f1678df98` preserve the exact source lineage.
- Local formatting, locked all-target/all-feature check, strict GUI Clippy, demo-provider tests
  (`153 passed; 3 ignored`), no-default tests (`82 passed; 1 ignored`), targeted
  replacement/database/parent tests (`3`/`5`/`1` passed), localization audits, l10n
  synchronization, Flatpak metadata, and diff checks passed. Corrected source-pin push
  Native/Flatpak/Foundation runs `29835149907`/`29835149914`/`29835149955` and pull-request
  runs `29835154608`/`29835154630`/`29835155142` passed. The first code-head Flatpak run
  `29834999139` failed only on the stale source pin.
- Status-head push Native/Flatpak/Foundation runs `29835701523`/`29835701634`/`29835701563` and
  pull-request runs `29835705780`/`29835705840`/`29835706300` passed.

This is unreleased Linux storage hardening evidence only. Broader same-UID filesystem/VFS
variants, abrupt power-loss recovery, other clients, signed artifacts, rollback authorization,
and stable-release approval remain outside the claim.

## 2026-07-21 — Linux alternate-directory replacement race hardening

Assumption: replacing a validated private profile-database parent with a distinct private
directory must fail closed even when owner, permissions, and directory type remain valid.

- Linux code `14bb30e814d6d4ffcbf55c5a409d3729db2af967` retains the preflight parent device/inode,
  compares both after `openat2(RESOLVE_NO_SYMLINKS)`, and adds the deterministic alternate-directory
  replacement regression. Existing symlink/regular-file parent and symlink/hard-link final-component
  regressions remain covered.
- Local formatting, all-target/all-feature locked offline check, strict GUI Clippy, demo-provider
  tests (`151 passed; 3 ignored`), targeted storage tests, localization audits, l10n synchronization,
  Flatpak metadata, and diff checks passed. Packaging pin is `2dc3e49db9489eeaa2f9f3ec8fd70eb639bfb118`;
  status/docs head is `b3019913751bdbff7580a98708792fd84a5e6dea`.
- The first code-head Flatpak push/PR runs `29833169613`/`29833171987` failed only on the stale
  `3b2b69c` source pin. Corrected source-pin push Native/Flatpak/Foundation runs
  `29833316179`/`29833316220`/`29833316231` and PR runs `29833318520`/`29833318770`/`29833318526`
  passed. Status-head push Native/Flatpak/Foundation runs `29833853428`/`29833853406`/`29833853465`
  and PR runs `29833858405`/`29833858644`/`29833858612` also passed.

This is unreleased Linux storage hardening evidence only. Broader same-UID filesystem/VFS variants,
abrupt power-loss recovery, other clients, signed artifacts, rollback authorization, and stable
release approval remain outside the claim.

## 2026-07-21 — Linux provider mnemonic focus fixture

Assumption: Linux keyboard accessibility must verify both the provider form's explicit Tab order
and a visible-label mnemonic activation on the real GTK binary, including the Arabic fixture whose
catalog keeps this label in English fallback.

- Linux code `3b2b69c020eb6cc9f18488702916de175cb92700` records the `provider_preset` focus event
  from `Alt+P` in the existing X11/xfwm4 keyboard probe before asserting Tab/Shift+Tab traversal.
  Packaging/docs `123e4e4a6f7f3ddd7a041c1878edd197e435929b` repins Flatpak to `1030e88` and records
  the fixture behavior.
- The first code-head push/PR Flatpak runs `29830652002`/`29830655585` failed only because the
  manifest still referenced `c25bd31`; Native push/PR runs `29830652010`/`29830655820` passed.
  Corrected source-pin push Native/Flatpak/Foundation runs `29830916108`/`29830916150`/`29830916154`
  and PR runs `29830918743`/`29830918767`/`29830918756` passed. Final docs-head push
  Native/Flatpak/Foundation runs `29831556653`/`29831556427`/`29831556369` and PR runs
  `29831559867`/`29831560089`/`29831559828` passed.

This is automated Linux keyboard evidence only; physical keyboard, visual/RTL, Orca listening,
other-client, signing, rollback, and stable-release review remain separate gates.

## 2026-07-21 — Linux fallback-provider label relation

Assumption: every focusable provider-selection control must expose its visible label through both
the GTK mnemonic path and the exported `LabelledBy` relation, including the disabled fallback
selector shown before a provider is connected.

- Linux code `c25bd3142644ebe00a1609ca17f4ac7438326126` connects the fallback-provider label to its
  dropdown and extends the serialized GTK accessibility regression with relation and mnemonic
  assertions; production fallback-consent behavior is unchanged.
- Packaging/docs `b74b854d430179866abf134df3fa7052b33947ae` repins Flatpak to the exact code head,
  documents the fallback-provider relation, and records the first stale-pin failure.
- Local 82/150 Linux library suites (`1`/`3` ignored), formatting, locked checks, strict Clippy,
  localization audits, Flatpak metadata, and diff checks passed. Final push Native/Flatpak/Foundation
  runs `29829811241`/`29829811272`/`29829811222` and pull-request runs
  `29829814249`/`29829814264`/`29829814189` all passed.

This is automated Linux accessibility evidence only; human Orca listening, physical keyboard and
visual review, other clients, signing, rollback, and stable release remain open.

## 2026-07-21 — Linux runtime pseudo-localization

Assumption: the generated Linux `en-XA` and `ar-XB` PO/MO packs are test data for layout and
direction coverage, not qualified translations.

- Linux code `64a28771873cc9fa1e30451ecb5ed40bb497ca30` adds both pseudo-locales to the GTK runtime
  selector after the twelve official packs, wires catalog lookup, plural rules, locale names, and
  RTL metadata, and preserves the existing official order and language tags. Packaging/docs head
  `cf0b689070dc554584209638704b25db11943b18` repins Flatpak to the exact code head.
- Local formatting, all-target/all-feature check, strict Clippy, localization key/placeholder/
  visible audits, l10n synchronization, Flatpak metadata, and library suites passed: 82 passed
  with 1 ignored (no demo provider) and 150 passed with 3 ignored (demo provider).
- Final Linux push Native/Flatpak/Foundation runs `29824916845`/`29824916822`/`29824916804` and
  pull-request runs `29824919512`/`29824919621`/`29824919573` all passed. The first `64a2877`
  Flatpak attempt was correctly rejected for a stale build-input pin and is superseded by the
  exact-pin `cf0b689` head.

This is automated pseudo-localization evidence only; human translated-copy, plural, visual,
compositor, and screen-reader review remain separate release gates.

## 2026-07-21 — Linux pseudo-localized GTK/AT-SPI fixtures

Assumption: pseudo-locales must exercise the same live accessibility tree as the official locale
fixtures, while process-based window discovery keeps the test independent of expanded window titles.

- Linux fixture/docs head `22ff8f8` extends `tools/gtk-atspi-inspect.py` with exact expanded `en-XA`
  and bidi-isolated `ar-XB` control expectations, and Native CI runs both fixtures through the real
  GTK application with `LINGUAMESH_TEST_LOCALE=en-XA` and `LINGUAMESH_TEST_LOCALE=ar-XB`.
- The first fixture head `0c6151a` failed only because the harness searched for the literal
  `LinguaMesh` window title; corrective source head `304e683` locates the visible application window
  by process. Corrected push Native/Flatpak/Foundation runs `29825878061`/`29825878027`/`29825878160`
  and pull-request runs `29825880504`/`29825880581`/`29825880584` passed. The PR Flatpak run first
  hit a transient Flathub network fetch failure and passed on rerun; this remains automation evidence,
  not human translated-copy, visual, or screen-reader review.

## 2026-07-21 — Linux desktop text-scaling preference fixture

Assumption: Linux must inherit desktop text scaling through GTK/Pango without replacing the user's
font preference, alongside high contrast and reduced motion.

- Linux code `62c72fa` extends the serialized `gtk_accessibility_preferences_follow_desktop_settings`
  fixture with a process-local `Sans 24` font and asserts that the onboarding title's Pango context
  receives at least the requested 24-point size; theme, animation, and font settings are restored.
  Packaging/docs head `ed196d1` pins Flatpak to the code head and documents the isolated fixture.
- Local formatting, all-target/all-feature locked offline check, strict Clippy, Flatpak metadata,
  shell syntax, and diff checks passed. The real GTK fixture is CI-only on this host because the
  matching Xvfb/GTK runtime is unavailable locally.
- Final push Native/Flatpak/Foundation runs `29828098608`/`29828098596`/`29828098740` and
  pull-request Native/Flatpak/Foundation runs `29828100998`/`29828100985`/`29828100954` passed,
  including the isolated high-contrast, reduced-motion, and text-scaling assertions. Manual visual
  review remains a separate release gate.

## 2026-07-21 — Linux visible GTK localization audit scope

Assumption: the Linux source audit must cover every Rust UI module, including file-filter names,
while allowing empty label resets used to clear transient state.

- Linux `56a081272ed3fb6b42dcd3111616a620763f51c8` expands
  `tools/check-visible-localization.py` from two fixed files to every `src/**/*.rs` file and adds
  `set_name` coverage for file-filter labels. The audit passes with three intentional empty/reset
  call sites and no non-empty hard-coded GTK strings.
- Local key/placeholder/visible audits, l10n synchronization, Flatpak metadata, formatting,
  locked offline checks, strict Clippy, and 81/149 library tests passed. Status/docs head
  `89d4e22` passed Linux push Native/Flatpak/Foundation runs
  `29823219039`/`29823218980`/`29823219144` and pull-request runs
  `29823221964`/`29823221885`/`29823221874`.

This strengthens repeatable Linux source evidence only; translated-copy, plural, visual locale,
physical desktop, other-client, signing, and stable-release review remain open.

## 2026-07-21 — Linux Arabic headless Orca fixture

Assumption: Linux screen-reader automation should exercise the same production Stop control in
Arabic as the semantic and keyboard fixtures, while keeping human speech-quality review separate.

- Code/docs head `490657b0751527e5c7fae3ab89993b90bb97f575` maps the test locale to the production
  Stop accessible name and adds a second private Xvfb/private-D-Bus Orca run with
  `LINGUAMESH_TEST_LOCALE=ar`. English still requires the application-tree and `SPEECH GENERATOR`
  records; Arabic requires the localized AT-SPI tree and focus path only because the CI speech backend
  did not emit a stable locale-specific speech record. The initial `7c9b7e4` attempt failed at that
  boundary and remains recorded as corrective evidence.
- Local Python compile, shell syntax, rustfmt, locked offline check, and diff checks passed. Corrected
  code-head push Native/Flatpak/Foundation runs `29821349008`/`29821349052`/`29821349030` and
  pull-request runs `29821346477`/`29821346416`/`29821346504` passed, including both Orca fixtures.
- Status/docs head `b574cc4342944b076f8fbdf993172e639433226c` passed push
  Native/Flatpak/Foundation `29821778205`/`29821778263`/`29821778215` and pull-request
  Native/Flatpak/Foundation `29821775327`/`29821775342`/`29821775256`.

This strengthens automated Linux Scenario 13 headless accessibility evidence only; human Orca
listening, speech quality, translated-copy/RTL, physical visual/compositor review, other clients,
signing, and stable-release approval remain open.

## 2026-07-21 — Linux Arabic AT-SPI semantic fixture

Assumption: Scenario 13 requires the Arabic accessibility tree to expose localized names and
stable roles for the production controls, while preserving explicit English fallback names where
the pinned Arabic catalog remains untranslated.

- Linux code head `3ce10d576bc2b0835daffd2aa5bb19fc9d9e6dc4` adds Arabic expectations to the live
  AT-SPI inspector: localized Open (`فتح ملف نصي`), Translate (`ترجمة`), and Stop (`إيقاف الترجمة`),
  plus English Retry and fallback names; the fixture still requires button/checkbox roles and two
  text-editor roles. Native CI runs the real binary in a private Xvfb/AT-SPI session.
- Local Python compile, shell syntax, rustfmt, locked offline check, localization audits, and diff
  checks passed. Code-head push Native/Flatpak/Foundation runs
  `29819765571`/`29819765594`/`29819765609` and pull-request runs
  `29819762498`/`29819762505`/`29819762534` all passed, including the Arabic fixture output.
- Status/docs head `c5db4e417a50220dee6481d8a53bc3a43186477c` passed push
  Native/Flatpak/Foundation `29820197646`/`29820197676`/`29820197652` and pull-request
  Native/Flatpak/Foundation `29820195059`/`29820195042`/`29820194969`.

This strengthens automated Linux Scenario 13 accessibility evidence only; human Orca speech,
translated-copy/RTL, physical visual/compositor review, other clients, signing, and stable-release
approval remain open.

## 2026-07-21 — Linux Arabic RTL keyboard-focus fixture

Assumption: Scenario 13 requires keyboard traversal to remain usable after the production GTK
workspace switches to Arabic RTL, not only a unit-level direction flag.

- Linux fixture/runtime code head `743ddaebde9ae3627ba8e8de38d04c6b79ed87c6` runs the existing
  English Xvfb/xfwm4 focus traversal and a second `LINGUAMESH_TEST_LOCALE=ar` traversal that
  requires the production workspace to report RTL. Flatpak build input is pinned at
  `fedc1a9bd28e1ceb54a3d963efb2785354e9f479`.
- Local rustfmt, all-target/all-feature locked offline check, demo-provider tests (`149 passed; 3
  ignored`), no-default tests (`81 passed; 1 ignored`), strict Clippy, localization audits,
  Flatpak metadata, synchronization, and diff checks passed.
- The first 743 code-head Flatpak attempt failed because its manifest still referenced `59b57c0`;
  the corrected `fedc1a9` pin passed push Native/Flatpak/Foundation
  `29818596872`/`29818597026`/`29818596824` and PR Native/Flatpak/Foundation
  `29818599326`/`29818599257`/`29818599479`.
- Status/docs head `23c3a56af90917d616660480e267cc537bb7e1ce` then passed push
  Native/Flatpak/Foundation `29819019804`/`29819019831`/`29819019803` and PR
  Native/Flatpak/Foundation `29819022552`/`29819022529`/`29819022599`.

This strengthens automated Linux Scenario 13 keyboard evidence only; manual translated-copy/RTL,
screen-reader, visual/compositor, other clients, signing, and stable-release review remain open.

## 2026-07-21 — Linux post-preflight regular-file and hard-link race regressions

Assumption: Linux storage validation must reject same-UID replacement of a validated parent or
database leaf even when the replacement is not a symbolic link, without widening the release claim.

- Linux code head `59b57c00f9f4745154f3fe2daa93a49d94a445e0` adds regressions for a regular-file
  parent replacement and a hard-linked final database component after preflight; both fail closed,
  and the linked target remains unchanged. Flatpak build input is pinned at `751ac1eb069aee06c69abc2c63d2a7a7c46e3bd6`.
- Local Linux formatting, targeted regressions, demo-provider tests (`149 passed; 3 ignored`),
  no-default tests (`81 passed; 1 ignored`), strict Clippy, localization audits, Flatpak metadata,
  synchronization, and diff checks passed.
- The first push/PR Flatpak gates failed because the manifest still referenced ancestor `f53c44d`; after
  repinning, final push Native/Flatpak/Foundation runs `29817292493`/`29817292344`/`29817292390`
  and PR Native/Flatpak/Foundation runs `29817295183`/`29817295210`/`29817295244` all passed.
- Linux docs/status follow-up head is `b078b8e5862fad3a3a4aae8ef78fcf3273562d1b`; status-only
  push Native/Flatpak/Foundation runs `29817714165`/`29817714101`/`29817714200` and PR
  Native/Flatpak/Foundation runs `29817717903`/`29817717896`/`29817717877` all passed.

This expands automated Linux storage-race evidence only. Broader filesystem/VFS variants, power
loss, human review, other clients, signing, and stable release remain open.

## 2026-07-21 — Linux storage-race validation boundary correction

Assumption: status documentation must distinguish tested Linux path races from broader
filesystem/VFS and power-loss behavior that remains unverified.

- Linux docs/status head `488575e7e5ba15b2836d7a8c7e9f0afed49fa9d4` clarifies that parent-directory
  and final-database-component replacement races are covered by descriptor-pinned `openat2` and
  Core `O_NOFOLLOW`; broader same-UID variants, alternate VFS behavior, and power loss remain
  outside the claim. No runtime source or compatibility pin changed.
- Push Native/Flatpak/Foundation runs `29816104837`/`29816104784`/`29816104797` and pull-request
  Native/Flatpak/Foundation runs `29816107833`/`29816107893`/`29816107760` all passed.

This is documentation-boundary evidence only; Linux remains unreleased.

## 2026-07-21 — Linux Core compatibility rejection matrix

Assumption: the Linux client must fail closed for every reviewed Core compatibility dimension
before provider work begins, while keeping the release train unreleased.

- Linux source/docs head `92b5136b53ee5042aba26a07ea039b626dd1afdf` expands
  `reviewed_core_contract_is_required_exactly` to reject Core semantic-version, ABI-major,
  protocol-version, provider-catalog, and required-feature mismatches with typed
  `ProtocolIncompatible` errors. The Flatpak manifest pins the build-input source to code head
  `f53c44de3e36a432d8cca75a02e354a941fb564b`.
- Local Linux no-default/demo-provider suites passed (`81 passed; 1 ignored` / `147 passed; 3
  ignored`), with formatting, all-target/all-feature check, strict Clippy, localization audits,
  Flatpak metadata, synchronization, and diff checks.
- The initial push/PR Flatpak gates failed honestly because the manifest still referenced ancestor
  `12e810b`; after repinning, final push Native/Flatpak/Foundation runs
  `29815397653`/`29815397736`/`29815397742` and PR Native/Flatpak/Foundation runs
  `29815402318`/`29815402263`/`29815402242` all passed.

This strengthens Linux Scenario 16 evidence only. Other clients, human review, broader filesystem
and power-loss behavior, signed artifacts, and stable-release authorization remain open.

## 2026-07-21 — Core SQLite WAL replay and Linux compatibility evidence

Assumption: Linux should verify the shared Core writer-disconnect recovery sequence without
claiming arbitrary power-loss or SQLite VFS behavior.

- Core `4badabe735499a50265a1260a838df3254622c15` adds a storage regression that commits a provider
  profile while a reader snapshot holds the WAL, disconnects the writer, and verifies the next
  `Storage::open` restores the profile and non-secret SecretRef/model fields. Core workspace tests,
  strict Clippy, formatting, and the Linux SDK package smoke passed; the reproducible package SHA-256
  was `9857c972ce16ae3d0243fecfe76755f301abe94ca3a3c10f880f62a2836914f`.
- Linux status/docs head `9406d3a4e794ace27582434ad7c941c07749a721` pins that exact Core revision in
  Native CI and Flatpak. Local Linux no-default/demo-provider suites passed (`81 passed; 1 ignored`
  / `147 passed; 3 ignored`) with strict Clippy, localization audits, Flatpak metadata, and diff
  checks.
- Push Native/Flatpak/Foundation runs `29813283713`/`29813283776`/`29813283818` and pull-request
  Native/Flatpak/Foundation runs `29813286614`/`29813286582`/`29813286593` passed all jobs,
  including the Core package smoke and Linux GTK/accessibility fixtures.

This remains unreleased Linux-first persistence evidence. Abrupt power loss, alternate SQLite VFS
behavior, cross-client persistence, signed artifacts, and stable-release authorization remain open.

# 2026-07-21 — Linux system accessibility preference evidence

Assumption: the Linux client should inherit desktop high-contrast and reduced-motion preferences
through GTK/libadwaita without introducing a private contrast or animation policy.

- Linux status/docs head `53cd41f` adds a serialized GTK component fixture that applies a temporary
  `HighContrast` theme, disables `gtk-enable-animations`, asserts libadwaita detection, and restores
  both process-local settings. Native CI runs it in a private Xvfb/DBus session.
- Linux push Native/Flatpak/Foundation runs `29811402708`/`29811402703`/`29811402563` and PR
  Native/Flatpak/Foundation runs `29811404883`/`29811404846`/`29811404855` passed. The Native logs
  include the high-contrast and reduced-motion assertions.
- Local Linux formatting, all-target check, strict Clippy, no-default tests (`81 passed; 1 ignored`),
  shell syntax, and diff checks passed; the display-backed fixture is CI evidence because this host
  lacks `xvfb-run`.

This is Linux prerelease accessibility evidence only. Manual visual, RTL, screen-reader, and
compositor review, other clients, signed artifacts, and stable-release approval remain open.

# 2026-07-21 — Clean bootstrap acceptance evidence

Assumption: Scenario 19 must be proven from a disposable workspace, not inferred from the already
prepared local checkout.

- A fresh clone of `linguamesh-project` ran `GITHUB_OWNER=getio0909 bash tools/bootstrap.sh` in a
  temporary directory. The script cloned all seven canonical public repositories and then passed
  strict workspace validation, global-goal pin checks, release-manifest schema/compatibility checks,
  documentation-link checks, and credential-signature scanning.
- The temporary workspace was removed after the run. Existing repositories, user changes, and
  remotes were not modified.

This proves the reproducible bootstrap path only; native client parity, signed artifacts, and stable
release evidence remain open.

## 2026-07-21 — Reproducible Linux SDK package verification

Assumption: the Linux SDK archive is prerelease evidence only; reproducibility and consumer
linkage must be verified before any artifact can be considered for a signed release.

- Core documentation head `f09a632` records `bash tools/verify-linux-sdk-package.sh` rebuilding
  the `0.1.0-alpha.2` archive twice from functional Core pin
  `19229184a21a6725326a3d30dea9bc72e5ac999f` with SHA-256
  `487c83c17f80634826437e94ca7d817e83f0addf60999d6789fcb58beb774afc`.
- The verifier accepted the outer archive and every packaged file, validated `linguamesh-core.pc`,
  and compiled and ran the packaged static-library C consumer smoke test.
- This updates prerelease evidence only. Core `source_revision` remains the functional pin and no
  signed or stable artifact is added to the release manifest. Central coordination workflow
  `29807730525` passed both Linux and PowerShell validation jobs.

## 2026-07-21 — Linux Native CI pinned Core SDK package smoke

Assumption: Linux Native CI must verify the exact Core package consumed by the client before
client tests run; the generated archive remains prerelease evidence until release authorization.

- Linux commit `cef6ac1` runs `bash tools/verify-linux-sdk-package.sh` from the checked-out Core
  tree at `19229184a21a6725326a3d30dea9bc72e5ac999f`. The verifier rebuilt the release archive
  twice, checked the outer and per-file SHA-256 manifests, validated pkg-config metadata, and ran
  the packaged static C consumer; archive SHA-256 was
  `3b42d10a347a32e45abb63f3ddb4bf052f90da26f940d2436256f66baae0c9f5`.
- Push Native/Flatpak/Foundation `29808320946`/`29808320963`/`29808320962` and PR
  Native/Flatpak/Foundation `29808324340`/`29808324366`/`29808324395` passed. Follow-up status
  head `bd9559c` reran push `29808700811`/`29808700809`/`29808700814` and PR
  `29808703288`/`29808703310`/`29808703348` successfully.

This confirms Linux/Core prerelease compatibility inputs only; no signed, published, or stable
artifact is claimed.

## 2026-07-21 — Linux dependency and provenance gate

Assumption: Linux release candidates need the same dependency advisory, license, and source policy
as Core, while duplicate GTK graph versions remain warnings during convergence.

- Linux documentation/status head `ca4d11f89ee9323f18a19b5ccc75e270359705d2` adds `deny.toml`,
  the pinned cargo-deny Native step, and Foundation presence validation. Local cargo-deny passed;
  duplicate `getrandom`, `hashbrown`, and `windows-sys` versions are warnings.
- Push Native/Flatpak/Foundation `29806613032`/`29806613069`/`29806613012` and PR
  Native/Flatpak/Foundation `29806615931`/`29806615901`/`29806615910` all passed. The release
  manifest now points to this Linux head; no stable release is authorized.

## 2026-07-21 — Linux localized live AT-SPI fixture

Assumption: live accessibility evidence should include catalog-backed names in a non-English
locale while retaining the English baseline and strict role assertions.

- Linux final head `b2a3f476138d9b70569525acf066e9120a7b21b5` adds the test-only
  `LINGUAMESH_TEST_LOCALE` override, explicit English/Simplified Chinese expected names, and a
  second Native CI fixture with `LINGUAMESH_TEST_LOCALE=zh-CN`. Ordinary startup remains English.
- Push Native/Flatpak/Foundation `29804861125`/`29804861156`/`29804861132` and PR
  Native/Flatpak/Foundation `29804863422`/`29804863440`/`29804863421` passed all jobs. The Native
  log records the five Chinese names and their roles; Flatpak validates the exact reviewed source
  pin at `346b9499261da31d092c04703918195ba2678b14`.
- The preceding code-head Flatpak runs failed only because the packaging manifest still pointed at
  `93fd6f2`; the failure is retained as corrective evidence and the pin was updated before the
  passing run.

This remains unreleased Linux-first accessibility evidence. Human Orca listening, translated-copy/
RTL review, physical desktop rendering, other clients, signing, distributable artifacts, and stable
release remain open.

## 2026-07-21 — Linux AT-SPI status-role fixture boundary

Assumption: a live AT-SPI assertion must match the roles exported by the pinned GTK runtime; a
failed semantic assertion is evidence of a fixture/runtime boundary, not permission to weaken it.

- Attempted Linux head `995c9fa2435f710a540a861a1ccace08d6fca728` required live `ROLE_STATUS` and
  `ROLE_ALERT`; Native push `29803564933` and PR `29803567256` failed because the GTK/AT-SPI bridge
  exported empty status/error regions as `ROLE_LABEL`.
- Corrected Linux head `a4c9d3fde77e91f0655784d296f3a957367613a2` reverts the incompatible live-tree
  assertion, retains existing GTK unit-level `AccessibleRole::Status`/`AccessibleRole::Alert`
  checks, and documents the runtime limitation. Corrected push Native/Flatpak/Foundation
  `29803843127`/`29803843131`/`29803843157` and PR `29803845060`/`29803845055`/`29803845046`
  passed all jobs.

This remains unreleased Linux-first evidence. A runtime-compatible live status/error fixture, human
Orca listening, translated-copy/RTL review, physical desktop rendering, other clients, signing,
distributable artifacts, and stable release remain open.

## 2026-07-21 — Linux testing-guide suite-count refresh

Assumption: contributor-facing test documentation must match the current runnable suite rather
than historical checkpoint counts.

- Linux documentation head `6b8cdc8426939fd19c7e977d5e0159a9a7fb35ac` updates `docs/testing.md`
  from stale 54/104-test descriptions to the observed no-default/demo-provider totals
  (`81 passed; 1 ignored` / `147 passed; 3 ignored`) and names the external prerequisites for the
  ignored cases.
- Final push Native/Flatpak/Foundation `29802930525`/`29802930632`/`29802930547` and PR
  Native/Flatpak/Foundation `29802932689`/`29802932707`/`29802932683` passed all jobs. This is a
  documentation consistency correction; no release status changes.

## 2026-07-21 — Linux final database-component race regression

Assumption: the profile database must reject a final-path replacement that occurs after pathname
preflight but before the descriptor is opened, not only a replaced parent directory.

- Linux code head `93fd6f2b7d258c2c9902386ee1edb7a94c45fd9b` adds
  `replaced_database_file_is_rejected_between_preflight_and_descriptor_open`; the test creates a
  post-preflight final-component symlink, opens the validated parent by descriptor, and requires
  the production `O_NOFOLLOW` path to reject it without modifying the target. Packaging pin head
  `2ce550da4c195ad6e93d0fb7a6924b1aafa6b008` points exactly to that code lineage, and final docs
  head is `1c0b1e98efd478df225ab2a95f6a10288da5ada6`.
- Local no-default tests (`81 passed; 1 ignored`), demo-provider tests (`147 passed; 3 ignored`),
  strict Clippy, localization audits, formatting, diff checks, and Flatpak metadata passed.
- Push Native/Flatpak/Foundation `29802525642`/`29802525571`/`29802525612` and PR
  Native/Flatpak/Foundation `29802527738`/`29802527705`/`29802527681` passed all jobs.

This remains unreleased Linux-first hardening evidence. Broader filesystem/VFS and power-loss
behavior, human review, other clients, signing, distributable artifacts, and stable release remain
open.

## 2026-07-21 — Linux validation boundary refresh

Assumption: the testing guide must distinguish completed automated evidence from the manual,
platform, and release work that still prevents a supported Linux release.

- Linux documentation head `175eb00c19176ac8ff24c05843a62a81e7908c02` updates `docs/testing.md`
  to name the automated GTK/AT-SPI semantic tree, headless Orca, portal, Flatpak,
  localization-invariant, and storage-boundary coverage already exercised by this branch.
- The residual list now explicitly covers human screen-reader and translated-copy/RTL review,
  physical compositor/GPU and broader X11 coverage, prompted Secret Service approval, broader
  filesystem/VFS and power-loss races, dependency/license/advisory automation, signed artifacts,
  stable-release authorization, and the other native clients.
- Linux push/PR Native, Flatpak, and Foundation runs
  `29801687294`/`29801687305`/`29801687356` and
  `29801689279`/`29801689288`/`29801689275` passed all jobs. This is documentation evidence only;
  the release manifest remains unreleased.

## 2026-07-21 — Linux fallback-consent accessible name

Assumption: an explicit fallback-consent checkbox must expose its localized accessible name on the
checkbox node itself, not only through a related label, while preserving runtime locale switching.

- Linux code `6c1d89f9c015e65a98568f71f40ade260554018b` sets and tests GTK
  `AccessibleProperty::Label` on the fallback checkbox; packaging head
  `e0eb47119cd63a3c9521af13e833b9051cacf43e` repins Flatpak to that exact source, and final
  documentation head is `5bc870b2c48c6d116a375382e83568e1900d99ba`.
- Local formatting, GUI all-target check, strict Clippy, key/placeholder/visible localization audits,
  no-default tests (`81 passed; 1 ignored`), and demo-provider tests (`146 passed; 3 ignored`)
  passed. The live Xvfb/AT-SPI fixture is CI-authoritative on this host.
- Push Native/Flatpak/Foundation `29801182286`/`29801182297`/`29801182271` and PR
  Native/Flatpak/Foundation `29801183970`/`29801183976`/`29801183979` passed all jobs. The prior
  PR Native run `29800755130` failed at the existing keyboard-focus fixture and was superseded by
  the passing rerun job `88541746697`; the final docs-head runs above are the authoritative evidence.

This remains unreleased Linux-first accessibility evidence. Human Orca listening, translated-copy/
RTL review, physical desktop rendering, other clients, signing, distributable artifacts, and stable
release remain open; PR #1 is Draft/Open and Issue #1 is Open.

## 2026-07-21 — Linux error-mapping localization coverage

Assumption: catalog completeness must include error-category and error-state mappings, not only
call sites that directly invoke a localization helper.

- Linux `37539e7d4af4c207355e99ea7ea21f9949a52ab7` extends `tools/check-localization-keys.py` to
  collect every `error.*` key declared in `src/model.rs` and `src/main.rs`, in addition to direct
  localization calls and diagnostics keys. The canonical catalog audit now covers 381 keys.
- Local placeholder and visible-string audits passed; Linux no-default tests passed (`81 passed;
  1 ignored`) and demo-provider tests passed (`146 passed; 3 ignored`).
- Push Native/Flatpak/Foundation `29800104908`/`29800104899`/`29800104894` and pull-request
  Native/Flatpak/Foundation `29800106522`/`29800106523`/`29800106590` passed all jobs. The Linux
  PR remains Draft/Open with no review requests.

This is unreleased Linux-first source-level evidence. Dynamic provider details, human translated-
copy/RTL review, Orca listening, other clients, signing, distributable artifacts, and stable-release
authorization remain open; central Issue #1 remains Open.

## 2026-07-21 — Linux AT-SPI action-name coverage

Assumption: the next Linux-first accessibility slice should strengthen the existing live AT-SPI
tree export without claiming human screen-reader listening or physical-desktop review.

- Linux `ef87a5b1fb6ebbfaaf8b9d4d93f572ae7f4bdf43` expands `tools/gtk-atspi-inspect.py` to require
  `Open text file`, `Translate`, `Retry translation`, and `Stop translation` as named push-button
  controls, plus the `Allow approved fallback` label/control and the existing two text-editor roles.
  GTK exports the fallback name on its associated label node; the GTK role/relation unit coverage
  remains authoritative for the checkbox itself.
- Local `python3 -m py_compile tools/gtk-atspi-inspect.py`, `bash -n tools/run-gtk-atspi-test.sh`,
  `git diff --check`, `cargo test --no-default-features --locked` (81 passed; 1 ignored), and
  `cargo test --features demo-provider --locked` (146 passed; 3 ignored) passed. This host lacks
  the Xvfb/AT-SPI runtime packages, so the live fixture is CI-authoritative.
- The initial remote head `9bda65b` correctly failed when it assumed the checkbox node carried the
  accessible name; the logs showed the expected label export. Corrected head `ef87a5b` passed all
  six gates: push Native/Flatpak/Foundation `29799549333`/`29799549300`/`29799549304` and PR
  Native/Flatpak/Foundation `29799551201`/`29799551179`/`29799551121`.

This remains unreleased Linux-first evidence. Human translated-copy/Orca listening review,
physical desktop rendering, broader filesystem races, Android/Windows/macOS clients, signing,
distributable artifacts, and stable-release authorization remain open; PR #1 is Draft/Open and
Issue #1 is Open.

## 2026-07-21 — Core POSIX document-descriptor consumption and Linux repin

Assumption: the Linux-first ABI boundary must duplicate a registered POSIX descriptor and apply
the shared bounded document parser before consuming the engine-scoped lease.

- Core `19229184a21a6725326a3d30dea9bc72e5ac999f` adds
  `lm_engine_file_lease_consume_posix_document`. It duplicates the registered descriptor, reads at
  most `MAX_DOCUMENT_BYTES + 1`, validates the shared document contract, consumes the lease only
  after successful parsing, and keeps oversized input retryable. Core local workspace tests,
  strict Clippy, and C/C++ Native SDK smoke passed.
- Core CI/Fuzz/Native SDK runs `29795469293`/`29795469253`/`29795469275` passed for the exact
  commit across Linux, Android, Windows, and Apple Native SDK jobs, retaining the protocol/document
  decoder AddressSanitizer gate.
- Linux `126699a1eb93fbecafcbb73f79d83c680652ce00` pins the exact Core revision in Native and
  Flatpak metadata. Local no-default/demo-provider suites passed (`81 passed; 1 ignored` /
  `145 passed; 3 ignored`), strict Clippy, all-target check, localization audits, and Flatpak
  metadata validation passed. Linux PR Native/Flatpak/Foundation `29795527184`/`29795527194`/
  `29795527187` passed all jobs, including GTK, portal, Orca, packaging, checksum, SBOM, and
  sandbox fixtures.

This closes the Linux/POSIX descriptor document-consumption sub-boundary only. Android ParcelFileDescriptor,
Windows handle transfer, other clients, human visual and prompt review, signing, rollback, stable
artifacts, and stable release remain open; PR #1 and Issue #1 remain open.

## 2026-07-21 — Linux Flatpak pin exactness and evidence refresh

Assumption: a packaging source pin should identify the exact reviewed Linux revision recorded by
the central release manifest, even when a validator can safely accept an unchanged ancestor.

- Linux `2fb277411822e348e8ef5d0444ee2aaa14cb78a2` updates the Flatpak source manifest from an
  unchanged ancestor to the exact Linux head and corrects the testing guide's historical Core
  command example. No runtime behavior or release status changed.
- Local Flatpak metadata, formatting, and diff checks passed. Push Native/Flatpak/Foundation runs
  `29796238918`/`29796238922`/`29796238931` and pull-request runs
  `29796240722`/`29796240700`/`29796240751` passed all jobs, including GTK, portal, Orca,
  packaging, checksum, SBOM, and sandbox fixtures.

This remains unreleased Linux-first evidence. Human visual/copy review, Android ParcelFileDescriptor,
Windows handle transfer, other clients, signing, rollback, stable artifacts, and stable release
remain open; PR #1 and Issue #1 remain open.

## 2026-07-21 — Linux prerelease rollback evidence sidecars

Assumption: CI can record a future rollback procedure without claiming a signed release or inventing
an unavailable previous stable revision.

- Linux `665eb928b88c0c6f900d4e74f32e4939e8d64589` adds deterministic `ROLLBACK.md` sidecars to
  the Native and Flatpak checksum/SPDX evidence generators. Each record carries the exact Linux,
  Core, and (for Native) localization revisions, stops short of signing, and instructs operators
  to restore a previously verified manifest/artifact before resuming distribution.
- Local no-default/demo-provider suites passed (`81 passed; 1 ignored` / `145 passed; 3 ignored`),
  localization audits, Flatpak metadata, evidence-generator smoke checks, formatting, and diff
  checks passed. Push Native/Flatpak/Foundation `29796868664`/`29796868631`/`29796868628` and PR
  runs `29796870557`/`29796870563`/`29796870547` passed all jobs, including uploaded rollback
  evidence and Flatpak sandbox smoke.

This is still unsigned prerelease evidence. No previous stable revision, signing key, stable artifact,
or release authorization is present; human review, other clients, handle transfer, and stable release
remain open. PR #1 and Issue #1 remain open.

## 2026-07-21 — Linux preflight replacement regression verified

Assumption: the deterministic preflight replacement fixture is valid evidence when the exact Linux
head and all six client gates are recorded, while broader filesystem races remain a separate scope.

- Linux code head `b463e5b94ed6b46ef24aee89ff9887d9dd5c038c` adds the replacement-boundary regression;
  docs-only head `43b9c5ee11397f5ce7fbf4033615b1609553f3c7` records the verified result. The Flatpak
  manifest pins the build-input ancestor `b463e5b9` because the later changes are documentation-only.
- Push Native/Flatpak/Foundation runs `29798721356`/`29798721343`/`29798721336` and PR runs
  `29798723569`/`29798723560`/`29798723668` passed all jobs. Native covered the preflight test;
  Flatpak validated the ancestor lineage, uploaded checksum/SPDX/rollback evidence, and completed
  sandbox smoke.

The canceled runner `29797697833` is not counted; it never started its reported step and was replaced
by the passing PR run above. Broader filesystem/VFS races, other clients, human review, signing,
stable artifacts, and stable release remain open; PR #1 and Issue #1 remain open.

## 2026-07-21 — Security and privacy evidence matrices

Assumption: the Milestone 8 security documents must map each required threat and privacy data
category to an implemented control, repository evidence, owner role, and residual review boundary;
an inventory without that mapping is not sufficient for stable-release review.

- Replaced the threat-model skeleton with an auditable abuse-case matrix covering credential/log
  leakage, endpoint redirects, prompt injection/output validation, archive/parser attacks,
  malformed protocol streams, local persistence/temporary files, fallback disclosure, locale and
  catalog tampering, FFI misuse, and supply-chain/stale-core risks.
- Replaced the brief privacy model with a data inventory covering content, credentials, file grants,
  operational metadata, preferences, and explicit diagnostic exports. Each category records its
  destination, retention/deletion behavior, user control, and current evidence boundary.
- The workspace and repository validators passed after the update; automated evidence points to
  Core/Linux tests and workflows while prompted UI approval, physical rendering, live provider
  privacy, other clients, signing, rollback, and stable-release review remain explicitly open.

## 2026-07-21 — Core document decoder fuzz gate and Linux compatibility repin

Assumption: the next Linux-first compatibility checkpoint must include reproducible protocol and
document-decoder fuzz/sanitizer gates, while keeping the stable-release decision blocked on the
remaining Milestone 8 evidence.

- Core `e7ca21df183b15e10e157f175526a1b7ac0b3ad0` adds bounded document-decoder fuzzing for text,
  subtitle, CSV, HTML, JSON, DOCX, PPTX, XLSX, EPUB, and PDF dispatch in the separate fuzz
  workspace. Fuzz run `29791113663` covered protocol and document targets under the fixed
  `nightly-2026-07-20` AddressSanitizer toolchain; Core CI `29791113656` and Native SDK
  `29791113659` passed all jobs.
- Linux `e71edf55ede238d729fc2fd34936dcd2ad8d4459` consumes the exact Core pin in Native and
  Flatpak metadata and updates compatibility documentation. Local no-default/demo-provider tests
  passed (`81 passed; 1 ignored` / `145 passed; 3 ignored`), as did strict Clippy, all-target
  check, localization audits, and Flatpak metadata validation. PR Native `29792553415`, Flatpak
  `29792553389`, and Foundation `29792553385` passed all jobs, including GTK, portal, Orca,
  packaging, checksum, SBOM, and sandbox fixtures.

This is unreleased Linux-first evidence. Document-command resource consumption, OS-handle transfer,
other clients, human visual review, signing, rollback, stable artifacts, and stable release remain
open; Linux PR #1 remains Draft/Open and central Issue #1 remains Open.

## 2026-07-21 — Core ABI one-shot document lease consumption

Assumption: ABI hosts need a bounded document-byte handoff that consumes a validated lease exactly
once, while platform-specific handle duplication remains an explicit later boundary.

- Core `1e0ae8d3fcf8bd5fead244ebf78cb3ea4a0ec300` adds
  `lm_engine_file_lease_consume_document`. The call bounds the source name and document snapshot,
  parses with the shared `linguamesh-document` contract, rejects malformed or expired input without
  consuming the lease, and removes the lease after successful validation. FFI regression coverage
  verifies one-shot consumption and retry-after-parse-failure; C and C++ Native SDK smoke passed.
- Core CI `29793500441`, Fuzz/ASAN `29793500440`, and Native SDK `29793500462` passed all jobs.
- Linux `37e9b74d79c414958e228bdb25dd84681981fb85` pins the exact Core revision in Native and
  Flatpak inputs. Local no-default/demo-provider suites passed (`81 passed; 1 ignored` /
  `145 passed; 3 ignored`), strict Clippy, all-target check, localization audits, and Flatpak
  metadata validation passed. Formal PR Native/Flatpak/Foundation `29793663690`/`29793663688`/
  `29793663685` passed all jobs; push Native/Flatpak/Foundation `29793660915`/`29793660941`/
  `29793660945` also passed.

This closes the bounded ABI document-byte consumption sub-boundary only. Linux's production GTK
path remains direct typed Rust; OS-handle duplication/transfer, other clients, signing, rollback,
stable artifacts, and stable release remain unverified. PR #1 and Issue #1 remain open.

## 2026-07-21 — Core ABI malformed-input hardening and Linux repin

Assumption: the next Linux-first compatibility checkpoint should exercise the real C ABI submit
boundary with bounded untrusted bytes while keeping sanitizer and coverage-guided fuzzing as explicit
Milestone 8 requirements.

- Core `9a959f142f6660f4a736174cb17f8bea6ff332c1` adds a deterministic 4,096-case malformed-input
  corpus through `lm_engine_submit`, caps each payload at the existing 1 MiB protocol limit, and
  requires controlled rejection or busy results without provider requests or panics. Targeted FFI,
  full workspace tests, formatting, strict Clippy, build, cargo-deny, and C/C++ Native SDK smoke
  passed locally. Core CI `29788492719` and Native SDK `29788492749` passed all jobs.
- Linux `1e631f1ee02a13b96737fbfb509a9d56fec4f925` pins that exact Core revision in Native and
  Flatpak inputs and updates architecture, testing, release, and status evidence. Local no-default
  and demo-provider suites passed (`81 passed; 1 ignored` / `145 passed; 3 ignored`), as did strict
  Clippy, all-target check, localization audits, and Flatpak metadata validation. Linux PR Native,
  Flatpak, and Foundation runs `29788818095`/`29788818096`/`29788818078` passed all jobs, including
  GTK, portal, accessibility, packaging, checksum, SBOM, and sandbox fixtures.
- A local all-target GUI build remains blocked by the host's installed GTK/Adwaita linker symbols;
  the remote Native gate completed the corresponding build and release-mode checks successfully.

This is unreleased Linux-first evidence. Coverage-guided fuzzing, sanitizer runs, document-command
resource consumption, OS-handle transfer, Android/Windows/macOS projections, human review, signing,
rollback, stable artifacts, and stable release remain open; Linux PR #1 and central Issue #1 remain
Draft/Open.

## 2026-07-20 — Core ABI FileLease lifecycle controls pinned to Linux

Assumption: native hosts need bounded lease lifecycle control before document commands can consume
platform resources; resource values must remain private to Core.

- Core `0396736235d4dc5c8992d3bfef5aded3abadf457` adds C ABI create calls for validated paths,
  POSIX descriptors, Android parcel descriptors, and Windows handles, returning only engine-scoped
  numeric tokens. Active-state, expire, revoke, and destroy calls are panic-safe, bounded to 64
  leases per engine, isolated between engines, and cleanable after shutdown. Core local fmt/check,
  strict Clippy, workspace tests/build, cargo-deny, and C/C++ SDK smoke passed; CI `29787040329`
  and Native SDK `29787040314` passed.
- Linux `8f52685ade7cfbe29f0cafa42263bb3b0a725259` pins the exact Core revision in Native and
  Flatpak workflows and documents that the direct Rust portal-read path remains authoritative until
  document commands consume ABI tokens. Local no-default/demo-provider suites passed (`81 passed;
  1 ignored` / `145 passed; 3 ignored`), strict Clippy, localization audits, Flatpak metadata, and
  diff checks passed. PR Native/Flatpak/Foundation `29787357289`/`29787357304`/`29787357315` passed.
- Coordination commit `9d8e151179da7d323134e3b112cf5daf623b6ed3` passed Validate project
  coordination workflow `29787744384` for Linux/PowerShell manifest, link, and credential checks.
- This is unreleased Linux-first evidence. ABI document-command resource consumption, OS-handle
  transfer, Android/Windows/macOS clients, human review, signing, rollback, stable artifacts, and
  stable release remain open. Linux PR #1 remains Draft/Open and central Issue #1 remains Open.

## 2026-07-20 — Linux FileLease document-import boundary

Assumption: Linux document imports must borrow a bounded Core file resource only for the read and
must fail closed if that lease expires or is explicitly revoked before decoding completes.

- Core `8b096478b1623bdaf5105e8a8f59e55e2fa8015d` adds `file_lease_v1` with opaque lease IDs,
  validated desktop/temporary/output paths, POSIX and Android parcel descriptors, Windows handles,
  monotonic expiry/revocation, and guard access that rechecks state. Domain and FFI tests cover all
  resource shapes, invalid values, and expiry; local full workspace/strict Clippy and C/C++ Native
  SDK smoke passed. Core CI `29784269272` and Native SDK `29784269356` passed.
- Linux `f95780db3dd05fdccfe47af254f73c5107587077` pins the exact Core revision, requires the feature
  during compatibility negotiation, checks leases in asynchronous GIO reads and decoding, maps
  expiry to the existing localized file-open path, and revokes after bytes are copied into a bounded
  `DocumentJob`. Local no-default/demo-provider tests passed (`81 passed; 1 ignored` / `145 passed;
  3 ignored`), as did strict Clippy, localization audits, Flatpak metadata, and diff checks.
- Linux Native/Flatpak/Foundation runs `29785377479`/`29785377512`/`29785377513` passed with jobs
  `88495671317`/`88495671975`/`88495671980`. This is unreleased Linux-first evidence; ABI handle
  transfer, Android/Windows/macOS clients, human accessibility review, signing, rollback, and stable
  release remain open. PR #1 remains Draft/Open and Issue #1 remains Open.
- Central coordination run `29785760751` passed Linux job `88496851860` and PowerShell job
  `88496851914` for the synchronized manifest, documentation, and credential-hygiene checks.

## 2026-07-20 — C ABI compatibility snapshot consumed by Linux

Assumption: native clients must negotiate Core semantic, ABI, protocol, catalog, and feature
dimensions through one versioned query before starting provider work; ABI file-lease handle transfer
remains outside this checkpoint.

- Core `c559b32d3869e01983f2bbf32f1386bad99c3290` adds `CompatibilitySnapshot` and
  `lm_engine_get_compatibility`; Core CI `29782822854` and Native SDK `29782822883` passed.
- Linux documentation/source-pin head `b38a8fd722d4740abd161e30197354793e3de1f6` pins workflow and
  Flatpak inputs to the exact Core revision. Local no-default/demo-provider suites, strict Clippy,
  localization audits, Flatpak metadata, and diff checks passed. PR Native `29783023917` (job
  `88488352790`), Foundation `29783023894` (job `88488352736`), and Flatpak `29783023872` (job
  `88488352708`) passed.
- This remains unreleased Linux-first evidence: file leases, other client projections, complete
  acceptance scenarios, human review, signing, rollback, and stable release remain open. PR #1 is
  Draft/Open and Issue #1 remains Open.

## 2026-07-20 — C ABI host-secret response projection consumed by Linux

Assumption: ABI 1 native clients must receive the same one-time, non-persistent secret-broker
semantics already enforced by the typed Rust application layer.

- Core `adc1e26f37db3761406bb30aa7515003a8bd2717` adds the backward-compatible `secret_ref`
  command field, versioned `secret_required` event, and one-shot `host_secret_response`. The FFI
  validates operation/correlation/request identity, resolution, size, replay, and late responses;
  local Core workspace check, strict Clippy, all-target/all-feature tests, and C/C++ Native SDK
  smoke passed. Core CI `29781845494` and Native SDK `29781845502` passed.
- Linux documentation/source-pin head `016c4d79131b08ad5eb66e0b7561b9e3e50f02b0` consumes the
  exact Core revision and refreshes Flatpak metadata. Local no-default tests passed (`80 passed;
  1 ignored`), demo-provider tests passed (`144 passed; 3 ignored`), strict Clippy, localization
  audits, Flatpak metadata, and diff checks passed. Linux Foundation/Native/Flatpak gates
  `29781942858`/`29781942757`/`29781942821` passed with jobs
  `88484970323`/`88484969938`/`88484969961`.
- This remains an unreleased Linux-first compatibility checkpoint: semantic/catalog/feature
  negotiation, file leases, other client projections, complete acceptance scenarios, human review,
  signing, rollback, and stable release remain open. PR #1 remains Draft/Open and Issue #1 remains
  Open.

## 2026-07-20 — Core RetryPolicy deserialization validation consumed by Linux

Assumption: retry-policy data restored from JSON or another serialized boundary must be subject to
the same bounds as freshly constructed policy data.

- Core `6e8c40224943a6ba892e5a064fb3b00657b3bf47` replaces derived `RetryPolicy` deserialization
  with validation through `RetryPolicy::new`, preventing serialized configurations from restoring
  unbounded backoff, jitter, circuit threshold, or cooldown values. Core domain, engine, and FFI
  tests passed (`36`, `5`, and `10` tests respectively), with formatting and diff checks clean.
- Linux documentation/source-pin head `5b807093c05995a3029e60bb3563ba55200597f9` consumes the
  exact Core revision and updates the Flatpak source manifest. Local no-default tests passed
  (`80 passed; 1 ignored`), demo-provider tests passed (`144 passed; 3 ignored`), strict Clippy,
  localization audits, and Flatpak metadata validation passed.
- GitHub Foundation `29780440569` (job `88480156512`), Native Linux `29780440461` (job
  `88480156210`), and Flatpak Linux `29780440421` (job `88480155904`) passed for the Linux head.
  PR #1 remains Draft/Open, Issue #1 remains Open, and the release train remains unreleased.

## 2026-07-20 — Shared Core RetryPolicy consumed by Linux

Assumption: retry and circuit-breaker bounds must be one validated Core contract so native clients
cannot drift in backoff, jitter, provider hints, or cooldown behavior.

- Core `8790eb41a52c4e2c908044699e8c12597d3c42a5` adds public `RetryPolicy` construction and
  standard defaults with bounded backoff, jitter, `Retry-After`, failure threshold, and cooldown;
  Core CI/Native SDK `29778375725`/`29778375728` passed.
- Linux source/pin `3ff10f4c9f54d82b7c43a0204946033cb063b92f` consumes that policy for routing retry
  and circuit state. Documentation/source-pin head `eb7e57869580917494d719ac61ec861c1c8bcff4`
  passed push Native/Flatpak/Foundation `29778624703`/`29778624674`/`29778624715` and PR
  `29778626906`/`29778626865`/`29778626849`.
- Final Linux status head `857dac37c1d54c3987b69bd5b96e357fb8977e82` passed push
  Native/Flatpak/Foundation `29779357668`/`29779357649`/`29779357690` (jobs
  `88476555747`/`88476555602`/`88476555686`) and PR
  `29779360891`/`29779360949`/`29779361066` (jobs
  `88476567289`/`88476567432`/`88476567728`).
- Local Core full workspace validation and Linux GUI check/Clippy/no-default/demo-provider suites
  passed; Linux remains the only actively implemented native priority. PR #1 remains Draft/Open,
  Issue #1 remains Open, and no stable release or artifact promotion is claimed.

## 2026-07-20 — Linux bounded routing retry and circuit-breaker policy

Assumption: retryable provider failures must advance only through the configured Linux routing
chain, with bounded waits, cancellation, and no sensitive data in retry state.

- Core `c03bd205e1d135c024f3a0a767dd94770030a723` adds optional `retry_after_ms` to
  `TranslationError`; HTTP-date and delta-seconds headers are bounded to sixty seconds and all
  four HTTP adapters preserve legacy payload compatibility when the hint is absent.
- Linux source/pin `4b345763af46bc4cd23bdecc54ecb6b8b52e597a` applies an eight-second maximum,
  deterministic safe-key jitter, shutdown-aware waits, and a two-failure/30-second in-memory
  circuit breaker. Core CI/Native SDK `29776309259`/`29776309263` passed, as did Linux source/pin
  push/PR Native/Flatpak/Foundation `29776662997`/`29776663334`/`29776662987` and
  `29776667400`/`29776667014`/`29776667068`. Documentation follow-up head
  `2a75ac0449dcc577ec263b73929c4c89ca10f063` passed push Native/Flatpak/Foundation
  `29777101390`/`29777101871`/`29777101540` and PR `29777102953`/`29777103017`/`29777103023`.
  Central coordination commit `adaa2a16e127b508b630c3a7711a2cb19d26ecb0` passed workflow
  `29777574182` (Linux and PowerShell validation).
- Local Core workspace tests passed 150 cases; Linux passed no-default (`80 passed; 1 ignored`)
  and demo-provider (`144 passed; 3 ignored`) suites, GUI all-target check, strict Clippy,
  l10n audits, Flatpak metadata validation, and diff checks. PR #1 remains Draft/Open and Issue #1
  remains Open; this is unreleased Linux-first evidence.

## 2026-07-20 — Linux explainable routing decision diagnostics

Assumption: Linux routing diagnostics must be inspectable while remaining free of provider
endpoints, credentials, source text, and translated output; Core's bounded candidate keys, stable
rejection reasons, and score components are safe to expose.

- Linux source/pin head `ab82f36963a63f43091d94e960541fc173175724` carries eligible candidates,
  rejected candidates with reason codes, ranking inputs, and configured fallback order from Core
  through Worker events and `AppState` into the localized GTK diagnostics panel. Model, worker, and
  serialized GTK lifecycle regressions assert the complete redacted summary.
- Localization revision `737d890e60fd34f15fd8708698448ef9ab96299f` adds the detail template and
  regenerated resources for all twelve packs. Local Linux formatting/check/Clippy, no-default and
  demo-provider tests, l10n synchronization, Flatpak metadata, and diff checks passed.
- Push Native/Flatpak/Foundation gates `29773735297`/`29773735296`/`29773735294` and PR gates
  `29773738883`/`29773738887`/`29773738924` passed. Documentation head `458a920321ae16e6d3983213a286a972e34c8a18`
  then passed push Native/Flatpak/Foundation `29774707677`/`29774707852`/`29774708075` and PR
  `29774709730`/`29774709849`/`29774710165`. PR #1 remains Draft/Open and the release train
  remains unreleased.

## 2026-07-20 — Linux GTK routing candidate accessibility lifecycle

Assumption: candidate-management acceptance requires the production GTK dialog to expose
focusable, screen-reader-labelled controls and preserve the selected profile through Use/close.

- Linux code/pin head `1c47ff9b6b103ee16d564480d3dd3cdfcda5e083` adds the ignored serialized
  `gtk_routing_profile_candidate_controls_have_accessible_lifecycle` fixture. It checks the
  labelled profile ID field, stable mode order, explicit fallback checkbox, focusable candidates,
  accessible movement labels, row reordering, Manual single-candidate enforcement, and Use
  close-and-select behavior through the real GTK dialog.
- Local formatting, GUI all-target check, strict Clippy, no-default-feature tests (`80 passed; 1
  ignored`), demo-provider tests (`142 passed; 3 ignored`), Flatpak metadata, and diff checks
  passed. The host has no `xvfb-run`; Native CI is authoritative for the GTK runtime fixture.
- Push Native/Flatpak/Foundation `29771475803`/`29771475775`/`29771475669` and PR
  `29771479057`/`29771478869`/`29771478884` passed. PR #1 remains Draft/Open and Issue #1 remains
  Open; visual/translated-copy review, end-user Orca acceptance, other clients, signing, rollback,
  and stable-release authorization remain open.

## 2026-07-20 — Linux fallback approval dialog lifecycle

Assumption: ordinary-text fallback requires explicit one-shot consent; dismissing the modal must
not dispatch or leave approval armed.

- Linux `62d70b1c57662515fadb447aa625cabe1b5d74e9` documents and tests the production GTK dialog
  through `gtk_fallback_approval_dialog_requires_an_explicit_one_shot_action`. The dedicated
  DBus/Xvfb fixture verifies modal/focusable warning controls, `Close` with zero dispatches, and a
  single `Translate` dispatch that records approval. The full Rust suite keeps this GTK test
  ignored because GTK initialization is thread-bound; the Native workflow runs it in a separate
  serialized process.
- Local Linux no-default tests passed `80 passed; 1 ignored`; demo-provider tests passed
  `142 passed; 3 ignored`. Formatting, GUI all-target check, strict Clippy, Flatpak metadata, and
  diff checks passed. This host lacks `xvfb-run`, so local GUI execution is represented by the
  remote fixture.
- Final Linux push Native/Flatpak/Foundation gates `29770058909`/`29770058926`/`29770058895` and
  PR gates `29770062559`/`29770062414`/`29770062090` passed. Earlier corrective failures are
  retained in the Linux status. Central coordination workflow `29770588175` passed for commit
  `7f2b1519f58212945ab027e33c0598f739d1d527`. PR #1 remains Draft/Open; no merge, signing,
  rollback, or stable release claim is made.

## 2026-07-20 — macOS native text slice

Assumption: the macOS SwiftUI/AppKit client may ship as an unreleased prerelease checkpoint
while typed host-secret transport, model discovery, persisted routing profiles, document jobs,
and distribution signing remain outside this slice.

- macOS `cad822c` adds the native SwiftUI/AppKit text workflow, generated Core Swift bridge,
  protocol/error validation, Keychain credential storage, locale/theme preferences, cancellation,
  partial-output preservation, diagnostics, source hygiene checks, app assembly, and ad-hoc signing
  smoke coverage. It pins project `b75d4d1`, Core `0db51464`, and l10n `7e8c987` with ABI 1 and
  protocol 1.
- Local source validation and diff checks pass. GitHub PR #1 is Draft/Open; native workflow run
  `29765906044` is the final remote build/test/package gate for this head. No merge, notarization,
  stable signing, rollback, or release promotion is claimed.

## 2026-07-20 — Linux Automatic routing fallback integration

Assumption: Automatic routing requires client-worker evidence in addition to Core ranking tests;
only candidates explicitly exposed by the saved routing profile may receive a retryable retry.

- Linux code head `0e2ae25c321cef243275d1322f2b8271f0602d06` adds a worker regression that creates
  two saved providers, verifies the Core quality preference selects the higher-quality candidate,
  shuts it down before dispatch, and asserts typed decision/fallback events before completion through
  the next approved candidate. The test does not introduce document-job fallback or unapproved data
  disclosure. Linux documentation head `75910c8a77d0c05d4bc9e069a40381808160f4aa` records the
  reproducible commands and corrective Flatpak source-pin change.
- Local Linux full tests passed (`142 passed; 3 ignored`), with formatting, GUI all-target check,
  strict Clippy, localization/Flatpak validation, and diff checks. Final documentation-head push/
  PR Native, Flatpak, and Foundation gates passed: push `29767680041`/`29767680024`/`29767680047`
  and PR `29767684643`/`29767684366`/`29767684440`. The initial code-head stale-pin Flatpak
  failures (`29767075134`/`29767080595`) are retained in the Linux status as corrective evidence.
- PR #1 remains Draft/Open; the release train is unreleased and no merge, signing, rollback, or
  stable-release claim is made.

## 2026-07-20 — Linux explicit provider connection test

Assumption: an explicit provider test may create a temporary provider session for model discovery,
but must not switch or persist the active profile, selected model, or credential.

- Linux `02efde00fb9faf3abfc4ab5dcf19b9c6036be656` adds a cancellable worker `TestConnection`
  command/event pair and a localized GTK provider-form action. The action validates the draft,
  clears the credential entry immediately, discovers models, and reports a typed result without
  changing the active translation session or saved profile.
- Linux worker regression `explicit_connection_test_discovers_models_without_switching_active_session`
  proves a successful and failed test leave the confirmed provider/model usable. Localization
  `7e8c987737444d4e0f8f2642b108eee4c7801f58` adds the action, tooltip, and success template to all
  generated locale resources.
- Local Linux check, 143 passing library tests with 12 environment-gated ignored, strict Clippy,
  localization audits, and Flatpak metadata validation passed. Push Native/Flatpak/Foundation
  runs `29758801692`/`29758801470`/`29758801642` and PR runs `29758805190`/`29758806520`/
  `29758805530` all passed. Central coordination workflow `29759295217` passed for commit
  `22eac8973cae90a9ab5e9f7244d968f5fedfcf79`. PR #1 remains Draft/Open and Issue #1 remains Open; no merge,
  signing, rollback, or stable-release action is claimed.

## 2026-07-20 — Linux document-routing evidence reconciliation

Assumption: the current Linux document-routing slice is complete for saved single-profile
selection, while document-job fallback and cross-client routing remain intentionally disabled.

- Linux worker tests `document_job_translation_uses_saved_routing_profile_without_fallback` and
  `document_job_resume_reconnects_saved_routing_profile_after_restart` select a saved
  document-capable candidate, emit a typed routing decision with zero fallback attempts, rebuild
  the translated document, and reconnect the persisted non-secret profile ID after restart.
- The behavior is implemented at Linux revision `02efde00fb9faf3abfc4ab5dcf19b9c6036be656`,
  against Core `115535c76d804020f045708867af7798b8d0294a`; the current push/PR Native, Flatpak,
  and Foundation gates all passed (`29755663043`/`29755662549`/`29755662552` and
  `29755666246`/`29755666022`/`29755666120`).
- Central release metadata now records document-job routing as implemented for this Linux slice;
  it does not claim automatic document fallback, other clients, signing, rollback, or a stable
  release.

## 2026-07-20 — Linux routing profile JSON exchange

Assumption: profile exchange is a non-secret portability path; importing an existing ID must fail
closed rather than silently replacing a profile referenced by a document job.

- Core `115535c76d804020f045708867af7798b8d0294a` adds bounded routing-profile JSON codecs. The
  codec validates all Core fields, rejects unknown fields (including endpoint/credential-shaped
  extensions), and enforces a 64 KiB UTF-8 exchange limit.
- l10n `7e8c987737444d4e0f8f2642b108eee4c7801f58` raises the canonical catalog to 425 messages and
  regenerates Linux PO/MO resources for all official and pseudo locales.
- Linux `02efde00fb9faf3abfc4ab5dcf19b9c6036be656` adds worker export/import commands and GTK native
  file chooser actions. Import rejects malformed, non-UTF-8, oversized, unknown-field, and
  duplicate-ID payloads; export contains only validated routing metadata and never logs file bytes.

Local evidence: Core workspace tests (all targets/features, including 29 domain and 33 storage
tests), Linux all-target check, strict Clippy, 142 Linux library tests with 12 environment-gated
ignored, localization check/generate-check, key/placeholder/visible audits, and Flatpak metadata
validation passed. Remote evidence: Core CI/Native SDK `29753851712`/`29753851733`; l10n
Localization/Foundation `29754460570`/`29754460635`; Linux push Native/Flatpak/Foundation
`29755663043`/`29755662549`/`29755662552`; Linux PR Native/Flatpak/Foundation
`29755666246`/`29755666022`/`29755666120`. PR #1 remains Draft/Open and Issue #1 remains Open;
no merge, signing, rollback, or stable-release action is claimed.

## 2026-07-20 — Linux request-level translation presets

Assumption: Linux is the first active client target; Android, Windows, and macOS remain out of scope
for this checkpoint. Document jobs persist the same bounded non-secret preset contract as text
requests, and legacy schema rows default to General.

- Core `9cacf6364a2a2c6e63f65b336bb7dfe5d460518f` adds the validated `TranslationPreset` request
  contract, `translation_presets_v1`, escaped prompt rendering, and translation-memory identity
  separation. All built-in provider adapters carry the request-level preset.
- l10n `7f65596bd71be3ed6e179ade3bf2e436545436a2` raises the catalog to 415 messages and regenerates
  Linux PO/MO resources for all official locales; non-English packs remain machine-generated drafts.
- Linux `7817108aef100de6fa65946ffc8456f0fdbab2a4` adds schema-18 document option persistence,
  localized GTK selector restoration, request propagation through plain/routed create, retry, and
  restart, compatibility requirement, and mapping regressions. Local Core and Linux tests,
  Clippy, locked builds, localization checks, Flatpak metadata, and diff checks passed.
- Remote evidence passed: Core CI/Native SDK `29751949004`/`29751948936`; l10n Localization/Foundation
  `29748435744`/`29748435654`; Linux push Native/Flatpak/Foundation `29752035759`/`29752035851`/
  `29752035798`; Linux PR Native/Flatpak/Foundation `29752038881`/`29752038779`/`29752038938`;
  coordination validation `29752543584` passed on central commit `52fe082f1f1f4c091dda8d732dcdf5e1c8ae2806`. PR #1 remains Draft/Open and Issue #1 remains Open; no
  merge, close, signing, rollback, or stable-release action is claimed.

## 2026-07-20 — Linux document quality-mode persistence

Assumption: a document job captures the selected `Fast`, `Balanced`, or `Best` policy at dispatch
time and reuses it for every segment after pause, retry, or process restart; legacy rows default to
`Balanced`.

- Core `f62f2df91584eeebdf5c30bd06c5e0893f2345d8` adds schema 17 migration
  `0017_document_quality_mode.sql`, stable-name parsing, and non-secret option round trips. Core
  CI/Native SDK runs `29744643575`/`29744643593` passed.
- Linux `c0ac94e25fb7a64b330fee538e64d82405f35aab` propagates quality mode through plain/routed
  document commands, applies it to every segment request, restores it into GTK state, and keeps
  the selector enabled for selected jobs. Local GUI check, strict Clippy, 140 tests with 3 ignored,
  locked build, localization audits, Flatpak metadata, and diff checks passed.
- Linux push Native/Flatpak/Foundation `29746095888`/`29746095985`/`29746095892` and PR
  Native/Flatpak/Foundation `29746099123`/`29746099062`/`29746099042` all passed. This remains an
  unreleased Linux-first checkpoint; no merge, signing, rollback, or stable-release action is claimed.

## 2026-07-20 — Linux translation quality modes checkpoint

Assumption: quality mode is a request-level deterministic policy shared by Core and Linux; `Best`
uses one provider request with an internal critique/revision instruction and does not claim live
provider quality, human review, or stable-release readiness.

- Core `d304afe01e21023a1e1f37ad8f674d49a23b5d42` adds `Fast`, `Balanced`, and `Best`, the shared
  `translation-prompt-v2` contract, malformed-output validation, and versioned translation-memory
  identity. Local workspace check, tests, strict Clippy, and locked build passed.
- l10n `e03d8ccc548d7d2eeeef9163b4b12b8204e68d6d` raises the catalog to 410 messages and regenerates
  official Linux resources. `PYTHON_BIN=/home/wangtinghu/miniconda3/envs/py313/bin/python make check`
  passed locally.
- Linux `aaffb87d4a7e52e64370c082b144fd8e50e84b43` adds the localized GTK quality selector, request
  propagation, and selection regressions. Flatpak pin `f78574d` follows the source; local GUI checks,
  140 tests with 3 ignored, strict Clippy, localization audits/sync, and Flatpak metadata validation
  passed.
- Core, l10n, Linux, and central pins are pushed. PR #1 remains Draft/Open and Issue #1 remains Open;
  Core CI/Native SDK `29742242153`/`29742242102`, l10n Localization/Foundation
  `29742198569`/`29742198614`, Linux push Native/Flatpak/Foundation `29742596157`/`29742596195`/
  `29742596247`, Linux PR Native/Flatpak/Foundation `29742602112`/`29742602104`/`29742602095`, and
  central coordination `29742676456` passed. Android, Windows, macOS, live-provider review, signing,
  rollback, and stable-release gates remain open.

## 2026-07-20 — Linux Provider Catalog compatibility checkpoint

Assumption: Core's bundled provider catalog is the authoritative non-secret contract for adapter
types and model-listing policy; Linux retains native localized labels and endpoint defaults, while a
stale mapping must stop before the GTK window is created.

- Linux `f1996faaae591f476ff2610746bd4cbeb9e0b53e` consumes Core's `linguamesh-provider-catalog`
  crate at `d304afe01e21023a1e1f37ad8f674d49a23b5d42`, caches the bundled catalog, derives
  manual-model visibility from `model_listing`, and validates all six GTK preset adapter mappings
  before startup. The Flatpak source pin follows this head.
- `provider_presets_map_to_stable_native_and_compatible_defaults` covers the stable GTK order and
  catalog compatibility without credentials or network access; mismatch fails closed with an
  English diagnostic.
- Local Linux formatting, GUI all-target check, strict Clippy, 140 demo-provider tests with 3
  ignored, localization audits/sync, Flatpak metadata, and diff checks passed. Push
  Native/Flatpak/Foundation `29743687368`/`29743687294`/`29743687262` and PR
  `29743689677`/`29743689725`/`29743689515` passed. PR #1 remains Draft/Open, central Issue #1
  remains Open, and the release train remains `unreleased`.

## 2026-07-20 — Linux OpenAI Responses typed-SSE checkpoint

Assumption: Linux remains the first active client target; OpenAI Responses model discovery uses the
shared `/v1/models` contract, while live account, quota, model availability, and cross-client
behavior remain unverified.

- Core `58075c997cecdcd9a179b9397cb493da375d3a50` adds `openai_responses` with Bearer
  authentication, `/v1/responses` request shaping, typed `response.output_text.delta` and
  `response.completed` SSE handling, redacted diagnostics, and `openai_responses_v1`. Local Core
  workspace tests, strict Clippy, and locked validation passed; CI/Native SDK runs
  `29739668055`/`29739668165` passed.
- l10n `95078b1a0c30defe98995a9879c4c669d213e5bc` adds the localized Responses preset copy and
  generated 405-message resources. Local `make check` passed; Localization/Foundation runs
  `29739956505`/`29739956524` passed.
- Linux functional revision `498323ee09a69f3183b903278efcab137836c3fb` adds the six-item GTK preset
  list and `openai_responses_provider_discovers_and_streams_typed_sse`; Flatpak pin revision
  `62385d4228750711f232381805bbdab2f560b309` follows the functional head. Local GUI/all-target
  check, 139 passing tests with 3 ignored, strict Clippy, localization audits/synchronization, and
  Flatpak metadata validation passed. Push/PR Native, Flatpak, and Foundation runs
  `29740264065`/`29740263971`/`29740263996` and `29740261207`/`29740261147`/`29740261173` all passed.
- PR #1 remains Draft/Open and central Issue #1 remains Open. The release train stays `unreleased`
  with empty artifact lists; Android, Windows, macOS, signing, rollback, and stable-release gates
  remain open.
- Central coordination commit `d8387a7fb8f6027a726f9948fcf45a5192246ba5` passed validation run
  `29740781908` for both Linux and PowerShell checks.

## 2026-07-20 — Linux Azure OpenAI provider checkpoint

Assumption: Linux is the first active client target; deterministic Azure loopback evidence proves
request shaping and session-secret handling while live Azure account, quota, deployment, other
clients, signing, rollback, and stable-release behavior remain unverified.

- Core `e46066ccafcd81e50b004c84d7eb8734e77f3279` adds `azure_openai_chat` with resource/deployment
  URL validation, pinned API version `2024-10-21`, `api-key` authentication, manual deployment
  selection, and deterministic testkit coverage.
- Linux `a679d57bf9b4d887d27fdd4c2cb2f87dfd6342db` adds the localized Azure OpenAI preset and
  `azure_openai_provider_uses_manual_deployment_and_api_key`; the fixture selects
  `fake-deployment`, makes no model-list request, and streams `你好，Azure！` through the worker.
- l10n `8e0e50577f8714b90bcc08a0d22cc790319f9239` contains 401 messages and generated Linux PO/MO
  resources. Core CI/Native SDK `29738151804`/`29738151858` and l10n Localization/Foundation
  `29738073868`/`29738073889` passed. Linux push Native/Flatpak/Foundation
  `29738486868`/`29738486841`/`29738486838` and PR Native/Flatpak/Foundation
  `29738489229`/`29738489379`/`29738489251` all passed. Central commit `df0d3b8994d5466b4a7fe209ab43288bbf689bac`
  passed coordination run `29738896174` (Linux and PowerShell). PR #1 remains Draft/Open and Issue
  #1 remains Open.

## 2026-07-20 — ABI 1 engine-bound buffer ownership documentation

Assumption: no ABI 0 SDK artifact or compatible native client was released, so the accepted ABI 1
ownership transition can proceed without a binary migration release.

- Central commit `81d3f3c37e6fde54da21034e60d716c56b67e981` publishes RFC-0001 and ADR-0004. The
  decision requires `lm_engine_buffer_free(engine, buffer)`, a bounded allocation registry owned
  by each engine, monotonic ownership tokens, descriptor validation, and wrapper copy-and-release.
- Core `232881263f4f523ce54b3713d83513f2d0170ff2` already implements ABI major 1 and tests wrong
  engine, forged/copied/duplicate descriptors, shutdown release, concurrent controls, and the
  64-buffer bound. Protocol version 1 is unchanged and the central release train remains
  `unreleased` with empty artifact lists.
- `bash tools/check-workspace.sh` and coordination CI `29736748680` (Linux and PowerShell jobs)
  passed for the implementation documentation head; follow-up documentation validation
  `29736800710` also passed. Android, Windows, and macOS wrapper conformance,
  sanitizers/fuzzing, signed SDK artifacts, and stable-release authorization remain open.

## 2026-07-20 — Linux Gemini end-to-end worker fixture

Assumption: the Linux-first Gemini acceptance boundary must traverse the same worker and
`ProviderManager` path used by the GTK client, while live external-account behavior remains out of
scope for deterministic CI.

- Core `232881263f4f523ce54b3713d83513f2d0170ff2` adds the deterministic Gemini test server;
  Linux `3edb91c5a17d774edffbd336564cfdc385f75fc5` consumes it and runs
  `gemini_provider_discovers_and_streams_without_secret`, selecting `gemini-2.0-flash` and
  producing `你好，Gemini！` through the worker.
- Core CI/Native SDK `29735977442`/`29735977484` passed. Linux documentation head
  `a698d47945367d4336a739f93185a0519d469fb2` passed all six final push/PR gates:
  push Native/Flatpak/Foundation `29736402002`/`29736401951`/`29736401989` and PR
  Native/Flatpak/Foundation `29736404211`/`29736404204`/`29736404197`. The central release
  manifest points to the functional Core/Linux pins with l10n
  `f9d74a8f83a89540a58bba65477a5031031bd619`, and coordination CI `29736800710` passed on the
  final central documentation head; status remains `unreleased`.

## 2026-07-20 — Linux Google Gemini Generate Content provider

Assumption: Linux remains the priority client; Android, Windows, and macOS stay deferred while this
shared provider slice is validated.

- Core `638713c34ce7d5bcc8003bb0d7e54c514ab49ea7` adds deterministic Gemini model discovery and
  fragmented SSE Generate Content streaming with cancellation, protected-span/glossary
  restoration, endpoint policy, and redacted API-key diagnostics. Linux `df9b0fe261bcbb3cba8d4b8660baa94c891ea44c`
  exposes the localized Google Gemini preset; l10n `f9d74a8f83a89540a58bba65477a5031031bd619`
  contains the 396-message generated bundle.
- Local Core workspace tests and strict Clippy passed. Linux formatting, GUI all-target check,
  strict Clippy, demo-provider tests (`136 passed; 3 ignored`), localization synchronization and
  three audits, Flatpak metadata validation, and diff checks passed. The deterministic fixture does
  not claim live Gemini account, credential, quota, or visual-copy coverage.
- Linux push/PR Native, Flatpak, and Foundation checks all passed for final head `df9b0fe`: push
  `29735086126`/`29735086106`/`29735086081`, PR `29735088589`/`29735088578`/`29735088610`.
  Core CI/Native SDK `29734921076`/`29734921078` also passed. PR #1 remains Draft/Open, Issue #1
  remains Open, and `release-manifest.toml` remains `unreleased` with the Core/Linux/l10n pins
  updated to these exact revisions. Stable signing, rollback, human review, complete acceptance
  scenarios, and other clients remain open.

## 2026-07-20 — Linux bounded concurrent document execution

Assumption: Linux is the first delivery target, so bounded worker concurrency can advance without
unfreezing the other clients or claiming a stable release.

- Linux code head `42b5ff36b3629c3001cda9177c1ba939ada1b478` runs up to four document jobs
  concurrently. Each job owns its event pump, cancellation handle, partial output, provider
  manager, and segment index; duplicate or fifth starts are rejected before persistence changes the
  job to Running. The Flatpak source pin follows `3e5b80df851a91c07fbef9cf98c494e142dc4332`.
- Added regressions for independent concurrent completion and targeted cancellation of one job while
  its survivor completes. Full local Linux validation passed: formatting, GUI all-target check,
  strict Clippy, demo-provider tests (`136 passed; 3 ignored`), Flatpak metadata, localization
  audits, synchronization, and diff checks.
- Code-head push/PR Native, Flatpak, and Foundation runs
  `29732668572`/`29732668556`/`29732668568` and `29732671353`/`29732671354`/`29732671362` passed.
  Documentation head `9dcc5818e757e663d63d2f7b783117057a57a0c0` then passed push/PR runs
  `29733047267`/`29733047292`/`29733047328` and `29733050760`/`29733050738`/`29733050725`.
  PR #1 remains Draft/Open and Issue #1 remains Open. Cross-platform clients, human
  accessibility/visual review, signing, rollback, and stable-release authorization remain open.
  Central coordination commit `cbde16f3323e9fdc68d800dde29ba461c1126c9e` and run `29733527316`
  passed both Linux and PowerShell validation.

## 2026-07-20 — Linux GTK routing candidate behavior evidence

Assumption: the Linux-first prerelease remains Draft/Open while the candidate-management callbacks
and remote GTK/Flatpak gates are verified, but human, cross-platform, signing, rollback, and stable
release gates remain incomplete.

- Linux code head `0658f0f31083e0eb90259784dc2bfd0e642412ed` exercises two sorted restored candidates
  through real GTK Down/Up callbacks, asserts order mutation and restoration, and restores the
  disabled-profile fixture state before continuing the existing lifecycle assertions. Documentation
  head `bf0906b97ac2f4a7065f0f9cfe7fe4f0e05841af` records the evidence; the Flatpak source pin
  remains on the code ancestor because the follow-up changes are documentation-only.
- Final code-head push Native/Flatpak/Foundation checks `29728346052`/`29728346055`/`29728346087`
  and PR checks `29728348382`/`29728348395`/`29728348472` passed. Documentation-head push checks
  `29728730611`/`29728730516`/`29728730520` and PR checks `29728732350`/`29728732354`/`29728732411`
  also passed. Earlier ordering and fixture-state failures `29727820986` and `29728076058` remain
  retained as evidence.
- Local Linux formatting, GUI all-target check, strict Clippy, demo-provider tests (`134 passed; 3
  ignored`), Flatpak metadata, localization audits, l10n synchronization, and diff checks pass;
  the host GTK test binary remains linker-limited, so Native CI is authoritative for GTK runtime.
- PR #1 remains Draft/Open and Issue #1 remains Open; no merge or stable release action occurred.

## 2026-07-20 — Linux document-job concurrency isolation evidence

Assumption: overlapping document starts remain fail-closed until bounded concurrent execution is
implemented; this Linux-first checkpoint proves isolation without claiming concurrency.

- Linux code head `36b81586b8b148d7adc08ecfc46203b2ef94af4d` adds
  `concurrent_document_start_is_rejected_without_interrupting_active_job`; Flatpak source pin
  `17d25816d2cecb763c331c02e55248efcb172a54` follows that code head, and documentation head is
  `9fbc995747400528c6680977bb8ee6c0a51d7506`. The regression rejects the second start with a
  typed configuration error, preserves the active cancellation path, and leaves the second job
  pending.
- Full local Linux validation passed (`135 passed; 3 ignored`) with formatting, GUI all-target
  check, strict Clippy, Flatpak metadata, l10n synchronization, three localization audits, and
  diff checks. Code-head push/PR Native, Flatpak, and Foundation runs
  `29730049695`/`29730049744`/`29730049648` and `29730052583`/`29730052576`/`29730052602` passed;
  docs-head push/PR runs `29730511966`/`29730512095`/`29730511907` and
  `29730513799`/`29730513772`/`29730513834` passed. Initial Flatpak pin failures
  `29729850476` and `29729852622` remain retained as corrective evidence.
- Central coordination run `29730453936` passed. PR #1 remains Draft/Open and Issue #1 remains
  Open; true concurrent document execution, other clients, signing, rollback, and stable-release
  authorization remain open.

## 2026-07-20 — Linux GTK routing-control evidence refresh

Assumption: the Linux-first prerelease remains Draft/Open while the latest automated evidence is
current but human, cross-platform, signing, rollback, and stable-release gates remain incomplete.

- Linux final evidence head `ca2d4fcefc411aabdf087e6bdde34bd1b0e170df` records the real GTK routing-
  profile dialog lifecycle regression for localized, keyboard-focusable candidate movement controls.
- Push Native/Flatpak/Foundation checks `29726610000`/`29726609962`/`29726609977` and PR
  Native/Flatpak/Foundation checks `29726612473`/`29726612471`/`29726612454` all completed
  successfully. Local Linux formatting, GUI check, strict Clippy, demo-provider tests (`134
  passed; 3 ignored`), Flatpak metadata validation, localization audits, and diff checks pass;
  the host GTK test binary remains linker-limited, so Native CI is authoritative for GTK runtime.
- PR #1 is still Draft/Open with no merge or release action. Issue #1 is Open and now points to
  this head and central coordination run `29724974241`; user-owned RFC/ADR drafts remain
  uncommitted and are not altered.

## 2026-07-20 — GitHub PR and issue triage checkpoint

Assumption: the Linux-first prerelease remains open while automated evidence is current and
human, cross-platform, signing, rollback, and stable-release gates remain incomplete.

- The canonical repositories were checked with the authenticated `getio0909` account. Only
  `getio0909/linguamesh-linux#1` has an open pull request; it remains Draft/Open and mergeable.
- PR #1 has no submitted reviews and no unresolved review threads. Native, Flatpak, and Foundation
  push/PR checks all pass at Linux head `f41e14af53b6d2d70b0f1d452ea32eda10d63095`.
- Central `getio0909/linguamesh-project#1` is the only open issue in the canonical set. Its body
  and the Linux PR body now point to current Core/l10n pins and central coordination run
  `29722312762`; neither item was closed, merged, or marked ready for release.
- The central release manifest remains `status = "unreleased"`; no source revision or artifact
  pin changed during this triage checkpoint, so workspace and release manifests remain consistent.

## 2026-07-20 — Core C ABI concurrent-control regression checkpoint

Assumption: the new Core revision is a test-only descendant for ABI safety evidence; the Linux
production pin remains unchanged until a functional client slice consumes it.

- Core `7068b1d565177c7541c6d6a35f8d8e7475dd126e` adds a concurrent host-control-call regression
  covering cancellation, shutdown, polling, engine-scoped buffer cleanup, and fail-closed polling
  after shutdown. The test joins twelve host threads before destroying the engine.
- Core local workspace formatting, strict Clippy, all-target/all-feature tests, locked workspace
  build, and cargo-deny checks passed. CI `29723055135` passed; Native SDK `29723055154` passed
  Linux, Android, Apple, and Windows jobs (the Windows runner emitted only an existing Node.js
  action deprecation annotation).
- This descendant is not promoted into the Linux source pin or release manifests. The Linux PR
  and central issue remain Draft/Open and the release train remains unreleased while human review,
  cross-client parity, signing, rollback, and stable-release gates remain incomplete.

## 2026-07-20 — Linux document queue boundary documentation checkpoint

Assumption: the Linux GTK queue-selection surface is implemented and must be documented separately
from the still-unverified concurrent document-execution boundary.

- Linux `8167481cbdea` corrects `docs/architecture.md` to describe explicit selection among
  multiple persisted jobs while retaining single-active-job execution as the current validation
  boundary. No runtime code, provider contract, persistence schema, source pin, or release-manifest
  value changed.
- The existing queue regression passed locally alongside 134 demo-provider tests (3 ignored),
  formatting, GUI check, strict Clippy, localization key/placeholder/visible-string audits,
  l10n synchronization, Flatpak metadata validation, and diff checks.
- Linux push Native/Flatpak/Foundation `29723524259`/`29723524286`/`29723524238` and PR
  `29723526302`/`29723526314`/`29723526298` all passed. PR #1 remains Draft/Open and Issue #1
  remains Open; no merge or stable release action was taken.

## 2026-07-20 — Linux Secret Service prompt protocol checkpoint

Assumption: a private D-Bus prompt fixture can verify adapter protocol handling, but cannot replace
real-user approval or visual/unlock-UX review evidence.

- Linux `8eaf7435094c` records the four-case prompt fixture: approved and dismissed `CreateItem`,
  plus approved and dismissed `Delete`. Approved cases complete the operation; dismissed cases
  return typed `SecureStorageUnavailable`. No runtime source pin or release-manifest value changed.
- Local `bash tools/run-secret-service-prompt-test.sh` passed all four cases. Linux push
  Native/Flatpak/Foundation `29724116604`/`29724116747`/`29724116697` and PR
  `29724118466`/`29724118446`/`29724118428` all passed. The Linux PR remains Draft/Open, the
  central issue remains Open, and the release train remains unreleased.

## 2026-07-20 — Linux document release-boundary consistency checkpoint

Assumption: the current Native/Flatpak gates verify queue listing, explicit job selection, and
sequential document-job execution, but do not establish concurrent document execution or stable
release readiness.

- Linux `01d7ba7` updates `docs/releasing.md` to distinguish the verified document-job path from
  the still-open concurrent-execution and stable-release boundaries. Central `PLANS.md` uses the
  same wording instead of listing already-supported archive formats as future work.
- Linux push Native/Flatpak/Foundation `29724628374`/`29724628347`/`29724628370` and PR
  `29724630281`/`29724630307`/`29724630279` all passed. No runtime code, source pin,
  workspace-manifest value, or release-manifest value changed. The Linux PR remains Draft/Open,
  Issue #1 remains Open, and no merge or stable release action was taken.

## 2026-07-20 — Linux Anthropic Messages GTK preset checkpoint

Assumption: Linux remains the priority client and Anthropic model discovery remains manual until a
provider catalog service is intentionally introduced; the GTK form must validate the model ID
before any host SecretRef is resolved.

- Linux final evidence head `f41e14af53b6d2d70b0f1d452ea32eda10d63095` consumes Core
  `a87aaf2bef7cca287c4a6faa8addd340e0245b0e` and l10n
  `e1ee15a5e9470e2c49077e52b4969597a5c8283f` (393 messages, bundle SHA-256
  `a30db30a44a16588db3b79b1958c849149677d40939cf5427413539b18d73282`).
- The l10n revision's Localization/Foundation runs `29720509844`/`29720509865` passed before
  Linux consumed the generated resources.
- The GTK provider form now exposes the localized Anthropic Messages preset, HTTPS `/v1/` default,
  manual Model ID field, saved-model restoration, focus/accessibility wiring, and local empty-model
  rejection before worker or Secret Service activity. The regression is folded into the existing
  single GTK lifecycle test to preserve GTK thread ownership.
- Local Linux formatting, all-target/all-feature check, strict Clippy, no-default-feature tests
  (`79 passed; 1 ignored`), demo-provider tests (`134 passed; 3 ignored`), localization audits,
  l10n synchronization, Flatpak metadata validation, and diff checks passed. The host cannot link
  the all-feature GTK test binary; Native CI is authoritative for that boundary.
- Initial malformed Flatpak pin and standalone-test attempts are retained as failures in Linux
  evidence. Final push Native/Flatpak/Foundation `29721751141`/`29721751155`/`29721751111` and PR
  `29721753040`/`29721753048`/`29721753045` all passed (Native/Flatpak/Foundation jobs
  `88284977586`/`88284977776`/`88284977563` and PR jobs `88284984553`/`88284984617`/
  `88284984699`). The Linux PR remains Draft/Open and the release train remains unreleased.

## 2026-07-20 — Core Anthropic Messages adapter checkpoint

Assumption: Anthropic model discovery is manual because this integration does not rely on a general
model-list endpoint; a selected model must be validated before any host secret request.

- Core `a87aaf2bef7cca287c4a6faa8addd340e0245b0e` adds the `linguamesh-provider-anthropic` crate,
  catalog entry, application dispatch, `/v1/messages` SSE streaming, required version/API-key
  headers, bounded response parsing, cancellation, protected-span restoration, typed HTTP errors,
  redacted diagnostics, and session credential clearing.
- Core provider tests cover fragmented UTF-8 SSE, headers/body, manual model listing, cancellation,
  and diagnostics redaction. Full Core workspace check, Clippy, tests, build, and cargo-deny passed;
  CI `29718737864` and Native SDK `29718737836` also passed.
- This is an unreleased provider-family checkpoint. Linux pins the revision and binds the GTK
  preset in the later checkpoint above; other clients remain deferred by the Linux-first priority.

## 2026-07-20 — Linux Core pin and Flatpak source checkpoint

Assumption: Linux should consume the verified Core adapter without claiming a Linux Anthropic UI
that has not been implemented.

- Linux `d15e915a516796b7565c34053b27a913c3a2aed4` pins Core
  `a87aaf2bef7cca287c4a6faa8addd340e0245b0e`, updates `Cargo.lock`, and refreshes the Flatpak
  source manifest. Local non-GTK checks, 134 demo-provider tests (3 ignored), localization audits,
  and Flatpak metadata validation passed.
- The host all-feature test binary could not link against its installed GTK runtime; the exact
  linker limitation is recorded in the Linux repository. Final push/PR Native, Flatpak, and
  Foundation runs `29719373604`/`29719373628`/`29719373607` and
  `29719371860`/`29719371922`/`29719371859` passed.
- The prior Flatpak stale-source-pin failure is retained in Linux evidence; no stable release is
  claimed. Prompted unlock approval, human visual/listening review, other clients, signing, and
  rollback remain open.

## 2026-07-20 — Linux Secret Service session-only recovery

Assumption: when persistent Secret Service storage fails, the user must receive an explicit,
localized session-only recovery choice and must never be silently downgraded or submit a
connection unintentionally.

- Linux `7df461ec5e0d1cc5736e2c2edef48333fcf5ff14` adds a modal after persistent credential-store
  failure. The session-only action disables Remember and focuses the credential field; Close
  leaves the connect operation unsubmitted. No credential value enters diagnostics.
- Local formatting, all-target/all-feature check, strict Clippy, 134 demo-provider tests (3
  ignored), localization placeholder audit, Flatpak metadata validation, and diff checks passed.
- The first attempt's placeholder-audit and stale-Flatpak-pin failures are retained:
  `29717314361`, `29717314328`, `29717312990`, and `29717312998`. After correction, Push
  Native/Flatpak/Foundation `29717769144`/`29717769121`/`29717769119` (jobs
  `88274285611`/`88274285568`/`88274285482`) and PR Native/Flatpak/Foundation
  `29717770780`/`29717770833`/`29717770765` (jobs `88274289941`/`88274290099`/`88274289936`)
  all completed successfully.

End-user prompt approval, visual/translated-copy review, other clients, signing, rollback, and
stable-release evidence remain open.

## 2026-07-20 — Linux read-only profile storage fallback

Assumption: a read-only profile database directory must reject persistent mutations without
silently creating or replacing state, while preserving session-only translation.

- Linux `06a9a76c8b964a9e0badc087b243a2fc4cd09544` adds
  `read_only_database_directory_reports_error_but_session_mode_still_works`. The test uses a
  private `0500` directory, verifies a typed persistence failure and no database creation,
  completes a session-only fake-provider translation, and rejects saved-profile deletion.
- Local Linux format/check/strict Clippy/full tests passed (`134 passed; 3 ignored`); Flatpak
  metadata validation and diff checks passed. Push Native/Flatpak/Foundation
  `29716832991`/`29716832970`/`29716832961` (jobs `88271663136`/`88271663160`/`88271663435`)
  and PR Native/Flatpak/Foundation `29716835042`/`29716835044`/`29716835030` (jobs
  `88271669287`/`88271669310`/`88271669196`) all completed successfully. Power-loss and broader
  SQLite VFS behavior remain open.

## 2026-07-20 — Linux descriptor-pinned database open

Assumption: Linux profile storage must keep the validated database inode fixed through Core's
migration/open call, not merely preflight a replaceable pathname.

- Linux source revision `0479dbcc7e629d48f1d65002cfd2cb43439b77d5` opens the private parent with
  `openat2(RESOLVE_NO_SYMLINKS)`, opens the final file with `O_NOFOLLOW | O_CLOEXEC`, and calls
  Core's narrowly validated `Storage::open_from_trusted_descriptor` on `/proc/self/fd/<fd>`.
  Ordinary Core paths still require SQLite no-follow.
- Local Linux format/check/strict Clippy/full tests passed (`133 passed; 3 ignored`), as did Core
  workspace format/Clippy/tests and the new trusted-descriptor storage regression. Push
  Native/Flatpak/Foundation `29715772612`/`29715772573`/`29715772602` (jobs
  `88268680841`/`88268680801`/`88268680852`) and PR Native/Flatpak/Foundation
  `29715774034`/`29715774044`/`29715774031` (jobs `88268684940`/`88268684830`/`88268684784`)
  all completed successfully. Core CI/Native SDK `29714966974`/`29714966969` also passed.
- The first code push's stale Flatpak pin failures (`29715256438`, `29715257892`) are retained as
  failures; corrected pin gates passed before this final status record. Prompted unlock UX,
  physical visual/manual review, other clients, signing, rollback, and stable release remain open.

## 2026-07-20 — Linux final database component no-follow hardening

Assumption: the Linux host should reject a final profile-database path component swapped to a
symbolic link during open, while the existing Core no-follow gate remains authoritative for SQLite.

- Linux source revision `651767d1493662f0631bf8e4245d0c525b684edc` adds final-component
  `O_NOFOLLOW | O_CLOEXEC` flags alongside static path checks and post-open inode comparison. A
  regression proves a symlinked database file is rejected without following or modifying its target.
- Local `cargo fmt --all -- --check`, all-target/all-feature offline check, strict Clippy, demo-provider
  tests (`132 passed; 3 ignored`), Flatpak metadata validation, and diff checks passed. Push
  Native/Flatpak/Foundation `29714091446`/`29714091453`/`29714091474` (jobs
  `88263531538`/`88263531565`/`88263531611`) and PR Native/Flatpak/Foundation
  `29714093213`/`29714093215`/`29714093207` (jobs `88263537445`/`88263537464`/`88263537556`)
  all completed successfully.
- Parent-directory replacement races still require a future directory-descriptor or `openat2`
  design. Prompted Secret Service/portal unlock UI, physical visual review, other clients, signing,
  rollback, and stable release remain open.

## 2026-07-20 — Linux Manual routing candidate cardinality

Assumption: Manual routing must identify exactly one provider/model; candidate chains belong to
Ordered and Automatic modes.

- Linux source revision `be985e0bf906f8c5ddcb229f4e6cc6b26d9efe7b` now deactivates extra Manual
  selections in the GTK editor and normalizes the save path to the first displayed candidate;
  Ordered and Automatic preserve their selected chains. The Linux status record includes the
  local format/check/Clippy/test/Flatpak evidence and remote run IDs. The final push checks are
  Native/Flatpak/Foundation `29713205178`/`29713205186`/`29713205194`; the final PR checks are
  `29713206482`/`29713206495`/`29713206461`; all six completed successfully.
- This remains a Linux-first configuration-surface checkpoint. Complete candidate-management
  release evidence, physical visual review, other clients, signing, rollback, and stable release
  remain open.

## 2026-07-20 — Linux third-party Ollama interoperability harness

Assumption: deterministic loopback fixtures prove the wire contract only; third-party daemon
interoperability requires an installed model and an external daemon that is not treated as a
release fixture.

- Linux head `8645caf3c0504b225a4a44d97fd634af9ab67d0c` adds the opt-in
  `tools/run-ollama-interop-test.sh` harness and an ignored worker regression covering `/api/tags`
  discovery, model selection, and translation without serialized secrets. Default CI keeps this
  external test ignored.
- Local validation passed with 131 tests passed and 3 ignored; formatting, all-target checks,
  strict Clippy, localization audits, Flatpak metadata, and diff checks also passed.
- Local and remote validation passed with 133 Rust tests passed and 12 ignored in Native CI; the
  local offline suite passed 131 tests with 3 ignored. Push Native/Flatpak/Foundation runs
  `29712165334`/`29712165338`/`29712165360` (jobs `88257689365`/`88257689383`/`88257689424`) and
  PR Native/Flatpak/Foundation runs `29712166849`/`29712166856`/`29712166851` (jobs
  `88257693555`/`88257693727`/`88257693563`)
  all completed successfully. Native PR evidence includes the fallback-confirmation regression,
  GTK AT-SPI fixture, and Orca Speech Dispatcher fixture.
- A Docker `ollama/ollama:0.11.10` daemon served `/api/tags` and `/api/chat` for
  `qwen2.5-0.5b-instruct:latest`; the opt-in harness reported `1 passed; 0 failed` without a
  credential. The public Qwen GGUF SHA-256 was
  `9ee36184e616dfc76df4f5dd66f908dbde6979524ae36e6cefb67f532f798cb8`, and the Ollama model
  digest was `91a334af822cdceab2234d673b0099d726d4944e1997b275744f4418e8b6a254`. The temporary
  model and daemon were removed. This closes the Linux third-party daemon/model gate for this
  prerelease checkpoint; GPU and stable-release evidence remain open.

## 2026-07-20 — Linux fallback-send confirmation remote evidence

- Linux source revisions `af200122e4862f6230d89268f5292f16438449bb` and Flatpak pin correction
  `8dba6129f1706f9f450537477ef6d45ef6531d87` add a localized, modal confirmation before an
  ordinary request with approved fallback enabled is dispatched. **Translate** grants one request;
  **Close** queues no worker command. The one-shot approval resets after dispatch.
- Push Native/Flatpak/Foundation runs `29711055269`/`29711055278`/`29711055281` (jobs
  `88254903448`/`88254903504`/`88254903474`) and PR Native/Flatpak/Foundation runs
  `29711056550`/`29711056549`/`29711056544` (jobs `88254906904`/`88254906952`/`88254906935`)
  all completed successfully. Prompted Secret Service/portal unlock UI, human listening,
  translated-copy review, other clients, signing, rollback, and stable release remain open.

## 2026-07-20 — Linux headless Orca remote gate evidence

- Linux source revision `a3bd4a3229088e24c8f1a6cd9fb6c1574ca55839` passed push Native/Flatpak/Foundation
  `29710531278`/`29710531303`/`29710531308` and PR Native/Flatpak/Foundation
  `29710532205`/`29710532203`/`29710532204`; all six jobs completed successfully.
- Native job `88253669507` records the AT-SPI named-control inspection and Orca Speech Dispatcher
  `SPEECH GENERATOR` output for the Linux application tree. This is headless process evidence only;
  the GTK4/Orca focus handoff limitation, human listening, translated-copy review, other clients,
  signing, rollback, and stable release remain open.

## 2026-07-19 — Linux localization fallback-template consistency final verification

- Documentation-only Linux head `81eed4f051e0f70406efbe47dca82e4f215c4cce` passed push
  Native/Flatpak/Foundation `29708338140`/`29708338160`/`29708338159` and PR
  Native/Flatpak/Foundation `29708339322`/`29708339336`/`29708339368`.
- Native and Flatpak evidence artifacts were non-expired; the Native push artifact was 5,590,542
  bytes. The earlier Flatpak pin failure and its manifest correction are documented in the Linux
  status history. This remains unsigned prerelease evidence.

## 2026-07-19 — Linux localization placeholder audit final verification

- Documentation-only Linux head `3f5f9ee00dd6359759cec0b96dbc8b6d8b89c70d` passed push
  Native/Flatpak/Foundation `29707758213`/`29707758214`/`29707758216` and PR
  Native/Flatpak/Foundation `29707759245`/`29707759269`/`29707759252`.
- The final Native push evidence artifact was non-expired at 5,590,080 bytes; push and PR Flatpak
  bundles/evidence and the PR Native artifact were also non-expired. The Linux release remains
  unsigned prerelease evidence.

## 2026-07-19 — Linux localization placeholder audit evidence

Assumption: literal fallback templates are part of the Linux visible-string contract, so source
validation should reject malformed braces and placeholder drift before GTK or release checks.

- Linux `3a20620eb95806baadb1b22ef4833302d0438fea` adds a dependency-free audit for literal
  `text`, `text_plural`, mnemonic, and template calls against the canonical l10n placeholder
  contract. Local validation checked 363 calls and passed alongside key/visible-string audits,
  l10n synchronization, formatting, and 131 Rust tests with 2 ignored.
- Push Native/Flatpak/Foundation `29707410914`/`29707410888`/`29707410893` and PR
  Native/Flatpak/Foundation `29707412487`/`29707412476`/`29707412474` all passed. Native and
  Flatpak evidence artifacts were non-expired; this is source-level prerelease evidence only.
- Human translated-copy/plural/visual review, Orca speech, end-user prompt approval, other clients,
  signing, rollback, distributable artifacts, and stable-release authorization remain open.

## 2026-07-19 — Linux performance baseline evidence

Assumption: performance numbers are meaningful only with their runner context and are retained as
trend evidence until a measured platform budget is established.

- Linux `4d6f041f388606dcc99311826ee4dbd3503edfd8` records the performance-baseline documentation
  head. The measured host baseline was DOCX `0.404s`, XLSX `0.382s`, and saved-routing dispatch
  `0.399s`; these values are machine-specific and not portable claims.
- Linux push Native/Flatpak/Foundation `29706935372`/`29706935324`/`29706935322` and PR
  Native/Flatpak/Foundation `29706936415`/`29706936411`/`29706936399` all passed. The current-head
  Native artifact was non-expired and its downloaded contents included the binary, source archive,
  checksums, SPDX SBOM, build context, and `LINUX-PERFORMANCE-BASELINE.tsv`.

## 2026-07-19 — Linux source archive and AT-SPI cleanup verification

Assumption: the Linux source snapshot is repository-only evidence and must retain explicit sibling
Core/l10n pins; a test-fixture cleanup fix is acceptable only when assertions remain unchanged.

- Linux `d5525263f2b5e339933a3b3c6dac7d21537ad990` records the repository-only
  `linguamesh-linux-source.tar.gz` and appends its SHA-256 to the native evidence checksums. It
  also makes AT-SPI fixture cleanup retry bounded deletion after the first source-archive attempt
  `29705840151` failed only because asynchronous portal files made `rm` return non-zero after all
  accessibility assertions passed.
- Final push Native/Flatpak/Foundation runs `29706120410`/`29706120412`/`29706120423` and PR
  Native/Flatpak/Foundation runs `29706121615`/`29706121557`/`29706121564` all passed. Native
  push/PR evidence artifacts were non-expired (5,584,791 and 5,584,680 bytes) and include the
  release binary, source archive, checksums, SBOM, and build context. This remains unsigned CI
  evidence; no standalone or stable source release is claimed.

## 2026-07-19 — Linux native release-mode evidence remote verification

Assumption: unsigned release-mode Linux binaries may be retained as prerelease CI evidence while
the stable release train remains closed.

- Linux `c6dae33698587e9db1fd8356ac7938d6bd7944ba` builds the GTK binary with `--release` and
  uploads the binary, `SHA256SUMS`, deterministic SPDX 2.3 `SBOM.spdx.json`, and fixed-context
  `BUILD-INFO.txt` in a non-expired artifact. Local non-GUI validation passed 131 tests with 2
  ignored, both localization audits, formatting, and diff checks; local GUI release linking is
  unavailable because this host lacks `gtk4.pc` and `libadwaita-1.pc`.
- Linux push Native/Flatpak/Foundation `29705491999`/`29705491988`/`29705492011` and PR
  Native/Flatpak/Foundation `29705493161`/`29705493148`/`29705493163` all passed. Native push and
  PR artifacts were non-expired (4,933,798 bytes each); Flatpak bundle and evidence artifacts were
  also non-expired. No signing, source archive, rollback, or stable artifact is claimed.

## 2026-07-19 — Flatpak checksum and SBOM evidence checkpoint

Assumption: Linux prerelease packaging should emit reproducible integrity evidence without implying
that an unsigned CI artifact is a stable release.

- Linux `dc1c0bc3485c95a57810ac658dab2c0a232f1af7` adds a dependency-free generator that hashes the
  Flatpak bundle and emits a deterministic SPDX 2.3 SBOM from the locked Cargo package set. The
  workflow uploads `SHA256SUMS` and `SBOM.spdx.json` sidecars after the SDK build.
- Local self-check validated the SHA-256 sidecar and SPDX schema with 230 locked packages. Push
  Native/Flatpak/Foundation `29704836385`/`29704836408`/`29704836382` and PR
  Native/Flatpak/Foundation `29704837824`/`29704837805`/`29704837827` all passed; non-expired
  evidence artifacts were present on both Flatpak runs.
- This remains CI-only prerelease evidence; no signing, notarization, or stable artifact is claimed.

## 2026-07-19 — Flatpak source-pin integrity checkpoint

Assumption: Flatpak CI must build the reviewed Linux application revision, or a source-compatible
ancestor with unchanged build inputs; packaging-only follow-up commits must not create a false green
gate.

- Linux `212de54d7eaa62eaeba8f7bc06297b2632d7a09b` updates the Flatpak manifest lineage and makes
  `tools/validate-flatpak-metadata.sh` compare the pinned Linux source with the current checkout
  (or an ancestor whose build inputs are unchanged). The workflow fetches full history and runs
  the check before the SDK build, using only a scoped Git safety setting in CI.
- Local metadata, localization, l10n synchronization, and diff checks passed. Push Native/Flatpak/
  Foundation `29704472892`/`29704472889`/`29704472884` and PR Native/Flatpak/Foundation
  `29704474147`/`29704474173`/`29704474207` all passed.
- This is an unreleased CI integrity checkpoint; no distributable or stable artifact is claimed.

## 2026-07-19 — Linux visible-string localization audit checkpoint

Assumption: complete Linux gettext coverage requires a repeatable source check that rejects
non-empty visible GTK literals, while empty labels used to clear transient state remain valid.

- Linux `2386d495123d3aeacf2b5815d0c45577808c7a44` adds the dependency-free
  `tools/check-visible-localization.py` audit for labels, titles, tooltips, placeholders, dialog
  actions, and direct list options. Native and Foundation workflows run it beside the 263-key
  catalog audit, and the foundation check requires the script.
- l10n `3362732be198450ff1ca00f30ec092aab2cf4189` contains 387 messages and all 59 generated
  resources. Local formatting, GUI-feature check, strict Clippy, 131 demo-provider tests with 2
  ignored, both localization audits, l10n synchronization, Flatpak metadata, and diff checks
  passed. The host GUI all-target linker limitation remains documented; remote Native covers it.
- Linux push Native/Flatpak/Foundation `29703945583`/`29703945586`/`29703945637` and PR
  Native/Flatpak/Foundation `29703946800`/`29703946783`/`29703946789` all passed.

## 2026-07-19 — Linux routing allow/deny and request-limit checkpoint

Assumption: provider/model allow-deny lists, minimum quality, and maximum request bytes are
non-secret Core routing constraints and should be editable on Linux first; validation remains
owned by Core and Edit/Save must preserve every other constraint.

- Linux `f64054924102b5611eb0e17761c7acb8b3a771dd` adds localized GTK controls and bounded parsers
  for provider/model allowlists and denylists, minimum quality, and maximum request bytes. The
  pure text helpers reject empty/invalid identifiers and non-positive numeric limits, while
  existing profile fields remain preserved.
- l10n functional bundle `c366124539d4e8c909c66ca7cc33fb16ed92e8b2` contains 387 messages and all
  59 generated resources; documentation-only correction `3362732` follows it. Local l10n `make
  check` and Linux format/check/clippy/non-GUI tests, localization audit/sync, Flatpak metadata,
  and diff checks passed. GUI all-target linking remains blocked by missing GTK symbols locally.
- Linux push Native/Flatpak/Foundation runs `29703371083`/`29703371057`/`29703371084` and PR
  Native/Flatpak/Foundation runs `29703373063`/`29703373065`/`29703373076` all passed.

## 2026-07-19 — Linux routing constraint controls checkpoint

Assumption: Core's non-secret routing constraints must be user-editable in the native Linux profile
dialog; editing visible controls must preserve future Core fields that the GTK surface does not yet
expose.

- Linux `0afc6aff9cf8b7a513827201c0e23de79de00553` adds localized controls for Automatic preference
  (none/local/quality/latency/cost), local-only routing, remote-candidate permission,
  privacy-sensitive requests, streaming capability, and document capability. Local-only and remote
  permission are mutually exclusive in the UI.
- Existing profile edits restore these controls and preserve hidden allow/model lists, minimum
  quality, and request-size limits when saving; helper tests cover preference mapping and preservation.
- l10n `b871a881f0eaf88cdda67a50f9221375f4c814ce` contains 377 messages and all 59 generated
  resources; Linux consumes the immutable revision and audits 253 catalog-backed source keys.
- Local Linux validation passed formatting, GUI all-target check, strict Clippy, 131 tests with 2
  ignored, localization synchronization/key audit, Flatpak metadata, and diff checks. GUI test
  linking remains environment-blocked by missing GTK 4 symbols.
- Remote Linux push Native/Flatpak/Foundation runs `29702482460`/`29702482435`/`29702482419` and
  PR Native/Flatpak/Foundation runs `29702484581`/`29702484564`/`29702484572` all passed.

## 2026-07-19 — Linux editor text-metrics checkpoint

Assumption: the editor should expose non-sensitive size feedback, while tokenization remains
provider/model dependent and must be presented as approximate.

- Linux `7ae70945c60934605d2eca82400a2278c753297f` adds localized source/output character counts
  and an approximate token estimate; buffer changes update the source metric immediately and
  output metrics refresh with the UI without logging source or output text.
- l10n `8adb1f4558e4b1d93a00ce03cf026a98d4a1a5ed` contains 360 messages and all 59 generated
  resources; Linux audits 236 catalog-backed source keys.
- Local l10n validation passed. Linux formatting, GUI all-target check, strict Clippy, the
  non-GUI demo-provider suite (131 passed, 2 ignored), localization sync/audit, Flatpak metadata,
  and diff checks passed. GUI test linking remains environment-blocked by missing GTK 4 symbols.

Remote Linux push/PR Native, Flatpak, and Foundation runs
`29701632363`/`29701632341`/`29701632350` and
`29701633693`/`29701633692`/`29701633700` all passed. Provider-specific token accuracy, full Orca
speech, manual visual review, other clients, signed artifacts, and a stable release remain open.

## 2026-07-19 — Linux duplicate routing-profile ID checkpoint

Assumption: allowing multiple profile IDs must not turn a new-profile action into an accidental
upsert of an existing record; only explicit Edit may replace a saved ID.

- Linux `21c89c7e9c671617477a6410240ff1fb0a0c9ff7` rejects a new routing profile when its validated
  ID already exists, while explicit Edit continues to update the selected record.
- l10n `712c4b1ac814ffbab265e4d0d40629d9d2bba02d` contains 359 messages and all 59 generated
  resources; Linux consumes that immutable revision and audits 235 source keys.
- Local Linux checks passed formatting, GUI all-target check, strict Clippy, 131 tests with 2
  ignored, localization synchronization/key audit, Flatpak metadata, and diff checks. Push
  Native/Flatpak/Foundation `29701039457`/`29701039458`/`29701039459` and PR
  Native/Flatpak/Foundation `29701040720`/`29701040695`/`29701040689` all passed. l10n
  Localization/Foundation `29700989823`/`29700989820` passed.

This closes accidental new-profile replacement without claiming complete fallback-chain editing,
full Orca speech, manual visual review, other clients, signed artifacts, or a stable release.

## 2026-07-19 — Linux multiple routing-profile IDs checkpoint

Assumption: a useful saved-profile manager must support more than one stable routing-profile ID;
existing edits must keep their ID immutable so document-job and selection references remain valid.

- Linux `f00cf23f95d33d7c3c9abbc35ebe2141233a80b8` adds a localized profile-ID field, validates
  1–128 ASCII letters/numbers/`.`, `_`, or `-` against the Core identifier rule, and locks the ID
  while editing an existing profile.
- l10n `7b832d765788e5ca64d7ba483b8ad12b3dd382d2` contains 358 messages and all 59 generated
  resources; Linux consumes the immutable revision and audits 234 source keys.
- Local Linux checks passed: formatting, GUI all-target check, strict Clippy, 131 tests with 2
  ignored, localization sync/key audit, Flatpak metadata, and diff checks. Push Native/Flatpak/
  Foundation `29700497023`/`29700497020`/`29700497017` and PR Native/Flatpak/Foundation
  `29700498213`/`29700498197`/`29700498198` all passed. l10n Localization/Foundation
  `29700369900`/`29700369903` passed.

This advances Linux profile management without claiming complete fallback-chain editing, full Orca
speech, manual visual review, other clients, signed artifacts, or a stable release.

## 2026-07-19 — Linux routing profile edit checkpoint

Assumption: complete Linux routing-profile management requires loading an existing non-secret
profile back into the same editor and replacing its stable ID, while preserving constraints that
the UI does not expose.

- Linux `a4dd4aa644335a3b6539db4d40473423c6292c71` adds an **Edit** action to saved routing-profile
  rows. The editor restores mode, explicit fallback consent, candidate selection/order, and stable
  ID; **Save routing profile** upserts that ID instead of creating a duplicate.
- The Linux worker regression now verifies same-ID replacement and a single updated record without
  endpoints, credentials, or source content. l10n `aea172c15f421da09a0c848accae7c443820fb27`
  adds the edit/save actions to all twelve official packs; the bundle contains 356 messages and
  the Linux source audit covers 232 keys.
- Local Linux validation passed. Push Native/Flatpak/Foundation runs
  `29699870066`/`29699870068`/`29699870071` and PR Native/Flatpak/Foundation runs
  `29699871302`/`29699871301`/`29699871311` all passed.

This closes the saved-profile edit/upsert slice without claiming complete fallback-chain editing,
full Orca speech, manual visual review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux routing candidate drag-order checkpoint

Assumption: Ordered routing needs both keyboard-accessible bounded moves and a direct pointer
gesture for placing a selected candidate before another; invalid drag payloads must fail closed.

- Linux `c0cdee8b729a6800904f6754f30221feb55f78e` adds GTK text drag sources and row drop targets
  to the routing-profile dialog. Dropping a candidate before another row rebuilds the visible list
  and preserves the resulting Ordered-mode sequence used by profile creation; localized icon labels
  and keyboard controls remain available.
- `move_routing_profile_id_before` rejects self, unknown, and missing target IDs; regression
  `routing_candidate_drag_reordering_is_bounded` covers forward, reverse, self, and unknown cases.
- Local Linux targeted/full validation passed. Push Native/Flatpak/Foundation runs
  `29699210798`/`29699210802`/`29699210801` and PR Native/Flatpak/Foundation runs
  `29699211832`/`29699211818`/`29699211830` all passed after a cleanup-only AT-SPI rerun.

This advances Linux candidate management without claiming complete profile editing, full Orca
speech, manual visual review, other clients, release artifacts, or a stable release.

## Current checkpoint

Linux routing configuration revision `c0cdee8b729a6800904f6754f30221feb55f78e` now exposes Core's
`Manual`, `Ordered`, and `Automatic` modes, explicit fallback consent defaulting off, focusable
candidate checkboxes, keyboard-focusable up/down candidate reordering, row drag-and-drop ordering,
and catalog-backed accessible names for icon controls. Local Linux validation passed with 133 tests
(`131 passed; 2 ignored`), GUI all-target check, strict Clippy, formatting, localization sync/audit,
Flatpak metadata, and diff checks. Push Native/Flatpak/Foundation runs
`29699210798`/`29699210802`/`29699210801` and PR Native/Flatpak/Foundation runs
`29699211832`/`29699211818`/`29699211830` all passed after a cleanup-only AT-SPI rerun. This is a
Linux configuration slice only and does not claim complete profile editing, Orca speech, other
clients, visual review, distributable artifacts, or a stable release.

## 2026-07-19 — Linux routing candidate accessibility-label checkpoint

Assumption: icon-only candidate movement controls need catalog-backed accessible names in addition
to tooltips; full screen-reader speech and manual visual review remain separate gates.

- Linux `84bed28deaa6034fb45e4f6c925fd5c2713c8782` uses `action.move_candidate_up` and
  `action.move_candidate_down` for both tooltips and GTK accessible `Label` properties.
- l10n `0d2d8c08f3dec5cd3044558b0b7c75f669a9535d` adds the two Linux-only keys to all twelve official
  packs and regenerates PO/MO resources; the Linux source audit covers 230 keys.
- Local Linux and l10n validation passed. Linux push/PR gates passed
  (`29698745522`, `29698745519`, `29698745529`; `29698747220`, `29698747211`, `29698747194`).

This strengthens icon-control semantics without claiming complete candidate management, Orca speech,
manual visual review, other clients, release artifacts, or a stable release.

## 2026-07-19 — Linux routing candidate-order checkpoint

Assumption: Ordered routing needs an explicit, keyboard-focusable way to change the sequence of
selected candidates; drag/drop and screen-reader copy review remain separate accessibility work.

- Linux `21d79530fbb7aedafe3fdc8a025e4db18c285fc4` adds bounded up/down candidate controls and
  rebuilds the GTK list before persistence, so the Core profile receives the exact Ordered-mode
  sequence selected by the user.
- `move_routing_profile_id` rejects unknown and out-of-range moves; the regression covers forward,
  reverse, boundary, and missing-candidate behavior.
- Local validation passed with 132 tests (`130 passed; 2 ignored`), GUI check, strict Clippy,
  localization/Flatpak audits, and diff checks. Push/PR Foundation, Native, and Flatpak gates all
  passed (`29697776890`, `29697776947`, `29697776897`; `29697778336`, `29697778335`, `29697778323`).

This remains a Linux configuration slice and does not claim complete candidate management, other
clients, visual/Orca review, release artifacts, or a stable release.

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
| Latest Linux Secret Service session fallback | Validated locally and remotely | Linux `7df461ec5e0d1cc5736e2c2edef48333fcf5ff14` provides an explicit localized session-only recovery modal after persistent Secret Service failure; the session path disables Remember and Close leaves Connect unsubmitted. Local 134-test/3-ignored, all-target, strict Clippy, localization placeholder, Flatpak, and diff checks passed. Final Push Native/Flatpak/Foundation `29717769144`/`29717769121`/`29717769119` and PR `29717770780`/`29717770833`/`29717770765` passed with jobs `88274285611`/`88274285568`/`88274285482` and `88274289941`/`88274290099`/`88274289936`; initial placeholder/stale-pin failures remain recorded above. |
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
| GitHub Actions | Passed | Core revision `123d5c4d7a76873e597895763ca5d78e1ea42ea0` remains validated; l10n revision `85b9d45569ce840c17dc0acc7d7366d6810be48e` passed Localization/Foundation gates; Linux head `7df461ec5e0d1cc5736e2c2edef48333fcf5ff14` passed push Native/Flatpak/Foundation `29717769144`/`29717769121`/`29717769119` and PR Native/Flatpak/Foundation `29717770780`/`29717770833`/`29717770765`; the session-only recovery, read-only storage, corrupt-database, offline-provider, aliased-export, localization, and routing checks passed in Native; central coordination remains separately tracked. |
| Non-functional repository heads | Published | Core head `d1c03ba84362c0c672c57045a59fc8092db470be`, l10n head `bd06a76bcd498748b520143c61964a92727d1b51`, and Linux behavioral/evidence head `7df461ec5e0d1cc5736e2c2edef48333fcf5ff14` are published. Current-head Linux Native/Flatpak/Foundation push and PR gates passed; the release manifest remains unreleased with no artifacts. |
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
