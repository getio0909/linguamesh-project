# Data-Flow Diagram

```text
user
  | source, options, file grants
  v
native client -----------------------> platform secure storage
  | command and FileLease                    | scoped secret
  v                                          v
shared Rust core <-------------------- host-service response
  |   |              |
  |   |              +--> local SQLite metadata and optional history/memory
  |   +-----------------> private temporary files and validated output
  +---------------------> selected local or remote provider
                               |
                               +--> streamed untrusted response to core
```

Before transmission, the client displays the selected provider and model. The core constructs a delimited request, obtains only the required credential, sends content directly to that provider, validates streamed output, and emits bounded typed events. Automatic remote fallback follows only a user-approved chain.

Documents enter through a platform-granted lease. Extraction and reconstruction remain local; only eligible segment content and approved context reach the provider. Output is built at a temporary destination, structurally validated, and finalized under a collision-safe name without replacing the source.

Logs, diagnostics, release metadata, and default telemetry receive neither credential values nor unnecessary content. Incognito mode bypasses history and translation-memory persistence.

