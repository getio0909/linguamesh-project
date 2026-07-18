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

## Progress

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
  state during action-label changes, and apply Arabic RTL root direction; complete visible-string
  gettext coverage remains a later Linux slice.
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
- [ ] Continue through Milestones 2–8 and all 20 mandatory acceptance scenarios.

## Active Linux-first checkpoint — secure provider foundation

Change identifier: `LM-CHANGE-2026-07-LINUX-SECURE-PROVIDER-1`

The user's latest explicit priority is Linux. Android, Windows, and macOS implementation work is
frozen for this checkpoint. Shared Core changes are in scope only when the Linux client cannot
correctly own the behavior itself.

Assumption: adding dependencies between existing first-party LinguaMesh workspace crates is a
contract change, not a new third-party production dependency. No new third-party dependency will
be added without a separate maintenance, security, and license review.

Assumption: the existing untracked central RFC and ADR drafts are unrelated user work and must
remain untouched unless their owner explicitly incorporates them into this checkpoint.

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

## Checkpoint update protocol

At every checkpoint, update this plan, `IMPLEMENTATION_STATUS.md`, relevant ADRs, `workspace-manifest.toml`, `release-manifest.toml`, and validation evidence. Record failures as failures, distinguish unavailable host builds from successful CI builds, and do not mark a milestone complete from partial or indirect evidence.
