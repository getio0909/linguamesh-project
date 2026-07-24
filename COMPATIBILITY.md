# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

### Android persisted provider-profile metadata — 2026-07-24

Android code head `df8320e1898981814fe3135bcd41024e5d2e006e` consumes Core ABI 1 and persists bounded
non-secret provider-profile metadata in DataStore, restoring and re-registering profiles at
startup while keeping credentials in the Android Keystore broker. Local debug/release builds,
18-test JVM suites, instrumentation compilation, l10n synchronization, Foundation checks, and
lint pass; status head `4b2093bc94b8016c5eca721a18b5f049ac7330d8` records hosted validation
`30091714901` as passed. This is an unreleased client
checkpoint; Core-owned persistence, device restoration, document/background workflows, signing,
and stable-release evidence remain open. Central coordination workflow `30092269717` passed the
synchronized manifest, compatibility, documentation, and credential-scan checks.

### Windows native reference slice — 2026-07-24

Windows `d922b40c7db19aadebf77c2ea734ee5779ecc8ef` provides a C++20 state/event reference
surface, deterministic streaming/cancellation fixture, SecretRef-only credential boundary,
PasswordVault adapter, and WinUI/XAML shell. Local Foundation/source checks, CMake Release,
CTest (1/1), and hosted Windows validation pass (`30090288192`; Foundation `30090288187`),
including unsigned Debug/Release MSIX preparation. UI runtime, UI automation, accessibility,
generated Core-wrapper conformance, other-client parity, signing, and stable-release evidence
remain open.

### Linux-first provider proxy authentication

Core `cee5bd8abc5b35a50640c484bc4fbeedeb426745` adds schema 30 persistence for an optional
`ProviderProfile.proxy_auth_ref`. Linux `34b3194c5445f640141de8ad57195768aaa6c3d0` adds a
masked proxy credential field, session-only transport, explicit Secret Service persistence, and
reference-only restore behavior; l10n `f0b1c507d73f540f298a534303d0e6e63d44e87b` supplies the
source-revision-58 strings and generated catalogs. Credentials are parsed as bounded
`username:password`, applied as proxy Basic authentication across the built-in adapters, and are
never embedded in proxy URLs, SQLite, diagnostics, or logs. Linux push Native/Flatpak/Foundation
runs `29976201970`/`29976201964`/`29976201962` and PR Native/Flatpak/Foundation runs
`29976204361`/`29976204358`/`29976204331` passed for the exact documentation head. Other clients,
client-certificate TLS policy, human review,
signing, rollback, and stable-release authorization remain open; status stays `unreleased`.

## Unreleased compatibility matrix

### Linux-first provider custom trusted certificates

Core `913be49da8bc44f9c53baab7b918f2bb002fd64f` adds schema 29 persistence and bounded PEM
validation for an optional `ProviderProfile.trusted_certificates_pem`. Linux
`e8f0bcf2c55032cae59f40dba505c6e66a2fdd89` exposes the field, restores it with saved profiles,
and forwards it through Test connection and Connect; l10n
`d315efe808e05ce2fb0ee24c0247076298d57947` supplies the 474-message bundle. Core appends valid
certificates to system roots with TLS verification enabled; malformed bundles, private-key
material, control characters, and oversized input are rejected before provider requests. Local
Core/Linux/l10n synchronization and Flatpak checks passed. Client certificates, proxy
authentication, other clients, human review, signing, rollback, and stable-release authorization
remain open; status stays `unreleased`.

### Linux-first provider timeout settings

Core `b247155ad429639fdb65d3b063c3efc580ce46a4` adds schema 28 persistence for a bounded
streaming idle timeout. Linux `24b69a646a9463b13710502ce35a1bd0d15ee427` adds the localized GTK
control, restores it with saved profiles, defaults new profiles to 60 seconds, and pins Core/l10n
in Native and Flatpak metadata; l10n `2e223f9a416f4b461b72224f12c31cbf7981dae3` supplies the
471-message bundle. Values from 1 through 300 seconds are validated before host-secret requests,
applied to all four provider families, and reset after each received response chunk. A stalled-body
provider regression returns the typed timeout error. TLS policy, other clients, human review,
signing, rollback, and stable-release authorization remain open; release remains `unreleased`.

Core `e9a569f8bb6d66db4fdb1c9bd1d6834e93d10f39` adds schema 27 persistence for bounded total
request and connection-establishment timeouts. Linux `6fbf53da024bd37d64f93025222a57f7b0296d47`
adds the localized GTK controls, restores them with saved profiles, defaults new profiles to 30 and
10 seconds respectively, and pins Core/l10n in Native and Flatpak metadata; l10n
`46ca70b2863fa951b417eda7ce5848e152c46605` supplies the 469-message bundle. Values from 1 through
600 seconds for total requests and 1 through 120 seconds for connection establishment are validated
before host-secret requests and applied independently to OpenAI Chat/Responses/Azure, Anthropic,
Gemini, and Ollama transports.
Local Core workspace tests and strict Clippy, Linux locked checks/tests (`159 passed; 3 ignored`),
l10n audits/synchronization, and Flatpak metadata validation passed. Core CI/Fuzz/Native SDK
`29969609373`/`29969609372`/`29969609379`, l10n Localization/Foundation
`29969625867`/`29969625942`, Linux documentation-head push Native/Flatpak/Foundation
`29970072910`/`29970072901`/`29970072923`, and PR runs
`29970070485`/`29970070480`/`29970070516` passed for the exact revisions. Streaming-idle and TLS-specific timeout
fields, other clients, human review, signing, rollback,
and stable release remain open; status stays `unreleased`.

### Linux-first provider proxy settings

Core `7a9da3f467c5dec539dd8f7850b90b54ae712331` adds schema 25 persistence for an optional,
bounded non-secret `ProviderProfile.proxy_url`. Linux `c03535f82f07ed10c273fb250654c984540ed935`
adds the localized GTK field and pins Core/l10n in Native and Flatpak metadata; l10n
`bba90a89089c954bdfe1dcda19c210e6ea230b9e` supplies the 465-message bundle. Supported
schemes are HTTP, HTTPS, SOCKS5, and SOCKS5H. Userinfo, credentials, query strings, and non-root
paths are rejected before persistence. Core applies the URL to OpenAI Chat/Responses/Azure,
Anthropic, Gemini, and Ollama transports without emitting the value in diagnostics. Local Core
workspace tests and strict Clippy, Linux locked checks/tests (`159 passed; 3 ignored`), l10n
audits/synchronization, and Flatpak metadata validation passed. Linux push/PR Native, Flatpak, and
Foundation runs are `29966869662`/`29966869643`/`29966869658` and
`29966872082`/`29966872046`/`29966872048`, all passed for the exact Linux head. Proxy authentication, other clients, human review, signing, rollback,
and stable release remain open; status stays `unreleased`.

### Linux-first secret custom-header references

Core `28baaa2f85bb70b4fc6ecc4c07566e7004a659c5` adds schema 24 persistence for an optional
`ProviderProfile.secret_custom_headers_ref`. The host secret broker resolves that reference only
for an active connection; the OpenAI-compatible Chat, Responses, and Azure adapters parse the
bounded JSON in memory and never serialize or expose its values. Linux `e52a43cb361c5a395aa4e8ecd4d8d5252192d384`
adds a dedicated masked GTK field, clears it immediately, stores only a persistent Secret Service
reference when Remember is selected, and passes a session-only one-shot value otherwise. l10n
`32397a72c267677f04419a5084514f025f94a0bc` supplies the three Linux messages in the 462-message
bundle. Local Core/Linux/l10n checks and Linux push Native/Flatpak/Foundation runs
`29965156891`/`29965156910`/`29965156886` plus PR runs
`29965159879`/`29965159874`/`29965159952` passed for the exact Linux head. The PR and Issue remain
open. Other clients, human review, signing, rollback, and stable release remain open. Release
remains `unreleased`.

### ABI 1 provider metadata projection

Core `530e6ea75ef3ccba5defd264227fb6dd6802e17a` adds optional non-secret `organization`, `project`,
and bounded `custom_headers_json` fields to `TranslateTextCommand` without changing protocol 1.
The C ABI validates credential-shaped identifiers and unsafe headers before host-secret requests,
then forwards accepted metadata to the OpenAI-compatible adapter; Android exposes compatible
optional parameters. Linux `5cf0fcd133c7df823d4c33f934786a1c940670bb` pins the same Core source in
Native and Flatpak metadata while retaining the direct typed-Rust path. Core CI/Fuzz/Native SDK
`29961301539`/`29961301501`/`29961301583` and Linux push/PR Native/Flatpak/Foundation
`29961456792`/`29961456832`/`29961456791` and `29961459180`/`29961459196`/`29961459185` passed.
This is prerelease ABI evidence only; other-client conformance, human review, signing, rollback,
and stable release remain open.

### Linux Azure custom-header application wiring

Core `cf08384c829ca1b95ecfc79d23bc5b0feb3a701f` adds the existing bounded custom-header contract
to `AzureOpenAiConfig` and forwards it through `ProviderManager` into Azure Chat Completions.
Provider and application loopback regressions prove safe headers are applied without replacing the
`api-key`; organization/project headers remain limited to Chat Completions and Responses.

l10n `294e593ab2c71b9ab0ea3475c35ebc61bca2bbc6` remains source revision 51 with 459 messages.
Linux `61a7317746adea35f35a88f948a94f7e8223bac1` pins the exact Core/l10n/Flatpak inputs and
records local GUI, Clippy, 158-pass/3-ignored demo-provider, localization-audit, synchronization,
and metadata evidence. Core CI/Fuzz/Native SDK `29958775964`/`29958776018`/`29958776042` and Linux
push/PR Native/Flatpak/Foundation `29959014144`/`29959014132`/`29959014154` and
`29959016415`/`29959016426`/`29959016416` passed; coordination `29959537603` also passed.
Release remains `unreleased`.

### Linux provider profile bounded custom headers

Core `be5b7220587289be78b7654d979099c57ea4cc6d` adds schema 23 persistence and canonical JSON
validation for optional non-secret custom request headers. The contract permits at most 16
headers, 128-byte token names, and 2 KiB values; authorization, credential-shaped, and built-in
metadata names are rejected. The OpenAI Chat Completions and Responses adapters apply safe headers
without replacing authentication metadata, while proxy settings and secret custom headers remain
out of scope.

