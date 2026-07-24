# LinguaMesh Completion Gap Analysis

Status: Linux-first prerelease audit, 2026-07-24. This document complements
`PROJECT_GOAL.md`; it does not lower any acceptance requirement.

## Latest Linux provider-form keyboard traversal completion

Linux runtime source `195664199d1884c53940a4c78f2c15bd500ad8a3` now includes the optional
client-certificate identity and the non-mutating **Test connection** action in the explicit
application-window Tab/Shift+Tab order. The keyboard probe and Xvfb fixture require both controls
without logging field contents. Final packaging/status head `e1a2ba9130a198212098e93276e5d16bdfec8e3b`
pins that runtime source in Flatpak. The initial stale-pin guards `30117215386`/`30117219370` are
superseded by final push Native/Flatpak/Foundation `30117422502`/`30117422386`/`30117422399` and
PR `30117426489`/`30117426644`/`30117426431`, all passed. Manual keyboard/accessibility review,
physical compositor/GPU coverage, other clients, signing, rollback, and stable release remain open.

## Latest Linux runtime AT-SPI status/error export fixture

Linux runtime/test head `8713bdc23b81263e1bdbc65e8d010ce57673877a` preserves production GTK
`Status`/`Alert` roles and adds a test-only fixed invalid-UTF-8 state/error fixture. Standard
`ROLE_LABEL` nodes are checked through AT-SPI name, description, or Text exports for localized
status/error prefixes without printing arbitrary content. Flatpak/release-pin head
`ec50565461b8a94311d297e054f8e6abd95fb130` is a documentation-only descendant of runtime/package
head `749ff81766d5963827110411d77bb1714eae91cc`; hosted push Native/Flatpak/Foundation
`30115826450`/`30115826498`/`30115826518` passed. Human Orca listening, visual/RTL review,
physical compositor/GPU coverage, other clients, signing, rollback, and stable release remain
open.

## Latest Linux final SQLite sidecar stability recheck

Linux implementation `e75317015e970a283f9a3d4ae47718b12e557e32` performs a final `-wal`/`-shm`
identity check after profile hydration and before storage publication. The reviewed packaging and
documentation descendant is `d3244ff017fb7178017310065f8d7708dd41a9ea`; local focused/all-feature
checks passed, and hosted Native `30108528343`, Flatpak `30108528414`, and Foundation `30108528360`
passed. Post-publish replacement, broader VFS variants, physical power loss, cross-client parity,
manual review, signing, rollback, and stable release remain open.

## Latest Linux Flatpak release-pin documentation alignment

Linux head `920c0c5439fcfe5825fd6ecbe6d57158377c583d` corrects the release guide to the exact
Flatpak source pin `af680cee7fd696d859debc896c1136ba002bda89` used by the packaging manifest.
Push/PR Native, Flatpak, and Foundation runs `30103724040`/`30103724131`/`30103723982` and
`30103720635`/`30103720724`/`30103720669` passed. This is documentation-only; physical power-loss,
manual review, cross-client conformance, signing, rollback, and stable-release evidence remain
open.

## Latest Linux contributor pin alignment

Linux head `8d9a378d34e35e14a5618ad51b4787c616b7ae70` is a documentation-only descendant of the
registered custom-VFS checkpoint and aligns contributor instructions with Core
`9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`.
Push/PR Native, Flatpak, and Foundation runs `30102784838`/`30102784832`/`30102784964` and
`30102781098`/`30102781136`/`30102781145` passed. No runtime behavior changed; physical power-loss,
manual review, cross-client conformance, signing, rollback, and stable-release evidence remain
open.

## Latest macOS Core checkpoint

macOS head `a039bcbd39c032fabb58adb389eec1e68ae9c2c6` consumes Core
`9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`.
PR workflow `30101768570` rebuilt and verified the exact XCFramework, generated wrapper tests,
strict Swift concurrency, unit/integration tests, app assembly, and ad-hoc signing smoke. Device
accessibility, profile persistence, documents, distribution signing, rollback, cross-client
conformance, and stable-release evidence remain open.

## Latest Android checkpoint

Android head `240afae` consumes Core `9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n
`7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`. Hosted workflow `30099769434` rebuilt and verified
the exact Core AAR, then passed debug/release assembly, 19 JVM tests per variant, instrumentation
compilation, and debug/release lint. The typed ABI-1 host-secret gateway is compatible with the
Linux-only Core VFS descendant. Device execution, Core-owned persistence, document/background
workflows, signing, rollback, cross-client conformance, and stable release remain open.

## Latest macOS checkpoint

macOS head `75b5bfe` consumes Core `b39dbdc2877a60c6666697cc0817f31225496cb2` and implements
the ABI-1 typed host-secret exchange: a session-only `secret_ref` is carried in the translation
command, a matching `secret_required` event is resolved through Keychain, and exactly one bounded
response is sent through the generated Apple wrapper. Hosted macOS run `30095987188` passed Core
XCFramework generation, strict Swift 6 concurrency, all 20 XCTest cases (including the credentialed
loopback path), app assembly, and ad-hoc signing smoke. The superseded initialization failure
`30095764844` is corrected in `c528bfc`. Local Swift/Xcode and manual accessibility evidence remain
unavailable; generated typed Swift protocol projections, profile persistence, distribution signing,
cross-client conformance, and stable-release evidence remain open.

## Latest Android checkpoint

Android head `ab81a9b8b7c416c54e543968ef50723c8df0ee7b` consumes Core
`b39dbdc2877a60c6666697cc0817f31225496cb2` and adds typed host-secret transport: the release
gateway passes the opaque profile `secretRef`, consumes `SecretRequired`, validates the reference,
resolves one-shot Keystore bytes, sends bounded typed responses, and clears resolved byte arrays.
Core wrapper and Android local non-native checks passed; the local AAR rebuild is blocked by an
incomplete NDK installation. Hosted run `30094317628` passed clean Core AAR provenance, debug and
release builds, 19 JVM tests per variant, instrumentation compilation, and debug/release lint;
the superseded typed-event compile failure `30093907047` is recorded as corrected. Core-owned
persistence, device restoration, document/background workflows, device Keystore execution,
signing, and stable release remain open. Central coordination workflow `30094924852` passed its
Linux and PowerShell jobs for the preceding Android synchronization.

### Prior Android metadata checkpoint

Android code head `535e4485ff555b04702c0390ca76428ff995d457` adds bounded DataStore persistence for
non-secret provider-profile metadata, background restore and Core re-registration, active-profile
selection persistence, and JVM coverage. Local Foundation, l10n sync, debug/release builds, 18
debug/release JVM tests, instrumentation compilation, and debug/release lint passed. Status head
`8e0b898` records the final status after hosted run `30092613918` passed the bounded-write
follow-up; the earlier status head `4b2093bc94b8016c5eca721a18b5f049ac7330d8` records hosted run
`30091714901` as passed. The superseded stale-pin run `30091670253`
failed before build execution. Core-owned persistence,
device restoration, document and background workflows, real-provider credentials, signing, and
stable release remain open. Central coordination workflow `30092269717` passed the synchronized
manifest, compatibility, documentation, and credential-scan checks.

## Latest Windows checkpoint

Windows code head `718ee51cdeb774f6150eb1e2a1da54a04fd219fe` (status-only descendant
`ba1451ad91fdc58c58fdacc7731b96409cfc5fd8`) consumes Core
`9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n `7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`.
Local Foundation/source-boundary, CMake Release, and CTest (1/1) checks passed. Hosted Native
Windows `30106874477` passed immutable-Core C++ wrapper smoke, portable C++, WinUI Debug/Release,
and unsigned MSIX preparation; Foundation `30106874484` passed. Windows UI runtime, UI
automation, PasswordVault integration, accessibility, generated C++/WinRT projection, device,
signing, rollback, full client capabilities, and cross-client parity remain open. Release remains
`unreleased`.

