# Privacy Model

LinguaMesh is designed for bring-your-own-key, direct-to-provider operation. It has no required account, hosted relay, cloud synchronization, or telemetry. Telemetry is off by default.

## Data flow

Source content is sent only to the provider and model shown before transmission. Automatic routing is opt-in, and remote fallback requires explicit user permission. Local loopback providers can be used without transmitting content to a remote service. Provider privacy terms remain the user's responsibility.

## Local data

The shared core may store non-secret settings, provider profile metadata, job state, history, translation memory, and usage records in SQLite. Users must be able to disable history, use incognito mode, delete local records, and clear temporary files. Incognito operations must not persist source text, output text, history, or translation-memory entries.

Credentials are resolved just in time from Android Keystore-backed storage, Windows credential protection, macOS Keychain, or Linux Secret Service. If secure persistence is unavailable, only an explicit session-only option is allowed. Credential values must never enter SQLite, logs, diagnostics, release manifests, or crash reports.

Document inputs remain unchanged by default. Outputs are finalized under a distinct name only after reconstruction and validation. Temporary resources must be private, bounded, and cleaned after success, failure, or cancellation.

See [`docs/security/privacy-model.md`](docs/security/privacy-model.md) for trust boundaries and retention controls.

