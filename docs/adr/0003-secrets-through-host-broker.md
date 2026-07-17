# ADR-0003: Secrets Through a Native Host Broker

Status: Accepted

Date: 2026-07-17

## Context

The core needs provider credentials but cannot implement equivalent secure storage across all native platforms or persist credential values safely in shared state.

## Decision

Persist only stable `SecretRef` identifiers. At operation time, the core emits a scoped secret request; the native client resolves it from platform secure storage and provides it for that operation. The core clears the value as soon as practical.

## Consequences

The protocol and wrappers must support host requests, response ordering, cancellation, zeroization-aware containers, and redaction tests. Secure-storage unavailability permits only a warned, explicit session-only secret.

## Alternatives considered

SQLite, plaintext preferences, environment persistence, and preloading all provider credentials were rejected.

## Compatibility and rollback

Secret host messages are versioned protocol contracts. A rollback may retain newer secure-storage entries but must not export or migrate secret values into normal settings.
