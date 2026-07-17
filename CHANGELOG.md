# Changelog

All notable project-wide changes will be documented here. This project follows semantic versioning once versioned releases begin.

## Unreleased

### Added

- Central repository policies, architecture records, manifests, workspace automation, contribution templates, and validation CI for the initial local foundation.
- Local foundations for every canonical repository and the first verified Rust core/CLI streaming checkpoint, including cancellation, protocol/ABI foundations, SQLite migrations, provider catalog validation, and local fake-provider tests.
- Canonical localization `0.1.0` development data, deterministic Android, Windows, macOS, and Linux resources, pseudo-locales, validation, and CI bundle evidence.
- Core and Linux `0.1.0-alpha.2` source checkpoints for canonical provider profiles, typed
  host-secret brokerage, one-shot session credentials, explicit provider/model selection,
  cancellation, atomic provider-switch rollback, and native GTK/D-Bus/Xvfb CI evidence.
- Core Linux default-VFS SQLite no-follow hardening and Linux explicit credential-free
  multi-profile create/update/activate/switch/delete, disconnected full-list/default restart
  restoration, per-profile models, connected-row session continuation, private XDG storage,
  unsafe-path rejection, credential isolation, and persistence rollback evidence. Credentials
  remain session-only, and persistent secret references fail closed.
- Linux derived provider setup through Ready/Unavailable, stable next-request provider/model
  identity, persistent session-only degradation warnings, worker-loss command blocking, and
  authenticated A/B request-counter evidence for remembered model switching. Secret Service and
  secure persistent-credential onboarding remain unimplemented.

### Fixed

- Linux persistent Connect, model-update, and profile-deletion transactions now reject real
  post-startup `ENOSPC` failures before success, degrade the active connection to session-only,
  preserve the prior validated engine/model, and restore only pre-fault state after restart.
