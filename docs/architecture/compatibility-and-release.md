# Compatibility and Release Trains

LinguaMesh versions the core, SDK artifacts, clients, localization bundle, provider catalog, and protocol schema with semantic versioning. The C ABI has an additional monotonic major version.

`release-manifest.toml` identifies one known-good train: exact component versions and source revisions, ABI and schema versions, minimum compatibility, checksummed artifacts, status, and limitations. Stable clients consume pinned released artifacts, never an unpinned core branch.

At startup, each client queries the core semantic version, ABI version, protocol version, provider-catalog version, and enabled features. An unknown ABI major or incompatible protocol fails closed. `COMPATIBILITY.md` is the human-readable view of the same facts.

A breaking ABI change requires an RFC, ADR, new ABI major, regenerated bindings, migration guidance, client changes, conformance tests, and an updated release train. Release promotion requires source and artifact provenance, license and third-party notices, checksums, SBOMs where practical, platform build evidence, rollback instructions, and acceptance-scenario evidence.

The current unreleased matrix pins Core functional revision
`fbf3e9b5927049dccaa19f8c36013495ffebba12` and Linux functional revision
`c37702c76c3b1a2f9cec805cf9e219721ef7b5ce`, both at `0.1.0-alpha.2`, ABI 1, and wire protocol 1.
Linux evidence head `2eadf06e5e63eec5b7a512a53a2741f4f2c77704` adds only evidence documentation
relative to that functional source. Native CI verifies the current GTK flow under X11/Xvfb and
forced Wayland/headless Weston plus real post-startup `ENOSPC` rollback for persistent connection,
model-update, and deletion transactions. This does not prove every database or storage failure.
Their CI evidence publishes no artifact. Linux credential-free multi-profile/session onboarding,
next-request routing, and storage rollback are not evidence of completed secure credential storage
or a complete acceptance scenario. Values such as `0.0.0-dev`, prerelease source checkpoints,
empty artifact lists, and `unreleased` remain explicit non-releases.
