# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Unreleased compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0`; `protected_spans_v1` shields common structured spans, applies bounded request-level glossary rules, and restores immutable or required target terms across streamed output; `long_text_chunking_v1` splits oversized UTF-8 input on semantic boundaries, streams chunks in order, and propagates cancellation; `bounded_text_document_v1` validates bounded UTF-8 TXT/Markdown/SRT/WebVTT/CSV/JSON/HTML, bounded DOCX/PPTX/XLSX/EPUB packages, and text-based PDF pages, preserves line endings, cue IDs, headers, timestamps, delimiters, quoted fields, variable-width rows, selected-column boundaries, JSON keys, primitive values, whitespace, escaping, HTML tags, attributes, scripts, styles, supported OOXML text nodes, EPUB metadata/navigation/spine/CSS/resources, PDF page association and available coordinates, and OPF language updates while retaining package non-text resources, classifies Markdown fences and subtitle structure, and reconstructs completed segments; subtitle warnings report cue-level line-length and reading-speed guidance with configurable limits; deterministic glossary CSV import/export validates a fixed schema, 4 MiB bound, and 256-row bound; `TranslationPrivacyMode` carries an explicit Standard/Incognito local persistence policy with serde-default compatibility; schema 3 adds bounded translation history, schema 4 persists its enable/disable policy, schema 5 adds optional bounded translation memory with versioned identity and exact controls, schema 6 adds bounded document-job/segment snapshots, schema 7 adds transactional paused-job state and restart resumability, schema 8 adds validated non-secret document source/target locales, provider/model IDs, and bounded glossary options, schema 9 expands stored document formats for subtitle, CSV, JSON, and HTML jobs, schema 10 persists bounded DOCX package bytes, schema 11 persists bounded PPTX package bytes, schema 12 persists bounded XLSX package bytes, schema 13 persists bounded EPUB package bytes, and schema 14 persists bounded PDF package bytes with structured fidelity warnings | Functional source `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` passed CI `29655212117` and Native SDK `29655212149`, unreleased; default budget is an approximate 16 KiB UTF-8 byte bound |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1`; 306 canonical messages including Linux-only status, partial-output, text-import, opt-in image-only PDF OCR controls and errors, glossary CSV import/export and rule-validation errors, PDF fidelity and subtitle readability warnings, document-job actions/dialog/status/tooltip controls, exported-output open/failure actions, Incognito privacy controls, history and translation-memory controls/status, translation-export, provider-profile, source-target, onboarding-stage, active-provider, notification, draft-note, locale selector language names, fixed provider/file/worker errors, reducer-state/category guidance, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, and Core/loopback startup plus profile-storage error copy; paired PO/MO Linux resources | CI-verified development bundle at l10n revision `cacc1577bc1a19a94c11faeffa7a63016d54d64e`, 59 generated artifacts, deterministic bundle SHA-256 `6fc6839fce3a449eaf37d2efb9a52fa0ede1eab3a39fecdaff68682a79d8a4f8`, Localization `29668388983`, Foundation `29668388992`, unreleased |
| Android client | `0.0.0-dev` | No SDK selected | Unreleased |

Linux-first CSV document checkpoint: Core `5feaa3700764e3f174a69a4b490ae67b2d5cd8c9` adds
bounded CSV delimiter/quote parsing, selected-column segmentation, safe provider decoding and
schema-9 persistence. Linux `f198aa539d51f21e2e29b8e366884013ea436360` accepts `.csv` in the native
chooser and routes decoded fields through the worker. Native `29646594392` (job `88085783161`),
Foundation `29646594377`, and Flatpak `29646594396` (job `88085783170`) passed; this remains
unreleased.

Linux-first JSON document checkpoint: Core `ae8e437ff51fb045a6961604db6a19ebe488e0ba` adds
bounded JSON syntax validation, raw-structure preservation, default string-value segmentation,
RFC 6901 include/exclude paths, primitive/key protection, and JSON string escaping on reconstruction.
Linux `3f6d7e577afacb3aa3b7ad8c9825a243c9a0f13f` accepts `.json` in the native chooser and routes
decoded string values through the worker. Native `29647794016` (job `88088841342`), Foundation
`29647793982`, and Flatpak `29647794021` (job `88088841323`) are the current Linux gate evidence;
this remains unreleased.

