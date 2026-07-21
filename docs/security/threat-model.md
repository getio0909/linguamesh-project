# Threat Model

Status: maintained Milestone 8 evidence map; stable-release sign-off remains blocked until every
residual risk below has an owner, test evidence, and review result.

Review date: 2026-07-21  |  Owners: Core maintainers, native-client maintainers, release coordinator

## Scope and trust boundaries

Protected assets are credentials, source and translated content, document structure, local history
and translation memory, routing choices, release artifacts, and update metadata. Actors include
malicious endpoints or providers, compromised dependencies or locale packs, crafted documents,
local attackers, and accidental disclosure through diagnostics.

The boundaries are native UI ↔ versioned Core ABI/typed API, Core ↔ platform secret/file brokers,
Core ↔ local or remote providers, parsers ↔ untrusted bytes and generated output, and CI ↔ public
registries/signing/release systems. The authoritative flow diagrams are
[`data-flow.md`](data-flow.md) and [`trust-boundaries.md`](trust-boundaries.md).

## Abuse cases, controls, and evidence

| Threat | Required control | Evidence / owner | Status |
| --- | --- | --- | --- |
| API-key or log leakage | Just-in-time `SecretRef`; redacted errors; no credential/content logs | Core domain/application redaction tests; Linux Secret Service and diagnostics tests / Core + Linux maintainers | Automated |
| Redirect or malicious endpoint | HTTPS by default; loopback HTTP exception; origin-checked redirects; no TLS bypass | Provider API endpoint-policy tests / Core maintainers | Automated |
| Prompt injection or malicious output | Delimited untrusted data, protected-span restoration, bounded output validation, no execution | Provider prompt, engine, and streamed-output tests / Core maintainers | Automated |
| ZIP bombs, traversal, XML entities, parser exhaustion | Entry/path/ratio/size/depth limits; reject DTD/entities and unsafe packages | Document codec tests plus `document_decoders` ASAN fuzz target / Core maintainers | Automated |
| Malformed SSE, Protobuf, or oversized responses | Typed decoders, cancellation, hard byte bounds, one terminal event | Protocol fuzz, provider decoder, and FFI tests / Core maintainers | Automated |
| Database, temporary-file, clipboard, or crash disclosure | `NOFOLLOW`, private temp/output paths, opt-in history/memory, redacted diagnostics | Core storage tests; Linux file/import/history tests / Core + Linux maintainers | Automated; crash-report policy review pending |
| Unapproved fallback disclosure | Display receiving provider/model and require explicit consent for remote fallback | Linux routing/fallback worker and GTK lifecycle tests / Linux maintainers | Automated; human copy review pending |
| Malicious locale/catalog or remote catalog tampering | Schema validation, immutable pins, no executable locale content, source-level audits | Core catalog tests, Linux localization audits, workspace pin checks / Release coordinator | Automated |
| FFI memory corruption or use-after-free | Version/length/ownership checks, panic containment, engine-scoped lifetimes, sanitizers | Core FFI tests, C/C++ smoke, fuzz/ASAN workflow / Core maintainers | Automated |
| Dependency compromise or stale native Core | Advisory/license/secret scans and exact cross-repository revisions | `cargo deny`, repository foundation CI, `release-manifest.toml` / Release coordinator | Automated |

## Residual risk and release gate

Prompted desktop approval, physical compositor/GPU rendering, end-user visual/Orca review, live
provider account behavior, other-client conformance, signed artifacts, rollback rehearsal, and
stable release authorization are not proven by headless CI. Each must be recorded in
`IMPLEMENTATION_STATUS.md` with a named role, reproducible evidence, and review date before a
stable release is permitted. Never treat a green automated check as evidence for a manual boundary.
