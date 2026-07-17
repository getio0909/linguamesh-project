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
- Baseline Linux GTK accessibility semantics on GTK 4.10+: named roles and editors, label
  mnemonics and `LabelledBy` relations, focusable controls/actions, hidden empty errors, and
  Busy/reset state handling. AT-SPI/Orca and physical-keyboard coverage remain unverified.
- Linux GIO D-Bus Secret Service adapter for persistent SecretRef create/update/resolve/delete
  paths, with unavailable, locked, or interactive keyrings failing closed and an explicitly
  labeled session-only fallback. Native CI records the integration boundary; real desktop keyring
  CRUD, cleanup, and secure persistent-credential onboarding remain open.
- Linux runtime PO catalog loading for English and Simplified Chinese action labels. Locale changes
  update Translate and Stop without losing active text; uncovered UI strings retain explicit English
  fallback while complete gettext coverage remains open.
- Linux completion notifications now use the registered `GApplication` path with fixed generic text;
  source and translated content are excluded from notification payloads, while desktop delivery
  and packaging remain release-gate work.
- Linux now offers bounded native TXT/Markdown import through GTK `FileDialog` and asynchronous GIO
  reads, with UTF-8/BOM validation and a 4 MiB limit; a single GIO file can also be dropped onto
  the source editor through the same validation path, while portal leases remain open.
- Central release and compatibility records now pin the verified Linux source-drop checkpoint and
  retain unreleased status with empty artifact lists; coordination validation passed on Linux and
  Windows PowerShell.
- Linux Secret Service session setup now uses the required single-layer plain-string Variant;
  the wire-shape regression is covered while real desktop keyring lifecycle evidence remains open.
- Central compatibility and release records now pin the Secret Service wire-fix checkpoint and
  retain unreleased status with empty artifact lists; Linux and Windows PowerShell coordination
  validation passed.

### Fixed

- Linux persistent Connect, model-update, and profile-deletion transactions now reject real
  post-startup `ENOSPC` failures before success, degrade the active connection to session-only,
  preserve the prior validated engine/model, and restore only pre-fault state after restart.
