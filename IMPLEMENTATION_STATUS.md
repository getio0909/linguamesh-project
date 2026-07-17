# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

Milestone 0, the first Rust core/CLI checkpoint, and localization development bundle `0.1.0` are implemented, committed, locally validated, published to the canonical public repositories owned by `getio0909`, and verified by GitHub Actions. No stable product release, completed native client, released SDK artifact, or supported document codec is claimed here.

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
| Rust core checkpoint | Validated locally | Core revision `e5fb2311b3e699db83084ce96240b79d482ad896` passed rustfmt, strict Clippy, 18 tests, locked build, cargo-deny policy, credential-signature scan, and workflow YAML parsing. |
| Localization bundle | Validated locally and remotely | l10n revision `4b36889116eba037721cb31827342409e8836168` contains 41 canonical messages, 12 official locale packs, two pseudo-locales, 45 generated artifacts, 25 passing tests, platform-format checks, and deterministic bundle SHA-256 `47bc84bd7562fb6ada7f88fd07490e79843c5c4e9d9b747f87a206dbecd0394a`. Non-English packs remain explicitly unreviewed drafts. |
| GitHub Actions | Passed | Core run `29551581397` passed. Central runs `29551747796` and `29552361617` passed Linux and Windows validation. l10n runs `29553012283` and `29553012269` passed; the downloaded CI bundle passed its embedded checksum and matched the local reproducible hash. Initial foundation runs passed for Android (`29551588891`), Windows (`29551592425`), macOS (`29551595832`), and Linux (`29551599044`). |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not started | Scenarios 2–20 do not yet have reproducible passing evidence. |

## Validation limitations

PowerShell validation was not executed locally because `pwsh` is unavailable on this Linux host; central GitHub Actions run `29551747796` executed it successfully on Windows. Full third-party JSON Schema validation was not run locally because the Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator independently checked the manifest's required repository, component, version, status, source, checksum, owner, and remote invariants.

## Release posture

`release-manifest.toml` is deliberately `unreleased`. It records the locally verified core source revision and development contract versions, while all artifacts remain empty because no release artifacts exist. Publishing a stable release is prohibited until compatibility and all required acceptance evidence are recorded.
