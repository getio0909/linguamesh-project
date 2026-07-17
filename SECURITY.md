# Security Policy

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability. Use GitHub's private vulnerability-reporting feature for the affected canonical repository. If private reporting is unavailable, contact the maintainers through a private channel listed on the repository owner's profile and disclose only enough information to establish contact.

Include the affected repository and revision, impact, reproducible steps, and any proposed mitigation. Do not include real API keys, source documents, user content, or unrelated personal data. Maintainers should acknowledge a report within seven days and coordinate disclosure after a fix is available.

## Security boundaries

- Credentials belong in platform secure storage; the Rust core persists only `SecretRef` identifiers.
- Remote endpoints must use HTTPS. Plain HTTP is limited to loopback unless the user explicitly accepts the risk.
- Authorization must never follow an origin-changing redirect.
- Provider input, model output, documents, locale packs, catalogs, and protocol messages are untrusted.
- Logs, diagnostics, crash reports, tests, and fixtures must not contain credentials or unnecessary translation content.
- Default CI must not use paid-provider credentials or expose privileged secrets to forked pull requests.

See [`docs/security/threat-model.md`](docs/security/threat-model.md), [`docs/security/secure-coding-checklist.md`](docs/security/secure-coding-checklist.md), and [`PRIVACY.md`](PRIVACY.md).

## Supported versions

No stable release exists yet. Security fixes target the latest prerelease line recorded in `release-manifest.toml`; support policy will be versioned before 1.0.