Linux-first HTML document checkpoint: Core `912780f21d8dbb19571c9b991879778a053272f8` adds
bounded structural tag-stack validation, void-tag handling, raw script/style protection, visible
text-node segmentation, original tag/attribute/link preservation, and safe HTML text escaping on
reconstruction. Linux `2a04c096594f5358638fc9e5b1610c78c1051a13` accepts `.html`/`.htm` in the native
chooser and routes visible text nodes through the worker. Native `29648437605` (job `88090534144`),
Foundation `29648437590`, and Flatpak `29648437562` (job `88090534114`) are the current Linux gate
evidence; this remains unreleased.

Linux-first persisted document queue checkpoint: Linux `ba7d4a3ad9d1cc152d5c52e5acf84633ae46ef92`
adds the non-blocking queue-list command, localized “Document jobs” action, empty/list dialog,
progress/state metadata, and selection back into the existing resume/retry/pause/cancel/export
controls. Packaging revision `71e8b24dd6f233c4667c705066524489b065e49a` pins the Flatpak source.
Native `29649067477` (job `88092162300`), Foundation `29649067457`, and Flatpak `29649067473`
(job `88092162266`) passed; archive codecs and the remaining platform clients remain open.

Linux-first DOCX package checkpoint: Core `08eb64cb87d9cf6df624225819818d8287063c4c` adds
bounded ZIP/XML inspection, schema-10 package persistence, safe OOXML text-node reconstruction, and
resource retention. Linux packaging revision `3725ef97584b30ee34e7807e35cddc16df6ad8ae` pins the
DOCX-capable Linux source and current vendored dependency set. Native `29650642852` (job
`88096278936`), Foundation `29650642855`, and Flatpak `29650642850` (job `88096278936`) passed.
Packages over 4 MiB or 512 entries, encrypted/traversal/duplicate/malformed/DTD-bearing packages,
and incomplete exports are rejected; PPTX/XLSX, EPUB, PDF/OCR, remaining archive codecs, and other
platform clients remain open.

Linux-first subtitle readability checkpoint: Core `81be0b8be9d7115b98eae3f134b4fd0f25411bbb` adds
cue-level `DocumentWarning` values for configurable subtitle line-length and reading-speed guidance
while preserving timing and source content. Linux `60b560383e53bf4cf9ccc5ecf3821fe735206446`
persists the warnings and renders cue-number-only guidance without exposing subtitle source text.
Localization `738a7c7328f24acc12c15be78bb11737220bbbae` supplies the PDF and subtitle warning
messages. Core CI `29655212117`, Native SDK `29655212149`, Linux Native `29656158543`, Foundation
`29656158527`, and Flatpak `29656158526` passed; defaults are 42 Unicode characters per line and
17 non-whitespace characters per second, with custom limits available through Core. OCR, remaining
archive codecs, complete acceptance scenarios, and non-Linux clients remain open.

Linux-first document queue localization checkpoint: l10n `0ef4fb9b6878655e46e2b8ca5bbed9562f97b0f0`
adds ten catalog-backed Linux-only action, dialog, status, progress, and tooltip messages, raising
the bundle to 277 messages with checksum
`e26da1a391369ed84c0f57f5fd5d440f50ed56dcbc8f069abd4d6d27db7dd9c1`. Linux `191345c55dc8989d518680c864a4c4a643165f6c`
syncs all twelve PO/MO packs and asserts the queue keys alongside PDF/subtitle warnings. l10n
Localization `29656496378` and Foundation `29656496361`, Linux Native `29656549651`, Foundation
`29656549644`, and Flatpak `29656549677` passed; non-English packs remain unreviewed drafts and
complete visible-string coverage, cross-platform clients, OCR, and stable-release evidence remain open.
Linux test head `1e60e3725b0548a82bb88402c5257eb0f5f0bb0c` additionally asserts keyboard focusability
for the queue actions; Native `29657086074`, Foundation `29657086060`, and Flatpak `29657086067` passed.

