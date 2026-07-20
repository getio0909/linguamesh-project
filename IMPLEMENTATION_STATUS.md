# Implementation Status

Last updated: 2026-07-20

## 2026-07-20 — C ABI compatibility snapshot consumed by Linux

Assumption: native clients must negotiate Core semantic, ABI, protocol, catalog, and feature
dimensions through one versioned query before starting provider work; file-lease capabilities remain
outside this checkpoint.

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
