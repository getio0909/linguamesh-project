# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Unreleased compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0` | Functional source `fbf3e9b5927049dccaa19f8c36013495ffebba12` CI-verified, unreleased |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1` | CI-verified development bundle, unreleased |
| Android client | `0.0.0-dev` | No SDK selected | Unreleased |
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; non-secret multi-profile/model persistence; session credentials | Functional source `c88d37a5de2f03c2ae5d2940c4d25e5d998c301d` passed native CI, unreleased |

The Linux client fails closed for persistent secrets because a native Secret Service backend is not
implemented. It can create, update, switch, and delete multiple credential-free provider profiles,
preserve independent confirmed model preferences, restore the full list/default without connecting,
require explicit Connect for activation, and keep a deleted connected row's validated runtime as
session-only. It requires credential re-entry and does not persist a credential or secret reference
or fall back to plaintext. Secret Service, complete onboarding, and Scenarios 3 and 5 remain
incomplete. Stable clients must pin a released core and reject an unknown ABI major. Every
release-train update must include source revisions, artifact checksums, minimum compatible versions,
known limitations, and cross-repository conformance evidence. Development placeholders and the
alpha.2 source checkpoints are not consumable releases.