Linux-first exported-output checkpoint: l10n `4be0401a09ce26e65c8fd3c921e333d6011e8706`
adds localized open-output and open-failure messages, raising the bundle to 280 messages with
checksum `61fe261fb62e996b637745913bb89e5a5e0c0a16a82c5d2fe536a254cf61b6ee`. Linux
`45d9365eaba0b25d58c65a09e4a5dcfa2bae0840` records the last successfully exported GIO URI only
after the asynchronous write completes, exposes a focusable Open exported output action, launches
it through the default GIO handler, clears stale destinations on new imports/translations, and
reports a fixed localized error without exposing paths. l10n Localization `29657734947` and
Foundation `29657734951`, Linux Native `29657811742`, Foundation `29657811734`, and Flatpak
`29657811738` passed; routing fallback, OCR, screen-reader narration, physical keyboard traversal,
other platform clients, complete acceptance scenarios, and stable-release evidence remain open.

Linux-first approved text fallback checkpoint: l10n `273be8a4e9c3b1084f393ce0086cdf2c42fcd4e9`
adds six Linux-only messages, producing 286 canonical messages with deterministic bundle checksum
`ee7c269571beca22cdbd7bea971ae266975b8004490b02ead4b71305e3a93872`. Linux
`878a9c015d29ce49633046d435f48f5fee4c9a47` adds an explicit different saved-provider selector and
single retry for network/timeout failures on ordinary text only; partial output is retained and the
selection is localized without exposing endpoints or content. Document jobs, cancellation,
authentication/model failures, unapproved profiles, and session-only profiles never fall back. Local
Linux suites passed (61/100 tests, one existing environment-dependent ignore), strict Clippy, GUI
check, l10n sync, and diff checks; Native `29659054771`, Foundation `29659054755`, and Flatpak
`29659054756` passed for the current head.

Linux-first keyboard traversal checkpoint: Linux `8f2cba0` adds an application-window Capture-phase
provider-form Tab/Shift+Tab order while preserving modified Ctrl/Alt/Super shortcuts, and the
Xvfb/xfwm4 fixture verifies provider fields plus onboarding/workspace controls from a real GTK
focus path. Default-branch Native `29663597817` (job `88130256368`), Foundation `29663597809` (job
`88130256318`), and Flatpak `29663597831` (job `88130256370`) passed; screen-reader narration, physical desktop
review, OCR, other platform clients, and stable-release evidence remain open.

Linux-first AT-SPI semantic export checkpoint: Linux `7480579e4ae305758397082b7456715939666a9e`
adds an isolated Xvfb/xfwm4 fixture that starts the AT-SPI bus and reads the running GTK tree with
`python3-pyatspi`, verifying the named `Stop translation` push button and two text-editor roles;
the existing GTK helper continues to verify label relations, editor properties, and state changes.
Default-branch Native `29664478686` (job `88132499067`), Foundation `29664478672`, and Flatpak
`29664478670` passed. Orca speech, provider-form default Tab-chain review, physical desktop
accessibility, OCR, other platform clients, and stable-release evidence remain open.

Linux-first dialog field localization checkpoint: Linux `1b68cef85d89324baba20689ce246486ab28c49b`
uses the catalog-backed `field.source_text` and `field.translation` labels for source and translated
content prefixes in the history and translation-memory dialogs. Native `29664934283` (job
`88133657483`), Foundation `29664934298`, and Flatpak `29664934279` passed; dynamic `Job` and
`Identity` metadata, complete visible-string gettext coverage, and the remaining Linux/release
boundaries remain open.

Linux-first dialog metadata localization checkpoint: Linux `c19192fbd78b30aa55a5bac94c133c7400c78642`
routes the document-job identifier and translation-memory identity prefixes through the active
catalog, reusing the existing Linux dialog keys without changing stored content or locale packs.
Native `29665343100` (job `88134735908`), Foundation `29665343120`, and Flatpak `29665343145`
passed. Complete visible-string gettext coverage, Orca speech, physical desktop review, OCR,
other platform clients, and stable-release evidence remain open.

Linux-first multi-job queue controls checkpoint: Linux `014a79a19cb72b4eceba3d7c0c592b7655e1cdd0`
adds catalog-backed pause, resume, and retry actions to each persisted document-job row while
reusing the existing worker commands and storage state machine. Native `29665725241`, Foundation
`29665725238`, and Flatpak `29665725434` passed; OCR, Orca speech, physical desktop review,
complete visible-string gettext coverage, other platform clients, and stable-release evidence
remain open.

