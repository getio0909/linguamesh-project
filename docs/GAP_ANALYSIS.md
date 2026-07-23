# LinguaMesh Completion Gap Analysis

Status: Linux-first prerelease audit, 2026-07-23. This document complements
`PROJECT_GOAL.md`; it does not lower any acceptance requirement.

Assumption: Linux is the active implementation scope for the current checkpoint, while
Android, Windows, and macOS evidence must still be completed before a stable release.

The latest Linux-first mTLS client-authentication checkpoint adds runtime/test
`7513d983011fdd81374cfb879b23647aef388f7e`, source-pin `deffb80df01cb9f6c76a8b46e0ad725080e07ea6`,
and final status head `597ccc961f9530836f8cef4c9a12a64b5c0a311c`. A temporary endpoint with a
different client-CA trust chain rejects the session-only identity at the TLS handshake, while
the trusted endpoint succeeds; the unrelated server CA and wrong-SAN cases remain covered, with
no secret-name leakage. All four exact local runners pass once, and final status-head push/PR
Native, Flatpak, and Foundation runs `30052187039`/`30052187036`/`30052187043` and
`30052189474`/`30052189521`/`30052189488` all pass. Enterprise-provider interoperability, human
review, cross-client parity, signing, rollback, and stable authorization remain open.

The latest Linux-first mTLS hostname checkpoint adds runtime/test `ec6c9971e0271e5eddc89bdc64121761a9cb46df`,
source-pin commit `9fc633feeca328b356b8f98eead03e29d28d0d46`, and final status head
`1629547c0eca1a5aabcd06cb7a96ecdfeaf97e80`. The fixture proves that a session-only client
certificate reaches a trusted endpoint, that an unrelated-CA endpoint is rejected, and that a
wrong-SAN endpoint is rejected even when its signing CA is trusted; no secret name is exposed.
Local runners pass once for all three cases, and final status-head push/PR Native, Flatpak, and
Foundation runs `30050789607`/`30050789609`/`30050789567` and `30050792424`/`30050792455`/
`30050792453` all pass. Enterprise-provider interoperability, human review, cross-client parity,
signing, rollback, and stable authorization remain open.

The latest Linux-first mTLS checkpoint adds runtime/test `896cd2352aef73a86ca80d7d92e2b5c7850af7d7`,
source-pin commit `cb6a3b166344c240c135a829ef32d14e6b5214e6`, and final status head
`6113f4898a3d81fedd103b413d739797238c8490`. The fixture proves that the session-only client
certificate reaches a trusted endpoint and that the configured trust bundle rejects an endpoint
signed by an unrelated CA, without exposing the secret name. Local positive and negative runners
each pass once, and final status-head push/PR Native, Flatpak, and Foundation runs
`30049361416`/`30049361411`/`30049361698` and `30049363915`/`30049363922`/`30049363912` all pass.
Enterprise-provider interoperability, human review, cross-client parity, signing, rollback, and
stable authorization remain open.

The latest Linux-first client-certificate HTTPS checkpoint adds runtime/test
`4b5a3f2ec0e65060d104068be6a6f31446007ee4`, packaging/docs `7b69933e1b0b92e1ee2136e01b6d39fa765ec761`,
certificate hardening `e9406d56e1345be765c01ecfe2600e8e0d10dde9`, and final status head
`14b601ae1ac11e98e09a4d2727f6ebb584f32ad4`. A temporary Python HTTPS endpoint requires a client
certificate and serves `/v1/models`; the Linux worker supplies the session-only identity and bounded
trust bundle. The exact local fixture runner passes, and push Native/Flatpak/Foundation
`30047564119`/`30047564124`/`30047564131` plus PR `30047567575`/`30047567392`/`30047567456` all pass.
This is bounded rustls and server-side client-authentication evidence: enterprise-provider
interoperability, human review, cross-client parity, signing, rollback, and stable authorization
remain open.

