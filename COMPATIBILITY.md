# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Unreleased compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0`; `protected_spans_v1` shields common structured spans, applies bounded request-level glossary rules, and restores immutable or required target terms across streamed output; `long_text_chunking_v1` splits oversized UTF-8 input on semantic boundaries, streams chunks in order, and propagates cancellation; deterministic glossary CSV import/export validates a fixed schema, 4 MiB bound, and 256-row bound; `TranslationPrivacyMode` carries an explicit Standard/Incognito local persistence policy with serde-default compatibility; schema 3 adds bounded translation history with a 100-entry and 4 MiB source/output limit | Functional source `6079138348f3182b19c017f50db768df05da62cb` CI-verified, unreleased; default budget is an approximate 16 KiB UTF-8 byte bound |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1`; 240 canonical messages including Linux-only status, partial-output, text-import, glossary CSV import/export, Incognito privacy controls, history controls/status, translation-export, provider-profile, source-target, onboarding-stage, active-provider, notification, draft-note, locale selector language names, fixed provider/file/worker errors, reducer-state/category guidance, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, and Core/loopback startup plus profile-storage error copy; paired PO/MO Linux resources | CI-verified development bundle at l10n evidence revision `971d1691a4eff396c71216b898e30fcfb23e72fa`, 59 generated artifacts, deterministic bundle SHA-256 `36f782f45a228f68520c691a7d015a4839531a892732e31119fd5c0e83a2be9c`, unreleased |
| Android client | `0.0.0-dev` | No SDK selected | Unreleased |
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; `protected_spans_v1` and `long_text_chunking_v1` negotiation with common URL/email/Markdown-code/placeholder and bounded request-level glossary restoration plus fail-closed marker validation; semantic chunking keeps oversized requests ordered and cancellation-aware; bounded fixed-schema glossary CSV import/export through GTK FileDialog; explicit Incognito request policy routed into Core; bounded local translation history with startup count and clear-all control, skipping Incognito completions; multi-profile/model persistence; derived onboarding with catalog-backed stage and detail guidance; session credentials; GIO Secret Service adapter with a valid single-layer plain-string OpenSession payload, isolated real-daemon CRUD/cleanup, persistent daemon-restart/locked-item fail-closed lifecycle, secure persistent-credential onboarding, and prompted store/delete fail-closed verification, plus session-only fallback; no-credential OpenAI-compatible loopback provider connection and streaming; twelve official Linux PO/MO packs with runtime action-label, workspace-widget, active-provider, active-provider transition/mode, status-summary/partial-output, text-file import/export, glossary CSV import/export, Incognito and history controls, provider-profile, source/target language, locale selector language names, onboarding-stage, draft-note, fixed provider/file/worker and reducer-state/category error messages, fixed worker/file/storage/provider-error guidance, construction-stage provider/default-control and request-level glossary copy, Core/loopback startup and profile-storage error copy, and theme-option switching, source-buffer preservation across a Simplified Chinese-to-Arabic locale switch, and Arabic RTL root direction; generic completion desktop notification without source/translated content; private notification-service `Notify` transport verification; headless real `dunst` notification-daemon delivery and visible viewable Dunst window verification; real XDG document-portal lease lifecycle verification; direct interactive `xdg-desktop-portal-gtk` FileChooser backend verification; application-level GTK FileDialog callback and source-editor URI-list drag/drop verification; bounded native UTF-8 TXT/Markdown import up to 4 MiB; asynchronous UTF-8 translation export with source-file overwrite protection; post-startup storage degradation; baseline GTK accessibility semantics on GTK 4.10+; bounded history inspection, exact per-entry deletion, and escaped UTF-8 TSV export; pinned Flatpak packaging scaffold with GNOME 49 SDK build, prerelease CI bundle, and bounded sandbox startup smoke | Functional source `9ff8f3fb9cf61e1f51c3fc5e042e5fc8f601b837` passed Native run `29638278667` (job `88064319932`), Foundation run `29638278676`, and Flatpak run `29638278677` (job `88064320034`); end-user prompt approval, complete visible-string gettext coverage, physical compositor/GPU rendering, signing, distributable release, translation-memory stores and history enable/disable policy remain open, unreleased |

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
compositor/GPU rendering and packaging remain runtime boundaries. Native Open text file import accepts bounded UTF-8 TXT/Markdown content, and a single
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
