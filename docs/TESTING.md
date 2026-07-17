# Testing and Validation

## Central repository

Run both implementations when their shells are available:

```sh
tools/check-workspace.sh
tools/check-workspace.sh --require-repositories
git diff --check
```

```powershell
./tools/check-workspace.ps1
./tools/check-workspace.ps1 -RequireRepositories
```

The central checker validates required files and directories, the exact canonical repository set, release components and unreleased/stable invariants, release-manifest schema presence, Markdown links, `.codex/` exclusion, and common credential signatures. Strict mode also requires every sibling directory and its minimum policy files.

## Cross-repository evidence

Every code repository owns format, lint, unit, integration, security, packaging, and platform commands. Default CI uses a local fake provider and no paid credentials. A release record must cite exact commands, runner platform, revision, result, and artifact checksum. Unsupported host builds must be identified as unavailable, not passed.

Cross-repository conformance runs the same fake-provider scenarios against pinned SDK/client versions. Tests and checkboxes count only when their scope covers the claimed behavior.

The scheduled and manually dispatched `cross-repository.yml` workflow clones public canonical siblings using the runtime repository owner and runs strict validation. It has read-only contents permission and is not triggered by untrusted pull requests.