The latest Linux-first proxy-secret checkpoint adds runtime test
`911994eb3f4c364af3ea043b783f2aff18e09888`, packaging/docs `968b5c88cdda64ae69a2c80add729bb37ca7548b`,
and final status head `f78d0939dd78c1646da4f7e3fa7f87665a534bf5`. A worker-level loopback proxy
fixture verifies the absolute provider request, exact Basic authorization value, and successful
model response while the profile contains only a session SecretRef. Local checks pass; push
Native/Flatpak/Foundation `30045229527`/`30045229529`/`30045229541` and PR
`30045232877`/`30045232887`/`30045232885` all pass. Live proxy deployment, provider accounts,
interactive prompts, human review, cross-client parity, signing, rollback, and stable authorization
remain open.

The latest Linux-first secret-boundary checkpoint adds runtime tests
`f0a65c0d7bd1ddfda6e531db1b93c6be0096d491`, packaging/docs `dcd3f49620b427d460c98082acaf97498f2b98ff`,
and final status head `4cfa3fa8cfa29f5dc036e53bafa388444b8de94e`. Session-only proxy-authentication
and client-certificate identity canaries reach Core validation and are absent from surfaced
diagnostics. Local checks pass; push Native/Flatpak/Foundation `30043522421`/`30043522574`/
`30043521477` and PR `30043524643`/`30043524550`/`30043524574` all pass. Live proxy/certificate
interoperability, interactive prompts, human review, cross-client parity, signing, rollback, and
stable authorization remain open.

The latest Linux-first Secret Service persistence checkpoint adds runtime test
`bb6bc5bef572eb19d7c066e24a2d48546bf4fb08`, packaging/docs `9dc863eeb9fc5825c7354863c59bb21bf4447381`,
and final status head `2c3212c562eb8d425ee302a329f77ed7821a3231`. The worker filter now proves that
persistent primary, secret-header, proxy-auth, and client-certificate SecretRefs survive profile
persistence while all three session-only refs are removed before SQLite. Local checks pass; push
Native/Flatpak/Foundation `30041197129`/`30041196965`/`30041196986` and PR
`30041200604`/`30041200579`/`30041200581` all pass, with Native completing the real GTK Secret
Service integration fixture. This strengthens unreleased Linux secure-onboarding evidence;
interactive prompts, human review, cross-client parity, signing, rollback, and stable
authorization remain open.

The latest Linux-first Secret Service checkpoint adds runtime test
`f6cdb44dd6e411c2fab1c9f39cd3cd63361a1352`, packaging/docs `d1e7368edcf8426d3986165fc5b2adbd33cabe48`,
and final status head `e9b7d80e3ecac045eeb10b37ea59871c0ada6198`. The GTK Remember/clear-form
fixture enters bounded secret custom-header JSON, verifies a second persistent SecretRef and
active-profile restoration, clears both sensitive fields, scans SQLite artifacts for both canaries,
and deletes both Secret Service items. Local checks pass; push Native/Flatpak/Foundation
`30039406785`/`30039406821`/`30039406753` and PR `30039409345`/`30039409381`/`30039409339` all
pass, with Native explicitly completing the real GTK Secret Service integration fixture. This
strengthens unreleased Linux secure-onboarding evidence; interactive prompts, human review,
cross-client parity, signing, rollback, and stable authorization remain open.

The latest Linux-first export checkpoint adds runtime/test commit
`361ac7ba9d6a18c26de4487ab424d6500fbbeafd` and packaging/status head
`71b6fa34d536ec5753160ad270b507bd9fffa518`. A serialized GTK child-process fixture is killed
after its same-directory temporary file is synchronized and before final move; the final
destination remains absent while the durable temporary bytes remain intact. Local checks pass,
and final status-head push Native/Flatpak/Foundation `30037853956`/`30037853881`/`30037853988` plus PR
`30037855907`/`30037855888`/`30037855890` all pass, with Native explicitly completing the new
fixture. This remains bounded process/crash-durability evidence: physical power-loss recovery,
alternate VFS behavior, other clients, human review, signing, rollback, and stable authorization
remain open.

