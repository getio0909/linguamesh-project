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
- [ ] Complete the active Linux-first secure-provider checkpoint described below.
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
6. integrate the reviewed Core revision into Linux, resolve persistent credentials through Secret
   Service, offer an explicitly labeled in-memory session fallback when secure storage is
   unavailable, and never fall back to plaintext;
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
- [x] Linux functional revision `c58a54c2479045773358bd9c456b45a958e98e1e` passed 29 no-default
  tests, 50 demo-provider tests, strict all-feature Clippy, the real GTK test, and the native
  all-target build in Native Linux run `29574265570`.
- [ ] Implement and review a native Secret Service backend before accepting persistent credential
  references.
- [ ] Implement onboarding, create/update/delete, and active switching for multiple saved profiles.
- [x] Persist a non-secret profile/model preference, restore it after restart without
  auto-connection, and verify switching, cancellation rollback, path hardening, and redacted
  diagnostics in native CI.

This checkpoint may remain prerelease. It does not authorize a stable release or a claim that the
complete Provider Hub, all provider protocols, or every Linux milestone is finished.

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

## Checkpoint update protocol

At every checkpoint, update this plan, `IMPLEMENTATION_STATUS.md`, relevant ADRs, `workspace-manifest.toml`, `release-manifest.toml`, and validation evidence. Record failures as failures, distinguish unavailable host builds from successful CI builds, and do not mark a milestone complete from partial or indirect evidence.
