# Compatibility and Release Trains

LinguaMesh versions the core, SDK artifacts, clients, localization bundle, provider catalog, and protocol schema with semantic versioning. The C ABI has an additional monotonic major version.

`release-manifest.toml` identifies one known-good train: exact component versions and source revisions, ABI and schema versions, minimum compatibility, checksummed artifacts, status, and limitations. Stable clients consume pinned released artifacts, never an unpinned core branch.

At startup, each client queries the core semantic version, ABI version, protocol version, provider-catalog version, and enabled features. An unknown ABI major or incompatible protocol fails closed. `COMPATIBILITY.md` is the human-readable view of the same facts.

A breaking ABI change requires an RFC, ADR, new ABI major, regenerated bindings, migration guidance, client changes, conformance tests, and an updated release train. Release promotion requires source and artifact provenance, license and third-party notices, checksums, SBOMs where practical, platform build evidence, rollback instructions, and acceptance-scenario evidence.

The current unreleased matrix pins Core functional revision
`fbf3e9b5927049dccaa19f8c36013495ffebba12` and Linux functional revision
`96d34a5448d0f718fd87c68e88129c05fed43ee5`, both at `0.1.0-alpha.2`, ABI 1, and wire protocol 1.
Linux evidence head `1553841dc527f1f3bc9556ce5f88650f28221d85` adds only evidence documentation
relative to that functional source. Native CI verifies the current GTK flow under X11/Xvfb and
forced Wayland/headless Weston plus real post-startup `ENOSPC` rollback for persistent connection,
model-update, and deletion transactions. The same GTK test verifies baseline roles, named
multi-line editors, label/mnemonic relations, focusability, hidden empty errors, and Busy/reset
semantics using GTK 4.10 APIs. Completed translations emit a generic desktop notification without
source or translated content; notification-server delivery and packaging remain open. Native text
import uses a bounded UTF-8 GTK FileDialog/GIO path; portal leases and drag-and-drop remain open.
The GIO Secret Service adapter is present, but the CI environment
does not provide a real desktop keyring service, so CRUD, locked/prompted behavior, and cleanup
remain unverified. Runtime catalog switching currently covers the Translate and Stop labels, not
the complete UI. This does not prove every database or storage failure, AT-SPI/Orca,
physical keyboard traversal, or a complete desktop accessibility matrix.
Their CI evidence publishes no artifact. Linux multi-profile/session onboarding, next-request
routing, and storage rollback are not evidence of completed secure credential storage or a complete
acceptance scenario. Values such as `0.0.0-dev`, prerelease source checkpoints,
empty artifact lists, and `unreleased` remain explicit non-releases.