The current Linux-first local-export durability checkpoint adds runtime `cf4246c24e087de870adae4878379512cbaf2b8a`
and packaging/documentation head `9085ed2f8a3acf39f24930ca2dcf98567427c80f`. Local filesystem
exports sync temporary file bytes before the non-overwriting move and sync the destination
directory afterward; failures surface as save errors. Local formatting, locked compile, strict
Clippy, 163 demo-provider tests (three documented ignores), localization, synchronization,
Flatpak metadata, and diff checks pass. Push Native/Flatpak/Foundation `30032394587`/
`30032394653`/`30032394626` and PR `30032396787`/`30032396790`/`30032396829` pass. This is
bounded crash-durability evidence only: physical power-loss recovery, alternate VFS behavior,
other clients, human review, signing, rollback, and stable authorization remain open.
The canonical localization input is `c2526bfb3f6ff57895bdc3eeed743e26c8783613`, matching Linux's
checked synchronization script and generated resources; no new l10n strings were needed here.

The follow-up Linux export regression adds direct file/parent-directory sync coverage at
`3a84352410271ce53f01cfed162d83aad8c33719`; runtime remains `cf4246c24e087de870adae4878379512cbaf2b8a`,
docs/packaging is `8dc86c50ddd5a03fe223a9eaaa5f2a9326e1175b`, and final status is
`d52ab2f7bd339f360a26497d5a42bb7184b742e9`. Push Native/Flatpak/Foundation
`30034083462`/`30034083390`/`30034083610` and PR
`30034086699`/`30034087655`/`30034086738` passed. This remains bounded local-filesystem evidence;
physical power-loss recovery, alternate VFS behavior, other clients, human review, signing,
rollback, and stable authorization remain open.

The Linux candidate-management reconciliation is now documented at status/docs head
`e13d6804b7ce17edb1490c5dc6629b9664d6c3b7`. Existing editor commits
`c0cdee8b729a6800904f67535430221feb55f78e` and `a4dd4aa644335a3b6539db4d40473423c6292c71`
provide drag ordering and same-ID edit/save; serialized GTK test
`5c49a3a18c448542bc9cf055cd81b4a0b5f01e15` covers accessible controls, Manual single-candidate
normalization, Ordered/Automatic chain persistence, and Use lifecycle. Worker fallback-chain and
one-shot approval are covered by `0e2ae25c321cef243275d1322f2b8271f0602d06` and
`af200122e4862f6230d89268f5292f16438449bb`. Push Native/Flatpak/Foundation
`30035253038`/`30035253264`/`30035253013` and PR
`30035256459`/`30035256435`/`30035256652` passed. Visual/translated-copy/Orca review,
cross-client parity, signing, rollback, and stable authorization remain open.

The current Linux-first language-swap checkpoint adds Linux code
`4e5a94feef09bbe382a0b6690dc8e8f7b138656f`, packaging/docs head
`6a9adf472c6ca7afb26311dd0bbe06de2a0f1c05`, and localization
`c2526bfb3f6ff57895bdc3eeed743e26c8783613` (506 messages): the localized, focusable Swap languages
control exchanges only the supported English/Chinese selector pair locally, preserves editor
contents, and remains disabled for Auto-source or Japanese-target combinations. Local Linux/l10n
checks pass. PR #1 Native/Flatpak/Foundation runs `30030245422`/`30030245461`/`30030245538` passed;
push Native/Flatpak/Foundation `30030243332`/`30030242763`/`30030242764` all passed. The PR stays
Draft/Open and Issue #1 stays Open; human visual/Orca review, cross-client
parity, signing, rollback, and stable authorization remain open.

The current Linux-first text workspace checkpoint adds Linux code `38275fd96f0b9ed00b7d3269974780fd61874936`,
packaging/workflow head `54b9a29b6a72db38ae8eabcb91e1cf98dd73ecab`, and l10n
`99e0e04d200a03b2de79a8dd4a8d018847519ea2` (504 messages): the localized, focusable Clear workspace
action removes source/output text, request diagnostics, transient notices, and file URIs locally
without a worker command, while preserving provider, locale, glossary, and history settings. The
reducer and GTK regressions pass locally; current-head Linux push/PR Native, Flatpak, and Foundation
gates `30027666940`/`30027665976`/`30027665616` and `30027667935`/`30027667025`/`30027666925` passed.
The PR remains Draft/Open and Issue #1 remains Open; visual/Orca review, cross-client parity, signing,
rollback, and stable authorization remain open.

