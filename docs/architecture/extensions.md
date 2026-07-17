# Extension Guides

## Add a provider preset

Add data to the core catalog using a stable preset ID, schema version, endpoint template, authentication fields, adapter type, discovery strategy, safe headers, capability hints, and official documentation link. Include schema, migration, no-secret, and non-overwrite tests. Review names and assets for trademark and license compliance.

## Add a provider adapter

Implement a protocol family behind the abstract transport and normalized domain interfaces. Cover request construction, incremental decoding, split UTF-8, malformed responses, size/time limits, cancellation, retries, redirects, typed errors, usage, and the local fake-provider contract. Do not add provider HTTP behavior to a native client.

## Add a document codec

Implement inspect, extract, reconstruct, and validate independently of inference. Define parser limits and fidelity limitations. Add redistributable fixtures for ordering, source preservation, cancellation, restart recovery, malformed input, traversal, resource exhaustion, output collision, and structural validation. Advertise support only after the native workflow uses the completed codec.

## Add a locale

Contribute data-only messages in `linguamesh-l10n` with a BCP 47 tag, direction, plural rules, descriptions, typed placeholders, source revision, and compatibility metadata. Generate and validate Android, Windows, macOS, and Linux resources; test fallback, runtime switching, RTL where applicable, pseudo-localization, formatting, and accessibility. Machine-generated drafts must be labeled and never described as reviewed.
