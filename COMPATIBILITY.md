# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Unreleased compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0` | Functional source `c9a96da52e10554c8458f4d49600ec9336ea651b` CI-verified, unreleased |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1` | CI-verified development bundle, unreleased |
| Android client | `0.0.0-dev` | No SDK selected | Unreleased |
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; session credentials only | Functional source `0455baf8f258c6280d66d1d568fd6a01fdad8486` passed native CI, unreleased |

The Linux client fails closed for persistent secrets because a native Secret Service backend is not
implemented. It does not persist provider profiles, restore them after restart, or fall back to
plaintext. Stable clients must pin a released core and reject an unknown ABI major. Every
release-train update must include source revisions, artifact checksums, minimum compatible
versions, known limitations, and cross-repository conformance evidence. Development placeholders
and the alpha.2 source checkpoints are not consumable releases.
