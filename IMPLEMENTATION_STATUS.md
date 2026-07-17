# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, Core `0.1.0-alpha.2`, localization development bundle `0.1.0`, and the Linux
`0.1.0-alpha.2` session-secret vertical slice are implemented, committed, published to the
canonical public repositories owned by `getio0909`, and verified by applicable local and GitHub
Actions gates. The active Linux secure-provider checkpoint remains incomplete because native
Secret Service persistence, saved profiles, and restart restoration are not implemented. No stable
product release, completed native client, released SDK artifact, or supported document codec is
claimed here.

## Evidence

| Area | Status | Evidence |
| --- | --- | --- |
| Authoritative goal and plan | Present | `PROJECT_GOAL.md`, `AGENTS.md`, and `PLANS.md` were read before implementation. |
| Central policies and documentation | Validated locally | `bash tools/check-workspace.sh` passed required-file and Markdown-link checks. |
| Workspace and release manifests | Validated locally | Default and strict Bash checks parsed both TOML files, enforced the canonical set and release invariants, parsed the JSON schema, and passed. |
| Workspace automation | Bash validated | `bash -n tools/bootstrap.sh tools/check-workspace.sh` and `bash tools/bootstrap.sh --check-only` passed. The check-only run preserved all seven existing directories. |
| GitHub repositories | Published and verified | All seven repositories are public, use `main` as the default branch, have Issues and Actions enabled, have Wiki disabled, and initially matched their local committed HEAD. Canonical remotes are recorded in `workspace-manifest.toml`. |
| GitHub metadata | Validated | The repository Python 3.13 environment parsed all workflow and issue-template YAML files successfully; remote run evidence is listed below. |
| Canonical sibling repositories | Layout validated | `bash tools/check-workspace.sh --require-repositories` found all seven canonical directories and their minimum policy files. This does not verify sibling application behavior. |
| Rust core checkpoint | Validated locally and remotely | Functional revision `c9a96da52e10554c8458f4d49600ec9336ea651b` advances the workspace to `0.1.0-alpha.2` and uses ABI 1 and protocol 1. It passed rustfmt, strict Clippy, 56 tests, locked build, cargo-deny policy, native SDK checks, credential scans, and CI. Canonical profiles, SQLite schema 2 migration, and the bounded typed host-secret broker are implemented without credential-value persistence. |
| Localization bundle | Validated locally and remotely | l10n revision `4b36889116eba037721cb31827342409e8836168` contains 41 canonical messages, 12 official locale packs, two pseudo-locales, 45 generated artifacts, 25 passing tests, platform-format checks, and deterministic bundle SHA-256 `47bc84bd7562fb6ada7f88fd07490e79843c5c4e9d9b747f87a206dbecd0394a`. Non-English packs remain explicitly unreviewed drafts. |
| Native Linux alpha.2 slice | Validated locally and remotely | Functional revision `0455baf8f258c6280d66d1d568fd6a01fdad8486` starts disconnected, requires explicit connection and model selection, resolves one-shot session secrets through Core, streams and cancels real loopback HTTP/SSE work, preserves a working provider after failed switching, and fails closed for persistent secrets. Local toolkit-independent suites passed 23 and 35 tests. Native Ubuntu CI passed 35 library tests plus the real GTK button test and all-feature build under D-Bus/Xvfb. |
| GitHub Actions | Passed | Core run `29564543164` and Native SDK run `29564543160` passed for the alpha.2 functional Core source, including Linux SDK job `87834118139`. Linux foundation run `29569227294` (job `87848829297`) and Native Linux run `29569227256` (job `87848829235`) passed for the functional client source. Central runs `29551747796` and `29552361617` passed Linux and Windows validation; prior repository and localization evidence remains recorded in the component status files. |
| Documentation-only repository heads | Passed | Core head `418fd48e5f64e6758947dda8e33306db887bc978` differs from its functional source only in `IMPLEMENTATION_STATUS.md`; Core run `29564807329` and Native SDK run `29564807242` passed. Linux head `c9e9a95ea96eafa3ed1929d12511b7971bd051b7` has the same one-file relationship; foundation run `29569388826` (job `87849343236`) and Native Linux run `29569388657` (job `87849342648`) passed. The release manifest intentionally pins the functional revisions. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not passed | Scenarios 2–20 do not yet have complete reproducible passing evidence. The Linux alpha.2 slice is partial implementation evidence and does not complete Scenario 3 or the secure-provider checkpoint. |

## Validation limitations

PowerShell validation was not executed locally because `pwsh` is unavailable on this Linux host;
central GitHub Actions run `29551747796` executed it successfully on Windows. Native GTK headers
are also unavailable locally; Linux run `29569227256` supplies the native compile, link, X11,
D-Bus, and GTK test evidence. Full third-party JSON Schema validation was not run locally because
the Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator
independently checked the manifest's required repository, component, version, status, source,
checksum, owner, and remote invariants. Native Secret Service, restart restoration, packaging,
accessibility, Wayland, and third-party local-server interoperability remain unverified.

## Release posture

`release-manifest.toml` remains deliberately `unreleased`. It records the exact functional Core
and Linux alpha.2 source revisions, ABI 1, protocol schema `0.1.0`, and the current catalog and
localization contracts. Every artifact list remains empty because these workflow results are
evidence, not published releases. Publishing a stable release is prohibited until secure profile
persistence, compatible stable components, checksummed artifacts, and all required acceptance
evidence are recorded.