The current Linux-first clipboard checkpoint adds Linux `e56e56bec0bcea9fe963ca326e3918da54f50790`
and l10n `0ee87720a8613d3dc130dfb379ab4dc7bc1e1f62` (502 messages): completed output has an explicit
localized GTK Copy translation action, empty output keeps the action disabled, and a headless GTK
regression reads the copied text back through the display clipboard. Clipboard contents never enter
Core persistence, diagnostics, or notifications. Local Linux/l10n checks pass; current-head Linux
push Native/Flatpak/Foundation runs `30024453944`/`30024454262`/`30024454369` and PR
Native/Flatpak/Foundation runs `30024457039`/`30024457175`/`30024457027` all passed for the
documentation/Flatpak pin head `89f0f2d4fe9f748f34ea388daf91c52228b92b74`. Cross-client parity,
human review, signing, rollback, and stable authorization remain open. Central manifest/document
coordination commit `555c83e00b5556101d95465771c23617cb909192` passed workflow `30025928902` on
Linux and PowerShell.

The current Linux-first provider error checkpoint adds Core `8623b2c8829e4d9cf7299c74440dcfabb4e320db`,
l10n `630a8f36d96be358d81b72e2efc87cd527e66974`, and Linux `a7ac73d6fe8707519dd02698c26ebf8ca78a4246`:
HTTP 429 responses normalize to `RateLimited`, bounded `Retry-After` hints survive the provider
boundary, and Linux renders localized plural retry guidance. Local Core/Linux/l10n checks pass;
current-head Push Native/Flatpak/Foundation runs `30022122318`/`30022122787`/`30022122379` and PR
Native/Flatpak/Foundation runs `30022125925`/`30022125926`/`30022126939` all passed. Live quota
behavior, cross-client parity, human review, signing, rollback, and stable authorization remain open.

## Current Linux-first checkpoint

The Linux provider form now exposes an optional manual model field for every preset. Core
`7d0f61ee528d32a5671c65d3c253c12368cf40c4` preserves a validated selected model as a localized
`Manual` entry when native/protocol discovery is empty or returns `ModelUnavailable` (including
HTTP 404); authentication, network, and timeout failures remain typed errors. Linux functional
code `871c2da4e5f41cfb8197c7688ee0dd9f11b245fe` and packaging/status head `9bda4c64263167cba271fbf70abec546aa68b3fc` carry the UI,
Flatpak pins, and evidence. Local Core/Linux validation passed; the exact GTK binary is compile-
verified but cannot link on this host because GTK/GDK/Graphene symbols are unavailable. This remains
prerelease Linux evidence; other clients, human/physical review, signing, rollback, and stable
authorization remain open.

The Provider Hub health label now has a serialized GTK lifecycle fixture at Linux
`1155a224f74da8b2e2b201ad01139ef1df97a2e2`, covering hidden, UTC success, normalized failure,
clear, and no-selection states without exposing credentials or raw diagnostics. The synchronized
documentation/Flatpak head is `c39a5566ae0c87ef892cf9ba38f446b3a16429e5`, with Core
`460728d79b0e2373445c3d8994793d069b8057b9` and l10n
`74f773774bdf01ca5d2ab61ce199dbd76cdadb04`. Push Native/Flatpak/Foundation runs
`30016302142`/`30016302028`/`30016302180` passed; PR Native/Flatpak/Foundation runs
`30016306021`/`30016305892`/`30016305878` also completed successfully. This remains prerelease evidence; other clients,
qualified human/physical review, signing, rollback, and stable authorization remain open.

