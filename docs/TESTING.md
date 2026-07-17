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

Linux functional revision `c37702c76c3b1a2f9cec805cf9e219721ef7b5ce` passed 66 ordinary library
tests, the same real GTK binary flow under X11/Xvfb and forced Wayland/headless Weston, the native
build, and an exact real-`ENOSPC` regression in Native Linux run `29586532049` (job `87904787338`).
The dedicated test passed once with zero ignored tests through Ubuntu's controlled mount fallback.
Evidence head `2eadf06e5e63eec5b7a512a53a2741f4f2c77704` reran the same gates in Native Linux run
`29586802067` (job `87905686187`); repository-foundation run `29586802183` (job `87905686613`) also
passed. This is transaction and protocol/backend evidence for the current slice, not evidence for
every storage fault, a physical compositor, GPU rendering, accessibility, packaging, or a complete
desktop matrix.

The scheduled and manually dispatched `cross-repository.yml` workflow clones public canonical siblings using the runtime repository owner and runs strict validation. It has read-only contents permission and is not triggered by untrusted pull requests.