l10n `294e593ab2c71b9ab0ea3475c35ebc61bca2bbc6` contains source revision 51 and 459 messages.
Linux `1e3a96b18990ea4f7b8ba85faed2df4407ed18b9` binds and restores the localized field and pins
the exact Core/l10n/Flatpak inputs. Local Core, Linux, l10n, localization, and Flatpak checks
passed. Core CI/Fuzz/Native SDK `29956720294`/`29956720284`/`29956720340`, l10n
Localization/Foundation `29956431231`/`29956431233`, and Linux push/PR Native, Flatpak, and
Foundation gates `29956837428`/`29956837112`/`29956837081` and
`29956840773`/`29956840966`/`29956840730` passed. Release remains `unreleased`, and
central coordination workflow `29957596432` passed. Cross-client compatibility, manual
visual/Orca review, signing, rollback, and stable-release acceptance remain open.

### Linux provider profile project application wiring correction

Core `8717251375290cc3f825cee86d467ab1c60dd508` corrects the application-layer construction of
both OpenAI Chat Completions and Responses configurations so persisted `ProviderProfile.project`
is forwarded as `OpenAI-Project`. Header-enforced Chat and Responses regressions passed locally;
Core CI/Fuzz/Native SDK runs `29953260332`/`29953260318`/`29953260372` passed. Linux code head
`69b2d4510c51e9f34d7807687e6536ec411b1611` consumes that Core revision with l10n
`ec538de57c1edc198fa13d3dfc1de576ee9b2c12`; final status head
`ec4b32d7dd0efd6d00d27d3a60750307b9c6ff31` passed Linux push/PR Native, Flatpak, and Foundation
gates `29954097684`/`29954097694`/`29954097748` and `29954100960`/`29954102119`/`29954100976`.
This corrects the earlier project persistence checkpoint; release remains `unreleased` and
other clients, human review, signing, rollback, and stable-release acceptance remain open.

### Linux provider profile region/account checkpoint

Core `158ade12cf1e3284d4b8a0883e771dd62abcff97` adds schema 22 optional bounded non-secret
`ProviderProfile.region` and `ProviderProfile.account_identifier`, with validation and persistence
but no provider-specific wire interpretation. Linux status head `69fb128` (runtime/packaging
head `761a931538fc49c30d759089185cdf21cf2015ab`)
binds, restores, clears, and preserves both fields through GTK Test connection and Connect; l10n
`ec538de57c1edc198fa13d3dfc1de576ee9b2c12` contains 456 messages. Local Core, l10n, and Linux
checks passed. The final status head `69fb128` passed push Native/Flatpak/Foundation runs
`29952240768`/`29952240852`/`29952240819` and pull-request Native/Flatpak/Foundation runs
`29952245004`/`29952244151`/`29952244148`. An earlier stale-pin Flatpak attempt (`29951517923`,
`29951520086`) was superseded. This remains unreleased Linux-first evidence; other clients,
provider-specific semantics, human review, signing, rollback, and stable-release acceptance remain
open.

### Linux provider profile project checkpoint

Core `17342ba0bf19dd4978707a7875bc7dbe85efae54` adds schema 21 optional bounded non-secret
`ProviderProfile.project`, with validation, persistence, and an OpenAI-compatible `OpenAI-Project`
request header for Chat Completions and Responses. Linux status head
`108cba3e5b1cb128cf77003fc0cb530e822bd7f7` binds, restores, and clears the localized field; l10n
`fea84439f035f30b009532b40d7f67a30049846c` contains 450 messages. Local Core, l10n, and Linux
checks passed; Core CI/Fuzz/Native SDK, l10n Localization/Foundation, and Linux push/PR
Native/Flatpak/Foundation gates all passed (`29949462141`/`29949462126`/`29949462107` and
`29949468527`/`29949466704`/`29949468689`). This remains unreleased Linux-first evidence; other
clients, human review, signing, rollback, and stable-release acceptance remain open.

### Linux provider profile organization checkpoint

Core `1b8737bbad3d1bb6df7cd5c852d51838f72b9ca1` adds schema 20 optional bounded non-secret
`ProviderProfile.organization`, with validation, persistence, and an OpenAI-compatible
`OpenAI-Organization` request header for Chat Completions and Responses. Linux head
`88114a7a08e814e6b75ee0fe0a5814573104fd08` binds and restores the localized field; l10n
`94438a6a9ff8148cadad605c4760f88110d78984` contains 447 messages. Core and l10n checks passed;
Linux push/PR Native, Flatpak, and Foundation gates
`29946828234`/`29946829779`/`29946829000` and
`29946831489`/`29946831590`/`29946832071` passed. This remains unreleased Linux-first evidence;
other clients, human review, signing, rollback, and stable-release acceptance remain open.

### Linux provider profile notes checkpoint

Core revision `072d6b92df875153a60a9d1256ab814891fe775b` adds schema 19 optional bounded
`ProviderProfile.user_notes`. Linux runtime/packaging revision `eaa9dc3e6bf07222fe3b2da5c078d39e9419b88d` binds the
localized Profile notes field, restores it with saved profiles, clears it for new profiles, and
keeps it out of provider requests and diagnostics. l10n revision
`6aa074e48058bb411d09b2783cd27ba415dc7c55` contains 444 messages. Final status revision
`3c1a4ad5e9f8d8ae613c5b2f8aa447d057212de0` records passed Linux Native/Flatpak/Foundation push
and pull-request gates. This remains unreleased
Linux-first evidence and does not satisfy cross-client or stable-release acceptance.

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0`; the versioned `CompatibilitySnapshot` exposes Core semantic version, ABI major, protocol version, provider catalog version, and enabled features through `lm_engine_get_compatibility`; `file_lease_v1` adds bounded path, POSIX descriptor, Android ParcelFileDescriptor, Windows handle, temporary-path, and output-path lifecycle states with monotonic expiry/revocation checks; `protected_spans_v1` shields common structured spans, applies bounded request-level glossary rules, and restores immutable or required target terms across streamed output; `long_text_chunking_v1` splits oversized UTF-8 input on semantic boundaries, streams chunks in order, and propagates cancellation; `bounded_text_document_v1` validates bounded UTF-8 TXT/Markdown/SRT/WebVTT/CSV/JSON/HTML, bounded DOCX/PPTX/XLSX/EPUB packages, and text-based PDF pages, preserves line endings, cue IDs, headers, timestamps, delimiters, quoted fields, variable-width rows, selected-column boundaries, JSON keys, primitive values, whitespace, escaping, HTML tags, attributes, scripts, styles, supported OOXML text nodes, EPUB metadata/navigation/spine/CSS/resources, PDF page association and available coordinates, and OPF language updates while retaining package non-text resources, classifies Markdown fences and subtitle structure, and reconstructs completed segments; subtitle warnings report cue-level line-length and reading-speed guidance with configurable limits; deterministic glossary CSV import/export validates a fixed schema, 4 MiB bound, and 256-row bound; `TranslationPrivacyMode` carries an explicit Standard/Incognito local persistence policy with serde-default compatibility; schema 3 adds bounded translation history, schema 4 persists its enable/disable policy, schema 5 adds optional bounded translation memory with versioned identity and exact controls, schema 6 adds bounded document-job/segment snapshots, schema 7 adds transactional paused-job state and restart resumability, schema 8 adds validated non-secret document source/target locales, provider/model IDs, and bounded glossary options, schema 9 expands stored document formats for subtitle, CSV, JSON, and HTML jobs, schema 10 persists bounded DOCX package bytes, schema 11 persists bounded PPTX package bytes, schema 12 persists bounded XLSX package bytes, schema 13 persists bounded EPUB package bytes, and schema 14 persists bounded PDF package bytes with structured fidelity warnings; the provider catalog now includes a loopback-only `ollama` preset for native `/api/tags` discovery and `/api/chat` NDJSON streaming alongside the OpenAI-compatible `/v1/` adapter; Core HTTP adapters parse bounded numeric or HTTP-date `Retry-After` hints into an optional backward-compatible error field for Linux retry policy; public `RetryPolicy` validates bounded backoff, jitter, provider hints, failure thresholds, and cooldowns; Core storage also exposes a narrowly validated `/proc/self/fd/<fd>` open for hosts that pin a private inode while ordinary paths retain SQLite no-follow | Functional source `8b096478b1623bdaf5105e8a8f59e55e2fa8015d` passed local workspace, strict Clippy, full tests, FFI lease-expiration, and C/C++ Native SDK smoke; Core CI `29784269272` and Native SDK `29784269356` passed, unreleased; default budget is an approximate 16 KiB UTF-8 byte bound |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1`; 441 canonical messages including Linux-only status, partial-output, text-import, opt-in image-only PDF OCR controls and errors, glossary CSV import/export and rule-validation errors, PDF fidelity and subtitle readability warnings, document-job actions/dialog/status/tooltip controls, exported-output open/failure actions, Incognito privacy controls, history and translation-memory controls/status, translation-export, provider-profile, provider preset labels/tooltips, routing-profile ID/edit/save/candidate-order/accessibility/duplicate-ID/routing-constraint labels, provider/model allow-deny lists, quality/request-size limits, source-target, onboarding-stage, active-provider, notification, draft-note, locale selector language names, fixed provider/file/worker errors, reducer-state/category guidance, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, diagnostics labels/state values, explainable routing detail labels, Secret Service prompt-dismissal guidance, GTK drag-fixture label, built-in provider default names, editor text-metrics labels, Anthropic Messages preset/model validation copy, Core/loopback startup plus profile-storage error copy, open-source license action/dialog/tooltip labels, and About version/compatibility labels; paired PO/MO Linux resources | CI-verified development bundle at l10n revision `a65a327a8418332e50d9ab302fca24508e7266ef`, 59 generated artifacts, unreleased |
| Android client | `0.1.0-alpha.1` | Native Kotlin/Compose onboarding and translation-state slice with Keystore credential storage, Core ABI 1 adapter source, generated l10n resources, and debug/release preparation pinned to Core `8837e593` and l10n `3724cc9d`; Android workflow run `29932649692` passed AAR rebuild/checksum/JNI verification, debug/release builds, 16 JVM tests per variant, instrumentation compilation, and lint | Unreleased; device/instrumentation execution, provider credentials, document/history/routing/background workflows, signing, and distribution remain open |
| Windows client | `0.0.0-dev` | Foundation repository only; no native product slice or artifact | Unreleased |
| macOS client | `0.1.0-alpha.1` | SwiftUI/AppKit text slice, ABI 1/protocol 1, Core `0db51464`, l10n `7e8c987`; Native CI `29765906044` passed build, tests, bundle, and ad-hoc signing smoke check | Unreleased |
| Linux client | `0.1.0-alpha.2` | GTK client with provider/routing/document slices at Linux `0d7b392`, Core `8b096478`, and l10n `a65a327`; Linux pins the five-dimension Core compatibility contract through the direct Rust layer and requires `file_lease_v1`; generic OpenAI-compatible `/v1/` behavior includes a deterministic LM Studio-style fixture; document imports validate the selected URI lease during asynchronous GIO reads and revoke it after bounded bytes are copied; explainable routing diagnostics expose eligible/rejected candidates, stable rejection reasons, ranking inputs, and fallback order without secrets; retryable routing fallback consumes Core `RetryPolicy` for bounded eight-second backoff with stable jitter, optional Retry-After hints, shutdown cancellation, and a two-failure/30-second in-memory circuit breaker; the bundled read-only license-notices dialog exposes GTK 4/LGPL/MIT/first-party notice text; the localized About dialog exposes only application version and Core semantic version/ABI/protocol compatibility; status head `b71e209` passed local checks and push/PR Native/Flatpak/Foundation gates `29939876568`/`29939877021`/`29939876501` and `29939879474`/`29939879969`/`29939879856` | Unreleased |

