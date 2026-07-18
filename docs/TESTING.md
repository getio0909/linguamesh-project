# Testing and Validation

## Central repository

Run both implementations when their shells are available:

```sh
tools/check-workspace.sh
tools/check-workspace.sh --require-repositories
git diff --check
```

```powershell
./tools/check-workspace.ps1
./tools/check-workspace.ps1 -RequireRepositories
```

The central checker validates required files and directories, the exact canonical repository set, release components and unreleased/stable invariants, release-manifest schema presence, Markdown links, `.codex/` exclusion, and common credential signatures. Strict mode also requires every sibling directory and its minimum policy files.

## Cross-repository evidence

Every code repository owns format, lint, unit, integration, security, packaging, and platform commands. Default CI uses a local fake provider and no paid credentials. A release record must cite exact commands, runner platform, revision, result, and artifact checksum. Unsupported host builds must be identified as unavailable, not passed.

Cross-repository conformance runs the same fake-provider scenarios against pinned SDK/client versions. Tests and checkboxes count only when their scope covers the claimed behavior.

The current Linux-first history slice is pinned to Core `8cd65c5846a677e70c4828e4b4a5192319d775d5`,
l10n `4678fc3810b1e21e5ab8c1095e552930b8649687`, and Linux `dbec42349b4bebc57f56f8e63d2391c4e2318b0a`.
Core CI `29636624648` and Native SDK `29636624656` passed; l10n Localization `29636630359` and
Foundation `29636630348` passed with the 230-message bundle checksum
`03889105a74aec819ae716ee577f78e1da8a235d42be4918aa0fb6f9c5e194b8`. Linux Native `29636710260`
(job `88060223294`) and Foundation `29636710261` passed; Flatpak `29636710259` (job `88060223278`)
is pending. Local Core storage tests and Linux worker tests verify bounded standard history writes,
Incognito skip, startup count restoration, and clear-all behavior; history inspection/export,
per-entry deletion, and translation memory remain unimplemented.

Central integration revision `a7ca1f84eef3f98647a4383dc931c11049171b63` passed coordination run
`29604649153`, including Linux job `87964871597` and Windows PowerShell job `87964871588`.

Linux Secret Service wire-shape fix revision `9bcd8d9ca30d109f5c7c9c20e6f72f6a77df078d` passed
Native Linux run `29598255988` (job `87943844854`) and repository-foundation run `29598255993`
(job `87943844922`). The native job passed strict Clippy, the GTK-enabled suite, both display
gates, the storage-fault test, and the all-target build after the `(sv)` plain-string regression
test was added. Persistent desktop keyring restoration and locked/prompted behavior remain
unverified because the CI session has no unlocked desktop keyring.

Linux Secret Service CRUD functional revision `726508f8412727f8b14e32d27407487491f5e4cd` passed
Native Linux run `29600898951` (job `87952473459`) and repository-foundation run `29600898977`.
The native job passed 75 library tests with 2 intentional ignores, the real GTK binary test under
X11/Xvfb and forced Wayland/headless Weston, the exact storage-fault gate, the isolated real-daemon
store/resolve/delete fixture, and the all-target native build. Evidence head
`93f40456a53074ad437e4ee74634348c35afc049` reran the same native gates in run `29601110914`
(job `87953169459`); repository-foundation run `29601110906` also passed. Persistent desktop
restoration and locked/prompted behavior remain separate lifecycle gates.

Linux Secret Service persistent-lifecycle revision `f58388a8e58341a8630088dc8b1782f61ab63a7c`
passed Native Linux run `29602287284` (job `87957053225`) and repository-foundation run
`29602287281`. The native fixture stored a persistent item in the `login` collection, verified
resolution, locked the collection and checked fail-closed lookup, restarted the daemon, resolved
and deleted the item, and reran cleanup. Prompted interactive flows and secure persistent-credential
onboarding remain separate gates.

