# Detailed Privacy Model

## Data categories

- User content: source text, documents, translations, glossaries, and context.
- Credentials: API keys and secret custom headers.
- Operational metadata: provider/model IDs, routing decisions, usage, errors, job state, and timestamps.
- Local preferences: locale, theme, window state, and accessibility settings.

## Processing and retention

User content is processed locally except when deliberately sent to the displayed provider. History and translation memory are optional local features. Incognito mode persists neither input nor output content. Document job metadata retains only what resume requires and is user-deletable. Diagnostics exclude credentials and unnecessary content.

Credentials remain in platform secure storage and enter core memory only after a scoped request. They are never serialized. If secure persistence is unavailable, the client offers an explicit memory-only session with a warning.

## User control

Users can choose local-only routing, disable history and memory, clear each data class, remove providers, delete job metadata and temporary files, export non-secret settings, and reset local data. Remote fallback and multi-call quality modes require understandable consent.

## Data-flow review

Each feature review records the source, destination, purpose, retention, deletion path, provider identity, failure behavior, and whether data can cross a new trust boundary. No telemetry or hosted service is assumed.

