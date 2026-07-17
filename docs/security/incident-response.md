# Incident Response

1. Receive reports through the private process in `SECURITY.md`; avoid copying secrets or user content into issues.
2. Confirm scope, affected versions and repositories, exploitability, and whether release or provider communication must pause.
3. Contain exposure without destructive history rewriting. Revoke compromised external credentials only with authorized owner action.
4. Develop and test the smallest complete fix, including regression, redaction, migration, and compatibility coverage.
5. Coordinate patched versions across the release manifest, native clients, notices, checksums, and rollback guidance.
6. Publish an advisory only after affected maintainers agree on disclosure timing. Credit reporters who consent.
7. Record a content-free post-incident review covering cause, detection gap, corrective controls, and follow-up owners.

Never claim a credential was rotated, an artifact withdrawn, or a user notified without direct evidence.

