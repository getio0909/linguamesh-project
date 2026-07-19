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
- [ ] Continue through Milestones 2–8 and all 20 mandatory acceptance scenarios.

## Active Linux-first checkpoint — approved text fallback routing

Change identifier: `LM-CHANGE-2026-07-LINUX-FALLBACK-1`

The Linux client is the only platform in scope for this checkpoint. Fallback is opt-in, limited to
ordinary text requests, and requires a different saved provider selected from the UI. A retryable
network or timeout failure may switch once; the decision is surfaced without exposing endpoints or
content, partial primary output is preserved, and cancellation or non-retryable errors terminate
without trying another provider.

Assumption: a single selected saved profile is the smallest complete approved chain for Scenario 7;
ordered multi-provider chains and automatic routing remain future work.

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

Assumption: schema-6 document recovery stores only an opaque job ID, source basename, format,
ordered bounded segments, and lifecycle state. Pending/running jobs are restored on Linux worker
startup; the Linux GTK queue now presents those bounded snapshots, while archive codecs remain future
work.

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

## Checkpoint update protocol

At every checkpoint, update this plan, `IMPLEMENTATION_STATUS.md`, relevant ADRs, `workspace-manifest.toml`, `release-manifest.toml`, and validation evidence. Record failures as failures, distinguish unavailable host builds from successful CI builds, and do not mark a milestone complete from partial or indirect evidence.