## Latest Linux/Core checkpoint

### Linux registered custom VFS compatibility probe

Linux head `402b97ac50bf62e89f9c27caedebff10d2ae7b8c` consumes Core
`9e69d01cbae1ca0421923e059aa3252c4ecbe1be` and l10n
`7fd210692bb269ef52f7453bfeb2b0f0759b1d4c`. Core's Linux storage regression registers a distinct
test VFS name over the validated `unix-excl` callbacks, runs schema migration and provider-profile
persistence/reopen through that name, and rechecks the symlink/no-follow rejection. Core
CI/Fuzz/ASAN/Native SDK `30097756099`/`30097756186`/`30097756137` and Linux push/PR Native,
Flatpak, and Foundation `30098393451`/`30098393429`/`30098393452` and
`30098395935`/`30098395913`/`30098395889` all passed. The probe is deterministic
registration/callback evidence only; arbitrary third-party VFS implementations and physical
power-loss recovery remain open, as do cross-client parity, manual review, signing, rollback, and
stable release.

### Linux CI evidence documentation head

Linux status head `26c88b026a9cf0de1ab585de979a0e2576df805c` is documentation-only after corrected
Core pin head `dfe30a2618311a820451a4748e2acff49ffd2b93` passed push/PR Native, Flatpak, and Foundation
runs `30078310878`/`30078310868`/`30078310871` and `30078307212`/`30078307159`/`30078307167`.
Its own push runs `30078731326`/`30078731415`/`30078731405` and PR runs
`30078727061`/`30078727008`/`30078727028` also all passed. Release remains `unreleased`.

### Linux Native CI Core pin alignment

Linux head `dfe30a2618311a820451a4748e2acff49ffd2b93` corrects `.github/workflows/native.yml` to
check out approved Core `77c6bf426ace65c6bd960120b253e10e59a70a13`, matching Flatpak, documentation,
and the release manifest instead of stale `b29067…`. Local commit-existence, diff, and Flatpak
metadata checks passed. Corrected push runs are Native `30078310878`, Flatpak `30078310868`, and
Foundation `30078310871`; corrected PR runs are Native `30078307212`, Flatpak `30078307159`, and
Foundation `30078307167`. Native remains in hosted dependency installation, so the corrected
checkout is not yet fully hosted-verified; release remains `unreleased`.

### Linux persisted document-job metadata deletion

Linux status head `7d0970cc90a9170f6be59b2e75bad672e5ace0bf` adds a Core-backed worker delete
command/event and a localized GTK confirmation for persisted document-job metadata and segment rows.
Deletion is rejected while document work is active and successful deletion clears only the selected
job association, leaving editor source/output buffers intact. Local localization, Flatpak, format,
check, strict Clippy, no-default (`85 passed; 1 ignored`), demo-provider (`166 passed; 7 ignored`),
build, and cargo-deny checks passed. Push Native/Flatpak/Foundation and PR Flatpak/Foundation runs
`30077159723`/`30077159767`/`30077159771` and `30077157438`/`30077157429` passed; docs-only PR
Native `30077157435` remains in progress at hosted dependency installation, while code-head PR
Native `30076649572` passed the exact GTK matrix. PR #1 remains Draft/Open/mergeable and Issue #1 remains Open. Cross-client,
physical/manual, custom-VFS/power-loss, signing, rollback, and stable-release gates remain open;
release status stays `unreleased`.

### Explicit source-locale prompt and Linux pin

Core `77c6bf426ace65c6bd960120b253e10e59a70a13` now forwards an optional explicit source locale
as a bounded English hint to every built-in provider adapter, while omitted source locale remains
auto-detect. Prompt and translation-memory identity are v3. Linux
`b8bbfa865a0a9c1199c88ad88c15e9a3d490e5a2` updates report metadata and the Flatpak source pin.
Core local fmt/check/strict-Clippy/tests/build/cargo-deny and Linux localization, metadata,
formatting, check, Clippy, no-default (`85 passed; 1 ignored`), and demo-provider
(`166 passed; 7 ignored`) validation passed. Core CI/Fuzz/Native SDK
`30073841816`/`30073841796`/`30073841790` and Linux push/PR Native, Flatpak, and Foundation
`30074447292`/`30074447281`/`30074447301` and `30074449163`/`30074449164`/`30074449176`
passed. PR #1 remains Draft/Open/mergeable with no reviews; Issue #1 remains Open. Cross-client,
live-provider, custom-VFS/power-loss, manual/physical, signing, rollback, and stable-release
evidence remain gaps, so the release stays `unreleased`. Final evidence comments are Linux
`5067323802` and central `5067324171`; central coordination workflow `30075645168` passed with
Linux job `89425665916` and PowerShell job `89425665987`.

