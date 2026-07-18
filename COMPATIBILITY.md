# Compatibility

No compatible stable release train exists yet. The authoritative machine-readable record is [`release-manifest.toml`](release-manifest.toml); its shape is defined by [`schemas/release-manifest.schema.json`](schemas/release-manifest.schema.json).

Global goal revision: `sha256:11f9a65927aac7e57e2af119e9d21cc98e8d5a08b8a112a19ee1c47903e36198`.

## Unreleased compatibility matrix

| Component | Version | Compatibility | Status |
| --- | --- | --- | --- |
| Core | `0.1.0-alpha.2` | ABI `1`, protocol schema `0.1.0` (wire version 1), provider catalog `0.1.0` | Functional source `fbf3e9b5927049dccaa19f8c36013495ffebba12` CI-verified, unreleased |
| Provider catalog | `0.1.0` | Schema `1` | Locally verified, unreleased |
| Localization | `0.1.0` | Message schema `1.0.0`; resource contract `1`; 172 canonical messages including Linux-only status, partial-output, text-import, provider-profile, source-target, onboarding-stage, active-provider, notification, draft-note, fixed provider/file/worker errors, reducer-state/category guidance, and fixed worker/file/storage/provider-error guidance; paired PO/MO Linux resources | CI-verified development bundle at l10n evidence revision `cc841103c3480ece237baa088bbb5881a321cf0a`, 59 generated artifacts, deterministic bundle SHA-256 `e55dbd79f9ba010161ac998a940d4a8a142c8aca0385731882b65f38acc3228e`, unreleased |
| Android client | `0.0.0-dev` | No SDK selected | Unreleased |
| Windows client | `0.0.0-dev` | No SDK selected | Unreleased |
| macOS client | `0.0.0-dev` | No SDK selected | Unreleased |
| Linux client | `0.1.0-alpha.2` | Exact Core `0.1.0-alpha.2`; ABI `1`; wire protocol 1; multi-profile/model persistence; derived onboarding with catalog-backed stage and detail guidance; session credentials; GIO Secret Service adapter with a valid single-layer plain-string OpenSession payload, isolated real-daemon CRUD/cleanup, persistent daemon-restart/locked-item fail-closed lifecycle, secure persistent-credential onboarding, and prompted store/delete fail-closed verification, plus session-only fallback; no-credential OpenAI-compatible loopback provider connection and streaming; twelve official Linux PO/MO packs with runtime action-label, workspace-widget, active-provider, active-provider transition/mode, status-summary/partial-output, text-file import, provider-profile, source/target language, onboarding-stage, draft-note, fixed provider/file/worker and reducer-state/category error messages, fixed worker/file/storage/provider-error guidance, and theme-option switching, source-buffer preservation across a Simplified Chinese-to-Arabic locale switch, and Arabic RTL root direction; generic completion desktop notification without source/translated content; private notification-service `Notify` transport verification; headless real `dunst` notification-daemon delivery and visible viewable Dunst window verification; real XDG document-portal lease lifecycle verification; direct interactive `xdg-desktop-portal-gtk` FileChooser backend verification; application-level GTK FileDialog callback and source-editor URI-list drag/drop verification; bounded native UTF-8 TXT/Markdown import up to 4 MiB; post-startup storage degradation; baseline GTK accessibility semantics on GTK 4.10+; pinned Flatpak packaging scaffold with GNOME 49 SDK build, prerelease CI bundle, and bounded sandbox startup smoke | Functional source `e7d2f7776d3c129e1f66a1feacd04c4826160a2b` passed Native run `29629498575`, Foundation run `29629498574`, and Flatpak run `29629498588`; end-user prompt approval, complete visible-string gettext coverage, physical compositor/GPU rendering, signing, and distributable release remain open, unreleased |

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
