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
- [ ] Resolve the GitHub owner and audit all canonical local and remote repository names.
- [ ] Record host toolchains and unavailable-platform constraints.
- [ ] Complete Checkpoint 0 and publish verified repository foundations.
- [ ] Complete Checkpoint 1 and publish the verified Rust CLI vertical slice.
- [ ] Continue through Milestones 2–8 and all 20 mandatory acceptance scenarios.

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

## Checkpoint update protocol

At every checkpoint, update this plan, `IMPLEMENTATION_STATUS.md`, relevant ADRs, `workspace-manifest.toml`, `release-manifest.toml`, and validation evidence. Record failures as failures, distinguish unavailable host builds from successful CI builds, and do not mark a milestone complete from partial or indirect evidence.
