# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Bootstrap compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.1` | ABI `0`, protocol `0.1.0` | Locally verified, unreleased |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.0.0-dev` | Message schema `0` | Unreleased |
| Android client | `0.0.0-dev` | No SDK selected | Unreleased |
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.0.0-dev` | No core selected | Unreleased |

Stable clients must pin a released core and reject an unknown ABI major. Every release-train update must include source revisions, artifact checksums, minimum compatible versions, known limitations, and cross-repository conformance evidence. Development placeholders are not consumable releases.
