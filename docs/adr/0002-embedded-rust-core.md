# ADR-0002: Embedded Rust Core with Native Clients

Status: Accepted

Date: 2026-07-17

## Context

Shared provider, translation, document, persistence, and error behavior must remain consistent while each platform requires native UI, lifecycle, accessibility, and secure storage.

## Decision

Embed a shared Rust core as a native library. Android, Windows, and macOS use generated wrappers around a stable C ABI and versioned event protocol; Linux uses the same Rust application behavior directly. Platform clients remain fully native and own host services.

## Consequences

The boundary requires explicit ownership, version negotiation, event polling, panic containment, generated wrappers, and cross-platform conformance tests. Large files use leases instead of copied protocol payloads.

## Alternatives considered

Shared UI frameworks, a local daemon, a localhost API, and direct Rust callbacks into arbitrary runtime threads were rejected as production defaults.

## Compatibility and rollback

Breaking ABI changes require an RFC, a new ABI major, regenerated bindings, client migrations, and conformance evidence. Clients fail closed on unknown majors.
