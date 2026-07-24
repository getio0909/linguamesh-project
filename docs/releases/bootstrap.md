# Release Train bootstrap

Status: Draft

Date: 2026-07-24

This record describes the current Linux-first prerelease checkpoint. It is not a stable release
and must not be promoted without the acceptance and authorization gates listed below.

## Components and contracts

| Component | Version | Source revision |
| --- | --- | --- |
| Core | `0.1.0-alpha.2` | `01e228ca251252de331b285e5381cbb4fe0c30da` |
| Localization | `0.1.0` | `c2526bfb3f6ff57895bdc3eeed743e26c8783613` |
| Android | `0.1.0-alpha.1` | `afe7a566bac77a16243f70295d17a4d9cab1151f` |
| Windows | `0.0.0-dev` | `unreleased` |
| macOS | `0.1.0-alpha.1` | `cad822c69dcf1ad20f8cab2151f407866a577420` |
| Linux | `0.1.0-alpha.2` | `5904d2be68dee4ee8e02e137ba3c9ae9cf6568a4` |

Contracts: ABI major `1`, protocol schema `0.1.0`, provider catalog `0.1.0`, and localization
schema `1.0.0`. The authoritative pins are in `release-manifest.toml`.

## Artifact provenance and checksums

No stable artifacts are published. Core Fuzz/ASAN run `30064410428` (job `89392449201`) passed
protocol, document, bounded FFI input, FFI lifecycle, and valid loopback-command targets; Core CI
`30064410443` and Native SDK run `30064410436` passed all four platform jobs. Linux push Native,
Flatpak, and Foundation runs `30064750977`/`30064750908`/`30064750909`, plus PR runs
`30064752313`/`30064752315`/`30064752308`, generated and verified Linux checksum/SBOM evidence,
completed the GTK/portal/Wayland/Orca gates and Flatpak sandbox smoke, and passed repository
validation. These remain CI artifacts, not signed releases.

## Validation evidence

- Host-pinned Rust 1.93.0 Core check passed with `cargo check --workspace --locked --offline`.
- Core FFI ASAN smokes passed locally: valid loopback commands completed 136 time-bounded
  iterations with 10,653 coverage features, malformed-input and lifecycle targets passed 200 runs
  each, and `ffi_handles` completed 1,068 time-bounded iterations without crash or leak report.
  These fixtures use no commercial credentials and do not claim live-provider or cross-client
  coverage.
- Host-pinned Rust 1.93.0 Core storage regression passed `55 passed; 0 failed` with
  `cargo +1.93.0 test -p linguamesh-storage --locked --offline`, covering WAL replay,
  abrupt-process recovery, busy-checkpoint retry, migrations, secure deletion, symlink rejection,
  and trusted descriptor validation. Alternate VFS and physical power-loss behavior remain
  unverified.
- Linux non-GUI demo-provider tests passed `166 passed; 0 failed; 7 ignored` with loopback proxy
  bypassed. Native CI is authoritative for the GTK/AT-SPI, portal, mTLS, build, performance,
  checksum, and SBOM gates because this host lacks GTK4/Graphene development packages.
- Linux Core pin synchronization head `42efabc3746c405136f347de4206e2cc5a13dc98` passed all six
  current-head Native/Flatpak/Foundation gates listed above; the runtime/build parent is
  `449facf5aaf7fe79e0cea91ea9ec3934a9b6f8d4`.
- Central synchronization commit `a5dee2ad1f9e8039e9d9a1ad44225c5200b3362c` passed coordination
  workflow `30063863934` on Linux `89390817246` and PowerShell `89390817242`.
- Central source-pin consistency commit `d17f47a9f85fce9583167560216ef333dd426247` aligned the
  manifest and this table to Linux `42efabc3746c405136f347de4206e2cc5a13dc98`; coordination
  workflow `30065425740` passed Linux `89395294587` and PowerShell `89395294630`.
- Core `01e228ca251252de331b285e5381cbb4fe0c30da` adds the Linux-only bundled `unix-excl` VFS
  storage migrations, file/parent-path symlink, and process-crash WAL-replay regressions. Host-pinned storage tests
  passed `57 passed; 0 failed`; Core CI `30066150481`, Fuzz/ASAN `30066150469`, and Native SDK
  `30066150422` all passed. Linux `5904d2be68dee4ee8e02e137ba3c9ae9cf6568a4` passed push
  Native/Flatpak/Foundation `30067853996`/`30067853960`/`30067853957` and PR
  `30067852102`/`30067852064`/`30067852097`. This remains unsigned prerelease evidence; custom
  VFS, physical power-loss, signing, rollback, and stable-release evidence remain open.
- The current handle-lifetime manifest synchronization commit `59c9cc4d16610d18559d2bab96c1518e242c0d7e`
  passed coordination workflow `30065102174` on Linux `89394395492` and PowerShell `89394395538`.
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
- Final Core pin synchronization commit `62085d82b4aa2fe7efd3e635e1f2868c9e66bf8d` passed
  coordination workflow `30061527364` (Linux `89383965632`, PowerShell `89383965670`).
- Core valid-command pin `b29067b78d420c96f57d670d3dd860cba3abc703` passed Core CI
  `30062160464`, Fuzz/ASAN `30062160452`, and Native SDK `30062161560`. Central synchronization
  commit `b2d1ae9dc425cafd359746ef75031dce9f9a9ea2` passed coordination workflow `30062468039`
  (Linux `89386679596`, PowerShell `89386679650`).

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