## Linux FileLease document-import checkpoint

Core `8b096478b1623bdaf5105e8a8f59e55e2fa8015d` adds `file_lease_v1`, a bounded domain lifecycle
for desktop and temporary/output paths, POSIX and Android ParcelFileDescriptor-derived descriptors,
and duplicated Windows handles. Core tests cover invalid resource values and fail-closed access after
expiry or explicit revocation; the FFI suite includes the expiry regression and the C/C++ smoke test
passes. The ABI advertises the feature but does not yet expose platform-handle transfer or lease
creation/revocation calls.

Linux `f95780db3dd05fdccfe47af254f73c5107587077` consumes the exact Core pin, requires
`file_lease_v1` during compatibility negotiation, validates the lease around asynchronous portal/GIO
document reads, rejects expired decoding, and revokes the lease after bounded bytes are copied into
the document job. Local no-default (`81 passed; 1 ignored`) and demo-provider (`145 passed; 3 ignored`)
tests, strict Clippy, localization audits, Flatpak metadata validation, and diff checks passed.
Linux PR Native/Flatpak/Foundation runs `29785377479`/`29785377512`/`29785377513` passed with jobs
`88495671317`/`88495671975`/`88495671980`; this remains unreleased Linux-first evidence and does not
claim native ABI lease transport, other clients, signing, rollback, or stable release. Central
coordination `29785760751` passed Linux/PowerShell jobs `88496851860`/`88496851914`.

## Linux explainable routing diagnostics checkpoint

Linux source/pin head `ab82f36963a63f43091d94e960541fc173175724` carries Core's bounded routing
decision summary through typed Worker events into the localized GTK diagnostics panel. The summary
includes eligible candidate keys, rejected keys with stable reason codes, ranking inputs, and the
configured fallback order; endpoints, credentials, source text, and translated output are excluded.
The localized template is supplied by l10n `737d890e60fd34f15fd8708698448ef9ab96299f` (426
messages). Push Native/Flatpak/Foundation gates `29773735297`/`29773735296`/`29773735294` and PR
gates `29773738883`/`29773738887`/`29773738924` passed. Documentation head `458a920` also passed
push Native/Flatpak/Foundation `29774707677`/`29774707852`/`29774708075` and PR
`29774709730`/`29774709849`/`29774710165`. This is unreleased Linux-first evidence; visual/
translated-copy review, Orca acceptance, other clients, signing, rollback, and stable release
remain open.

## Linux-first shared RetryPolicy checkpoint

Core revision `8790eb41a52c4e2c908044699e8c12597d3c42a5` adds the public bounded `RetryPolicy`
domain contract with standard backoff, jitter, provider `Retry-After`, circuit-failure, and
cooldown limits. Linux source/pin `3ff10f4c9f54d82b7c43a0204946033cb063b92f` consumes the policy for
approved routing fallback and circuit state; documentation/source-pin head
`eb7e57869580917494d719ac61ec861c1c8bcff4` records the compatibility pin. Core CI/Native SDK
`29778375725`/`29778375728` and Linux push Native/Flatpak/Foundation
`29778624703`/`29778624674`/`29778624715` plus PR
`29778626906`/`29778626865`/`29778626849` passed. This is unreleased Linux-first evidence; other
clients, live provider quota behavior, human review, signing, rollback, and stable release remain
unverified.

Final Linux status head `857dac37c1d54c3987b69bd5b96e357fb8977e82` passed push
Native/Flatpak/Foundation `29779357668`/`29779357649`/`29779357690` and PR
`29779360891`/`29779360949`/`29779361066`, confirming the recorded evidence head and Flatpak pin.

## Linux-first RetryPolicy deserialization hardening

Core revision `6e8c40224943a6ba892e5a064fb3b00657b3bf47` validates every serialized `RetryPolicy`
through the bounded constructor, so restored policy data cannot bypass backoff, jitter, circuit
threshold, or cooldown limits. Linux documentation/source-pin head
`5b807093c05995a3029e60bb3563ba55200597f9` consumes that exact Core revision and updates the
Flatpak manifest. Foundation/Native/Flatpak gates `29780440569`/`29780440461`/`29780440421`
passed with jobs `88480156512`/`88480156210`/`88480155904`. This remains unreleased Linux-first
evidence; other clients, stable distribution, signing, rollback, and live quota behavior remain
unverified.

## Linux-first bounded routing retry checkpoint

Core revision `c03bd205e1d135c024f3a0a767dd94770030a723` adds an optional `retry_after_ms` field to
typed translation errors. Numeric and HTTP-date `Retry-After` values are parsed and capped at
sixty seconds by the four HTTP provider adapters, while legacy error payloads remain valid when the
field is absent. Linux source/pin head `4b345763af46bc4cd23bdecc54ecb6b8b52e597a` applies an
eight-second maximum backoff with deterministic candidate-key jitter, cancellation-aware waits,
and an in-memory circuit that opens after two retryable failures for thirty seconds. Candidate keys
contain only safe provider/model identifiers; document jobs and explicit single-provider fallback
remain separate paths. Core CI/Native SDK `29776309259`/`29776309263` passed. Linux push
Native/Flatpak/Foundation `29776662997`/`29776663334`/`29776662987` and PR
`29776667400`/`29776667014`/`29776667068` passed. The follow-up documentation head
`2a75ac0449dcc577ec263b73929c4c89ca10f063` also passed push Native/Flatpak/Foundation
`29777101390`/`29777101871`/`29777101540` and PR `29777102953`/`29777103017`/`29777103023`.
Central coordination commit `adaa2a16e127b508b630c3a7711a2cb19d26ecb0` passed workflow
`29777574182`.
This remains unreleased Linux-first evidence; provider quota behavior, physical review, other
clients, signing, rollback, and stable release remain open.

## Core Anthropic Messages adapter checkpoint

Core source revision `a87aaf2bef7cca287c4a6faa8addd340e0245b0e` adds the
`linguamesh-provider-anthropic` adapter and catalog entry. It validates HTTPS or loopback endpoints,
uses the Anthropic Messages `/v1/messages` streaming contract with required version/API-key headers,
supports manual model listing because no general model-list endpoint is assumed, bounds SSE decoding,
restores protected spans, cancels in-flight work, and clears session credentials. Core application
connection rejects a missing manual model before asking the host secret broker. Core CI `29718737864`
and Native SDK `29718737836` passed; this remains unreleased provider-family evidence.

## Linux-first Core pin and Flatpak source checkpoint

Linux source revision `d15e915a516796b7565c34053b27a913c3a2aed4` pins Core
`a87aaf2bef7cca287c4a6faa8addd340e0245b0e` and refreshes the lockfile and Flatpak source manifest.
Local non-GTK checks, demo-provider tests (`134 passed; 3 ignored`), localization audits, and
Flatpak metadata validation passed. The host's all-feature test binary could not link against its
installed GTK runtime, so full GTK/portal/Secret-Service/AT-SPI/Orca/Wayland evidence is taken from
CI. Final push Native/Flatpak/Foundation runs `29719373604`/`29719373628`/`29719373607` and PR
runs `29719371860`/`29719371922`/`29719371859` all passed. The later Anthropic GTK preset is
recorded below; prompted unlock approval, human visual/listening review, other clients, signing,
rollback, and stable release remain open.

## Linux-first Secret Service session-fallback checkpoint

Linux source revision `7df461ec5e0d1cc5736e2c2edef48333fcf5ff14` adds an explicit localized
recovery modal after a persistent Secret Service store failure. The user may choose a clearly
labeled session-only path, which disables Remember and focuses the credential field; closing the
modal leaves the connection unsubmitted. Local formatting, localization placeholder audit,
Flatpak metadata validation, 134 tests (3 ignored), all-target check, strict Clippy, and diff
checks passed. The first remote attempt is retained as a failure because the new fallback literal
did not match the canonical catalog and the Flatpak source pin was stale (`29717314361`,
`29717314328`, `29717312990`, `29717312998`). After the corrected literal and pin, final Push
Native/Flatpak/Foundation runs `29717769144`/`29717769121`/`29717769119` and PR
Native/Flatpak/Foundation runs `29717770780`/`29717770833`/`29717770765` all passed, with jobs
`88274285611`/`88274285568`/`88274285482` and `88274289941`/`88274290099`/`88274289936`.
End-user prompt approval, visual/translated-copy review, other clients, signing, rollback, and
stable release remain open.

## Linux-first Anthropic GTK preset checkpoint