Linux-first glossary validation localization checkpoint: l10n `ede66149c501a1680ed050d76b8b78e7b565ba01`
adds three Linux-only catalog keys for glossary syntax, invalid/credential-like data, and
conflicting rules, producing 289 canonical messages and bundle checksum
`c8bd6b0464ebbfa015988a4fc0cfd30b1f9e28d9e1aad19b8c50d36976128e8f`. Linux `cb22b2052362ce7b4990cc4be99e26a152b07800` synchronizes the PO/MO snapshot and maps these errors through
the runtime catalog. Native `29666379600`, Foundation `29666379579`, and Flatpak `29666379586`
passed; complete visible-string gettext coverage, Orca speech, physical desktop review, OCR,
other platform clients, and stable-release evidence remain open.

Linux-first provider-form Tab-chain evidence checkpoint: Linux `713c86b3da9b057cc25e72c687dc6c4c265f6439`
records the application-window Capture-phase Tab/Shift+Tab order for saved-profile, provider,
credential, Connect, and Remember controls while preserving modified shortcuts. Native
`29666820550`, Foundation `29666820602`, and Flatpak `29666820579` passed the current head,
including the Xvfb/xfwm4 keyboard fixture. Orca speech, physical desktop review, OCR, complete
visible-string gettext coverage, other platform clients, and stable-release evidence remain open.

Linux-first document-job metadata localization checkpoint: l10n `c81728faf8679e7a5e9854537ad7c70c046c7800`
adds seven Linux-only catalog messages for the document-job row template and pending/running/
paused/completed/cancelled/failed states, producing 296 canonical messages and bundle checksum
`d2f4fd439b5fbc8fc6d48f1be0a91ee92f558c70b851271d643829cfe8590e9b`. Linux
`76b5f632fee62dc8e323e0cfec5d420e6fcc6992` maps document format and lifecycle metadata through
the active catalog instead of Rust debug output. Native `29667553178`, Foundation `29667553139`,
and Flatpak `29667553149` passed, including the GTK AT-SPI/Wayland and Flatpak smoke gates. Orca
speech, physical desktop review, OCR, complete visible-string gettext coverage, other platform
clients, and stable-release evidence remain open.

Linux-first PPTX package checkpoint: Core `0f71a652a536753f48bb8c852fd38e97740c23ce` adds bounded
PPTX ZIP/XML inspection, schema-11 package persistence, safe slide/notes/master/layout/handout/
comments text-node reconstruction, and resource retention. Linux functional revision
`ce08d1232889522bead58e6056d296f0fc8d56e1` adds native chooser/import, worker reconstruction, and
binary export; packaging revision `766b78e4b236f15ee7a6f1d6e61ebd828415da82` pins the final source.
Native `29651317600`, Foundation `29651317621`, and Flatpak `29651317679` passed. Packages over 4 MiB or 512 entries, encrypted/traversal/duplicate/
malformed/DTD-bearing packages, and incomplete exports are rejected; XLSX, EPUB, PDF/OCR, remaining
archive codecs, and other platform clients remain open.

Linux-first XLSX package checkpoint: Core `36f256637236636889b0933cc5fe6a70bffff02c` adds bounded
XLSX ZIP/XML inspection, schema-12 package persistence, safe shared-string/worksheet text-node
reconstruction, and resource retention. Linux functional revision `731072eb3d9b29a43fe0e238084290cd5c253e59`
adds native chooser/import, worker reconstruction, and binary export. Native `29651990077`,
Foundation `29651990067`, and Flatpak `29651990064` passed. Packages over 4 MiB or 512 entries,
encrypted/traversal/duplicate/malformed/DTD-bearing packages, and incomplete exports are rejected;
EPUB, PDF/OCR, remaining archive codecs, and other platform clients remain open.

Linux-first EPUB package checkpoint: Core `554c09521b57de45be154a99edfbf24aa2fc6538` adds bounded
EPUB ZIP/XML inspection, schema-13 package persistence, safe XHTML/HTML text reconstruction,
OPF `dc:language` updates from the persisted target locale, and package resource retention. Linux
functional revision `3f0f659ccba195e58789d80d9fdc20b087a10b68` adds native chooser/import, worker
reconstruction, binary export, MIME filtering, Flatpak pinning, and documentation. Local Core
document/storage tests (22/28) and Linux checks/Clippy/library tests (61) passed; Core CI `29652884450`,
Native SDK `29652884430`, Linux Native `29652937783`, Foundation `29652937750`, and Flatpak
`29652937761` passed. Packages over 4 MiB or 512 entries, wrong first `mimetype`,
encrypted/traversal/duplicate/malformed/DTD-bearing packages, and incomplete exports are rejected;
PDF/OCR, remaining archive codecs, and other platform clients remain open.