### Core ABI status reconciliation

Core `3397eafb4a4a23cfbedb8d0b0c8b086dd34f5d6a` corrects a stale status entry without changing
runtime or dependency pins. The current ABI file-lease and bounded FFI sanitizer/fuzz surfaces are
implemented and covered by local tests and passing Core CI `30072627363`, Fuzz/ASAN `30072627365`,
and Native SDK `30072627332` across Linux, Android, Apple, and Windows. Linux remains pinned
to Core `f5b818c3598d78e7cac30604577fa8057d380737`. Generated platform projections, distribution
artifacts, cross-client conformance, manual/physical review, signing, rollback, and stable-release
evidence remain gaps, so release status stays `unreleased`.

### Final Linux PR and Issue audit

Linux PR #1 remains Draft/Open and mergeable at head `4612827d0ce78b9629fbbc24853677e18ee9d0a1`;
all six current push/PR Native, Flatpak, and Foundation checks passed, with zero submitted reviews
and no unresolved review threads. Central Issue #1 remains Open with no external review feedback;
the final evidence comments are Linux `5066899799` and central `5066899925`. A current source and
status audit found no additional deterministic Linux implementation slice within the authorized
Linux-first scope. The remaining gaps are therefore cross-client, physical/manual, custom-VFS and
power-loss, signing, rollback, and stable-release evidence; the release remains `unreleased`.

The current host revalidation for Linux `b8bbfa865a0a9c1199c88ad88c15e9a3d490e5a2` and Core
`77c6bf426ace65c6bd960120b253e10e59a70a13` passed localization, Flatpak metadata, formatting,
locked checks, strict Clippy, cargo-deny, no-default tests (`85 passed; 1 ignored`), and
demo-provider tests (`166 passed; 7 ignored`) plus the demo-provider build. Core storage has no
source diff from the pinned runtime. Native GTK display execution remains CI-backed because the
host lacks GTK development headers; this does not close the manual, physical, cross-client,
signing, rollback, or stable-release gaps.

Assumption: Core `f5b818c3598d78e7cac30604577fa8057d380737` preserves ABI 1 and Linux application
contracts while rejecting the bundled non-locking `unix-none` VFS before migrations; Linux
`4612827d0ce78b9629fbbc24853677e18ee9d0a1` is a documentation/status-only descendant.

The focused Core regression rejects the unsupported VFS with a persistence error and leaves zero
SQLite schema tables. Core local storage reports `59 passed; 0 failed`; full fmt, check, strict
Clippy, workspace tests, build, and cargo-deny pass. Core CI/Fuzz/ASAN/Native SDK
`30070685571`/`30070685557`/`30070685594` pass. Linux local localization, Flatpak, formatting,
locked checks, Clippy, no-default (`85 passed; 1 ignored`), and demo-provider (`166 passed; 7
ignored`) validation pass; push/PR Native, Flatpak, and Foundation runs
`30071367773`/`30071367788`/`30071367816` and `30071369693`/`30071369679`/`30071369672` pass.
Central manifest/docs commit `d9d13945d59370a8bc0ca576a66c8b3fa5fd9468` passed coordination
workflow `30071892709` with Linux `89414323628` and PowerShell `89414323574`.
Custom/third-party VFS, physical power-loss, cross-client, live-provider, human/physical, signing,
rollback, and stable-release evidence remain open; release stays `unreleased`.

## Core CLI acceptance revalidation

The pinned Core CLI now has a fresh credential-free smoke record: the loopback fake provider
discovered and selected `fake-translator`, streamed `你好，LinguaMesh！`, and completed. A second
run selected `fake-slow-translator`, retained the first delta `你好`, and cancelled at the 320 ms
deadline with the required terminal cancellation result. This strengthens Scenario 1 only; the
cross-client, manual/physical, power-loss, signing, rollback, and stable-release boundaries remain
open.

The current-tree revalidation passed without changing source or dependency pins: Core's pinned
Rust 1.93.0 fmt/check/strict-Clippy/workspace-test set is green, and Linux's localization audits,
Flatpak metadata, formatting, all-target check, strict Clippy, no-default suite (`85 passed; 1
ignored`), and demo-provider suite (`166 passed; 7 ignored`) are green. This confirms the existing
Linux-first evidence but does not close custom/third-party VFS, physical power-loss, cross-client,
live-provider, human/physical, signing, rollback, or stable-release boundaries.

The Linux-first alternate-VFS checkpoint is now verified at Core
`900b0a90113b75dd0f49e535900b9af8e75ef0f3` and Linux
`4f4472ee9ef5ceef821301f4b2af71f54372174d`. Core's Linux-only storage regressions exercise the
bundled SQLite `unix-excl` VFS with `SQLITE_OPEN_NOFOLLOW`, schema/WAL/profile reopen behavior,
process-crash WAL replay, and file/parent-path symbolic-link rejection. Core CI `30069351232`, Fuzz/ASAN
`30069351157`, Native SDK `30069351240`, and all six Linux push/PR Native, Flatpak, and Foundation
gates passed (`30069403841`/`30069403823`/`30069403845` and
`30069406482`/`30069406504`/`30069406492`). The bundled `unix-dotfile` VFS is also probed and
rejected before migrations when it cannot provide required WAL, with no schema tables created;
Core does not silently downgrade durability. Central coordination commit
Central commit `f79dbd2217d63c7c95b3da91367e4f77b79b68cc` passed coordination workflow
`30069776643`. This closes only the tested bundled `unix-excl` path; custom/third-party VFS,
physical power-loss, cross-client, signing, rollback, and stable-release evidence remain open.