Linux source revision `f41e14af53b6d2d70b0f1d452ea32eda10d63095` consumes Core
`a87aaf2bef7cca287c4a6faa8addd340e0245b0e` and l10n
`e1ee15a5e9470e2c49077e52b4969597a5c8283f` (393 messages, bundle SHA-256
`a30db30a44a16588db3b79b1958c849149677d40939cf5427413539b18d73282`). The GTK form exposes the
localized Anthropic Messages preset with an HTTPS `/v1/` default and manual Model ID input; empty
IDs fail locally before any worker connection or host SecretRef resolution. Final push and PR
Native/Flatpak/Foundation checks all passed: push `29721751141`/`29721751155`/`29721751111` and
PR `29721753040`/`29721753048`/`29721753045`. This remains unreleased; human visual/copy review,
prompt approval, other clients, signing, rollback, and stable release remain open.

## Linux-first final database no-follow hardening checkpoint

Linux source revision `651767d1493662f0631bf8e4245d0c525b684edc` opens the final profile-database
component with `O_NOFOLLOW | O_CLOEXEC`, retaining static path checks, inode comparison, and the
Core SQLite no-follow gate. The symlink regression proves the target is not followed or modified;
local format/check/Clippy/full-test, Flatpak metadata, and diff validation passed. Push
Native/Flatpak/Foundation `29714091446`/`29714091453`/`29714091474` and PR
Native/Flatpak/Foundation `29714093213`/`29714093215`/`29714093207` all passed. Parent-directory
replacement races still require a future directory-descriptor or `openat2` design; this is
prerelease evidence only and does not advance other clients, signing, rollback, or stable release.

## Linux-first descriptor-pinned database checkpoint

Linux source revision `0479dbcc7e629d48f1d65002cfd2cb43439b77d5` pins the private parent with
`openat2(RESOLVE_NO_SYMLINKS)`, opens the final file with `O_NOFOLLOW | O_CLOEXEC`, and hands Core
the live `/proc/self/fd/<fd>` path. The regression survives a rename-and-symlink replacement of
the visible parent and keeps migrations in the original directory. Core
`b5febb8daec88ab0401af4d6ceb20ec848f65138` ordinary
paths remain no-follow; only the exact trusted descriptor form is accepted. Push
Native/Flatpak/Foundation `29715772612`/`29715772573`/`29715772602` and PR
Native/Flatpak/Foundation `29715774034`/`29715774044`/`29715774031` all passed. The Linux PR remains
draft; prompted unlock UX, visual/manual review, other clients, signing, rollback, and stable
release remain open.

## Linux-first read-only profile storage checkpoint

Linux source revision `06a9a76c8b964a9e0badc087b243a2fc4cd09544` adds the regression
`read_only_database_directory_reports_error_but_session_mode_still_works`. A private `0500`
profile directory rejects persistent startup with a typed persistence error, does not create a
database file, and still permits session-only fake-provider translation. The local targeted and
full Linux suites passed. Push Native/Flatpak/Foundation `29716832991`/`29716832970`/`29716832961`
and PR Native/Flatpak/Foundation `29716835042`/`29716835044`/`29716835030` all passed, with jobs
`88271663136`/`88271663160`/`88271663435` and `88271669287`/`88271669310`/`88271669196`.
Corrupt-database and `ENOSPC` fail-closed boundaries remain separately recorded; power-loss and
broader SQLite VFS behavior remain open.

## Linux-first headless Orca checkpoint

Linux source revision `a3bd4a3229088e24c8f1a6cd9fb6c1574ca55839` adds an isolated Xvfb/private-D-Bus
Orca fixture. `python3-pyatspi` confirms the production `Stop translation` control, while Orca with
Speech Dispatcher records `SPEECH GENERATOR` output for the Linux application tree. Push
Native/Flatpak/Foundation `29710531278`/`29710531303`/`29710531308` and PR
Native/Flatpak/Foundation `29710532205`/`29710532203`/`29710532204` passed. This is headless process
evidence, not human listening, translated-copy/visual review, or a stable release claim.

## Linux-first Manual routing cardinality checkpoint

Linux source revision `be985e0bf906f8c5ddcb229f4e6cc6b26d9efe7b` constrains Manual routing profiles
to exactly the first displayed provider/model candidate. The GTK editor deactivates extra Manual
selections when loading or switching modes; Ordered and Automatic retain their selected candidate
chains. Local format/check/Clippy/test, Flatpak metadata, and diff validation passed. Push
Native/Flatpak/Foundation `29713205178`/`29713205186`/`29713205194` and PR
Native/Flatpak/Foundation `29713206482`/`29713206495`/`29713206461` all passed. Complete candidate-management
release evidence, physical visual review, other clients, signing, rollback, and stable release
remain open.

## Linux-first fallback-send confirmation checkpoint

Linux source revision `8dba6129f1706f9f450537477ef6d45ef6531d87` adds a localized modal confirmation
before an ordinary request with approved fallback enabled is dispatched. **Translate** grants one
request and **Close** sends nothing; the existing retryable-only and partial-output policy is
unchanged. Push Native/Flatpak/Foundation `29711055269`/`29711055278`/`29711055281` and PR
Native/Flatpak/Foundation `29711056550`/`29711056549`/`29711056544` all passed. Prompted Secret
Service/portal unlock UI, human listening, translated-copy/visual review, other clients, signing,
rollback, and stable release remain open.

## Linux-first fallback approval lifecycle checkpoint

Linux `62d70b1c57662515fadb447aa625cabe1b5d74e9` adds a dedicated serialized GTK regression for
the production fallback confirmation window. It verifies modal/focusable warning controls,
`Close` with no approval or dispatch, and one `Translate` action with one-shot approval and exactly
one dispatch. Push Native/Flatpak/Foundation `29770058909`/`29770058926`/`29770058895` and PR
Native/Flatpak/Foundation `29770062559`/`29770062414`/`29770062090` all passed. This remains
unreleased evidence; human copy/accessibility review, other clients, signing, rollback, and
stable release remain open.

## Linux-first routing candidate accessibility lifecycle checkpoint

Linux source/pin revision `1c47ff9b6b103ee16d564480d3dd3cdfcda5e083` adds the serialized GTK
`gtk_routing_profile_candidate_controls_have_accessible_lifecycle` regression. It exercises the
production routing dialog's labelled profile ID field, stable modes, explicit fallback control,
focusable candidate checkboxes, accessible up/down labels, row reordering, Manual cardinality, and
Use close-and-select lifecycle. Push Native/Flatpak/Foundation `29771475803`/`29771475775`/
`29771475669` and PR `29771479057`/`29771478869`/`29771478884` all passed. This remains
unreleased evidence; human visual/copy review, end-user Orca acceptance, other clients, signing,
rollback, and stable release remain open.

## Linux-first third-party Ollama interoperability checkpoint

Linux head `8645caf3c0504b225a4a44d97fd634af9ab67d0c` adds an opt-in daemon harness and an ignored
worker regression for native `/api/tags` discovery, model selection, and translation. Local
validation passed with 131 tests passed and 3 ignored locally; Native CI passed 133 tests with 12
ignored. Push Native/Flatpak/Foundation `29712165334`/`29712165338`/`29712165360` and PR
Native/Flatpak/Foundation `29712166849`/`29712166856`/`29712166851` all passed; the Native PR also
records the fallback, AT-SPI, and Orca fixtures. A Docker `ollama/ollama:0.11.10` daemon served
`/api/tags` and `/api/chat` for `qwen2.5-0.5b-instruct:latest`, and the harness reported
`1 passed; 0 failed` without a credential. The model and daemon were removed after validation;
GPU and stable-release evidence remain open.

## Linux-first editor text-metrics checkpoint

Linux `7ae70945c60934605d2eca82400a2278c753297f` displays localized source/output character counts
and an explicitly approximate token estimate without logging text content. l10n
`8adb1f4558e4b1d93a00ce03cf026a98d4a1a5ed` supplies the message in all twelve official packs.
Local l10n validation, Linux source-key audit (236 keys), formatting, GUI checks, strict Clippy,
tests, and Flatpak metadata validation passed. Push Native/Flatpak/Foundation runs
`29701632363`/`29701632341`/`29701632350` and PR Native/Flatpak/Foundation runs
`29701633693`/`29701633692`/`29701633700` passed. Provider-specific token accuracy, Orca speech, visual review, other
clients, artifacts, and stable release remain open.

## Linux-first routing-constraint checkpoint

Linux `f64054924102b5611eb0e17761c7acb8b3a771dd` exposes localized Automatic preference,
local-only/remote permission, privacy-sensitive, streaming-capability, document-capability,
provider/model allow-deny lists, minimum quality, and maximum request-size controls. Existing
profile edits restore these values while preserving other Core fields. l10n
`c366124539d4e8c909c66ca7cc33fb16ed92e8b2` supplies the 27 routing-constraint messages in all
twelve official packs. Local Linux validation passed; push Native/Flatpak/Foundation runs
`29703371083`/`29703371057`/`29703371084` and PR Native/Flatpak/Foundation runs
`29703373063`/`29703373065`/`29703373076` all passed.

## Linux-first visible-string localization and Flatpak pin checkpoint

Linux `212de54d7eaa62eaeba8f7bc06297b2632d7a09b` adds a dependency-free source audit that rejects
non-empty hard-coded GTK labels, titles, tooltips, placeholders, dialog actions, and direct list
options while allowing empty reset labels. Its Flatpak manifest pins the Linux source to a
source-compatible ancestor and validates that no build inputs changed; the workflow fetches full
history before this check. The existing key audit covers 263 Linux source keys; l10n
`3362732be198450ff1ca00f30ec092aab2cf4189` contains the 387-message generated bundle. Local Linux
validation passed, and push Native/Flatpak/Foundation runs `29704472892`/`29704472889`/`29704472884`
plus PR Native/Flatpak/Foundation runs `29704474147`/`29704474173`/`29704474207` all passed.
Complete translated-copy, plural, visual/RTL, and Orca review remain manual boundaries.

## Linux-first Flatpak integrity-evidence checkpoint

Linux `dc1c0bc3485c95a57810ac658dab2c0a232f1af7` adds CI-only SHA-256 and deterministic SPDX 2.3
SBOM sidecars for the generated Flatpak bundle. The evidence generator reads the bundle and locked
Cargo package set; it does not sign or publish a stable artifact. Push Native/Flatpak/Foundation
runs `29704836385`/`29704836408`/`29704836382` and PR Native/Flatpak/Foundation runs
`29704837824`/`29704837805`/`29704837827` passed, with non-expired evidence artifacts uploaded on
both push and PR runs. Stable release packaging remains open.

