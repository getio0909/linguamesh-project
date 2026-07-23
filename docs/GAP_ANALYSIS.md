# LinguaMesh Completion Gap Analysis

Status: Linux-first prerelease audit, 2026-07-23. This document complements
`PROJECT_GOAL.md`; it does not lower any acceptance requirement.

Assumption: Linux is the active implementation scope for the current checkpoint, while
Android, Windows, and macOS evidence must still be completed before a stable release.

The current Linux-first provider error checkpoint adds Core `8623b2c8829e4d9cf7299c74440dcfabb4e320db`,
l10n `630a8f36d96be358d81b72e2efc87cd527e66974`, and Linux `a7ac73d6fe8707519dd02698c26ebf8ca78a4246`:
HTTP 429 responses normalize to `RateLimited`, bounded `Retry-After` hints survive the provider
boundary, and Linux renders localized plural retry guidance. Local Core/Linux/l10n checks pass;
remote CI, live quota behavior, cross-client parity, human review, signing, rollback, and stable
authorization remain open.

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
