# Implementation Status

Last updated: 2026-07-17

## Current checkpoint

The central-repository portion of Milestone 0 and the first Rust core/CLI checkpoint are implemented, locally committed, and locally validated. Every canonical sibling repository has a verified foundation commit. No remote repository, GitHub Actions run, stable product release, native client, SDK artifact, or supported document codec is claimed here.

## Evidence

| Area | Status | Evidence |
| --- | --- | --- |
| Authoritative goal and plan | Present | `PROJECT_GOAL.md`, `AGENTS.md`, and `PLANS.md` were read before implementation. |
| Central policies and documentation | Validated locally | `bash tools/check-workspace.sh` passed required-file and Markdown-link checks. |
| Workspace and release manifests | Validated locally | Default and strict Bash checks parsed both TOML files, enforced the canonical set and release invariants, parsed the JSON schema, and passed. |
| Workspace automation | Bash validated | `bash -n tools/bootstrap.sh tools/check-workspace.sh` and `bash tools/bootstrap.sh --check-only` passed. The check-only run preserved all seven existing directories. |
| GitHub metadata | Syntax validated | The repository Python 3.13 environment parsed all workflow and issue-template YAML files successfully. No remote operation was performed. |
| Canonical sibling repositories | Layout validated | `bash tools/check-workspace.sh --require-repositories` found all seven canonical directories and their minimum policy files. This does not verify sibling application behavior. |
| Rust core checkpoint | Validated locally | Core revision `e5fb2311b3e699db83084ce96240b79d482ad896` passed rustfmt, strict Clippy, 18 tests, locked build, cargo-deny policy, credential-signature scan, and workflow YAML parsing. |
| Acceptance Scenario 1 | Passed locally | The reference CLI discovered and selected a fake model, streamed `你好，LinguaMesh！` over loopback HTTP/SSE, and completed without a key. A separate slow-stream run retained `你好` and emitted cancellation. |
| Remaining acceptance scenarios | Not started | Scenarios 2–20 do not yet have reproducible passing evidence. |

## Validation limitations

PowerShell validation was not executed because `pwsh` is unavailable on this Linux host; the Windows GitHub Actions job is configured to run it. Full third-party JSON Schema validation was not run because the local Python environment lacks `jsonschema`; the schema parsed as JSON and the Bash validator independently checked the manifest's required repository, component, version, status, source, and checksum invariants. GitHub owner resolution, remote creation, push, and Actions execution are blocked by the absence of an authenticated `gh` host or runtime token.

## Release posture

`release-manifest.toml` is deliberately `unreleased`. It records the locally verified core source revision and development contract versions, while all artifacts remain empty because no release artifacts exist. Publishing a stable release is prohibited until compatibility and all required acceptance evidence are recorded.