## Linux-first native release-mode evidence checkpoint

Linux `c6dae33698587e9db1fd8356ac7938d6bd7944ba` builds the native GTK binary in release mode and
uploads it with SHA-256, deterministic SPDX 2.3, and fixed build-context sidecars. Native and
Flatpak push/PR gates passed: `29705491999`/`29705491988`/`29705492011` and
`29705493161`/`29705493148`/`29705493163`. The artifacts are non-expired CI evidence, not signed
or distributable releases; source archive, rollback, cross-client artifacts, and stable promotion
remain open.

## Linux-first source archive evidence checkpoint

Linux `d5525263f2b5e339933a3b3c6dac7d21537ad990` adds a repository-only source archive to the
native evidence artifact and appends its SHA-256 to `SHA256SUMS`; the archive still requires the
pinned Core and localization repositories. Final push Native/Flatpak/Foundation runs
`29706120410`/`29706120412`/`29706120423` and PR Native/Flatpak/Foundation runs
`29706121615`/`29706121557`/`29706121564` passed. The first attempt `29705840151` failed only during
AT-SPI temporary-directory cleanup after its assertions passed; the bounded retry fix is covered by
the final gates. No standalone or stable source release is claimed.

## Linux-first performance-baseline checkpoint

Linux `4d6f041f388606dcc99311826ee4dbd3503edfd8` records a machine-contextual baseline for DOCX
reconstruction, XLSX reconstruction, and saved-profile routing dispatch (`0.404s`, `0.382s`, and
`0.399s` on the documented host). Push Native/Flatpak/Foundation runs
`29706935372`/`29706935324`/`29706935322` and PR Native/Flatpak/Foundation runs
`29706936415`/`29706936411`/`29706936399` passed, and the current Native artifact contains the
baseline TSV. The values are trend evidence only; no portable budget or stable-release claim is made.

## Linux-first localization-placeholder checkpoint

Linux `3a20620eb95806baadb1b22ef4833302d0438fea` adds a dependency-free source audit for malformed
braces and placeholder drift in literal catalog-backed fallback templates. Push
Native/Flatpak/Foundation `29707410914`/`29707410888`/`29707410893` and PR
Native/Flatpak/Foundation `29707412487`/`29707412476`/`29707412474` passed; Native and Flatpak
evidence artifacts were non-expired. This remains source-level prerelease evidence, not human
translated-copy or stable-release approval.

The documentation-only Linux head `3f5f9ee00dd6359759cec0b96dbc8b6d8b89c70d` passed push
Native/Flatpak/Foundation `29707758213`/`29707758214`/`29707758216` and PR
`29707759245`/`29707759269`/`29707759252`; final Native and Flatpak evidence artifacts were
non-expired.

The final Linux status head `81eed4f051e0f70406efbe47dca82e4f215c4cce` passed push
Native/Flatpak/Foundation `29708338140`/`29708338160`/`29708338159` and PR
`29708339322`/`29708339336`/`29708339368`; its Native and Flatpak artifacts were non-expired.

## Linux-first duplicate routing-profile ID checkpoint

Linux `21c89c7e9c671617477a6410240ff1fb0a0c9ff7` rejects a new profile whose validated ID already
exists, while explicit Edit continues to replace the selected record. l10n
`712c4b1ac814ffbab265e4d0d40629d9d2bba02d` supplies the duplicate-ID error in all twelve official
packs. Local Linux/l10n checks and all push/PR Native/Flatpak/Foundation gates passed; complete
fallback-chain editing, Orca speech, visual review, other clients, artifacts, and stable release
remain open.

## Linux-first routing profile identifier checkpoint

Linux `f00cf23f95d33d7c3c9abbc35ebe2141233a80b8` adds a localized routing-profile ID field with
Core-compatible 1–128 byte ASCII validation. New profiles can use distinct IDs; editing an existing
profile locks its ID so document-job and selection references remain stable. l10n
`7b832d765788e5ca64d7ba483b8ad12b3dd382d2` supplies the label and invalid-ID error in all twelve
official packs. Local Linux/l10n checks and push/PR Native/Flatpak/Foundation gates passed; full
fallback-chain editing, Orca speech, visual review, other clients, artifacts, and stable release
remain open.

## Linux-first routing candidate drag-order checkpoint

Linux `c0cdee8b729a6800904f6754f30221feb55f78e` extends the routing-profile dialog with GTK text
drag sources and row drop targets. Dropping a candidate before another row rebuilds the list and
persists the resulting Ordered-mode sequence; invalid, missing, and self-targeted IDs fail closed.
Keyboard up/down controls and catalog-backed accessible labels remain available.

Local Linux validation passed with 133 tests (`131 passed; 2 ignored`), GUI all-target check, strict
Clippy, formatting, localization sync/audit, Flatpak metadata, and diff checks. Push
Native/Flatpak/Foundation runs `29699210798`/`29699210802`/`29699210801` and PR
Native/Flatpak/Foundation runs `29699211832`/`29699211818`/`29699211830` all passed after a
cleanup-only AT-SPI rerun. Full profile editing, Orca speech, visual review, other clients,
artifacts, and stable release remain open.

## Linux-first routing profile edit/upsert checkpoint

Linux `a4dd4aa644335a3b6539db4d40473423c6292c71` adds an **Edit** action to saved routing-profile
rows. The editor restores the persisted mode, explicit fallback consent, candidate selection/order,
and stable profile ID; **Save routing profile** preserves hidden constraints and replaces the same ID
through the storage upsert path. The worker regression verifies one updated record without endpoints,
credentials, or source content.

Localization revision `aea172c15f421da09a0c848accae7c443820fb27` adds the edit/save actions to all
twelve official packs and produces a 356-message development bundle. Local Linux/l10n checks passed.
Push Native/Flatpak/Foundation runs `29699870066`/`29699870068`/`29699870071` and PR
Native/Flatpak/Foundation runs `29699871302`/`29699871301`/`29699871311` all passed. Full
fallback-chain editing, Orca speech, visual review, other clients, artifacts, and stable release
remain open.

## Linux-first routing candidate accessibility checkpoint

Linux `84bed28deaa6034fb45e4f6c925fd5c2713c8782` adds focusable candidate checkboxes and adjacent
up/down controls with catalog-backed accessible names to the GTK routing-profile dialog. Only
explicitly checked enabled saved provider/model pairs are serialized, in the user-selected Ordered
sequence; unknown IDs and out-of-range moves fail closed. The existing Core Manual/Ordered/Automatic
mode and explicit fallback-consent behavior remain unchanged.

Local Linux validation passed with 132 tests (`130 passed; 2 ignored`), GUI check, strict Clippy,
formatting, localization sync/audit, Flatpak metadata, and diff checks. Push Native/Flatpak/Foundation
runs `29698745522`/`29698745519`/`29698745529` and PR Native/Flatpak/Foundation runs
`29698747220`/`29698747211`/`29698747194` passed. Localization revision
`0d2d8c08f3dec5cd3044558b0b7c75f669a9535d` passed Localization/Foundation runs
`29698455887`/`29698455897`. Drag/drop ordering, other clients, visual/Orca review, artifacts, and
stable release remain open.

## Linux-first routing mode and fallback-consent checkpoint

Linux `88c04495d427fbca09ce2bc6c020dd057652dae9` maps a stable GTK dropdown to Core's `Manual`,
`Ordered`, and `Automatic` routing modes and persists the selected mode with the non-secret routing
profile. A separate fallback-consent checkbox is explicit and disabled by default; manual and
document dispatches remain non-fallback paths. Existing catalog-backed routing labels are reused.

Local Linux GUI check, 130 demo-provider tests (`128 passed; 2 ignored`), strict Clippy, formatting,
localization sync/audit, Flatpak metadata, and diff checks passed. Push Native/Flatpak/Foundation
runs `29696348120`/`29696348121`/`29696348094` and PR Native/Flatpak/Foundation runs
`29696349676`/`29696349689`/`29696349695` all passed; other clients, visual/Orca review, artifacts,
and stable release remain unverified.

## Linux-first routed document restart checkpoint

Core `9926d0f9bf6394c6011c6cc886d142bfeb54e10f` extends the document-job storage contract to
schema 16 with nullable `routing_profile_id`. The field contains only a validated non-secret
profile identifier; schema-15 snapshots without it remain readable and continue their persisted
provider/model resume path. Linux `202f565f65738345d23c3e19b428a99494ad7cfe` reconnects the saved
profile through the host secret broker for Resume and Retry after restart, emits a zero-fallback
routing decision, and keeps document fallback disabled.

Local Core storage/workspace validation and Linux formatting, GUI check, 129-test suite (127
passed, 2 ignored), strict Clippy, localization-key audit, Flatpak metadata validation, and diff
checks passed. Core CI/Native SDK `29694632345`/`29694632350` passed. Linux Native/Foundation
push and PR gates `29694926451`/`29694926454`/`29694927642`/`29694927681` passed. Final Linux
push Native/Flatpak/Foundation `29695388000`/`29695388015`/`29695387996` and PR
Native/Flatpak/Foundation `29695389589`/`29695389588`/`29695389602` also passed.

Linux-first CSV document checkpoint: Core `5feaa3700764e3f174a69a4b490ae67b2d5cd8c9` adds
bounded CSV delimiter/quote parsing, selected-column segmentation, safe provider decoding and
schema-9 persistence. Linux `f198aa539d51f21e2e29b8e366884013ea436360` accepts `.csv` in the native
chooser and routes decoded fields through the worker. Native `29646594392` (job `88085783161`),
Foundation `29646594377`, and Flatpak `29646594396` (job `88085783170`) passed; this remains
unreleased.

Linux-first JSON document checkpoint: Core `ae8e437ff51fb045a6961604db6a19ebe488e0ba` adds
bounded JSON syntax validation, raw-structure preservation, default string-value segmentation,
RFC 6901 include/exclude paths, primitive/key protection, and JSON string escaping on reconstruction.
Linux `3f6d7e577afacb3aa3b7ad8c9825a243c9a0f13f` accepts `.json` in the native chooser and routes
decoded string values through the worker. Native `29647794016` (job `88088841342`), Foundation
`29647793982`, and Flatpak `29647794021` (job `88088841323`) are the current Linux gate evidence;
this remains unreleased.

