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

The current Linux-first TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB/PDF document slice is pinned to Core
`81be0b8be9d7115b98eae3f134b4fd0f25411bbb`, l10n `273be8a4e9c3b1084f393ce0086cdf2c42fcd4e9`, and
Linux `8f2cba0`. Core CI `29655212117`, Native SDK `29655212149`, and default-branch Linux Native `29663597817`
(job `88130256368`), Foundation `29663597809` (job `88130256318`), and Flatpak `29663597831` (job `88130256370`) passed. The l10n Localization `29658713355`
and Foundation `29658713372` passed with the 286-message bundle checksum
`ee7c269571beca22cdbd7bea971ae266975b8004490b02ead4b71305e3a93872`. Local Core storage tests
and Linux worker tests verify bounded standard history writes, Incognito skip, startup count/policy
restoration, cache identity/reuse, clear-all, newest-first inspection, exact per-entry deletion,
escaped UTF-8 TSV export, the bounded Core TXT/Markdown/CSV/SRT/WebVTT document contract with BOM,
line-ending, cue-ID, header, timestamp, subtitle-structure, CSV delimiter/quote, variable-width row,
and selected-column preservation, JSON path selection, primitive/key protection, escaping, HTML tag-stack validation, script/style protection, text-node escaping, bounded DOCX/PPTX/XLSX/EPUB package path/XML/resource preservation, page-aware text-PDF extraction/reconstruction and structured HTML fallback, cue-level subtitle line-length/reading-speed warnings with configurable limits, schema-14 job bounds/options, segment updates, and restart
recovery of pending/running/paused jobs without paths or credentials; bounded PDF warnings for
image-only pages, uncertain reading order, and limited reconstruction; pause/resume/retry worker
and GTK control regressions, including restart reuse and persisted-job queue selection, are covered
by the Linux library suite. The current Linux GTK slice also records successful asynchronous export
URIs and opens them through the default GIO handler; stale destinations are cleared on new imports
or translations, and open failures use a fixed localized message without exposing paths. Linux ordinary
text also has a user-approved saved-provider fallback path that retries only network/timeout failures,
retains partial output, and never applies to document jobs, cancellation, authentication/model errors,
or unapproved/session-only profiles; its focused worker test passes locally.
The Linux keyboard fixture runs the real GTK binary under Xvfb with `xfwm4`, injects Tab/Shift+Tab,
and asserts focus events for the tested onboarding/workspace controls. Provider fields are checked as
enabled, mapped, and focusable, but their omission from the default Tab chain is recorded as an open
Linux accessibility item.
Central coordination run `29659286541` passed Linux validation job `88118991875` and PowerShell
validation job `88118991823` after the approved-fallback manifest and compatibility updates.

Central integration revision `e1bcf55ed16f734e14a559e292588dc8285c672e` passed coordination run
`29639330664`, including Linux job `88067060177` and Windows PowerShell job `88067060171`.

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
AT-SPI/Orca, physical desktop keyboard, a physical compositor, GPU rendering, packaging, or a
complete desktop matrix.

The scheduled and manually dispatched `cross-repository.yml` workflow clones public canonical siblings using the runtime repository owner and runs strict validation. It has read-only contents permission and is not triggered by untrusted pull requests.
Central documentation revision `d547d882812c61dc0a9a7a3c0abd93c3ea41acce` passed coordination run
`29649436735` (Linux job `88093116621`, PowerShell job `88093116615`) after the Linux persisted
document queue pins, evidence, and unreleased limitations were updated. The Linux document-job execution
slice is covered by the same Native and Flatpak gates; its GTK queue lists persisted snapshots and
selection reuses the existing job controls, while provider parameters are supplied again when
resuming after restart.