Core ABI 1 handle-lifetime hardening is now verified at Core
`b54ab4ab7ebcd3a439678ead9c0af1e6b5c5dae8` and Linux `42efabc3746c405136f347de4206e2cc5a13dc98`.
The registry uses monotonic opaque tokens and `Arc` state references, so stale, forged, repeated,
and concurrent-destroy calls fail closed without dereferencing freed memory. Core Fuzz/ASAN
`30064410428` (job `89392449201`), CI `30064410443`, Native SDK `30064410436`, and Linux push/PR
Native, Flatpak, and Foundation runs all passed. This closes the arbitrary raw-engine-pointer
use-after-free gap for the covered ABI entry points; cross-client worker coordination, live
providers, human/physical review, signing, rollback authorization, and stable release remain open.

Assumption: Linux is the active implementation scope for the current checkpoint, while
Android, Windows, and macOS evidence must still be completed before a stable release.

Core commit `b29067b78d420c96f57d670d3dd860cba3abc703` adds a valid-command `ffi_commands` fuzz
target backed by the loopback `FakeProviderServer`. Local pinned-nightly smoke completed 136
time-bounded iterations with 10,653 coverage features and a 49-file corpus; the existing FFI input
and lifecycle targets passed 200 iterations each. Core CI `30062160464`, Fuzz/ASAN `30062160452`,
and Native SDK `30062161560` all passed, including Linux `89385808651`. This closes only the
bounded loopback command path; raw-pointer use-after-free, live providers, cross-client parity,
physical/alternate-VFS recovery, signing, rollback authorization, and stable release remain open.
Central pin synchronization commit `b2d1ae9dc425cafd359746ef75031dce9f9a9ea2` passed coordination
workflow `30062468039` on Linux `89386679596` and PowerShell `89386679650`.

Linux Core pin synchronization is now recorded at runtime/build head
`449facf5aaf7fe79e0cea91ea9ec3934a9b6f8d4` and final evidence head
`4b592e7f7b1e60545d5539a40a9a33edd9b86a09`. Core `b29067b…` and l10n `c2526b…` are consumed
immutably; local Linux non-GUI checks passed with 166 demo-provider tests and 7 environment-gated
ignores, while the host GTK development-package blocker remains explicit. Push and PR Native,
Flatpak, and Foundation runs `30063415446`/`30063415485`/`30063415440` and
`30063417561`/`30063417542`/`30063417551` all passed, including GTK/portal/Wayland/Orca,
Flatpak sandbox, checksum, SBOM, and performance evidence. This is prerelease compatibility and
provenance evidence only; the release remains `unreleased`.
Central synchronization commit `a5dee2ad1f9e8039e9d9a1ad44225c5200b3362c` passed workflow
`30063863934` on Linux `89390817246` and PowerShell `89390817242`.

The later central source-pin consistency follow-up aligns `release-manifest.toml` and the Draft
release record to current Linux head `42efabc3746c405136f347de4206e2cc5a13dc98` rather than the
historical status-only head `4b592e7f7b1e60545d5539a40a9a33edd9b86a09`. Local workspace validation
and `git diff --check` passed; central commit `d17f47a9f85fce9583167560216ef333dd426247` passed
coordination workflow `30065425740` on Linux `89395294587` and PowerShell `89395294630`. The
release remains `unreleased`.

Core commit `5e22931d5772231b0a8183cbf05ba0cbda0dfebf` adds bounded C ABI `ffi_inputs` and
`ffi_sequences` libFuzzer targets. Local pinned-nightly ASAN smokes passed 200 runs with 299 and
2,326 coverage features and 29- and 47-file minimized corpora; Core CI `30061241968`, Fuzz/ASAN
`30061241972` (job `89383142786`), and Native SDK `30061241961` (Windows `89383142743`, Android
`89383142706`, Apple `89383142744`, Linux `89383142774`) passed. This covers malformed/unsupported
inputs and safe lifecycle/control sequences only; valid commands, arbitrary raw-engine-pointer
use-after-free, physical/alternate-VFS recovery, signing, rollback authorization, and stable release
remain open.

The host-pinned Rust 1.93.0 storage regression `cargo +1.93.0 test -p linguamesh-storage --locked
--offline` passed 55 tests with 0 failures. It provides deterministic default-Unix-VFS evidence
for WAL replay, abrupt process recovery, busy checkpoint retry, migrations, secure deletion,
symlink rejection, and trusted descriptor validation. Alternate SQLite VFS enforcement and
physical power-loss behavior remain unverified and are still release blockers.

The 2026-07-24 disposable Debian trixie checkpoint expands local Linux evidence without changing
release posture. Under a non-root Xvfb/DBus session, the locked suite passed with library
`168 passed; 0 failed; 16 ignored` and binary `30 passed; 0 failed; 21 ignored`; all 18 dedicated
ignored GTK lifecycle fixtures passed. Notification transport and dunst delivery, file chooser,
drag-and-drop, English/Arabic keyboard focus, headless Wayland, OCR, four mTLS cases, Secret
Service prompt/persistence, performance baseline, and debug/optimized builds passed. The
container used Rust 1.93.1 rather than the pinned 1.93.0 and mounted source read-only with named
cache volumes, so this is bounded supplementary evidence.

The follow-up privileged-container run passed the document-portal lease and storage-fault fixtures
with `/dev/fuse`, `SYS_ADMIN`, and AppArmor isolation explicitly granted. The Ubuntu 24.04 runtime
container also passed the live AT-SPI inspector against the actual Linux binary for English,
Simplified Chinese, Arabic, `en-XA`, and `ar-XB`. The earlier Debian trixie `label`-role mismatch
is a bridge-version difference, not a product failure; the inspected binary came from the
disposable Rust 1.93.1 build cache rather than the pinned 1.93.0 toolchain. The unexpired Flatpak
bundle from Native run `30052187036` for Linux head `597ccc961f9530836f8cef4c9a12a64b5c0a311c`
passed sandbox smoke on GNOME runtime `org.gnome.Platform/x86_64/49`; its checksum matched
`a01177a9a1a3d84ac8e3de0cc509305f71494307134281ce42882a0e40e2dc02`, and its SPDX 2.3 SBOM parsed
with 234 packages. These remaining boundaries do not justify a stable-release claim, and
human/physical review, live providers, other clients, signing, rollback, and release authorization
remain open.

