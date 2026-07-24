# Release Train bootstrap

Status: Draft

Date: 2026-07-24

This record describes the current Linux-first prerelease checkpoint. It is not a stable release
and must not be promoted without the acceptance and authorization gates listed below.

## Components and contracts

| Component | Version | Source revision |
| --- | --- | --- |
| Core | `0.1.0-alpha.2` | `8623b2c8829e4d9cf7299c74440dcfabb4e320db` |
| Localization | `0.1.0` | `c2526bfb3f6ff57895bdc3eeed743e26c8783613` |
| Android | `0.1.0-alpha.1` | `afe7a566bac77a16243f70295d17a4d9cab1151f` |
| Windows | `0.0.0-dev` | `unreleased` |
| macOS | `0.1.0-alpha.1` | `cad822c69dcf1ad20f8cab2151f407866a577420` |
| Linux | `0.1.0-alpha.2` | `1c513e2e52236fce03a60548dbcab242c6878bed` |

Contracts: ABI major `1`, protocol schema `0.1.0`, provider catalog `0.1.0`, and localization
schema `1.0.0`. The authoritative pins are in `release-manifest.toml`.

## Artifact provenance and checksums

No stable artifacts are published. Linux Native run `30058395686` and Flatpak run `30058395689`
generated and verified checksum/SBOM evidence and completed the Flatpak sandbox smoke; Foundation
run `30058395669` passed repository validation. These remain CI artifacts, not signed releases.

## Validation evidence

- Host-pinned Rust 1.93.0 Core check passed with `cargo check --workspace --locked --offline`.
- Linux non-GUI demo-provider tests passed `166 passed; 0 failed; 7 ignored` with loopback proxy
  bypassed. Native CI is authoritative for the GTK/AT-SPI, portal, mTLS, build, performance,
  checksum, and SBOM gates because this host lacks GTK4/Graphene development packages.
- Central workflow `30059285976` passed Linux and PowerShell validation for the synchronized
  coordination documents and release manifest.
- The documented clean-bootstrap flow cloned all seven public repositories in a disposable
  workspace and passed strict workspace, goal-pin, manifest, link, and credential-signature checks.

## Acceptance scenarios

Linux evidence covers the deterministic portions of Scenarios 4–18 and central/Core evidence
covers Scenarios 1 and 19. Scenarios requiring every client, qualified human or physical review,
or a stable release remain incomplete.

## Security, privacy, licenses, and SBOMs

Credentials remain runtime-only and are excluded from source, persistence, diagnostics, and CI.
The Native and Flatpak runs generated SPDX/checksum evidence; signing and notarization are not
claimed. The repositories remain MIT-licensed and dependency/license checks passed in CI.

## Known limitations

Android, Windows, and macOS parity; live-provider account interoperability; human visual,
translation, and screen-reader review; physical VFS/power-loss behavior; signed artifacts;
rollback rehearsal; and stable-release authorization remain open. Release status stays
`unreleased`.

## Migration and rollback

This draft changes no persisted schema or public contract. To roll back this checkpoint, restore
the previous verified Linux revision in `release-manifest.toml`, run `bash tools/check-workspace.sh`
and the central workflow, then document the resulting source and CI revisions. Do not force-push,
rewrite published history, or promote the rollback as stable without explicit authorization.

## Signing and publication status

No tag, GitHub Release, signing, notarization, or stable publication was performed. Any future
release must first satisfy every mandatory acceptance scenario and update this record together
with the manifest, compatibility table, checksums, SBOMs, and rollback evidence.
