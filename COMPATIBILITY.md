# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Unreleased compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0`; `protected_spans_v1` shields common structured spans, applies bounded request-level glossary rules, and restores immutable or required target terms across streamed output; `long_text_chunking_v1` splits oversized UTF-8 input on semantic boundaries, streams chunks in order, and propagates cancellation; `bounded_text_document_v1` validates bounded UTF-8 TXT/Markdown/SRT/WebVTT/CSV/JSON/HTML and bounded DOCX/PPTX/XLSX/EPUB packages, preserves line endings, cue IDs, headers, timestamps, delimiters, quoted fields, variable-width rows, selected-column boundaries, JSON keys, primitive values, whitespace, escaping, HTML tags, attributes, scripts, styles, supported OOXML text nodes, EPUB metadata/navigation/spine/CSS/resources, and OPF language updates while retaining package non-text resources, classifies Markdown fences and subtitle structure, and reconstructs completed segments; deterministic glossary CSV import/export validates a fixed schema, 4 MiB bound, and 256-row bound; `TranslationPrivacyMode` carries an explicit Standard/Incognito local persistence policy with serde-default compatibility; schema 3 adds bounded translation history, schema 4 persists its enable/disable policy, schema 5 adds optional bounded translation memory with versioned identity and exact controls, schema 6 adds bounded document-job/segment snapshots, schema 7 adds transactional paused-job state and restart resumability, schema 8 adds validated non-secret document source/target locales, provider/model IDs, and bounded glossary options, schema 9 expands stored document formats for subtitle, CSV, JSON, and HTML jobs, schema 10 persists bounded DOCX package bytes, schema 11 persists bounded PPTX package bytes, schema 12 persists bounded XLSX package bytes, and schema 13 persists bounded EPUB package bytes | Functional source `554c09521b57de45be154a99edfbf24aa2fc6538` CI pending and Native SDK pending, unreleased; default budget is an approximate 16 KiB UTF-8 byte bound |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1`; 262 canonical messages including Linux-only status, partial-output, text-import, glossary CSV import/export, Incognito privacy controls, history and translation-memory controls/status, translation-export, provider-profile, source-target, onboarding-stage, active-provider, notification, draft-note, locale selector language names, fixed provider/file/worker errors, reducer-state/category guidance, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, and Core/loopback startup plus profile-storage error copy; paired PO/MO Linux resources | CI-verified development bundle at l10n evidence revision `d64d4085fb3c1cc69c9f7965bd97ffca54ca1995`, 59 generated artifacts, deterministic bundle SHA-256 `a3de4b0bf4afd710a01d15e0426f0d163b56910c0b04f26c411870eae9eea368`, unreleased |
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
document/storage tests (22/28) and Linux checks/Clippy/library tests (61) passed; Native, Foundation,
and Flatpak GitHub gates are pending. Packages over 4 MiB or 512 entries, wrong first `mimetype`,
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
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; `protected_spans_v1`, `long_text_chunking_v1`, and `bounded_text_document_v1` negotiation with common URL/email/Markdown-code/placeholder and bounded request-level glossary restoration plus fail-closed marker validation; semantic chunking keeps oversized requests ordered and cancellation-aware; Core TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX inspection preserves BOM, line endings, Markdown fences, cue IDs, headers, timestamps, CSV delimiters, quoting, variable-width rows, selected-column boundaries, JSON structure, keys, primitive values, string escaping, exact include/exclude path selection, HTML tags, attributes, links, scripts, styles, text-node structure, supported OOXML text nodes, and DOCX/PPTX/XLSX non-text resources; schema-12 document-job create/list/update/pause/resume/retry/cancel commands persist bounded segment progress, validated non-secret source/target/provider/model/glossary options, and bounded DOCX/PPTX/XLSX package bytes, restoring pending/running/paused jobs after worker restart without filesystem paths or credentials; native TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX import now creates persisted jobs before editor population, and the GTK queue lists persisted snapshots with progress/state metadata and selection back into resume/retry/pause/cancel/export controls; TranslateDocumentJob sequentially translates pending prose segments while committing each completed segment; binary DOCX/PPTX/XLSX export retains package resources and rejects incomplete jobs; bounded fixed-schema glossary CSV import/export through GTK FileDialog; explicit Incognito request policy routed into Core and rejected for new durable document jobs; bounded local translation history with startup count and clear-all control, skipping Incognito completions; multi-profile/model persistence; derived onboarding with catalog-backed stage and detail guidance; session credentials; GIO Secret Service adapter with a valid single-layer plain-string OpenSession payload, isolated real-daemon CRUD/cleanup, persistent daemon-restart/locked-item fail-closed lifecycle, secure persistent-credential onboarding, and prompted store/delete fail-closed verification, plus session-only fallback; no-credential OpenAI-compatible loopback provider connection and streaming; twelve official Linux PO/MO packs with runtime action-label, workspace-widget, active-provider, active-provider transition/mode, status-summary/partial-output, text-file import/export, glossary CSV import/export, Incognito and history controls, provider-profile, source/target language, locale selector language names, onboarding-stage, draft-note, fixed provider/file/worker and reducer-state/category error messages, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, Core/loopback startup and profile-storage error copy, and theme-option switching, source-buffer preservation across a Simplified Chinese-to-Arabic locale switch, and Arabic RTL root direction; generic completion desktop notification without source or translated content; private notification-service `Notify` transport verification; headless real `dunst` notification-daemon delivery and visible viewable Dunst window verification; real XDG document-portal lease lifecycle verification; direct interactive `xdg-desktop-portal-gtk` FileChooser backend verification; application-level GTK FileDialog callback and source-editor URI-list drag/drop verification; bounded native UTF-8 TXT/Markdown/CSV/JSON/HTML/SRT/WebVTT/DOCX/PPTX/XLSX import up to 4 MiB; asynchronous UTF-8 text and binary document export with source-file overwrite protection; post-startup storage degradation; baseline GTK accessibility semantics on GTK 4.10+; bounded history inspection, exact per-entry deletion, escaped UTF-8 TSV export, persisted history enable/disable policy, and optional translation-memory policy/cache with versioned identity, Incognito bypass, inspection, export, exact deletion, and clear-all; pinned Flatpak packaging scaffold with GNOME 49 SDK build, prerelease CI bundle, and bounded sandbox startup smoke | Functional source `731072eb3d9b29a43fe0e238084290cd5c253e59` passed Native `29651990077`, Foundation `29651990067`, and Flatpak `29651990064`; end-user prompt approval, complete visible-string gettext coverage, physical compositor/GPU rendering, signing, distributable release, and stable release remain open, unreleased |

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