Linux-first subtitle document checkpoint: Core `e4962fc19dd09ca2ef45d4841ffb617cb25a1342` adds
bounded SRT/WebVTT detection, cue/timestamp structural validation, and inter-cue WebVTT metadata
handling on top of schema-8 document options. Linux `33b47852f3bd3a0a4a8997cd6592c756a0b254a3`
accepts `.srt`/`.vtt` in the native chooser, maps malformed structures to a safe import error, and
keeps cue IDs/timestamps unchanged while translating cue text. Native `29645547013` (job
`88083068099`), Foundation `29645547036` (job `88083068179`), and Flatpak `29645547024` (job
`88083068088`) passed; Core CI `29645385353` and
Native SDK `29645385324` passed. This remains unreleased.
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; `protected_spans_v1`, `long_text_chunking_v1`, and `bounded_text_document_v1` negotiation with common URL/email/Markdown-code/placeholder and bounded request-level glossary restoration plus fail-closed marker validation; semantic chunking keeps oversized requests ordered and cancellation-aware; Core TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX/EPUB inspection preserves BOM, line endings, Markdown fences, cue IDs, headers, timestamps, CSV delimiters, quoting, variable-width rows, selected-column boundaries, JSON structure, keys, primitive values, string escaping, exact include/exclude path selection, HTML tags, attributes, links, scripts, styles, text-node structure, supported OOXML text nodes, EPUB metadata/navigation/spine/CSS/resources, and text-PDF page association/coordinates with structured HTML fallback; schema-14 document jobs persist bounded segment progress, validated non-secret source/target/provider/model/glossary options, PDF warning metadata, and package bytes, restoring pending/running/paused jobs after worker restart without filesystem paths or credentials; native imports create persisted jobs before editor population, and the GTK queue lists snapshots with localized action/dialog/status/progress/tooltip controls and selection back into resume/retry/pause/cancel/export; TranslateDocumentJob sequentially translates pending prose segments while committing each completed segment; binary package/PDF export retains resources or falls back to page-aware HTML when required; bounded fixed-schema glossary CSV import/export through GTK FileDialog; explicit Incognito request policy routed into Core and rejected for new durable document jobs; bounded local history and translation-memory controls; multi-profile/model persistence; derived onboarding with catalog-backed stage/detail guidance; session credentials; GIO Secret Service adapter and no-credential OpenAI-compatible loopback provider; twelve official Linux PO/MO packs with catalog-backed runtime controls, PDF/subtitle warnings, document queue controls, Arabic RTL root direction, and explicit opt-in bounded image-only PDF OCR to page-marked TXT; generic completion notification; private notification-service, dunst, document-portal, FileDialog, drag/drop, GTK accessibility, headless Xvfb/xfwm4 keyboard traversal, and Flatpak smoke verification | Functional source `d18e8dfa3dd98d56dbe0d5d1eabc536d38b96f1c` passed Native `29668688201` (job `88143670012`), Foundation `29668688202`, and Flatpak `29668688223` (job `88143670073`); l10n `cacc1577bc1a19a94c11faeffa7a63016d54d64e` passed Localization `29668388983` and Foundation `29668388992`; end-user prompt approval, complete visible-string gettext coverage, physical compositor/GPU rendering, signing, distributable release, and stable release remain open, unreleased |

The Linux row above is superseded by the current EPUB checkpoint: Core `554c09521b57de45be154a99edfbf24aa2fc6538`, Linux `3f0f659ccba195e58789d80d9fdc20b087a10b68`, schema 13, and passed Core CI `29652884450`, Native SDK `29652884430`, Linux Native `29652937783`, Foundation `29652937750`, and Flatpak `29652937761`. EPUB package metadata, navigation, CSS, resources, visible XHTML/HTML text, and OPF language updates are included; PDF/OCR and other platform clients remain open.

