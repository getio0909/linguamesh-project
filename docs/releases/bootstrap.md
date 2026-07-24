# Release Train bootstrap

Status: Draft

Date: 2026-07-24

This record describes the current Linux-first prerelease checkpoint. It is not a stable release
and must not be promoted without the acceptance and authorization gates listed below.

## Components and contracts

| Component | Version | Source revision |
| --- | --- | --- |
| Core | `0.1.0-alpha.2` | `6786754f4c42056b55e4d68780326a16eb6a4e4f` |
| Localization | `0.1.0` | `c2526bfb3f6ff57895bdc3eeed743e26c8783613` |
| Android | `0.1.0-alpha.1` | `afe7a566bac77a16243f70295d17a4d9cab1151f` |
| Windows | `0.0.0-dev` | `unreleased` |
| macOS | `0.1.0-alpha.1` | `cad822c69dcf1ad20f8cab2151f407866a577420` |
| Linux | `0.1.0-alpha.2` | `1c513e2e52236fce03a60548dbcab242c6878bed` |

Contracts: ABI major `1`, protocol schema `0.1.0`, provider catalog `0.1.0`, and localization
schema `1.0.0`. The authoritative pins are in `release-manifest.toml`.

## Artifact provenance and checksums

No stable artifacts are published. Core Fuzz/ASAN run `30060612978` (job `89381326908`) passed
protocol, document, and bounded FFI input targets; Core CI `30060612966` and Native SDK run
`30060612972` passed all four platform jobs. Linux Native run `30058395686` and Flatpak run `30058395689`
generated and verified checksum/SBOM evidence and completed the Flatpak sandbox smoke; Foundation
run `30058395669` passed repository validation. These remain CI artifacts, not signed releases.

## Validation evidence

- Host-pinned Rust 1.93.0 Core check passed with `cargo check --workspace --locked --offline`.
- Core FFI input ASAN smoke passed 200 local runs with 299 coverage features and a 29-file
  minimized corpus. The target bounds input at 1 MiB, skips valid translation envelopes, and
  asserts controlled malformed/unsupported result codes without provider/network work.
- Host-pinned Rust 1.93.0 Core storage regression passed `55 passed; 0 failed` with
  `cargo +1.93.0 test -p linguamesh-storage --locked --offline`, covering WAL replay,
  abrupt-process recovery, busy-checkpoint retry, migrations, secure deletion, symlink rejection,
  and trusted descriptor validation. Alternate VFS and physical power-loss behavior remain
  unverified.
- Linux non-GUI demo-provider tests passed `166 passed; 0 failed; 7 ignored` with loopback proxy
  bypassed. Native CI is authoritative for the GTK/AT-SPI, portal, mTLS, build, performance,
  checksum, and SBOM gates because this host lacks GTK4/Graphene development packages.
- Central workflow `30059904373` passed Linux and PowerShell validation for the synchronized
  coordination documents and release manifest.
- The documented clean-bootstrap flow cloned all seven public repositories in a disposable
  workspace and passed strict workspace, goal-pin, manifest, link, and credential-signature checks.
- Manifest rollback rehearsal passed with:
  `python3 tools/rehearse-release-rollback.py --component linux --target-revision
  597ccc961f9530836f8cef4c9a12a64b5c0a311c --repository ../linguamesh-linux`.
- The disposable-fixture regression `python3 tools/test-release-rollback.py` passed and is part of
  central workflow `30060144548` (Linux `89379970142`, PowerShell `89379970114`); it asserts that
  the rehearsal does not modify its manifest or repository fixture.
- Core FFI manifest synchronization commit `adab809ed7d265aac85e7cd53393d5b9ba0dfdef` passed
  coordination workflow `30060907288` (Linux `89382183919`, PowerShell `89382183959`).

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
production rollback authorization; and stable-release authorization remain open. Release status stays
`unreleased`.

## Migration and rollback

This draft changes no persisted schema or public contract. To roll back this checkpoint, restore
the previous verified Linux revision in `release-manifest.toml`, run `bash tools/check-workspace.sh`
and the central workflow, then document the resulting source and CI revisions. Do not force-push,
rewrite published history, or promote the rollback as stable without explicit authorization. The
manifest-only rehearsal verifies this transition in a temporary file; it does not authorize a
production rollback or claim physical storage recovery.

## Signing and publication status

No tag, GitHub Release, signing, notarization, or stable publication was performed. Any future
release must first satisfy every mandatory acceptance scenario and update this record together
with the manifest, compatibility table, checksums, SBOMs, and rollback evidence.
