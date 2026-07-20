# ADR-0004: Engine-Bound FFI Buffer Ownership

Status: Accepted

Date: 2026-07-17

## Context

The ABI 0 skeleton released Rust-owned event bytes through a buffer-only function. Authenticating arbitrary descriptors under that signature required global mutable ownership state, while trusting raw pointer metadata would allow invalid frees.

## Decision

Adopt ABI major 1 and require the producing opaque engine in the sole buffer-release function. Store a bounded allocation registry and monotonic ownership tokens inside each engine. Platform wrappers copy event bytes and release the native allocation before ending the engine call.

## Consequences

Wrong-engine, forged, stale-copy, and duplicate descriptors fail safely. Outstanding native buffers are bounded. ABI 0 source consumers must migrate, while high-level Kotlin, C++, and Swift polling APIs retain platform-owned return values.

## Alternatives considered

A global registry, descriptor-only trust, embedded callable destructors, and an unsafe ABI 0 compatibility shim were rejected. Each either violates the architecture rules, accepts untrusted pointer metadata, or cannot preserve ownership safety.

## Compatibility and rollback

This is the ABI 0 to ABI 1 transition defined by [RFC-0001](../rfc/0001-abi-1-engine-bound-buffers.md) and tracked by [issue #1](https://github.com/getio0909/linguamesh-project/issues/1). Protocol version 1 is unchanged. Rollback selects an exact pre-transition source checkpoint; no ABI 0 SDK artifact is promoted or represented as compatible.
