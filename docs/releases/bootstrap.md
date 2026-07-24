# Release Train bootstrap

Status: Draft

Date: 2026-07-24

This record describes the current Linux-first prerelease checkpoint. It is not a stable release
and must not be promoted without the acceptance and authorization gates listed below.

## Components and contracts

| Component | Version | Source revision |
| --- | --- | --- |
| Core | `0.1.0-alpha.2` | `9e69d01cbae1ca0421923e059aa3252c4ecbe1be` |
| Localization | `0.1.0` | `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c` |
| Android | `0.1.0-alpha.1` | `240afaeebe22dc13dea988591dbdd87aa233fc79` |
| Windows | `0.0.0-dev` | `unreleased` |
| macOS | `0.1.0-alpha.1` | `a039bcbd39c032fabb58adb389eec1e68ae9c2c6` |
| Linux | `0.1.0-alpha.2` | `e1a2ba9130a198212098e93276e5d16bdfec8e3b` |

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

- macOS head `a039bcbd39c032fabb58adb389eec1e68ae9c2c6` consumes Core
  `9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`.
  PR workflow `30101768570` rebuilt the exact XCFramework and passed generated wrapper tests,
  strict Swift concurrency, unit/integration tests, app assembly, and ad-hoc signing smoke. Device,
  accessibility, distribution signing, and notarization remain open.

- Android head `240afae` consumes Core `9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n
  `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`. Hosted workflow `30099769434` rebuilt and
  checksum-verified the AAR, then passed debug/release assembly, 19 JVM tests per variant,
  instrumentation compilation, and debug/release lint. Device, document, signing, and distribution
  evidence remain open.

- Windows code head `718ee51cdeb774f6150eb1e2a1da54a04fd219fe` (status-only descendant
  `ba1451ad91fdc58c58fdacc7731b96409cfc5fd8`) consumes Core
  `9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`.
  Hosted Native Windows `30106874477` passed pinned-Core C++ wrapper smoke, portable reference,
  WinUI Debug/Release, and unsigned MSIX preparation; Foundation `30106874484` passed. UI runtime,
  PasswordVault, accessibility, generated C++/WinRT projection, device, signing, and distribution
  evidence remain open.

- Current Linux-first storage checkpoint uses Core `9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and
  Linux status head `1407f0d`. The implementation head `e75317015e970a283f9a3d4ae47718b12e557e32`
  performs a final `-wal`/`-shm` identity check after profile hydration and before storage
  publication; the reviewed Flatpak/documentation descendant is `d3244ff017fb7178017310065f8d7708dd41a9ea`.
  The deterministic replacement regression, local Linux validation, and hosted Native/Flatpak/
  Foundation runs `30108528343`/`30108528414`/`30108528360` passed. Post-publish replacement,
  physical power loss, broader VFS variants, cross-client parity, signing, rollback, and stable
  release remain open.

- Current Linux accessibility checkpoint uses runtime/test head
  `8713bdc23b81263e1bdbc65e8d010ce57673877a` and packaging/status head
  `ec50565461b8a94311d297e054f8e6abd95fb130` (documentation-only descendant of runtime/package
  head `749ff81766d5963827110411d77bb1714eae91cc`). It preserves production `Status`/`Alert` roles,
  adds a test-only fixed invalid-UTF-8 `ROLE_LABEL` fixture, and verifies localized status/error
  prefixes through AT-SPI name, description, or Text exports. Hosted push Native/Flatpak/Foundation
  `30115826450`/`30115826498`/`30115826518` passed. Human listening/visual review, physical
  compositor/GPU, other clients, signing, rollback, and stable-release evidence remain open.

- Latest Linux keyboard traversal checkpoint uses runtime `195664199d1884c53940a4c78f2c15bd500ad8a3`
  and packaging/status head `e1a2ba9130a198212098e93276e5d16bdfec8e3b`. It includes the optional
  client-certificate identity and **Test connection** in the explicit provider Tab/Shift+Tab order.
  Hosted push/PR Native, Flatpak, and Foundation runs `30117422502`/`30117422386`/`30117422399`
  and `30117426489`/`30117426644`/`30117426431` passed. Manual accessibility, physical desktop,
  cross-client, signing, rollback, and stable-release evidence remain open.

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
  passed `57 passed; 0 failed`; Core CI `30067774797`, Fuzz/ASAN `30067774823`, and Native SDK
  `30067774805` all passed. Linux `5904d2be68dee4ee8e02e137ba3c9ae9cf6568a4` passed push
  Native/Flatpak/Foundation `30067853996`/`30067853960`/`30067853957` and PR
  `30067852102`/`30067852064`/`30067852097`. This remains unsigned prerelease evidence; custom
  VFS, physical power-loss, signing, rollback, and stable-release evidence remain open.
- Core `900b0a90113b75dd0f49e535900b9af8e75ef0f3` adds the Linux-only negative
  `unix-dotfile` VFS probe; it fails before migrations when WAL cannot be enabled and leaves no
  schema tables. Linux `4f4472ee9ef5ceef821301f4b2af71f54372174d` passes all local non-GUI
  validation. Core CI/Fuzz/ASAN/Native SDK `30069351232`/`30069351157`/`30069351240` and Linux
  push Native/Flatpak/Foundation `30069403841`/`30069403823`/`30069403845` plus PR
  `30069406482`/`30069406504`/`30069406492` all passed. Central commit
  `f79dbd2217d63c7c95b3da91367e4f77b79b68cc` passed coordination workflow `30069776643`.
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
