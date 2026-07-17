# Provider Architecture

Provider behavior lives behind core-owned protocol adapters and an abstract cancellable HTTP transport. Domain and UI code depend on normalized capabilities, models, events, usage, and typed errors rather than vendor response shapes.

A `ProviderProfile` contains endpoint configuration, adapter type, non-secret headers, timeouts, model sources, and `SecretRef` identifiers. It never contains a credential value. The native host resolves a requested secret from platform secure storage for one intended operation; the core clears it as soon as practical.

The versioned provider catalog supplies schema-validated presets without secrets. It cannot silently change the active provider, model, endpoint, headers, routing, or TLS policy. Models retain their source: discovered, catalog, or manual. Discovery failure never deletes manual configuration.

Routing modes are manual, ordered, or opt-in automatic. Decisions record eligible and rejected candidates, reasons, ranking inputs, selection, and approved fallback order. Remote fallback is off by default for sensitive content and documents. Cancellation never triggers retry.

Remote endpoints require HTTPS. Loopback HTTP is permitted for local models; other plaintext endpoints require a warning and explicit confirmation. Authorization is never forwarded across an origin-changing redirect, and TLS verification cannot be globally disabled.

To add a preset or adapter, follow [`extensions.md`](extensions.md) and include schema, contract, error, streaming, cancellation, security, attribution, and fake-provider tests.