Linux-first text-PDF checkpoint: Core `4f03618ffb1f37f27fb1edcf2de5a80e3bec540d` adds bounded PDF
object/page inspection, page-aware text segments, basic coordinates and reading-order boundaries,
Flate stream support, safe ASCII literal/hex rewriting, schema-14 persistence, and a structured
HTML alternative when target text cannot be safely encoded, plus structured warnings for image-only
pages, uncertain reading order, and limited reconstruction. Linux `edbfad1a8e443d86f39c782f4ad991a029cb8e76`
adds PDF chooser/MIME filtering, worker export fallback to `.html`, localized UI warning plumbing,
and updated documentation. Core CI `29654538722`, Native SDK `29654538670`, Linux Native
`29654651108`, Foundation `29654651074`, and Flatpak `29654651067` are the current gates; OCR,
pixel-identical reconstruction, image-only page translation, remaining archive codecs, and other
platform clients remain open.

The Linux client uses a GIO D-Bus Secret Service adapter for persistent SecretRef values and fails
closed when the service is unavailable, locked, or requests interaction. It can create, update,
switch, and delete multiple provider profiles,
preserve independent confirmed model preferences, restore the full list/default without connecting,
require explicit Connect for activation, and keep a deleted connected row's validated runtime as
session-only. Its derived setup card identifies the stable provider/model for the next request,
retains storage-degradation warnings, and disables commands after worker loss. Authenticated A/B
request counters verify Linux-side remembered model routing and failed-switch isolation. Credential
re-entry remains required for session-only connections; only persistent SecretRef identifiers are
stored, never credential values or session references, and nothing falls back to plaintext. A real Linux `ENOSPC` gate verifies that failed persistent Connect, model-update,
and deletion transactions reject before success, preserve the prior session, and restore only
pre-fault state. The GTK flow also exposes baseline roles, named multi-line editors, visible-label
mnemonics, focusable controls, hidden empty errors, and translation Busy/reset semantics on GTK
4.10+. Runtime switching exposes all twelve official Linux PO packs, switches catalog-backed
Translate and Stop labels, refreshes catalog-backed workspace widgets and status summaries/partial-output markers, and applies Arabic RTL root direction, with explicit English fallback for
uncovered UI keys. Completed translations send a generic desktop notification
without source or translated content; private notification-service transport, headless delivery to a
real `dunst` daemon, and a visible viewable Dunst desktop-shell window are verified, while physical
compositor/GPU rendering and packaging remain runtime boundaries. Native Open text file import accepts bounded UTF-8 TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT content, and a single
GIO file can be dropped onto the source editor through the same validation path; the real document-
portal lease lifecycle and a direct interactive `xdg-desktop-portal-gtk` FileChooser backend are
verified, and application-level GTK FileDialog and source-editor drag/drop fixtures pass under
Xvfb. It does not cover every database or storage failure. Real
end-user prompt approval and complete UI gettext coverage remain open; global Scenarios 3 and 5
still require cross-platform evidence. Stable clients must pin
a released core and reject an unknown ABI major. Every release-train update must include source
revisions, artifact checksums, minimum compatible versions, known limitations, and cross-repository
conformance evidence. Development placeholders and the alpha.2 source checkpoints are not
consumable releases.

Linux-first optional image-only PDF OCR checkpoint: l10n `cacc1577bc1a19a94c11faeffa7a63016d54d64e`
adds ten Linux-only toggle, progress, and fixed-error messages, producing 306 canonical messages
and deterministic bundle checksum `6fc6839fce3a449eaf37d2efb9a52fa0ede1eab3a39fecdaff68682a79d8a4f8`.
Linux `d18e8dfa3dd98d56dbe0d5d1eabc536d38b96f1c` invokes bounded, shell-free `pdftoppm`/`tesseract`
only after explicit user opt-in for image-only PDF pages, stores page-marked text as a TXT job, and
keeps the source PDF untouched. Native `29668688201` (job `88143670012`), Foundation `29668688202`,
and Flatpak `29668688223` (job `88143670073`) passed; the Native fixture exercised the external OCR
tools. OCR is not enabled by packaging defaults, and Orca speech, physical desktop review, complete
visible-string gettext coverage, other clients, and stable-release evidence remain open.
