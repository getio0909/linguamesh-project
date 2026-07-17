# Secure Coding Checklist

Use this checklist in implementation and review:

- [ ] Secrets are represented by `SecretRef`, resolved just in time, zeroized where practical, and absent from logs, errors, databases, fixtures, and diagnostics.
- [ ] Remote transport uses HTTPS, validates TLS, bounds redirects and sizes, and drops authorization on origin change.
- [ ] Cancellation reaches transport and parsing work without retries or duplicate terminal events.
- [ ] Provider, model, protocol, locale, catalog, and document data is decoded defensively with explicit limits.
- [ ] Archives reject traversal, absolute paths, bombs, excessive entries, and unsafe extraction targets; XML external entities are disabled.
- [ ] Temporary files are private, leased, cleaned, and never replace the source by default.
- [ ] FFI validates pointers, lengths, versions, ownership, panic containment, shutdown, and concurrency.
- [ ] Routing and fallback expose the receiving provider and require the applicable consent.
- [ ] CI with untrusted changes has no production credentials or privileged release permissions.
- [ ] Dependencies and assets have maintenance, vulnerability, provenance, and license review.
- [ ] Tests include adversarial fixtures, redaction assertions, and safe failure paths.

