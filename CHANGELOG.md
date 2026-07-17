# Changelog

All notable project-wide changes will be documented here. This project follows semantic versioning once versioned releases begin.

## Unreleased

### Added

- Central repository policies, architecture records, manifests, workspace automation, contribution templates, and validation CI for the initial local foundation.
- Local foundations for every canonical repository and the first verified Rust core/CLI streaming checkpoint, including cancellation, protocol/ABI foundations, SQLite migrations, provider catalog validation, and local fake-provider tests.
- Canonical localization `0.1.0` development data, deterministic Android, Windows, macOS, and Linux resources, pseudo-locales, validation, and CI bundle evidence.
- Core and Linux `0.1.0-alpha.2` source checkpoints for canonical provider profiles, typed
  host-secret brokerage, one-shot session credentials, explicit provider/model selection,
  cancellation, atomic provider-switch rollback, and native GTK/D-Bus/Xvfb CI evidence. Persistent
  Secret Service storage remains unimplemented and fails closed.
