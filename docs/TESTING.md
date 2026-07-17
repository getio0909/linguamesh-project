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

Linux functional revision `d6bd2bd06ccdf04f3aead0c7f1da5ba74f84c550` passed 66 ordinary library
tests, the same real GTK binary flow under X11/Xvfb and forced Wayland/headless Weston, the native
build, an exact real-`ENOSPC` regression, and baseline GTK accessibility assertions in Native Linux
run `29589043315` (job `87913221576`).
The dedicated test passed once with zero ignored tests through Ubuntu's controlled mount fallback.
Evidence head `07d0b4daddf04d369768893a531276d507292356` reran the same gates in Native Linux run
`29589332282` (job `87914189125`); repository-foundation run `29589332132` also passed. The GTK
assertions cover roles, named multi-line editors, visible-label relations and mnemonics, focusability,
hidden empty errors, and Busy/reset semantics using GTK 4.10 APIs. This is transaction, protocol,
backend, and semantic-widget evidence for the current slice, not evidence for every storage fault,
AT-SPI/Orca, physical keyboard traversal, a physical compositor, GPU rendering, packaging, or a
complete desktop matrix.

The scheduled and manually dispatched `cross-repository.yml` workflow clones public canonical siblings using the runtime repository owner and runs strict validation. It has read-only contents permission and is not triggered by untrusted pull requests.
