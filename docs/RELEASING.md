# Release Process

1. Open or update a release-train record under `docs/releases/` and keep status `draft` or `prerelease`.
2. Pin exact source revisions and contract versions. Build from clean, reviewed revisions using documented toolchains.
3. Run repository tests, platform packaging checks, ABI/protocol conformance, localization validation, security scans, license review, and applicable acceptance scenarios.
4. Generate SHA-256 checksums, provenance, SBOMs where practical, third-party notices, and signing/notarization evidence. Clearly label unsigned artifacts.
5. Update clients to the verified core artifacts and run the cross-repository suite.
6. Update `COMPATIBILITY.md`, `release-manifest.toml`, its schema validation, the release record, changelogs, implementation status, limitations, migration, and rollback guidance in one coordinated change.
7. Publish only with explicit authorization. Never expose credentials, publish a draft as stable, or claim signing and platform tests without evidence.
8. Verify public artifact checksums, repository tags, default branches, release notes, and rollback references after publication.

A stable train requires all mandatory acceptance scenarios and compatible stable versions of core, localization, Android, Windows, macOS, and Linux.