Linux-first HTML document checkpoint: Core `912780f21d8dbb19571c9b991879778a053272f8` adds
bounded structural tag-stack validation, void-tag handling, raw script/style protection, visible
text-node segmentation, original tag/attribute/link preservation, and safe HTML text escaping on
reconstruction. Linux `2a04c096594f5358638fc9e5b1610c78c1051a13` accepts `.html`/`.htm` in the native
chooser and routes visible text nodes through the worker. Native `29648437605` (job `88090534144`),
Foundation `29648437590`, and Flatpak `29648437562` (job `88090534114`) are the current Linux gate
evidence; this remains unreleased.

Linux-first persisted document queue checkpoint: Linux `ba7d4a3ad9d1cc152d5c52e5acf84633ae46ef92`
adds the non-blocking queue-list command, localized “Document jobs” action, empty/list dialog,
progress/state metadata, and selection back into the existing resume/retry/pause/cancel/export
controls. Packaging revision `71e8b24dd6f233c4667c705066524489b065e49a` pins the Flatpak source.
Native `29649067477` (job `88092162300`), Foundation `29649067457`, and Flatpak `29649067473`
(job `88092162266`) passed; archive codecs and the remaining platform clients remain open.

Linux-first DOCX package checkpoint: Core `08eb64cb87d9cf6df624225819818d8287063c4c` adds
bounded ZIP/XML inspection, schema-10 package persistence, safe OOXML text-node reconstruction, and
resource retention. Linux packaging revision `3725ef97584b30ee34e7807e35cddc16df6ad8ae` pins the
DOCX-capable Linux source and current vendored dependency set. Native `29650642852` (job
`88096278936`), Foundation `29650642855`, and Flatpak `29650642850` (job `88096278936`) passed.
Packages over 4 MiB or 512 entries, encrypted/traversal/duplicate/malformed/DTD-bearing packages,
and incomplete exports are rejected; PPTX/XLSX, EPUB, PDF/OCR, remaining archive codecs, and other
platform clients remain open.

Linux-first subtitle readability checkpoint: Core `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` adds
cue-level `DocumentWarning` values for configurable subtitle line-length and reading-speed guidance
while preserving timing and source content. Linux `60b560383e53bf4cf9ccc5ecf3821fe735206446`
persists the warnings and renders cue-number-only guidance without exposing subtitle source text.
Localization `738a7c7328f24acc12c15be78bb11737220bbbae` supplies the PDF and subtitle warning
messages. Core CI `29655212117`, Native SDK `29655212149`, Linux Native `29656158543`, Foundation
`29656158527`, and Flatpak `29656158526` passed; defaults are 42 Unicode characters per line and
17 non-whitespace characters per second, with custom limits available through Core. OCR, remaining
archive codecs, complete acceptance scenarios, and non-Linux clients remain open.

Linux-first document queue localization checkpoint: l10n `0ef4fb9b6878655e46e2b8ca5bbed9562f97b0f0`
adds ten catalog-backed Linux-only action, dialog, status, progress, and tooltip messages, raising
the bundle to 277 messages with checksum
`e26da1a391369ed84c0f57f5fd5d440f50ed56dcbc8f069abd4d6d27db7dd9c1`. Linux `191345c55dc8989d518680c864a4c4a643165f6c`
syncs all twelve PO/MO packs and asserts the queue keys alongside PDF/subtitle warnings. l10n
Localization `29656496378` and Foundation `29656496361`, Linux Native `29656549651`, Foundation
`29656549644`, and Flatpak `29656549677` passed; non-English packs remain unreviewed drafts and
complete visible-string coverage, cross-platform clients, OCR, and stable-release evidence remain open.
Linux test head `1e60e3725b0548a82bb88402c5257eb0f5f0bb0c` additionally asserts keyboard focusability
for the queue actions; Native `29657086074`, Foundation `29657086060`, and Flatpak `29657086067` passed.

Linux-first exported-output checkpoint: l10n `4be0401a09ce26e65c8fd3c921e333d6011e8706`
adds localized open-output and open-failure messages, raising the bundle to 280 messages with
checksum `61fe261fb62e996b637745913bb89e5a5e0c0a16a82c5d2fe536a254cf61b6ee`. Linux
`45d9365eaba0b25d58c65a09e4a5dcfa2bae0840` records the last successfully exported GIO URI only
after the asynchronous write completes, exposes a focusable Open exported output action, launches
it through the default GIO handler, clears stale destinations on new imports/translations, and
reports a fixed localized error without exposing paths. l10n Localization `29657734947` and
Foundation `29657734951`, Linux Native `29657811742`, Foundation `29657811734`, and Flatpak
`29657811738` passed; routing fallback, OCR, screen-reader narration, physical keyboard traversal,
other platform clients, complete acceptance scenarios, and stable-release evidence remain open.

Linux-first approved text fallback checkpoint: l10n `273be8a4e9c3b1084f393ce0086cdf2c42fcd4e9`
adds six Linux-only messages, producing 286 canonical messages with deterministic bundle checksum
`ee7c269571beca22cdbd7bea971ae266975b8004490b02ead4b71305e3a93872`. Linux
`878a9c015d29ce49633046d435f48f5fee4c9a47` adds an explicit different saved-provider selector and
single retry for network/timeout failures on ordinary text only; partial output is retained and the
selection is localized without exposing endpoints or content. Document jobs, cancellation,
authentication/model failures, unapproved profiles, and session-only profiles never fall back. Local
Linux suites passed (61/100 tests, one existing environment-dependent ignore), strict Clippy, GUI
check, l10n sync, and diff checks; Native `29659054771`, Foundation `29659054755`, and Flatpak
`29659054756` passed for the current head.

Linux-first keyboard traversal checkpoint: Linux `8f2cba0` adds an application-window Capture-phase
provider-form Tab/Shift+Tab order while preserving modified Ctrl/Alt/Super shortcuts, and the
Xvfb/xfwm4 fixture verifies provider fields plus onboarding/workspace controls from a real GTK
focus path. Default-branch Native `29663597817` (job `88130256368`), Foundation `29663597809` (job
`88130256318`), and Flatpak `29663597831` (job `88130256370`) passed; screen-reader narration, physical desktop
review, OCR, other platform clients, and stable-release evidence remain open.

Linux-first AT-SPI semantic export checkpoint: Linux `7480579e4ae305758397082b7456715939666a9e`
adds an isolated Xvfb/xfwm4 fixture that starts the AT-SPI bus and reads the running GTK tree with
`python3-pyatspi`, verifying the named `Stop translation` push button and two text-editor roles;
the existing GTK helper continues to verify label relations, editor properties, and state changes.
Default-branch Native `29664478686` (job `88132499067`), Foundation `29664478672`, and Flatpak
`29664478670` passed. Orca speech, provider-form default Tab-chain review, physical desktop
accessibility, OCR, other platform clients, and stable-release evidence remain open.

Linux-first dialog field localization checkpoint: Linux `1b68cef85d89324baba20689ce246486ab28c49b`
uses the catalog-backed `field.source_text` and `field.translation` labels for source and translated
content prefixes in the history and translation-memory dialogs. Native `29664934283` (job
`88133657483`), Foundation `29664934298`, and Flatpak `29664934279` passed; dynamic `Job` and
`Identity` metadata, complete visible-string gettext coverage, and the remaining Linux/release
boundaries remain open.

Linux-first dialog metadata localization checkpoint: Linux `c19192fbd78b30aa55a5bac94c133c7400c78642`
routes the document-job identifier and translation-memory identity prefixes through the active
catalog, reusing the existing Linux dialog keys without changing stored content or locale packs.
Native `29665343100` (job `88134735908`), Foundation `29665343120`, and Flatpak `29665343145`
passed. Complete visible-string gettext coverage, Orca speech, physical desktop review, OCR,
other platform clients, and stable-release evidence remain open.

Linux-first multi-job queue controls checkpoint: Linux `014a79a19cb72b4eceba3d7c0c592b7655e1cdd0`
adds catalog-backed pause, resume, and retry actions to each persisted document-job row while
reusing the existing worker commands and storage state machine. Native `29665725241`, Foundation
`29665725238`, and Flatpak `29665725434` passed; OCR, Orca speech, physical desktop review,
complete visible-string gettext coverage, other platform clients, and stable-release evidence
remain open.

Linux-first glossary validation localization checkpoint: l10n `ede66149c501a1680ed050d76b8b78e7b565ba01`
adds three Linux-only catalog keys for glossary syntax, invalid/credential-like data, and
conflicting rules, producing 289 canonical messages and bundle checksum
`c8bd6b0464ebbfa015988a4fc0cfd30b1f9e28d9e1aad19b8c50d36976128e8f`. Linux `cb22b2052362ce7b4990cc4be99e26a152b07800` synchronizes the PO/MO snapshot and maps these errors through
the runtime catalog. Native `29666379600`, Foundation `29666379579`, and Flatpak `29666379586`
passed; complete visible-string gettext coverage, Orca speech, physical desktop review, OCR,
other platform clients, and stable-release evidence remain open.

Linux-first provider-form Tab-chain evidence checkpoint: Linux `713c86b3da9b057cc25e72c687dc6c4c265f6439`
records the application-window Capture-phase Tab/Shift+Tab order for saved-profile, provider,
credential, Connect, and Remember controls while preserving modified shortcuts. Native
`29666820550`, Foundation `29666820602`, and Flatpak `29666820579` passed the current head,
including the Xvfb/xfwm4 keyboard fixture. Orca speech, physical desktop review, OCR, complete
visible-string gettext coverage, other platform clients, and stable-release evidence remain open.

Linux-first document-job metadata localization checkpoint: l10n `c81728faf8679e7a5e9854537ad7c70c046c7800`
adds seven Linux-only catalog messages for the document-job row template and pending/running/
paused/completed/cancelled/failed states, producing 296 canonical messages and bundle checksum
`d2f4fd439b5fbc8fc6d48f1be0a91ee92f558c70b851271d643829cfe8590e9b`. Linux
`76b5f632fee62dc8e323e0cfec5d420e6fcc6992` maps document format and lifecycle metadata through
the active catalog instead of Rust debug output. Native `29667553178`, Foundation `29667553139`,
and Flatpak `29667553149` passed, including the GTK AT-SPI/Wayland and Flatpak smoke gates. Orca
speech, physical desktop review, OCR, complete visible-string gettext coverage, other platform
clients, and stable-release evidence remain open.

