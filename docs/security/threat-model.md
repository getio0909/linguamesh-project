# Threat Model

Status: skeleton for Milestone 0; owners and test evidence must be completed before a stable release.

## Assets and actors

Protected assets include API credentials, source and translated content, document structure, local history and translation memory, routing choices, release artifacts, and update metadata. Threat actors include malicious endpoints, compromised providers or dependencies, crafted documents and locale packs, local attackers, and accidental disclosure through diagnostics.

## Trust boundaries

- Native UI to shared core through the versioned ABI or typed Rust API.
- Core to platform secret and file brokers through explicit host requests.
- Core transport to local or remote providers.
- Parsers to untrusted source documents and generated output.
- Build and release jobs to registries, signing systems, and public artifacts.

The diagrams and detailed flows are maintained in [`data-flow.md`](data-flow.md) and [`trust-boundaries.md`](trust-boundaries.md).

## Priority abuse cases

Credential leakage, cross-origin authorization forwarding, prompt injection, fallback to an unapproved provider, malformed SSE/Protobuf, ZIP traversal or bombs, XML entities, parser exhaustion, output overwrite or corruption, insecure temporary files, executable locale/catalog content, database or clipboard disclosure, FFI memory misuse, dependency compromise, and stale SDK artifacts.

## Required controls

Use just-in-time `SecretRef` resolution, redacted diagnostics, explicit provider identity and fallback consent, bounded parsing and queues, secure temporary storage, output validation and atomic distinct-name finalization, schema and checksum validation, ABI negotiation, fuzzing and sanitizers, dependency/license/secret scanning, and unprivileged fork CI.

Residual risk, control ownership, tests, and review dates must be tracked as implementations arrive.
