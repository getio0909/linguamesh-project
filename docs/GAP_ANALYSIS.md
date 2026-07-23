# LinguaMesh Completion Gap Analysis

Status: Linux-first prerelease audit, 2026-07-22. This document complements
`PROJECT_GOAL.md`; it does not lower any acceptance requirement.

Assumption: Linux is the active implementation scope for the current checkpoint, while
Android, Windows, and macOS evidence must still be completed before a stable release.

## Milestone matrix

| Milestone | Current evidence | Remaining completion work |
| --- | --- | --- |
| 0 — Foundation | Verified for all seven public repositories | Keep manifests and goal pins synchronized |
| 1 — Core vertical slice | Verified Core CLI, fake streaming, cancellation, ABI/protocol, storage, tests, and CI | Stable-release conformance and cross-client consumers |
| 2 — SDK artifacts | Prerelease Linux, Android, Apple artifacts and ABI 1 wrappers are CI-verified; Core ABI 1 now projects bounded provider metadata | Windows/Android/Apple host-service conformance, lease transfer, signed artifacts |
| 3 — Native clients | Linux GTK slice is substantially verified; Android and macOS are partial; Windows is foundation-only | Real provider/secret/model/translation flows on all four clients, device and desktop evidence |
| 4–5 — Providers and quality | Linux catalog, local models, routing, fallback, glossary, chunking, history, memory, presets, bounded proxy transport settings, and bounded total request timeout have deterministic evidence | Cross-client parity, live-provider interoperability, proxy authentication, connection/streaming-idle/TLS timeout policy, provider-specific semantics |
| 6 — Documents | Linux supports the bounded TXT/Markdown/HTML/JSON/CSV/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB/PDF slice | Native document workflows on the other clients and broader format acceptance |
| 7 — Localization/accessibility | Generated packs, runtime switching, RTL, pseudo-locales, keyboard and headless AT-SPI/Orca checks exist | Qualified translation review, human screen-reader/visual review, other-client checks |
| 8 — Hardening/release | Fuzzing, sanitizers, migrations, parser limits, checksums, SBOMs, and performance evidence exist | Physical VFS/power-loss evidence, signing, rollback rehearsal, stable release authorization |

## Acceptance-scenario matrix

Linux CI/runtime evidence exists for Scenarios 4, 6–18 (with the documented provider,
display, and human-review boundaries). Scenario 1 and Scenario 19 have central/core
evidence. Scenarios 2, 3, 5, 8, 13, and 16 have useful Linux or partial-client evidence
but are not globally complete until every required native client passes. Scenario 10 and
11 are Linux document evidence only. Scenario 20 is not achieved: the release manifest
is intentionally `unreleased` and contains no stable artifacts.

## Next executable gates

1. Keep the Linux PR and central issue synchronized with the latest verified heads, including the proxy-settings and request-timeout checkpoints.
2. Do not promote any prerelease evidence to a stable component or release artifact.
3. When the Linux-first scope is released by the user, implement the next native-client
   conformance slice and repeat the same Core/l10n/manifest/CI evidence loop.

Unverified manual, physical, credentialed, signing, and other-client work remains explicitly
unverified rather than being inferred from deterministic Linux fixtures.
