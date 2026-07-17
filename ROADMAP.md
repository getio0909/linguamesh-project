# Roadmap

Roadmap status is evidence-based. Dates are intentionally omitted until toolchains, staffing, and release quality support reliable forecasts.

## Milestone 0 — Foundation

- Central policies, architecture records, manifests, workspace automation, templates, and CI.
- Local foundations for all canonical repositories.

## Milestone 1 — Core translation slice

- Provider-neutral Rust engine, protocol, fake streaming provider, OpenAI-compatible adapter, model selection, cancellation, typed errors, SQLite migrations, CLI, and tests.

## Milestones 2–3 — SDKs and native clients

- Versioned C ABI, Protobuf event protocol, generated Android/Windows/macOS wrappers, and direct Linux integration.
- Working native translation vertical slices on Android, Windows, macOS, and Linux.

## Milestones 4–5 — Providers and quality

- Required provider families, model discovery, routing, explicit fallback, usage normalization, protected spans, glossaries, chunking, translation memory, history, and incognito mode.

## Milestones 6–7 — Documents, localization, and accessibility

- Incremental format delivery with extraction, reconstruction, validation, and source preservation.
- Twelve official UI locales, runtime switching, RTL, pseudo-localization, keyboard access, and native accessibility evidence.

## Milestone 8 — Hardening and stable release

- Threat and privacy reviews, fuzzing, migrations, performance baselines, packaging, SBOMs, checksums, conformance CI, and all mandatory acceptance scenarios.

Only versions with reproducible compatibility evidence may enter a stable release train.

