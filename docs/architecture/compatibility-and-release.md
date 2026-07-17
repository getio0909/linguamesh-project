# Compatibility and Release Trains

LinguaMesh versions the core, SDK artifacts, clients, localization bundle, provider catalog, and protocol schema with semantic versioning. The C ABI has an additional monotonic major version.

`release-manifest.toml` identifies one known-good train: exact component versions and source revisions, ABI and schema versions, minimum compatibility, checksummed artifacts, status, and limitations. Stable clients consume pinned released artifacts, never an unpinned core branch.

At startup, each client queries the core semantic version, ABI version, protocol version, provider-catalog version, and enabled features. An unknown ABI major or incompatible protocol fails closed. `COMPATIBILITY.md` is the human-readable view of the same facts.

A breaking ABI change requires an RFC, ADR, new ABI major, regenerated bindings, migration guidance, client changes, conformance tests, and an updated release train. Release promotion requires source and artifact provenance, license and third-party notices, checksums, SBOMs where practical, platform build evidence, rollback instructions, and acceptance-scenario evidence.

The current unreleased matrix pins Core functional revision
`fbf3e9b5927049dccaa19f8c36013495ffebba12` and Linux functional revision
`726508f8412727f8b14e32d27407487491f5e4cd`, both at `0.1.0-alpha.2`, ABI 1, and wire protocol 1.
Linux evidence head `93f40456a53074ad437e4ee74634348c35afc049` adds only evidence documentation
relative to that functional source. Native CI verifies the current GTK flow under X11/Xvfb and
forced Wayland/headless Weston plus real post-startup `ENOSPC` rollback for persistent connection,
model-update, and deletion transactions. The same GTK test verifies baseline roles, named
multi-line editors, label/mnemonic relations, focusability, hidden empty errors, and Busy/reset
semantics using GTK 4.10 APIs. Completed translations emit a generic desktop notification without
source or translated content; notification-server delivery and packaging remain open. Native text
import uses a bounded UTF-8 GTK FileDialog/GIO path and a single-file source-editor DropTarget;
portal leases remain open.
The GIO Secret Service adapter sends a valid single-layer plain-string OpenSession Variant, and an
isolated real-daemon fixture verifies default-collection CRUD, resolution, and cleanup. Persistent
desktop restoration and locked/prompted behavior remain unverified. Runtime catalog switching currently covers the Translate and Stop labels, not
the complete UI. This does not prove every database or storage failure, AT-SPI/Orca,
physical keyboard traversal, or a complete desktop accessibility matrix.
Their CI evidence publishes no artifact. Linux multi-profile/session onboarding, next-request
routing, and storage rollback are not evidence of completed secure credential storage or a complete
acceptance scenario. Values such as `0.0.0-dev`, prerelease source checkpoints,
empty artifact lists, and `unreleased` remain explicit non-releases.
