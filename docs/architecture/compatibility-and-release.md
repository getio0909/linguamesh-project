# Compatibility and Release Trains

LinguaMesh versions the core, SDK artifacts, clients, localization bundle, provider catalog, and protocol schema with semantic versioning. The C ABI has an additional monotonic major version.

`release-manifest.toml` identifies one known-good train: exact component versions and source revisions, ABI and schema versions, minimum compatibility, checksummed artifacts, status, and limitations. Stable clients consume pinned released artifacts, never an unpinned core branch.

At startup, each client queries the core semantic version, ABI version, protocol version, provider-catalog version, and enabled features. An unknown ABI major or incompatible protocol fails closed. `COMPATIBILITY.md` is the human-readable view of the same facts.

A breaking ABI change requires an RFC, ADR, new ABI major, regenerated bindings, migration guidance, client changes, conformance tests, and an updated release train. Release promotion requires source and artifact provenance, license and third-party notices, checksums, SBOMs where practical, platform build evidence, rollback instructions, and acceptance-scenario evidence.

Bootstrap values such as `0.0.0-dev`, ABI `0`, or `unreleased` are explicit non-releases.