The pinned third-party Ollama fixture was also re-run with `ollama/ollama:0.11.10` and
`smollm:135m`; the worker test now uses a dedicated 30-second deadline for cold model startup.
The exact ignored worker test passed `1 passed; 0 failed` without a credential after download, and
the result makes no cold-start performance claim.

An exact Rust 1.93.0 Linux build was attempted in a disposable container, but Rustup timed out
fetching `channel-rust-1.93.0.toml.sha256` from both the official distribution endpoint and the
configured Tuna mirror. The host-pinned toolchain was then used after removing only generated
target caches: Core `cargo check --workspace --locked --offline` passed and Linux's non-GUI
demo-provider suite passed `166 passed; 0 failed; 7 ignored` with loopback proxy bypassed. The
host GUI check remains unavailable because `gtk4` and `graphene-gobject-1.0` packages are absent;
Native CI remains authoritative for display-backed validation.

Linux worker commit `c03c7e2065c1a0f74f6326d9e5071ee3cbde6299` and Flatpak source-pin commit
`1c513e2e52236fce03a60548dbcab242c6878bed` passed Native `30058395686`, Flatpak `30058395689`,
and Foundation `30058395669`. The Native gate completed all GTK, accessibility, portal, mTLS,
build, performance, checksum, and SBOM steps; Flatpak completed its sandbox smoke.

The central release manifest now points `[components.linux].source_revision` at the same verified
Linux head `1c513e2e52236fce03a60548dbcab242c6878bed`; central commit
`ae9dcee854dc74af0cf8414850145de39be11057` passed coordination workflow `30059016853` on Linux
and PowerShell. This synchronization does not change the `unreleased` posture.

The Draft release-train record `docs/releases/bootstrap.md` now captures the same component pins,
contract versions, CI provenance, unsigned-artifact status, known limitations, and manifest-only
rollback procedure. It is documentation evidence only; it does not close the stable-release gate.

Scenario 19 was rerun from a temporary shallow clone of central `main`: the bootstrap script cloned
all seven public canonical repositories and passed strict workspace, goal-pin, manifest, link, and
credential-signature validation. This strengthens clean-bootstrap evidence without changing the
existing checkouts or claiming unsupported platform builds.

The manifest-only rollback rehearsal `tools/rehearse-release-rollback.py` passed for the Linux pin
transition from `1c513e2e52236fce03a60548dbcab242c6878bed` to previously verified
`597ccc961f9530836f8cef4c9a12a64b5c0a311c`. It verified target commit existence, isolated the
single revision change in a temporary parsed manifest, preserved `unreleased`, and made no checkout
changes. This does not cover physical VFS/power-loss behavior, signed artifacts, or production
rollback authorization.

The new `tools/test-release-rollback.py` regression also passed with Python 3.13. It creates a
temporary Git repository and asserts that the rehearsal leaves both the manifest and repository
files unchanged; central workflow `30060144548` passed Linux `89379970142` and PowerShell
`89379970114` with this regression enabled. This strengthens the manifest-only invariant but does
not close production rollback authorization or physical and alternate-VFS gaps.

The 2026-07-23 GitHub triage refresh confirms Linux PR #1 and macOS PR #1 are both Draft/Open and
mergeable with their current checks successful, and neither has submitted reviews or unresolved
inline threads. macOS Native `29765906044` and Foundation `29765906715`/`29765904969` passed;
Linux's current six push/PR gates also passed. Triage comments were recorded on the macOS PR and
central Issue #1. No merge or stable promotion is authorized; Linux remains the active priority and
the release stays `unreleased` while cross-client, human, signing, rollback, and stable-release
boundaries remain open.

The latest Linux automation audit re-ran the four mTLS cases, the 166-test library suite, all
localization/Clippy/Flatpak/workspace checks, and the Secret Service prompt/persistence fixtures
successfully. Display-backed Secret Service execution remains host-limited by missing `xvfb-run`,
and the document portal cannot mount its FUSE path under this unprivileged session. The available
GNOME SDK image lacks Rust/Cargo, so it is not a drop-in replacement for the pinned build. These
are recorded as unavailable evidence; no deterministic Linux implementation gap was inferred and
no stable-release claim was made.

The latest Linux-first mTLS client-authentication checkpoint adds runtime/test
`7513d983011fdd81374cfb879b23647aef388f7e`, source-pin `deffb80df01cb9f6c76a8b46e0ad725080e07ea6`,
and final status head `597ccc961f9530836f8cef4c9a12a64b5c0a311c`. A temporary endpoint with a
different client-CA trust chain rejects the session-only identity at the TLS handshake, while
the trusted endpoint succeeds; the unrelated server CA and wrong-SAN cases remain covered, with
no secret-name leakage. All four exact local runners pass once, and final status-head push/PR
Native, Flatpak, and Foundation runs `30052187039`/`30052187036`/`30052187043` and
`30052189474`/`30052189521`/`30052189488` all pass. Enterprise-provider interoperability, human
review, cross-client parity, signing, rollback, and stable authorization remain open.

The latest Linux-first mTLS hostname checkpoint adds runtime/test `ec6c9971e0271e5eddc89bdc64121761a9cb46df`,
source-pin commit `9fc633feeca328b356b8f98eead03e29d28d0d46`, and final status head
`1629547c0eca1a5aabcd06cb7a96ecdfeaf97e80`. The fixture proves that a session-only client
certificate reaches a trusted endpoint, that an unrelated-CA endpoint is rejected, and that a
wrong-SAN endpoint is rejected even when its signing CA is trusted; no secret name is exposed.
Local runners pass once for all three cases, and final status-head push/PR Native, Flatpak, and
Foundation runs `30050789607`/`30050789609`/`30050789567` and `30050792424`/`30050792455`/
`30050792453` all pass. Enterprise-provider interoperability, human review, cross-client parity,
signing, rollback, and stable authorization remain open.