Linux secure persistent-credential onboarding revision `6654a46b378d68c2c6012ccf2f30e24ae564dc7c`
passed Native Linux run `29603486498` (job `87960961963`) and repository-foundation run
`29603486477`; documentation head `3f4ba2f2c0bd0e48c5990f1640cd39b637907769` passed Native Linux
run `29603706638` (job `87961679587`) and foundation run `29603706640`. The fixture verified worker
connect/translate/restart without credential re-entry and the GTK Remember/clear-form path with
SecretRef-only SQLite persistence and an authenticated loopback provider. Prompted interactive flows
remain separate.

Linux loopback-provider revision `7d7eba9960b657f0460fb0daaaaebaaa609f39b1` passed Native Linux
run `29604269568` (job `87963611054`) and repository-foundation run `29604269516`; the ordinary
worker suite now explicitly connects to an OpenAI-compatible loopback endpoint without a credential,
selects a model, streams the fake translation, and asserts one chat request.

Linux drag-and-drop functional revision `b0da3819d97ae24f8c85147da5e7e1c65fe2d6fc` passed Native
Linux run `29597016894` (job `87939785693`) and repository-foundation run `29597016893` (job
`87939785643`). The native job passed 71 GUI-enabled library tests with one intentional ignore,
the bounded UTF-8 decoder tests, the real GTK flow including the focusable Open text file control
and single-file source-editor `DropTarget`, worker-loss disablement, the exact storage-fault gate,
both display gates, strict Clippy, and the native build. Interactive file selection, drag/drop
gestures, and portal leases remain manual boundaries.

Evidence head `cdc711320c284eae1f1376635e0d84234d8863a` passed Native Linux run `29597182692`
(job `87940328074`) and repository-foundation run `29597182729` (job `87940328419`).

Evidence head `0e86e6fb47a11dbf16fd9689795592da648c9eb3` passed Native Linux run `29598405209`
(job `87944328685`) and repository-foundation run `29598405197` (job `87944328254`).

Linux notification functional revision `07b89f36269155469a488ab830e8f485b3a1323b` passed Native
Linux run `29594795691` (job `87932451631`) and repository-foundation run `29594795681` (job
`87932451692`). The native job passed 68 GUI-enabled library tests with one intentional ignore,
the real GTK flow, the exact storage-fault gate, both X11/Xvfb and forced Wayland/headless Weston
passes, strict Clippy, and the native build. The completed-translation notification path sends
fixed generic English text without source or translated content; desktop notification-server
delivery and packaging remain unverified.

Evidence head `a7554e81c40b7d92d29a0eb8ab4fa22b1517648f` passed Native Linux run `29594948933`
(job `87932966303`) and repository-foundation run `29594948857` (job `87932965793`).

Runtime localization validation revision `1dfe2bcac684696ee55f56e625fcf89ffcb1a6dd` passed 71
GUI-enabled library tests with one intentional ignore, the same real GTK binary flow under
X11/Xvfb and forced Wayland/headless Weston, the native build, an exact real-`ENOSPC` regression,
baseline GTK accessibility assertions, and catalog-backed Translate/Stop label switching in Native
Linux run `29593874961` (job `87929412911`). Repository-foundation run `29593874763` (job
`87929412298`) also passed. The dedicated test passed once with zero ignored tests through Ubuntu's
controlled mount fallback. The CI environment does not provide a desktop Secret Service
implementation; these runs verify GIO integration and fail-closed behavior, not real keyring CRUD
or cleanup.
Evidence head `bc827d55118199e2e64e063a106da281f8a8bdf1` reran the same gates in Native Linux run
`29594014033` (job `87929863334`); repository-foundation run `29594014184` (job `87929863882`) also
passed. The GTK
assertions cover roles, named multi-line editors, visible-label relations and mnemonics, focusability,
hidden empty errors, and Busy/reset semantics using GTK 4.10 APIs. This is transaction, protocol,
backend, and semantic-widget evidence for the current slice, not evidence for every storage fault,
AT-SPI/Orca, physical keyboard traversal, a physical compositor, GPU rendering, packaging, or a
complete desktop matrix.

The scheduled and manually dispatched `cross-repository.yml` workflow clones public canonical siblings using the runtime repository owner and runs strict validation. It has read-only contents permission and is not triggered by untrusted pull requests.
