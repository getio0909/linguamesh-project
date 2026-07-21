# Privacy Model

Status: maintained data-inventory and minimization checkpoint; this model does not authorize a
stable release until manual review, cross-client conformance, and release controls are evidenced.

Review date: 2026-07-21  |  Owners: Core maintainers, native-client maintainers, release coordinator

## Data inventory

| Category | Examples | Destination | Retention and deletion | User control / evidence |
| --- | --- | --- | --- | --- |
| Source and translated content | Text, document segments, glossary context, output | Core memory; selected provider only after consent | Core bounds buffers; optional history/memory are local and clearable; Incognito writes neither | Provider/model is shown before dispatch; Core request, history, and memory policy tests |
| Credentials | API keys and custom secret headers | Platform secure storage; short-lived Core request | Never serialized or logged; delete from secure storage or drop session reference | `SecretRef` only; secret-canary and Linux Secret Service lifecycle tests |
| Document grants and paths | Portal lease, source basename, output destination | Host file broker and bounded job metadata | Lease expires/revokes; job metadata is user-deletable; source is not replaced by default | Explicit file selection and collision-safe output; FileLease/storage/import tests |
| Operational metadata | Provider/model IDs, routing decisions, usage, errors, timestamps | Local SQLite metadata and redacted UI diagnostics | Bounded by schema and clear-history/job controls; no telemetry by default | Diagnostics omit endpoints, credentials, and content; Core/Linux redaction tests |
| Local preferences | Locale, theme, window/accessibility settings | Native client configuration | User reset/export controls; no provider transmission | Native client settings and localization tests |
| Crash or diagnostic exports | User-selected technical context only | User-selected destination | Created only on explicit export; must remain content-free by default | Export review must reject credentials, headers, cookies, and unrequested content |

## Invariants

- Telemetry is off by default and never receives translation content or keys.
- Source text is data, not instructions; provider identity, model, and destination are explicit
  before transmission. Remote fallback requires the applicable saved-provider consent.
- Incognito mode bypasses history and translation-memory persistence. Disabling those features keeps
  existing entries until the user clears them, preventing a settings toggle from destroying data.
- Secure-storage failure offers an explicitly labeled memory-only session; plaintext persistence is
  never a fallback. Temporary files are private, bounded, cleaned after failure, and finalized
  under a distinct collision-safe name.

## Evidence and open review

Automated evidence is mapped in [`threat-model.md`](threat-model.md), [`data-flow.md`](data-flow.md),
and [`trust-boundaries.md`](trust-boundaries.md), with repository-level checks in the Core/Linux
workflows and `release-manifest.toml`. Manual visual/copy/accessibility review, physical desktop
behavior, live provider privacy terms, Android/Windows/macOS projections, signed artifacts, rollback,
and stable-release approval remain open and must be recorded before promotion.