The latest Linux-first mTLS checkpoint adds runtime/test `896cd2352aef73a86ca80d7d92e2b5c7850af7d7`,
source-pin commit `cb6a3b166344c240c135a829ef32d14e6b5214e6`, and final status head
`6113f4898a3d81fedd103b413d739797238c8490`. The fixture proves that the session-only client
certificate reaches a trusted endpoint and that the configured trust bundle rejects an endpoint
signed by an unrelated CA, without exposing the secret name. Local positive and negative runners
each pass once, and final status-head push/PR Native, Flatpak, and Foundation runs
`30049361416`/`30049361411`/`30049361698` and `30049363915`/`30049363922`/`30049363912` all pass.
Enterprise-provider interoperability, human review, cross-client parity, signing, rollback, and
stable authorization remain open.

The latest Linux-first client-certificate HTTPS checkpoint adds runtime/test
`4b5a3f2ec0e65060d104068be6a6f31446007ee4`, packaging/docs `7b69933e1b0b92e1ee2136e01b6d39fa765ec761`,
certificate hardening `e9406d56e1345be765c01ecfe2600e8e0d10dde9`, and final status head
`14b601ae1ac11e98e09a4d2727f6ebb584f32ad4`. A temporary Python HTTPS endpoint requires a client
certificate and serves `/v1/models`; the Linux worker supplies the session-only identity and bounded
trust bundle. The exact local fixture runner passes, and push Native/Flatpak/Foundation
`30047564119`/`30047564124`/`30047564131` plus PR `30047567575`/`30047567392`/`30047567456` all pass.
This is bounded rustls and server-side client-authentication evidence: enterprise-provider
interoperability, human review, cross-client parity, signing, rollback, and stable authorization
remain open.

The latest Linux-first proxy-secret checkpoint adds runtime test
`911994eb3f4c364af3ea043b783f2aff18e09888`, packaging/docs `968b5c88cdda64ae69a2c80add729bb37ca7548b`,
and final status head `f78d0939dd78c1646da4f7e3fa7f87665a534bf5`. A worker-level loopback proxy
fixture verifies the absolute provider request, exact Basic authorization value, and successful
model response while the profile contains only a session SecretRef. Local checks pass; push
Native/Flatpak/Foundation `30045229527`/`30045229529`/`30045229541` and PR
`30045232877`/`30045232887`/`30045232885` all pass. Live proxy deployment, provider accounts,
interactive prompts, human review, cross-client parity, signing, rollback, and stable authorization
remain open.

The latest Linux-first secret-boundary checkpoint adds runtime tests
`f0a65c0d7bd1ddfda6e531db1b93c6be0096d491`, packaging/docs `dcd3f49620b427d460c98082acaf97498f2b98ff`,
and final status head `4cfa3fa8cfa29f5dc036e53bafa388444b8de94e`. Session-only proxy-authentication
and client-certificate identity canaries reach Core validation and are absent from surfaced
diagnostics. Local checks pass; push Native/Flatpak/Foundation `30043522421`/`30043522574`/
`30043521477` and PR `30043524643`/`30043524550`/`30043524574` all pass. Live proxy/certificate
interoperability, interactive prompts, human review, cross-client parity, signing, rollback, and
stable authorization remain open.

The latest Linux-first Secret Service persistence checkpoint adds runtime test
`bb6bc5bef572eb19d7c066e24a2d48546bf4fb08`, packaging/docs `9dc863eeb9fc5825c7354863c59bb21bf4447381`,
and final status head `2c3212c562eb8d425ee302a329f77ed7821a3231`. The worker filter now proves that
persistent primary, secret-header, proxy-auth, and client-certificate SecretRefs survive profile
persistence while all three session-only refs are removed before SQLite. Local checks pass; push
Native/Flatpak/Foundation `30041197129`/`30041196965`/`30041196986` and PR
`30041200604`/`30041200579`/`30041200581` all pass, with Native completing the real GTK Secret
Service integration fixture. This strengthens unreleased Linux secure-onboarding evidence;
interactive prompts, human review, cross-client parity, signing, rollback, and stable
authorization remain open.

The latest Linux-first Secret Service checkpoint adds runtime test
`f6cdb44dd6e411c2fab1c9f39cd3cd63361a1352`, packaging/docs `d1e7368edcf8426d3986165fc5b2adbd33cabe48`,
and final status head `e9b7d80e3ecac045eeb10b37ea59871c0ada6198`. The GTK Remember/clear-form
fixture enters bounded secret custom-header JSON, verifies a second persistent SecretRef and
active-profile restoration, clears both sensitive fields, scans SQLite artifacts for both canaries,
and deletes both Secret Service items. Local checks pass; push Native/Flatpak/Foundation
`30039406785`/`30039406821`/`30039406753` and PR `30039409345`/`30039409381`/`30039409339` all
pass, with Native explicitly completing the real GTK Secret Service integration fixture. This
strengthens unreleased Linux secure-onboarding evidence; interactive prompts, human review,
cross-client parity, signing, rollback, and stable authorization remain open.

The latest Linux-first export checkpoint adds runtime/test commit
`361ac7ba9d6a18c26de4487ab424d6500fbbeafd` and packaging/status head
`71b6fa34d536ec5753160ad270b507bd9fffa518`. A serialized GTK child-process fixture is killed
after its same-directory temporary file is synchronized and before final move; the final
destination remains absent while the durable temporary bytes remain intact. Local checks pass,
and final status-head push Native/Flatpak/Foundation `30037853956`/`30037853881`/`30037853988` plus PR
`30037855907`/`30037855888`/`30037855890` all pass, with Native explicitly completing the new
fixture. This remains bounded process/crash-durability evidence: physical power-loss recovery,
alternate VFS behavior, other clients, human review, signing, rollback, and stable authorization
remain open.

