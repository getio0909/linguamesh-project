# RFC-0001: ABI 1 Engine-Bound Buffer Ownership

Status: Accepted

Authors: LinguaMesh maintainers

Tracking issue: [#1](https://github.com/getio0909/linguamesh-project/issues/1)

## Summary

Promote the prerelease native boundary from ABI major 0 to 1. Replace the process-wide buffer release contract with `lm_engine_buffer_free(engine, buffer)`, and keep every active allocation and ownership token inside the producing engine.

## Motivation and user impact

The published ABI 0 skeleton exposed `lm_buffer_free(buffer)`. Safely rejecting forged, copied, wrong-owner, and duplicate descriptors under that signature requires process-global mutable ownership state, which conflicts with the Rust architecture rules. No ABI 0 SDK artifact or compatible client was released, but changing the signature is still a breaking contract change and therefore requires a new ABI major.

## Detailed design

- Each engine owns a bounded registry of at most 64 outstanding event buffers.
- Polling reserves capacity before consuming an event and fails with `LM_RESULT_RESOURCE_EXHAUSTED` when the caller has not released enough buffers.
- A non-empty descriptor carries a nonzero allocation ID. Release validates engine ownership, ID, pointer, length, and capacity before dropping the allocation.
- Shutdown preserves buffer release; clients must release all buffers before destroying the engine.
- Kotlin/JNI, C++, and Swift wrappers copy event bytes and release the native allocation while the engine call remains active.

## Security and privacy

The design never dereferences an unregistered data pointer and never frees client-owned memory. Registries are per-engine, bounded, process-local, non-persistent, and contain no credential data by design. Existing stale-handle and forged-engine limitations remain explicit for ABI 1 prerelease work.

## Compatibility and migration

ABI 0 clients must regenerate or update their wrapper and call the engine-bound release function. Clients query ABI major 1 and fail closed for any other major. Protocol version 1 and message encodings are unchanged.

## Platform impact

Android JNI, the generic C++ wrapper, and the Swift package change internally. Their public high-level polling APIs continue returning owned platform byte containers. Linux direct-Rust integration does not cross this C allocation boundary.

## Test and release plan

Core tests cover wrong-engine release, forged and copied descriptors, duplicate release, shutdown-time release, bounded exhaustion, and slot recovery. C/C++ smoke tests and native platform jobs must pass before clients pin the exact Core revision. The central manifest remains `unreleased`.

## Alternatives

A process-global registry was rejected because global mutable state is prohibited. Trusting descriptor pointers or embedding an unvalidated owner pointer was rejected because forged input could trigger invalid memory access. Leaking ABI 0 compatibility shims was rejected because they could not preserve the required safety properties.

## Rollback

Before any release, clients can roll back to the last verified source checkpoint, which has no consumable SDK artifact. After an ABI 1 prerelease is recorded, rollback means selecting an exact compatible source/artifact train; published history is never rewritten.

## Unresolved questions

None for this transition. Handle-registry hardening, sanitizers, fuzzing, and full platform conformance remain later prerelease gates.