The Linux Provider Hub now renders persisted provider-health outcomes without exposing raw
diagnostics or credentials. Linux code `8a913b263475bec70639c55550bdf9717ded4012`, localization
`74f773774bdf01ca5d2ab61ce199dbd76cdadb04` (499 messages), and documentation/Flatpak head
`c75508f887a76e46782a6176e61b560888983c13` are synchronized. Push and PR Native/Flatpak/Foundation
gates passed at `30013497323`/`30013497315`/`30013497291` and
`30013503182`/`30013503000`/`30013502922`. This remains prerelease evidence; other clients,
qualified human/physical review, signing, rollback, and stable authorization remain open.

## Milestone matrix

| Milestone | Current evidence | Remaining completion work |
| --- | --- | --- |
| 0 — Foundation | Verified for all seven public repositories | Keep manifests and goal pins synchronized |
| 1 — Core vertical slice | Verified Core CLI, fake streaming, cancellation, ABI/protocol, storage, tests, and CI | Stable-release conformance and cross-client consumers |
| 2 — SDK artifacts | Prerelease Linux, Android, Apple artifacts and ABI 1 wrappers are CI-verified; Core ABI 1 now projects bounded provider metadata | Windows/Android/Apple host-service conformance, lease transfer, signed artifacts |
| 3 — Native clients | Linux GTK slice is substantially verified; Android and macOS are partial; Windows is foundation-only | Real provider/secret/model/translation flows on all four clients, device and desktop evidence |
| 4–5 — Providers and quality | Linux catalog, local models, model-source provenance labels, persisted Provider Hub health outcomes, routing, candidate-chain editing, one-shot fallback consent, request-level glossary protection, bounded TBX import, persistent Core schema 33 glossary libraries with GTK save/list/load/delete controls, chunking, history, memory, domain/tone/formality/audience presets, bounded regional-locale/script presets, bounded proxy transport settings and SecretRef authentication, bounded total/connection/streaming-idle timeout settings, additive custom PEM trust bundles, client-certificate SecretRef identities, and a pinned third-party Ollama daemon fixture have deterministic evidence | Cross-client parity, live-provider account/quota interoperability, provider-specific semantics |
| 6 — Documents | Linux supports the bounded TXT/Markdown/HTML/JSON/CSV/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB/PDF slice plus an explicit image-only PDF OCR fixture | Native document workflows on the other clients and broader format acceptance |
| 7 — Localization/accessibility | Generated packs, runtime switching, RTL, pseudo-locales, keyboard and headless AT-SPI/Orca checks exist | Qualified translation review, human screen-reader/visual review, other-client checks |
| 8 — Hardening/release | Fuzzing, sanitizers, migrations, parser limits, checksums, SBOMs, performance evidence, Unix process-crash WAL recovery, and controlled ENOSPC degradation exist | Physical VFS/power-loss evidence, alternate-VFS coverage, signing, rollback rehearsal, stable release authorization |

## Acceptance-scenario matrix

Linux CI/runtime evidence exists for Scenarios 4–18 (with the documented provider, display,
and human-review boundaries), including the production GTK Scenario 5 A→B switch fixture, the
candidate-chain/fallback-consent lifecycle fixture, and Anthropic/Gemini/Azure protocol-preset
transport fixture.
Scenario 1 and Scenario 19 have central/core evidence. Scenarios 2, 3, 5, 8, 13, and 16
remain globally incomplete until every required native client passes. Scenario 10 and 11
are Linux document evidence only. Scenario 20 is not achieved: the release manifest is
intentionally `unreleased` and contains no stable artifacts.

## Next executable gates

1. Keep the Linux PR, central issue, and release documentation synchronized with the latest
   verified heads, including the Provider Hub health UI, shared routing planner and approved
   fallback, glossary-library selector/localization, bounded TBX import, model-source provenance
   labels, regional-locale/script presets, provider-switch, Anthropic/Gemini/Azure protocol-preset,
   proxy-authentication, proxy-settings, timeout, custom-trust-bundle, and client-certificate
   identity checkpoints.
2. Do not promote any prerelease evidence to a stable component or release artifact.
3. When the Linux-first scope is released by the user, implement the next native-client
   conformance slice and repeat the same Core/l10n/manifest/CI evidence loop.

Unverified manual, physical, credentialed, signing, and other-client work remains explicitly
unverified rather than being inferred from deterministic Linux fixtures.