The current Linux-first local-export durability checkpoint adds runtime `cf4246c24e087de870adae4878379512cbaf2b8a`
and packaging/documentation head `9085ed2f8a3acf39f24930ca2dcf98567427c80f`. Local filesystem
exports sync temporary file bytes before the non-overwriting move and sync the destination
directory afterward; failures surface as save errors. Local formatting, locked compile, strict
Clippy, 163 demo-provider tests (three documented ignores), localization, synchronization,
Flatpak metadata, and diff checks pass. Push Native/Flatpak/Foundation `30032394587`/
`30032394653`/`30032394626` and PR `30032396787`/`30032396790`/`30032396829` pass. This is
bounded crash-durability evidence only: physical power-loss recovery, alternate VFS behavior,
other clients, human review, signing, rollback, and stable authorization remain open.
The canonical localization input is `c2526bfb3f6ff57895bdc3eeed743e26c8783613`, matching Linux's
checked synchronization script and generated resources; no new l10n strings were needed here.

The follow-up Linux export regression adds direct file/parent-directory sync coverage at
`3a84352410271ce53f01cfed162d83aad8c33719`; runtime remains `cf4246c24e087de870adae4878379512cbaf2b8a`,
docs/packaging is `8dc86c50ddd5a03fe223a9eaaa5f2a9326e1175b`, and final status is
`d52ab2f7bd339f360a26497d5a42bb7184b742e9`. Push Native/Flatpak/Foundation
`30034083462`/`30034083390`/`30034083610` and PR
`30034086699`/`30034087655`/`30034086738` passed. This remains bounded local-filesystem evidence;
physical power-loss recovery, alternate VFS behavior, other clients, human review, signing,
rollback, and stable authorization remain open.

The Linux candidate-management reconciliation is now documented at status/docs head
`e13d6804b7ce17edb1490c5dc6629b9664d6c3b7`. Existing editor commits
`c0cdee8b729a6800904f67535430221feb55f78e` and `a4dd4aa644335a3b6539db4d40473423c6292c71`
provide drag ordering and same-ID edit/save; serialized GTK test
`5c49a3a18c448542bc9cf055cd81b4a0b5f01e15` covers accessible controls, Manual single-candidate
normalization, Ordered/Automatic chain persistence, and Use lifecycle. Worker fallback-chain and
one-shot approval are covered by `0e2ae25c321cef243275d1322f2b8271f0602d06` and
`af200122e4862f6230d89268f5292f16438449bb`. Push Native/Flatpak/Foundation
`30035253038`/`30035253264`/`30035253013` and PR
`30035256459`/`30035256435`/`30035256652` passed. Visual/translated-copy/Orca review,
cross-client parity, signing, rollback, and stable authorization remain open.

The current Linux-first language-swap checkpoint adds Linux code
`4e5a94feef09bbe382a0b6690dc8e8f7b138656f`, packaging/docs head
`6a9adf472c6ca7afb26311dd0bbe06de2a0f1c05`, and localization
`c2526bfb3f6ff57895bdc3eeed743e26c8783613` (506 messages): the localized, focusable Swap languages
control exchanges only the supported English/Chinese selector pair locally, preserves editor
contents, and remains disabled for Auto-source or Japanese-target combinations. Local Linux/l10n
checks pass. PR #1 Native/Flatpak/Foundation runs `30030245422`/`30030245461`/`30030245538` passed;
push Native/Flatpak/Foundation `30030243332`/`30030242763`/`30030242764` all passed. The PR stays
Draft/Open and Issue #1 stays Open; human visual/Orca review, cross-client
parity, signing, rollback, and stable authorization remain open.

The current Linux-first text workspace checkpoint adds Linux code `38275fd96f0b9ed00b7d3269974780fd61874936`,
packaging/workflow head `54b9a29b6a72db38ae8eabcb91e1cf98dd73ecab`, and l10n
`99e0e04d200a03b2de79a8dd4a8d018847519ea2` (504 messages): the localized, focusable Clear workspace
action removes source/output text, request diagnostics, transient notices, and file URIs locally
without a worker command, while preserving provider, locale, glossary, and history settings. The
reducer and GTK regressions pass locally; current-head Linux push/PR Native, Flatpak, and Foundation
gates `30027666940`/`30027665976`/`30027665616` and `30027667935`/`30027667025`/`30027666925` passed.
The PR remains Draft/Open and Issue #1 remains Open; visual/Orca review, cross-client parity, signing,
rollback, and stable authorization remain open.

The current Linux-first clipboard checkpoint adds Linux `e56e56bec0bcea9fe963ca326e3918da54f50790`
and l10n `0ee87720a8613d3dc130dfb379ab4dc7bc1e1f62` (502 messages): completed output has an explicit
localized GTK Copy translation action, empty output keeps the action disabled, and a headless GTK
regression reads the copied text back through the display clipboard. Clipboard contents never enter
Core persistence, diagnostics, or notifications. Local Linux/l10n checks pass; current-head Linux
push Native/Flatpak/Foundation runs `30024453944`/`30024454262`/`30024454369` and PR
Native/Flatpak/Foundation runs `30024457039`/`30024457175`/`30024457027` all passed for the
documentation/Flatpak pin head `89f0f2d4fe9f748f34ea388daf91c52228b92b74`. Cross-client parity,
human review, signing, rollback, and stable authorization remain open. Central manifest/document
coordination commit `555c83e00b5556101d95465771c23617cb909192` passed workflow `30025928902` on
Linux and PowerShell.

The current Linux-first provider error checkpoint adds Core `8623b2c8829e4d9cf7299c74440dcfabb4e320db`,
l10n `630a8f36d96be358d81b72e2efc87cd527e66974`, and Linux `a7ac73d6fe8707519dd02698c26ebf8ca78a4246`:
HTTP 429 responses normalize to `RateLimited`, bounded `Retry-After` hints survive the provider
boundary, and Linux renders localized plural retry guidance. Local Core/Linux/l10n checks pass;
current-head Push Native/Flatpak/Foundation runs `30022122318`/`30022122787`/`30022122379` and PR
Native/Flatpak/Foundation runs `30022125925`/`30022125926`/`30022126939` all passed. Live quota
behavior, cross-client parity, human review, signing, rollback, and stable authorization remain open.

## Current Linux-first checkpoint

