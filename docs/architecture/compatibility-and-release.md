# Compatibility and Release Trains

LinguaMesh versions the core, SDK artifacts, clients, localization bundle, provider catalog, and protocol schema with semantic versioning. The C ABI has an additional monotonic major version.

`release-manifest.toml` identifies one known-good train: exact component versions and source revisions, ABI and schema versions, minimum compatibility, checksummed artifacts, status, and limitations. Stable clients consume pinned released artifacts, never an unpinned core branch.

At startup, each client queries the core semantic version, ABI version, protocol version, provider-catalog version, and enabled features. An unknown ABI major or incompatible protocol fails closed. `COMPATIBILITY.md` is the human-readable view of the same facts.

A breaking ABI change requires an RFC, ADR, new ABI major, regenerated bindings, migration guidance, client changes, conformance tests, and an updated release train. Release promotion requires source and artifact provenance, license and third-party notices, checksums, SBOMs where practical, platform build evidence, rollback instructions, and acceptance-scenario evidence.

The current unreleased matrix pins Core functional revision
`0f71a652a536753f48bb8c852fd38e97740c23ce` and Linux functional revision
`766b78e4b236f15ee7a6f1d6e61ebd828415da82`, both at `0.1.0-alpha.2`, ABI 1, and wire protocol 1.
Linux evidence head `029e7f21322f3d0f3619a8f3a0158e7157972e30` adds official locale-pack switching,
Arabic RTL direction, Secret Service prompted-flow,
notification-daemon, portal,
interactive FileChooser backend, application FileDialog callback, source-editor drag/drop,
source-buffer-preservation, status-summary/partial-output, text-file import, provider-profile/source-target, onboarding-stage, active-provider, notification, and draft-note localization evidence documentation
relative to that functional source. Native CI verifies the current GTK flow under X11/Xvfb and
forced Wayland/headless Weston plus real post-startup `ENOSPC` rollback for persistent connection,
model-update, and deletion transactions. The same GTK test verifies baseline roles, named
multi-line editors, label/mnemonic relations, focusability, hidden empty errors, and Busy/reset
semantics using GTK 4.10 APIs. Completed translations emit a generic desktop notification without
source or translated content; private notification-service transport and headless delivery to a real
`dunst` daemon and a visible viewable Dunst window are verified, while physical compositor/GPU rendering, signing, and distributable artifacts remain open. Native text
import uses a bounded UTF-8 GTK FileDialog/GIO path for TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT plus bounded DOCX/PPTX packages and a URI-list/GIO source-editor DropTarget; the GTK queue lists persisted document snapshots with progress/state metadata and rebinds a selected job to the existing controls;
the real document-portal lease lifecycle, direct interactive `xdg-desktop-portal-gtk` FileChooser
backend, application FileDialog callback, and source-editor drag/drop gesture are verified under
Xvfb.
The GIO Secret Service adapter sends a valid single-layer plain-string OpenSession Variant, and an
isolated real-daemon fixture verifies default-collection CRUD, resolution, cleanup, persistent
daemon-restart restoration, locked-item fail-closed lookup, and secure persistent-credential
onboarding through both worker and GTK paths. The no-credential OpenAI-compatible loopback path is
also covered. A pinned Flatpak manifest, generated Cargo source set, desktop metadata, and icon pass
static validation; the GNOME 49 SDK workflow built a prerelease CI bundle and passed bounded sandbox
startup smoke, while physical compositor/GPU rendering, signing, and distributable artifacts remain
unverified. End-user prompt approval remains unverified; the adapter's store/delete prompt paths are
verified to fail closed. Runtime catalog switching covers all twelve official Linux packs for the
Translate and Stop labels plus catalog-backed workspace widgets, active-provider/status-summary/partial-output/text-file-import/provider-profile/source-target/onboarding-stage/notification/draft-note/theme-option labels, preserves active source text across the tested Arabic switch, and applies Arabic RTL direction, not the complete visible UI. This does not prove every database or storage failure, AT-SPI/Orca,
physical keyboard traversal, or a complete desktop accessibility matrix.
Their CI evidence publishes no artifact. Linux multi-profile/session onboarding, next-request
routing, and storage rollback are not evidence of completed secure credential storage or a complete
acceptance scenario. Values such as `0.0.0-dev`, prerelease source checkpoints,
empty artifact lists, and `unreleased` remain explicit non-releases.
