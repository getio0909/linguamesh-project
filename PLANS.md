# LinguaMesh Execution Plan

Status: Active
Started: 2026-07-17
Authority: `PROJECT_GOAL.md` and the active user goal

## Objective

Deliver LinguaMesh as a production-grade, local-first native translation suite across the canonical project, core, localization, Android, Windows, macOS, and Linux repositories. Completion requires compatible stable releases in `release-manifest.toml`, all mandatory acceptance scenarios passing, and reproducible evidence for every claimed capability.

## Safety and operating constraints

- Preserve existing local and remote work; inspect before creating or updating repositories.
- Never delete repositories, force-push, rewrite published history, expose credentials, create paid resources, or publish an unverified stable release.
- Commit and push only verified checkpoints.
- Keep production credentials out of source, tests, logs, diagnostics, and public-fork CI.
- Use native platform stacks and keep shared non-UI behavior in the Rust core.

Assumption: The authenticated GitHub user resolved by `gh api user` is the canonical owner unless existing repositories or account state contradict that.

Assumption: This Debian x86_64 host is authoritative for Linux and portable Rust checks; unavailable Android, Windows, and macOS builds require appropriately configured GitHub Actions evidence.

Assumption: Planned files and commands are not evidence until they exist and complete successfully.

## 2026-07-24 — Linux Core pin synchronization

Assumption: Core `b29067b78d420c96f57d670d3dd860cba3abc703` is a fuzz/docs-only descendant of the
Linux runtime baseline; pin synchronization records compatibility provenance without claiming a
new Linux runtime feature.

- [x] Synchronize Linux Native workflow, Flatpak Core source, contributor guidance, architecture,
  testing, release, and implementation-status documentation to Core `b29067b…` and l10n
  `c2526b…`; preserve historical entries and keep release `unreleased`.
- [x] Pass local Linux localization audits, Flatpak metadata validation, formatting, offline
  demo-provider check, DOCS_RS Clippy, 85 no-default tests, 166 demo-provider tests, cargo-deny,
  and Core runtime-source cleanliness checks; record the local GTK development-package blocker.
- [x] Push Linux runtime/build head `449facf…` and final evidence head `4b592e7…`. Push and PR
  Native/Flatpak/Foundation runs `30063415446`/`30063415485`/`30063415440` and
  `30063417561`/`30063417542`/`30063417551` passed with jobs recorded in Linux status.
- [ ] Keep human/physical review, other clients, signed artifacts, rollback authorization, and
  stable release authorization open.

## 2026-07-24 — Core valid-command FFI fuzz checkpoint

Assumption: the local `FakeProviderServer` is a deterministic loopback fixture; it proves the C ABI
submit/event/buffer lifecycle without commercial credentials, live-provider behavior, or client parity.

- [x] Add Core `ffi_commands` libFuzzer coverage for bounded valid `TranslateText` commands,
  terminal-event uniqueness, buffer release, and engine destruction; retain its minimized corpus.
- [x] Pass local pinned-nightly fuzz smokes: `ffi_commands` completed 136 time-bounded iterations
  with 10,653 coverage features and 49 corpus files; `ffi_inputs` and `ffi_sequences` passed 200
  iterations each. Core FFI unit tests passed 20/20 and locked/offline checks passed.
- [x] Push Core `b29067b78d420c96f57d670d3dd860cba3abc703`; CI `30062160464`, Fuzz/ASAN
  `30062160452`, and Native SDK `30062161560` all passed, including Linux, Windows, Android, and
  Apple jobs. Update the central Core source pin in commit `b2d1ae9dc425cafd359746ef75031dce9f9a9ea2`;
  coordination workflow `30062468039` passed Linux `89386679596` and PowerShell `89386679650`.
- [x] Refresh GitHub triage with Issue #1 comment `5065656009`, Linux PR #1 comment `5065656120`,
  and macOS PR #1 comment `5065656205`; no actionable review threads were present, and no merge or
  stable promotion was performed.
- [ ] Keep raw engine-pointer use-after-free, cross-client parity, signing, production rollback
  authorization, physical/alternate-VFS recovery, and stable release authorization open.

## 2026-07-24 — Core FFI fuzz and sanitizer checkpoint

Assumption: malformed and unsupported C ABI inputs are the safe automated boundary; valid provider
commands, forged raw handles, cross-client parity, and release qualification require separate gates.

- [x] Add Core `ffi_inputs` and `ffi_sequences` libFuzzer coverage through `lm_engine_submit` and
  lifecycle/control calls, with a 1 MiB input cap and provider/network-free handling of valid
  translation envelopes.
- [x] Pass local pinned-nightly ASAN smokes (`200` runs, `299`/`2,326` coverage features, 29-/47-file
  corpora), Core CI `30061241968`, Fuzz/ASAN `30061241972`, and Native SDK `30061241961` across all
  four jobs.
- [x] Pin central commit `adab809ed7d265aac85e7cd53393d5b9ba0dfdef`; coordination workflow
  `30060907288` passed Linux `89382183919` and PowerShell `89382183959`.
- [x] Synchronize the final Core pin in central commit `62085d82b4aa2fe7efd3e635e1f2868c9e66bf8d`;
  coordination workflow `30061527364` passed Linux `89383965632` and PowerShell `89383965670`.
- [x] Move valid-command fuzzing to the separate loopback gate above.
- [ ] Keep raw-handle misuse, signing, production rollback authorization, physical/alternate-VFS
  recovery, and stable release authorization open.

## 2026-07-24 — Core storage durability regression

Assumption: the host-pinned Rust 1.93.0 storage run is deterministic Linux evidence for the
default SQLite Unix VFS; it does not substitute for alternate-VFS or physical power-loss testing.

- [x] Run `cargo +1.93.0 test -p linguamesh-storage --locked --offline`: 55 tests passed, 0
  failed, including WAL replay after writer disconnect and abrupt process termination, busy
  checkpoint retry, schema migration, secure deletion, symlink rejection, and trusted-descriptor
  path validation.
- [x] Keep the documented boundary explicit: alternate SQLite VFS enforcement and physical
  power-loss behavior remain unverified; no stable-release claim follows from this run.

## 2026-07-24 — Automated rollback rehearsal regression

Assumption: a temporary Git fixture can prove the rehearsal script's manifest-only invariant
without standing in for production rollback authorization or physical storage recovery.

- [x] Add `tools/test-release-rollback.py`, which creates a disposable Git repository, runs the
  rollback rehearsal, and asserts that neither the manifest nor repository files change.
- [x] Run `/home/wangtinghu/miniconda3/envs/py313/bin/python tools/test-release-rollback.py`; the
  unittest passed, and the test is now part of the central Linux validation workflow
  `30060144548` (Linux `89379970142`, PowerShell `89379970114`).
- [ ] Keep production rollback authorization, signed-artifact rollback, alternate VFS, and
  physical power-loss behavior open.

## 2026-07-24 — Containerized Linux validation checkpoint

Assumption: the disposable Debian trixie container is bounded Linux evidence only; its Rust
1.93.1 toolchain is compatible with, but does not replace, the repository's pinned 1.93.0
toolchain, and container capability failures remain unverified rather than passing results.

- [x] Run the locked all-target test suite as a non-root user under Xvfb/DBus: the library passed
  `168 passed; 0 failed; 16 ignored` and the binary passed `30 passed; 0 failed; 21 ignored`.
  All 18 dedicated ignored GTK lifecycle fixtures passed, including fallback approval, Secret
  Service fallback, redacted authentication errors, offline recovery, provider switching,
  cancellation, glossary/protected spans, incognito mode, document resume, atomic output, and
  malicious archive rejection.
- [x] Pass notification transport and dunst delivery, interactive file chooser, GTK file chooser,
  drag-and-drop, English and Arabic keyboard focus, headless Wayland, OCR, four-case mTLS,
  performance-baseline generation, debug build, and optimized release build (`2m 36s`).
- [x] Re-run Secret Service persistence/prompt fixtures; store/delete, restart, locked-item, and
  cleanup cases passed. The Debian container also passed the notification daemon desktop-shell
  rendering fixture with generic, non-content payloads.
- [x] Re-run the document-portal lease and storage-fault fixtures in a disposable container with
  `/dev/fuse`, `SYS_ADMIN`, and AppArmor isolation explicitly granted: both passed, including
  add/map/grant/revoke/delete and ENOSPC degradation to session mode.
- [x] Reproduce the live AT-SPI inspector in an Ubuntu 24.04 runtime container (the Native CI
  base family) against the actual Linux binary: English, Simplified Chinese, Arabic, `en-XA`,
  and `ar-XB` all passed. Debian trixie remains a known bridge-version difference, not a product
  failure; the binary was built in the disposable Rust 1.93.1 cache environment.
- [x] Download the unexpired Flatpak bundle from Native CI run `30052187036` for Linux head
  `597ccc961f9530836f8cef4c9a12a64b5c0a311c`, verify its checksum against the matching evidence
  artifact (`a01177a9a1a3d84ac8e3de0cc509305f71494307134281ce42882a0e40e2dc02`), parse the SPDX 2.3
  SBOM (234 packages), and pass the sandbox smoke on GNOME runtime `org.gnome.Platform/x86_64/49`.
- [x] Re-run the pinned third-party Ollama interop fixture with `ollama/ollama:0.11.10` and
  `smollm:135m`: after model download/warm-up, the exact ignored worker test passed `1 passed;
  0 failed` without a credential. The worker test now uses a dedicated 30-second harness deadline
  for cold model startup; the earlier generic five-second helper timed out cold, so no cold-start
  performance claim is made.
- [x] Attempt the exact Rust 1.93.0 Linux build in a disposable container. Rustup timed out while
  fetching `channel-rust-1.93.0.toml.sha256` from both the official distribution endpoint and the
  configured Tuna mirror; this is recorded as unavailable evidence, not a passing build. No
  source or dependency files were changed, and Ubuntu Native CI remains authoritative.
- [x] Use the host-pinned Rust 1.93.0 toolchain after removing only generated target caches: Core
  `cargo check --workspace --locked --offline` passed, and Linux's non-GUI demo-provider suite
  passed `166 passed; 0 failed; 7 ignored` with loopback proxy bypassed. The host GUI check remains
  unavailable because `gtk4` and `graphene-gobject-1.0` development packages are absent; Native
  CI remains authoritative for display-backed validation.
- [x] Push Linux worker test commit `c03c7e2065c1a0f74f6326d9e5071ee3cbde6299` and Flatpak
  source-pin commit `1c513e2e52236fce03a60548dbcab242c6878bed`. Native `30058395686`, Flatpak
  `30058395689`, and Foundation `30058395669` all passed, including the Ollama test's dedicated
  cold-start deadline, Flatpak sandbox smoke, checksums, and SBOM evidence.
- [ ] Keep release `unreleased`; human/physical review, live providers, other clients, signing,
  rollback, and stable-release authorization remain open.

## 2026-07-24 — Linux release-manifest synchronization

Assumption: the verified Linux branch head is the source revision for the prerelease component,
while the release train remains unreleased until every cross-client and qualification gate passes.

- [x] Align `[components.linux].source_revision` with verified Linux head
  `1c513e2e52236fce03a60548dbcab242c6878bed`; the previous `597ccc...` pin was stale.
- [x] Run `bash tools/check-workspace.sh` and push central commit `ae9dcee854dc74af0cf8414850145de39be11057`;
  coordination workflow `30059016853` passed Linux job `89376633187` and PowerShell job
  `89376633215`.
- [ ] Keep the release `unreleased`; no stable artifact or client merge is authorized by this
  manifest-only synchronization.

## 2026-07-24 — Draft release-train record

Assumption: a documented Draft record improves reproducibility without implying that the current
Linux-first checkpoint is a stable release.

- [x] Add `docs/releases/bootstrap.md` with component pins, contract versions, CI provenance,
  known limitations, signing status, and a reversible manifest-only rollback procedure.
- [x] Push the record at central commit `6168bd5e067e6839aa35fd7f16ec1834809573b0`; coordination
  workflow `30059285976` passed Linux job `89377421652` and PowerShell job `89377421691`.
- [ ] Keep the record Draft and release status `unreleased` until all four native clients,
  physical/qualified human review, signing, rollback rehearsal, and stable authorization pass.

## 2026-07-24 — Clean bootstrap acceptance rerun

Assumption: a disposable clone of the public central repository and its seven canonical siblings
is the appropriate evidence for Scenario 19; it must not alter any existing checkout.

- [x] Run the documented `git clone --depth=1` plus `GITHUB_OWNER=getio0909 tools/bootstrap.sh`
  flow in a temporary workspace. All seven repositories cloned and strict workspace, goal-pin,
  manifest, documentation-link, and credential-signature checks passed.
- [x] Record the rerun in central commit `6d586e0a4f40327998850e86a38f5fe68f4b2b8b`; coordination
  workflow `30059408522` passed Linux job `89377790156` and PowerShell job `89377790104`.
- [ ] Keep commercial credentials, stable publication, and unsupported platform execution outside
  the default bootstrap acceptance path.

## 2026-07-24 — Manifest rollback rehearsal

Assumption: a manifest-only rehearsal can verify the reversible pin transition without pretending
to exercise physical power loss, signed artifact rollback, or production authorization.

- [x] Add `tools/rehearse-release-rollback.py`; it verifies that the target Linux commit exists,
  changes only the selected component revision in a temporary parsed manifest, preserves
  `unreleased`, and leaves repository files untouched.
- [x] Run the rehearsal from the current workspace from Linux `1c513e2...` to previously verified
  `597ccc...`; it passed with English diagnostics and no checkout mutation.
- [x] Push the rehearsal at central commit `ac6a0dff7c54883891b482cedc42015b0a81954e`; coordination
  workflow `30059622064` passed Linux job `89378438634` and PowerShell job `89378438650`.
- [ ] Keep physical VFS/power-loss behavior, signed artifact rollback, and production rollback
  authorization open.

## 2026-07-23 — Linux automation boundary audit

Assumption: the current Linux plan and gap matrix are authoritative for deciding whether another
headless slice is still automatable; missing host dependencies must remain explicit failures.

- [x] Re-run the current mTLS client-certificate fixture: all four exact cases passed once; the
  Linux library suite passed `166 passed; 0 failed; 7 ignored`; formatting, Clippy, localization,
  Flatpak metadata, and workspace checks passed.
- [x] Re-run Secret Service coverage: prompted store/delete approval and dismissal cases passed;
  persistent store/restart checks passed. The complete display-backed runner stopped at the missing
  local `xvfb-run` command, and the document-portal runner could not mount `/run/user/1000/doc`
  because this host denied the FUSE mount.
- [x] Audit the Linux gap matrix and open PRs: Linux PR #1 and macOS PR #1 have no reviews or
  unresolved threads; remaining Linux gaps are human/physical, live-provider, signing, rollback,
  or release-authorization boundaries rather than an unimplemented deterministic Linux slice.
- [x] Check the available GNOME SDK container: it provides `xvfb-run` and `flatpak-builder` but
  not Rust/Cargo, so it cannot be substituted for the pinned Linux build without changing the
  toolchain. No dependency installation or claim of local GTK execution was made.
- [x] Push the audit at central revision `d492233dd65944ec72b2b6cece4e2c1702a137c2`;
  coordination workflow `30053493214` passed both Linux and PowerShell validation jobs.
- [ ] Keep the release `unreleased` and continue only with authorized cross-client or external
  qualification work when its required environment and scope are available.

## 2026-07-23 — GitHub PR and Issue triage refresh

Assumption: authenticated connector metadata and completed check runs are authoritative for review
triage, while Draft/Open state remains the safe posture until the explicitly open qualification gates
are complete.

- [x] Recheck Linux PR #1 at head `597ccc961f9530836f8cef4c9a12a64b5c0a311c`: it remains
  Draft/Open and mergeable; Native/Flatpak/Foundation push and PR checks all passed.
- [x] Recheck macOS PR #1 at head `cad822c69dcf1ad20f8cab2151f407866a577420`: it remains
  Draft/Open and mergeable; Native `29765906044` and Foundation runs `29765906715`/
  `29765904969` passed.
- [x] Confirm both PRs have no submitted reviews or unresolved inline threads, and record the
  result on macOS PR #1 and central Issue #1. No merge, stable promotion, or release-manifest
  status change was performed.
- [x] Push the central triage documentation at `c5bbe3520a73feacbc43c9d94a05b136dc20a3d2`;
  coordination workflow `30053066918` passed both Linux and PowerShell validation jobs.
- [ ] Keep Linux as the active implementation priority; Android, Windows, macOS parity, live
  provider interoperability, prompted approval, qualified human review, signing, rollback, and
  stable-release acceptance remain open.

## 2026-07-23 — Linux mTLS client-authentication rejection

Assumption: a temporary endpoint that trusts a different client CA is bounded evidence that the
Linux worker rejects an untrusted client certificate; enterprise interoperability remains open.

- [x] Add the fourth ignored worker regression and client-CA fixture at runtime/test commit
  `7513d983011fdd81374cfb879b23647aef388f7e`; all four exact local runners passed once.
- [x] Align Flatpak/release source pins at `deffb80df01cb9f6c76a8b46e0ad725080e07ea6` and record
  status evidence at `597ccc961f9530836f8cef4c9a12a64b5c0a311c`; local library validation passed
  `166 passed; 0 failed; 7 ignored`.
- [x] Pass final status-head push Native/Flatpak/Foundation `30052187039`/`30052187036`/
  `30052187043` and PR Native/Flatpak/Foundation `30052189474`/`30052189521`/`30052189488`.
- [ ] Keep enterprise interoperability, prompt approval, human review, cross-client parity,
  signing, rollback, and stable-release authorization open; keep PR #1 Draft/Open, Issue #1 Open,
  and release status `unreleased`.

## 2026-07-23 — Linux mTLS hostname verification

Assumption: a trusted-CA server certificate with a wrong SAN is bounded evidence that hostname
verification remains enabled; enterprise interoperability remains open.

- [x] Add the ignored hostname-mismatch worker regression and temporary HTTPS fixture at Linux
  runtime/test commit `ec6c9971e0271e5eddc89bdc64121761a9cb46df`; trusted, untrusted-CA, and
  wrong-SAN runners each passed `1 passed; 0 failed` locally.
- [x] Align the Flatpak/release source pin at `9fc633feeca328b356b8f98eead03e29d28d0d46` after
  the stale-pin validation failure, and record status evidence at `1629547c0eca1a5aabcd06cb7a96ecdfeaf97e80`.
- [x] Pass final status-head push Native/Flatpak/Foundation `30050789607`/`30050789609`/
  `30050789567` and PR Native/Flatpak/Foundation `30050792424`/`30050792455`/`30050792453`.
- [ ] Keep enterprise interoperability, prompt approval, human review, cross-client parity,
  signing, rollback, and stable-release authorization open; keep PR #1 Draft/Open, Issue #1 Open,
  and release status `unreleased`.

## 2026-07-23 — Linux mTLS trust-bundle rejection

Assumption: a second local HTTPS endpoint signed by an unrelated CA is bounded evidence that the
configured trust bundle rejects an untrusted server; enterprise interoperability remains open.

- [x] Extend the Linux client-certificate fixture at runtime/test commit
  `896cd2352aef73a86ca80d7d92e2b5c7850af7d7` with trusted and unrelated-CA endpoints; the local
  runner passed both positive and negative regressions (`1 passed; 0 failed` each).
- [x] Align Flatpak/release source pins at `cb6a3b166344c240c135a829ef32d14e6b5214e6` and record
  status evidence at `6113f4898a3d81fedd103b413d739797238c8490`; local library validation passed
  `166 passed; 0 failed; 5 ignored`.
- [x] Pass final status-head push Native/Flatpak/Foundation `30049361416`/`30049361411`/
  `30049361698` and PR Native/Flatpak/Foundation `30049363915`/`30049363922`/`30049363912`.
- [ ] Keep enterprise interoperability, prompt approval, human review, cross-client parity,
  signing, rollback, and stable-release authorization open; keep PR #1 Draft/Open, Issue #1 Open,
  and release status `unreleased`.

## 2026-07-23 — Linux client-certificate HTTPS transport

Assumption: a temporary local mutual-TLS endpoint is bounded Linux transport evidence; live
enterprise endpoints and cross-client certificate handling remain open.

- [x] Add the Linux worker regression and temporary HTTPS fixture at runtime/test commit
  `4b5a3f2ec0e65060d104068be6a6f31446007ee4`; the exact local runner passed with `1 passed; 0 failed`.
- [x] Pin Flatpak and document the fixture at `7b69933e1b0b92e1ee2136e01b6d39fa765ec761`, then
  harden generated certificate extensions at `e9406d56e1345be765c01ecfe2600e8e0d10dde9`.
- [x] Record final status head `14b601ae1ac11e98e09a4d2727f6ebb584f32ad4`; push
  Native/Flatpak/Foundation `30047564119`/`30047564124`/`30047564131` and PR
  `30047567575`/`30047567392`/`30047567456` all passed.
- [ ] Keep enterprise interoperability, prompt approval, human review, cross-client parity,
  signing, rollback, and stable-release authorization open; keep PR #1 Draft/Open, Issue #1 Open,
  and release status `unreleased`.

## 2026-07-23 — Linux session proxy authentication transport

Assumption: a local HTTP proxy fixture is bounded Linux transport evidence; live proxy deployment
and provider interoperability remain open.

- [x] Add worker-level proxy transport regression at Linux `911994eb3f4c364af3ea043b783f2aff18e09888`;
  it asserts the absolute provider target, exact Basic header, and model response with a session
  SecretRef.
- [x] Pin Flatpak and release documentation at `968b5c88cdda64ae69a2c80add729bb37ca7548b`; local
  formatting, locked checks, strict Clippy, 166 tests with three documented ignores, l10n sync,
  Flatpak metadata, and diff checks passed.
- [x] Record final Linux status head `f78d0939dd78c1646da4f7e3fa7f87665a534bf5`; push
  Native/Flatpak/Foundation `30045229527`/`30045229529`/`30045229541` and PR
  `30045232877`/`30045232887`/`30045232885` all passed.
- [ ] Keep live provider interoperability, prompt approval, human review, cross-client parity,
  signing, rollback, and stable-release authorization open; keep PR #1 Draft/Open, Issue #1 Open,
  and release status `unreleased`.

## 2026-07-23 — Linux session SecretRef validation paths

Assumption: worker-level rejection tests are bounded evidence for session-only proxy-authentication
and client-certificate identity handling; live proxy/certificate interoperability remains open.

- [x] Add runtime regressions at Linux `f0a65c0d7bd1ddfda6e531db1b93c6be0096d491`; invalid
  session-only values reach Core validation and their canaries remain absent from diagnostics.
- [x] Pin Flatpak and release documentation at `dcd3f49620b427d460c98082acaf97498f2b98ff`; local
  formatting, locked checks, strict Clippy, 165 tests with three documented ignores, l10n sync,
  Flatpak metadata, and diff checks passed.
- [x] Record final Linux status head `4cfa3fa8cfa29f5dc036e53bafa388444b8de94e`; push
  Native/Flatpak/Foundation `30043522421`/`30043522574`/`30043521477` and PR
  `30043524643`/`30043524550`/`30043524574` all passed.
- [ ] Keep live provider interoperability, prompt approval, human review, cross-client parity,
  signing, rollback, and stable-release authorization open; keep PR #1 Draft/Open, Issue #1 Open,
  and release status `unreleased`.

## 2026-07-23 — Linux all-SecretRef persistence filtering

Assumption: the worker-level persistence regression is the smallest reproducible evidence that
session-only secret references cannot reach SQLite; the GTK Secret Service fixture remains the
runtime integration boundary.

- [x] Extend the Linux profile filter regression at runtime test
  `bb6bc5bef572eb19d7c066e24a2d48546bf4fb08` across the primary credential, secret custom
  headers, proxy authentication, and client certificate identity SecretRefs. Persistent refs
  remain and all three session-only refs are removed before persistence.
- [x] Pin Flatpak and document the boundary at Linux packaging/docs commit
  `9dc863eeb9fc5825c7354863c59bb21bf4447381`; local formatting, locked checks, strict Clippy,
  163 demo-provider tests with three documented ignores, localization, Flatpak metadata, and
  diff checks passed.
- [x] Record Linux final status head `2c3212c562eb8d425ee302a329f77ed7821a3231`; push
  Native/Flatpak/Foundation `30041197129`/`30041196965`/`30041196986` and PR
  Native/Flatpak/Foundation `30041200604`/`30041200579`/`30041200581` all passed.
- [ ] Keep interactive prompt approval, human visual/Orca review, cross-client parity, signing,
  rollback, and stable-release authorization explicitly open; keep PR #1 Draft/Open, Issue #1
  Open, and release status `unreleased`.

## 2026-07-23 — Linux Secret Service custom-header onboarding

Assumption: the authenticated loopback and private Secret Service fixture is the smallest
reproducible evidence for the second GTK secret editor path; interactive prompts, human review,
and other clients remain separate qualification gates.

- [x] Extend the GTK Remember/clear-form regression to enter bounded secret custom-header JSON,
  verify a second persistent SecretRef and active-profile restoration, clear both sensitive fields,
  scan SQLite artifacts for both canaries, and delete both Secret Service items. Linux runtime test
  `f6cdb44dd6e411c2fab1c9f39cd3cd63361a1352` and packaging/docs `d1e7368edcf8426d3986165fc5b2adbd33cabe48`
  implement and document the slice.
- [x] Record final status head `e9b7d80e3ecac045eeb10b37ea59871c0ada6198`; push Native/Flatpak/
  Foundation `30039406785`/`30039406821`/`30039406753` and PR Native/Flatpak/Foundation
  `30039409345`/`30039409381`/`30039409339` all passed.
- [ ] Keep interactive prompt approval, visual/translated-copy/Orca review, cross-client parity,
  signing, rollback, and stable-release authorization explicitly open.

## 2026-07-23 — Linux process-interruption export regression

Assumption: terminating a dedicated GTK child after temporary-file synchronization is the
smallest reproducible process-interruption boundary; physical power-loss and alternate-VFS
recovery remain unverified.

- [x] Add Linux runtime/test commit `361ac7ba9d6a18c26de4487ab424d6500fbbeafd`; the child-process
  fixture kills the writer before the final move and verifies no final destination appears while
  the synced `.linguamesh-export-*` bytes remain intact.
- [x] Pin Linux packaging/docs at `71b6fa34d536ec5753160ad270b507bd9fffa518`; local formatting,
  locked checks, strict Clippy, 163 demo-provider tests with three documented ignores, and
  Flatpak metadata/diff validation passed. The host GTK linker limitation remains documented.
- [x] Pass final status-head push Native/Flatpak/Foundation `30037853956`/`30037853881`/`30037853988` and
  PR Native/Flatpak/Foundation `30037855907`/`30037855888`/`30037855890`; Native explicitly
  completed the interrupted export fixture. Keep PR #1 Draft/Open, Issue #1 Open, and release
  status `unreleased`.

## 2026-07-23 — Linux local-export durability barriers

Assumption: Linux local exports require bounded crash-durability barriers for file bytes and
directory metadata; physical power-loss recovery and alternate-VFS behavior remain separate,
unverified acceptance boundaries.

- [x] Add Linux runtime `cf4246c24e087de870adae4878379512cbaf2b8a` barriers that sync a local
  export file before the atomic move and sync its parent directory after the move; barrier
  failures report a save error, while non-local GIO destinations retain the remote-VFS boundary.
- [x] Document the contract in Linux testing, architecture, and implementation status; pin the
  Flatpak/source documentation head at `9085ed2f8a3acf39f24930ca2dcf98567427c80f`.
- [x] Pass local formatting, locked compile, strict Clippy, 163 demo-provider tests with three
  documented ignores, localization audits, l10n synchronization, Flatpak metadata, and diff checks.
- [x] Pass push Native/Flatpak/Foundation `30032394587`/`30032394653`/`30032394626` and PR
  Native/Flatpak/Foundation `30032396787`/`30032396790`/`30032396829`; keep the PR Draft/Open,
  Issue #1 Open, and release status `unreleased`.

## 2026-07-23 — Linux local-export barrier regression evidence

Assumption: the direct file-and-parent-directory sync regression strengthens the bounded local
filesystem guarantee, but it does not prove physical power-loss recovery or alternate-VFS behavior.

- [x] Add direct Linux regression `3a84352410271ce53f01cfed162d83aad8c33719` for file and parent
  directory synchronization, with runtime `cf4246c24e087de870adae4878379512cbaf2b8a`.
- [x] Record the regression and host GTK linker boundary in Linux docs/status at `8dc86c5` and
  `d52ab2f7bd339f360a26497d5a42bb7184b742e9`; pin the Flatpak source input at `8dc86c5`.
- [x] Pass local format, locked all-target and test checks, strict Clippy, 163 demo-provider
  tests with three documented ignores, localization audits/sync, Flatpak metadata, and diff checks.
- [x] Pass push Native/Flatpak/Foundation `30034083462`/`30034083390`/`30034083610` and PR
  Native/Flatpak/Foundation `30034086699`/`30034087655`/`30034086738`.
- [x] Keep PR #1 Draft/Open, Issue #1 Open, manifests synchronized, and release status
  `unreleased`; physical power-loss, alternate-VFS, other-client, signing, rollback, and stable
  release evidence remain open.

## 2026-07-23 — Linux routing candidate-management evidence reconciliation

Assumption: the automated Linux candidate editor, ordered/automatic fallback selection, and
one-shot approval boundaries are verified; visual, translated-copy, end-user Orca, cross-client,
and stable-release qualification remain separate gates.

- [x] Reconcile Linux release documentation with the candidate editor lineage
  `c0cdee8b729a6800904f67535430221feb55f78e`, `a4dd4aa644335a3b6539db4d40473423c6292c71`, and
  GTK lifecycle test `5c49a3a18c448542bc9cf055cd81b4a0b5f01e15`.
- [x] Record worker fallback-chain/approval evidence from `0e2ae25c321cef243275d1322f2b8271f0602d06`
  and `af200122e4862f6230d89268f5292f16438449bb`; fallback remains disabled by default.
- [x] Pass the new Linux docs-head gates at `e13d6804b7ce17edb1490c5dc6629b9664d6c3b7`: push
  Native/Flatpak/Foundation `30035253038`/`30035253264`/`30035253013` and PR
  Native/Flatpak/Foundation `30035256459`/`30035256435`/`30035256652`.

## 2026-07-23 — Central localization pin consistency

Assumption: the current canonical localization input is the immutable l10n `c2526bfb3f6ff57895bdc3eeed743e26c8783613`, which includes the earlier copy, clear, and language-swap messages; no new localization content is required for the export durability slice.

- [x] Correct `release-manifest.toml` to use the l10n revision consumed by Linux's checked
  `tools/sync-l10n.sh` and the generated PO/MO resources.
- [x] Re-run central manifest, documentation-link, credential-hygiene, and diff validation; keep
  all release components `unreleased` and do not change the Linux PR or stable-release state.

## 2026-07-23 — Linux localized language swap action

Assumption: Linux is the active implementation priority; swapping is local and request-free for the
supported English/Chinese pair, and unsupported Auto/Japanese combinations remain disabled.

- [x] Add Linux `4e5a94feef09bbe382a0b6690dc8e8f7b138656f` localized Swap languages UI, sensitivity
  gating, locale refresh, and unit/GTK regression coverage.
- [x] Push localization `c2526bfb3f6ff57895bdc3eeed743e26c8783613`; `make check` passed 506 messages
  and 26 tests; synchronize Linux PO/MO resources and Native workflow pin.
- [x] Pass local format, GUI/all-target checks, strict Clippy, 163 demo-provider library tests with
  three documented ignores, localization audits, Flatpak metadata, sync, and diff checks.
- [x] Record green PR Native/Flatpak/Foundation `30030245422`/`30030245461`/`30030245538` and push
  Native/Flatpak/Foundation `30030243332`/`30030242763`/`30030242764`.
- [x] Keep PR #1 Draft/Open, Issue #1 Open, manifests synchronized, and release status `unreleased`.

## 2026-07-23 — Linux explicit Clear workspace action

Assumption: Linux remains the active implementation priority; clearing the text workspace must not
send a worker command or alter provider, locale, glossary, or history settings.

- [x] Add Linux `38275fd96f0b9ed00b7d3269974780fd61874936` Clear workspace reducer/UI behavior,
  localized focusable action, document-job/active-request sensitivity guards, and GTK/model regressions.
- [x] Push l10n `99e0e04d200a03b2de79a8dd4a8d018847519ea2`; `make check` passed 504 messages and 26
  tests; synchronize the Linux PO/MO resources and workflow revision pin.
- [x] Pass local format, GUI/all-target checks, strict Clippy, 163 demo-provider tests with 3
  documented ignores, localization audits, l10n synchronization, Flatpak metadata, and diff checks.
- [x] Record green current-head push/PR Native, Flatpak, and Foundation gates
  `30027666940`/`30027665976`/`30027665616` and `30027667935`/`30027667025`/`30027666925`.
- [x] Keep PR #1 Draft/Open, Issue #1 Open, manifests synchronized, and release status `unreleased`.

## 2026-07-23 — Linux native clipboard copy action

Assumption: Linux remains the active implementation priority; a dedicated GTK clipboard action is
the smallest complete native surface for copying finished output, and clipboard bytes must remain
outside Core persistence, diagnostics, notifications, and logs. Other clients and stable release
remain deferred.

- [x] Add Linux `e56e56bec0bcea9fe963ca326e3918da54f50790` Copy translation action, empty-output
  sensitivity gating, localized accessible labels/tooltips, asynchronous clipboard-read regression,
  and synchronized README/architecture/testing/release documentation.
- [x] Push l10n `0ee87720a8613d3dc130dfb379ab4dc7bc1e1f62`; local `make check` passed 502 messages and
  26 tests, with generated Linux resources synchronized into the client.
- [x] Pass local Linux format, GUI/all-target checks, strict Clippy, 162 demo-provider tests with 3
  documented ignores, localization audits, Flatpak metadata, and diff checks.
- [x] Record green Linux push/PR Native, Flatpak, and Foundation gates:
  `30024453944`/`30024454262`/`30024454369` and
  `30024457039`/`30024457175`/`30024457027` for Linux `89f0f2d4fe9f748f34ea388daf91c52228b92b74`.
- [x] Synchronize the Draft PR, open Issue #1, central manifests, and `unreleased` release
  boundary without merging; central commit `555c83e00b5556101d95465771c23617cb909192` passed
  coordination workflow `30025928902` on Linux and PowerShell. PR #1 remains Draft/Open and
  mergeable; Issue #1 remains Open.

## 2026-07-23 — Linux manual model discovery fallback

Assumption: Linux remains the active implementation priority; provider discovery fallback is bounded
to an already validated manual model and does not weaken typed authentication, network, or timeout
errors. Other clients, stable release, and human acceptance remain deferred.

- [x] Push Core `7d0f61ee528d32a5671c65d3c253c12368cf40c4` with empty/404 model-list fallback,
  manual-source projection, and a manual-only fake-provider translation regression; strict Clippy
  and all-workspace tests passed.
- [x] Push Linux functional code `871c2da4e5f41cfb8197c7688ee0dd9f11b245fe` and packaging/status head
  `9bda4c64263167cba271fbf70abec546aa68b3fc`; expose the optional manual field for all presets while retaining required validation
  for Anthropic/Azure-style manual deployments.
- [x] Pass Linux formatting, GUI/all-target checks, 161 demo-provider tests with 3 documented
  ignores, localization audits, Flatpak metadata, and diff checks; host GTK linker limitation is
  recorded and Native CI remains authoritative.
- [x] Refresh the Linux PR and central Issue with the final CI evidence, then keep the PR Draft/Open,
  Issue Open, and the release train `unreleased`.

## 2026-07-23 — Linux Provider Hub health label GTK lifecycle

Assumption: Linux remains the active implementation priority; the fixture uses only persisted,
non-secret health state and does not substitute for other-client or human acceptance evidence.

- [x] Add the serialized GTK lifecycle fixture at Linux `1155a224f74da8b2e2b201ad01139ef1df97a2e2`
  and document its hidden/success/failure/clear/no-selection assertions.
- [x] Repin the Linux Flatpak source and documentation head at `c39a5566ae0c87ef892cf9ba38f446b3a16429e5`;
  Core remains `460728d79b0e2373445c3d8994793d069b8057b9` and l10n remains `74f773774bdf01ca5d2ab61ce199dbd76cdadb04`.
- [x] Pass local format, GUI/all-target compile, demo-provider library, localization, Flatpak, and
  diff checks; push Native/Flatpak/Foundation `30016302142`/`30016302028`/`30016302180` passed.
- [x] Finish GitHub PR check aggregation for PR runs `30016306021`/`30016305892`/`30016305878`; all
  six push/PR gates are green. Synchronize the Draft PR and open central Issue #1 without merging
  or promoting a stable release.
- [x] Validate the synchronized central manifests and documentation with coordination workflow
  `30017427553` on Linux and PowerShell.

## 2026-07-23 — Linux typed provider rate-limit handling

Assumption: HTTP 429 is the stable cross-provider signal for temporary throttling; quota/billing,
live-provider behavior, other clients, and stable-release evidence remain open.

- [x] Push Core `8623b2c8829e4d9cf7299c74440dcfabb4e320db` with shared `RateLimited` mapping,
  bounded retry-hint preservation, storage/ABI round trips, and locked workspace validation.
- [x] Push l10n `630a8f36d96be358d81b72e2efc87cd527e66974` with the Linux category in all official
  packs and deterministic PO/MO resources; `make check` passed 500 messages and 26 tests.
- [x] Push Linux `a7ac73d6fe8707519dd02698c26ebf8ca78a4246` with localized plural retry guidance,
  Flatpak source pins, 162 local demo-provider tests, and all local audits.
- [x] Record green current-head Linux push/PR Native, Flatpak, and Foundation CI:
  `30022122318`/`30022122787`/`30022122379` and
  `30022125925`/`30022125926`/`30022126939`; keep PR #1 Draft/Open and Issue #1 Open.

## 2026-07-23 — Linux Provider Hub health status

Assumption: Linux remains the active implementation priority; persisted health data is non-secret,
and other-client, human/physical, signing, rollback, and stable-release gates remain deferred.

- [x] Push localization `74f773774bdf01ca5d2ab61ce199dbd76cdadb04` with the two health-status
  templates and regenerated 499-message resources; Localization/Foundation
  `30013123046`/`30013122894` passed.
- [x] Add Linux `8a913b263475bec70639c55550bdf9717ded4012` Provider Hub rendering for the selected
  saved/active profile's UTC success timestamp or normalized failure category, with no raw error or
  credential exposure; docs and Flatpak pin are at `c75508f887a76e46782a6176e61b560888983c13`.
- [x] Pass Linux push Native/Flatpak/Foundation `30013497323`/`30013497315`/`30013497291` and PR
  Native/Flatpak/Foundation `30013503182`/`30013503000`/`30013502922`, plus local format, Clippy,
  library-test, synchronization, localization-audit, Flatpak, and diff checks.
- [x] Central coordination workflow `30014149373` passed on Linux and PowerShell after the
  release manifest, gap analysis, status, and plan were synchronized.
- [x] Keep PR #1 Draft/Open and Issue #1 Open while synchronizing central manifests and evidence;
  final central coordination workflow `30015232878` passed. No merge or stable release promotion
  was performed.

## 2026-07-23 — Linux provider health persistence

Assumption: Linux remains the active client priority; provider health metadata is non-secret local
state, while other clients and stable-release conditions remain deferred.

- [x] Push Core `460728d79b0e2373445c3d8994793d069b8057b9` with schema-34 profile health fields,
  normalized failure categories, and round-trip storage tests.
- [x] Push Linux code `fb9b1e6c9bb3703ade5c4b8e4c1993f716d3126c` with explicit connection-test health
  recording, saved-profile refresh, restart coverage, and Core compatibility feature
  `provider_health_status_v1`; Flatpak packaging `4784764b50b4362833e26a1e88b3792a811ae768`
  points to the health-aware Core and Linux inputs.
- [x] Pass local Core workspace tests and Linux `cargo test --lib --all-features` (163 passed,
  12 documented environment-gated ignores). Push Native/Flatpak/Foundation
  `30010795356`/`30010795221`/`30010795318` and PR Native/Flatpak/Foundation
  `30010798544`/`30010798478`/`30010798760` passed; release stays `unreleased`.

## 2026-07-23 — Linux release-document pin alignment

Assumption: release documentation must match the exact Linux/l10n pins used by the green workflows;
this follow-up changes no functional release pin and keeps the train `unreleased`.

- [x] Correct Linux `docs/releasing.md` at `99ae05daa82d8317b4fcf7f6de792d10d349d3bc` to the
  497-message l10n revision `7c2cb9fd71835ea0f9c6605d82dac87c0df012f0`, Linux code head
  `00186c29fc4e3e6682114ee29cd587d31610a1d6`, and packaging pin `73051b70028359c56654e1260621ada77def67e9`.
- [x] Pass local diff, Flatpak metadata, l10n synchronization, and formatting checks.
- [x] Confirm Push/PR Native, Flatpak, and Foundation runs
  `30008592951`/`30008592908`/`30008592945` and
  `30008596468`/`30008596531`/`30008596470` all passed.
- [x] Refresh the Linux PR and central Issue descriptions without merging, closing, signing, or
  promoting a stable release.

## 2026-07-23 — Linux model provenance labels

Assumption: Linux remains the active client priority; the existing Core `ModelSource` contract is
the source of truth for selector provenance, while other-client and human-review requirements
remain open.

- [x] Audit Core's existing `Discovered`, `Catalog`, and `Manual` model-source contract and add
  localized source labels to all 12 l10n packs (`7c2cb9fd71835ea0f9c6605d82dac87c0df012f0`,
  497 messages).
- [x] Render the source beside every GTK model entry, add the regression test, and repin Linux
  packaging (`00186c29fc4e3e6682114ee29cd587d31610a1d6`, pin `73051b70028359c56654e1260621ada77def67e9`).
- [x] Pass local Linux/l10n validation and all six Linux push/PR gates:
  `30006418545`/`30006418485`/`30006418554` and
  `30006415855`/`30006415873`/`30006415861`.
- [x] Synchronize central status, gap analysis, and release pins; retain `unreleased` until
  cross-client parity, manual/physical evidence, signing, rollback, and authorization exist.

## 2026-07-23 — Linux model-provenance documentation head

Assumption: this is a documentation-only follow-up; the functional Linux pin remains the
verified packaging commit and no release artifact is promoted.

- [x] Synchronize Linux `IMPLEMENTATION_STATUS.md`, `README.md`, and `docs/architecture.md` at
  documentation head `99c5c5e` with the model-source labels and l10n revision `7c2cb9f`.
- [x] Re-run local Linux synchronization, formatting, library tests, Clippy, GUI cargo check,
  localization audits, Flatpak metadata, and diff checks.
- [x] Confirm all six Linux Push/PR Native, Flatpak, and Foundation gates passed:
  `30007622306`/`30007622052`/`30007622063` and
  `30007624889`/`30007624904`/`30007625187`.
- [x] Keep the PR Draft/Open, issue Open, and release status `unreleased` while cross-client,
  human/physical, signing, rollback, and stable authorization evidence remains incomplete.

## 2026-07-23 — Linux/Core bounded TBX glossary import

Assumption: Linux remains the active client priority; a restricted TBX parser and native chooser
path are sufficient for this slice, while other-client parity and physical evidence remain open.

- [x] Add Core's bounded UTF-8 TBX import contract with deterministic language mapping, locale/note
  preservation, XML entity decoding, DTD/entity rejection, conflict validation, and focused tests.
- [x] Wire Linux GTK CSV/TBX filters and extension-based dispatch, synchronize revision-62
  localization resources, update docs/status, and repin Native/Flatpak inputs.
- [x] Push Core `dffa07eca2b006279f99673edff5bd0ae1b24a0f`, localization
  `d8d9084cdf0448039ad0aa7612e8725c6c875036`, and Linux `d61a96f`; central manifests now match
  these heads.
- [x] Obtain remote Linux gate evidence for this new head: push Native/Flatpak/Foundation
  `30004896060`/`30004896007`/`30004896045` and PR Native/Flatpak/Foundation
  `30004893289`/`30004893240`/`30004893064` all passed. Keep the release train `unreleased` until
  all global acceptance and authorization conditions exist.

## 2026-07-23 — Current pinned regression rerun

Assumption: this checkpoint only refreshes reproducible evidence; it does not change the functional
release pins or promote prerelease work.

- [x] Re-run the current pinned Core, Linux, localization, and central validation. Core
  `53eee86ce0862bcb0b86f86da5e91257b07fe6d7` passed the locked workspace tests (226 passed, no
  failures or ignored tests) and strict Clippy. Linux status head
  `3eb710ee35c6aa626714a4c8618e37cc831661c3` passed the demo-provider library suite (160 passed,
  3 environment-gated ignored), and localization `1de68c9568b5c380845089efc9282ff6edd04bc1`
  passed `make check` with 494 messages and 26 tests. Central workspace validation and diff checks
  passed, and coordination workflow `30002603575` passed on Linux and PowerShell; release remains
  `unreleased`.

## 2026-07-23 — Linux regional-locale and script translation presets

Assumption: the existing GTK translation-preset selector is the smallest complete Linux surface
for Core's bounded regional-locale and script preferences; cross-client parity remains open.

- [x] Add Core `english_us` (`en-US`/`Latn`) and `chinese_simplified` (`zh-CN`/`Hans`) presets
  at `53eee86ce0862bcb0b86f86da5e91257b07fe6d7`, with domain validation and round-trip tests.
- [x] Expose both choices in Linux GTK at `52a9eb7fc579fff07627c55d7ce0f49eac5048ad`, sync
  localization `1de68c9568b5c380845089efc9282ff6edd04bc1` (494 messages), and repin Native and
  Flatpak inputs. Local 160-test/3-ignore suite, strict Clippy, l10n checks, synchronization,
  Flatpak metadata, and diff checks passed. Core CI/Fuzz/Native SDK
  `30000596855`/`30000596731`/`30000596716`, l10n Localization/Foundation
  `30000492370`/`30000492390`, Linux push/PR Native/Flatpak/Foundation
  `30000751775`/`30000751755`/`30000751799` and `30000748043`/`30000747816`/`30000747915`, and
  central coordination `30000926993` all passed.
- [ ] Add equivalent regional/script controls to Android, Windows, and macOS before stable
  release; retain explicit human translation and accessibility review boundaries.

## 2026-07-23 — Linux GTK glossary-library selector checkpoint

Assumption: the request-level glossary editor remains authoritative; the new GTK selector is a
bounded Linux client surface over Core schema 33, and TBX/cross-client parity remain separate work.

- [x] Complete the Linux glossary-library UI and localization slice. Core is pinned to
  `1bd150b3063b6471dbf8a279db1fccb03d2c916c`; Linux UI/worker `cb17d52254db03614929db38228c5f482716f6c0`,
  packaging head `e21629584394fb313c8af8bc95d1fb6ddf885508`, and l10n `c4173bf52a5f44ebcf387de2d5dc6fcccc07338e`
  (492 messages). Local Linux tests (`160 passed; 3 ignored`), strict Clippy, l10n `make check`,
  synchronization, and Flatpak metadata passed. Final push/PR Native, Flatpak, and Foundation
  gates `29999190331`/`29999193186`/`29999193181` and `29999190239`/`29999193188`/`29999190245`
  passed. TBX import, other clients, human accessibility review, signing, rollback, and stable
  release remain open; release stays `unreleased`.

## Progress

- [x] Implement and verify Linux-first normalized usage-record persistence. Core `e48d1040a992b2fd3daaa27af2ae6bd700b25fc5`
  adds schema 32 and atomic history/usage cleanup with endpoint and credential redaction; Linux
  `064a6f17e37030351ef27a7bb047db2910167fe3` wires provider-reported and local-estimate records,
  Incognito, history policy, deletion, and restart coverage. Core CI/Fuzz/Native SDK
  `29992377731`/`29992376984`/`29992377385` and Linux push/PR Native, Flatpak, Foundation
  `29992795496`/`29992795837`/`29992795547` and `29992800736`/`29992800675`/`29992800292` passed.
  Other clients, live accounting, human review, signing, rollback, and stable release remain open.

- [x] Implement and verify the Linux-first persistent glossary-library slice. Core
  `1bd150b3063b6471dbf8a279db1fccb03d2c916c` adds schema 33 normalized `glossaries` and
  `glossary_terms` storage with bounded IDs, atomic replacement, revalidated reads, and cascading
  deletion. Linux `cc74e61` adds worker save/list/delete commands and restart/delete coverage;
  packaging/status head `35fea77` aligns the Flatpak source pin. Core CI/Fuzz/Native SDK
  `29995295648`/`29995295576`/`29995295577` and Linux Push/PR Native, Flatpak, Foundation
  `29996102525`/`29996102475`/`29996102477` and `29996105093`/`29996105285`/`29996105371`
  passed. GTK library selection, TBX import, other clients, signing, rollback, and stable release
  remain open.

- [x] Refresh the Linux usage-persistence documentation head. Linux `c4966caa37213225c52e7b0ee8a357c5e85becd7`
  passed push Native/Flatpak/Foundation `29993630277`/`29993630247`/`29993631103` and PR
  `29993633187`/`29993633058`/`29993633663`; all six PR checks pass and the functional release pin
  remains `064a6f17e37030351ef27a7bb047db2910167fe3`.

- [x] Refresh the Linux PR documentation-head gate record. Linux status head `90a2753` was
  pushed after the prior propagation-lag observation; PR Native `29990141179` and Repository
  Foundation `29990141145` passed, while PR Flatpak `29990141186` completed build, checksum,
  SBOM, sandbox-smoke, and cleanup steps with its check-run aggregation still `in_progress`.
  The PR remains Draft/Open and the release remains `unreleased`; no merge or promotion was
  performed.

- [x] Complete the Linux status-head gate refresh for `90a2753`. Push Native/Flatpak/Foundation
  `29990602946`/`29990602971`/`29990602947` and PR Native/Flatpak/Foundation
  `29990604854`/`29990604856`/`29990604877` completed successfully. The PR remains Draft/Open;
  no merge or release promotion was performed while GitHub check aggregation propagated.

- [x] Re-run the exact current Core/Linux regression gates before advancing the active goal. Core
  `2f91f313025b189df237294485fd47bafc1f1f53` passed
  `cargo test --workspace --locked --all-targets` with 222 passing tests and no failures or
  ignored tests; Linux `dffc87f4e1499ce7adcc803123db4dfdac4eec1e` passed the no-default library
  suite with 83 passed and 1 environment-gated OCR test ignored. Central `bash
  tools/check-workspace.sh` and `git diff --check` passed. Earlier 227-test evidence is retained as
  historical checkpoint data; no functional pin or release-manifest value changed.

- [x] Re-run the current Linux `demo-provider` library suite after the documentation checkpoint.
  Linux status head `40091f78f1aca3b13f1f8efda11d359e00fe97ae` passed 159 tests with 3 explicit
  environment-gated ignores and no failures; Native/Flatpak/Foundation workflow dispatch runs
  `29988891946`/`29988892002`/`29988891951` all passed. This is portable Linux evidence only; no
  stable or cross-client claim is made. The automatic push gates passed after a transient Flathub
  fetch retry (`29989088159`/`29989088223`/`29989088163`); PR Native/Foundation passed
  (`29989286385`/`29989286425`), while the PR Flatpak run `29989286410` completed successfully
  with check aggregation still awaiting GitHub propagation at record time.

- [x] Refresh the Linux/Core crash-recovery evidence at the approved heads. Core
  `2f91f313025b189df237294485fd47bafc1f1f53` passed the focused WAL child-abort regression and the
  locked workspace suite (`227 passed`); Linux runtime `04478701e3b0192cc7f90228c47badd9f6bb2d2b`
  and current documentation/status head `dffc87f4e1499ce7adcc803123db4dfdac4eec1e` passed
  `cargo test --no-default-features --lib` (`83 passed; 1 ignored`), formatting, GUI check, strict
  Clippy, cargo-deny policy, l10n synchronization/audits, Flatpak metadata validation, and the
  explicit image-only PDF OCR fixture (`bash tools/run-ocr-test.sh`, `1 passed`) plus the private
  mount ENOSPC regression (`bash tools/run-storage-fault-test.sh`, `1 passed`). Push Native/Flatpak/
  Foundation `29987023670`/`29987023696`/`29987023655` and PR
  `29987026057`/`29987026021`/`29987026006` all passed. A temporary host-network
  `ollama/ollama:0.11.10` daemon with `smollm:135m` also passed the real third-party `/api` regression
  once without credentials. This is controlled process-crash/OCR/storage-fault/provider evidence,
  not physical power-loss or alternate-VFS evidence; the release remains `unreleased`.

- [x] Record the verified Linux GTK candidate-chain editor and one-shot fallback-consent
  lifecycle. Documentation head `04478701e3b0192cc7f90228c47badd9f6bb2d2b` is covered by passing
  push Native/Flatpak/Foundation runs `29984727975`/`29984727998`/`29984727932` and PR runs
  `29984730138`/`29984730127`/`29984730117`; the production fixture reports one passing
  candidate-chain fixture and one passing fallback-approval fixture. This closes only the Linux
  deterministic UI evidence gap; cross-client parity, live providers, human review, signing,
  rollback, and stable release remain open.

- [x] Add Linux production GTK Anthropic Messages protocol-preset transport evidence. Core
  `2f91f313025b189df237294485fd47bafc1f1f53` adds the deterministic `/v1/messages` testkit route
  with `x-api-key`, usage, fragmented content, and `message_stop` events. Linux implementation
  `2f12c7482a4d0376bbdd7ea86fd7f25557fea75f` drives Anthropic, Gemini, and Azure through the real
  GTK lifecycle; packaging head `0a77a14d35fad42d66c812398827b2ca50edb51c` and status head
  `b218c814c21b6e6a2f4ad691b5f6f09bf33d7bc0` pin and document the final state. Core CI/Fuzz/Native
  SDK `29982822450`/`29982822441`/`29982822462` and Linux push/PR Native, Flatpak, Foundation
  `29983438263`/`29983438252`/`29983438279` and `29983440294`/`29983440326`/`29983440348` passed.
  Live Anthropic interoperability, other clients, human review, signing, rollback, and stable
  release remain open.

- [x] Add Linux production GTK Gemini/Azure protocol-preset transport evidence. Linux
  implementation `8006f7a37b81db7c547be717b72860ee610ca7d7` drives both native GTK presets
  through real Gemini `/v1beta/` and Azure resource-path handlers, deliberate model selection,
  credential clearing, and streamed translation with deterministic loopback providers. Final
  packaging head `5f1634c615f9e1a7ca3de8e37a99e4efc1f02b9e` repins the Flatpak source; Linux
  status head `d0e188f1018dc2f004edf2b1332469625c876913` records the final gates.
  Local format, GUI source check, strict Clippy, core-library tests (`83 passed; 1 ignored`), and
  diff checks passed; the full GTK link is unavailable on this host. Push Native/Flatpak/Foundation
  `29981441794`/`29981441765`/`29981441767` and PR `29981443146`/`29981443162`/`29981443177` all
  passed. Live provider account/quota/deployment behavior, other clients, human review, signing,
  rollback, and stable release remain open.

- [x] Add Linux production GTK evidence for the one-click provider switch. Linux `988be0c` adds
  the serialized A→B session switch fixture and Native workflow step; it proves selection alone
  performs no inference, the active provider remains unchanged until B validates, B receives the
  next request, A receives no extra request, and both one-shot credential fields are cleared. Push
  Native/Flatpak/Foundation `29980182737`/`29980182712`/`29980182800` and PR
  `29980184753`/`29980184796`/`29980184751` passed. Linux Scenario 5 is now deterministic evidence;
  global completion still requires equivalent evidence on the other native clients.

- [x] Complete in-scope privacy and changelog documentation for Core, l10n, and Linux. Core
  `5a5a4cb89985083d02aac9d9aa226184992f3774`, l10n `538a15f7917f991b4995d3675f3becba1b5008e2`,
  and Linux `0ffb1c1132bbff9534f54354e0e71230963363d0` add the required policy files without
  changing runtime behavior. Core CI/Fuzz/Native SDK `29979348220`/`29979348138`/`29979348170`,
  l10n `29979357957`/`29979357930`, and Linux push/PR gates
  `29979370911`/`29979370877`/`29979370915` and `29979372688`/`29979372682`/`29979372622`
  passed. Android and Windows policy files remain deferred under the explicit Linux-first scope.

- [x] Add and pin the Linux-first client-certificate TLS identity SecretRef slice. Core
  `2a3534faa9a2531cbbc6cc06d325ad7c82c69394` adds schema 31, bounded/redacted combined PEM
  identity parsing, persistent/session SecretRef resolution, and rustls identity wiring across
  all built-in adapters. l10n `552d87e88a8df42055b1ac76e4dfbaadca92e291` supplies source revision 59
  and 480 generated messages. Linux implementation `b4bd13c1ec778e62ef466b7fa9d106de87731f29`
  adds the masked GTK field, immediate clearing, Secret Service/session handling, restore
  behavior, and exact Flatpak/source pins. Local Core/Linux/l10n/Flatpak checks passed; Core
  CI/Fuzz/Native SDK `29978060455`/`29978060459`/`29978060500`, l10n `29977582751`/`29977582767`,
  and Linux implementation push/PR Native/Flatpak/Foundation gates
  `29978367171`/`29978367181`/`29978367167` and `29978368905`/`29978368870`/`29978368862`
  passed. Final status head `bf5398de6b747841d779b72a9ac51752a19047ef` passed push/PR gates
  `29978696500`/`29978696556`/`29978696510` and `29978698516`/`29978698538`/`29978698523`.
  Central coordination `dfcecee8fde665d1cc6e4d9f0d2b1681072e100f`/`29978472198` passed. Other clients, live-provider
  interoperability, manual review, signing, rollback, and stable release remain open.

- [x] Add and pin the Linux-first proxy-authentication SecretRef slice. Core
  `cee5bd8abc5b35a50640c484bc4fbeedeb426745` adds schema 30, bounded/redacted proxy credential
  parsing, storage rejection of session references, and proxy Basic-auth forwarding across the
  built-in adapters. l10n `f0b1c507d73f540f298a534303d0e6e63d44e87b` supplies the source-revision-58
  Linux strings and generated resources. Linux `34b3194c5445f640141de8ad57195768aaa6c3d0` adds
  the masked GTK field, immediate clearing, session/Secret Service handling, localization sync,
  and exact Core/l10n/Flatpak pins. Local Core/Linux/l10n/Flatpak checks passed. Linux push
  Native/Flatpak/Foundation `29976201970`/`29976201964`/`29976201962` and PR
  Native/Flatpak/Foundation `29976204361`/`29976204358`/`29976204331` passed for the exact final
  documentation head. Other clients, live-provider interoperability, human review, signing,
  rollback, and stable release remain open.

- [x] Add and pin the Linux-first bounded custom trusted-certificate bundle slice. Core
  `913be49da8bc44f9c53baab7b918f2bb002fd64f` adds schema 29 persistence, PEM validation, and
  additive reqwest root-certificate wiring across OpenAI Chat/Responses/Azure, Anthropic, Gemini,
  and Ollama without disabling TLS verification. l10n `d315efe808e05ce2fb0ee24c0247076298d57947`
  supplies the 474-message bundle. Linux `e8f0bcf2c55032cae59f40dba505c6e66a2fdd89` adds the
  GTK field, restore/default behavior, Test connection/Connect forwarding, and exact source pins.
  Local Core/Linux/l10n/Flatpak checks passed; full-feature GTK linking is host-limited by missing
  GTK symbols. Core CI/Fuzz/Native SDK `29973111006`/`29973111045`/`29973111016`, l10n
  Localization/Foundation `29972855206`/`29972855181`, and Linux push Native/Flatpak/Foundation
  `29973126765`/`29973126853`/`29973126883` plus PR
  `29973129042`/`29973129135`/`29973129087` passed. Central coordination commit `b431d626ca3ce04b6d06f65d2e2d8973e7c65708`
  and run `29973194356` passed. Client certificates, proxy authentication, cross-client parity,
  review, signing, rollback, and stable release remain open.

- [x] Add and pin the Linux-first bounded provider streaming-idle timeout slice. Core
  `b247155ad429639fdb65d3b063c3efc580ce46a4` adds schema 28 persistence, 1–300 second validation,
  per-chunk timeout handling, and typed timeout coverage across OpenAI Chat/Responses/Azure,
  Anthropic, Gemini, and Ollama. l10n `2e223f9a416f4b461b72224f12c31cbf7981dae3` supplies the
  471-message bundle. Linux `c9d9a518103e370d4b21343cbe2e46dcd976422d` adds the GTK control,
  restore/default behavior, exact Core/l10n/Flatpak pins, and release documentation. Local Core,
  Linux, l10n, synchronization, and Flatpak checks passed. Linux push Native/Flatpak/Foundation
  `29971755022`/`29971755009`/`29971755012` and PR `29971756513`/`29971756522`/`29971756554` passed
  for final head `24b69a646a9463b13710502ce35a1bd0d15ee427`. TLS policy, cross-client parity, human
  review, signing, rollback, and stable release remain open.

- [x] Add and pin the Linux-first bounded provider connection-establishment timeout slice. Core
  `e9a569f8bb6d66db4fdb1c9bd1d6834e93d10f39` adds schema 27 persistence, 1–120 second validation,
  and independent transport wiring across OpenAI Chat/Responses/Azure, Anthropic, Gemini, and
  Ollama. l10n `46ca70b2863fa951b417eda7ce5848e152c46605` supplies the 469-message bundle. Linux
  `6fbf53da024bd37d64f93025222a57f7b0296d47` adds the GTK control and exact Core/l10n/Flatpak pins.
  Local Core/Linux/l10n/Flatpak checks passed. Core CI/Fuzz/Native SDK
  `29969609373`/`29969609372`/`29969609379`, l10n Localization/Foundation
  `29969625867`/`29969625942`, and Linux push/PR Native/Flatpak/Foundation
  `29970072910`/`29970072901`/`29970072923` and `29970070485`/`29970070480`/`29970070516` passed.
  Streaming-idle/TLS policy, cross-client parity, human review, signing, rollback, and stable
  release remain open.

- [x] Add and pin the Linux-first bounded total provider request timeout slice. Core
  `7e78cb0086d85eb5c218d8863b7f11f506bae016` adds schema 26 persistence, 1–600 second validation,
  and transport wiring across OpenAI Chat/Responses/Azure, Anthropic, Gemini, and Ollama. l10n
  `65bf0c8772f75649b2be2e2f9cea610772657c93` supplies the 467-message bundle. Linux
  `c5db93676128e84a577f628906aad2980f919909` adds the GTK control and exact Core/l10n/Flatpak pins.
  Local Core/Linux/l10n/Flatpak checks passed. Linux push Native/Flatpak/Foundation
  `29968376701`/`29968376654`/`29968376661` and PR
  `29968379682`/`29968379660`/`29968379655` passed for the exact head. Connection/idle/TLS
  timeout fields, cross-client parity, human review, signing, rollback, and stable release remain
  open.

- [x] Implement the Linux-first bounded provider proxy settings slice. Core
  `7a9da3f467c5dec539dd8f7850b90b54ae712331` adds schema 25 persistence and applies validated
  HTTP/HTTPS/SOCKS5/SOCKS5H URLs to all four provider transport families; l10n
  `bba90a89089c954bdfe1dcda19c210e6ea230b9e` adds the 465-message bundle; Linux
  `c03535f82f07ed10c273fb250654c984540ed935` adds GTK onboarding and exact source pins. Local
  Core/Linux/l10n/Flatpak checks passed. Core CI/Fuzz/Native SDK
  `29966758398`/`29966758388`/`29966758389` and Linux push Native/Flatpak/Foundation
  `29966869662`/`29966869643`/`29966869658` plus PR
  `29966872082`/`29966872046`/`29966872048` all passed. Proxy auth, cross-client parity, manual
  review, signing, rollback, and stable release remain open.

- [x] Complete the Linux secret custom-header GTK onboarding slice. l10n
  `32397a72c267677f04419a5084514f025f94a0bc` adds the three Linux messages and regenerates the
  462-message bundle. Linux `e52a43cb361c5a395aa4e8ecd4d8d5252192d384` adds masked input,
  immediate clearing, persistent Secret Service storage, session-only WorkerCommand transport,
  l10n/Flatpak pins, and a Core-validation regression for malformed session headers. Local Linux,
  l10n, localization, Flatpak, and diff checks passed; remote gate IDs follow in the implementation
  record. Other clients, human review, signing, rollback, and stable release remain open.

- [x] Verify and record the Linux-first secret custom-header SecretRef slice. Core
  `28baaa2f85bb70b4fc6ecc4c07566e7004a659c5` adds schema 24 persistence and host-broker-backed
  in-memory application for OpenAI-compatible Chat/Responses/Azure; Linux
  `9d0ffc10a5ee9dd114e40b95db277679969d2593` preserves and cleans up persistent references.
  Local Core/Linux validation passed; Core remote runs `29963034872`/`29963034867`/`29963034863`,
  Linux push/PR runs `29963506897`/`29963506924`/`29963506877` and
  `29963509821`/`29963509808`/`29963509782`, and central coordination `29963944562` passed.
  The second GTK editor/onboarding regression is now covered by Linux runtime test
  `f6cdb44dd6e411c2fab1c9f39cd3cd63361a1352` and final status head
  `e9b7d80e3ecac045eeb10b37ea59871c0ada6198`; push/PR Native, Flatpak, and Foundation gates
  `30039406785`/`30039406821`/`30039406753` and `30039409345`/`30039409381`/`30039409339`
  passed. Cross-client support, human review, signing, rollback, and stable release remain open.

- [x] Add the cross-repository completion gap audit in [`docs/GAP_ANALYSIS.md`](docs/GAP_ANALYSIS.md),
  mapping Milestones 0–8 and all 20 mandatory scenarios to current evidence. The audit preserves
  the Linux-first scope and records cross-client, manual, physical, signing, rollback, and stable
  release work as explicitly incomplete rather than inferring completion from Linux fixtures.

- [x] Project bounded non-secret provider metadata through ABI 1 and repin Linux. Core
  `530e6ea75ef3ccba5defd264227fb6dd6802e17a` adds optional organization/project/custom-header
  command fields with fail-closed validation, Android wrapper parameters, FFI forwarding, and
  regression coverage. Linux `5cf0fcd133c7df823d4c33f934786a1c940670bb` pins the exact Core
  revision. Core CI/Fuzz/Native SDK `29961301539`/`29961301501`/`29961301583` and Linux push/PR
  Native/Flatpak/Foundation `29961456792`/`29961456832`/`29961456791` and
  `29961459180`/`29961459196`/`29961459185` passed; release remains `unreleased`.

- [x] Close and record the Linux Azure OpenAI custom-header application wiring gap. Core
  `cf08384c829ca1b95ecfc79d23bc5b0feb3a701f` adds `AzureOpenAiConfig.custom_headers` and forwards
  the persisted bounded value through `ProviderManager` without replacing Azure `api-key`.
  Provider/application loopback regressions, Core workspace tests, strict Clippy, and Linux local
  GUI/demo-provider/localization/Flatpak checks passed. Linux `61a7317746adea35f35a88f948a94f7e8223bac1`
  pins the new Core revision; Core CI/Fuzz/Native SDK `29958775964`/`29958776018`/`29958776042`,
  Linux push/PR Native/Flatpak/Foundation `29959014144`/`29959014132`/`29959014154` and
  `29959016415`/`29959016426`/`29959016416`, and central coordination `29959537603` passed.
  Release remains `unreleased`.

- [x] Add and remotely verify the Linux-first bounded custom provider-header slice. Core
  `be5b7220587289be78b7654d979099c57ea4cc6d` adds schema 23 persistence, canonical bounded
  non-secret header validation, and OpenAI Chat/Responses application with reserved-header and
  credential-shape rejection. l10n `294e593ab2c71b9ab0ea3475c35ebc61bca2bbc6` adds the three
  Linux messages at source revision 51 (459 messages). Linux `1e3a96b18990ea4f7b8ba85faed2df4407ed18b9`
  binds/restores/clears the GTK field, synchronizes PO/MO resources, and pins Core/l10n/Flatpak.
  Local Core, Linux, l10n, localization, Flatpak, and diff validation passed. Core CI/Fuzz/Native
  SDK runs `29956720294`/`29956720284`/`29956720340`, l10n Localization/Foundation runs
  `29956431231`/`29956431233`, and Linux push Native/Flatpak/Foundation runs
  `29956837428`/`29956837112`/`29956837081` plus PR runs
  `29956840773`/`29956840966`/`29956840730` all passed. Central coordination workflow
  `29957596432` also passed; release remains `unreleased`.

- [x] Close and remotely verify the Linux provider-project application wiring gap. Core
  `8717251375290cc3f825cee86d467ab1c60dd508` now forwards the persisted project value into both
  OpenAI Chat and Responses adapters, with header-enforced application regressions and full
  workspace validation passing locally. Linux code head `69b2d4510c51e9f34d7807687e6536ec411b1611`
  and final status head `ec4b32d7dd0efd6d00d27d3a60750307b9c6ff31` passed all six Native/Flatpak/
  Foundation push/PR gates (`29954097684`/`29954097694`/`29954097748` and
  `29954100960`/`29954102119`/`29954100976`). Release remains `unreleased`.

- [x] Add the Linux-first ProviderProfile notes slice to the central compatibility record after
  remote Linux gates complete. Core `072d6b92df875153a60a9d1256ab814891fe775b`, Linux runtime/
  packaging `eaa9dc3e6bf07222fe3b2da5c078d39e9419b88d`, final status `3c1a4ad5e9f8d8ae613c5b2f8aa447d057212de0`,
  and l10n `6aa074e48058bb411d09b2783cd27ba415dc7c55` are published; Core/l10n CI and all six
  Linux Native/Flatpak/Foundation push/PR gates passed.

- [x] Add the Linux-first ProviderProfile organization slice. Core `1b8737bbad3d1bb6df7cd5c852d51838f72b9ca1`
  persists bounded non-secret `organization` metadata in schema 20 and sends it only as the
  `OpenAI-Organization` header for Chat/Responses; Linux/l10n head `88114a7a08e814e6b75ee0fe0a5814573104fd08`/
  `94438a6a9ff8148cadad605c4760f88110d78984` binds the GTK field and 447-message catalog. Final
  Linux push Native/Flatpak/Foundation `29946828234`/`29946829779`/`29946829000` and PR
  `29946831489`/`29946831590`/`29946832071` passed; PR #1 remains Draft/Open and the release train
  remains `unreleased`.

- [x] Add and remotely verify the Linux-first ProviderProfile project slice. Core
  `17342ba0bf19dd4978707a7875bc7dbe85efae54` persists bounded non-secret `project` metadata in
  schema 21 and sends it only as the `OpenAI-Project` header for Chat/Responses; l10n
  `fea84439f035f30b009532b40d7f67a30049846c` adds the three Linux form messages (450-message
  bundle), and Linux status head `108cba3e5b1cb128cf77003fc0cb530e822bd7f7` binds the field,
  runtime copies, and exact Core/l10n/Flatpak pins. Local checks passed; Core CI/Fuzz/Native SDK,
  l10n Localization/Foundation, and Linux push/PR Native/Flatpak/Foundation gates all passed:
  `29949462141`/`29949462126`/`29949462107` and `29949468527`/`29949466704`/`29949468689`.
  Release remains `unreleased`.

- [x] Add and remotely verify the Linux-first ProviderProfile region/account metadata slice. Core
  `158ade12cf1e3284d4b8a0883e771dd62abcff97` adds schema 22 bounded non-secret fields and storage
  tests; l10n `ec538de57c1edc198fa13d3dfc1de576ee9b2c12` adds six Linux messages (456-message
  bundle); Linux runtime/packaging head `761a931538fc49c30d759089185cdf21cf2015ab` and status head
  `69fb128` bind/restore/clear both fields and pin the exact inputs. Local checks passed; Linux
  push Native/Flatpak/Foundation `29952240768`/`29952240852`/`29952240819` and PR
  `29952245004`/`29952244151`/`29952244148` passed. The earlier stale-pin Flatpak runs
  `29951517923`/`29951520086` were superseded. Release remains `unreleased`.

- [x] Add the Linux About compatibility dialog and final CI evidence. Runtime/packaging head
  `0d7b3927fb98e461317feaefeb4c806676e6acc0`, l10n `a65a327a8418332e50d9ab302fca24508e7266ef`,
  and final status head `b71e209` passed local Linux checks plus push Native/Flatpak/Foundation
  `29939876568`/`29939877021`/`29939876501` and PR
  `29939879474`/`29939879969`/`29939879856`. The localized read-only dialog exposes only app
  version and Core semantic version/ABI/protocol compatibility. The l10n-pin, GTK mnemonic, and
  stale Flatpak pin failures are recorded as superseded; PR #1 remains Draft/Open and release
  status is `unreleased`.

- [x] Refresh the Linux current-head regression evidence after the approved-fallback checkpoint.
  Linux runtime/packaging head `4154aaef160a0578624f581063dbd62a29cadb79` and status head
  `3ef694d97caab7de8f98eac177d77ed29fe2a40c` passed local formatting, GUI
  all-target checks, locked offline demo-provider tests (`158 passed; 3 ignored`), strict Clippy,
  l10n synchronization, Flatpak metadata, and diff checks. Push Native/Flatpak/Foundation
  `29935017464`/`29935017253`/`29935017458` and PR `29935021969`/`29935020280`/`29935020571` all
  passed. PR #1 remains Draft/Open and Issue #1 remains Open; the release train stays `unreleased`.

- [x] Add explicit Linux evidence for LM Studio-style generic OpenAI compatibility. Runtime
  `74e817f07b5d386706999fdc66a21a357286af6c` adds the deterministic `/v1/` fixture; packaging/status
  head `4154aaef160a0578624f581063dbd62a29cadb79` pins Flatpak and documents the protocol boundary.
  Push Native/Flatpak/Foundation `29930209615`/`29930209070`/`29930209231` and PR
  `29930217543`/`29930215088`/`29930217498` all passed. PR #1 remains Draft/Open and Issue #1
  remains Open; central synchronization `78f4724e6ccd976ded93765723013f02d8d4f847` passed
  workflow `29930966325`; the release train stays `unreleased`.

- [x] Add the Linux bundled open-source license-notices surface. Runtime `909083dee4c436d0f343785a4c95f1cda4207e35`
  adds a catalog-backed action and read-only focusable GTK dialog over `THIRD_PARTY_NOTICES.md`; l10n
  `3724cc9d436ebdbac3b8ebf0df9bce9af1b41b15` adds the action/dialog/tooltip labels. Status/packaging
  head `c2c1f24c872fdc7a314986376e399ce24788df68` records the corrected full Flatpak pin and local
  validation. Final push Native/Flatpak/Foundation `29928729926`/`29928727256`/`29928727822` and
  PR `29928731491`/`29928731735`/`29928730487` all passed. PR #1 remains Draft/Open and Issue #1
  remains Open; central synchronization commit `c9495526d46af65cd800cacd47883a6abd69f017` passed
  coordination workflow `29929324598` on Linux and PowerShell; release status stays `unreleased`.

- [x] Triage the Linux pull request and coordination issue. On 2026-07-22, Linux PR #1 had no
  submitted reviews, change requests, or unresolved threads; all six current-head Native, Flatpak,
  and Foundation push/PR checks passed. The PR remains Draft/Open and mergeable. Central Issue #1
  remains Open for manual desktop approval/review, physical VFS and power-loss coverage,
  cross-client work, signing, rollback authorization, and stable-release evidence. Triage comments
  are recorded on the PR and issue; coordination workflow `29905044867` passed Linux and
  PowerShell validation; no merge or release action was taken.

- [x] Verify Linux prerelease checksum and SBOM evidence before artifact upload. Workflow head
  `48ccbca9523fb4c633e3d806c23104c34b5fa623` adds Native and Flatpak upload gates that re-check all
  `SHA256SUMS` entries and parse SPDX JSON; the Native source archive checksum is normalized to the
  evidence directory. Documentation/status head `3bd2c7a0b9cae2e7de55b700e7863b9fcf3805ff` records
  the correction. The first two Native path attempts failed honestly (`29902104277`/`29902106668`);
  final push Native/Flatpak/Foundation `29903015347`/`29903015532`/`29903015352` and PR
  `29903018444`/`29903018422`/`29903018395` all passed. Artifacts remain unsigned prerelease
  evidence; PR #1 remains Draft/Open and Issue #1 remains Open.

- [x] Strengthen Linux document-report body redaction evidence. Runtime regression commit
  `89de426c6fcfce77a395fc066017c01a5bb7c247` explicitly asserts that translated and pending source
  segment bodies do not appear in the report, alongside the deterministic local usage JSON check.
  Packaging/docs head `b50a69a61436535e196e2d8f5c997f491e726c74` pins that tested source and records
  the contract. Local formatting, locked all-target/all-feature checks, strict Clippy, localization
  audits, Flatpak metadata, and diff checks passed. Push Native/Flatpak/Foundation
  `29901156887`/`29901156926`/`29901156939` and PR `29901160007`/`29901159988`/`29901160074` all
  passed; Native completed the full GTK, accessibility, release, checksum/SBOM, and performance
  suites. PR #1 remains Draft/Open and Issue #1 remains Open; release status is `unreleased`.

- [x] Add non-sensitive Linux document-report usage estimation. Runtime
  `ae4750beec1d9aa1c2d53c96754a6ca5a4e55c66` derives bounded local token estimates from persisted
  source/translated segments and serializes only usage metadata; `retried_count` remains explicit
  `unknown` because attempt history is not persisted. Packaging/docs head `130dc051e61250ff6c029afedb490f4eea4863b9`
  pins the runtime and records the redacted report contract. Local formatting, locked all-target/all-
  feature checks, strict Clippy, localization audits, Flatpak metadata, and diff checks passed.
  Push Native/Flatpak/Foundation `29899915398`/`29899915416`/`29899915427` and PR
  `29899917681`/`29899917650`/`29899917663` all passed; Native completed the full GTK, accessibility,
  release, checksum/SBOM, and performance suites. PR #1 remains Draft/Open and Issue #1 remains
  Open; release status is `unreleased`.

- [x] Strengthen Linux Scenario 18 source preservation for non-local URIs. Runtime
  `dc5304c679feedce407981ea67d832979d81157e` adds
  `non_local_source_alias_is_rejected_by_uri_identity`, proving the production export guard rejects
  an identical SMB URI and allows a distinct sibling URI without relying on local inode checks.
  Packaging/docs head `6de5e2eb89e493c770376e6c55721f429024f651` pins the runtime and records the
  remote VFS boundary. Local formatting, locked all-target/all-feature checks, strict Clippy,
  localization audits, Flatpak metadata, and diff checks passed. Push Native/Flatpak/Foundation
  `29898746678`/`29898746646`/`29898746643` and PR `29898749118`/`29898749101`/`29898749056` all
  passed; Native completed the full GTK, release, checksum/SBOM, and performance suites. PR #1
  remains Draft/Open and Issue #1 remains Open; release status is `unreleased`.

- [x] Make the Linux non-local GIO export boundary explicit. Runtime commit
  `54003159107919f5c9c55b4637aa45054d457c4d` introduces `ExportWriteStrategy`: local paths with a
  parent retain same-directory atomic finalization, while non-local or parentless URIs use GIO
  exclusive creation and preserve the original URI. The `non_local_export_uses_exclusive_create_fallback`
  regression protects this policy. Linux packaging/docs head `e8d301694709ef2737ad92383300018e7c4a5e24`
  pins the tested runtime and records that remote VFS atomicity is unverified. Local formatting,
  locked all-target/all-feature check, strict Clippy, localization audits, Flatpak metadata, and
  diff checks passed. Push Native/Flatpak/Foundation `29897680877`/`29897680772`/`29897680880` and
  PR `29897682852`/`29897682904`/`29897682859` all passed; Native completed the full GTK, release,
  checksum/SBOM, and performance suites. PR #1 remains Draft/Open and Issue #1 remains Open;
  release status is `unreleased`.

- [x] Verify the Linux Secret Service session-only recovery UX at the production GTK boundary.
  Runtime test commit `64909399aa55de6b3dc70b69b46e01ae34bc0606` adds the serialized
  `gtk_secret_storage_fallback_dialog_requires_explicit_session_only_action` fixture. It verifies
  the localized modal warning, focusable controls, explicit Remember clearing only after the
  session-only action, and unchanged Remember state on Close. Packaging/docs/status head
  `804c72ac39bcfa1bdc4ba0127c9352db3bb2f396` pins the tested runtime and documents the
  window-manager focus limitation. Local checks passed; the host lacks `xvfb-run`, so display
  evidence is CI-authoritative. Push Native/Flatpak/Foundation runs
  `29896626177`/`29896626188`/`29896626170` and PR runs
  `29896629236`/`29896629228`/`29896629219` all passed, with Native executing the exact fixture
  and the complete GTK, Secret Service, accessibility, release, and evidence suites. This closes
  the automatable Linux recovery-UX boundary without claiming end-user prompt approval or visual
  review; human review, non-local VFS/power-loss evidence, other clients, signing, rollback, and
  stable release remain open.

- [x] Close the Linux source-level visible-string gettext coverage gap. Linux head
  `31f3a874918aaf867b8d2434385157bff4a62877` passes the dependency-free key, placeholder, and
  visible-control audits: 390 catalog-backed source keys, 448 placeholder calls, and no non-empty
  hard-coded GTK strings across `src/**/*.rs` (three intentional empty/reset call sites). The
  generated official and pseudo-locale catalogs remain covered by the existing runtime suite at
  l10n `88765d3358450ccfac12f396caf5290230a83577`. This is source-level evidence; human translated
  copy, plural, visual, other-client, signing, rollback, and stable-release review remain open.

- [x] Complete the Linux local export pipeline with temporary output and atomic finalization.
  Runtime commit `6e6bc31c7d9d584e9357d272f55132bd02ee367d` keeps non-local URIs on the existing
  GIO exclusive-create fallback, while local paths write and close a same-directory UUID temporary
  file and use GIO's non-overwriting move; failed finalization removes the temporary artifact.
  The ignored GTK fixture is now `gtk_atomic_output_writer_never_replaces_existing_file` and
  checks both occupied-destination preservation and cleanup. Packaging/workflow commit
  `31f3a874918aaf867b8d2434385157bff4a62877` updates the Flatpak source pin and Native workflow.
  Local formatting, locked checks, strict Clippy, demo-provider tests (`157 passed; 3 ignored`),
  Flatpak metadata, and diff checks passed. Push Native/Flatpak/Foundation runs
  `29894536354`/`29894536297`/`29894536351` and PR runs
  `29894538235`/`29894538243`/`29894538211` all passed; Native executed the exact atomic fixture,
  full GTK suite, release build, performance baseline, and checksum/SBOM evidence. This remains
  unreleased Linux Scenario 18 evidence; local full-feature GUI linking, human visual/copy/Orca
  review, other clients, signing, rollback, and stable release remain open.

- [x] Close remaining Linux user-visible export overwrite paths. Runtime commit
  `c11e80bbb69b869b1d021d07e1f97247cf0ae7b4` routes glossary CSV, routing-profile JSON,
  translation-history TSV, and translation-memory TSV through the same GIO exclusive asynchronous
  writer used by translated output and reports; no `replace_contents_bytes_async` export call sites
  remain. Packaging/docs commit `c7afb4c351b5a092318dda3ea93f1a1c1043c097` pins Flatpak and
  documents the shared writer, while final Linux status head
  `831fcf276010419359fb7bf983be1d47de8d3767` records the evidence. Local formatting, locked checks,
  strict Clippy, demo-provider tests (`157 passed; 3 ignored`), localization audits, Flatpak
  metadata, diff checks, and static replacement audit passed. Code-head push Native/Flatpak/
  Foundation `29892239963`/`29892239946`/`29892239987` and PR runs
  `29892242173`/`29892242176`/`29892242188` all passed; Native executed the exact fixture and
  completed the release/evidence suite. Final status-head push Native/Flatpak/Foundation
  `29892566477`/`29892566480`/`29892566481` and PR
  `29892568592`/`29892568596`/`29892568579` also passed. This remains unreleased Linux Scenario 18
  evidence; human
  visual/copy/Orca review, other clients, signing, rollback, and stable release remain open.

- [x] Close the Linux translation-export race window. Runtime commit
  `a48dafe259b794211ed2d1bec0a858b647dcd3d3` replaces plain-text, document-report, and binary
  export replacement writes with GIO exclusive creation plus asynchronous write-and-close, so a
  destination occupied after collision selection is preserved and the export fails closed.
  Packaging/workflow commit `95a47ef6dcec45bb55feb967076cc2bfcb5f5919` adds the serialized GTK
  `gtk_exclusive_output_writer_never_replaces_existing_file` fixture and pins the Flatpak source;
  final status head `a6ddc4766a89f4ad9bf87df773d5f53ea4fa82dd` records the evidence. Local formatting,
  locked checks, strict Clippy, demo-provider tests (`157 passed; 3 ignored`), Flatpak metadata,
  and diff checks passed. Push Native/Flatpak/Foundation `29891347377`/`29891347329`/`29891347335`
  and PR runs `29891349140`/`29891349152`/`29891349162` all passed, with Native executing the
  exclusive fixture and the full release/evidence suite. This remains unreleased Linux evidence;
  human visual/copy/Orca review, other clients, signing, rollback, and stable release remain open.

- [x] Implement Linux collision-safe translation output naming. Runtime commits
  `c8ff5be178d4f85709d8f6e4efe991dd180b3837` and
  `193ca90b94302f7ae42e2b919576d2ffd68f0aae` derive
  `<original-base-name>.<target-bcp47-tag>.<extension>`, sanitize path/control characters, carry
  the persisted target locale through document export, select deterministic `-1`, `-2`, ...
  collision suffixes, and expose the stable output identifier in reports. Packaging/status head
  `56c71b21aedcefbf91ad64c85672d5436ca91a6f` pins the tested runtime input. Local formatting,
  locked checks, strict Clippy, 157-pass demo-provider library tests (3 ignored), localization
  audits, l10n sync, Flatpak metadata, and diff checks passed; the full-feature binary target is
  linker-limited on this host by incomplete GTK/GDK/Graphene symbols. Final push
  Native/Flatpak/Foundation `29890568417`/`29890568416`/`29890568445` and PR runs
  `29890570161`/`29890570133`/`29890570165` all passed, with Native completing the full GTK,
  release-build, checksum/SBOM, and performance-baseline suite. This remains unreleased Linux
  evidence; human visual/copy/Orca review, other clients, signing, rollback, and stable release
  remain open.

- [x] Close the Linux production report-action evidence gap. Runtime/docs commit
  `e28981870563970549ca88c4faa691451ed710e7` extends the serialized
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` fixture to require exactly one
  focusable **Export translation report** button and redacted-TSV tooltip for each pending,
  paused, and cancelled row; formatting commit `07208e1b09e42ecec4a184efa69336570f6243dc` and
  Flatpak pin `ad3012fd0fdf34e81e6cc6bb2e4571e94a324dfc` keep the source input synchronized. Local
  formatting, locked all-target/all-feature check, strict Clippy, 157-pass demo-provider tests
  (3 ignored), localization audits, l10n sync, Flatpak metadata, and diff checks passed. The
  full GTK binary cannot link on this host because installed GTK/GDK/Graphene symbols are
  incomplete; Native CI is authoritative. Final head `ad3012fd0fdf34e81e6cc6bb2e4571e94a324dfc`
  passed push Native/Flatpak/Foundation `29889128173`/`29889128185`/`29889128176` and PR
  Native/Flatpak/Foundation `29889129723`/`29889129750`/`29889129727`; Native executed the full
  fixture suite. This remains unreleased Linux evidence; chooser interaction, visual/copy/Orca
  review, other clients, signing, rollback, and stable release remain open.

- [x] Add the Linux production document translation report surface. Assumption: the first
  report format is a redacted, deterministic TSV snapshot; provider usage and retry counts are
  explicit `unknown` because the persisted document-job schema does not retain them. Linux runtime
  commit `cc5beeea530e500ee2d42b6d05d26dc34a26c7ab` adds the per-job GTK export action and safe
  report builder; packaging/workflow commits `4407ce947f86af070f986e4c4ee0fee6b2305683` and
  `c14760c4c14fe26681c2f11a22a5dd8e9af6b1e9` pin the tested Linux and l10n revisions. Canonical
  l10n `88765d3358450ccfac12f396caf5290230a83577` passed its full 26-test/generated-resource
  validation. Local Linux formatting, locked checks, strict Clippy, 157-pass demo-provider tests
  (3 ignored), localization audits, Flatpak metadata, and diff checks passed. The initial Native
  CI failure `29887678331` was a stale workflow pin to l10n `b817ba9`; after correction, push
  Native/Flatpak/Foundation runs `29887890227`/`29887890202`/`29887890226` and PR runs
  `29887892891`/`29887892948`/`29887892894` all passed, with Native completing the full GTK,
  release-build, checksum/SBOM, and performance-baseline suite. Final status head
  `a3af4c40a01db6256e5549cdd08ecf78be3ad1d1` also passed push Native/Flatpak/Foundation runs
  `29888261417`/`29888261423`/`29888261426` and PR runs `29888264002`/`29888263976`/`29888263981`.
  This remains unreleased Linux evidence;
  output identifiers are `<not-exported>` until an output is persisted, and human visual/copy/
  Orca review, other clients, signing, rollback, and stable release remain open.

- [x] Extend Linux document-job queue evidence through the production pending-job Pause action.
  Linux runtime commit `8c05797011a04cdc11988cfbe9c35c2d05d2269b` extends the serialized
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` fixture so pending, paused, and
  cancelled snapshots each expose their single queue action. It activates `Pause document` for
  `gtk-queue-first` and confirms the pending job remains selected with `Pending` state while the
  dialog closes after sending the command. Packaging pin commit
  `4bc6da51ac6510503e41234bfb3eea5e794fe1e7` and final Linux status head
  `3fa224a1047a30826ce1c62b45bc8138a02b6e8f` record the evidence. Local formatting, locked
  all-target/all-feature check, strict Clippy, 157-pass demo-provider tests (3 ignored),
  localization audits, l10n sync, Flatpak metadata, and diff checks passed. Code-head push/PR
  Native/Flatpak/Foundation runs `29885792891`/`29885792900`/`29885792902` and
  `29885795224`/`29885795226`/`29885795242` passed; final status-head push/PR runs
  `29886174310`/`29886174217`/`29886174265` and `29886176680`/`29886176559`/`29886176546`
  also passed, with Native executing the exact queue fixture successfully. This remains unreleased
  Linux evidence; human visual/copy/Orca review, physical interruption behavior, other clients,
  signing, rollback, and stable release remain open.

- [x] Extend Linux document-job queue evidence through the production cancelled-job Retry action.
  Linux runtime commit `819eff7cff79b8e6514120d550f72658ff276bf9` extends the serialized
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` fixture with a cancelled third
  snapshot: it verifies the three-file queue, requires the single `Retry document` action, emits
  it, and confirms `gtk-queue-cancelled` remains selected with `Cancelled` state while the dialog
  closes after sending the command. Packaging/docs commit `8fae49ee451c5df22ec766eabe14c1ad0dc71ee2`
  pins Flatpak and documents the assertion; final Linux status head `5432b021d3073a703d3d8824dd3fbd00118ba66d` records the evidence. Local
  formatting, locked all-target/all-feature check, strict Clippy, 157-pass demo-provider tests
  (3 ignored), localization audits, l10n sync, Flatpak metadata, and diff checks passed. Final
  status-head push Native/Flatpak/Foundation runs `29884616494`/`29884616511`/`29884616504` and
  PR runs `29884618885`/`29884618826`/`29884618821` all passed; Native executed the exact queue
  fixture successfully. This remains unreleased Linux evidence; human visual/copy/Orca review,
  physical interruption behavior, other clients, signing, rollback, and stable release remain
  open.

- [x] Extend Linux document-job queue evidence through the production paused-job Resume action.
  Linux runtime commit `7b92bd43915ebefde3e29463252aacb94d064691` extends the serialized
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` fixture: after selecting the paused
  second snapshot it reopens the production queue, requires the single `Resume document` action,
  activates it, and verifies the same job ID/state remains selected while the dialog closes after
  sending the command. Packaging/docs commit `ea5bf4768a9f8b40fd04fbc929d8ea788ead32bc` pins
  Flatpak and documents the assertion; final Linux status head `755ed9a87ee3034c282ef655915a8ad0ec4fe941`
  records the evidence. Local formatting, locked all-target/all-feature check, strict Clippy,
  157-pass demo-provider tests (3 ignored), localization audits, l10n sync, Flatpak metadata, and
  diff checks passed. Final status-head push Native/Flatpak/Foundation runs
  `29883868226`/`29883868326`/`29883868256` and PR runs `29883870536`/`29883870487`/`29883870484`
  all passed; Native executed the exact queue fixture successfully. This remains unreleased Linux
  evidence; human visual/copy/Orca review, physical interruption behavior, other clients, signing,
  rollback, and stable release remain open.

- [x] Extend Linux document-job queue evidence through the production GTK selection boundary. Linux
  runtime commit `c652232196f09ee9a2cbf69f7eaa9e01ca7672e7` adds the ignored serialized
  `gtk_document_jobs_dialog_selects_between_multiple_jobs` fixture, which creates two persisted
  jobs, asserts both filenames and metadata are visible in the real dialog, selects the second
  row, and verifies the selected snapshot ID, paused state, and source text. Packaging/CI commit
  `e21cd11e5d3518a8248bf95712cad55c6bef57ec` adds the dedicated DBus/Xvfb Native step. Local
  formatting, locked all-target/all-feature check, strict Clippy, 157-pass demo-provider tests
  (3 ignored), localization audits, l10n sync, Flatpak metadata, and diff checks passed. Push
  Native/Flatpak/Foundation runs `29882794626`/`29882794606`/`29882794617` and PR runs
  `29882796272`/`29882796303`/`29882796264` are the authoritative six-gate set and all passed;
  Native executed the exact fixture successfully. This remains unreleased Linux evidence; human visual/copy/Orca
  review, other clients, signing, rollback, and stable release remain open.

- [x] Extend Linux Scenario 15 through the production GTK OOXML safety boundary. The serialized
  `gtk_malicious_archive_import_fails_closed_before_document_job` fixture now drives DOCX
  traversal, suspicious-compression, macro (`word/vbaProject.bin`), and digital-signature
  (`_xmlsignatures/sig1.xml`) packages through asynchronous GIO import, proving fixed rejection,
  no document job, an unchanged empty source editor, and no forbidden extraction. Linux commit
  `ed1d419e4c13e614d5470f500e5d0736390449c6` pins Flatpak to the tested source. Local formatting,
  locked checks, strict Clippy, 157-pass demo-provider tests (3 ignored), localization audits,
  l10n synchronization, Flatpak metadata, and diff checks passed. Push Native/Flatpak/Foundation
  runs `29881709701`/`29881709736`/`29881709671` and PR runs
  `29881711799`/`29881711798`/`29881711800` all passed; Native executed the exact GTK fixture.
  This remains unreleased Linux evidence; human review, other clients, signing, rollback, and
  stable release remain open.

- [x] Extend Linux Scenario 15 through the production GTK malicious-archive boundary. Linux
  runtime code `acb15c2b17bc58f311a31edd57f8793fb7f90e7f` adds the serialized
  `gtk_malicious_archive_import_fails_closed_before_document_job` fixture and feeds the real
  asynchronous GIO loader DOCX archives containing a `../outside.txt` traversal entry and a highly
  compressed repetitive resource, then verifies fixed rejection remains visible, no document-job
  snapshot, an unchanged source editor, and no forbidden extraction. Local locked checks, strict Clippy,
  no-default/demo-provider suites (`83/1` and `157/3` ignored), localization audits, l10n sync,
  Flatpak metadata, diff checks, and cargo-deny passed; display-backed execution is CI-authoritative
  because this host lacks xvfb/GTK development symbols. Final packaging/status head `2900f19c1fe70b184e2d5fd2de1c40627c26a80f` pins Flatpak to the runtime fix; push
  Native/Flatpak/Foundation `29880789834`/`29880789824`/`29880789819` and PR
  `29880792162`/`29880792135`/`29880792142` passed. This remains unreleased Linux evidence.

- [x] Extend Linux Scenario 14 through the production GTK Incognito privacy boundary.
  Linux runtime code `47bbe58bf16ecac11976828575c5964f511198fb` adds the serialized
  `gtk_incognito_translation_bypasses_memory_and_persistence` fixture. It drives the GTK Incognito
  toggle, authenticated connection, model selection, standard translation, and repeated private
  translation; the provider request counter increases for the Incognito repeat, while reopened
  SQLite history and translation-memory counts remain exactly one each. Final Linux status/docs
  head `ca130eec9643c4bf08d9a5877a921d26ef20e9cb` pins the runtime source and records local
  formatting, locked checks, strict Clippy, no-default/demo-provider suites (`83 passed; 1 ignored`
  and `157 passed; 3 ignored`), localization audits, l10n synchronization, Flatpak metadata, and
  diff checks. Final status-head push Native/Flatpak/Foundation runs
  `29878453604`/`29878453311`/`29878453609` and PR runs
  `29878456310`/`29878456278`/`29878456340` passed. Human privacy review, other clients, signing,
  rollback, and stable release remain open.

- [x] Extend Linux Scenario 14 through worker-level Incognito translation-memory isolation.
  Linux runtime `0203b2183ee79d3ba4d836cddeb714ad64091231` keeps Incognito requests out of
  translation-memory lookup and out of history/memory persistence. The regression
  `incognito_translation_bypasses_existing_memory_and_persists_nothing` first records a standard
  request, then requires an identical Incognito request to reach the provider again while the
  reopened database remains at one history row and one memory row. Local formatting, locked
  all-target/all-feature checks, strict Clippy, no-default/demo-provider suites (`83 passed; 1
  ignored` and `160 passed; 3 ignored`), localization audits, l10n synchronization, Flatpak
  metadata, and diff checks passed. Push Native/Flatpak/Foundation runs
  `29876038029`/`29876038007`/`29876038060` and PR runs
  `29876035413`/`29876035445`/`29876035433` passed. This remains unreleased Linux evidence;
  physical privacy review, other clients, signing, rollback, and stable release remain open.

- [x] Extend Linux Scenario 12 through the production GTK interrupted document-job restart path.
  Linux runtime `ca67c8b6b50cd79700c6be505bd7a950c73ed870` adds the serialized
  `gtk_interrupted_document_job_restores_and_resumes` fixture: a two-segment TXT job is translated
  through the real GTK form, paused after one committed segment, persisted in a private database,
  restored by a second GTK worker, reconnected with a fresh session credential under the same
  non-secret provider identity, and resumed without duplicating completed output. Linux evidence
  documentation head `1be587b2d910690cb3fdc07c0342fd0bb9c55ef4` records local formatting, locked
  all-target checks, strict Clippy, no-default/demo-provider suites (`83/1` and `156/3` ignored),
  localization audits, l10n synchronization, Flatpak metadata, and diff checks. Code-head push
  Native/Flatpak/Foundation gates `29873822240`/`29873822363`/`29873822338` and PR gates
  `29873825162`/`29873825141`/`29873825142` passed; evidence-head push gates
  `29874337974`/`29874337743`/`29874337869` and PR gates
  `29874339972`/`29874339969`/`29874339977` passed; final documentation-head push gates
  `29874798901`/`29874798855`/`29874798868` and PR gates
  `29874801196`/`29874801209`/`29874801193` also passed. Physical power-loss recovery, live
  provider interoperability, human visual/copy/Orca review, other clients, signing, rollback,
  and stable-release approval remain open.

- [x] Extend Linux Scenario 9 through the real GTK glossary/protected-span boundary. Linux runtime
  `aa0e0206c20e325bf0dd340dab039eea400a9ab0` adds the serialized
  `gtk_glossary_and_protected_terms_preserve_translation` fixture: a real GTK glossary entry
  replaces `LinguaMesh` with an opaque marker before dispatch, the loopback provider splits that
  marker across streamed deltas, and the production reducer restores `你好，凌瓦网！`. Final Linux
  status/docs head `b6f4fbebc9daf928edccf05ee4b401be2a945658` pins the Flatpak input and records local
  formatting, locked checks, strict Clippy, no-default/demo-provider suites (`83/1` and `156/3`
  ignored), localization audits, l10n synchronization, Flatpak metadata, and diff checks. Code-head
  push/PR Native, Flatpak, and Foundation gates `29868747478`/`29868747474`/`29868747461` and
  `29868750361`/`29868750281`/`29868750341` passed; final status-head gates
  `29869815247`/`29869815332`/`29869815462` and `29869819086`/`29869818840`/`29869819166` also
  passed, with Native explicitly running the exact fixture. Provider-specific glossary semantics,
  human visual/copy/Orca review, other clients, signed artifacts, rollback, and stable release
  remain open.

- [x] Extend Linux Scenario 6 through the real GTK translation-cancellation boundary. Linux
  runtime `2730a24bc67f9c424b3cce845ced895d9f2710b2` adds the serialized
  `gtk_cancel_translation_preserves_partial_output` fixture: the production Stop action cancels
  after the first streamed `你好` delta, preserves the partial output, reaches `Cancelled`, disables
  Stop, and enables Retry without an error or later output mutation. Packaging/status head
  `5e74f79a2b2af049b84c010632aa979a064f9b1c` records local formatting, locked checks, strict
  Clippy, no-default/demo-provider suites (`83/1` and `156/3` ignored), localization audits, l10n
  sync, Flatpak metadata, and diff checks. Code-head push Native/Flatpak/Foundation
  `29866519789`/`29866519798`/`29866519885` and PR gates
  `29866523643`/`29866523637`/`29866523644` passed. Final status-head push/PR gates
  `29867517962`/`29867519068`/`29867518348` and `29867521905`/`29867521950`/`29867521920`
  also passed. Physical
  provider transport cancellation, human visual/copy/Orca review, other clients, signed artifacts,
  rollback, and stable release remain open.

- [x] Extend Linux Provider Hub and Scenario 8 through the production GTK Test connection action.
  Linux runtime `2d5f625067fb84af260b664e5e2d9c027095e6d8` adds the serialized
  `gtk_connection_test_reports_models_and_redacts_credential` fixture: a bearer-token probe reports
  a bounded model count without committing a session, clears the credential field, and preserves
  typed authentication errors for localized redacted failure copy. Linux status head
  `ef83869df4901adbdcb3baaa7ade27c8ad685dd3` records local no-default/demo-provider suites
  (`83/1` and `156/3` ignored), formatting, all-target/all-feature check, strict Clippy,
  localization audits, l10n synchronization, Flatpak metadata, and diff checks. Final push
  Native/Flatpak/Foundation `29864753592`/`29864753479`/`29864753370` and PR
  `29864757307`/`29864757739`/`29864757412` all passed; Native explicitly ran the new fixture.
  Human copy/visual/Orca review, live-provider interoperability, other clients, signing, rollback,
  and stable release remain open.

- [x] Make Linux authentication failures actionable and localized. Linux code
  `c66f6df42fd03c67b3991c5b7fb4229dccadce97` maps provider HTTP 401/403 failures to the canonical
  `error.authentication` copy before GTK rendering, with a regression for Simplified Chinese and
  backend-status redaction. Local no-default/demo-provider suites passed (`83/1` and `156/3`),
  localization key/placeholder/visible audits and Flatpak metadata passed. The first c66f6df
  Flatpak push/PR runs `29856562427`/`29856565472` exposed a stale source pin; corrected packaging
  head `5a18ba9bc04b2430b7d07a30fdb2c64d82df8a26` passed push Native/Flatpak/Foundation
  `29856805455`/`29856805550`/`29856805478` and PR
  `29856808412`/`29856808321`/`29856808250`. Human copy/visual/Orca review, live-provider
  interoperability, other clients, signing, rollback, and stable release remain open.

- [x] Extend Linux Scenario 8 through the real GTK authentication-failure boundary. Linux code
  `bd3487461e725ec5718636b3c2057aa1edd3315b` adds the serialized
  `gtk_authentication_failure_shows_localized_redacted_error` fixture: a wrong session credential
  travels through the GTK Connect button and worker rejection event, then renders Simplified
  Chinese catalog copy in an `Alert` without the credential or 401/403 detail. Packaging/docs head
  `9e45b2a8b721cf0f316d94009d66390677dac480` consumes that code. Local no-default/demo-provider
  suites passed (`83/1` and `156/3`), and push Native/Flatpak/Foundation gates
  `29859661736`/`29859661796`/`29859661669`, PR Native/Flatpak/Foundation gates
  `29859664966`/`29859664991`/`29859665005` passed. Native explicitly runs the exact
  authentication-failure GTK fixture. Human translated-copy/visual/Orca review, live-provider
  interoperability, other clients, signing, rollback, and stable release remain open.

- [x] Extend Linux Scenario 17 through the real GTK offline-session boundary. Linux code
  `3242133acbf77a7e72374ab680a83f4ff676ff0c` adds the serialized
  `gtk_offline_connection_failure_preserves_confirmed_session` fixture: a confirmed bearer-token
  session and selected model survive a second connection attempt to a deliberately released
  loopback port, while the credential field clears, the localized network `Alert` is shown, and
  source text remains unchanged. Packaging/status head `97c1f6f9d4e2af9e19193e606b2449dc66161247`
  records the final evidence. Local no-default/demo-provider suites passed (`83/1` and `156/3`),
  and final push Native/Flatpak/Foundation gates `29861846026`/`29861846105`/`29861845971` plus
  PR gates `29861848727`/`29861848911`/`29861848713` passed. Native explicitly reports the exact
  offline GTK fixture successful. Human offline/visual/copy/Orca review, physical outage
  simulation, other clients, signing, rollback, and stable release remain open.

- [x] Add deterministic Unix WAL process-crash recovery evidence. Core
  `8837e59395742b5385af5037aa36a2596af3b025` starts a child test process with a reader snapshot,
  commits a provider profile under `synchronous=FULL`, terminates abruptly, and verifies parent
  reopen restores the model and persistent `SecretRef`; Core local formatting, checks, Clippy, and
  full workspace tests passed. Core CI/Fuzz/Native SDK runs
  `29854340447`/`29854339357`/`29854340140` passed. Linux docs/status head
  `b9c1c0e2c337eef609656aa1e62bf718068382e1` pins that Core revision; Linux code-head push
  Native/Flatpak/Foundation `29854770351`/`29854770380`/`29854770404` and PR
  `29854773408`/`29854773406`/`29854773414` passed, followed by final status-head push
  `29855336417`/`29855336358`/`29855336333` and PR
  `29855339737`/`29855339709`/`29855339713`. Physical power-loss and alternate VFS behavior
  remain unverified; this is unreleased Linux hardening evidence.

- [x] Harden Linux-first SQLite WAL commit durability. Core `cfecf17802f022b3dc49cff2917de5a77382aefa`
  sets `synchronous=FULL` while retaining WAL, foreign-key enforcement, and secure deletion; Linux
  docs/status head `94d57f61c16be45dd18e9a0519d7296cebefcb8f` pins that Core revision. Core local
  formatting, checks, Clippy, and full workspace tests passed; Core CI, fuzz/sanitizer, and native
  SDK runs `29852245672`/`29852245746`/`29852246017` passed. Linux local checks and push gates
  `29853359722`/`29853359731`/`29853360059`, plus PR gates
  `29853364106`/`29853364378`/`29853364352`, passed. Physical power-loss recovery and alternate
  SQLite VFS behavior remain unverified; this is unreleased hardening evidence.

- [x] Add Linux-first normalized usage metadata and provider wire parsing. Core
  `117a72ea80f40258a0abf582ffe1fae93c155786` carries typed provider usage events and normalizes
  OpenAI Chat/Responses, Anthropic, Gemini, and Ollama metadata; l10n
  `b817ba911c2ffafb35b7a29755681ab39e950368` adds five source/draft labels; Linux docs/status head
  `507e028d10d2c360053d7b06389ceae910dd5fe9` pins Core and keeps Flatpak Linux code at
  `5d59646adeed72750964fa628eb0a3088911ac24`. Local Core/Linux/l10n validation passed, including
  provider decoder regressions, 82/1 and 155/3 Linux suites, audits, and Flatpak metadata. Core
  push CI/Native SDK/Fuzz `29850220180`/`29850220219`/`29850220238`, Linux push
  Native/Flatpak/Foundation `29850547006`/`29850546971`/`29850548756`, and Linux PR
  Native/Flatpak/Foundation `29850550865`/`29850550890`/`29850550591` passed. Central coordination
  implementation checkpoint `c60b1752dc969f270a40d857895f028b789c7d86` and documentation
  alignment commit `7efe0ebf1981b3930628ad0c6aa0fc33447d53b1` passed workflows
  `29851043287`/`29851347134`. Billing equivalence, pricing, other clients,
  human visual/copy/Orca review, signing, rollback, and stable release remain open.

- [x] Verify Linux GTK routing profile deletion cleanup. Linux code `7f3ed8d` extends the serialized
  candidate lifecycle fixture through Use, Delete, `RoutingProfileDeleted`, selected-ID cleanup,
  and an empty worker reload; Flatpak pin `e4682e4` and Linux docs/status head `a4a17ae` record the
  exact lineage. Local formatting, locked checks, strict GUI Clippy, demo-provider/no-default
  suites (`155/3` and `82/1` ignored), localization, l10n, Flatpak, and diff checks passed.
  Code-head push Native/Flatpak/Foundation `29844751533`/`29844750810`/`29844750926`, PR
  `29844754143`/`29844754151`/`29844754090`, and final status-head push Native/Flatpak/Foundation
  `29845371082`/`29845371250`/`29845370967`, PR `29845374385`/`29845374215`/`29845374014` all
  passed. This remains unreleased Linux automation evidence; visual/copy/Orca review, broader
  candidate-management criteria, other clients, signing, rollback, and stable release remain open.

- [x] Verify Linux GTK routing candidate edit persistence. Linux code `dda682d` adds a serialized
  lifecycle assertion that locks an existing profile ID in edit mode, deselects a candidate, saves
  the same record, lists it through the worker, and reopens the editor to confirm the reduced chain
  persists. Flatpak pin `70e6074` and Linux docs/status head `9cab5ba` record the exact lineage.
  Local formatting, locked checks, strict GUI Clippy, demo-provider/no-default suites (`155/3`
  and `82/1` ignored), localization, l10n, Flatpak, and diff checks passed. Corrected code-head
  push Native/Flatpak/Foundation `29842604602`/`29842604156`/`29842607411` and PR
  `29842605446`/`29842605764`/`29842605418` passed. Final status-head push Native/Flatpak/Foundation
  `29843266745`/`29843267871`/`29843267747` and PR `29843272666`/`29843272809`/`29843272670` also
  passed. This remains unreleased Linux automation evidence; human visual/copy/Orca review,
  broader candidate-management release criteria, other clients, signing, rollback, and stable
  release remain open.

- [x] Expose the generated Linux `en-XA` accented and `ar-XB` RTL pseudo-locales in the native GTK
  runtime selector. Linux code `64a2877` adds catalog lookup, plural rules, locale names, and RTL
  metadata after the twelve official packs; packaging/docs head `cf0b689` repins Flatpak exactly.
  Local formatting, all-target/all-feature check, strict Clippy, localization audits, l10n sync,
  Flatpak metadata, and 82/150 library suites passed (`1`/`3` ignored). Final push/PR Native,
  Flatpak, and Foundation gates `29824916845`/`29824916822`/`29824916804` and
  `29824919512`/`29824919621`/`29824919573` passed. Pseudo-locales remain layout/direction test
  data, not qualified translations.

- [x] Exercise Linux pseudo-locales through the real GTK/AT-SPI fixture. Fixture/docs head `22ff8f8`
  asserts expanded `en-XA` and bidi-isolated `ar-XB` control names and roles; corrective source head
  `304e683` uses process-based window discovery after the first title-based attempt failed. Push
  Native/Flatpak/Foundation runs `29825878061`/`29825878027`/`29825878160` and PR runs
  `29825880504`/`29825880581`/`29825880584` passed, with the PR Flatpak rerun clearing a transient
  Flathub fetch failure. This is automation evidence only; human copy, visual, and screen-reader
  review remain open.

- [x] Verify Linux desktop text scaling alongside high contrast and reduced motion. Code `62c72fa`
  applies an isolated `Sans 24` GTK preference and asserts the production title's Pango context
  receives the requested size; packaging/docs head `ed196d1` and status head `d92e1a4` document the
  fixture. Push Native/Flatpak/Foundation runs `29828098608`/`29828098596`/`29828098740` and PR
  runs `29828100998`/`29828100985`/`29828100954` passed. Manual visual/text-scaling review remains
  open.

- [x] Verify the fallback-provider dropdown's visible label relation. Linux code `c25bd31` connects
  the disabled fallback selector to its mnemonic label and extends the serialized GTK regression
  with `LabelledBy` and mnemonic assertions. Packaging/docs `b74b854` repins Flatpak to the exact
  code head and records the first stale-pin failure. Local 82/150 suites (`1`/`3` ignored), strict
  Clippy, localization audits, Flatpak metadata, and diff checks passed. Final push
  Native/Flatpak/Foundation runs `29829811241`/`29829811272`/`29829811222` and PR runs
  `29829814249`/`29829814264`/`29829814189` passed. Human accessibility review and stable release
  remain open.

- [x] Verify Linux provider mnemonic activation in the real keyboard fixture. Code `3b2b69c` now
  records and requires `provider_preset` focus after the fixture sends `Alt+P`, then keeps the
  existing Tab/Shift+Tab and Arabic RTL traversal checks. Packaging/docs head `123e4e4` repins
  Flatpak to `1030e88` and records the stale-pin correction. Final docs-head push
  Native/Flatpak/Foundation runs `29831556653`/`29831556427`/`29831556369` and PR runs
  `29831559867`/`29831560089`/`29831559828` passed; code-head Native runs also passed after the
  initial Flatpak pin failure. Physical keyboard and human accessibility review remain open.

- [x] Widen the Linux visible-string localization audit. Linux code head `56a0812` now scans every
  Rust source file under `src/**/*.rs` and checks file-filter names in addition to labels, titles,
  tooltips, placeholders, dialog actions, and direct list literals. Local localization audits,
  l10n synchronization, Flatpak metadata, formatting, locked offline checks, strict Clippy, and
  81/149 library tests passed. Push Native/Flatpak/Foundation runs
  `29823219039`/`29823218980`/`29823219144` and pull-request runs
  `29823221964`/`29823221885`/`29823221874` passed; status/docs head `89d4e22` records the evidence.
  This is source-level evidence only; translated-copy, plural, visual, and stable-release review
  remain open.

- [x] Extend the Linux headless Orca fixture to Arabic. Corrected code/docs head `490657b` maps the
  localized Stop control and runs the Arabic private Xvfb/AT-SPI focus path while retaining the full
  English speech-generation assertion; the initial `7c9b7e4` attempt failed only at the unstable
  Arabic speech backend and is recorded. Code-head push/PR Native/Flatpak/Foundation runs
  `29821349008`/`29821349052`/`29821349030` and `29821346477`/`29821346416`/`29821346504` passed;
  status/docs head `b574cc4` passed `29821778205`/`29821778263`/`29821778215` and
  `29821775327`/`29821775342`/`29821775256`. Human listening and speech-quality review remain open.

- [x] Add the Linux Arabic live AT-SPI fixture. Code head `3ce10d5` extends the existing semantic
  tree inspection with localized Arabic Open/Translate/Stop names and the catalog's English Retry
  and fallback names, preserving button/checkbox roles and two text-editor checks. Code-head push/
  PR Native/Flatpak/Foundation runs `29819765571`/`29819765594`/`29819765609` and
  `29819762498`/`29819762505`/`29819762534` passed; status/docs head `c5db4e4` passed
  `29820197646`/`29820197676`/`29820197652` and `29820195059`/`29820195042`/`29820194969`.
  Human Orca speech, copy/RTL and physical review, other clients, signing, and stable release remain open.

- [x] Add and verify Linux desktop accessibility preference evidence. Linux `53cd41f` adds the
  isolated GTK high-contrast/reduced-motion fixture; push Native/Flatpak/Foundation
  `29811402708`/`29811402703`/`29811402563` and PR
  `29811404883`/`29811404846`/`29811404855` passed. Manual visual, RTL, screen-reader, and
  compositor review plus other-client and stable-release work remain open.

- [x] Verify the clean-bootstrap acceptance path in a disposable workspace. A fresh clone of
  `linguamesh-project` ran `GITHUB_OWNER=getio0909 bash tools/bootstrap.sh`, cloned all seven
  canonical public repositories, and passed strict workspace validation, global-goal pin checks,
  release-manifest validation, documentation-link checks, and credential-signature scanning. The
  temporary workspace was removed afterward; no existing user worktree was changed.

- [x] Reverify the reproducible Linux SDK package against the current Core ABI/document pin.
  Core documentation head `f09a632` passed `bash tools/verify-linux-sdk-package.sh`: the
  `0.1.0-alpha.2` archive rebuilt twice with SHA-256
  `487c83c17f80634826437e94ca7d817e83f0addf60999d6789fcb58beb774afc`, all packaged checksums and
  pkg-config metadata validated, and the packaged static-library C consumer smoke passed. The
  archive is unsigned local prerelease evidence; central coordination workflow `29807730525`
  passed Linux and PowerShell validation. The functional Core release pin remains
  `19229184a21a6725326a3d30dea9bc72e5ac999f` and no stable artifact is claimed.

- [x] Add the pinned Core Linux SDK package smoke to Linux Native CI. Linux commit `cef6ac1`
  runs `bash tools/verify-linux-sdk-package.sh` from the exact Core revision
  `19229184a21a6725326a3d30dea9bc72e5ac999f`; the release archive rebuilt twice, every external
  and packaged SHA-256 entry passed, pkg-config validated, and the packaged static C consumer
  passed with archive SHA-256
  `3b42d10a347a32e45abb63f3ddb4bf052f90da26f940d2436256f66baae0c9f5`. Push Native/Flatpak/
  Foundation `29808320946`/`29808320963`/`29808320962` and PR
  Native/Flatpak/Foundation `29808324340`/`29808324366`/`29808324395` passed; the follow-up
  status head `bd9559c` reran push `29808700811`/`29808700809`/`29808700814` and PR
  `29808703288`/`29808703310`/`29808703348` successfully. This is prerelease coordination
  evidence only; no signed or stable artifact is authorized.

- [x] Add the Linux dependency advisory, license, and provenance gate. Linux `deny.toml` reuses
  the reviewed Core policy, with duplicate dependency versions warning while advisories, licenses,
  and sources fail closed. Local `cargo deny --manifest-path Cargo.toml --all-features check` passed;
  push Native/Flatpak/Foundation `29806613032`/`29806613069`/`29806613012` and PR
  Native/Flatpak/Foundation `29806615931`/`29806615901`/`29806615910` passed at Linux
  documentation/status head `ca4d11f89ee9323f18a19b5ccc75e270359705d2`. Stable artifacts,
  signing, human desktop review, other clients, and stable release remain open.

- [x] Replace the Milestone 8 threat/privacy document skeletons with evidence matrices. The threat
  model now maps required abuse cases to controls, repository evidence, owner roles, and residual
  review boundaries; the privacy model inventories content, credentials, file grants, operational
  metadata, preferences, and explicit diagnostic exports with retention and user controls. Workspace
  and repository validation passed. Manual UI/physical review, other clients, signing, rollback,
  and stable-release approval remain open.

- [x] Add the Linux-first FileLease document-import vertical slice. Core
  `8b096478b1623bdaf5105e8a8f59e55e2fa8015d` adds `file_lease_v1`, validates all required resource
  shapes, and proves fail-closed access after expiry/revocation through domain and FFI tests. Linux
  `f95780db3dd05fdccfe47af254f73c5107587077` requires the feature, validates the lease around portal/
  GIO reads, rejects expired decoding, and revokes the lease after bounded bytes are copied. Local
  no-default/demo-provider suites (`81 passed; 1 ignored` / `145 passed; 3 ignored`), strict Clippy,
  localization audits, Flatpak metadata, Core CI `29784269272`, and Native SDK smoke passed; Linux
  Linux PR Native/Flatpak/Foundation runs `29785377479`/`29785377512`/`29785377513` passed with jobs
  `88495671317`/`88495671975`/`88495671980`. ABI lease transfer, other clients, signing, rollback,
  and stable release remain open. Central coordination `29785760751` passed Linux/PowerShell jobs
  `88496851860`/`88496851914`.

- [x] Project the bounded FileLease lifecycle through the Core ABI and repin Linux. Core
  `0396736235d4dc5c8992d3bfef5aded3abadf457` adds engine-scoped create, active-state, expire,
  revoke, and destroy calls for validated paths and platform descriptors; resource values remain
  private to Core. Core CI/Native SDK `29787040329`/`29787040314` passed. Linux
  `8f52685ade7cfbe29f0cafa42263bb3b0a725259` consumes the exact pin; local no-default/demo-provider
  suites (`81 passed; 1 ignored` / `145 passed; 3 ignored`), strict Clippy, localization audits,
  Flatpak metadata, and PR Native/Flatpak/Foundation `29787357289`/`29787357304`/`29787357315`
  passed. ABI document-command resource consumption, OS-handle transfer, other clients, signing,
  rollback, and stable release remain open; central validation `29787744384` passed; PR #1 and
  Issue #1 stay open.

- [x] Add bounded malformed-input hardening at the Core C ABI boundary and repin Linux. Core
  `9a959f1` adds a deterministic 4,096-case corpus through `lm_engine_submit`, capped at the 1 MiB
  protocol limit and requiring controlled results without provider requests; Core CI/Native SDK
  `29788492719`/`29788492749` passed. Linux `1e631f1` consumes the exact pin; local no-default and
  demo-provider suites (`81 passed; 1 ignored` / `145 passed; 3 ignored`), strict Clippy, all-target
  check, localization audits, and Flatpak metadata passed. Linux PR Native/Flatpak/Foundation
  `29788818095`/`29788818096`/`29788818078` passed. Coverage-guided fuzzing, sanitizer runs,
  document-command resource consumption, OS-handle transfer, other clients, signing, rollback,
  and stable release remain open; PR #1 and Issue #1 stay open.

- [x] Add a reproducible Core protocol decoder fuzz and sanitizer smoke gate and repin Linux. Core
  `8b12a65` passed CI/Fuzz/Native SDK `29789910147`/`29789910142`/`29789910099` with 2,000 bounded
  cargo-fuzz runs on the fixed nightly toolchain. Linux `0a9a98f` consumed the exact pin; local
  no-default/demo-provider suites, strict Clippy, all-target check, localization audits, and
  Flatpak metadata passed. Linux PR Native/Flatpak/Foundation `29790092019`/`29790092011`/
  `29790091990` passed all jobs. Document-parser fuzzing, broader FFI misuse sanitizers, other
  clients, signing, rollback, and stable release remain open; PR #1 and Issue #1 stay open.

- [x] Add bounded Core document-decoder fuzzing and repin Linux. Core `e7ca21d` passed CI/Fuzz/
  Native SDK `29791113656`/`29791113663`/`29791113659`; protocol and document targets each ran
  2,000 cargo-fuzz iterations under the fixed nightly AddressSanitizer toolchain. Linux `e71edf5`
  consumed the exact pin; local no-default/demo-provider suites, strict Clippy, all-target check,
  localization audits, and Flatpak metadata passed. Linux PR Native/Flatpak/Foundation
  `29792553415`/`29792553389`/`29792553385` passed all jobs. Broader FFI misuse sanitizers,
  document-command resource consumption, other clients, signing, rollback, and stable release
  remain open; PR #1 and Issue #1 stay open.

- [x] Add bounded Core ABI document-byte consumption and repin Linux. Core `1e0ae8d` passed
  CI/Fuzz/Native SDK `29793500441`/`29793500440`/`29793500462`; the C ABI validates a bounded
  document snapshot under an engine-scoped lease and consumes it once on success. Linux `37e9b74`
  passed formal PR Native/Flatpak/Foundation `29793663690`/`29793663688`/`29793663685`; OS-handle
  duplication/transfer, other clients, signing, rollback, and stable release remain open.

- [x] Add Linux-first Core POSIX-descriptor document consumption and repin Linux. Core `1922918`
  passed CI/Fuzz/Native SDK `29795469293`/`29795469253`/`29795469275`; the C ABI duplicates a
  registered descriptor, reads a bounded document snapshot, and consumes the lease only after
  shared parsing succeeds. Linux `126699a1` passed PR Native/Flatpak/Foundation
  `29795527184`/`29795527194`/`29795527187`; Android/Windows handle transfer, other clients,
  signing, rollback, and stable release remain open.

- [x] Align the Linux Flatpak source pin with the exact reviewed head. Linux `2fb2774` updates
  packaging and the testing-guide Core example without runtime changes; local metadata/formatting
  checks passed. Push Native/Flatpak/Foundation `29796238918`/`29796238922`/`29796238931` and PR
  runs `29796240722`/`29796240700`/`29796240751` passed; the PR and Issue remain open and no
  stable-release claim is made.

- [x] Attach bounded rollback evidence to Linux prerelease sidecars. Linux `665eb92` generates
  exact-pin `ROLLBACK.md` records for Native and Flatpak evidence; local tests/audits passed. Push
  Native/Flatpak/Foundation `29796868664`/`29796868631`/`29796868628` and PR
  `29796870557`/`29796870563`/`29796870547` passed all jobs. The records contain no previous stable
  revision or signing material, so stable release remains open.

- [x] Verify the Linux preflight parent-replacement regression. Code head `b463e5b` and docs-only
  head `43b9c5e` are covered by push Native/Flatpak/Foundation
  `29798721356`/`29798721343`/`29798721336` and PR
  `29798723569`/`29798723560`/`29798723668`; all passed. The canceled stale runner is excluded,
  and broader filesystem races plus stable release remain open.

- [x] Expand the Linux live AT-SPI action-name fixture. Linux `ef87a5b` requires named Open,
  Translate, Retry, fallback-consent label/control, and Stop controls with expected roles while
  retaining text-editor checks. The first `9bda65b` run exposed GTK's label-node export for the
  fallback checkbox; `ef87a5b` corrects that assertion. Push Native/Flatpak/Foundation
  `29799549333`/`29799549300`/`29799549304` and PR
  `29799551201`/`29799551179`/`29799551121` passed all jobs. Human Orca listening, physical review,
  other clients, signing, and stable release remain open.

- [x] Extend Linux localization key coverage to error mappings. Linux `37539e7` makes the source
  audit verify every declared `error.*` mapping against the canonical catalog; the checked set is
  now 381 keys, with placeholder and visible-string audits still passing. Push Native/Flatpak/
  Foundation `29800104908`/`29800104899`/`29800104894` and PR
  `29800106522`/`29800106523`/`29800106590` passed all jobs. Human copy/RTL review, other clients,
  signing, and stable release remain open.

- [x] Export the fallback-consent accessible name on the Linux checkbox itself. Code head `6c1d89f`
  adds the localized GTK Accessible Label property and test assertion; packaging head `e0eb471`
  repins Flatpak to the exact source, and final docs head `5bc870b` records the result. Final push
  Native/Flatpak/Foundation `29801182286`/`29801182297`/`29801182271` and PR
  `29801183970`/`29801183976`/`29801183979` passed all jobs. The earlier PR Native keyboard-focus
  race and rerun are retained in Linux status. Human Orca listening, physical review, other
  clients, signing, and stable release remain open.

- [x] Refresh the Linux testing-guide validation boundary. Documentation head `175eb00` records
  the automated GTK/AT-SPI, headless Orca, portal, Flatpak, localization-invariant, and storage
  evidence already exercised, and narrows the remaining list to human screen-reader/copy/RTL
  review, physical desktop and broader X11 coverage, prompted Secret Service approval, broader
  filesystem races, dependency/license/advisory automation, signed artifacts, stable-release
  authorization, and other native clients. Push Native/Flatpak/Foundation
  `29801687294`/`29801687305`/`29801687356` and PR
  `29801689279`/`29801689288`/`29801689275` passed all jobs.

- [x] Cover the Linux final database-component replacement race. Code head `93fd6f2` adds a
  deterministic regression that places a symlink at the final database path after pathname
  preflight and requires the production `O_NOFOLLOW` open to reject it without modifying the
  target; packaging pin `2ce550d` and evidence head `6b8cdc8` preserve the exact source lineage.
  Local no-default/demo-provider suites, strict Clippy, localization audits, formatting, and
  Flatpak metadata passed. Push Native/Flatpak/Foundation
  `29802525642`/`29802525571`/`29802525612` and PR
  `29802527738`/`29802527705`/`29802527681` passed all jobs. Broader filesystem/VFS and power-loss
  behavior remain outside the claim.

- [x] Refresh the Linux testing-guide suite counts. Documentation head `6b8cdc8` replaces stale
  54/104-test descriptions with the observed no-default/demo-provider totals (`81 passed; 1
  ignored` / `147 passed; 3 ignored`) and names the external prerequisites for ignored cases. Final
  push Native/Flatpak/Foundation `29802930525`/`29802930632`/`29802930547` and PR
  `29802932689`/`29802932707`/`29802932683` passed all jobs.

- [x] Validate the Linux AT-SPI status/error role boundary without weakening evidence. Attempted
  head `995c9fa` required live `ROLE_STATUS`/`ROLE_ALERT` and failed Native because the pinned GTK
  bridge exported empty regions as `ROLE_LABEL`; corrected head `a4c9d3f` reverts that incompatible
  assertion and records the failure while retaining GTK unit-level semantic-role checks. Corrected
  push Native/Flatpak/Foundation `29803843127`/`29803843131`/`29803843157` and PR
  `29803845060`/`29803845055`/`29803845046` passed all jobs. A runtime-compatible live status/error
  fixture and human Orca review remain open.

- [x] Verify localized names in the Linux live AT-SPI tree. The test-only
  `LINGUAMESH_TEST_LOCALE` override runs the existing English fixture and a second Simplified
  Chinese fixture without changing ordinary startup defaults; both retain the named-control role
  and two-text-editor assertions. The first run exposed the expected stale Flatpak source pin;
  final head `b2a3f47` documents the corrected pin `346b949`. Push Native/Flatpak/Foundation
  `29804861125`/`29804861156`/`29804861132` and PR
  `29804863422`/`29804863440`/`29804863421` passed, and the Native log records all five Chinese
  accessible names. Human Orca listening, visual/RTL review, other clients, signing, and stable
  release remain open.

- [x] Project the five-dimension Core compatibility snapshot through ABI 1 and consume the exact
  Core pin from Linux. Core `c559b32` passed CI `29782822854` and Native SDK `29782822883`; Linux
  `b38a8fd` passed PR Native/Flatpak/Foundation `29783023917`/`29783023872`/`29783023894` with
  jobs `88488352790`/`88488352708`/`88488352736`. File-lease projection, other clients, and stable
  release remain open.

- [x] Verify and reconcile the macOS native text slice at PR `getio0909/linguamesh-macos#1`.
  Branch `agent/macos-native-slice` head `cad822c` pins project `b75d4d1`, Core `0db51464`, and
  l10n `7e8c987`; Native CI `29765906044` passed build, tests, bundle, and ad-hoc signing smoke
  checks. Typed host-secret transport, model discovery, persisted routing profiles, document jobs,
  notarization, and stable release remain open.

- [x] Verify the Linux Automatic routing worker slice at code head `0e2ae25` and documentation
  head `75910c8`. The integration regression proves Core quality ranking selects the higher-quality
  saved candidate, then a retryable failure switches only through the explicitly approved fallback
  chain. Local Linux tests passed (`142 passed; 3 ignored`); final documentation-head push/PR
  Native, Flatpak, and Foundation gates passed (`29767680041`/`29767680024`/`29767680047` and
  `29767684643`/`29767684366`/`29767684440`). The earlier code-head stale-pin Flatpak failures
  (`29767075134`/`29767080595`) remain recorded as corrective evidence. The Linux PR remains
  Draft/Open and the release train remains unreleased.

- [x] Add and remotely verify the Linux GTK fallback-approval dialog lifecycle at code/pin head
  `62d70b1`. The dedicated serialized fixture proves the production modal warning is focusable,
  `Close` leaves approval and dispatch untouched, and one `Translate` action records one-shot
  approval and exactly one dispatch. Push Native/Flatpak/Foundation gates
  `29770058909`/`29770058926`/`29770058895` and PR gates
  `29770062559`/`29770062414`/`29770062090` passed. The earlier thread-bound GTK, stale-pin, and
  mnemonic-label failures remain documented. Central coordination `29770588175` passed for
  commit `7f2b151`; the PR stays Draft/Open and the release train stays unreleased.

- [x] Add and remotely verify the Linux GTK routing candidate dialog accessibility lifecycle at
  code/pin head `1c47ff9`. The dedicated fixture checks the labelled profile ID field, stable mode
  choices, explicit fallback control, focusable candidates, accessible movement labels, row
  reordering, Manual single-candidate enforcement, and Use close-and-select behavior. Push
  Native/Flatpak/Foundation `29771475803`/`29771475775`/`29771475669` and PR gates
  `29771479057`/`29771478869`/`29771478884` passed; the PR remains Draft/Open and the release
  train remains unreleased.

- [x] Add and remotely verify Linux explainable routing diagnostics at source/pin head `ab82f36`.
  Core-validated eligible candidates, rejected candidates with stable reason codes, ranking inputs,
  and fallback order now flow through Worker events into the localized GTK diagnostics panel without
  endpoints, credentials, or translated content. Local no-default/demo-provider suites passed
  (`80 passed; 1 ignored` and `142 passed; 3 ignored`); push Native/Flatpak/Foundation
  `29773735297`/`29773735296`/`29773735294` and PR gates `29773738883`/`29773738887`/
  `29773738924` passed. Documentation head `458a920` passed push Native/Flatpak/Foundation
  `29774707677`/`29774707852`/`29774708075` and PR gates `29774709730`/`29774709849`/
  `29774710165`. The Linux PR remains Draft/Open and the release train remains unreleased.

- [x] Add and remotely verify the Linux bounded routing retry policy at documentation head
  `2a75ac0`. Core `c03bd205` carries bounded, optional Retry-After hints from all four HTTP
  adapters; Linux source/pin `4b34576` applies an eight-second maximum backoff with stable jitter,
  shutdown cancellation, and a two-failure/30-second in-memory circuit breaker. Core CI/Native SDK
  `29776309259`/`29776309263` and Linux source/pin push/PR Native, Flatpak, and Foundation gates
  `29776662997`/`29776663334`/`29776662987` and `29776667400`/`29776667014`/`29776667068` passed.
  Documentation-head push Native/Flatpak/Foundation `29777101390`/`29777101871`/`29777101540` and
  PR gates `29777102953`/`29777103017`/`29777103023` also passed. The Linux PR remains Draft/Open
  and the release train remains unreleased. Central coordination commit `adaa2a1` passed workflow
  `29777574182`.

- [x] Move bounded retry and circuit-breaker limits into the shared Core `RetryPolicy` contract and
  consume it from Linux routing. Core `8790eb4` passed CI/Native SDK `29778375725`/`29778375728`;
  Linux code/pin `3ff10f4` and documentation head `eb7e578` passed push Native/Flatpak/Foundation
  runs `29778624703`/`29778624674`/`29778624715` and PR runs
  `29778626906`/`29778626865`/`29778626849`. Local Core and Linux validation is recorded in both
  repositories. Final Linux status head `857dac3` passed push Native/Flatpak/Foundation
  `29779357668`/`29779357649`/`29779357690` and PR
  `29779360891`/`29779360949`/`29779361066` (jobs
  `88476555747`/`88476555602`/`88476555686` and
  `88476567289`/`88476567432`/`88476567728`). The Linux PR remains Draft/Open and the release
  train remains unreleased.

- [x] Enforce shared `RetryPolicy` bounds at the serialized Core boundary. Core
  `6e8c40224943a6ba892e5a064fb3b00657b3bf47` validates deserialized policy fields through the
  constructor, and Linux documentation/source-pin head `5b807093c05995a3029e60bb3563ba55200597f9`
  consumes that exact revision. Core domain/engine/FFI tests and Linux no-default/demo-provider,
  strict Clippy, localization, and Flatpak metadata checks passed. GitHub Foundation/Native/
  Flatpak gates `29780440569`/`29780440461`/`29780440421` passed (jobs
  `88480156512`/`88480156210`/`88480155904`). The Linux PR remains Draft/Open and the release
  train remains unreleased.

- [x] Project the one-time host-secret flow through ABI 1. Core
  `adc1e26f37db3761406bb30aa7515003a8bd2717` adds the optional non-secret `secret_ref` command
  field, `secret_required` event, and matching one-shot `host_secret_response`; FFI tests cover
  authenticated loopback streaming, correlation checks, replay rejection, bounded resolutions,
  and terminal event ordering. Core CI/Native SDK `29781845494`/`29781845502` passed. Linux
  documentation/source-pin head `016c4d79131b08ad5eb66e0b7561b9e3e50f02b0` consumes the exact
  revision; Linux Foundation/Native/Flatpak gates `29781942858`/`29781942757`/`29781942821`
  passed (jobs `88484970323`/`88484969938`/`88484969961`). The Linux PR remains Draft/Open and
  the release train remains unreleased.

- [x] Add the Linux-first request-level `TranslationPreset` contract, localized GTK General/
  Technical/Marketing selector, Core prompt/memory identity propagation, compatibility guard, and
  schema-18 persistence through Linux document creation, routed dispatch, pause, retry, and restart.
  Assumption: Android, Windows, and macOS remain out of scope for this checkpoint.

- [x] Add Linux routing-profile JSON exchange: Core-bounded non-secret serialization, GTK import/
  export file actions, duplicate-ID protection, and malformed/unknown-field/size validation.
  Assumption: import never overwrites an existing profile; replacement remains an explicit edit.

- [x] Reconcile central evidence for Linux document-job routing: saved document-capable candidate
  selection and non-secret profile-ID restart recovery are implemented and remotely verified;
  document fallback and cross-client routing remain disabled.

- [x] Read the active goal attachment, `AGENTS.md`, and `PROJECT_GOAL.md` completely.
- [x] Confirm that `PLANS.md` was absent before creating this plan.
- [x] Confirm that `linguamesh-project` initially contained only `PROJECT_GOAL.md`, `AGENTS.md`, and ignored local Codex configuration, with no Git repository.
- [x] Audit all canonical local repository names and public candidates under the only non-authoritative owner hint.
- [x] Resolve the authenticated GitHub owner as `getio0909` using `gh auth status` and `gh api user`.
- [x] Record host toolchains and unavailable-platform constraints.
- [x] Create, validate, and locally commit the central, localization, Android, Windows, macOS, and Linux repository foundations.
- [x] Implement, validate, and locally commit the first Rust core/CLI checkpoint.
- [x] Complete Checkpoint 0 and publish verified repository foundations to all seven public repositories.
- [x] Obtain GitHub Actions evidence for the published Rust CLI vertical slice and all repository foundations.
- [x] Publish and remotely verify the localization `0.1.0` development bundle, generated native resources, pseudo-locales, and deterministic checksum.
- [x] Deliver and remotely verify the first native Linux GTK text-translation checkpoint with
  session-only local-provider switching, real streamed output, cancellation, rollback, and a
  serialized D-Bus/Xvfb button test.
- [x] Deliver and remotely verify Linux non-secret multi-profile create, update, switch, delete,
  restart restoration, exact-ID state handling, and credential-isolation behavior.
- [x] Deliver and remotely verify derived Linux provider setup, safe worker/storage degradation,
  and Linux-side authenticated A/B next-request routing for remembered model switches.
- [x] Run the same real Linux GTK flow under both X11/Xvfb and forced Wayland/headless Weston,
  with bounded compositor startup and cleanup and no X11 fallback in the Wayland gate.
- [x] Reject real post-startup Linux `ENOSPC` persistence failures before false success, preserve
  the prior validated session in memory, and verify restart recovery of only pre-fault state.
- [x] Deliver and remotely verify baseline Linux GTK accessibility semantics on the existing GTK
  4.10+ boundary, including roles, labels, relations, focusability, hidden errors, and Busy reset.
- [x] Complete the active Linux-first secure-provider checkpoint described below, including the
  isolated prompted store/delete fail-closed fixture; end-user Secret Service prompt approval
  remains a later Linux boundary.
- [x] Expose all twelve official Linux PO packs through runtime locale switching, preserve active
  state during action-label changes, and apply Arabic RTL root direction. Source-level visible
  gettext coverage is now separately verified above; human translated-copy and plural review remain
  explicit boundaries.
- [x] Add Linux translation export through the native GTK save dialog, asynchronous UTF-8 writing,
  localized success/error messages, and source-file overwrite protection; cross-platform export
  remains out of scope for this Linux-first checkpoint.
- [x] Add explicit Linux standard-text fallback routing: only a different user-approved saved
  provider may receive a retryable network/timeout retry; document jobs, cancellation,
  authentication/model failures, unapproved profiles, and session-only profiles never fall back.
- [x] Verify Linux completion-notification transport through a private
  `org.freedesktop.Notifications` service with fixed generic payloads and no source/translated
  content; desktop-shell rendering remains an explicit boundary.
- [x] Verify headless Linux notification delivery to a real `dunst` daemon under Xvfb, including
  service-name acquisition, GTK `Notify` delivery, generic-payload privacy assertions, and a visible
  viewable Dunst desktop-shell window; physical compositor/GPU rendering remains an explicit boundary.
- [x] Verify the Linux XDG document-portal lease lifecycle against real portal services, including
  file-descriptor add, host-path mapping, application permission grant/revoke, and deletion;
  interactive application callbacks are covered by the dedicated GTK fixture below.
- [x] Verify the real `xdg-desktop-portal-gtk` FileChooser backend under Xvfb with an actual
  `FileChooser.OpenFile` request, visible chooser selection, returned URI, and UTF-8 contents;
  verify the application-level GTK FileDialog callback and a real source-editor URI-list drag/drop
  gesture with the native GTK fixtures.
- [x] Add the first Linux-first local history vertical slice: Core schema 3 bounded SQLite history,
  standard completion persistence, Incognito skip, startup count restoration, clear-all control,
  and localized Linux status/action copy.
- [x] Add the Linux history inspection window, newest-first Core listing, exact per-entry deletion,
  and deterministic escaped UTF-8 TSV export.
- [x] Add a persisted Linux history enable/disable policy that preserves existing entries, blocks
  future standard writes while disabled, and restores across Core storage reopen.
- [x] Add optional Linux translation memory with versioned request identity, Incognito bypass,
  persisted enable/disable policy, cache reuse, inspection, export, exact deletion, and clear-all.
- [x] Add the bounded Core TXT/Markdown document contract with preserved line endings and
  Markdown fenced structure, and route Linux native text import through it.
- [x] Add bounded Core schema-6 document-job/segment persistence and Linux worker startup recovery,
  explicit segment updates, resume/cancel state transitions, and path/credential exclusion tests.
- [x] Extend the Linux-first document slice with bounded CSV parsing, selected-column segmentation,
  safe provider-field decoding/re-encoding, schema-9 persistence migration, and native `.csv`
  chooser coverage.
- [x] Extend the Linux-first document slice with bounded JSON parsing, exact RFC 6901 include/exclude
  paths, primitive/key protection, escaping preservation, schema-9 mapping, and native `.json` chooser
  coverage.
- [x] Extend the Linux-first document slice with bounded structural HTML tag-stack validation,
  script/style protection, visible text-node segmentation, safe text escaping, schema-9 mapping, and
  native `.html`/`.htm` chooser coverage.
- [x] Add Linux GTK presentation for persisted document jobs, including a non-blocking list command,
  progress/state metadata, empty-state handling, and selection back into the existing job controls.
- [x] Localize Linux document-job row format, lifecycle state, and completed/total metadata through
  the canonical l10n catalog, replacing Rust debug-format presentation.
- [x] Add native Linux DOCX/XLSX package regression fixtures that exercise wrapper import and Core
  reconstruction while preserving non-text package parts, formulas, numbers, and unselected values.
- [x] Add native Linux malicious-DOCX fixtures that reject ZIP path traversal and oversized
  uncompressed entries before import.
- [x] Verify native Linux queue listing returns multiple pending jobs for explicit selection.
- [x] Verify Linux bounded concurrent document execution: four jobs may run with per-job event and
  cancellation isolation, while duplicate and fifth starts are rejected before Running persistence.
- [x] Verify native Linux worker translation reconstructs DOCX/XLSX jobs end to end while retaining
  binary resources, formulas, and numeric cells.
- [x] Publish and remotely verify the shared Core `routing_planner_v1` contract and Linux exact
  compatibility pin; GTK automatic/ordered routing controls remain a later client slice.
- [x] Close the Linux source-level compound-summary gettext gap for history/memory metadata,
  document-job IDs, active-provider mode summaries, and unavailable provider/model labels; l10n
  and Linux remote Native/Foundation/Flatpak gates passed at the pinned revisions.
- [x] Add Linux routing-profile persistence and a catalog-backed non-secret profile editor on top
  of Core `routing_planner_v1`; ordinary-text dispatch and Ordered/Automatic fallback execution
  are verified, while document-job selection is now covered by the Linux document-routing slice.
- [x] Execute Linux ordinary-text Ordered/Automatic routing fallback chains, including unavailable
  candidate connection skipping, retryable stream-failure switching, typed fallback events, and
  event-sequence/partial-output preservation; document-job routing remains out of scope.
- [x] Route Linux document jobs through a selected saved document-capable routing candidate,
  persist the selected provider/model options, preserve pause/resume segment state, and keep
  document-job fallback disabled.
- [x] Persist the non-secret routing-profile ID in Core schema 16 and reconnect that saved profile
  for Linux document Resume/Retry after worker restart; legacy snapshots without an ID retain their
  provider/model resume path.
- [x] Expose Linux GTK routing-profile mode selection (`Manual`, `Ordered`, `Automatic`) and an
  explicit fallback-consent checkbox defaulting off; verify the Core mode order and local routing
  validation without expanding scope to other clients.
- [x] Add and verify the Linux-first Google Gemini Generate Content provider slice with deterministic
  model discovery, SSE streaming, cancellation, redacted diagnostics, localized GTK preset copy,
  and pinned Core/l10n compatibility revisions.
- [x] Add and verify the Linux-first Azure OpenAI provider slice with resource/deployment URL
  validation, pinned API version, `api-key` session authentication, manual deployment selection,
  deterministic Core/Linux fixtures, localized GTK copy, and synchronized Core/l10n pins.
- [x] Add and verify the Linux-first OpenAI Responses provider slice with `/v1/models` discovery,
  Bearer session authentication, typed `/v1/responses` SSE decoding, deterministic Core/Linux
  fixtures, localized GTK copy, and synchronized Core/l10n/Flatpak pins.
- [x] Publish the accepted ABI 1 engine-bound buffer ownership RFC/ADR and keep the central issue,
  Core ABI contract, and migration documentation aligned without claiming a stable SDK release.
- [x] Add Linux routing-profile candidate selection for enabled saved provider/model pairs, preserve
  the displayed order, reject unknown IDs and empty selections, and verify the remote Linux gates.
- [x] Add keyboard-focusable Linux up/down controls for routing candidate ordering, persist the
  resulting Ordered sequence, and verify the bounded reordering helper and remote gates.
- [x] Add catalog-backed accessible labels and tooltips for Linux routing candidate movement
  controls, regenerate all official PO/MO packs, pin the l10n revision in CI, and verify remote gates.
- [x] Exercise the routing-profile candidate movement controls through the serialized GTK dialog
  lifecycle after restored provider profiles are available; click the sorted first candidate's
  Down and Up callbacks, assert visible order changes and restoration, and record push/PR Native,
  Flatpak, and Foundation evidence without changing the Linux production source pin.
- [x] Add Linux GTK text drag sources and row drop targets for routing candidates, persist the
  resulting Ordered sequence, reject invalid drag payloads, and verify push/PR gates.
- [x] Add Linux Edit/Save routing-profile actions that restore mode, consent, candidate order, and
  stable ID, then verify same-ID upsert without duplicate records.
- [x] Add a Core-compatible Linux routing-profile ID field so new profiles can use distinct stable
  IDs while existing edits lock their ID; verify localized validation, generated resources, and
  push/PR gates.
- [x] Reject new Linux routing-profile IDs that already exist, while preserving explicit Edit
  upsert behavior; verify localized error coverage and all push/PR gates.
- [x] Expose Core routing preference, local/remote, privacy, streaming, and document constraints in
  the Linux profile editor; preserve hidden constraints during Edit/Save and verify all gates.
- [x] Expose provider/model allowlists and denylists plus minimum-quality and request-size limits in
  the Linux profile editor; preserve Core fields during Edit/Save and verify all gates.
- [x] Enforce Linux visible-string localization coverage with a dependency-free GTK source audit,
  run it in Native/Foundation CI, and verify the pinned l10n resources and all Linux gates.
- [x] Make the Flatpak Linux source pin build-input compatible with the current checkout, validate
  it before the SDK build, and verify full-history push/PR gates.
- [x] Emit CI-only SHA-256 and deterministic SPDX SBOM sidecars for the Linux Flatpak bundle and
  verify their upload without claiming a stable release artifact.
- [x] Build and remotely verify a Linux release-mode native binary with SHA-256, deterministic SPDX
  SBOM, and fixed build-context sidecars; retain it as unsigned prerelease evidence only.
- [x] Add and remotely verify a repository-only Linux source archive with a SHA-256 entry in the
  native evidence artifact; keep sibling Core/l10n pins and stable-release authorization explicit.
- [x] Capture and remotely verify a machine-contextual Linux performance baseline for document
  reconstruction and saved-routing dispatch without claiming portable performance numbers.
- [x] Add and remotely verify a Linux source-level localization placeholder audit for literal
  fallback templates, keeping malformed braces and placeholder drift out of GTK/release gates.
- [x] Add Linux-first translation quality modes with synchronized Core, localization, GTK, storage,
  prompt-contract, output-validation, and Flatpak source-pin evidence.
- [x] Consume the validated Core provider catalog in the Linux GTK preset flow, derive model-listing
  policy from the catalog, and fail closed on adapter drift.
- [x] Persist Linux document-job quality modes through Core schema 17, restore them on queue
  selection and worker restart, and verify routed `Best` recovery.
- [x] Add an explicit Linux provider connection test that discovers models in a temporary session,
  preserves the active profile/model and storage, clears entered credentials immediately, and
  reports localized typed success/failure results.
- [ ] Continue through Milestones 2–8 and all 20 mandatory acceptance scenarios.

- [x] Strengthen Linux Scenario 13 keyboard evidence. Code head `743ddae` adds a real Arabic RTL
  Xvfb/xfwm4 focus traversal with a production workspace-direction assertion; Flatpak pin head
  `fedc1a9` and status/docs head `23c3a56` passed push Native/Flatpak/Foundation
  `29819019804`/`29819019831`/`29819019803` and PR Native/Flatpak/Foundation
  `29819022552`/`29819022529`/`29819022599`. Manual visual, translated-copy, and screen-reader
  review remain open.

- [x] Correct the Linux storage-race evidence boundary. Code head `59b57c0` now adds regular-file
  parent and hard-link final-component replacement regressions after preflight; docs/status head
  `b078b8e` records the evidence. Final push Native/Flatpak/Foundation
  `29817292493`/`29817292344`/`29817292390` and PR Native/Flatpak/Foundation
  `29817295183`/`29817295210`/`29817295244` passed. Status-only docs head `b078b8e` then passed
  push Native/Flatpak/Foundation `29817714165`/`29817714101`/`29817714200` and PR
  `29817717903`/`29817717896`/`29817717877`. Broader same-UID filesystem/VFS variants and
  power-loss behavior remain open.

- [x] Harden the Linux storage race against same-UID alternate-directory replacement. Code
  `14bb30e814d6d4ffcbf55c5a409d3729db2af967` retains the preflight parent device/inode and rejects
  a distinct private directory after descriptor acquisition; packaging pin `2dc3e49` and status/docs
  head `b301991` record the evidence. Corrected source-pin push/PR Native/Flatpak/Foundation runs
  `29833316179`/`29833316220`/`29833316231` and `29833318520`/`29833318770`/`29833318526` passed;
  status-head push/PR runs `29833853428`/`29833853406`/`29833853465` and
  `29833858405`/`29833858644`/`29833858612` also passed. Broader VFS variants and power-loss
  behavior remain open.

- [x] Harden the Linux final database leaf against same-UID replacement and creation races. Code
  `a7cee699bd973c8f05893c37b5583dd8c4998471` pins the preflight leaf device/inode, rejects a
  distinct regular-file replacement after descriptor acquisition, and uses exclusive creation
  for a missing leaf; packaging pin `87361ec9fbe37417dbf83f64b181cb834a5a4aa7` and status/docs
  head `5ae3b579d7393511d1a8fbdeedbdc86f1678df98` record the exact lineage. The first code-head
  Flatpak run `29834999139` failed only on the stale source pin; corrected push Native/Flatpak/
  Foundation `29835149907`/`29835149914`/`29835149955`, PR `29835154608`/`29835154630`/
  `29835155142`, status-head push `29835701523`/`29835701634`/`29835701563`, and status-head PR
  `29835705780`/`29835705840`/`29835706300` passed. Broader VFS variants and power-loss behavior
  remain open.

- [x] Reject pre-existing Linux SQLite WAL/SHM sidecar aliases before Core opens a profile
  database. Code `2077efb3349505b1125c8f0c686fd707ba439628` inspects both sidecars through the
  pinned parent with `O_PATH|O_NOFOLLOW` and rejects non-regular or hard-linked aliases; the
  regression covers both suffixes and proves an external hard-link target is unchanged. Packaging
  pin `a220b18cfadffdcc39d40b9739cc510c66d45880` and status/docs head
  `2362a5f213098c4cfc0a44580c17ae08dad20094` record the exact lineage. The first code-head
  Flatpak push/PR runs `29837248939`/`29837255929` failed only on the stale pin; corrected
  source-pin push `29837460916`/`29837461045`/`29837460822`, PR
  `29837463776`/`29837464358`/`29837464171`, status-head push
  `29838016659`/`29838016535`/`29838016509`, and status-head PR
  `29838022061`/`29838022446`/`29838022044` passed. Sidecar replacement after inspection,
  broader VFS behavior, and power-loss behavior remain open.

- [x] Recheck Linux SQLite sidecar identities after Core migration/open. Code
  `c6c5528314ddef98f2ac5f24aac8202b0e0d62d1` retains the pinned parent descriptor and pre-open
  `-wal`/`-shm` identities, failing closed when an existing sidecar changes identity or becomes an
  invalid alias; absent sidecars may still be created by SQLite and are validated after open. The
  deterministic atomic-rename regression corrected the inode-reuse failure in PR run
  `29839491260`. Flatpak pin `1432242c96fad806094bf295703dc0df992d882a` and Linux docs/status
  head `49ea6212eba69c614403edf90d1e5ad9f044c26f` record the lineage. Corrected push/PR six-gate
  runs `29839920685`/`29839920594`/`29839920501` and
  `29839923879`/`29839924044`/`29839923994`, plus final status-head push/PR six-gate runs
  `29840468206`/`29840467826`/`29840468229` and
  `29840473167`/`29840473177`/`29840473045`, passed. Replacement after the second inspection,
  broader VFS behavior, and power-loss behavior remain open.

- [x] Strengthen Linux Scenario 16 compatibility rejection. Linux code head `f53c44d` now rejects
  Core semantic-version, ABI-major, protocol-version, provider-catalog, and required-feature
  mismatches before provider work; docs/status head `92b5136` records the evidence. The first
  Flatpak attempt failed because its manifest still referenced ancestor `12e810b`; corrected pin
  `f53c44d` passed the replacement gate. Final push Native/Flatpak/Foundation
  `29815397653`/`29815397736`/`29815397742` and PR Native/Flatpak/Foundation
  `29815402318`/`29815402263`/`29815402242` passed. Other clients, human review, broader VFS/power
  loss behavior, signing, and stable release remain open.

- [x] Verify the Core SQLite WAL replay regression through the Linux client. Core
  `4badabe735499a50265a1260a838df3254622c15` adds a bounded writer-disconnect test that restores a
  committed provider profile from the WAL sidecar after a reader snapshot; Core workspace tests,
  Clippy, and the reproducible Linux SDK package smoke passed. Linux `9406d3a` pins that Core
  revision in Native CI and Flatpak. Push Native/Flatpak/Foundation
  `29813283713`/`29813283776`/`29813283818` and PR Native/Flatpak/Foundation
  `29813286614`/`29813286582`/`29813286593` passed all jobs. Power-loss, alternate VFS behavior,
  cross-client persistence, and stable release remain open.

## Completed Linux-first checkpoint — explicit provider connection test

Assumption: connection tests are diagnostics only; they never activate, persist, or replace the
current session and are disabled while translation/document work is busy.

- Linux `02efde00fb9faf3abfc4ab5dcf19b9c6036be656` adds the worker command/event contract, temporary
  provider manager, cancellation propagation, GTK action, immediate credential-field clearing,
  and a regression covering success, network failure, and continued baseline translation.
- l10n `7e8c987737444d4e0f8f2642b108eee4c7801f58` adds localized action, tooltip, and model-count
  status resources across all official and pseudo-locale outputs.
- Local Linux tests, strict Clippy, localization audits, generated-resource checks, and Flatpak
  metadata validation passed. Push Native/Flatpak/Foundation runs
  `29758801692`/`29758801470`/`29758801642` and PR runs `29758805190`/`29758806520`/`29758805530`
  all passed; central coordination workflow `29759295217` passed. PR #1 remains Draft/Open and
  Issue #1 remains Open.

## Completed Linux-first checkpoint — document quality-mode persistence

Assumption: a document job captures the selected `Fast`, `Balanced`, or `Best` policy at dispatch
time and reuses it for every segment after pause, retry, or process restart; legacy rows default to
`Balanced`.

- Core `f62f2df91584eeebdf5c30bd06c5e0893f2345d8` adds transactional schema 17 migration
  `0017_document_quality_mode.sql`, validated stable names, and restart-safe `DocumentJobOptions`
  persistence. Core offline check, 139 workspace tests, strict Clippy, locked build, and diff checks
  passed; Core CI/Native SDK `29744643575`/`29744643593` passed.
- Linux `c0ac94e25fb7a64b330fee538e64d82405f35aab` passes quality mode through plain and routed
  worker commands, applies it to every document request, restores it into GTK state, and keeps the
  selector enabled for selected jobs. The routed restart regression selects `Best`, resumes after
  shutdown, and asserts the completed snapshot retains `Best`.
- Local Linux GUI check, strict Clippy, 140 tests with 3 ignored, locked build, localization audits,
  Flatpak metadata, and diff checks passed. Linux push Native/Flatpak/Foundation
  `29746095888`/`29746095985`/`29746095892` and PR Native/Flatpak/Foundation
  `29746099123`/`29746099062`/`29746099042` all passed. No merge or stable release was authorized.

## Completed Linux-first checkpoint — translation quality modes

Assumption: quality mode is a request-level deterministic policy shared by Core and Linux; `Best`
uses one provider request with an internal critique/revision instruction and does not imply hidden
extra provider calls or stable-release readiness.

- Core `d304afe01e21023a1e1f37ad8f674d49a23b5d42` adds `Fast`, `Balanced`, and `Best`, the shared
  `translation-prompt-v2` contract, malformed-output validation, and versioned translation-memory
  identity. Core workspace checks, tests, Clippy, and locked build passed locally.
- l10n `e03d8ccc548d7d2eeeef9163b4b12b8204e68d6d` raises the catalog to 410 messages and regenerates
  all official Linux resources. `PYTHON_BIN=/home/wangtinghu/miniconda3/envs/py313/bin/python make check`
  passed locally.
- Linux functional head `aaffb87d4a7e52e64370c082b144fd8e50e84b43` adds the localized GTK selector,
  request propagation, and selection regressions. Flatpak pin `f78574d` follows the source and
  metadata validation passed; Linux local GUI/all-target checks, 140 tests with 3 ignored, strict
  Clippy, localization audits, sync, and diff checks passed.
- Core, l10n, Linux, and central changes are pushed; PR #1 remains Draft/Open and Issue #1 remains
  Open. Core CI/Native SDK `29742242153`/`29742242102`, l10n Localization/Foundation
  `29742198569`/`29742198614`, Linux push Native/Flatpak/Foundation `29742596157`/`29742596195`/
  `29742596247`, Linux PR Native/Flatpak/Foundation `29742602112`/`29742602104`/`29742602095`, and
  central coordination `29742676456` passed. No merge or stable release was authorized.

## Completed Linux-first checkpoint — provider catalog compatibility

Assumption: Core's bundled provider catalog is the authoritative non-secret contract for adapter
types and model-listing policy; Linux retains native localized labels and endpoint defaults, while a
stale mapping must stop before the GTK window is created.

- Linux `f1996faaae591f476ff2610746bd4cbeb9e0b53e` directly consumes Core's
  `linguamesh-provider-catalog` crate at `d304afe01e21023a1e1f37ad8f674d49a23b5d42`, caches the
  bundled catalog, derives manual-model visibility from `model_listing`, and validates all six
  GTK preset adapter mappings before startup. Flatpak pin follows the same head.
- The regression `provider_presets_map_to_stable_native_and_compatible_defaults` covers the stable
  GTK order and catalog compatibility without credentials or network access. A mismatch fails
  closed with an English diagnostic.
- Local Linux formatting, GUI all-target check, strict Clippy, 140 demo-provider tests with 3
  ignored, localization audits/sync, Flatpak metadata, and diff checks passed. Push
  Native/Flatpak/Foundation `29743687368`/`29743687294`/`29743687262` and PR
  `29743689677`/`29743689725`/`29743689515` passed. PR #1 remains Draft/Open and no stable release
  action was taken.

## Completed Linux-first checkpoint — OpenAI Responses typed SSE

Assumption: OpenAI Responses model discovery remains compatible with `/v1/models`; the deterministic
fixture proves request shaping, Bearer session authentication, typed SSE delta/completion handling,
and secret isolation without claiming live account, quota, or model availability.

- Core `58075c997cecdcd9a179b9397cb493da375d3a50` adds `openai_responses`, the typed
  `response.output_text.delta`/`response.completed` decoder, the `openai_responses_v1` feature, and
  deterministic application/testkit coverage. Core CI/Native SDK `29739668055`/`29739668165` passed.
- l10n `95078b1a0c30defe98995a9879c4c669d213e5bc` contains 405 messages and generated resources;
  Localization/Foundation `29739956505`/`29739956524` passed.
- Linux functional head `498323ee09a69f3183b903278efcab137836c3fb` adds the localized six-item preset
  list and `openai_responses_provider_discovers_and_streams_typed_sse`; Flatpak pin head is
  `62385d4228750711f232381805bbdab2f560b309`. Local Linux GUI check, 139 passing tests with 3
  ignored, strict Clippy, l10n sync/audits, and Flatpak metadata validation passed.
- Linux push Native/Flatpak/Foundation `29740264065`/`29740263971`/`29740263996` and PR
  Native/Flatpak/Foundation `29740261207`/`29740261147`/`29740261173` all passed. PR #1 remains
  Draft/Open; central Issue #1 remains Open. Central coordination commit `d8387a7fb8f6027a726f9948fcf45a5192246ba5`
  passed validation run `29740781908` for Linux and PowerShell; other clients and stable release
  remain out of scope.

## Completed cross-repository checkpoint — ABI 1 engine-bound buffer ownership

Assumption: the ABI 0 source skeleton has no released binary consumers, so the safe engine-bound
buffer transition can be accepted before any stable SDK artifact is published.

Central commit `81d3f3c37e6fde54da21034e60d716c56b67e981` publishes accepted RFC-0001 and ADR-0004.
They require ABI major 1, `lm_engine_buffer_free(engine, buffer)`, bounded per-engine allocation
registries, token/pointer/length/capacity validation, and wrapper-side copy-and-release behavior.
Core already implements and tests that contract at `638713c34ce7d5bcc8003bb0d7e54c514ab49ea7`;
the release manifest remains `unreleased` because no stable SDK artifact or compatible four-client
train exists. Central workspace validation passed; coordination CI is pending for this documentation
head.

## Completed Linux-first checkpoint — document-job concurrency isolation

Assumption: before bounded concurrent document execution exists, overlapping starts must fail closed
without cancelling or mutating the active job.

Linux adds `concurrent_document_start_is_rejected_without_interrupting_active_job`. The regression
starts a slow active document, submits a second start during a streamed delta, asserts the typed
configuration rejection, cancels the active job, and verifies the second snapshot remains pending.
Local formatting and the filtered demo-provider test passed (`1 passed; 0 failed`). The Flatpak
source pin follows Linux code head `36b81586b8b148d7adc08ecfc46203b2ef94af4d`; no Core,
localization, workspace-manifest, or release-manifest pin changed. True concurrent document
execution, other clients, signing, rollback, and stable release remain open.
The full local suite passed at code head (`135 passed; 3 ignored`); code-head push/PR Native,
Flatpak, and Foundation runs `29730049695`/`29730049744`/`29730049648` and
`29730052583`/`29730052576`/`29730052602` passed after correcting the initial Flatpak pin failures
`29729850476` and `29729852622`. Documentation head `9fbc995747400528c6680977bb8ee6c0a51d7506`
then passed push/PR Native, Flatpak, and Foundation runs
`29730511966`/`29730512095`/`29730511907` and `29730513799`/`29730513772`/`29730513834`.
Central coordination run `29730453936` passed.

## Completed Linux-first checkpoint — Azure OpenAI provider

Assumption: Linux is the first active client target; deterministic Azure loopback coverage proves
request shaping and session-secret handling while live Azure account, quota, deployment, other
clients, signing, rollback, and stable-release behavior remain unverified.

Core `e46066ccafcd81e50b004c84d7eb8734e77f3279` adds the `azure_openai_chat` adapter with resource
and deployment validation, API version `2024-10-21`, `api-key` authentication, manual deployment
model listing, and a deterministic testkit fixture. Linux `a679d57bf9b4d887d27fdd4c2cb2f87dfd6342db`
adds the localized Azure OpenAI preset and worker regression, while l10n
`8e0e50577f8714b90bcc08a0d22cc790319f9239` supplies the 401-message generated bundle. Local Core,
Linux, localization, and Flatpak validation passed. Core CI/Native SDK
`29738151804`/`29738151858`, l10n Localization/Foundation `29738073868`/`29738073889`, and Linux
push/PR Native/Flatpak/Foundation `29738486868`/`29738486841`/`29738486838` and
`29738489229`/`29738489379`/`29738489251` all passed. Central commit
`df0d3b8994d5466b4a7fe209ab43288bbf689bac` passed coordination run `29738896174` (Linux and
PowerShell). PR #1 remains Draft/Open and Issue #1 remains Open.

## Completed Linux-first checkpoint — Google Gemini Generate Content provider

Assumption: Gemini is an opt-in Linux provider slice; deterministic loopback coverage proves the
wire contract without claiming live account, quota, or stable-release evidence.

Core `232881263f4f523ce54b3713d83513f2d0170ff2` adds `gemini_generate_content` with `/v1beta/models`
discovery, `:streamGenerateContent?alt=sse` candidate streaming, cancellation, protected-span and
glossary restoration, endpoint policy, and redacted `x-goog-api-key` handling. Linux
`df9b0fe261bcbb3cba8d4b8660baa94c891ea44c` exposes the localized Google Gemini preset and keeps
manual-model controls Anthropic-only. l10n `f9d74a8f83a89540a58bba65477a5031031bd619` supplies the
396-message generated Linux bundle. Linux `3edb91c5a17d774edffbd336564cfdc385f75fc5` runs the
same fixture through `ProviderManager` and deliberately selects `gemini-2.0-flash` before
translating `你好，Gemini！` without a credential.

Core workspace tests, strict Clippy, Linux formatting/check/Clippy, demo-provider tests (`136 passed;
3 ignored`), localization synchronization and three audits, Flatpak metadata validation, and diff
checks passed locally. Linux push Native/Flatpak/Foundation `29735086126`/`29735086106`/`29735086081`
and PR `29735088589`/`29735088578`/`29735088610` all passed. The newer worker documentation head
`a698d47945367d4336a739f93185a0519d469fb2` also passed push Native/Flatpak/Foundation
`29736402002`/`29736401951`/`29736401989` and PR Native/Flatpak/Foundation
`29736404211`/`29736404204`/`29736404197`. Core CI/Native SDK
`29735977442`/`29735977484` passed. The PR remains Draft/Open, the central issue remains Open, and
the release train stays `unreleased`. Central coordination `29736748680` and follow-up validation
`29736800710` passed on the resulting documentation heads.

## Completed Linux-first checkpoint — bounded concurrent document execution

Assumption: Linux remains the priority client, so bounded worker concurrency can advance while the
other clients, stable release, signing, and rollback work stay explicitly open.

Linux code head `42b5ff36b3629c3001cda9177c1ba939ada1b478` (Flatpak source pin `3e5b80df851a91c07fbef9cf98c494e142dc4332`) runs up to four document jobs concurrently. Each job has an isolated event pump, cancellation handle, partial output, provider manager, and segment index; duplicate or fifth starts are rejected before a Running snapshot is persisted. Regressions cover independent completion and targeted cancellation of one job while its survivor completes.

Local formatting, GUI all-target check, strict Clippy, demo-provider tests (`136 passed; 3 ignored`),
Flatpak metadata, l10n synchronization, three localization audits, and diff checks passed. Code-head
push/PR Native, Flatpak, and Foundation runs `29732668572`/`29732668556`/`29732668568` and
`29732671353`/`29732671354`/`29732671362` passed. Documentation head
`9dcc5818e757e663d63d2f7b783117057a57a0c0` then passed push/PR runs
`29733047267`/`29733047292`/`29733047328` and `29733050760`/`29733050738`/`29733050725`.
The Linux PR remains Draft/Open and central Issue #1 remains Open; cross-platform clients, human
accessibility/visual review, signing, rollback, and stable-release authorization remain open.
Central coordination commit `cbde16f3323e9fdc68d800dde29ba461c1126c9e` and run `29733527316` passed.

## Completed Linux-first checkpoint — GTK routing candidate reorder behavior

Assumption: Linux candidate-management evidence must exercise the real GTK callbacks and resulting
row order while preserving the existing lifecycle fixture state used by later assertions.

Linux code head `0658f0f31083e0eb90259784dc2bfd0e642412ed` adds two enabled restored provider/model
candidates to the serialized routing-profile dialog regression, clicks the first sorted candidate's
Down and Up controls, verifies the visible order changes and returns to its original order, then
restores the disabled-profile fixture state. Documentation head `bf0906b97ac2f4a7065f0f9cfe7fe4f0e05841af`
records the final evidence and keeps the Flatpak source pin on the code ancestor.

Local formatting, GUI all-target check, strict Clippy, demo-provider tests (`134 passed; 3 ignored`),
Flatpak metadata, localization audits, l10n synchronization, and diff checks passed. The host GTK
test binary remains linker-limited; Native CI is authoritative for GTK runtime behavior.

Final code-head push Native/Flatpak/Foundation `29728346052`/`29728346055`/`29728346087` and PR
`29728348382`/`29728348395`/`29728348472` passed. Documentation-head push
`29728730611`/`29728730516`/`29728730520` and PR `29728732350`/`29728732354`/`29728732411` also
passed. Earlier fixture failures `29727820986` and `29728076058` remain recorded. Human review,
cross-platform parity, signing, rollback, and stable release remain open.

## Completed Linux-first checkpoint — GTK routing candidate accessibility lifecycle

Assumption: candidate-management acceptance requires the production GTK dialog to expose
focusable, screen-reader-labelled controls and preserve the selected profile through Use/close.

Linux code/pin head `1c47ff9b6b103ee16d564480d3dd3cdfcda5e083` adds the ignored serialized
`gtk_routing_profile_candidate_controls_have_accessible_lifecycle` fixture. It constructs the
real dialog with two saved provider/model pairs, checks the labelled profile ID field, stable
Manual/Ordered/Automatic choices, explicit fallback checkbox, focusable candidate checkboxes,
accessible up/down labels, row reordering, Manual cardinality enforcement, and Use selection.
Local formatting, GUI all-target check, strict Clippy, no-default-feature tests (`80 passed; 1
ignored`), demo-provider tests (`142 passed; 3 ignored`), Flatpak metadata, and diff checks passed.
The host has no `xvfb-run`; Native CI is authoritative for runtime GTK/AT-SPI behavior. Push
Native/Flatpak/Foundation `29771475803`/`29771475775`/`29771475669` and PR
`29771479057`/`29771478869`/`29771478884` passed. Visual/translated-copy review, end-user Orca
acceptance, other clients, signing, rollback, and stable release remain open.

## Completed Linux-first checkpoint — third-party Ollama interoperability harness

Change identifier: `LM-CHANGE-2026-07-OLLAMA-INTEROP-HARNESS-1`

Linux head `8645caf3c0504b225a4a44d97fd634af9ab67d0c` adds an opt-in
`tools/run-ollama-interop-test.sh` path plus an ignored worker regression. The harness requires a
real daemon and installed model, keeps credentials out of the test state, and is intentionally not
part of the default offline suite. Local validation passed with 131 tests passed and 3 ignored.

Push Native/Flatpak/Foundation `29712165334`/`29712165338`/`29712165360` and PR
Native/Flatpak/Foundation `29712166849`/`29712166856`/`29712166851` all passed. A temporary Docker
`ollama/ollama:0.11.10` daemon served `/api/tags` and `/api/chat` for
`qwen2.5-0.5b-instruct:latest`; the harness reported `1 passed; 0 failed` without a credential.
The model and daemon were removed after validation; GPU and stable-release evidence remain open.

## Completed Linux-first checkpoint — approved text fallback routing

Change identifier: `LM-CHANGE-2026-07-LINUX-FALLBACK-1`

The Linux client is the only platform in scope for this checkpoint. Fallback is opt-in, limited to
ordinary text requests, and requires a different saved provider selected from the UI. A retryable
network or timeout failure may switch once; the decision is surfaced without exposing endpoints or
content, partial primary output is preserved, and cancellation or non-retryable errors terminate
without trying another provider.

Assumption: this checkpoint remains the explicit single-provider fallback boundary for Scenario 7;
multi-provider Ordered/Automatic execution is recorded in the completed routing fallback checkpoint
below and remains ordinary-text-only.

- [x] Linux `878a9c015d29ce49633046d435f48f5fee4c9a47` implements the opt-in saved-provider
  fallback path, bounded retry policy, partial-output preservation, cancellation boundary, and
  localized decision notice without endpoint or content disclosure. l10n
  `273be8a4e9c3b1084f393ce0086cdf2c42fcd4e9` supplies the six fallback messages.
- [x] Local no-default/demo-provider suites (`61`/`100` tests with one documented environment
  skip), strict Clippy, GUI check, synchronization, and diff checks passed; Native/Foundation/
  Flatpak gates `29659054771`/`29659054755`/`29659054756` passed. The checkpoint remains
  unreleased and Linux-scoped.

## Completed Linux-first checkpoint — shared routing planner contract

Change identifier: `LM-CHANGE-2026-07-ROUTING-PLANNER-1`

Core now owns the non-secret routing policy contract and schema-15 persistence. `RoutingProfile` supports Manual, Ordered, and
Automatic modes, bounded local/privacy/capability/size/locale/quality/latency/cost constraints,
stable rejection reasons, deterministic ranking, and explicit fallback ordering. Linux negotiates
`routing_planner_v1` before provider work and pins Core `9926d0f9bf6394c6011c6cc886d142bfeb54e10f`.
The GTK surface retains the explicitly approved single fallback control while ordinary-text
Ordered/Automatic chain execution is covered by the completed checkpoint below.

Evidence: Core CI `29688550094`, Core Native SDK `29688550109`; Linux push Native/Foundation/Flatpak
`29688581267`/`29688581251`/`29688581258`; Linux PR Native/Foundation/Flatpak
`29688582602`/`29688582637`/`29688582608` all passed.

- [x] Core `d1c03ba84362c0c672c57045a59fc8092db470be` and Linux
  `eba4b036649cdb1fb4b466844b5c0429d3ff4de5` are recorded as the compatible Core routing planner
  contract and Linux feature gate. The contract is shared, bounded, deterministic, and non-secret;
  complete cross-client parity and stable-release evidence remain open.

## Completed Linux-first checkpoint — routing profile persistence/editor

Change identifier: `LM-CHANGE-2026-07-ROUTING-PROFILES-1`

Linux `9cbd4d5a270a004eff8e71c0e813d7648f74068d` adds worker CRUD and a GTK dialog for validated,
non-secret Core routing profiles. It can create a bounded `linux-default` automatic,
local-preferred profile from saved provider/model selections, inspect mode/candidate counts, and
delete profiles. It does not yet select a routing profile for actual translation dispatch.

The l10n catalog is pinned to `5f98f8bf760bb552c5d9e6cc7ace575e427bae10` (350 messages). Local
l10n/Linux/Flatpak validation passed. Linux push Native/Foundation/Flatpak
`29691040234`/`29691040260`/`29691040243` passed, as did duplicate PR-triggered
Native/Foundation/Flatpak `29691041454`/`29691041501`/`29691041451`. Central coordination
commit `bcff9b563df6f72d8a285ba4a29e8ec799d666a0` passed workflow `29691253266`.

## Completed Linux-first checkpoint — ordinary-text saved routing execution

Change identifier: `LM-CHANGE-2026-07-ROUTING-DISPATCH-1`

Linux `128a03ef82a031d69ad55597467d501d0415522d` adds an ordinary-text routing command. The
worker builds a bounded, non-secret Core routing context, selects a candidate through
`routing_planner_v1`, resolves the saved provider profile through the host secret broker, and
streams the result with a typed decision event. The GTK profile dialog now has an explicit Use
action; document jobs and the existing explicit single-provider fallback remain separate paths.

The l10n catalog is pinned to `fade545ec14793893de2603c62e0994689d9c4df` (352 messages). Local
Linux validation passed 124 tests with 2 ignored, GUI check, strict Clippy, localization sync and
228-key audit, Flatpak metadata, and diff checks. Push Native/Foundation/Flatpak runs
`29692401405`/`29692401396`/`29692401402` passed, as did duplicate PR-triggered runs
`29692402861`/`29692402845`/`29692402867`; l10n Foundation/Localization runs
`29691938103`/`29691938112` passed.

Document-job routing, cross-platform pins, accepted draft publication, distributable artifacts, and
stable-release evidence remain open.

## Completed Linux-first checkpoint — ordered/automatic routing fallback execution

Change identifier: `LM-CHANGE-2026-07-ROUTING-FALLBACK-1`

Linux `8a3b806490191f858411c802070ccaea6af606b8` now executes the remaining eligible candidates
from Core `routing_planner_v1` for ordinary text. Ordered and Automatic profiles skip unavailable
saved providers during initial dispatch; retryable network/timeout stream failures reconnect the
next candidate, preserve partial output, remap event sequence numbers, and emit a typed fallback
event without endpoints, credentials, or source content. The GTK surface reuses the existing
generic fallback notice, and document jobs remain separate.

The local Linux suite passed 125 tests with 2 ignored, GUI all-target check, strict Clippy,
formatting, and diff checks. GitHub PR #1 for this head passed Native, Flatpak, and Foundation
push/duplicate-PR gates: Native `29693118757`/`29693117355`, Flatpak `29693118741`/`29693117348`,
and Foundation `29693118742`/`29693117351`.

Assumption: routing fallback remains ordinary-text-only until document-job provider selection and
resume semantics are specified and independently verified.

Complete document-job routing, other clients, accepted draft publication, distributable artifacts,
and stable-release evidence remain open.

## Completed Linux-first checkpoint — document-job saved routing execution

Change identifier: `LM-CHANGE-2026-07-ROUTING-DOCUMENT-1`

Linux `08a85653b303345bc54e242405a537a03fb1ad32` routes a document job through the selected saved
Core routing profile when the candidate is document-capable. The worker resolves the candidate
through the host secret broker, persists the actual provider/model options, emits a typed non-secret
routing decision, and reuses the selected manager for segment continuation and same-process
pause/resume. Document jobs never auto-fallback, even when a profile advertises explicit fallback;
restart recovery currently reuses the persisted provider/model options because the document-job
schema does not yet persist a routing-profile ID.

Local Linux evidence: 126 tests passed with 2 ignored; GUI all-target check, strict Clippy,
formatting, localization sync and 228-key audit, Flatpak metadata, and diff checks passed. Linux
push and PR Native/Flatpak/Foundation gates all passed: Native `29693935010`/`29693936875`,
Flatpak `29693934970`/`29693936887`, and Foundation `29693934974`/`29693936881`.

Assumption: retaining the schema-15 document snapshot and actual selected provider/model is the
smallest complete Linux slice; persisting the profile ID and cross-client routing remain future work.

Other clients, accepted draft publication, distributable artifacts, and stable-release evidence
remain open.

## Completed Linux-first checkpoint — routed document restart recovery

Change identifier: `LM-CHANGE-2026-07-ROUTING-DOCUMENT-RESTART-1`

Core `9926d0f9bf6394c6011c6cc886d142bfeb54e10f` adds schema 16 and a nullable,
non-secret `document_job_options.routing_profile_id` with a transactional migration. Linux
`202f565f65738345d23c3e19b428a99494ad7cfe` persists that ID for routed document jobs and reconnects
the saved profile through the host secret broker for Resume and Retry after restart. Legacy jobs
without an ID continue through their persisted provider/model options; document fallback remains
disabled.

Local Core and Linux validation passed, including the 129-test Linux suite and the dedicated
restart regression. Core CI/Native SDK `29694632345`/`29694632350` passed. Linux push Native and
Foundation `29694926451`/`29694926454` and PR Native/Foundation `29694927642`/`29694927681` passed.
Final Linux push Native/Flatpak/Foundation `29695388000`/`29695388015`/`29695387996` and PR
Native/Flatpak/Foundation `29695389589`/`29695389588`/`29695389602` passed.

Assumption: a nullable route ID preserves backward compatibility for schema-15 snapshots without
persisting endpoints, credentials, source content, or translated content.

## Completed Linux-first checkpoint — routing candidate selection

Change identifier: `LM-CHANGE-2026-07-ROUTING-CANDIDATES-1`

Linux `cd9df9fff290fa2f3ebaf64fcf8e5819039eaf7f` adds focusable candidate checkboxes for enabled
saved provider/model pairs to the routing-profile dialog. The selected IDs are filtered against
current saved profiles and serialized in displayed order; an empty selection fails through the
existing fixed no-candidate error. Regression `routing_candidate_selection_preserves_order_and_rejects_unknown_profiles`
proves deterministic order and unknown-ID rejection without exposing endpoints, credentials, or
content.

Local Linux validation passed with 131 tests (`129 passed; 2 ignored`), GUI check, strict Clippy,
formatting, l10n sync/audit, Flatpak metadata, and diff checks. Push Native/Flatpak/Foundation
`29697021191`/`29697021176`/`29697021171` and PR Native/Flatpak/Foundation
`29697022738`/`29697022740`/`29697022751` passed after a cleanup-only AT-SPI rerun.

Drag/drop candidate ordering, complete candidate management, other clients, artifacts, and stable
release remain open.

## Completed Linux-first checkpoint — routing candidate ordering

Change identifier: `LM-CHANGE-2026-07-ROUTING-CANDIDATE-ORDER-1`

Linux `21d79530fbb7aedafe3fdc8a025e4db18c285fc4` adds focusable up/down controls beside enabled
routing candidates. GTK rebuilds the rows after a bounded move, and the selected IDs are persisted
in the resulting Ordered-mode sequence. `move_routing_profile_id` rejects unknown and out-of-range
moves; `routing_candidate_reordering_is_bounded` covers forward, reverse, boundary, and missing IDs.

Local Linux validation passed with 132 tests (`130 passed; 2 ignored`), GUI check, strict Clippy,
formatting, l10n sync/audit, Flatpak metadata, and diff checks. Push Native/Flatpak/Foundation
`29697776890`/`29697776947`/`29697776897` and PR Native/Flatpak/Foundation
`29697778336`/`29697778335`/`29697778323` passed; the Push Flatpak run was rerun after a transient
Flathub network failure.

Drag/drop ordering, complete candidate management, other clients, artifacts, and stable release
remain open.

## Completed Linux-first checkpoint — routing candidate drag ordering

Change identifier: `LM-CHANGE-2026-07-ROUTING-CANDIDATE-DRAG-1`

Linux `c0cdee8b729a6800904f6754f30221feb55f78e` adds GTK text drag sources and row drop targets
to the routing-profile dialog. Dropping a candidate before another row rebuilds the list and
preserves the resulting Ordered-mode sequence used by profile creation. The Core-facing
`move_routing_profile_id_before` helper rejects self, unknown, and missing target IDs, with
`routing_candidate_drag_reordering_is_bounded` covering those boundaries.

Local Linux formatting, GUI all-target check, strict Clippy, 131 passing demo-provider tests with 2
ignored, localization sync/key audit, Flatpak metadata, and diff checks passed. Push
Native/Flatpak/Foundation runs `29699210798`/`29699210802`/`29699210801` and PR
Native/Flatpak/Foundation runs `29699211832`/`29699211818`/`29699211830` all passed after a
cleanup-only AT-SPI rerun. Full profile editing, Orca speech, visual review, other clients,
artifacts, and stable release remain open.

## Completed Linux-first checkpoint — routing profile edit/upsert

Change identifier: `LM-CHANGE-2026-07-ROUTING-PROFILE-EDIT-1`

Linux `a4dd4aa644335a3b6539db4d40473423c6292c71` adds an **Edit** action to each saved routing
profile row. The editor restores the persisted mode, explicit fallback consent, candidate checks and
order, and stable profile ID; **Save routing profile** preserves hidden constraints and replaces the
same ID through the existing storage upsert path. The worker regression verifies one updated record,
without endpoints, credentials, or source content.

l10n `aea172c15f421da09a0c848accae7c443820fb27` adds the edit/save actions to all twelve official
packs and produces a 356-message bundle. Local Linux/l10n checks passed. Push
Native/Flatpak/Foundation runs `29699870066`/`29699870068`/`29699870071` and PR
Native/Flatpak/Foundation runs `29699871302`/`29699871301`/`29699871311` all passed. Full
fallback-chain editing, Orca speech, visual review, other clients, artifacts, and stable release
remain open.

## Completed Linux-first checkpoint — editor text metrics

Change identifier: `LM-CHANGE-2026-07-TEXT-METRICS-1`

Assumption: source and output size feedback must not expose text content, and token counts must be
described as approximate because providers tokenize differently.

Linux `7ae70945c60934605d2eca82400a2278c753297f` adds localized character counts and an approximate
token estimate below both editor panes. Source-buffer changes update immediately; output metrics
refresh with the translated UI. l10n `8adb1f4558e4b1d93a00ce03cf026a98d4a1a5ed` contains 360
messages and all 59 generated resources. Local Linux/l10n checks passed. Push Native/Flatpak/Foundation
runs `29701632363`/`29701632341`/`29701632350` and PR Native/Flatpak/Foundation runs
`29701633693`/`29701633692`/`29701633700` passed. Provider-specific token accuracy, full Orca speech, visual review, other
clients, artifacts, and stable release remain open.

## Completed Linux-first checkpoint — routing constraints

Change identifier: `LM-CHANGE-2026-07-ROUTING-CONSTRAINTS-1`

Assumption: Core's non-secret routing constraints should be editable in the Linux profile dialog,
while fields not yet represented by GTK must survive an Edit/Save round trip.

Linux `0afc6aff9cf8b7a513827201c0e23de79de00553` adds localized controls for Automatic preference,
local-only and remote permission, privacy-sensitive requests, streaming capability, and document
capability. Edit/Save preserves hidden allow/model lists, quality tiers, and request-size limits.
l10n `b871a881f0eaf88cdda67a50f9221375f4c814ce` contains 377 messages and all 59 generated
resources. Local validation passed. Push Native/Flatpak/Foundation runs
`29702482460`/`29702482435`/`29702482419` and PR Native/Flatpak/Foundation runs
`29702484581`/`29702484564`/`29702484572` all passed.

## Completed Linux-first checkpoint — routing constraint lists and limits

Change identifier: `LM-CHANGE-2026-07-ROUTING-CONSTRAINT-LISTS-1`

Assumption: provider/model allow-deny lists and positive quality/request-size limits are non-secret
Core routing constraints and should be editable in the Linux profile dialog without weakening Core
identifier or bound validation.

Linux `f64054924102b5611eb0e17761c7acb8b3a771dd` adds localized provider/model allowlists and
denylists, minimum-quality, and maximum-request-byte controls. Edit/Save restores and persists
these fields while retaining the existing routing constraints. l10n
`c366124539d4e8c909c66ca7cc33fb16ed92e8b2` contains 387 messages and all 59 generated resources.
Local Linux/l10n checks passed. Push Native/Flatpak/Foundation runs
`29703371083`/`29703371057`/`29703371084` and PR Native/Flatpak/Foundation runs
`29703373063`/`29703373065`/`29703373076` all passed. Documentation-only l10n correction `3362732`
was pushed afterward; the Linux build consumes the verified functional bundle `c3661245`.

## Completed Linux-first checkpoint — visible-string localization audit

Change identifier: `LM-CHANGE-2026-07-VISIBLE-LOCALIZATION-AUDIT-1`

Assumption: Linux gettext coverage must fail closed when a new non-empty GTK-visible literal is
introduced, while empty labels used to clear transient state remain valid.

Linux `2386d495123d3aeacf2b5815d0c45577808c7a44` adds
`tools/check-visible-localization.py` and runs it alongside the 263-key catalog audit in Native
and Foundation CI. The audit covers GTK labels, titles, tooltips, placeholders, dialog actions,
and direct list options. l10n `3362732be198450ff1ca00f30ec092aab2cf4189` supplies the immutable
387-message generated resources. Local Linux checks passed; push Native/Flatpak/Foundation runs
`29703945583`/`29703945586`/`29703945637` and PR Native/Flatpak/Foundation runs
`29703946800`/`29703946783`/`29703946789` all passed. Human translated-copy, plural, visual/RTL,
and Orca review remain open boundaries.

## Completed Linux-first checkpoint — Flatpak source-pin integrity

Change identifier: `LM-CHANGE-2026-07-FLATPAK-SOURCE-PIN-1`

Assumption: Flatpak CI must build the reviewed Linux application revision, or a source-compatible
ancestor whose build inputs are unchanged; packaging-only follow-up commits must not create a false
green gate.

Linux `212de54d7eaa62eaeba8f7bc06297b2632d7a09b` updates the Flatpak manifest to the current
application lineage, validates the pin and build-input diff with a scoped Git safety setting, and
fetches full history in the Flatpak workflow. Local metadata/localization checks passed. Push
Native/Flatpak/Foundation runs `29704472892`/`29704472889`/`29704472884` and PR
Native/Flatpak/Foundation runs `29704474147`/`29704474173`/`29704474207` all passed. This remains
an unreleased CI integrity checkpoint; distributable and stable artifacts are not claimed.

## Completed Linux-first checkpoint — Flatpak checksum and SBOM evidence

Change identifier: `LM-CHANGE-2026-07-FLATPAK-EVIDENCE-1`

Assumption: Linux prerelease packaging should provide reproducible bundle integrity and dependency
evidence, while unsigned CI outputs remain explicitly non-release artifacts.

Linux `dc1c0bc3485c95a57810ac658dab2c0a232f1af7` adds a dependency-free evidence generator that
writes `SHA256SUMS` and a deterministic SPDX 2.3 SBOM from the Flatpak bundle and locked Cargo
package set. The Flatpak workflow uploads these sidecars after the SDK build; push Native/Flatpak/
Foundation runs `29704836385`/`29704836408`/`29704836382` and PR Native/Flatpak/Foundation runs
`29704837824`/`29704837805`/`29704837827` all passed, with non-expired evidence artifacts present
on both Flatpak runs. Stable signing, publication, and cross-platform release artifacts remain open.

## Completed Linux-first checkpoint — native release-mode evidence

Change identifier: `LM-CHANGE-2026-07-NATIVE-EVIDENCE-1`

Assumption: the native Linux release build should be reproducible in CI and accompanied by
integrity metadata before any signing or stable-release authorization.

Linux `c6dae33698587e9db1fd8356ac7938d6bd7944ba` adds a release-mode `linguamesh-linux` build and
uploads the binary with `SHA256SUMS`, deterministic SPDX 2.3 `SBOM.spdx.json`, and `BUILD-INFO.txt`.
Local non-GUI tests and evidence self-checks passed; the host lacks GTK development metadata for a
local GUI link. Push Native/Flatpak/Foundation `29705491999`/`29705491988`/`29705492011` and PR
Native/Flatpak/Foundation `29705493161`/`29705493148`/`29705493163` all passed with non-expired
native and Flatpak artifacts. Signing, source archives, rollback, cross-client artifacts, and
stable-release authorization remain open.

## Completed Linux-first checkpoint — source archive evidence and AT-SPI cleanup

Change identifier: `LM-CHANGE-2026-07-LINUX-SOURCE-ARCHIVE-1`

Assumption: a repository-only source archive is useful prerelease evidence only when its external
Core and localization pins remain documented; test cleanup retries must not alter accessibility
assertions.

Linux `d5525263f2b5e339933a3b3c6dac7d21537ad990` adds the source archive and checksum entry and
hardens the exact temporary-directory cleanup used by the AT-SPI fixture. The initial push run
`29705840151` failed only during cleanup after passing its assertions; final push
Native/Flatpak/Foundation `29706120410`/`29706120412`/`29706120423` and PR
Native/Flatpak/Foundation `29706121615`/`29706121557`/`29706121564` all passed with non-expired
native and Flatpak artifacts. The archive remains unsigned repository-only evidence, not a stable
source release.

## Completed Linux-first checkpoint — performance baseline evidence

Change identifier: `LM-CHANGE-2026-07-LINUX-PERFORMANCE-BASELINE-1`

Assumption: Linux hardening should retain exact runner context and representative elapsed times
before setting a portable performance budget.

Linux `4d6f041f388606dcc99311826ee4dbd3503edfd8` documents a dependency-free baseline runner for
DOCX reconstruction, XLSX reconstruction, and saved-profile routing dispatch. Local measurements
were `0.404s`/`0.382s`/`0.399s`; push Native/Flatpak/Foundation `29706935372`/`29706935324`/
`29706935322` and PR Native/Flatpak/Foundation `29706936415`/`29706936411`/`29706936399` all
passed, with the baseline present in the non-expired Native artifact. These are machine-specific
trend values, not a stable performance guarantee.

## Completed Linux-first checkpoint — localization placeholder audit

Linux `3a20620eb95806baadb1b22ef4833302d0438fea` adds a dependency-free source parser that checks
literal `text`, `text_plural`, mnemonic, and template fallback arguments against canonical
placeholder identities. Native and Foundation CI run the audit beside key and visible-string
checks; push Native/Flatpak/Foundation `29707410914`/`29707410888`/`29707410893` and PR
Native/Flatpak/Foundation `29707412487`/`29707412476`/`29707412474` passed with non-expired
Native and Flatpak artifacts. Documentation-only head `3f5f9ee00dd6359759cec0b96dbc8b6d8b89c70d`
then passed push Native/Flatpak/Foundation `29707758213`/`29707758214`/`29707758216` and PR
`29707759245`/`29707759269`/`29707759252`. This verifies source-level fallback safety only;
translated-copy, plural/visual review, Orca speech, signing, other clients, and stable release
remain open.

The final status head `81eed4f051e0f70406efbe47dca82e4f215c4cce` passed push
Native/Flatpak/Foundation `29708338140`/`29708338160`/`29708338159` and PR
`29708339322`/`29708339336`/`29708339368`; its artifacts were non-expired.

## Completed Linux-first checkpoint — multiple routing-profile IDs

Change identifier: `LM-CHANGE-2026-07-ROUTING-PROFILE-ID-1`

Linux `f00cf23f95d33d7c3c9abbc35ebe2141233a80b8` adds a localized ID entry validated against Core's
1–128 byte ASCII identifier rule. New profiles can use distinct IDs; editing an existing profile
locks its ID so document-job and selection references remain stable.

l10n `7b832d765788e5ca64d7ba483b8ad12b3dd382d2` contains 358 messages and all 59 generated
resources. Local Linux/l10n checks passed. Push Native/Flatpak/Foundation runs
`29700497023`/`29700497020`/`29700497017` and PR Native/Flatpak/Foundation runs
`29700498213`/`29700498197`/`29700498198` all passed; l10n Localization/Foundation runs
`29700369900`/`29700369903` passed. Full fallback-chain editing, Orca speech, visual review, other
clients, artifacts, and stable release remain open.

## Completed Linux-first checkpoint — duplicate routing-profile IDs

Change identifier: `LM-CHANGE-2026-07-ROUTING-PROFILE-ID-DUPLICATE-1`

Linux `21c89c7e9c671617477a6410240ff1fb0a0c9ff7` rejects a new profile when its validated ID is
already present, while explicit Edit keeps same-ID storage replacement. l10n
`712c4b1ac814ffbab265e4d0d40629d9d2bba02d` contains 359 messages and all 59 generated resources.
Local Linux/l10n checks passed. Push Native/Flatpak/Foundation runs
`29701039457`/`29701039458`/`29701039459` and PR Native/Flatpak/Foundation runs
`29701040720`/`29701040695`/`29701040689` all passed; l10n Localization/Foundation runs
`29700989823`/`29700989820` passed. Complete fallback-chain editing, Orca speech, visual review,
other clients, artifacts, and stable release remain open.

## Completed Linux-first checkpoint — routing candidate accessibility labels

Change identifier: `LM-CHANGE-2026-07-ROUTING-CANDIDATE-A11Y-1`

Linux `84bed28deaa6034fb45e4f6c925fd5c2713c8782` uses catalog-backed
`action.move_candidate_up` and `action.move_candidate_down` strings for both tooltip text and GTK
accessible `Label` properties on the icon-only Ordered-mode controls. Localization `0d2d8c0` adds
the keys to all twelve official packs and regenerates native resources.

Local l10n validation passed (26 tests, generated-resource checks, and Foundation validation).
Linux validation passed (GUI check, strict Clippy, 132 tests with 130 passed and 2 ignored, l10n
sync/key audit, Flatpak metadata, and diff checks). Push Native/Flatpak/Foundation
`29698745522`/`29698745519`/`29698745529` and PR Native/Flatpak/Foundation
`29698747220`/`29698747211`/`29698747194` passed.

Full Orca speech, manual visual review, drag/drop ordering, complete candidate management, other
clients, artifacts, and stable release remain open.

## Completed Linux-first checkpoint — routing mode and fallback consent

Change identifier: `LM-CHANGE-2026-07-ROUTING-MODE-CONSENT-1`

Linux `88c04495d427fbca09ce2bc6c020dd057652dae9` exposes Core's `Manual`, `Ordered`, and
`Automatic` routing modes in a stable GTK dropdown and persists the selected mode with the saved
profile. A separate **Allow approved fallback** checkbox records explicit consent and defaults off;
Core still rejects fallback for manual mode and document jobs. Existing catalog keys are reused.

Local Linux validation passed: GUI all-target check, 130 demo-provider tests (`128 passed; 2
ignored`), strict Clippy, formatting, localization sync/audit, Flatpak metadata, and diff checks.
Push Native/Flatpak/Foundation runs `29696348120`/`29696348121`/`29696348094` and PR
Native/Flatpak/Foundation runs `29696349676`/`29696349689`/`29696349695` all passed.

This checkpoint advances Linux routing configuration only; complete candidate management, other
clients, visual/Orca review, distributable artifacts, and stable-release evidence remain open.

## Completed Linux-first checkpoint — secure provider foundation

Change identifier: `LM-CHANGE-2026-07-LINUX-SECURE-PROVIDER-1`

The user's latest explicit priority is Linux. Android, Windows, and macOS implementation work is
frozen for this checkpoint. Shared Core changes are in scope only when the Linux client cannot
correctly own the behavior itself.

Assumption: adding dependencies between existing first-party LinguaMesh workspace crates is a
contract change, not a new third-party production dependency. No new third-party dependency will
be added without a separate maintenance, security, and license review.

Assumption: the existing untracked central RFC and ADR drafts are unrelated user work and must
remain untouched unless their owner explicitly incorporates them into this checkpoint.

Assumption: schema-6 document recovery stores only an opaque job ID, source basename, format,
ordered bounded segments, and lifecycle state. Pending/running jobs are restored on Linux worker
startup; the Linux GTK queue now presents those bounded snapshots. Supported archive/document
formats are covered by later bounded import/reconstruction checkpoints; concurrent document
execution remains outside the current validation gate.

Assumption: exhausting a private Linux tmpfs to `ENOSPC` verifies the implemented SQLite
transaction-failure boundary, not corruption, read-only media, power loss, or every VFS failure.

Assumption: the existing optional gtk-rs `v4_10` feature is the compatibility boundary for these
baseline semantics; no new accessibility crate or runtime catalog dependency is added. Ubuntu
24.04 native CI is authoritative for the GTK path, while AT-SPI/Orca and physical-keyboard
behavior remain separately unverified.

Deliver the prerequisite Core contract before wiring the native Linux host service:

1. expose one typed compatibility description containing the Core semantic version, ABI major,
   protocol version, provider-catalog version, and enabled feature identifiers;
2. define canonical non-secret `SecretRef` and `ProviderProfile` domain types instead of retaining
   a Linux-only profile model;
3. add an explicit SQLite migration chain, transactional provider-profile CRUD, active-profile
   selection, and per-profile last-model persistence without any credential value column;
4. implement a bounded, typed host-secret request/response flow whose diagnostics and persistence
   never contain the secret value;
5. test incompatible-version rejection, schema migration from the prior version, on-disk reopen,
   secret canaries, request correlation, cancellation, and one-terminal-event behavior;
6. integrate the reviewed Core revision into Linux, resolve persistent credentials through the
   existing GIO Secret Service adapter, offer an explicitly labeled in-memory session fallback
   when secure storage is unavailable, and never fall back to plaintext;
7. verify save, restart restoration, secret resolution, provider switching, translation,
   cancellation, and redacted diagnostics under the native Linux CI environment.

Checkpoint evidence:

- [x] Core steps 1–5 are implemented in functional revision
  `fbf3e9b5927049dccaa19f8c36013495ffebba12`; 57 tests, the Core/Native SDK workflows, and the
  Linux default-VFS no-follow prerequisite passed.
- [x] Linux integrates the exact Core alpha.2 contract, begins disconnected, requires explicit
  connection and model selection, resolves one-shot session secrets, streams and cancels loopback
  translation, preserves the active provider after a failed switch, persists only non-secret
  profile/model state, and never persists plaintext.
- [x] Linux functional revision `9729b23ce1a4280ebb434339e880010103b4859d` passed 40 no-default
  tests, 65 demo-provider tests, strict all-feature Clippy, the real GTK provider-setup and
  multi-profile test, and the native all-target build in Native Linux run `29580444723` (job
  `87884607879`).
- [x] Linux verification revision `53837eeb5bc3f3b5a3f9ab4241488679500f523a` retained the X11 gate
  and reran the same GTK binary test under forced Wayland/headless Weston. Functional run
  `29582513061` (job `87891382469`) and evidence-head run `29582714651` (job `87892044520`) passed;
  physical compositor, GPU, and assistive-technology coverage remain open.
- [x] Linux functional revision `c37702c76c3b1a2f9cec805cf9e219721ef7b5ce` rejects persistent
  Connect, model-update, and deletion `ENOSPC` failures before success, degrades to session-only,
  preserves the prior engine/model, and restores only pre-fault state. Foundation run `29586531915`
  (job `87904787120`) and Native Linux run `29586532049` (job `87904787338`) passed; evidence head
  `2eadf06e5e63eec5b7a512a53a2741f4f2c77704` reran the native gates in run `29586802067` (job
  `87905686187`).
- [x] Implement the Linux GIO Secret Service adapter for persistent SecretRef search, create,
  update, resolution, and deletion; unavailable, locked, and interactive keyring paths fail closed.
- [x] Verify Secret Service default-collection store/resolve/delete and cleanup against an
  isolated real `gnome-keyring` daemon in native Linux CI.
- [x] Verify persistent desktop keyring restoration, locked-item fail-closed behavior, and secure
  persistent-credential onboarding under a real daemon lifecycle; prompted interactive flows remain
  open.
- [x] Implement create/update/delete and deliberate Connect-based activation and switching for
  multiple credential-free saved profiles, including independent model preferences and
  connected-row session continuation.
- [x] Persist a non-secret profile/model preference, restore it after restart without
  auto-connection, and verify switching, cancellation rollback, path hardening, and redacted
  diagnostics in native CI.
- [x] Derive session onboarding from authoritative state without a completion flag; keep model
  confirmation out of Ready, identify the stable next-request provider/model, fail closed when the
  worker stops, and retain storage-degradation warnings. Linux-side Scenario 5 regression evidence
  uses authenticated fake providers A/B and real request counters, but does not complete the global
  scenario without persistent secure credentials and stable-release evidence.

This checkpoint remains prerelease. It does not authorize a stable release or a claim that the
complete Provider Hub, all provider protocols, or every Linux milestone is finished. Prompted
interactive Secret Service flows fail closed and remain a separately documented boundary.

## Checkpoint 0 — Project and repository foundation

Create the central project artifacts required by `PROJECT_GOAL.md`: policies, manifests and release-manifest schema, compatibility records, implementation status, roadmap, architecture/ADR/RFC/release directories, bootstrap and workspace-check scripts, templates, exact proposed GitHub commands, and CI. Validate that secrets and local `.codex` state are ignored.

For each canonical sibling repository:

1. inspect local and remote state;
2. create only when missing;
3. initialize `main` locally;
4. add the MIT license, README, repository role, scoped AGENTS instructions, security/contribution/conduct policies, third-party notices, release guidance, `.gitignore`, and CI;
5. pin the global-goal revision;
6. run repository-specific validation;
7. commit, create or connect the public remote, push, and verify visibility/default branch.

Checkpoint evidence:

- `tools/check-workspace.sh` and PowerShell counterpart pass;
- manifests parse and list exactly the canonical repositories;
- every local repository is clean after its verified commit;
- every GitHub repository is public with `main` as default;
- GitHub Actions workflow files exist and remote branch heads match local commits.

## Checkpoint 1 — Rust text-translation vertical slice

Implement a pinned stable Cargo workspace in `linguamesh-core` with focused crates for domain types, command/event protocol, application engine, OpenAI-compatible transport, SQLite persistence, test support/fake provider, and CLI.

Required behavior:

- provider-neutral request, model, operation, event, and typed-error models;
- data-driven OpenAI-compatible endpoint and model listing;
- manual model selection that survives discovery failure;
- real HTTP SSE parsing with fragmented-line and split-UTF-8 handling;
- incremental output with exactly one completed, cancelled, or failed terminal event;
- cancellation propagated to transport without retry;
- initial SQLite schema migrations with no credential values;
- versioned command/event envelope foundation and checked-in Protobuf schema;
- stable C ABI skeleton with opaque handles, explicit buffers, panic containment, cancellation, event polling, shutdown, and ownership tests;
- versioned, schema-validated provider catalog containing no secrets;
- local fake provider covering discovery, streaming, errors, disconnects, and cancellation;
- CLI demo requiring no commercial key.

Required local evidence:

```sh
cargo fmt --all --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-targets --all-features
cargo run -p linguamesh-cli -- demo --text "Hello, LinguaMesh" --target zh-CN
cargo run -p linguamesh-cli -- demo --text "Cancel this stream" --target zh-CN --cancel-after-ms 100
```

Also run dependency/license, vulnerability, and secret checks where installed. Record exact outputs in `IMPLEMENTATION_STATUS.md`; update ADRs, manifests, and compatibility records before committing and pushing.

## Milestones 2–8

### Milestone 2 — Native SDK artifacts

Stabilize the C ABI and Protobuf command/event protocol; generate and test Android, C++/WinRT, and Swift wrappers plus direct Linux Rust integration. Publish only prerelease artifacts until conformance, ownership, checksums, protocol versions, and ABI negotiation are verified.

### Milestone 3 — Four native client vertical slices

Build real Kotlin/Compose, C++/WinRT/WinUI 3, SwiftUI/AppKit, and Rust/GTK 4 clients. Each must configure a provider securely, discover/select a model, stream fake-provider translation, cancel, localize typed errors, switch locale/theme, and report diagnostics.

### Milestones 4–5 — Provider routing and translation quality

Implement protocol-family adapters, provider catalog, local model support, explainable routing with explicit fallback consent, usage normalization, prompt versioning, protected spans, glossaries, chunking, translation memory, history, and incognito behavior.

### Milestone 6 — Document translation

Deliver each format incrementally only when extraction, reconstruction, validation, source preservation, cancellation/recovery, security fixtures, limitations, and native UI integration are all verified.

### Milestone 7 — Localization and accessibility

Deliver canonical locale data and native generators for all required locales, runtime switching, RTL, pseudo-localization, placeholder validation, keyboard access, and platform screen-reader evidence.

### Milestone 8 — Hardening and stable release

Complete threat/privacy models, parser hardening, fuzzing, migrations, performance baselines, packaging, SBOMs, third-party notices, cross-repository CI, release checksums, and every mandatory acceptance scenario. Only then promote compatible versions to stable in the central release manifest.

## Decisions and discoveries

- 2026-07-17: Use a federated polyrepository workspace without Git submodules, coordinated by versioned workspace and release manifests.
- 2026-07-17: Treat the CLI fake-provider path as the first executable proof; scaffolds and mock-only clients do not satisfy a checkpoint.
- 2026-07-17: Keep `.codex/` local-only because repository-local integration configuration may contain workstation-specific or sensitive values.
- 2026-07-17: After the user authenticated GitHub CLI, `gh auth status` and `gh api user` authoritatively resolved `getio0909`. All seven missing public repositories were created from prepared local commits, configured with Issues and Actions enabled and Wiki disabled, and verified with `main` as the default branch and matching local/remote commit IDs.
- 2026-07-17: Rust 1.93.0, Clippy, rustfmt, GCC, CMake, Ninja, Protobuf, and SQLite development libraries are available for the core. Apple and Windows toolchains, Android NDK/Rust targets, and GTK/libadwaita development headers are unavailable locally.
- 2026-07-17: All seven canonical local repositories now exist on `main`; every repository has a clean verified local checkpoint commit.
- 2026-07-17: Core revision `e5fb2311b3e699db83084ce96240b79d482ad896` passed formatting, strict Clippy, 18 tests, locked build, dependency/advisory/license/source policy, credential-signature scan, real streamed completion, and timed cancellation with partial output retained.
- 2026-07-17: GitHub Actions run `29551581397` passed the published Core checkpoint. Foundation workflows passed for l10n, Android, Windows, macOS, and Linux. Central run `29551747796` passed Bash and Windows PowerShell validation after line-ending-independent goal-digest validation was added.
- 2026-07-17: Localization revision `4b36889116eba037721cb31827342409e8836168` passed foundation and localization workflows. Downloaded CI artifact `linguamesh-l10n-0.1.0` matched the locally reproducible SHA-256 `47bc84bd7562fb6ada7f88fd07490e79843c5c4e9d9b747f87a206dbecd0394a`; it remains an unreleased development bundle with unreviewed non-English drafts.
- 2026-07-17: Core alpha.2 functional revision
  `c9a96da52e10554c8458f4d49600ec9336ea651b` completed the Linux secure-provider prerequisites
  and passed Core run `29564543164` plus Native SDK run `29564543160`.
- 2026-07-17: Linux alpha.2 functional revision
  `0455baf8f258c6280d66d1d568fd6a01fdad8486` passed foundation run `29569227294` and Native
  Linux run `29569227256`. The slice is session-only; Secret Service and restart persistence remain
  required, so `LM-CHANGE-2026-07-LINUX-SECURE-PROVIDER-1` stays open.
- 2026-07-17: Core functional revision
  `fbf3e9b5927049dccaa19f8c36013495ffebba12` added Linux default-VFS no-follow storage protection;
  Core run `29572377637` and Native SDK run `29572377631` passed.
- 2026-07-17: Linux functional revision
  `c58a54c2479045773358bd9c456b45a958e98e1e` added credential-free profile/model persistence,
  disconnected restart restoration, startup race prevention, selection rollback, and unsafe-path
  rejection. Foundation run `29574265553` and Native Linux run `29574265570` passed. Native Secret
  Service and complete saved-profile management remain required, so
  `LM-CHANGE-2026-07-LINUX-SECURE-PROVIDER-1` stays open.
- 2026-07-17: Linux functional revision
  `c88d37a5de2f03c2ae5d2940c4d25e5d998c301d` added exact-ID multi-profile
  create/update/switch/delete, full-list/default restart restoration, per-profile model updates,
  two-credential isolation, and connected-row deletion with session continuation. Foundation run
  `29577918346` and Native Linux run `29577918335` (job `87876528763`) passed 62 library tests,
  the real GTK multi-profile test, strict Clippy, and the all-feature build. Evidence head
  `7ba8909bd05a168e328af027e1308d23f257f0f9` passed Foundation run `29578055430` and Native Linux
  run `29578055393` (job `87876964652`). Secret Service and secure persistent-credential onboarding
  remain required, so `LM-CHANGE-2026-07-LINUX-SECURE-PROVIDER-1` stays open.
- 2026-07-17: Central integration revision `f2c3a5532fed81ebe056c0d6de33d81b404b15cf`
  pinned the CI-verified Linux functional revision while preserving `unreleased` status and empty
  artifact lists. Coordination run `29578424525` passed Linux job `87878121729` and Windows
  PowerShell job `87878121792`.
- 2026-07-17: Linux functional revision
  `9729b23ce1a4280ebb434339e880010103b4859d` added derived provider setup, stable next-request
  identity, safe worker/storage degradation, and authenticated A/B one-Connect routing evidence.
  Foundation run `29580444697` and Native Linux run `29580444723` (job `87884607879`) passed 65
  library tests, the real GTK test, strict Clippy, and the native build. Evidence head
  `e9a7591867c9300fcbff9a568a867aacc45195d3` passed Foundation run `29580595045` and Native Linux
  run `29580595042` (job `87885096648`). Secret Service and secure persistent-credential onboarding
  remain open, so neither the checkpoint nor global Scenario 5 is complete.
- 2026-07-17: Central integration revision `f7df9ef3675b218ebc94df74ba26f2256db6fa34`
  pinned the verified Linux onboarding functional source while preserving `unreleased` status,
  empty artifact lists, and partial-only Scenario 3/5 claims. Coordination run `29581079831` passed
  Linux job `87886675010` and Windows PowerShell job `87886675039`.
- 2026-07-17: Linux verification revision
  `53837eeb5bc3f3b5a3f9ab4241488679500f523a` added a test-only headless Weston runner with a private
  runtime directory, bounded readiness, forced Wayland, and cleanup traps while retaining the
  X11/Xvfb gate. Functional Foundation run `29582513073` and Native Linux run `29582513061` (job
  `87891382469`) passed 65 library tests and one real GTK test on each display backend; evidence-head
  Foundation run `29582714711` and Native Linux run `29582714651` (job `87892044520`) also passed.
  The release manifest continues to pin the unchanged Linux functional source.
- 2026-07-17: Central integration revision `4945769e4aac00926348c3f757c7910bcc610c9e`
  recorded the Linux verification head and dual-backend evidence while preserving the functional
  source pin, `unreleased` status, six empty artifact lists, and incomplete secure-provider and
  acceptance-scenario claims. Coordination run `29583121429` passed Linux job `87893397751` and
  Windows PowerShell job `87893397798`.
- 2026-07-17: Linux functional revision `c37702c76c3b1a2f9cec805cf9e219721ef7b5ce`
  implemented fail-closed post-startup persistence degradation and a real private-tmpfs `ENOSPC`
  gate for persistent Connect, model update, and deletion. Foundation run `29586531915` (job
  `87904787120`) and Native Linux run `29586532049` (job `87904787338`) passed 66 ordinary library
  tests, one exact fault test, the real GTK flow on X11 and forced Wayland, strict Clippy, and the
  native build. Evidence head `2eadf06e5e63eec5b7a512a53a2741f4f2c77704` passed Foundation run
  `29586802183` (job `87905686613`) and Native Linux run `29586802067` (job `87905686187`). Secret
  Service and broader storage-fault coverage remain open.
- 2026-07-17: Central integration revision `04c0e07ccb769a9e67e80ee76042d6c568a7f8d4`
  pinned the verified Linux runtime-storage functional source and recorded its exact fault-test
  boundary while preserving the Core pin, `unreleased` status, six empty artifact lists, and
  incomplete secure-provider and acceptance-scenario claims. Coordination run `29587437567`
  passed Linux job `87907811474` and Windows PowerShell job `87907811494`.
- 2026-07-17: Linux functional revision `d6bd2bd06ccdf04f3aead0c7f1da5ba74f84c550` added GTK
  4.10 baseline accessibility semantics. The first revision `e483ad8b9ff0fb9e35fd531e69959c1eb81e7e34`
  exposed a native focusability failure because dropdowns defaulted non-focusable; the fix made
  all labelled controls and actions explicitly focusable. Foundation run `29589043314` (job
  `87913221612`) and Native Linux run `29589043315` (job `87913221576`) passed. Evidence head
  `07d0b4daddf04d369768893a531276d507292356` passed Foundation run `29589332132` and Native Linux
  run `29589332282` (job `87914189125`). AT-SPI/Orca, physical keyboard, and full desktop
  accessibility remain open.
- 2026-07-17: Central integration revision `409e25716c36f94777fea5a2a6e9b1e9b13ce076` pinned the
  Linux accessibility functional source, recorded its GTK semantics and open desktop boundaries,
  and preserved `unreleased` status with empty artifact lists. Coordination run `29589860768`
  passed Linux job `87915946902` and Windows PowerShell job `87915946857`.
- 2026-07-17: Linux functional revision `73c60e751beed475aade1ea6e6ffa7c8b3e7164b` added the
  GIO D-Bus Secret Service adapter and fail-closed persistent SecretRef resolution. Validation
  head `81be457fc6cefcaebff6c6afd61408d6eb6900b3` passed Foundation run `29592320055` (job
  `87924170620`) and Native Linux run `29592319844` (job `87924169888`); evidence head
  `3623350bc4538affb59daf956ac26d909a0aff6c` passed Foundation run `29592545668` and Native
  Linux run `29592545963` (job `87924933377`). The CI environment has no desktop keyring service,
  so real Secret Service CRUD, cleanup, and secure persistent-credential onboarding remain open.
- 2026-07-17: Central integration revision `b00bc4d45e60ba7bea1ff6bd633150e28c6c68c5` pinned Linux
  functional revision `73c60e751beed475aade1ea6e6ffa7c8b3e7164b`, updated compatibility/release
  records for the GIO adapter and its evidence boundary, and preserved `unreleased` status and
  empty artifact lists. Coordination run `29593038301` passed Linux job `87926604854` and
  Windows PowerShell job `87926604724`.
- 2026-07-17: Linux functional revision `1dfe2bcac684696ee55f56e625fcf89ffcb1a6dd` added runtime
  PO catalog loading for English and Simplified Chinese action labels without losing active text.
  Validation run `29593874961` (job `87929412911`) and evidence head `bc827d55118199e2e64e063a106da281f8a8bdf1`
  run `29594014033` (job `87929863334`) passed Native Linux; Foundation runs `29593874763` and
  `29594014184` also passed. Complete UI gettext coverage and human review of non-English drafts
  remain open.
- 2026-07-17: Central integration revision `a964ac060c51665793ed455763137ee30bd22a26` pinned Linux
  functional revision `1dfe2bcac684696ee55f56e625fcf89ffcb1a6dd`, recorded runtime catalog
  switching and its coverage boundary, and preserved `unreleased` status and empty artifact lists.
  Coordination run `29594286528` passed Linux job `87930776189` and Windows PowerShell job
  `87930776107`.
- 2026-07-17: Linux functional revision `07b89f36269155469a488ab830e8f485b3a1323b` added a
  registered `GApplication` completion notification with fixed generic text that excludes source
  and translated content. Native Linux run `29594795691` (job `87932451631`) and foundation run
  `29594795681` (job `87932451692`) passed the functional slice; evidence head
  `a7554e81c40b7d92d29a0eb8ab4fa22b1517648f` passed Native Linux run `29594948933` (job
  `87932966303`) and foundation `29594948857` (job `87932965793`). Notification-server delivery,
  packaging, and full localization coverage remain open.
- 2026-07-17: Central integration revision `78ba57398ce93a164ca2b932a85046e5ddb0b363` pinned the
  Linux notification functional revision, recorded its privacy and delivery boundary, and kept
  `unreleased` status with empty artifact lists. Coordination run `29595318912` passed Linux job
  `87934171311` and Windows PowerShell job `87934171416`.
- 2026-07-17: Linux functional revision `96d34a5448d0f718fd87c68e88129c05fed43ee5` added a
  native GTK FileDialog action with bounded asynchronous GIO partial reads for UTF-8 TXT/Markdown
  input, UTF-8 BOM removal, invalid-text rejection, and a 4 MiB limit. Native Linux run
  `29596052224` (job `87936587342`) and foundation run `29596052213` (job `87936587361`) passed;
  evidence head `1553841dc527f1f3bc9556ce5f88650f28221d85` passed Native Linux run `29596239167`
  (job `87937214530`) and foundation `29596239653` (job `87937215981`). Portal leases,
  interactive file selection, drag-and-drop, and document codecs remain open.
- 2026-07-17: Central integration revision `b4d8b3c40b49f0ba327beb979d1b4b9fdbf6fdda` pinned the
  Linux text-import functional revision and recorded its 4 MiB/UTF-8 and portal boundary. The
  coordination run `29596541373` passed Linux job `87938213706` and Windows PowerShell job
  `87938213592`.
- 2026-07-17: Linux functional revision `b0da3819d97ae24f8c85147da5e7e1c65fe2d6fc` added a
  single-file GTK `DropTarget` on the source editor, reusing the bounded GIO UTF-8/4 MiB import
  path. Native Linux run `29597016894` (job `87939785693`) and foundation run `29597016893`
  (job `87939785643`) passed; evidence head `cdc711320c284eae1f1376635e0d84234d8863a` passed
  Native Linux run `29597182692` (job `87940328074`) and foundation `29597182729` (job
  `87940328419`). Portal leases and interactive gestures remain open.
- 2026-07-17: Central integration revision `18fc69e0eea5431bf82c767b8d90ce48fef38d01` pinned the
  Linux source-drop functional revision, recorded the evidence head, and kept the train unreleased
  with empty artifacts. Coordination run `29597565696` passed Linux job `87941565049` and
  PowerShell job `87941565102`.
- 2026-07-17: Linux functional revision `9bcd8d9ca30d109f5c7c9c20e6f72f6a77df078d` corrected the
  Secret Service `OpenSession` `(sv)` payload from a double-wrapped Variant to a plain-string
  Variant and added a regression test. Native Linux run `29598255988` (job `87943844854`) and
  foundation `29598255993` (job `87943844922`) passed; evidence head `0e86e6fb47a11dbf16fd9689795592da648c9eb3`
  passed Native Linux run `29598405209` (job `87944328685`) and foundation `29598405197` (job
  `87944328254`). Real desktop keyring lifecycle evidence remains open.
- 2026-07-17: Central integration revision `62231504584e8ae9e51111651ac26d7f5c30b1a1` pinned the
  Linux Secret Service wire-fix functional revision, recorded the evidence head, and preserved
  unreleased status with empty artifacts. Coordination run `29598784566` passed Linux job
  `87945581898` and PowerShell job `87945582009`.
- 2026-07-17: Linux functional revision `726508f8412727f8b14e32d27407487491f5e4cd` completed the
  Secret Service default-collection store/resolve/delete path and cleanup against an isolated real
  `gnome-keyring` daemon. Native Linux run `29600898951` (job `87952473459`) and foundation run
  `29600898977` passed; evidence head `93f40456a53074ad437e4ee74634348c35afc049` passed Native
  Linux run `29601110914` (job `87953169459`) and foundation run `29601110906`. Persistent desktop
  restoration, locked/prompted behavior, and secure persistent-credential onboarding remain open.
- 2026-07-17: Central integration revision `acdf43cde6a7a971d1cb27e0c6a672b6b86cbc21` pinned the
  verified Linux Secret Service CRUD functional revision and evidence head, preserved unreleased
  status with empty artifact lists, and passed coordination run `29601473308` with Linux job
  `87954353885` and PowerShell job `87954353964`.
- 2026-07-17: Linux functional revision `f58388a8e58341a8630088dc8b1782f61ab63a7c` verified
  persistent Secret Service storage, locked-item fail-closed lookup, daemon-restart restoration,
  deletion, and cleanup in Native Linux run `29602287284` (job `87957053225`) with Foundation
  run `29602287281`; secure persistent-credential onboarding and prompted interactive flows remain
  open.
- 2026-07-17: Central integration revision `b842ffd238cc648b0a22b45db0a8b300b5e9b455` pinned
  the verified Linux persistent-lifecycle functional source and evidence head, preserved unreleased
  status with empty artifact lists, and passed coordination run `29602906399` with Linux job
  `87959070945` and PowerShell job `87959071022`.
- 2026-07-17: Linux functional revision `6654a46b378d68c2c6012ccf2f30e24ae564dc7c` verified
  secure persistent-credential onboarding through worker and GTK paths, including form clearing,
  SecretRef-only persistence, authenticated translation, and restart reconnect. Native Linux run
  `29603486498` (job `87960961963`) and Foundation run `29603486477` passed; evidence head
  `3f4ba2f2c0bd0e48c5990f1640cd39b637907769` passed Native Linux run `29603706638` (job
  `87961679587`) and Foundation run `29603706640`.
- 2026-07-17: Central integration revision `3d3727b42c8e5cc1352c3415b4a635977569fbda` pinned
  the secure-onboarding Linux functional source and evidence head, preserved unreleased status
  with empty artifact lists, and passed coordination run `29603927123` with Linux job `87962420732`
  and PowerShell job `87962420692`.
- 2026-07-17: Linux functional revision `7d7eba9960b657f0460fb0daaaaebaaa609f39b1` added explicit
  no-credential OpenAI-compatible loopback connection, manual model selection, streamed translation,
  and request-count evidence. Native Linux run `29604269568` (job `87963611054`) and Foundation
  run `29604269516` passed; evidence head `a255b039ce37bcb2b362cfeb3d34a6283ed2aad5` passed its
  documentation gates in the same workflow.
- 2026-07-17: Central integration revision `a7ca1f84eef3f98647a4383dc931c11049171b63` pinned the
  loopback-provider Linux functional source and evidence head, preserved unreleased status with
  empty artifact lists, and passed coordination run `29604649153` with Linux job `87964871597` and
  PowerShell job `87964871588`.
- 2026-07-17: Linux packaging revision `302ba8c` added a pinned Flatpak scaffold with GNOME 48
  runtime metadata, immutable Core/Linux source pins, generated Cargo sources, desktop/AppStream
  metadata, icon, and constrained runtime permissions. Static JSON, desktop-file, AppStream, and
  source-hash validation passed locally; SDK/sandbox smoke and distributable artifacts remain open.
- 2026-07-17: Coordination run `29605424763` passed after the packaging checkpoint on Linux job
  `87967368496` and PowerShell job `87967368478`; no release artifact was produced.
- 2026-07-17: Flatpak Linux run `29605863496` failed because the GNOME 48 build sandbox lacked
  Cargo; run `29606146197` then exposed the Rust 1.89 extension being older than the workspace's
  Rust 1.92/1.93 requirements, and run `29606402301` exposed Flatpak debug extraction corrupting
  the temporary Rust toolchain. These failures were retained as boundary evidence and fixed in the
  manifest with the Rust stable SDK extension, a pinned Rust 1.93.0 toolchain module, and
  `no-debuginfo` for that build-only module.
- 2026-07-17: Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` passed
  `Flatpak Linux` run `29606612834` (job `87971271146`), built the optimized GTK application from
  pinned sources, and uploaded prerelease artifact `linguamesh-linux-x86_64-x86_64.flatpak` as
  artifact `8417198959` (2,390,377 bytes). Sandbox launch, portal/notification delivery, signing,
  and distributable release remain open; no release artifact was added to the manifest.
- 2026-07-17: Linux packaging revision `fd1f400058f4c68b47a9bd0823e790c6d9cef263` migrated the
  Flatpak manifest and CI image from the GNOME 48 runtime, which the CI image reported EOL, to GNOME
  49. Local metadata validation passed; Native Linux run `29607653918`, Foundation run `29607653880`,
  and `Flatpak Linux` run `29607653864` (job `87974679904`) passed. The GNOME 49 build uploaded
  prerelease artifact `8417588673` (2,396,371 bytes); sandbox launch, portal/notification delivery,
  signing, and distributable release remain open.
- 2026-07-17: Linux packaging commit `f24a2fd` added `tools/run-flatpak-smoke.sh`. `Flatpak Linux`
  run `29608245156` (job `87976563401`) uploaded artifact `8417803048` (2,395,628 bytes), installed
  it with the GNOME 49 runtime, and passed bounded startup under Xvfb/private D-Bus. Portal and
  notification delivery, signing, and distributable release remain open.
- 2026-07-17: Central evidence sync commit `f2bc443` recorded the GNOME 49 packaging and sandbox
  smoke result, preserved unreleased status with empty artifact lists, and passed coordination run
  `29608669489` with Linux job `87977918468` and PowerShell job `87977918397`.
- 2026-07-17: Linux notification transport revision `bf751479c3826ae1529d0d9c33effbc5212cd75f`
  added a private `org.freedesktop.Notifications` fixture and fixed generic payload assertions.
  Evidence head `ae44102ae90f70d543c001869557a8965dba2074` passed Foundation run `29610044117`
  (job `87982316925`), Native Linux run `29610044120` (job `87982316767`), and Flatpak run
  `29610044088` (job `87982316819`). Earlier fixture runs `29609357351` and `29609497086` remain
  retained failures because the first lacked a private D-Bus session and the second had no
  notification service. Desktop-shell rendering and portal leases remain open.
- 2026-07-17: Central integration revision `5ea07ebf3024668f3b50ed2b57637e6e6ca0f8d3`
  recorded the Linux notification transport evidence, preserved `unreleased` status and empty
  artifact lists, and passed coordination run `29610616057` with Linux job `87984136976` and
  PowerShell job `87984136992`.
- 2026-07-17: Follow-up manifest sync `94f9e12df9797b025f46d4021e7dc365e5c1ba10` preserved the
  same unreleased release posture and passed coordination run `29610693933` with Linux job
  `87984393628` and PowerShell job `87984393633`.
- 2026-07-17: Linux document-portal revision `7fbd65f08ebffa55777e0d7804d270fe683ca6c6`
  added the real XDG document-portal lease fixture. Evidence head `9897f10` passed Native Linux
  run `29611867060` (job `87988152626`), Foundation run `29611866929`, and Flatpak run
  `29611866969`; interactive file-chooser gestures and desktop-shell notification rendering
  remain open.
- 2026-07-17: Central integration revision `3ff3d1141f73ae1fbdb6529d94a1c4b4a87ff476`
  recorded the document-portal lease evidence, preserved the unreleased status and empty artifact
  lists, and passed coordination run `29612315893` with Linux job `87989566351` and PowerShell
  job `87989566349`.
- 2026-07-17: Linux evidence revision `20433c9f0f6f70c561093e96dc1fa35731617b36` added the real
  `dunst` notification-daemon delivery fixture. Native run `29613020196` (job `87990400327`),
  Foundation run `29613020145`, and Flatpak run `29613020144` passed; the fixture proves headless
  daemon delivery and generic payload privacy, while physical desktop-shell rendering remains open.
- 2026-07-17: Central integration revision `782f5b2` recorded the Linux notification-daemon
  evidence, preserved `unreleased` status and empty artifact lists, and passed coordination run
  `29613487659` with Linux job `87993296419` and PowerShell job `87993296429`.
- 2026-07-17: Linux evidence revision `e7bf31e4408f1873c51715ed32530ee4e9b8722c` added the real
  interactive `xdg-desktop-portal-gtk` FileChooser backend fixture. Native run `29615670319`
  (job `88000113663`), Foundation run `29615670336`, and Flatpak run `29615670344` passed; the
  fixture proves portal-backend UI/lease behavior, while application-level GTK FileDialog
  callbacks, drag/drop portal gestures, and physical desktop-shell rendering remain open.
- 2026-07-17: Central integration revision `6d433bc` recorded the interactive portal chooser
  evidence, preserved `unreleased` status and empty artifact lists, and passed coordination run
  `29616044432` with Linux job `88001278364` and PowerShell job `88001278398`.
- 2026-07-17: Linux evidence revision `d2fb3abe6c1505385850cd2a1053a7f64dbd7d0e` verified the
  application-level GTK FileDialog callback and a real XTest source-editor URI-list drag/drop
  gesture. Native run `29619390971`, Foundation run `29619390964`, and Flatpak run `29619390913`
  passed; prompted flows, physical desktop-shell rendering, and release artifacts remain open.
- 2026-07-17: Central integration revision `0de200a` recorded the application-level GTK evidence,
  preserved `unreleased` status and empty artifact lists, and passed coordination run `29619564326`
  with Linux job `88011719149` and PowerShell job `88011719080`.
- 2026-07-17: Linux evidence revision `0f8585e773f471e435e30020b0153025aabd7987` added visible
  Dunst desktop-shell window verification to the notification fixture. Native run `29619961909`,
  Foundation run `29619962316`, and Flatpak run `29619961877` passed; physical compositor/GPU
  rendering and release artifacts remain open.
- 2026-07-17: Central integration revision `b65e690` recorded the desktop-shell rendering evidence,
  preserved `unreleased` status and empty artifact lists, and passed coordination run `29620258790`
  with Linux job `88013724889` and PowerShell job `88013724860`.
- 2026-07-17: Linux evidence revision `259a7bf2c8c9fbd4ad0b7c7bb0f2792e78a881ba` added an
  isolated Python D-Bus Secret Service fixture that returns non-root prompt paths for `CreateItem`
  and `Delete`; the adapter rejected both with `SecureStorageUnavailable`. Native run `29620808496`
  (job `88015342381`), Foundation run `29620808409`, and Flatpak run `29620808411` passed; end-user
  prompt approval, physical compositor/GPU rendering, and release artifacts remain open.
- 2026-07-17: Central integration revision `1298a11` recorded the prompted-flow evidence and
  passed coordination run `29621166248` with Linux job `88016352833` and PowerShell job `88016352805`.
- 2026-07-17: Linux evidence revision `7a40c222a00ea7d3d31125507a01c600948a5b94` exposed all
  twelve official PO packs, added Arabic RTL root-direction switching, and passed Native run
  `29621513205` (job `88017339094`), Foundation run `29621513199` (job `88017339159`), and Flatpak
  run `29621513202` (job `88017339097`). Full visible-string gettext coverage remains open.
- 2026-07-17: Central integration revision `54c36d4` recorded the official locale-pack evidence
  and passed coordination run `29621850718` with Linux job `88018313045` and PowerShell job
  `88018313060`.
- 2026-07-17: Linux evidence revision `5515d9ad8fc78e91945acc739240dfb8291265fb` wired the
  catalog-backed application title, source/output headings, provider/settings labels, diagnostics
  heading, and editor accessibility labels into runtime locale refresh; the GTK test asserts the
  Simplified Chinese labels. Native run `29622079599` (job `88018959518`), Foundation run
  `29622079615`, and Flatpak run `29622079604` passed. Complete visible-string gettext coverage,
  end-user prompt approval, physical compositor/GPU rendering, and release artifacts remain open.
- 2026-07-18: Central integration revision `ee1f064` recorded the Linux widget-localization
  evidence and passed coordination run `29622418277` with Linux job `88019924677` and PowerShell
  job `88019924683`.
- 2026-07-18: Linux evidence revision `4db7076b3a30f0369cc33b7cc0394a8c7103c7f5` added
  catalog-backed active-provider and Ready/Translating/Cancelled status labels. Native run
  `29622526617` (job `88020226946`), Foundation run `29622526618`, and Flatpak run `29622526592`
  passed; complete visible-string gettext coverage, end-user prompt approval, physical compositor/
  GPU rendering, and release artifacts remain open.
- 2026-07-18: Central integration revision `db6f202` recorded the Linux active-provider/status
  evidence and passed coordination run `29622759405` with Linux job `88020903435` and PowerShell
  job `88020903427`.
- 2026-07-18: Linux evidence revision `52f9042f88c74dda1cc3c961e150d552c454c106` added runtime
  localization for System/Light/Dark theme options and asserted the Simplified Chinese Light label.
  Native run `29622930107` (job `88021425747`), Foundation run `29622930079`, and Flatpak run
  `29622930087` passed; complete visible-string gettext coverage and the other release boundaries
  remain open.
- 2026-07-18: Central integration revision `f22b5f1` recorded the Linux theme-option evidence and
  passed coordination run `29623135803` with Linux job `88022041698` and PowerShell job
  `88022041716`.
- 2026-07-18: Linux evidence revision `0a68d1572cef8d330f50a13a1f581ffdfe234715` recorded the
  GTK locale-switch regression that preserves source text while switching from Simplified Chinese
  to Arabic and verifies RTL direction. Native run `29623921134` (job `88024412823`), Foundation
  run `29623921097`, and Flatpak run `29623921145` (job `88024413053`) passed.
- 2026-07-18: Central integration revision `3b13df0` recorded the Linux source-buffer-preservation
  evidence and passed coordination run `29624204932` with Linux job `88025236212` and PowerShell
  job `88025236191`.
- 2026-07-18: Localization revision `24e6c6b387e52473922574ebb861a9b3bf049ba1` added eleven
  Linux-only status and partial-output messages. Its Foundation and Localization workflows passed
  as runs `29624475766` and `29624475769`; the deterministic bundle checksum is
  `4b8a1c49d0e028f775cdc20f704b0f6f50112d1ee2c7f47728e4a0ad51593f1f`.
- 2026-07-18: Linux status-localization revision `4d3cfdbdcc92c4caf4e494659ea88315e71bd081` first
  failed Native run `29624591250` before tests because the workflow still checked out the previous
  localization pin. Revision `edb9cd226a6468f858023a9125217b426ff58e6e` corrected the workflow pin;
  Native run `29624640319` (job `88026467667`), Foundation run `29624640306`, and Flatpak run
  `29624640300` (job `88026467605`) then passed.
- 2026-07-18: Central integration revision `2b670c3` recorded the Linux status-summary/partial-output
  localization and l10n revision update, passing coordination run `29624893274` with Linux job
  `88027207327` and PowerShell job `88027207325`.
- 2026-07-18: Localization revision `14a4d6bcd556d735dee2d7ed022650fbcc8593b8` added five
  Linux-only text-import controls (`Open`, `Open text file`, the UTF-8 text filter, dialog title,
  and tooltip). Its Localization and Foundation workflows passed as runs `29624998218` and
  `29624998224`; the deterministic bundle checksum is
  `40655730a4d07d522901e3b9ac0a76978d3208d379bad0bf219623ac3a04ae06`.
- 2026-07-18: Linux evidence revision `d563bc28ef6a08fd90c7a4eba3bf71ae8b07d57b` wired those
  catalog keys through the native GTK file-import controls and pinned the updated l10n revision.
  Native run `29625054878` (job `88027678296`), Foundation run `29625054875`, and Flatpak run
  `29625054911` (job `88027678198`) passed; the native gate also asserted Simplified Chinese
  status and Open text-file labels and Arabic RTL switching with source-buffer preservation.
- 2026-07-18: Central integration revision `79bf11e` recorded the Linux text-import localization
  evidence, l10n bundle checksum, and Flatpak run; coordination run `29625308528` passed with
  Linux job `88028407855` and PowerShell job `88028407843`.
- 2026-07-18: Localization revision `b583fbf63dc5ced27136ca1d8a87816593929379` added 23
  Linux-only provider-profile, tooltip, action, and source/target language messages, bringing the
  catalog to 80 messages. Its Localization and Foundation workflows passed as runs `29625641716`
  and `29625641740`; the deterministic bundle ZIP checksum is
  `e7c0edf2ea92992d682293b5f922c555be07e5132cef9ed63957bdebe8fb2d3b`.
- 2026-07-18: Linux evidence revision `c074c2d1f8f9446559f23a72d224c48e2e612947` wired the
  provider-profile card, tooltips, and source/target language options through the catalog and
  updated the workflow pin. Native run `29625778212` (job `88029765419`), Foundation run
  `29625778196`, and Flatpak run `29625778180` (job `88029765322`) passed; the Native GTK test
  asserted Simplified Chinese provider controls and language options together with Arabic RTL and
  source-buffer preservation.
- 2026-07-18: Central integration revision `c5b34c7` recorded the 80-message Linux provider-card
  localization evidence, l10n checksum, and updated release-manifest source pin; coordination run
  `29626082929` passed with Linux job `88030658949` and PowerShell job `88030658881`.
- 2026-07-18: Localization revision `5c2e5756f02fbc29ba1ca311958b6bf7d26027bf` added 17
  Linux onboarding-stage and onboarding-detail messages, restored the existing generic onboarding
  translations, and produced 97 canonical messages. Localization and Foundation workflows passed
  as runs `29626274539` and `29626274579`; the deterministic bundle ZIP checksum is
  `c4d08929cbaf89d1836e2b5934ffff880f72cdb28c74e25d30c9a9920ab8b3b7`.
- 2026-07-18: Linux evidence revision `029e7f21322f3d0f3619a8f3a0158e7157972e30` wired
  catalog-backed onboarding stage/detail guidance, dynamic provider/profile/model placeholders,
  and the 97-message snapshot into the GTK onboarding card. Native run `29626461099`, Foundation
  run `29626461122`, and Flatpak run `29626461131` passed; the workflow now pins l10n revision
  `5c2e5756f02fbc29ba1ca311958b6bf7d26027bf`.
- 2026-07-18: Central integration revision `4cc6a96` recorded the 97-message l10n bundle,
  onboarding-stage GTK evidence, release-manifest pin, and Linux remote gates; coordination run
  `29626700744` passed with Linux job `88032448228` and PowerShell job `88032448236`.
- 2026-07-18: Localization content revision `0536ae1695116f5130943c1114bc31c60376407e`,
  followed by evidence documentation revision `0ed08e9e5040edb8f981c90c82dff0fd30219e25`, added ten
  Linux-only active-provider transition/mode, completion-notification, and draft-locale-note keys,
  bringing the catalog to 107 messages. Localization and Foundation workflows passed as runs
  `29626983883` and `29626983894`; the deterministic bundle ZIP checksum is
  `9eb7acda3347cf9fede9eadf158cda2c233cfbd8399b45ffc4497f0802e32777`.
- 2026-07-18: Linux evidence revision `220add98a1fcebe0392234db08ce1b9f266d095e` wired the
  active-provider summaries, persistence-mode labels, completion notification copy, and locale
  draft note through the GTK runtime. Native run `29627288199`, Foundation run `29627288206`, and
  Flatpak run `29627288201` passed; the workflow pins l10n revision
  `0ed08e9e5040edb8f981c90c82dff0fd30219e25`.
- 2026-07-18: Central integration revision `35ee2d5` recorded the 107-message l10n bundle,
  active-provider/notification GTK evidence, release-manifest pin, and Linux remote gates;
  coordination run `29627110594` passed with Linux job `88033588032` and PowerShell job
  `88033588065`.
- 2026-07-18: Localization revision `0ba26705e113230ae7d9e74db54039e1e82296ce` added ten
  Linux-only fixed provider/file/worker error messages, bringing the catalog to 117 messages.
  Localization and Foundation workflows passed as runs `29627610120` and `29627610107`; the
  deterministic bundle ZIP checksum is
  `bdffb3472da8023e4c414ed40744e4431cb2ae551189ef1ecef701a77b39f01f`.
- 2026-07-18: Linux evidence revision `b6d2503` wired localized provider validation, saved-profile,
  active-provider, text-file import, and worker-disconnect/stop errors through the GTK runtime.
  Native run `29627668119`, Foundation run `29627668093`, and Flatpak run `29627668108` passed;
  the workflow pins l10n revision `0ba26705e113230ae7d9e74db54039e1e82296ce`.
- 2026-07-18: Central integration revision `522c94e` recorded the 117-message l10n bundle,
  fixed Linux error localization, release-manifest pin, and Linux remote gates; coordination run
  `29627851127` passed with Linux and PowerShell validation jobs.
- 2026-07-18: Localization revision `08118b498646ebf56cbb072b937d95fceb34b75c` added 31
  Linux-only reducer-state and error-category messages, bringing the catalog to 148 messages.
  Localization and Foundation workflows passed as runs `29628250037` and `29628250110`; the
  deterministic bundle ZIP checksum is
  `08d252c8d3fbdd163e7a5f18eea06ac806029667b8c2ec1e836245d66c2b2595`.
- 2026-07-18: Linux evidence revision `9f21836f214d3056934fac9322adc0f20791834e` wired
  localized fixed reducer errors and category prefixes through the GTK error label. Native run
  `29628307915`, Foundation run `29628307945`, and Flatpak run `29628307886` passed; the workflow
  pins l10n revision `08118b498646ebf56cbb072b937d95fceb34b75c`.
- 2026-07-18: Central integration revision `b4d6afe` recorded the 148-message l10n bundle,
  reducer-state Linux evidence, release-manifest pins, and all three Linux remote gates;
  coordination run `29628561782` passed with Linux job `88037742108` and PowerShell job
  `88037742148`.
- 2026-07-18: Localization revision `0b906034784a1b5e81a879649abbfda001fa9e67` added
  deterministic GNU MO companions for the 14 Linux PO catalogs. Localization and Foundation
  workflows passed as runs `29628807367` and `29628807378`; the deterministic bundle ZIP checksum
  is `d82a152aff0212b7dde55d9b9a67ceac7ed16245d6a0ca6de49564f7d1dafcc5`.
- 2026-07-18: Linux MO integration revision `6c5bfb305967d0f01488ad09ade6e5b88eebbdb0` switched
  the runtime locale loader to generated MO tables and pinned the updated workflow checkout.
  Native run `29628986188`, Foundation run `29628986160`, and Flatpak run `29628986187` passed;
  the workflow validates both PO syntax and MO readability.
- 2026-07-18: Central integration revision `db4c0ca` recorded the paired PO/MO Linux resources,
  l10n bundle checksum, release-manifest pins, and Linux MO evidence; coordination run
  `29629197379` passed with Linux job `88039490578` and PowerShell job `88039490592`.
- 2026-07-18: Localization revision `cc841103c3480ece237baa088bbb5881a321cf0a` added 24
  Linux-only fixed and detail-bearing worker/file/storage/provider error messages, bringing the
  catalog to 172 messages. Localization run `29629399707` and Foundation run `29629399734`
  passed; the deterministic bundle ZIP checksum is
  `e55dbd79f9ba010161ac998a940d4a8a142c8aca0385731882b65f38acc3228e`.
- 2026-07-18: Linux evidence revision `e7d2f7776d3c129e1f66a1feacd04c4826160a2b` wired the
  worker/file/storage/provider error keys through the runtime MO loader and pinned the new l10n
  checkout. Native run `29629498575`, Foundation run `29629498574`, and Flatpak run `29629498588`
  passed the Linux validation, MO/PO checks, GTK fixtures, and GNOME 49 sandbox smoke.
- 2026-07-18: Central integration revision `57210b4` recorded the 172-message l10n bundle,
  worker/file/storage/provider error coverage, release-manifest pins, and Linux remote gates;
  coordination run `29629679652` passed with Linux job `88040764195` and PowerShell job
  `88040764163`.
- 2026-07-18: Localization revision `d21c3b0d065831b20cf31c9bf3009ffd262e4797` added twelve
  Linux-only locale-selector language-name messages, bringing the catalog to 184 messages.
  Localization run `29629934280` and Foundation run `29629934219` passed; the deterministic
  bundle ZIP checksum is `116e5c70a5266197a0ee8ec91bbb35637802d68ba7456a9aad344838a5f40c1e`.
- 2026-07-18: Linux evidence revision `a50806edff6a374ad966ccc4f78203bfec1ce2e5` refreshed
  locale-selector labels during runtime locale switching and pinned the new l10n checkout.
  Native run `29629975421`, Foundation run `29629975449`, and Flatpak run `29629975454` passed
  the Linux validation, PO/MO checks, GTK locale assertions, and GNOME 49 sandbox smoke.
- 2026-07-18: Localization revision `6a1f0e914e56788c34970bd7b18c8f963026ff73` added eight
  Linux-only translation-export action, dialog, success, and error messages, bringing the
  catalog to 192 messages. Localization run `29630392940` and Foundation run `29630392962`
  passed; the deterministic bundle ZIP checksum is
  `22904dc801a3c61536d1e9f4fc5e7c2d2d6a3eea4d672072419ef61b8ad2be0e`.
- 2026-07-18: Linux evidence revision `e79df4442a104b2d4e89f8ac81d7442773636771` added the
  native translation-export action, asynchronous UTF-8 save flow, localized status/error copy,
  and source-file overwrite protection while pinning the new l10n checkout. Native run
  `29630434240` (job `88042823692`), Foundation run `29630434252` (job `88042823739`), and
  Flatpak run `29630434241` (job `88042823704`) passed the Linux validation, GTK export-aware
  assertions, PO/MO checks, and GNOME 49 sandbox smoke.
- 2026-07-18: Localization revision `057c1b8e859acfa4b4fd4eafbdc68ce01069f9a5` added the
  Linux construction-stage provider/default-control message and refreshed the catalog to 193
  messages. Localization run `29630969375` and Foundation run `29630969342` passed; the
  deterministic bundle ZIP checksum is
  `deab18a136383deb586f81d08d433cf5cb494c627c92a09b1b7a28f7b918f5da`.
- 2026-07-18: Linux evidence revision `1be3e7073962c899d152174b0164362c9d04e8f5` routed
  construction-time GTK labels, tooltips, accessible names, dropdown values, and the default
  provider name through the pinned catalog. Native run `29631012775` (job `88044414751`),
  Foundation run `29631012755`, and Flatpak run `29631012763` (job `88044414691`) passed the
  Linux validation, GTK construction-stage assertions, PO/MO checks, and GNOME 49 sandbox smoke.
- 2026-07-18: Central integration revision `0b3aeda37882646b6ad8e8d8565a3efdcca4b6ab` recorded
  the 192-message l10n bundle, Linux translation-export evidence, release-manifest pins, and
  all three Linux remote gates; coordination run `29630646183` passed with Linux job
  `88043385432` and PowerShell job `88043385414`.
- 2026-07-18: Central integration revision `11cd5e5be46aea8900cd49ac62d49fca3f4e3e67` recorded
  the 193-message l10n bundle, Linux construction-stage localization evidence, release-manifest
  pins, and all three Linux remote gates; coordination run `29631208474` passed with Linux job
  `88045006759` and PowerShell job `88045006770`.
- 2026-07-18: Localization revision `dc9a9d48a38dfeb8f6b2020417960023678d8252` added 15
  Linux-only Core, loopback-provider, runtime-startup, and profile-storage error messages,
  bringing the catalog to 208 messages. Localization run `29631551712` and Foundation run
  `29631551720` passed; the deterministic bundle ZIP checksum is
  `a8c5535b23eb27f02ff5fd3bb4c4c1c6948718f1233321305c173b1741b27e6f`.
- 2026-07-18: Linux functional revision `595a1fa81205bca0b5d17f9af624078ac82a0dbc` wired the
  runtime/storage error catalog keys through the native error mapper. Native run `29631662278`
  (job `88046380380`), Foundation run `29631662275` (job `88046380379`), and Flatpak run
  `29631662280` (job `88046380350`) passed the Linux validation, GTK, storage, Secret Service,
  portal, notification, drag/drop, and GNOME 49 sandbox gates.
- 2026-07-18: Linux evidence documentation revision `2277ffd1a358237cb55bde3aeaf570a94706306e`
  recorded those remote gates. Its Native run `29631828307`, Foundation run `29631828314`, and
  Flatpak run `29631828312` (job `88046930820`) passed after the evidence-only update.
- 2026-07-18: Central integration revision `30cb91557d96fbff82bea242ae8a9a722f93f9eb` recorded
  the 208-message l10n bundle, Linux runtime/storage error evidence, release-manifest pins, and
  the final Linux evidence head. Coordination run `29632016228` passed with Linux job
  `88047478552` and PowerShell job `88047478559`.
- 2026-07-18: Core functional revision `031b20cd6f4ddc7635057d1b2d949db4ac7d1f39` added
  automatic protection and streamed restoration for common URLs, email addresses, Markdown code,
  and placeholders, with typed fail-closed marker validation. Local Core checks passed; the
  functional revision's Native SDK run `29632398136` passed. A test-only descendant
  `c1406eb60c56cc4bebdf130f0cc6ee6602046c83` made the loopback HTTP regression case-insensitive
  for `Content-Length`; its CI run `29632565728` and Native SDK run `29632565726` passed all jobs.
- 2026-07-18: Linux revision `79de8d9e01bebdb4be666ef7a1aed6309ef25970` negotiated
  `protected_spans_v1`, pinned Core `031b20cd6f4ddc7635057d1b2d949db4ac7d1f39`, and documented
  the Linux boundary and automatic protection assumption. Native run `29632530497` (job
  `88048916214`), Foundation run `29632530524` (job `88048916265`), and Flatpak run
  `29632530485` (job `88048916150`) passed. Central manifests and compatibility records now pin
  this Linux revision while other clients remain deferred.
- 2026-07-18: Central integration revision `a662fd53209730d552bc3c2869b7a5f98e537023` recorded
  the protected-span Core/Linux pins, compatibility boundary, release-manifest source revisions,
  and remote evidence. Coordination run `29632758636` passed with Linux job `88049553494` and
  PowerShell job `88049553476`.
- 2026-07-18: Core functional revision `3f96de03eb4ff04add09473fc1473c2c49d67a51` added bounded,
  request-level glossary validation and protected-span restoration for required target terms or
  immutable names. Local workspace checks, full tests, build, cargo-deny, and Native SDK passed;
  its Native SDK run `29633431920` passed. Test-only descendant `da83df8effa9611e496e1c288e6a1f08e1560d2c`
  removed a credential-signature test fixture false positive; CI run `29633611719` and Native SDK
  run `29633611665` passed all Windows, Apple, Android, and Linux jobs.
- 2026-07-18: Localization revision `2e5e3033f453aa2882cf71217f9514dce8501269` added three
  request-level glossary messages to all twelve official/pseudo Linux packs, bringing the catalog
  to 211 messages. Lint, deterministic generation/test/build, and checksum `116a9cdedd8b0a3d31171b365969b745681e50257e183b40aa2c37c77f1e6d91` passed.
- 2026-07-18: Linux revision `3affedb1cc95d9ec57823459f7cf8c91f3eb16bb` exposed the request-level
  glossary field and semicolon-separated `source => target` UI rules, pinned Core/l10n revisions,
  synchronized PO/MO resources, and documented the in-memory scope. Local validation passed 53
  no-default tests, 80 demo-provider tests with one controlled ignore, locked build, Docs.rs
  checks, strict Clippy, PO syntax, and l10n sync. Native run `29633550137` (job `88051695699`),
  Foundation run `29633550177` (job `88051695826`), and Flatpak run `29633550134` (job `88051695714`)
  passed.
- 2026-07-18: Central release and compatibility records were advanced to Core functional
  `3f96de03eb4ff04add09473fc1473c2c49d67a51`, l10n `2e5e3033f453aa2882cf71217f9514dce8501269`,
  and Linux `3affedb1cc95d9ec57823459f7cf8c91f3eb16bb`; Android, Windows, and macOS remain deferred
  by the Linux-first scope.
- 2026-07-18: Central revision `b8f669cef2a2ca74ecb5b04f832feff0a63068d7` passed coordination run
  `29633816618` (Linux job `88052398800`, PowerShell job `88052398798`) after recording the
  Core/glossary, l10n, Linux, compatibility, and release-manifest evidence.
- 2026-07-18: Core functional revision `ce2b2ab6afa32cb6bbdd45c716fcad8baae00d29` added
  `long_text_chunking_v1`: UTF-8-safe semantic chunking, ordered sequential provider streaming,
  shared cancellation propagation, and a request-level byte limit with a conservative 16 KiB
  default. Local fmt, Clippy, full workspace tests, build, cargo-deny, and Native SDK checks
  passed; CI run `29634199994` and Native SDK run `29634199989` passed all matrix jobs.
- 2026-07-18: Linux functional revision `4adaae2cadbce5b19a38d6f133f4c8b843fd870d` negotiated
  `long_text_chunking_v1`, pinned Core `ce2b2ab6afa32cb6bbdd45c716fcad8baae00d29`, and documented
  ordered cancellation-aware chunk streaming plus the approximate byte-budget boundary. Local
  no-default and demo-provider suites, docs.rs checks, strict Clippy, l10n sync, and PO checks
  passed; Native run `29634278185` (job `88053679712`), Foundation run `29634278188`
  (job `88053679758`), and Flatpak run `29634278182` (job `88053679696`) passed.
- 2026-07-18: Central compatibility and release records were advanced to Core functional
  `ce2b2ab6afa32cb6bbdd45c716fcad8baae00d29`, Linux `4adaae2cadbce5b19a38d6f133f4c8b843fd870d`,
  and l10n `2e5e3033f453aa2882cf71217f9514dce8501269`; Linux remains the prioritized client while
  Android, Windows, and macOS stay deferred. Stable release status remains unreleased.
- 2026-07-18: Central revision `df262726d2f0727ff51a69d9d62701cc6504a86c` passed coordination run
  `29634540903` with Linux job `88054421542` and PowerShell job `88054421575` after recording the
  Core/Linux long-text pins, compatibility boundary, and unreleased release posture.
- 2026-07-18: Core functional revision `7adc9cdf6c8243243d42136f8b80fe3ee19f0af1` added a
  deterministic UTF-8 glossary CSV contract with a fixed header, 4 MiB byte bound, 256-row bound,
  strict quoting, value validation, conflict checks, and round-trip tests. Core CI run
  `29635065402` and Native SDK run `29635065341` passed all jobs.
- 2026-07-18: Localization revision `8fd778a5869c8b8c91610c22241883fff2e41c99` added eleven
  Linux-only glossary CSV actions, dialogs, errors, and status messages, bringing the catalog to
  222 messages. The deterministic bundle checksum is
  `7bab80f8f94d29a4e22d1257b20cfb45800ee45c74fd58ff25751d2a33e9284c`; Localization run
  `29635157822` and Foundation run `29635157780` passed.
- 2026-07-18: Linux revision `405ddc9f995499be69f78fc1311c80381e289fee` added native GTK/GIO
  glossary CSV import/export, request-level state routing, localized controls, bounded reads, and
  deterministic export. Native run `29635297466` (job `88056466684`), Foundation run
  `29635297461`, and Flatpak run `29635297451` (job `88056466121`) passed. Linux remains the
  prioritized client while Android, Windows, and macOS stay deferred; persistent glossary libraries
  and TBX import remain outside the current slice.
- 2026-07-18: Central revision `be7970f16c946ebcc38f849ef30fcc3c081b3867` recorded the Core, l10n,
  and Linux glossary CSV pins, evidence, checksums, and unreleased posture. Coordination run
  `29635479613` passed with Linux job `88056955332` and PowerShell job `88056955356`.
- 2026-07-18: Core revision `225d1edc0316b11ea0791c658adc14bd811dc865` added the explicit
  `TranslationPrivacyMode` Standard/Incognito request policy with serde-default compatibility and
  regression coverage. CI run `29635844739` and Native SDK run `29635844709` passed all matrix jobs.
- 2026-07-18: l10n revision `e5c51a046e01c51b106ba3d177e33e41a69b8aa0` added three Linux-only
  Incognito control/status messages, bringing the catalog to 225 messages. Localization run
  `29635848454` and Foundation run `29635848465` passed; the deterministic bundle checksum is
  `012fc5fb90e63259eac8e65e219f9b4d920f1b3cc0ebfa37b69718115900277c`.
- 2026-07-18: Linux revision `78293684227b40af0b26442d9d23e2ff71d3d36d` added the GTK Incognito
  toggle, reducer routing, localized status notice, and the updated Core/l10n pins. Native run
  `29635954249` (job `88058210096`), Foundation run `29635954224`, and Flatpak run `29635954240`
  (job `88058210082`) passed. The current worker has no history or translation-memory write path;
  those stores and end-user prompt approval remain open, while Android, Windows, and macOS stay
  deferred by the Linux-first scope.
- 2026-07-18: Central revision `651fc4ce9d7d6ebf61970e05b87109303bcb3f26` advanced the compatibility
  matrix, implementation status, release manifest pins, and known limitations for the Incognito
  checkpoint. Coordination run `29636156878` passed; stable release remains unreleased.
- 2026-07-18: Core revision `8cd65c5846a677e70c4828e4b4a5192319d775d5` added SQLite schema 3 bounded
  translation history with Incognito-aware writes, 100-entry/4 MiB limits, clear support, and
  storage tests. Core CI run `29636624648` and Native SDK run `29636624656` passed.
- 2026-07-18: l10n revision `4678fc3810b1e21e5ab8c1095e552930b8649687` added five Linux history
  action/status messages, bringing the catalog to 230 messages. Localization run `29636630359`
  and Foundation run `29636630348` passed; bundle checksum is
  `03889105a74aec819ae716ee577f78e1da8a235d42be4918aa0fb6f9c5e194b8`.
- 2026-07-18: Linux revision `b968cc21978dd5bea1b4bc6d1c8828bb8ecdc489` wired completed standard
  translations into bounded history, skipped Incognito writes, restored the startup count, and
  refreshed the count immediately after successful writes. Native run `29637270603`
  (job `88061682829`), Foundation run `29637270599`, and Flatpak run `29637270601`
  (job `88061682853`) passed. Documentation head `b01b4b9` records the evidence; Android, Windows,
  and macOS remain deferred by the Linux-first scope.
- 2026-07-18: Core revision `6079138348f3182b19c017f50db768df05da62cb` added newest-first history
  listing and exact per-entry deletion; Core CI `29638085207` and Native SDK `29638085241` passed.
- 2026-07-18: l10n revision `971d1691a4eff396c71216b898e30fcfb23e72fa` added ten Linux history
  window/export/delete messages, bringing the catalog to 240; Localization `29638057493` and
  Foundation `29638057470` passed with bundle checksum
  `36f782f45a228f68520c691a7d015a4839531a892732e31119fd5c0e83a2be9c`.
- 2026-07-18: Linux revision `9ff8f3fb9cf61e1f51c3fc5e042e5fc8f601b837` added the GTK history
  window, exact deletion, escaped UTF-8 TSV export, worker commands/events, and regression tests.
  Native `29638278667` (job `88064319932`), Foundation `29638278676`, and Flatpak `29638278677`
  (job `88064320034`) passed the Linux gates.
- 2026-07-18: Central revision `08250c870b42b6df249c30a0379a5db505ef23c2` recorded the Linux
  history-controls pins, evidence, and remaining translation-memory/history-policy limitations;
  coordination run `29638614216` passed with Linux job `88065175722` and PowerShell job
  `88065175707`.
- 2026-07-18: Core revision `fb00f3dd6b62a8a3a47350acc85831e60e266929` added schema 4 persisted
  history enable/disable policy; CI `29638960182` and Native SDK `29638960230` passed.
- 2026-07-18: l10n revision `40f3914e1b28fddd8f38d287fa121010f5192f1c` added four Linux history-policy
  messages, bringing the catalog to 244; Localization `29639069395` and Foundation `29639069371`
  passed with bundle checksum `f3e49113ed85e7e4fadeef6b872ccfe5a2e4fa67548028db5f4524479aedeeb4`.
- 2026-07-18: Linux revision `7173d4a4217d6211c7dc92c368d9f033874198f5` added the persisted
  history policy toggle and worker regression coverage; Native `29639139698` (job `88066556152`),
  Foundation `29639139712`, and Flatpak `29639139725` (job `88066556256`) passed.
- 2026-07-18: Central revision `e1bcf55ed16f734e14a559e292588dc8285c672e` recorded the Linux
  history-policy pins, evidence, and remaining translation-memory limitation; coordination run
  `29639330664` passed with Linux job `88067060177` and PowerShell job `88067060171`.
- 2026-07-18: Core revision `b5fb19cf2123b70587775cd6e4a68515a5790575` added schema 5 optional
  translation memory with versioned identity, persisted policy, Incognito bypass, cache reuse,
  inspection, export, exact deletion, and clear-all; CI `29640169852` and Native SDK `29640169834`
  passed. l10n revision `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995` added 262-message Linux controls;
  Localization `29640108992` and Foundation `29640108969` passed with checksum
  `a3de4b0bf4afd710a01d15e0426f0d163b56910c0b04f26c411870eae9eea368`. Linux revision
  `2cd9cdc2dfb423e5d9da56f3a235efba8727da53` passed Native `29640319555` (job `88069646252`),
  Foundation `29640319563`, and Flatpak `29640319593` (job `88069646300`).
- 2026-07-18: Core revision `e207754a35d9e29b8716420e1d19f755c9e27682` added the
  `linguamesh-document` crate and negotiated `bounded_text_document_v1` for bounded UTF-8 TXT/
  Markdown inspection, segment reconstruction, preserved line endings, and verbatim fenced code;
  CI `29640818611` and Native SDK `29640818595` passed. Linux revision
  `07065259f84dac09618627fda1b0f3c90f8bc9d0` routed native import through the contract and passed
  Native `29640999127` (job `88071403342`), Foundation `29640999121`, and Flatpak `29640999145`
  (job `88071403518`). The initial run `29640946521` failed before validation at an incorrect Core
  SHA checkout and is retained as failure evidence; the corrected pin is the verified source.
- 2026-07-18: Core revision `6c54f329e9a62ffa1d2f9503087e59d4b9e9d6e9` added schema-6 bounded
  `document_jobs`/`document_segments` snapshots, lifecycle state, segment updates, and restart-safe
  resumable-job APIs; CI `29641613390` and Native SDK `29641613407` passed. Linux revision
  `c0d944ddd86ea742fc8cc79187f8be81f240c144` wired worker create/list/update/resume/cancel commands
  and startup recovery without paths or credentials; Native `29641700063` (job `88073175248`),
  Foundation `29641700069`, and Flatpak `29641700077` (job `88073175155`) passed.
- 2026-07-18: Linux revision `ec7a12c649c03c20d7a9665a6499fe8eece6023e` connected native TXT/Markdown
  import to persisted Core jobs and added sequential `TranslateDocumentJob` execution, per-segment
  persistence, reconstruction, cancellation, glossary/privacy propagation, and startup editor restore.
  Local Linux validation passed 91 tests (one intentional environment skip), strict Clippy, format,
  l10n, and diff checks. Native `29642622311` (job `88075537969`), Foundation `29642623263` (job
  `88075540141`), and Flatpak `29642624183` (job `88075542529`) passed. Multi-job queue UI, retry,
  archive codecs, and automatic provider-parameter persistence remain open; Android, Windows, and
  macOS remain deferred.

- 2026-07-18: Core revision `31e7d3d06abbbf32199432bdedfcaf9a46dbed38` added schema-8 validated
  non-secret document options; Linux revision `d5e9bb13e75e172e8698d5227e4ac27a7e70dd35` added
  exact provider/model matching and worker-restart reuse. Native `29644639413` (job `88080730976`)
  and Foundation `29644639392` (job `88080730938`) passed; Flatpak `29644639396` (job `88080730937`)
  also passed.
  Core CI `29644499145` and Native SDK `29644499158` passed. The Linux-first scope still leaves
  multi-job selection, archive codecs, Android, Windows, and macOS open.
- 2026-07-18: Assumption: the next bounded Linux document slice preserves SRT/WebVTT cue IDs,
  headers, timestamps, ordering, and line endings while translating cue text only. Core revision
  `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` added subtitle structure/timestamp validation and
  inter-cue WebVTT metadata handling; Linux revision `33b47852f3bd3a0a4a8997cd6592c756a0b254a3`
  added `.srt`/`.vtt` chooser support and safe malformed-structure errors. Core CI
  `29645385353` passed; Native SDK `29645385324`, Linux Native `29645547013` (job `88083068099`),
  Foundation `29645547036` (job `88083068179`), and Flatpak `29645547024` (job `88083068088`) passed.
  Central coordination `29645763887` passed Linux job `88083632226` and PowerShell job
  `88083632209`. HTML and JSON were subsequently delivered in Core revisions `912780f21d8dbb19571c9b991879778a053272f8`
  and Linux revision `2a04c096594f5358638fc9e5b1610c78c1051a13`, with remote gates recorded in the
  central compatibility matrix. DOCX, PPTX/XLSX, EPUB, PDF/OCR, archive formats, multi-job selection,
  Android, Windows, and macOS remain open.

- 2026-07-18: Core revision `08eb64cb87d9cf6df624225819818d8287063c4c` added bounded DOCX package
  inspection/reconstruction and schema-10 package persistence; Linux revision
  `96c22dd1a5ac964b79124b790117b0b5dd16f2ae` added DOCX chooser/import, worker reconstruction, and
  binary export. Packaging revision `3725ef97584b30ee34e7807e35cddc16df6ad8ae` pins the final Linux
  source and vendored dependencies. Core CI `29650212367`, Native SDK `29650212378`, Linux Native
  `29650642852` (job `88096278936`), Foundation `29650642855`, and Flatpak `29650642850` (job
  `88096278936`) passed. DOCX is now the supported Linux archive slice; PPTX/XLSX, EPUB, PDF/OCR,
  remaining archive formats, Android, Windows, and macOS remain open.
- 2026-07-18: Core revision `0f71a652a536753f48bb8c852fd38e97740c23ce` added bounded PPTX
  inspection/reconstruction and schema-11 package persistence; Linux revision
  `ce08d1232889522bead58e6056d296f0fc8d56e1` added PPTX chooser/import, worker reconstruction, and
  binary export. Packaging revision `766b78e4b236f15ee7a6f1d6e61ebd828415da82` pins the final
  Linux source. Core CI `29651206485`, Native SDK `29651206487`, Linux Native `29651317600`, and
  Foundation `29651317621`, and Flatpak `29651317679` passed. Central coordination `29651628740`
  passed Linux job `88098822928` and PowerShell job `88098822937`. PPTX is now supported in the
  Linux archive slice; XLSX, EPUB, PDF/OCR, remaining archive formats, Android,
  Windows, and macOS remain open.
- 2026-07-18: Core revision `36f256637236636889b0933cc5fe6a70bffff02c` added bounded XLSX
  shared-string/worksheet inspection/reconstruction and schema-12 package persistence; Linux
  revision `731072eb3d9b29a43fe0e238084290cd5c253e59` added XLSX chooser/import, worker
  reconstruction, and binary export. Core CI `29651848624`, Native SDK `29651848606`, Linux
  Native `29651990077`, Foundation `29651990067`, and Flatpak `29651990064` passed. XLSX is now
  supported in the Linux archive slice; EPUB, PDF/OCR, remaining archive formats, Android, Windows,
  and macOS remain open.
- 2026-07-18: Assumption: Linux-first EPUB support is bounded to 4 MiB and 512 ZIP entries,
  requires a first uncompressed `mimetype`, `META-INF/container.xml`, an OPF package, and at least
  one XHTML/HTML content document. Core revision `554c09521b57de45be154a99edfbf24aa2fc6538` added
  schema-13 EPUB persistence, safe visible-text reconstruction, resource retention, and OPF
  `dc:language` updates from the target locale; Linux revision `3f0f659ccba195e58789d80d9fdc20b087a10b68`
  added chooser/import, worker export integration, MIME filtering, Flatpak pinning, and evidence
  docs. Core document/storage tests (22/28) and Linux checks/Clippy/library tests (61) passed;
  Core CI `29652884450`, Native SDK `29652884430`, Linux Native `29652937783`, Foundation
  `29652937750`, and Flatpak `29652937761` passed. EPUB is now the supported
  Linux archive slice; PDF/OCR, remaining archive formats, multi-job selection, Android, Windows,
  and macOS remain open.

- 2026-07-18: Assumption: Linux-first text-PDF support is bounded to 4 MiB, 256 pages, 4,096
  objects, and 100,000 content operators. Core revision `7275c5ec195946ea20a2d65e5f42790b2d631ff2`
  adds page-aware text extraction, basic coordinates and reading-order boundaries, Flate stream
  support, safe ASCII literal/hex rewriting, schema-14 persistence, and a structured HTML
  alternative when target text cannot be safely encoded. Linux revision
  `a64e3751bdab9e6f21901f1d3bc8a7eb8004d0f0` adds PDF chooser/MIME filtering and worker export
  fallback to `.html`; image-only pages, OCR, and pixel-identical reconstruction remain explicitly
  out of scope. Core CI `29653737299`, Native SDK `29653737293`, Linux Native `29653900764`,
  Foundation `29653900780`, and Flatpak `29653900782` passed. PDF is now the supported Linux
  text-document slice; OCR, remaining archive formats, multi-job selection, Android, Windows, and
  macOS remain open.

- 2026-07-18: Assumption: PDF fidelity warnings remain advisory structured metadata and never
  include source text or credentials. Core revision `4f03618ffb1f37f27fb1edcf2de5a80e3bec540d`
  added warnings for limited reconstruction, image-only pages, and uncertain reading order. Core CI
  `29654538722` and Native SDK `29654538670` passed. Linux revision
  `edbfad1a8e443d86f39c782f4ad991a029cb8e76` stores warnings on imported/restored jobs and renders
  bounded page-number-only UI text; Native `29654651108`, Foundation `29654651074`, and Flatpak
  `29654651067` passed. Central release and compatibility records must consume these pins; OCR,
  pixel-identical reconstruction, remaining archive codecs, and non-Linux clients remain deferred.

- 2026-07-18: Assumption: subtitle readability warnings are advisory cue-level metadata and never
  expose source text or rewrite timing. Core revision `81be0b8be9d7115b98eae3f134b4fd0f25411bbb`
  adds configurable line-length and reading-speed warnings with 42-character and 17
  non-whitespace-character-per-second defaults; Linux revision
  `829b502d98c570c72489720df49c3356dccc636a` persists and renders cue-number-only guidance. Core
  CI `29655212117`, Native SDK `29655212149`, Linux Native `29655260438`, Foundation `29655260426`,
  and Flatpak `29655260429` passed. OCR, remaining archive formats, acceptance scenarios 2–20,
  non-Linux clients, and stable release remain open.

- 2026-07-18: The Linux-first localization follow-up adds canonical `warning.subtitle_line_length`
  and `warning.subtitle_reading_speed` messages. l10n revision
  `6bcd237170d1fdfb0a6beb88ee97d1855c478611` contains 264 messages and bundle checksum
  `ee7bf5308a7cd652cad37e8d5e96973c520123dbbf964ddee58bf02bb24cbf7e`; Linux revision
  `07af541f5c8561da4f917406c6782155a2a5efb6` pins the generated PO/MO resources. Localization
  runs `29655762044` and `29655762054`, Native `29655816018`, Foundation `29655816025`, and
  Flatpak `29655816020` passed. Non-English translations remain explicitly unreviewed drafts.

- 2026-07-18: The Linux-first PDF localization follow-up adds canonical
  `warning.pdf_reconstruction_limited`, `warning.pdf_image_only_pages`, and
  `warning.pdf_uncertain_order` messages. l10n revision
  `738a7c7328f24acc12c15be78bb11737220bbbae` contains 267 messages and bundle checksum
  `49ccf84b2afac15c604f74c45c6e7e72a1c12617eb5efdb3ada1d5164cd3c259`; Linux revision
  `60b560383e53bf4cf9ccc5ecf3821fe735206446` consumes the generated PO/MO resources. Localization
  runs `29656124100` and `29656124109`, Native `29656158543`, Foundation `29656158527`, and
  Flatpak `29656158526` passed. Complete visible-string coverage beyond these document warnings
  and the remaining acceptance/release work remain open.

- 2026-07-18: The Linux-first document-queue localization follow-up adds ten canonical Linux-only
  action, dialog, empty/paused/progress status, and tooltip messages. l10n revision
  `0ef4fb9b6878655e46e2b8ca5bbed9562f97b0f0` contains 277 messages and bundle checksum
  `e26da1a391369ed84c0f57f5fd5d440f50ed56dcbc8f069abd4d6d27db7dd9c1`; Linux revision
  `191345c55dc8989d518680c864a4c4a643165f6c` synchronizes all twelve PO/MO packs and asserts the
  queue keys. Localization runs `29656496378` and `29656496361`, Native `29656549651`, Foundation
  `29656549644`, and Flatpak `29656549677` passed. Non-English packs remain explicitly unreviewed
  drafts; complete visible-string coverage, other clients, OCR, and stable release remain open.

- 2026-07-18: Linux test head `1e60e3725b0548a82bb88402c5257eb0f5f0bb0c` extends the real GTK
  lifecycle regression with keyboard-focus assertions for Document jobs, Pause, Resume, and Retry.
  Local format/check/Clippy and 61/99-test suites passed; Native `29657086074`, Foundation
  `29657086060`, and Flatpak `29657086067` passed. Screen-reader narration, physical keyboard
  traversal, routing fallback, OCR, and other acceptance gaps remain open.

- 2026-07-18: Linux-first exported-output follow-up adds l10n revision
  `4be0401a09ce26e65c8fd3c921e333d6011e8706` with localized open-output/open-failure messages,
  bringing the bundle to 280 messages and checksum
  `61fe261fb62e996b637745913bb89e5a5e0c0a16a82c5d2fe536a254cf61b6ee`. Linux revision
  `45d9365eaba0b25d58c65a09e4a5dcfa2bae0840` records only successfully written GIO URIs, exposes a
  focusable default-handler action, clears stale destinations on new imports/translations, and
  keeps open failures path-safe. Local no-default/demo-provider tests (61/99, one existing
  environment skip), GUI cargo check, strict Clippy, formatting, l10n sync, and diff checks passed;
  host GTK linking lacks required symbols. Localization `29657734947`/`29657734951`, Native
  `29657811742`, Foundation `29657811734`, and Flatpak `29657811738` passed. Routing fallback, OCR,
  screen-reader narration, physical keyboard traversal, other clients, and stable-release evidence
  remain open.

- 2026-07-18: Linux-first approved text fallback follow-up adds l10n revision
  `273be8a4e9c3b1084f393ce0086cdf2c42fcd4e9` with six Linux-only messages, raising the bundle to
  286 messages and checksum `ee7c269571beca22cdbd7bea971ae266975b8004490b02ead4b71305e3a93872`.
  Linux `878a9c015d29ce49633046d435f48f5fee4c9a47` adds a user-selected different saved provider
  fallback for retryable network/timeout failures on ordinary text only, preserving partial output;
  document jobs, cancellation, authentication/model failures, unapproved profiles, and session-only
  profiles never fall back. Local 61/100 tests plus the focused fallback test, strict Clippy, GUI check,
  l10n sync, and diff checks passed. Native `29659054771`, Foundation `29659054755`, and Flatpak
  `29659054756` passed; OCR, screen-reader narration, physical keyboard traversal, other clients,
  complete acceptance scenarios, and stable-release evidence remain open.

- 2026-07-18: Linux keyboard traversal follow-up adds a runtime-only GTK focus probe and the
  `tools/run-gtk-keyboard-focus-test.sh` Xvfb/xfwm4 fixture. Tab and Shift+Tab reach the tested
  onboarding/workspace controls; provider fields are asserted enabled, mapped, and focusable but
  remain outside the default Tab chain and are tracked as an explicit Linux follow-up. Linux
  revision `abdbe78` passed Native `29661215896` (job `88124076970`), Foundation `29661215890`,
  and Flatpak `29661215925` (job `88124076966`). Local formatting, GUI check, shell syntax, and
  diff checks passed. Screen-reader narration, provider-form Tab-chain repair, physical desktop
  review, OCR, other clients, and stable-release evidence remain open.

- 2026-07-18: Assumption: the provider form's explicit order is saved profile, remove saved
  profile, provider name, endpoint, credential, Connect, and Remember profile; Ctrl/Alt/Super
  modified Tab remains native workspace navigation. Linux revision `8f2cba09e500e8d3a3ea5e6ef9f10d6244369305`
  moves the handler to the application-window Capture phase and verifies the real GTK focus path
  with an Xvfb/xfwm4 fixture. Default-branch Native `29663597817` (job `88130256368`), Foundation
  `29663597809` (job `88130256318`), and Flatpak `29663597831` (job `88130256370`) passed; local format, strict
  Clippy, 61-library-test suite, shell syntax, and diff checks passed. Screen-reader narration,
  physical desktop review, OCR, other clients, and stable-release evidence remain open. Central
  coordination run `29663798879` (job `88130763937`) also passed.

- 2026-07-18: Assumption: the smallest reproducible Linux screen-reader slice is live AT-SPI tree
  export for the primary translation controls. Linux revision `7480579e4ae305758397082b7456715939666a9e`
  adds an isolated Xvfb/xfwm4 fixture that starts the AT-SPI bus and reads the running GTK tree with
  `python3-pyatspi`, verifying the named `Stop translation` push button and two text-editor roles;
  the existing GTK helper still verifies label relations, editor properties, and state changes.
  Default-branch Native `29664478686` (job `88132499067`), Foundation `29664478672`, and Flatpak
  `29664478670` passed. Orca speech, provider-form default Tab-chain review, physical desktop
  accessibility, OCR, other clients, and stable-release evidence remain open. Central coordination
  `29664611878` (Linux job `88132835095`, PowerShell job `88132835104`) passed.

- 2026-07-18: Assumption: existing catalog keys `field.source_text` and `field.translation` are
  the canonical labels for source and translated content in history and translation-memory dialogs.
  Linux revision `1b68cef85d89324baba20689ce246486ab28c49b` replaces those fixed English prefixes
  without changing stored content or adding locale-pack keys. Native `29664934283` (job
  `88133657483`), Foundation `29664934298`, and Flatpak `29664934279` passed. Dynamic `Job` and
  `Identity` metadata, complete visible-string gettext coverage, and the remaining Linux/release
  boundaries remain open.

- 2026-07-18: Assumption: the existing `dialog.document_jobs` and `dialog.memory` catalog titles
  are the canonical Linux labels for job and translation-memory metadata rows. Linux revision
  `c19192fbd78b30aa55a5bac94c133c7400c78642` routes those identifier prefixes through the active
  catalog without changing stored content or locale packs. Local fmt, strict Clippy, the locked
  no-default 61-test suite, and diff checks passed; Native `29665343100` (job `88134735908`),
  Foundation `29665343120`, and Flatpak `29665343145` passed. Complete visible-string gettext
  coverage, Orca speech, physical desktop review, OCR, other clients, and stable-release evidence
  remain open.

- 2026-07-18: Assumption: the persisted `DocumentJobSnapshot` list remains the source of truth
  for the Linux multi-job queue. Linux `014a79a19cb72b4eceba3d7c0c592b7655e1cdd0` adds
  catalog-backed pause, resume, and retry actions to each row while reusing the existing worker
  commands and state machine. Local strict Clippy, no-default 61 tests, demo-provider 99 tests
  (one existing environment-dependent ignore), formatting, and diff checks passed; Native
  `29665725241`, Foundation `29665725238`, and Flatpak `29665725434` passed. Orca speech, physical
  desktop review, OCR, complete visible-string gettext coverage, other clients, and stable-release
  evidence remain open.

- 2026-07-19: Assumption: request-level glossary syntax, credential-like data rejection, and
  conflicting-rule errors are stable Linux UI messages. l10n `ede66149c501a1680ed050d76b8b78e7b565ba01`
  adds three dedicated keys, producing 289 messages and checksum
  `c8bd6b0464ebbfa015988a4fc0cfd30b1f9e28d9e1aad19b8c50d36976128e8f`; Linux
  `cb22b2052362ce7b4990cc4be99e26a152b07800` synchronizes the catalogs and maps all three errors.
  Local l10n make check, targeted localization regression, strict Clippy, no-default 61 tests,
  l10n sync, and diff checks passed. Native `29666379600`, Foundation `29666379579`, and Flatpak
  `29666379586` passed. Complete gettext coverage, Orca speech, physical desktop review, OCR,
  other clients, and stable-release evidence remain open.

- 2026-07-19: Assumption: provider onboarding controls require a deterministic application-window
  Tab/Shift+Tab order while modified Ctrl/Alt/Super shortcuts remain native workspace navigation.
  Linux revision `713c86b3da9b057cc25e72c687dc6c4c265f6439` records the Capture-phase handler and
  its Xvfb/xfwm4 fixture evidence. Native `29666820550`, Foundation `29666820602`, and Flatpak
  `29666820579` passed for the current head. The local GTK fixture could not link because the host
  lacks the required GTK 4 symbols; the remote Native gate is the executable evidence. Orca speech,
  physical desktop review, OCR, complete visible-string gettext coverage, other clients, and
  stable-release evidence remain open.

- 2026-07-19: Assumption: document-job row metadata is user-visible Linux UI and must use stable
  technical format labels plus catalog-backed lifecycle labels; Rust `Debug` output is not a
  presentation contract. l10n revision `c81728faf8679e7a5e9854537ad7c70c046c7800` adds seven
  Linux-only messages, producing 296 canonical messages and bundle checksum
  `d2f4fd439b5fbc8fc6d48f1be0a91ee92f558c70b851271d643829cfe8590e9b`. Linux revision
  `76b5f632fee62dc8e323e0cfec5d420e6fcc6992` maps the row template and pending/running/paused/
  completed/cancelled/failed labels through the active catalog. Local l10n make check, Linux
  format/Clippy/test/sync checks passed; Native `29667553178`, Foundation `29667553139`, and
  Flatpak `29667553149` passed. The initial Native gate failed on the stale l10n pin and was fixed
  by `fd30017b8d59df8daed3c18cef47e8741f42d904`; Orca speech, physical desktop review, OCR,
  complete visible-string gettext coverage, other clients, and stable-release evidence remain open.

- 2026-07-19: Assumption: image-only PDF OCR is an explicit Linux opt-in capability, not a default
  reconstruction promise. l10n `3f3c1a1154b66d25f2936a02b8a08d2a8fc8a878` adds ten OCR toggle,
  progress, and fixed-error messages, producing 306 messages and bundle checksum
  `6fc6839fce3a449eaf37d2efb9a52fa0ede1eab3a39fecdaff68682a79d8a4f8`. Linux
  `d18e8dfa3dd98d56dbe0d5d1eabc536d38b96f1c` invokes bounded shell-free `pdftoppm`/`tesseract`
  processes only after explicit user opt-in, stores page-marked TXT jobs, and keeps source PDFs
  untouched. Local Linux tests and the generated OCR fixture passed; Native `29668688201`,
  Foundation `29668688202`, and Flatpak `29668688223` passed, as did l10n `29668388983`/`29668388992`.
  Orca speech, physical desktop review, complete visible-string gettext coverage, other clients,
  and stable-release evidence remain open.

- 2026-07-19: Assumption: literal keys passed to Linux localization helpers must exist in the
  canonical catalog; dynamic keys remain covered by runtime localization tests. Linux revision
  `a26ee1855e6d46ac1c174f1388bae5eb09420588` adds the dependency-free
  `tools/check-localization-keys.py` audit and runs it in Native/Foundation validation. The audit
  covered 187 source keys against the 306-message l10n revision
  `3f3c1a1154b66d25f2936a02b8a08d2a8fc8a878`; Native `29669448961`, Foundation `29669448991`,
  Flatpak `29669448995`, and pull-request reruns `29669459291`/`29669459309`/`29669459312` passed.
  Translated-copy, plural, visual locale/RTL, Orca speech, other clients, and stable-release
  evidence remain open.

- 2026-07-19: Assumption: the non-sensitive diagnostics panel is user-visible UI and its
  compatibility summary must follow runtime locale changes without exposing source text, endpoints,
  or secret references. Linux revision `3a135bf86d3627dafb48d53164e4568a9c9e5c03` routes the Core
  ABI/protocol header through `diagnostics.summary` and adds Simplified Chinese/source-exclusion
  regression coverage. Local Rust/l10n/OCR checks passed; push Native `29670658430`, Foundation
  `29670658434`, and Flatpak `29670658437` passed, as did PR reruns
  `29670659495`/`29670659502`/`29670659509`. Orca speech, manual visual review, prompt approval,
  other clients, and release artifacts remain open.

- 2026-07-19: Assumption: fixed diagnostics labels and state values are Linux-visible copy and must
  use the canonical catalog while identifiers, endpoints, and output content remain excluded.
  l10n `32bef261f5f0deb9f6a0426231e365d0bae72b62` adds 20 Linux-only diagnostics keys, raising the
  bundle to 326 messages with checksum
  `054d6749397cbbf652e099784f2c7d0e3650779a3c17c98e68d25560d286b2d3`; Linux revision
  `355481d937b3722e509dbd05cc1575c4e71be143` raises the source audit to 208 keys. Push Native
  `29671444706`, Foundation `29671444731`, and Flatpak `29671444733` passed, as did PR reruns
  `29671445475`/`29671445499`/`29671445495`. Translated-copy, plural, visual locale/RTL, Orca
  speech, other clients, and stable-release evidence remain open.

- 2026-07-19: Assumption: a document-pause command rejected by the bounded worker queue is
  user-visible UI and must use the same catalog-backed error rendering as other worker failures.
  Linux `1d96c9825b83cdc1cd6a2783b61fdd678b89e510` routes that queue-send failure through the
  reducer error path. Push Native `29672046465`, Foundation `29672046491`, and Flatpak `29672046488`
  passed, as did PR reruns `29672047299`/`29672047295`/`29672047296`. Complete visible-string
  gettext coverage, translated-copy/plural, visual locale/RTL, Orca speech, prompt approval,
  other clients, and stable-release evidence remain open.

- 2026-07-19: Assumption: Secret Service `CreateItem` and `Delete` prompt paths are explicit
  Linux security interactions. Linux `739538cb27bdcdc4b4f8530da6dcd5110550a310` calls the
  `org.freedesktop.Secret.Prompt` object, waits for `Completed`, accepts only approval, maps
  dismissal through a new catalog key, and fails closed on prompt-call or timeout failures. l10n
  `f00b00fda307660000b0e4068c5ca1072d266df1` contains 327 messages with checksum
  `53821e2397e6697b7551693c6f5787cc1f88e24d96b3077ac590645a848f1977`. Local 65/103-test
  suites, strict Clippy, the 208-key audit, sync checks, and four prompted-flow fixture cases
  passed. l10n Foundation `29672618359`/Localization `29672618363` passed; Linux push Native
  `29672741665`, Foundation `29672741666`, Flatpak `29672741675`, and PR reruns
  `29672743058`/`29672742959`/`29672742990` passed. End-user approval UX, broader storage
  faults, complete gettext/plural/visual/Orca review, other clients, and stable release remain open.

- 2026-07-19: Central revision `10657ea` records the Linux prompted-flow checkpoint, l10n
  `f00b00fda307660000b0e4068c5ca1072d266df1`, Linux behavioral/evidence heads, updated
  compatibility and release-manifest pins, and the unreleased posture. Coordination run
  `29673058773` passed Linux job `88155425506` and PowerShell job `88155425531`.

- 2026-07-19: Assumption: Linux-first Ollama acceptance can be bounded to its OpenAI-compatible
  `/v1/` surface. Core `0d0d475d22129e8211333ee8f664a7669948ce3a` adds a deterministic fixture
  returning `llama3.2:latest` and streaming `/v1/chat/completions`; Linux
  `c1e701b4b0ad35eb6cd2823d19ae83cdb235b30d` exercises explicit connect/model selection and
  streaming through `local-loopback`. Core/Linux local checks passed, as did push and PR Native
  and Flatpak runs `29673888541`, `29673888548`, `29673889609`, and `29673889576` with jobs
  `88157552503`, `88157552511`, `88157555098`, and `88157554910`. Native `/api` and a running
  third-party daemon remain unverified; Android, Windows, and macOS are deferred.

- 2026-07-19: Core `123d5c4d7a76873e597895763ca5d78e1ea42ea0` adds the loopback-only native Ollama
  `/api/tags` and `/api/chat` adapter, catalog preset, NDJSON decoder, cancellation, bounded
  response, and protected-span tests. Linux `a45ad953738766dc9fba5d9a6bd9e3b3280c62fa` adds the
  explicit `ollama_chat` worker profile and streams `你好，Ollama！` without a secret. Core CI
  `29674653973` and Native SDK `29674653960` passed; Linux push Native `29674767565`, Foundation
  `29674767554`, and Flatpak `29674767552` passed, as did PR reruns `29674768361`, `29674768357`,
  and `29674768359`. The GTK preset selector and interoperability with a running third-party
  daemon remain open.

- 2026-07-19: Central revision `c690660839606685c7e2b05d8b48041584950ff9` records Core
  `123d5c4d7a76873e597895763ca5d78e1ea42ea0`, Linux `a45ad953738766dc9fba5d9a6bd9e3b3280c62fa`,
  the native Ollama compatibility evidence, and the unreleased limitation boundary. Coordination
  run `29674950216` passed Linux job `88160536390` and PowerShell job `88160536391`.

- 2026-07-19: Assumption: verified native Ollama worker support is ready for explicit Linux GTK
  selection while third-party daemon interoperability remains external. l10n `d3d8381` adds five
  Linux provider-preset labels/tooltips (332 messages; bundle SHA-256
  `0650b68a49daf27b56c95ae149cd5c29621d890ba4c7554c7c79d5690e38a05b`). Linux
  `75d5ded3d6ab25e9a35c8614899b8ccc3cf94535` adds the localized preset dropdown, saved-profile
  restoration, default-preserving switching, and a fixture-backed GTK `/api/` connect/translate
  regression. Local GUI source checks, the 105-test worker suite, and l10n synchronization passed;
  push Native/Foundation/Flatpak runs `29675743173`/`29675743166`/`29675743159` and PR runs
  `29675744738`/`29675744785`/`29675744821` all passed. Central release and compatibility pins are
  updated while the train remains unreleased.

- 2026-07-19: Assumption: pinned gettext catalogs are the Linux runtime source of truth for plural
  selection. Linux `29e613a806b1eb096cabab2374c494ea6a07e807` retains all NUL-separated MO plural
  slots and exposes locale-specific `text_plural` selection with safe fallback. Local formatting,
  GUI checks, strict Clippy, 106-test demo-provider suite, 213-key audit, l10n sync, and diff checks
  passed. Push Native `29676132263`/job `88163825783`, Foundation `29676132239`, and Flatpak
  `29676132247`/job `88163825792` passed; PR Native `29676133164`, Foundation `29676133154`, and
  Flatpak `29676133165`/job `88163828359` also passed. Translated-copy/visual review, Orca, prompt
  approval, other clients, signing, distributable artifacts, and stable release remain open.

- 2026-07-19: Assumption: offline provider attempts must fail within a bounded interval while
  preserving the last confirmed provider, model, and request path. Linux
  `b09f47415e33c84981f0d6da6fbfc6a0e00c4a53` adds a loopback released-port regression requiring a
  typed `Network` failure under five seconds followed by successful translation through the prior
  session. Local formatting, GUI checks, strict Clippy, 107-test demo-provider suite, 213-key audit,
  l10n sync, and diff checks passed. Push Native `29676519123`/job `88164823336`, Foundation
  `29676519162`, and Flatpak `29676519121`/job `88164823343` passed; PR Native `29676520477`,
  Foundation `29676520497`, and Flatpak `29676520498`/job `88164827465` also passed. This advances
  Linux Scenario 17 evidence; physical offline conditions, third-party daemon, other clients, and
  stable release remain open.

- 2026-07-19: Assumption: visible GTK plural counts and model-discovery placeholders are
  user-facing strings and must use the canonical catalog. Linux
  `8d84636636c969e70943b534deba3818381daed6` wires the document-jobs dialog plural count and model
  placeholder, while retaining the bounded typed offline failure and previous-provider
  continuation regression. Local formatting, GUI checks, strict Clippy, 107-test demo-provider
  suite (2 ignored), 213-key audit, l10n sync, and diff checks passed. Push Native/Foundation/
  Flatpak `29676780532`/`29676780527`/`29676780531` and PR `29676781353`/`29676781358`/`29676781369`
  passed. Translated-copy, visual/RTL, Orca, physical offline, other clients, signing, artifacts,
  and stable release remain open.

- 2026-07-19: Assumption: URI equality alone cannot protect Scenario 18 when an export target is
  a source alias. Linux `c7b7599b118fa54baefe32e2063f57a890dc0f52` checks GIO identity, canonical
  native paths, and Unix device/inode metadata before text or binary replacement, with regression
  coverage for exact, symbolic-link, hard-link, and distinct targets. Local formatting, GUI checks,
  strict Clippy, 107-test demo-provider suite (2 ignored), 213-key audit, l10n sync, and diff checks
  passed. Push Native/Foundation/Flatpak `29677149812`/`29677149807`/`29677149811` and PR
  `29677151266`/`29677151263`/`29677151268` passed. Physical desktop review, Orca, other clients,
  artifacts, and stable release remain open.

- 2026-07-19: Assumption: a malformed SQLite file must fail closed without implicit repair or
  overwrite, while session-only translation remains available. Linux
  `10cc4e7414efa3f55058c5748e887c5a96481641` adds this regression and verifies typed persistence
  failure, unchanged corrupt bytes, successful session translation, and rejected saved-profile
  deletion. Local formatting, GUI checks, strict Clippy, 108-test demo-provider suite (2 ignored),
  213-key audit, l10n sync, and diff checks passed. Push Native/Foundation/Flatpak
  `29677532670`/`29677532645`/`29677532656` and PR `29677534287`/`29677534288`/`29677534304` passed.
  Physical corruption recovery, desktop/Orca review, other clients, artifacts, and stable release
  remain open.

- 2026-07-19: Assumption: the automated GTK drag-and-drop fixture button is still user-visible UI
  and must resolve through the canonical catalog. l10n `3aa86232974f9a9ece8d3a45e6760dee294fca81`
  adds `fixture.drag_file`, producing 333 messages with bundle SHA-256
  `61a054d99935b256e79d5be7feb4d929fc8cf61af663a02b8fd10475745d70bd`; Linux
  `ce1672ec3905d0c8fcc3b8f773bad64e5923158a` maps the fixture button and raises the source audit
  to 214 keys. Local formatting, GUI checks, strict Clippy, 108-test demo-provider suite (2
  ignored), l10n sync, and diff checks passed. l10n Foundation/Localization
  `29678032701`/`29678032702` passed. Push Native/Foundation/Flatpak
  `29678132379`/`29678132390`/`29678132392` and PR
  `29678130604`/`29678130600`/`29678130605` passed. Human translated-copy, visual/RTL, Orca,
  physical corruption recovery, other clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: built-in provider display names are user-visible Linux form values and
  must resolve through the canonical catalog while user-edited names remain untouched. l10n
  `85b9d45569ce840c17dc0acc7d7366d6810be48e` adds `profile.default_ollama_name`, producing 334
  messages with bundle SHA-256 `028d25b3637fbc19d41d497a860b414353615b9576db6f852a9f236bcbe770ce`;
  Linux `1153e0053b5f8e9d19dbb9ed46e9d79f9df9760a` routes new-profile initialization and untouched
  preset switching through localized default-name helpers and raises the source audit to 215 keys.
  Local formatting, GUI checks, strict Clippy, 108-test demo-provider suite (2 ignored), l10n sync,
  and diff checks passed. l10n Localization/Foundation `29678498771`/`29678498778` passed. Push
  Native/Foundation/Flatpak `29678586553`/`29678586556`/`29678586562` and PR
  `29678588077`/`29678588076`/`29678588073` passed. Human translated-copy, visual/RTL, Orca,
  physical corruption recovery, other clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: the GTK regression must drive the production locale dropdown and
  preset-notification path. Linux `f14fc89f3aecb20b3ac9611642de15d1a670ebf6` verifies localized
  OpenAI/Ollama defaults, user-edited name preservation, and demo-endpoint restoration. Local
  formatting, GUI checks, strict Clippy, 108-test demo-provider suite (2 ignored), l10n sync,
  215-key audit, and diff checks passed. Push Native/Foundation/Flatpak
  `29679490910`/`29679490922`/`29679490960` and PR `29679492044`/`29679492018`/`29679492030`
  passed. This strengthens Linux test evidence; human translated-copy, visual/RTL, Orca,
  physical corruption recovery, other clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: bounded OOXML package behavior must be verified through the Linux native
  import wrapper, not only through Core codec unit tests. Linux `258f4b3d2537e3920f63dbea561649483489d036`
  adds in-memory DOCX and XLSX fixtures: paragraph/table/header text and image retention, selected
  shared-string translation, unselected-value preservation, formula/number preservation, and
  source-buffer immutability. Local formatting, GUI checks, strict Clippy, 110-test demo-provider
  suite (2 ignored), l10n sync, 215-key audit, and diff checks passed. Push Native/Foundation/Flatpak
  `29680097142`/`29680097156`/`29680097153` and PR `29680098361`/`29680098362`/`29680098380` passed.
  This advances Linux Scenarios 10–11 evidence; macro/signature behavior, visual review, other
  clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: the Linux import boundary must reject unsafe OOXML archive entry names
  and bounded-size violations before any translation or reconstruction work. Linux
  `8e057640f9e299335c0b0d60c3881ed7c4a84346` adds in-memory DOCX `../outside.txt` and deflated
  oversized-entry fixtures, verifying `InvalidStructure` and `TooLarge` without touching an output
  path. Local formatting, GUI checks, strict Clippy, 112-test demo-provider suite (2 ignored), l10n
  sync, 215-key audit, and diff checks passed. Push Native/Foundation/Flatpak
  `29680662802`/`29680662805`/`29680662821` and PR `29680663901`/`29680663898`/`29680663922` passed.
  This advances Linux Scenario 15 evidence; full bomb heuristics, visual review, other clients,
  artifacts, and stable release remain open.

- 2026-07-19: Assumption: queue selection must expose more than one resumable job in a single worker
  listing before the GTK modal can claim multi-job coverage. Linux `be10088904be1ae2ebb833180df43b0a1c6295b8`
  retains the regression from `5b7d0d51f189412f92f722345e8dc6b4ec78314b`, creates two pending jobs,
  lists them through `ListDocumentJobs`, and verifies both stable IDs and pending states are returned
  together; `docs/testing.md` records the concurrent-translation boundary. Local formatting, GUI
  checks, strict Clippy, 113-test demo-provider suite (2 ignored), l10n sync, 215-key audit, and diff
  checks passed. Push Native/Foundation/Flatpak `29681283021`/`29681282976`/`29681282978` and PR
  `29681283843`/`29681283852`/`29681283837` passed. Concurrent translation, visual review, other
  clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: mandatory DOCX/XLSX evidence must exercise the persisted Linux worker
  command path, not only native wrapper or shared Core reconstruction fixtures. Linux
  `9ed0557a87b5c042d38e05cad5abf4a2afe487f9` adds end-to-end worker regressions that translate
  persisted DOCX and XLSX jobs through the fake provider, reconstruct the completed OOXML, and
  retain binary resources, formulas, and numeric cells; docs revision
  `468b915f050864bddff31001669ec80123263ac3` and validation docs revision
  `541d7cac307dfb4d63b61568cdc4ff441ed17c62` record the test names and actual local checks.
  Local formatting, GUI all-target checks, strict Clippy, 115-test demo-provider suite (2 ignored),
  l10n sync, 215-key audit, and diff checks passed. Push Native/Foundation/Flatpak
  `29682266701`/`29682266727`/`29682266698` and PR
  `29682268238`/`29682268236`/`29682268234` passed. Macro/signature behavior, visual review, other
  clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: the shared Core OOXML archive boundary is authoritative for Linux DOCX,
  PPTX, and XLSX safety; Linux must consume the exact immutable pin. Core
  `14cee83a650610b3a9a79a460c7c6f54ae9d21d4` rejects entries at least 1 KiB whose uncompressed size
  exceeds 200 times the compressed size, in addition to encrypted, symlinked, duplicate, traversal,
  entry-count, and total-size limits, and rejects `vbaProject.bin` and `_xmlsignatures/` parts before
  XML inspection. Core CI `29685742893` and Native SDK `29685742897` passed. Linux
  `e03a6afb93fc4d2a8d04e5feefe31e1de9935e7e` records the macro/signature boundary and bounded AT-SPI
  cleanup after the PPTX slide/notes/resource and compression-ratio evidence; local 119-pass/2-ignored
  validation and Flatpak metadata checks passed. The prior Native run `29685948051` against the old
  pin failed on the new rejection fixture; after updating the workflow pin, push Native `29686220611`, Foundation
  `29686220631`, and Flatpak `29686220605`, plus PR Native `29686222024`, Foundation `29686222035`,
  and Flatpak `29686222028`, all passed. Physical visual review, other clients, artifacts, and stable
  release remain open.

- 2026-07-19: Assumption: optional image-only PDF OCR evidence must be revalidated against the
  current Linux checkout and real external tools. Linux `0d5989186924362cb3d8de8008e8c57717669dd1`
  passed `bash tools/run-ocr-test.sh` locally using ImageMagick, Poppler, and Tesseract with the
  generated private fixture. Push Native/Foundation/Flatpak `29686617153`/`29686617163`/`29686617156`
  and PR Native/Flatpak/Foundation `29686619015`/`29686619042`/`29686619011` passed. This
  revalidates the bounded opt-in OCR path; pixel-identical PDF reconstruction, non-English OCR
  quality, physical visual review, other clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: an interrupted Linux document job must retain all pending segments and
  reuse its persisted provider/model options when explicitly retried. Linux
  `1e92fa3f145e61469f221c862584478dff95ae46` adds
  `cancelled_document_job_can_be_retried_without_losing_pending_segments`; local Linux validation
  passed with 120 tests and 2 ignored. Current-head push and PR Native/Flatpak/Foundation gates are
  push Native/Foundation/Flatpak `29687088567`/`29687088573`/`29687088558` and PR
  Native/Flatpak/Foundation `29687089446`/`29687089445`/`29687089480` passed. Concurrent document
  execution, physical interruption recovery, other clients, artifacts, and stable release remain open.

- 2026-07-19: Assumption: a failed or cancelled ordinary text request must be explicitly retryable
  without creating a document job or changing the confirmed provider/model. l10n
  `50688449ab16a8007f0edebabed2f8d6f0d3a90a` adds `action.retry_translation` and
  `tooltip.retry_translation`; Linux `9c19083aa87304ffb3fcc9cd3bfb276503d38a00` exposes the
  catalog-backed accessible action, reuses the existing Translate worker path, and guards it by
  failed/cancelled state. Local Linux validation passed 121 tests with 2 ignored, strict Clippy,
  formatting, l10n sync, 217-key audit, Flatpak metadata, and diff checks. The GUI all-target test
  binary cannot link on this host because the installed system GTK library lacks the gtk-rs GTK 4
  symbols. Linux Native/Foundation/Flatpak push and PR gates passed in runs 29689432043,
  29689432053, and 29689432045; duplicate push-triggered runs 29689431072, 29689431028, and
  29689431052 also passed. l10n runs 29689387482/29689387493 and central run 29689497792 passed.
  Automatic/ordered routing UI, other clients, artifacts, and stable release remain open.

- 2026-07-19: Linux revision `88c04495d427fbca09ce2bc6c020dd057652dae9` records the routing-mode
  and explicit fallback-consent UI evidence. The stable dropdown maps Core Manual/Ordered/Automatic
  modes, fallback consent defaults off, and local 130-test/GUI/Clippy/l10n/Flatpak checks passed.
  Push Native/Flatpak/Foundation `29696348120`/`29696348121`/`29696348094` and PR
  Native/Flatpak/Foundation `29696349676`/`29696349689`/`29696349695` passed. Complete candidate
  management, other clients, artifacts, and stable release remain open.
- 2026-07-19: Assumption: compound summaries visible to users must localize their complete
  template rather than concatenating an English prefix with data; technical identifiers,
  filenames, model IDs, and translation content remain data. l10n
  `bd06a76bcd498748b520143c61964a92727d1b51` adds `status.translation_entry_metadata`,
  `status.document_job_id`, and `provider.active_with_mode` to the 339-message bundle; Linux
  `5fe8d20cd0970e8ddb0ded0fdb207c9bc7360a36` consumes them and localizes the unavailable fallback.
  Local l10n `make check`, Linux formatting, 121 demo-provider tests with 2 ignored, GUI check,
  strict Clippy, l10n sync, 219-key audit, Flatpak metadata, and diff checks passed. Linux push
  Native/Foundation/Flatpak runs `29690203426`/`29690203419`/`29690203422` passed; duplicate
  PR-triggered Native/Flatpak runs `29690201544`/`29690201545` passed. l10n Foundation/Localization
  runs `29690127881`/`29690127894` passed; central coordination run `29690453908` passed. Human translated-copy review, Orca speech,
  automatic/ordered routing UI, other clients, artifacts, and stable release remain open.

- 2026-07-20: Assumption: Linux accessibility evidence should exercise the installed Orca process
  against the live GTK tree while keeping human listening and physical desktop review separate.
  Linux adds `tools/run-orca-atspi-test.sh` and `tools/orca-atspi-inspect.py`; Native CI installs
  Orca plus Speech Dispatcher, confirms the named `Stop translation` control through AT-SPI, and
  requires Orca's speech-generator debug record for the Linux application tree. The host lacks `xvfb-run` and `python3-pyatspi`,
  so local execution is unavailable; shell/Python static checks are the local evidence and the
  remote Native gate is required. This does not claim listening quality, translated-copy review,
  physical desktop behavior, other clients, artifacts, or stable release.

- 2026-07-20 correction: Native push run `29709041999` reached the Orca fixture but failed at job
  `88250409247` because the idle Stop button is disabled and AT-SPI rejected `grabFocus()`. The
  fixture now sets the test-only `LINGUAMESH_TEST_ORCA_ATSPI=1` flag so only that control is enabled
  during the isolated run; normal production idle behavior is unchanged. A rerun is required before
  the headless Orca checkpoint is considered verified.

- 2026-07-20: Linux headless Orca evidence is verified at source revision
  `a3bd4a3229088e24c8f1a6cd9fb6c1574ca55839`. The fixture confirms the named `Stop translation`
  control through AT-SPI and records Orca Speech Dispatcher speech-generator output for the Linux
  application tree; the remote GTK4/Orca focus handoff limitation and human-listening boundary are
  explicit. Push Native/Flatpak/Foundation `29710531278`/`29710531303`/`29710531308` and PR
  Native/Flatpak/Foundation `29710532205`/`29710532203`/`29710532204` all passed, including the
  full Native release build. Local execution remains unavailable because this host lacks `xvfb-run`
  and `python3-pyatspi`; other clients, signing, rollback, and stable release remain open.

- 2026-07-20: Assumption: Manual routing must identify exactly one provider/model; candidate chains
  belong to Ordered and Automatic modes. Linux `be985e0bf906f8c5ddcb229f4e6cc6b26d9efe7b`
  deactivates extra Manual selections in the GTK editor and normalizes save to the first displayed
  candidate, while Ordered and Automatic retain their selected chains. Local format/check/Clippy/
  test/Flatpak/diff validation passed. Push Native/Flatpak/Foundation `29713205178`/`29713205186`/
  `29713205194` and PR Native/Flatpak/Foundation `29713206482`/`29713206495`/`29713206461` are
  the current-head remote evidence; complete candidate-management release evidence, physical visual
  review, other clients, signing, rollback, and stable release remain open.

- 2026-07-20: Assumption: enabling fallback in configuration is not sufficient consent at the
  moment content may cross providers. Linux `af200122e4862f6230d89268f5292f16438449bb` adds a
  localized modal confirmation for ordinary text requests with fallback enabled; approval is
  one-shot and cancellation queues no worker command. Flatpak source pin `8dba6129f1706f9f450537477ef6d45ef6531d87`
  passed local metadata validation. Push Native/Flatpak/Foundation `29711055269`/`29711055278`/
  `29711055281` and PR `29711056550`/`29711056549`/`29711056544` all passed. Prompted Secret
  Service/portal unlock UI, human listening, translated-copy/visual review, other clients,
  signing, rollback, and stable release remain open.

- 2026-07-20: Assumption: the Linux host must reject a final profile-database path component
  replaced by a symbolic link during open, while the Core SQLite no-follow gate remains
  authoritative. Linux `651767d1493662f0631bf8e4245d0c525b684edc` adds `O_NOFOLLOW | O_CLOEXEC`
  to the final open and a regression that proves the symlink target is neither followed nor
  modified. Local format/check/Clippy/full-test/Flatpak/diff validation passed. Push
  Native/Flatpak/Foundation `29714091446`/`29714091453`/`29714091474` and PR
  `29714093213`/`29714093215`/`29714093207` all passed. Parent-directory replacement races still
  require a future directory-descriptor or `openat2` design; other clients, signing, rollback,
  and stable release remain open.

- 2026-07-20: Assumption: Linux profile storage must keep the validated database inode fixed
  through Core migration/open, not merely preflight a pathname. Core `b5febb8daec88ab0401af4d6ceb20ec848f65138`
  adds the narrowly validated `/proc/self/fd/<fd>` entry point; Linux `0479dbcc7e629d48f1d65002cfd2cb43439b77d5`
  pins the parent with `openat2(RESOLVE_NO_SYMLINKS)` and opens the final file with
  `O_NOFOLLOW | O_CLOEXEC`. The rename-and-symlink regression keeps migration in the pinned
  directory. Push Native/Flatpak/Foundation `29715772612`/`29715772573`/`29715772602` and PR
  `29715774034`/`29715774044`/`29715774031` all passed; Core CI/Native SDK
  `29714966974`/`29714966969` passed. The first code push's stale Flatpak pin failures
  `29715256438`/`29715257892` remain recorded as failures; prompted unlock UX, other clients,
  signing, rollback, and stable release remain open.

- 2026-07-20: Assumption: a read-only Linux profile database directory must fail closed for
  persistence while preserving session-only translation. Linux
  `06a9a76c8b964a9e0badc087b243a2fc4cd09544` adds
  `read_only_database_directory_reports_error_but_session_mode_still_works`, which uses a private
  `0500` directory, verifies typed persistence failure and no database creation, completes a
  session-only fake-provider translation, and rejects deletion. Local Linux format/check/Clippy/
  full-test and Flatpak metadata validation passed (`134 passed; 3 ignored`). Push
  Native/Flatpak/Foundation `29716832991`/`29716832970`/`29716832961` and PR
  Native/Flatpak/Foundation `29716835042`/`29716835044`/`29716835030` all passed, with jobs
  `88271663136`/`88271663160`/`88271663435` and `88271669287`/`88271669310`/`88271669196`.
  Power-loss and broader SQLite VFS behavior remain open.

- 2026-07-20: Assumption: persistent Secret Service failure must produce an explicit localized
  session-only recovery choice. Linux `7df461ec5e0d1cc5736e2c2edef48333fcf5ff14` adds the
  modal, disables Remember, focuses the credential field, and leaves Connect unsubmitted when
  closed. Local 134-test/3-ignored, formatting, strict Clippy, all-target, localization
  placeholder, Flatpak, and diff checks passed. The initial placeholder/pin failures
  `29717314361`/`29717314328`/`29717312990`/`29717312998` remain recorded; corrected Push
  `29717769144`/`29717769121`/`29717769119` and PR `29717770780`/`29717770833`/`29717770765`
  passed with jobs `88274285611`/`88274285568`/`88274285482` and
  `88274289941`/`88274290099`/`88274289936`. End-user prompt approval, other clients, visual
  review, artifacts, rollback, and stable release remain open.

- 2026-07-20: Assumption: Anthropic Messages model selection remains manual until a provider
  catalog service is intentionally introduced. Core `a87aaf2bef7cca287c4a6faa8addd340e0245b0e`
  adds the `anthropic_messages` adapter with bounded SSE, cancellation, protected-span restoration,
  typed errors, redacted diagnostics, and a pre-secret model-selection check. Core CI
  `29718737864` and Native SDK `29718737836` passed; the adapter is unreleased and Linux UI binding
  remains open.

- 2026-07-20: Linux `d15e915a516796b7565c34053b27a913c3a2aed4` pins that Core revision and refreshes
  the Flatpak source manifest. Local non-GTK validation passed; the host GTK test-link limitation is
  recorded explicitly. Final push/PR Native, Flatpak, and Foundation runs
  `29719373604`/`29719373628`/`29719373607` and `29719371860`/`29719371922`/`29719371859` passed.
  Prompted unlock approval, human review, other clients, signing, rollback, and stable release
  remain open.

- 2026-07-20: Assumption: Linux Anthropic Messages remains a manual-model provider until a catalog
  service is intentionally introduced. Linux `f41e14af53b6d2d70b0f1d452ea32eda10d63095` binds the
  localized Anthropic preset with HTTPS `/v1/`, saved-model restoration, focus/accessibility wiring,
  and pre-secret empty-model validation. l10n `e1ee15a5e9470e2c49077e52b4969597a5c8283f` contains
  393 messages and the generated Linux resources. Final push/PR Native/Flatpak/Foundation runs
  `29721751141`/`29721751155`/`29721751111` and `29721753040`/`29721753048`/`29721753045` all
  passed. The GTK test-link limitation, visual/copy review, prompt approval, other clients,
  signing, rollback, and stable release remain open.

- 2026-07-20: Assumption: GitHub review state must reflect the latest verified Linux evidence
  without implying merge or release readiness. Authenticated triage found only Linux PR #1 open
  (Draft/Open, mergeable, no reviews, no unresolved threads) and central Issue #1 open across the
  canonical repositories. The PR and issue bodies/comments now reference Linux `f41e14a`, Core
  `a87aaf2`, l10n `e1ee15a`, and coordination run `29722312762`; no stable release action was taken.

- 2026-07-20: Assumption: Core `7068b1d565177c7541c6d6a35f8d8e7475dd126e` is a test-only ABI
  hardening descendant, so the Linux production pin stays at `a87aaf2bef7cca287c4a6faa8addd340e0245b0e`.
  The concurrent C ABI control-call regression passed locally; Core CI `29723055135` and Native
  SDK `29723055154` passed all jobs. No workspace or release-manifest pin changed.

- 2026-07-20: Assumption: Linux queue selection is implemented, while concurrent document
  execution remains outside the validation gate. Linux `8167481cbdea` corrected the architecture
  boundary without changing runtime code or source pins. Existing queue selection and the full
  Linux local suite passed; push Native/Flatpak/Foundation `29723524259`/`29723524286`/`29723524238`
  and PR `29723526302`/`29723526314`/`29723526298` all passed. PR #1 remains Draft/Open and Issue
  #1 remains Open; no manifest pin or release status changed.

- 2026-07-20: Assumption: prompt fixtures prove Secret Service signal handling only; they do not
  stand in for real-user desktop approval. Linux `8eaf7435094c` documents approved and dismissed
  `CreateItem`/`Delete` cases, with the local four-case fixture passing. Push Native/Flatpak/
  Foundation `29724116604`/`29724116747`/`29724116697` and PR `29724118466`/`29724118446`/
  `29724118428` all passed. No source pin or release-manifest value changed.

- 2026-07-20: Assumption: the Native/Flatpak gates cover Linux queue listing, explicit selection,
  and sequential document execution, not concurrent document execution or stable readiness. Linux
  `01d7ba7` and the active plan now state that boundary accurately; no runtime code or manifest pin
  changed. Push Native/Flatpak/Foundation `29724628374`/`29724628347`/`29724628370` and PR
  `29724630281`/`29724630307`/`29724630279` all passed; the Linux PR/central issue remain
  Draft/Open and Open respectively.

- 2026-07-20: Assumption: routing-profile exchange files are portable non-secret metadata and must
  not silently replace saved IDs. Core `115535c76d804020f045708867af7798b8d0294a` adds the bounded
  JSON codec with unknown-field and 64 KiB rejection; l10n `026c35b8dbb1c13c22d77809cc5fe72e6af6f5a3`
  adds the GTK exchange strings; Linux `e6d87958ce13e8ccfb04a62c22b8bb5657bbb69e` adds worker
  commands, asynchronous GTK file chooser paths, and duplicate-ID rejection. Core CI/Native SDK
  `29753851712`/`29753851733`, l10n Localization/Foundation `29754460570`/`29754460635`, Linux
  push Native/Flatpak/Foundation `29755663043`/`29755662549`/`29755662552`, and Linux PR
  Native/Flatpak/Foundation `29755666246`/`29755666022`/`29755666120` all passed. PR #1 remains
  Draft/Open and Issue #1 remains Open; Android, Windows, macOS, signing, rollback, and stable
  release remain open.

- 2026-07-20: Assumption: the current Linux document-routing slice selects one saved
  document-capable candidate and reconnects its persisted non-secret profile ID after restart;
  document fallback and cross-client routing remain disabled. Existing Linux regressions
  `document_job_translation_uses_saved_routing_profile_without_fallback` and
  `document_job_resume_reconnects_saved_routing_profile_after_restart` passed at
  `e6d87958ce13e8ccfb04a62c22b8bb5657bbb69e`; current push/PR Native, Flatpak, and Foundation
  runs `29755663043`/`29755662549`/`29755662552` and `29755666246`/`29755666022`/`29755666120`
  passed. Central documentation now reflects this evidence without changing release status.

## Checkpoint update protocol

At every checkpoint, update this plan, `IMPLEMENTATION_STATUS.md`, relevant ADRs, `workspace-manifest.toml`, `release-manifest.toml`, and validation evidence. Record failures as failures, distinguish unavailable host builds from successful CI builds, and do not mark a milestone complete from partial or indirect evidence.

- 2026-07-22: Assumption: the Linux About surface should expose only localized, read-only app and
  shared-Core compatibility fields. Runtime/packaging `0d7b3927fb98e461317feaefeb4c806676e6acc0`,
  l10n `a65a327a8418332e50d9ab302fca24508e7266ef`, and final status head `b71e209` passed local
  checks and final push/PR Native, Flatpak, and Foundation gates
  `29939876568`/`29939877021`/`29939876501` and
  `29939879474`/`29939879969`/`29939879856`. The l10n-pin, mnemonic assertion, and stale Flatpak
  pin failures are retained as superseded evidence; PR #1 remains Draft/Open and release status
  stays `unreleased`.

- 2026-07-22: Assumption: Android can advance as a prerelease preparation slice without displacing
  the user's Linux-first priority. Android `afe7a566bac77a16243f70295d17a4d9cab1151f` pins Core
  `8837e59395742b5385af5037aa36a2596af3b025` and l10n `3724cc9d436ebdbac3b8ebf0df9bce9af1b41b15`.
  Workflow `29932649692` (job `88966082464`) passed clean AAR provenance checks, debug/release
  builds, 16 JVM tests per variant, instrumentation compilation, and lint; status-head rerun
  `29933216517` (job `88968007647`) also passed. Device execution,
  provider credentials, document/history/routing/background flows, signing, and stable release
  remain open; the first metadata assertion failure `29931908407` is retained as superseded evidence.

- 2026-07-22: GitHub triage found no actionable reviews or unresolved threads on Linux PR #1 or
  macOS PR #1. Linux's six current-head gates and macOS foundation/Native run `29765906044` pass;
  both remain Draft/Open. Central Issue #1 remains Open for device/manual review, signing,
  rollback, cross-client, and stable-release boundaries. Triage comments were recorded on the
  macOS PR and central issue; no merge or stable-release action was taken.