The Linux provider form now exposes an optional manual model field for every preset. Core
`7d0f61ee528d32a5671c65d3c253c12368cf40c4` preserves a validated selected model as a localized
`Manual` entry when native/protocol discovery is empty or returns `ModelUnavailable` (including
HTTP 404); authentication, network, and timeout failures remain typed errors. Linux functional
code `871c2da4e5f41cfb8197c7688ee0dd9f11b245fe` and packaging/status head `9bda4c64263167cba271fbf70abec546aa68b3fc` carry the UI,
Flatpak pins, and evidence. Local Core/Linux validation passed; the exact GTK binary is compile-
verified but cannot link on this host because GTK/GDK/Graphene symbols are unavailable. This remains
prerelease Linux evidence; other clients, human/physical review, signing, rollback, and stable
authorization remain open.

The Provider Hub health label now has a serialized GTK lifecycle fixture at Linux
`1155a224f74da8b2e2b201ad01139ef1df97a2e2`, covering hidden, UTC success, normalized failure,
clear, and no-selection states without exposing credentials or raw diagnostics. The synchronized
documentation/Flatpak head is `c39a5566ae0c87ef892cf9ba38f446b3a16429e5`, with Core
`460728d79b0e2373445c3d8994793d069b8057b9` and l10n
`74f773774bdf01ca5d2ab61ce199dbd76cdadb04`. Push Native/Flatpak/Foundation runs
`30016302142`/`30016302028`/`30016302180` passed; PR Native/Flatpak/Foundation runs
`30016306021`/`30016305892`/`30016305878` also completed successfully. This remains prerelease evidence; other clients,
qualified human/physical review, signing, rollback, and stable authorization remain open.

The Linux Provider Hub now renders persisted provider-health outcomes without exposing raw
diagnostics or credentials. Linux code `8a913b263475bec70639c55550bdf9717ded4012`, localization
`74f773774bdf01ca5d2ab61ce199dbd76cdadb04` (499 messages), and documentation/Flatpak head
`c75508f887a76e46782a6176e61b560888983c13` are synchronized. Push and PR Native/Flatpak/Foundation
gates passed at `30013497323`/`30013497315`/`30013497291` and
`30013503182`/`30013503000`/`30013502922`. This remains prerelease evidence; other clients,
qualified human/physical review, signing, rollback, and stable authorization remain open.

## Milestone matrix

| Milestone | Current evidence | Remaining completion work |
| --- | --- | --- |
| 0 — Foundation | Verified for all seven public repositories | Keep manifests and goal pins synchronized |
| 1 — Core vertical slice | Verified Core CLI, fake streaming, cancellation, ABI/protocol, storage, tests, and CI | Stable-release conformance and cross-client consumers |
| 2 — SDK artifacts | Prerelease Linux, Android, Apple artifacts and ABI 1 wrappers are CI-verified; Core ABI 1 now projects bounded provider metadata | Windows/Android/Apple host-service conformance, lease transfer, signed artifacts |
| 3 — Native clients | Linux GTK slice is substantially verified; Android and macOS are partial; Windows is foundation-only | Real provider/secret/model/translation flows on all four clients, device and desktop evidence |
| 4–5 — Providers and quality | Linux catalog, local models, model-source provenance labels, persisted Provider Hub health outcomes, routing, candidate-chain editing, one-shot fallback consent, request-level glossary protection, bounded TBX import, persistent Core schema 33 glossary libraries with GTK save/list/load/delete controls, chunking, history, memory, domain/tone/formality/audience presets, bounded regional-locale/script presets, bounded proxy transport settings and SecretRef authentication, bounded total/connection/streaming-idle timeout settings, additive custom PEM trust bundles, client-certificate SecretRef identities, and a pinned third-party Ollama daemon fixture have deterministic evidence | Cross-client parity, live-provider account/quota interoperability, provider-specific semantics |
| 6 — Documents | Linux supports the bounded TXT/Markdown/HTML/JSON/CSV/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB/PDF slice plus an explicit image-only PDF OCR fixture | Native document workflows on the other clients and broader format acceptance |
| 7 — Localization/accessibility | Generated packs, runtime switching, RTL, pseudo-locales, keyboard and headless AT-SPI/Orca checks exist | Qualified translation review, human screen-reader/visual review, other-client checks |
| 8 — Hardening/release | Protocol/document fuzzing, bounded C ABI malformed-input, safe lifecycle, valid-command, and opaque-handle lifetime fuzzing, sanitizers, migrations, parser limits, checksums, SBOMs, performance evidence, Unix process-crash WAL recovery, bundled `unix-excl` alternate-VFS regression, controlled ENOSPC degradation, and a manifest-only rollback rehearsal exist | Custom/third-party VFS and physical power-loss evidence, signing, production rollback authorization, stable release authorization |

## Acceptance-scenario matrix

Linux CI/runtime evidence exists for Scenarios 4–18 (with the documented provider, display,
and human-review boundaries), including the production GTK Scenario 5 A→B switch fixture, the
candidate-chain/fallback-consent lifecycle fixture, and Anthropic/Gemini/Azure protocol-preset
transport fixture.
Scenario 1 and Scenario 19 have central/core evidence. Scenarios 2, 3, 5, 8, 13, and 16
remain globally incomplete until every required native client passes. Scenario 10 and 11
are Linux document evidence only. Scenario 20 is not achieved: the release manifest is
intentionally `unreleased` and contains no stable artifacts.

## Next executable gates

1. Keep the Linux PR, central issue, and release documentation synchronized with the latest
   verified heads, including the Provider Hub health UI, shared routing planner and approved
   fallback, glossary-library selector/localization, bounded TBX import, model-source provenance
   labels, regional-locale/script presets, provider-switch, Anthropic/Gemini/Azure protocol-preset,
   proxy-authentication, proxy-settings, timeout, custom-trust-bundle, and client-certificate
   identity checkpoints.
2. Do not promote any prerelease evidence to a stable component or release artifact.
3. When the Linux-first scope is released by the user, implement the next native-client
   conformance slice and repeat the same Core/l10n/manifest/CI evidence loop.

Unverified manual, physical, credentialed, signing, and other-client work remains explicitly
unverified rather than being inferred from deterministic Linux fixtures.