Linux-first PPTX package checkpoint: Core `0f71a652a536753f48bb8c852fd38e97740c23ce` adds bounded
PPTX ZIP/XML inspection, schema-11 package persistence, safe slide/notes/master/layout/handout/
comments text-node reconstruction, and resource retention. Linux functional revision
`ce08d1232889522bead58e6056d296f0fc8d56e1` adds native chooser/import, worker reconstruction, and
binary export; packaging revision `766b78e4b236f15ee7a6f1d6e61ebd828415da82` pins the final source.
Native `29651317600`, Foundation `29651317621`, and Flatpak `29651317679` passed. Packages over 4 MiB or 512 entries, encrypted/traversal/duplicate/
malformed/DTD-bearing packages, and incomplete exports are rejected; XLSX, EPUB, PDF/OCR, remaining
archive codecs, and other platform clients remain open.

Linux-first XLSX package checkpoint: Core `36f256637236636889b0933cc5fe6a70bffff02c` adds bounded
XLSX ZIP/XML inspection, schema-12 package persistence, safe shared-string/worksheet text-node
reconstruction, and resource retention. Linux functional revision `731072eb3d9b29a43fe0e238084290cd5c253e59`
adds native chooser/import, worker reconstruction, and binary export. Native `29651990077`,
Foundation `29651990067`, and Flatpak `29651990064` passed. Packages over 4 MiB or 512 entries,
encrypted/traversal/duplicate/malformed/DTD-bearing packages, and incomplete exports are rejected;
EPUB, PDF/OCR, remaining archive codecs, and other platform clients remain open.

Linux-first EPUB package checkpoint: Core `554c09521b57de45be154a99edfbf24aa2fc6538` adds bounded
EPUB ZIP/XML inspection, schema-13 package persistence, safe XHTML/HTML text reconstruction,
OPF `dc:language` updates from the persisted target locale, and package resource retention. Linux
functional revision `3f0f659ccba195e58789d80d9fdc20b087a10b68` adds native chooser/import, worker
reconstruction, binary export, MIME filtering, Flatpak pinning, and documentation. Local Core
document/storage tests (22/28) and Linux checks/Clippy/library tests (61) passed; Core CI `29652884450`,
Native SDK `29652884430`, Linux Native `29652937783`, Foundation `29652937750`, and Flatpak
`29652937761` passed. Packages over 4 MiB or 512 entries, wrong first `mimetype`,
encrypted/traversal/duplicate/malformed/DTD-bearing packages, and incomplete exports are rejected;
PDF/OCR, remaining archive codecs, and other platform clients remain open.

Linux-first subtitle document checkpoint: Core `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` adds
bounded SRT/WebVTT detection, cue/timestamp structural validation, and inter-cue WebVTT metadata
handling on top of schema-8 document options. Linux `33b47852f3bd3a0a4a8997cd6592c756a0b254a3`
accepts `.srt`/`.vtt` in the native chooser, maps malformed structures to a safe import error, and
keeps cue IDs/timestamps unchanged while translating cue text. Native `29645547013` (job
`88083068099`), Foundation `29645547036` (job `88083068179`), and Flatpak `29645547024` (job
`88083068088`) passed; Core CI `29645385353` and
Native SDK `29645385324` passed. This remains unreleased.
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; `protected_spans_v1`, `long_text_chunking_v1`, and `bounded_text_document_v1` negotiation with common URL/email/Markdown-code/placeholder and bounded request-level glossary restoration plus fail-closed marker validation; semantic chunking keeps oversized requests ordered and cancellation-aware; Core TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB inspection preserves BOM, line endings, Markdown fences, cue IDs, headers, timestamps, CSV delimiters, quoting, variable-width rows, selected-column boundaries, JSON structure, keys, primitive values, string escaping, exact include/exclude path selection, HTML tags, attributes, links, scripts, styles, text-node structure, supported OOXML text nodes, EPUB metadata/navigation/spine/CSS/resources, and text-PDF page association/coordinates with structured HTML fallback; schema-14 document jobs persist bounded segment progress, validated non-secret source/target/provider/model/glossary options, PDF warning metadata, and package bytes, restoring pending/running/paused jobs after worker restart without filesystem paths or credentials; native imports create persisted jobs before editor population, and the GTK queue lists snapshots with localized action/dialog/status/progress/tooltip controls and selection back into resume/retry/pause/cancel/export; TranslateDocumentJob sequentially translates pending prose segments while committing each completed segment; binary package/PDF export retains resources or falls back to page-aware HTML when required; bounded fixed-schema glossary CSV import/export through GTK FileDialog; explicit Incognito request policy routed into Core and rejected for new durable document jobs; bounded local history and translation-memory controls; multi-profile/model persistence; derived onboarding with catalog-backed stage/detail guidance; session credentials; GIO Secret Service adapter and no-credential OpenAI-compatible loopback provider; twelve official Linux PO/MO packs with catalog-backed runtime controls, PDF/subtitle warnings, document queue controls, Arabic RTL root direction, and explicit opt-in bounded image-only PDF OCR to page-marked TXT; generic completion notification; private notification-service, dunst, document-portal, FileDialog, drag/drop, GTK accessibility, headless Xvfb/xfwm4 keyboard traversal, and Flatpak smoke verification; Native source-referenced localization keys are statically checked against the canonical catalog | Published audit head `a26ee1855e6d46ac1c174f1388bae5eb09420588` passed Native `29669448961` (job `88145739138`), Foundation `29669448991`, and Flatpak `29669448995` (job `88145739200`); pull-request reruns `29669459291`, `29669459309`, and `29669459312` also passed; l10n `3f3c1a1154b66d25f2936a02b8a08d2a8fc8a878` passed Localization `29669015989` and Foundation `29669016025`; end-user prompt approval, translated-copy/plural/visual review, physical compositor/GPU rendering, signing, distributable release, and stable release remain open, unreleased |

The Linux row above is superseded by the current EPUB checkpoint: Core `554c09521b57de45be154a99edfbf24aa2fc6538`, Linux `3f0f659ccba195e58789d80d9fdc20b087a10b68`, schema 13, and passed Core CI `29652884450`, Native SDK `29652884430`, Linux Native `29652937783`, Foundation `29652937750`, and Flatpak `29652937761`. EPUB package metadata, navigation, CSS, resources, visible XHTML/HTML text, and OPF language updates are included; PDF/OCR and other platform clients remain open.

Linux-first accessible progress, diagnostics-label, and pause-error localization checkpoint: Linux `1d96c9825b83cdc1cd6a2783b61fdd678b89e510` adds
the native GTK document-progress role, localized completed/total text, bounded fraction, and
hidden reset behavior, catalog-backed diagnostics summary, and localized fixed diagnostics labels
and state values, and routes document-pause queue errors through the catalog-backed reducer path.
Push Native `29672046465`, Foundation `29672046491`, and Flatpak `29672046488` passed; PR reruns
`29672047299`, `29672047295`, and `29672047296` also passed. Orca speech, manual
visual review, prompt approval, signing, distributable artifacts, and stable release remain open.

Linux-first text-PDF checkpoint: Core `4f03618ffb1f37f27fb1edcf2de5a80e3bec540d` adds bounded PDF
object/page inspection, page-aware text segments, basic coordinates and reading-order boundaries,
Flate stream support, safe ASCII literal/hex rewriting, schema-14 persistence, and a structured
HTML alternative when target text cannot be safely encoded, plus structured warnings for image-only
pages, uncertain reading order, and limited reconstruction. Linux `edbfad1a8e443d86f39c782f4ad991a029cb8e76`
adds PDF chooser/MIME filtering, worker export fallback to `.html`, localized UI warning plumbing,
and updated documentation. Core CI `29654538722`, Native SDK `29654538670`, Linux Native
`29654651108`, Foundation `29654651074`, and Flatpak `29654651067` are the current gates; OCR,
pixel-identical reconstruction, image-only page translation, remaining archive codecs, and other
platform clients remain open.

The Linux client uses a GIO D-Bus Secret Service adapter for persistent SecretRef values and fails
closed when the service is unavailable, locked, or requests interaction. It can create, update,
switch, and delete multiple provider profiles,
preserve independent confirmed model preferences, restore the full list/default without connecting,
require explicit Connect for activation, and keep a deleted connected row's validated runtime as
session-only. Its derived setup card identifies the stable provider/model for the next request,
retains storage-degradation warnings, and disables commands after worker loss. Authenticated A/B
request counters verify Linux-side remembered model routing and failed-switch isolation. Credential
re-entry remains required for session-only connections; only persistent SecretRef identifiers are
stored, never credential values or session references, and nothing falls back to plaintext. A real Linux `ENOSPC` gate verifies that failed persistent Connect, model-update,
and deletion transactions reject before success, preserve the prior session, and restore only
pre-fault state. The GTK flow also exposes baseline roles, named multi-line editors, visible-label
mnemonics, focusable controls, hidden empty errors, and translation Busy/reset semantics on GTK
4.10+. Runtime switching exposes all twelve official Linux PO packs, switches catalog-backed
Translate and Stop labels, refreshes catalog-backed workspace widgets and status summaries/partial-output markers, and applies Arabic RTL root direction, with explicit English fallback for
uncovered UI keys. Completed translations send a generic desktop notification
without source or translated content; private notification-service transport, headless delivery to a
real `dunst` daemon, and a visible viewable Dunst desktop-shell window are verified, while physical
compositor/GPU rendering and packaging remain runtime boundaries. Native Open text file import accepts bounded UTF-8 TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT content, and a single
GIO file can be dropped onto the source editor through the same validation path; the real document-
portal lease lifecycle and a direct interactive `xdg-desktop-portal-gtk` FileChooser backend are
verified, and application-level GTK FileDialog and source-editor drag/drop fixtures pass under
Xvfb. It does not cover every database or storage failure. Real
end-user prompt approval and complete UI gettext coverage remain open; global Scenarios 3 and 5
still require cross-platform evidence. Stable clients must pin
a released core and reject an unknown ABI major. Every release-train update must include source
revisions, artifact checksums, minimum compatible versions, known limitations, and cross-repository
conformance evidence. Development placeholders and the alpha.2 source checkpoints are not
consumable releases.

