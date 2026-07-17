# Contributing

## Start with repository scope

Read `AGENTS.md`, `REPOSITORY_ROLE.md`, `PROJECT_GOAL.md`, `PLANS.md`, and `IMPLEMENTATION_STATUS.md`. Put shared behavior in `linguamesh-core`, canonical UI messages in `linguamesh-l10n`, native UI in its platform repository, and cross-repository policy here.

Use an ExecPlan for multi-stage or compatibility-sensitive work. Record uncertain but reversible choices as `Assumption:` and capture durable architecture decisions in `docs/adr/`.

## Local checks

```sh
tools/check-workspace.sh
tools/check-workspace.sh --require-repositories
git diff --check
```

PowerShell contributors can run `./tools/check-workspace.ps1`. Repository-specific format, lint, test, and build commands remain mandatory for code changes. Default tests must not require commercial credentials.

## Changes and reviews

Keep commits focused and use an imperative subject with an optional scope, for example `docs: define ABI compatibility`. A pull request must describe scope, affected repositories, compatibility and privacy impact, linked issue/RFC/ADR, rollback approach, and exact validation evidence. Include screenshots for user-visible client changes and note unavailable platform builds honestly.

Do not commit credentials, translation content, local `.codex` state, generated secrets, or unreviewed third-party code. New production dependencies require maintenance and license review.

By participating, contributors agree to follow [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