Linux-first optional image-only PDF OCR checkpoint: l10n `3f3c1a1154b66d25f2936a02b8a08d2a8fc8a878`
adds ten Linux-only toggle, progress, and fixed-error messages, producing 306 canonical messages
and deterministic bundle checksum `6fc6839fce3a449eaf37d2efb9a52fa0ede1eab3a39fecdaff68682a79d8a4f8`.
Linux `d18e8dfa3dd98d56dbe0d5d1eabc536d38b96f1c` invokes bounded, shell-free `pdftoppm`/`tesseract`
only after explicit user opt-in for image-only PDF pages, stores page-marked text as a TXT job, and
keeps the source PDF untouched. Native `29668688201` (job `88143670012`), Foundation `29668688202`,
and Flatpak `29668688223` (job `88143670073`) passed; the Native fixture exercised the external OCR
tools. OCR is not enabled by packaging defaults, and Orca speech, physical desktop review, complete
visible-string gettext coverage, other clients, and stable-release evidence remain open.

Linux-first Secret Service prompted-flow checkpoint: Linux `739538cb27bdcdc4b4f8530da6dcd5110550a310`
calls the Secret Service prompt object for persistent store/delete operations, accepts only
an approved `Completed` result, maps dismissal through `error.storage.prompt_dismissed`, and
fails closed on prompt-call or timeout failures. l10n `f00b00fda307660000b0e4068c5ca1072d266df1`
contains 327 canonical messages and bundle checksum
`53821e2397e6697b7551693c6f5787cc1f88e24d96b3077ac590645a848f1977`. Push Native
`29672741665`, Foundation `29672741666`, and Flatpak `29672741675` passed; PR reruns Native
`29672743058`, Foundation `29672742959`, and Flatpak `29672742990` also passed. End-user
prompt approval UX, complete gettext/plural/visual/Orca review, broader storage faults, other
platform clients, signing, distributable artifacts, and stable release remain open.

Linux-first Ollama-compatible local endpoint checkpoint: Core `0d0d475d22129e8211333ee8f664a7669948ce3a`
adds a deterministic fixture for the OpenAI-compatible `/v1/models` and `/v1/chat/completions`
surface, returning `llama3.2:latest` and streamed `你好，Ollama！` without credentials. Linux
`c1e701b4b0ad35eb6cd2823d19ae83cdb235b30d` exercises explicit model selection and streaming through
the `local-loopback` preset. Push Native `29673888541`/job `88157552503`, Flatpak
`29673888548`/job `88157552511`, and PR Native `29673889609`/job `88157555098`, Flatpak
`29673889576`/job `88157554910` passed. Native Ollama `/api` behavior and a running third-party
daemon remain unverified; Android, Windows, and macOS stay deferred.

Linux-first native Ollama `/api` checkpoint: Core `123d5c4d7a76873e597895763ca5d78e1ea42ea0` adds
the loopback-only `ollama` catalog preset and a native adapter for `/api/tags` model discovery and
`/api/chat` NDJSON streaming, including fragmented UTF-8, cancellation, bounded responses, and
protected-span restoration. Linux `a45ad953738766dc9fba5d9a6bd9e3b3280c62fa` exercises an explicit
`ollama_chat` profile through the worker and streams `你好，Ollama！` without a secret. Core CI
`29674653973` and Native SDK `29674653960` passed. Linux push Native `29674767565` (job
`88160007604`), Foundation `29674767554` (job `88160007526`), and Flatpak `29674767552` (job
`88160007533`) passed; PR reruns Native `29674768361` (job `88160009796`), Foundation
`29674768357` (job `88160010009`), and Flatpak `29674768359` (job `88160009822`) also passed. A running third-party daemon, GPU acceleration, and GTK
preset selection remain unverified; Android, Windows, and macOS stay deferred.

Linux-first native Ollama GTK preset checkpoint: Linux `75d5ded3d6ab25e9a35c8614899b8ccc3cf94535`
adds localized OpenAI-compatible and native Ollama selections to the provider form, restores the
preset for saved profiles, preserves user-edited endpoints when switching, and exercises the
`ollama_chat` profile through a GTK fixture-backed `/api/` connection. Local worker, source-level
GUI checks, localization sync, and documentation validation passed. Push Native `29675743173`
(job `88162744428`), Foundation `29675743166` (job `88162744434`), and Flatpak `29675743159`
(job `88162744336`) passed; PR Native `29675744738` (job `88162748418`), Foundation `29675744785`
(job `88162748481`), and Flatpak `29675744821` (job `88162748719`) also passed. A running
third-party daemon, GPU acceleration, Orca/visual review, stable release, and other clients remain
unverified.

## ABI 1 compatibility snapshot checkpoint

Core revision `c559b32d3869e01983f2bbf32f1386bad99c3290` adds the versioned
`CompatibilitySnapshot` payload and `lm_engine_get_compatibility` query. The FFI regression decodes
Core semantic version, ABI major, protocol version, provider-catalog version, and enabled features,
then releases the engine-owned buffer. Core CI/Native SDK `29782822854`/`29782822883` passed.
Linux documentation/source-pin head `b38a8fd722d4740abd161e30197354793e3de1f6` pins the exact Core
revision; PR Native/Flatpak/Foundation `29783023917`/`29783023872`/`29783023894` passed with jobs
`88488352790`/`88488352708`/`88488352736`. File-lease projection, other clients, and stable
release remain unverified.

## ABI 1 host-secret response checkpoint

Core revision `adc1e26f37db3761406bb30aa7515003a8bd2717` projects the typed Rust secret broker
through the versioned ABI protocol: commands may carry only a `secret_ref`, Core emits one
`secret_required` event, and a matching `host_secret_response` provides or safely rejects the
credential exactly once. Operation/correlation/request identity, size limits, replay, late
responses, and authenticated loopback streaming are covered by the FFI regression. Core CI/
Native SDK `29781845494`/`29781845502` passed. Linux documentation/source-pin head
`016c4d79131b08ad5eb66e0b7561b9e3e50f02b0` consumes the same revision; Linux
Foundation/Native/Flatpak `29781942858`/`29781942757`/`29781942821` passed with jobs
`88484970323`/`88484969938`/`88484969961`. Semantic/catalog/feature negotiation, file leases,
other clients, and stable release remain unverified.

Linux-first gettext plural runtime checkpoint: Linux `29e613a806b1eb096cabab2374c494ea6a07e807`
retains every generated MO plural slot and selects locale-specific English/French/Russian/Arabic/
Hindi/Brazilian-Portuguese or one-form Chinese/Japanese/Korean variants with safe fallback. Local
formatting, GUI checks, strict Clippy, 106-test demo-provider suite, 213-key audit, l10n sync, and
diff checks passed. Push Native `29676132263` (job `88163825783`), Foundation `29676132239`, and
Flatpak `29676132247` (job `88163825792`) passed; PR Native `29676133164`, Foundation `29676133154`,
and Flatpak `29676133165` (job `88163828359`) also passed. Translated-copy/visual review, Orca,
prompt approval, other clients, signing, distributable artifacts, and stable release remain open.

Linux-first offline-provider preservation checkpoint: Linux `b09f47415e33c84981f0d6da6fbfc6a0e00c4a53`
adds a worker regression that rejects a released loopback endpoint as a typed `Network` failure in
under five seconds and then completes through the previously confirmed provider/model. Local
formatting, GUI checks, strict Clippy, 107-test demo-provider suite, 213-key audit, l10n sync, and
diff checks passed. Push Native `29676519123` (job `88164823336`), Foundation `29676519162`, and
Flatpak `29676519121` (job `88164823343`) passed; PR Native `29676520477`, Foundation `29676520497`,
and Flatpak `29676520498` (job `88164827465`) also passed. This strengthens Linux Scenario 17
evidence but does not claim a physical network outage, third-party daemon, or stable release.

Linux-first plural UI and provider-preservation checkpoint: Linux `8d84636636c969e70943b534deba3818381daed6`
wires a localized plural file count into the GTK document-jobs dialog and resolves the model
discovery placeholder through the canonical catalog. It also retains the typed offline `Network`
failure regression and previous-provider continuation from `b09f474`, with a five-second bound.
Local formatting, GUI checks, strict Clippy, 107 passing tests (2 ignored), the 213-key audit,
l10n synchronization, and diff checks passed. Push Native `29676780532`, Foundation `29676780527`,
and Flatpak `29676780531` passed; PR Native `29676781353`, Foundation `29676781358`, and Flatpak
`29676781369` also passed. Translated-copy, visual/RTL, Orca, physical offline, other clients,
signing, distributable artifacts, and stable-release evidence remain open.

Linux-first corrupt-database fail-closed checkpoint: Linux `10cc4e7414efa3f55058c5748e887c5a96481641`
rejects a malformed SQLite database as typed persistence failure, preserves the malformed bytes,
keeps session-only translation available, and rejects saved-profile deletion while storage is
unavailable. Local formatting, GUI checks, strict Clippy, 108 passing tests (2 ignored), the
213-key audit, l10n synchronization, and diff checks passed. Push Native `29677532670`, Foundation
`29677532645`, and Flatpak `29677532656` passed; PR Native `29677534287`, Foundation `29677534288`,
and Flatpak `29677534304` also passed. Physical corruption recovery, desktop/Orca review, other
clients, artifacts, and stable-release evidence remain open.

Linux-first output-safety alias checkpoint: Linux `c7b7599b118fa54baefe32e2063f57a890dc0f52`
rejects export destinations that identify the imported source through equal GIO identity,
canonical paths, or Unix device/inode metadata, covering text and binary document output before
asynchronous replacement. Local formatting, GUI checks, strict Clippy, 107 passing tests (2
ignored), the 213-key audit, l10n synchronization, and diff checks passed. Push Native
`29677149812`, Foundation `29677149807`, and Flatpak `29677149811` passed; PR Native
`29677151266`, Foundation `29677151263`, and Flatpak `29677151268` also passed. Physical desktop,
Orca, other-client, artifact, and stable-release evidence remain open.
