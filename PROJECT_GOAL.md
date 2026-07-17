/goal Build and release LinguaMesh as a production-grade, local-first, fully native, high-performance, multi-repository AI translation suite. Work continuously in verified checkpoints. Do not stop at planning, scaffolding, mock-only UI, or placeholder code. The durable completion condition is that compatible stable releases of the shared Rust core and the Android, Windows, macOS, and Linux native clients are recorded in the central release manifest, all mandatory acceptance scenarios pass, and all claimed capabilities have reproducible test evidence.

# PROJECT GOAL — LinguaMesh Native

## 0. Authority and Operating Role

You are Codex acting as:

- principal software architect;
- principal Rust systems engineer;
- senior Android engineer;
- senior Windows C++/WinRT engineer;
- senior macOS Swift engineer;
- senior Linux GTK/Rust engineer;
- LLM integration engineer;
- document-processing engineer;
- application-security engineer;
- performance engineer;
- QA and release engineer;
- technical writer;
- open-source maintainer.

Build and maintain LinguaMesh.

LinguaMesh is a local-first, provider-neutral, fully native AI translation suite powered by large language models. It must offer high-quality and highly configurable text and document translation on Android, Windows, macOS, and Linux.

This document is the global project objective. Treat it as authoritative unless a later explicit user instruction overrides it.

Resolve conflicts in this order:

1. Credential protection, user privacy, source-document integrity, and prevention of data loss.
2. Functional correctness.
3. Stable cross-repository contracts.
4. Native platform behavior.
5. Translation quality and provider correctness.
6. Performance and resource efficiency.
7. Maintainability and testability.
8. Developer convenience.
9. Cosmetic preferences.

When information is missing:

- Make the safest reversible decision.
- Record it with the prefix "Assumption:".
- Record important architectural decisions in an ADR.
- Do not ask for clarification unless the missing information creates an irreversible architecture decision, a destructive operation, a legal or licensing risk, or a material security risk.
- Continue all unaffected work.
- Never fabricate completed work, successful builds, supported platforms, provider capabilities, document fidelity, benchmark results, signing status, or test results.

Do not create remote repositories, push branches, publish packages, publish releases, sign binaries, rotate credentials, or modify external systems unless the user has explicitly authorized those writes in the current task.

Local repository initialization and local code generation are allowed.

---

## 1. Product Identity

Project name:

    LinguaMesh

Tagline:

    Native, local-first LLM translation for text and documents.

License:

    MIT

Primary platforms:

- Android
- Windows
- macOS
- Linux

Not required for the first stable release:

- iOS
- Web
- browser extensions
- hosted LinguaMesh accounts
- mandatory cloud synchronization

Default UI language:

    English

Primary product model:

- Open-source public repositories.
- Bring Your Own Key.
- User-configured endpoints.
- Direct communication between the client and the provider selected by the user.
- No bundled commercial API credentials.
- No mandatory LinguaMesh relay.
- No mandatory registration.
- No default telemetry.
- Local translation history and document-job state.
- Platform-protected credential storage.

The product must never claim that an AI-generated translation is legally certified, medically validated, professionally sworn, or equivalent to expert human review.

---

## 2. Product Mission

LinguaMesh must allow users to:

1. Translate text between practically any source and target languages supported by the configured model.
2. request source-language detection.
3. receive fluent, natural and context-aware target-language output.
4. observe real streamed output rather than simulated streaming.
5. configure provider API keys, endpoints, headers and model identifiers.
6. discover provider models when the provider supports discovery.
7. add models manually when discovery is unavailable.
8. switch provider and model with one deliberate action.
9. define ordered or automatic routing profiles.
10. use local models through Ollama or OpenAI-compatible local servers.
11. translate large text using safe chunking.
12. apply glossaries, protected terms, style, tone, formality and locale preferences.
13. translate documents while retaining document structure as far as the format and selected codec allow.
14. pause, resume, retry and cancel document jobs.
15. preserve completed document segments across application restarts.
16. export output without overwriting the source.
17. use the native client UI in multiple locales.
18. understand exactly which provider will receive their content.
19. inspect usage information and cost estimates where trustworthy information is available.
20. disable translation history and use incognito translation.

Translation-language support and UI-localization support are separate concepts. A model may translate a language even when LinguaMesh does not yet have an official UI locale for that language.

---

## 3. Non-Negotiable Native Architecture

### 3.1 Prohibited shared UI frameworks

Do not use any of the following as the production application UI architecture:

- Flutter
- Tauri
- React Native
- Electron
- Qt as a shared four-platform UI
- Compose Multiplatform
- .NET MAUI
- Avalonia
- Uno Platform
- browser-first shells
- WebView-first applications
- a locally hosted web application wrapped as a desktop or mobile client

A sandboxed WebView may be used only for a narrowly scoped feature such as an OAuth authorization page or a restricted document preview, and only after an ADR explains why a native implementation is impractical.

Do not share UI code across the four platform clients.

### 3.2 Required platform UI stacks

Use these platform stacks:

Android:

- Kotlin
- Jetpack Compose
- Android platform APIs
- Kotlin coroutines and Flow
- JNI only through the generated LinguaMesh Core Android wrapper

Windows:

- modern ISO C++
- C++/WinRT
- WinUI 3
- Windows App SDK
- XAML where appropriate
- direct use of the generated LinguaMesh Core C++ wrapper
- no production C# application layer by default

macOS:

- Swift
- SwiftUI
- AppKit for high-volume editors, tables or platform capabilities where SwiftUI is insufficient
- Swift concurrency
- generated Swift wrapper around the LinguaMesh Core XCFramework

Linux:

- Rust
- GTK 4 through gtk-rs
- libadwaita where useful without making core functionality depend on GNOME-only services
- GLib/GIO platform integration
- direct Rust dependency on the LinguaMesh core crates where possible

### 3.3 Shared core

All non-UI behavior that must remain consistent across platforms belongs in a shared Rust core.

The Rust core must own:

- provider protocol adapters;
- model discovery logic;
- provider and model routing;
- translation request construction;
- prompt template versioning;
- streaming response parsing;
- retry classification;
- cancellation state;
- text chunking;
- glossary enforcement;
- protected-span processing;
- translation memory rules;
- document inspection;
- document segmentation;
- document reconstruction;
- document validation;
- document-job state;
- local structured persistence;
- typed domain errors;
- usage normalization;
- provider capability normalization;
- provider catalog processing.

The native clients must own:

- native UI;
- native navigation;
- native accessibility;
- native window and application lifecycle;
- native file picking;
- native drag-and-drop;
- native credential storage;
- native notifications;
- native background-work integration;
- native share and clipboard integration;
- native sandbox or permission handling;
- platform-local visual preferences.

Do not duplicate provider adapters or document codecs in platform repositories.

### 3.4 Embedded library model

The Rust core must be embedded as a native library.

Do not make a local daemon, localhost HTTP server, Electron process, or gRPC sidecar the default production architecture.

A local fake provider server and developer test services are allowed for testing.

An optional out-of-process document worker may be added later only when isolation measurements justify it and an ADR defines lifecycle, authentication and recovery.

---

## 4. Multi-Repository Organization

Use a federated polyrepository architecture.

The canonical repository set is:

### 4.1 linguamesh-project

Purpose:

- global project goal;
- cross-repository architecture;
- cross-repository ADRs;
- roadmap;
- release manifest;
- compatibility matrix;
- global issue and RFC templates;
- project-wide security and privacy model;
- project bootstrap scripts;
- repository synchronization scripts;
- global implementation status.

Required major files:

    AGENTS.md
    PROJECT_GOAL.md
    PLANS.md
    README.md
    LICENSE
    SECURITY.md
    PRIVACY.md
    CODE_OF_CONDUCT.md
    CONTRIBUTING.md
    ROADMAP.md
    IMPLEMENTATION_STATUS.md
    COMPATIBILITY.md
    workspace-manifest.toml
    release-manifest.toml
    docs/architecture/
    docs/adr/
    docs/rfc/
    docs/releases/
    tools/bootstrap.sh
    tools/bootstrap.ps1
    tools/check-workspace.sh
    tools/check-workspace.ps1

### 4.2 linguamesh-core

Purpose:

- Rust translation engine;
- provider adapters;
- model router;
- document engine;
- SQLite persistence;
- stable C ABI;
- protocol schemas;
- generated binding packages;
- command-line reference client;
- fake provider;
- test corpus;
- benchmark suite.

### 4.3 linguamesh-l10n

Purpose:

- canonical UI message identifiers;
- canonical English source messages;
- official translations;
- terminology guide;
- locale metadata;
- placeholder validation;
- plural and select rules;
- generators for platform-native localization resources;
- pseudo-locales;
- translation contribution workflow.

### 4.4 linguamesh-android

Purpose:

- Kotlin and Jetpack Compose Android client;
- Android platform services;
- Android packaging and distribution.

### 4.5 linguamesh-windows

Purpose:

- C++/WinRT and WinUI 3 Windows client;
- Windows platform services;
- MSIX and optional portable packaging.

### 4.6 linguamesh-macos

Purpose:

- SwiftUI and AppKit macOS client;
- macOS platform services;
- app bundle, signing and notarization workflow.

### 4.7 linguamesh-linux

Purpose:

- Rust and GTK 4 Linux client;
- Linux platform services;
- Flatpak and distribution packaging.

### 4.8 Optional future repositories

Create separate plugin repositories only after an ADR demonstrates that the plugin has independent release, licensing, binary-size or security requirements.

Possible examples:

- linguamesh-plugin-ocr
- linguamesh-plugin-pdf
- linguamesh-site

Do not create optional repositories merely to make the repository count larger.

### 4.9 Repository coordination

Do not use Git submodules by default.

Use workspace-manifest.toml and bootstrap scripts to clone or update sibling repositories.

A normal local workspace should look similar to:

    linguamesh-workspace/
    ├── linguamesh-project/
    ├── linguamesh-core/
    ├── linguamesh-l10n/
    ├── linguamesh-android/
    ├── linguamesh-windows/
    ├── linguamesh-macos/
    └── linguamesh-linux/

Every code repository must contain:

- a concise AGENTS.md;
- a REPOSITORY_ROLE.md;
- a pinned snapshot or reference revision of the global project goal;
- exact setup, format, lint, test and build commands;
- local architecture documentation;
- local implementation status;
- MIT license;
- security policy;
- contribution guide;
- third-party notices;
- release instructions.

Each repository must record which revision of the global goal it implements.

CI must detect a repository whose global-goal revision is stale or incompatible.

---

## 5. Cross-Repository Contracts and Versioning

### 5.1 Versioning

Use semantic versioning for:

- Rust core;
- native SDK artifacts;
- each platform application;
- localization bundles;
- provider catalog;
- protocol schema.

Use a separate monotonic ABI major version for the native C ABI.

A breaking ABI change requires:

1. an RFC;
2. an ADR;
3. a new ABI major version;
4. regenerated bindings;
5. client compatibility changes;
6. migration documentation;
7. cross-platform conformance tests;
8. release-manifest update.

Never let a stable client consume an unpinned core build from the main branch.

### 5.2 Release manifest

The central release-manifest.toml must identify a known-good release train:

- core source version;
- ABI version;
- protocol schema version;
- provider catalog version;
- localization version;
- Android version;
- Windows version;
- macOS version;
- Linux version;
- artifact checksums;
- minimum compatible versions;
- release status;
- known limitations.

### 5.3 Core distribution artifacts

The core release pipeline should produce:

Android:

- AAR package;
- native libraries for selected Android ABIs;
- generated Kotlin wrapper;
- JNI layer;
- Protobuf runtime integration;
- symbols for debugging.

Windows:

- native DLL;
- import library;
- stable C header;
- generated C++ RAII wrapper;
- NuGet package suitable for a C++/WinUI application;
- x64 and ARM64 artifacts where supported;
- debug symbols.

macOS:

- XCFramework;
- generated Swift wrapper;
- Swift Package binary-target metadata;
- Apple Silicon support;
- additional architectures only where supported and documented;
- debug symbols.

Linux:

- Rust crates;
- shared or static native library where required;
- C header;
- pkg-config metadata where useful;
- source archive.

Every released artifact must have:

- checksum;
- license;
- third-party notices;
- ABI version;
- protocol version;
- build metadata;
- source revision;
- SBOM where practical.

### 5.4 Compatibility negotiation

At startup, every native client must query:

- core ABI version;
- core semantic version;
- protocol schema version;
- provider catalog version;
- enabled features.

The client must fail safely and display an actionable error when the embedded core is incompatible.

Do not attempt to continue with an unknown major ABI.

---

## 6. Rust Core Repository Architecture

Use a Cargo workspace.

A recommended logical structure is:

    linguamesh-core/
    ├── AGENTS.md
    ├── REPOSITORY_ROLE.md
    ├── Cargo.toml
    ├── Cargo.lock
    ├── rust-toolchain.toml
    ├── rustfmt.toml
    ├── deny.toml
    ├── crates/
    │   ├── linguamesh-domain/
    │   ├── linguamesh-application/
    │   ├── linguamesh-engine/
    │   ├── linguamesh-provider-api/
    │   ├── linguamesh-provider-openai/
    │   ├── linguamesh-provider-anthropic/
    │   ├── linguamesh-provider-gemini/
    │   ├── linguamesh-provider-azure/
    │   ├── linguamesh-provider-ollama/
    │   ├── linguamesh-router/
    │   ├── linguamesh-translation/
    │   ├── linguamesh-documents/
    │   ├── linguamesh-storage/
    │   ├── linguamesh-ffi/
    │   ├── linguamesh-cli/
    │   └── linguamesh-testkit/
    ├── contracts/
    │   ├── proto/
    │   ├── json-schema/
    │   └── abi/
    ├── assets/
    │   ├── provider-catalog/
    │   ├── prompt-templates/
    │   └── fixtures/
    ├── bindings/
    │   ├── android/
    │   ├── windows/
    │   └── macos/
    ├── fuzz/
    ├── benches/
    ├── tests/
    ├── docs/
    └── tools/

Adjust package boundaries only when the change reduces coupling or duplication.

Do not create trivial packages containing only one small type.

### 6.1 Toolchain

Use the latest stable Rust toolchain available at project bootstrap.

Pin the exact version in rust-toolchain.toml.

Do not use nightly Rust in production unless an ADR identifies the required feature, fallback and removal plan.

Use a committed Cargo.lock for reproducible application and artifact builds.

### 6.2 Rust standards

Required practices:

- strict formatting;
- strict Clippy;
- explicit public API documentation;
- typed errors;
- immutable values by default;
- bounded channels;
- cancellation propagation;
- structured concurrency;
- no global mutable state;
- deterministic tests;
- injected clocks and ID generators where tests need determinism;
- defensive decoding of all untrusted provider and document input;
- explicit memory and size limits;
- no secret values in Debug or Display output.

Unsafe Rust is allowed only in:

- the FFI boundary;
- proven platform interop;
- a measured performance-critical implementation.

Every unsafe block must include a meaningful SAFETY comment.

Use lints that prevent unsafe operations from being hidden inside unsafe functions.

A Rust panic must never cross the FFI boundary.

### 6.3 Core domain model

Define stable domain types for at least:

- ProviderProfile
- ProviderPreset
- ProviderCapabilities
- ModelDescriptor
- ModelCapabilities
- SecretRef
- EndpointConfiguration
- RoutingProfile
- RoutingCandidate
- RoutingDecision
- TranslationRequest
- TranslationOptions
- TranslationPreset
- TranslationEvent
- TranslationResult
- Glossary
- GlossaryTerm
- ProtectedSpan
- TranslationMemoryEntry
- DocumentJob
- DocumentManifest
- DocumentSegment
- DocumentOutput
- DocumentFormat
- UsageRecord
- CostEstimate
- LocalizedError
- RetryPolicy
- CancellationState
- OperationId
- CorrelationId

Use stable identifiers rather than user-visible names as database keys.

Use BCP 47 tags for languages and locales where possible.

### 6.4 HTTP transport

Provider adapters must depend on an abstract HTTP transport.

The transport abstraction must support:

- normal requests;
- streaming responses;
- request body streaming where needed;
- cancellation;
- connection timeout;
- request timeout;
- streaming idle timeout;
- bounded response sizes;
- proxy configuration;
- custom trusted certificates when explicitly configured;
- redirect policy;
- normalized typed errors;
- test injection.

Provide a high-performance Rust transport implementation.

If a platform cannot meet system certificate, system proxy or enterprise-network requirements through the default transport, add a platform-native transport bridge behind the same interface. Do not duplicate provider logic.

Never forward authorization headers across an origin-changing redirect.

Never disable TLS verification as a convenience option.

---

## 7. Stable Native Boundary

### 7.1 Required ABI model

Expose a stable C ABI.

Do not expose:

- Rust structs;
- Rust enums;
- Rust trait objects;
- Rust strings;
- Rust allocator-owned memory without an explicit release function;
- C++ objects;
- language-runtime exceptions;
- platform-specific UI objects.

Use:

- opaque handles;
- fixed-width primitive types;
- explicit buffer structs;
- explicit ownership;
- explicit result codes;
- versioned protocol messages.

### 7.2 Command and event protocol

Use versioned Protocol Buffers for commands, events and host responses.

Every command and event envelope must include:

- protocol version;
- operation ID;
- correlation ID;
- sequence number where applicable;
- message type;
- payload;
- safe timestamp metadata where useful.

Do not serialize large document bodies through Protobuf.

Pass large data using file paths, file descriptors, duplicated platform handles, memory-mapped files or temporary files under an explicit FileLease abstraction.

### 7.3 Event-polling architecture

Do not call arbitrary Swift, Kotlin or C++ callbacks from Rust worker threads.

The core must own its asynchronous runtime and event queue.

Provide an API conceptually equivalent to:

    lm_engine_create
    lm_engine_get_version
    lm_engine_submit
    lm_engine_poll_event
    lm_engine_send_host_response
    lm_engine_cancel
    lm_engine_shutdown
    lm_engine_destroy
    lm_buffer_free

The exact signatures may differ, but they must preserve:

- opaque engine ownership;
- operation submission;
- typed event retrieval;
- bounded blocking poll with timeout;
- cancellation;
- host-service responses;
- explicit buffer release;
- clean shutdown.

Each native client must run event polling on a dedicated non-UI execution context and dispatch normalized UI updates onto the platform UI thread.

### 7.4 FFI memory safety

Requirements:

- catch panics before returning across FFI;
- validate all pointers and lengths;
- reject unsupported protocol versions;
- use UTF-8 consistently;
- provide one allocator-owned buffer-release function;
- never free client-owned memory;
- never retain borrowed memory beyond the documented call;
- provide RAII or automatic wrappers in Kotlin, C++ and Swift;
- test double-free, use-after-free, invalid length and shutdown races;
- use sanitizers in CI where supported;
- fuzz the command decoder and event decoder.

### 7.5 Streaming performance

Do not send one UI event for every individual token when the provider produces very small deltas.

The core may batch adjacent text deltas using a short, bounded interval or byte threshold while retaining low perceived latency.

Preserve event order.

Every streamed operation must terminate with exactly one terminal event:

- completed;
- cancelled;
- failed.

A malformed or prematurely closed provider stream must not be reported as completed.

---

## 8. Platform Host Services

The core must use explicit host-service requests for functionality that belongs to the operating system.

### 8.1 Secret broker

Core persistence stores only SecretRef identifiers.

When an operation needs a credential:

1. the core emits a SecretRequired event;
2. the native client resolves the SecretRef using platform secure storage;
3. the client sends a one-time ProvideSecret host response;
4. the core uses the secret only for the intended operation;
5. the core clears and zeroizes the secret as soon as practical;
6. the secret is never persisted, logged, included in diagnostics or returned in an event.

A short-lived in-memory session cache may be implemented only when:

- it is bounded;
- it uses secret-aware memory containers;
- it can be cleared;
- it is never serialized;
- its behavior is documented.

Do not preload every configured provider key into the core.

### 8.2 Platform credential storage

Android:

- protect encryption keys with Android Keystore;
- store API-key ciphertext only in app-private storage;
- never store an API key as plaintext SharedPreferences or DataStore data.

Windows:

- use Windows Credential Locker or current-user-scoped OS data protection;
- account for Credential Locker limits;
- do not use plain registry values or plain application settings.

macOS:

- use Keychain Services;
- use an application-specific service namespace;
- use appropriate access controls.

Linux:

- use Secret Service or a compatible desktop keyring;
- support session-only secrets when a secure service is unavailable;
- never silently fall back to plaintext.

When secure persistent storage is unavailable:

- display a localized warning;
- offer a session-only credential;
- keep it only in memory;
- do not claim that it has been saved.

### 8.3 File broker

The platform clients own user file selection and platform permissions.

Support a FileLease abstraction capable of representing:

- desktop file path;
- POSIX file descriptor;
- Android ParcelFileDescriptor-derived descriptor;
- duplicated Windows file handle;
- temporary app-private file;
- output destination lease.

The core must not continue using a borrowed file handle after its lease expires.

Android must use the Storage Access Framework and ContentResolver correctly.

macOS must respect App Sandbox permissions and security-scoped resources.

Linux must support XDG desktop portals where appropriate.

Windows must use supported native file pickers and package-identity behavior.

### 8.4 Platform preferences

Native clients may store UI-only preferences natively, including:

- window size;
- window position;
- last selected page;
- theme;
- UI scale preferences;
- locale;
- reduced-motion preference.

Provider profiles, routing profiles, glossaries, translation jobs and history belong to the core database.

Secrets never belong to either normal preference store or the core database.

---

## 9. Native Client Requirements

## 9.1 Android client

Use:

- Kotlin;
- Jetpack Compose;
- Material 3;
- Android architecture components only where needed;
- Kotlin coroutines;
- Flow;
- generated JNI wrapper;
- native Android localization resources generated from linguamesh-l10n;
- Android Keystore;
- Storage Access Framework;
- WorkManager;
- a foreground service for user-visible long-running work when platform rules require it.

Architecture:

- single source of truth for each screen;
- immutable UI state;
- unidirectional event flow;
- no provider HTTP code in ViewModels;
- no document parsing in Kotlin;
- no direct raw JNI calls outside the core bridge module;
- no blocking work on the main thread.

Use WorkManager for resumable scheduling and a foreground service when an active document translation must continue under Android background restrictions.

Do not claim that a job continues after process termination unless it is actually restored and driven by supported Android scheduling.

Use DataStore only for UI-local preferences, not secrets or shared business data.

Use Android Macrobenchmark and Baseline Profiles where applicable.

The minimum supported Android API must be selected in an ADR based on:

- security API requirements;
- supported-device coverage;
- Compose support;
- CI availability;
- maintenance burden.

### 9.2 Windows client

Use:

- modern C++;
- C++/WinRT;
- WinUI 3;
- Windows App SDK;
- XAML for normal views;
- native Win32 or DirectWrite integration only when profiling or capability requirements justify it;
- generated C++ LinguaMesh Core wrapper;
- RAII for all native handles and FFI buffers;
- C++ coroutines or another documented asynchronous model.

Do not use a C# production application layer by default.

Changing to C# requires:

- an ADR;
- startup, memory and runtime measurements;
- confirmation that core hot paths remain in Rust;
- a release and packaging analysis;
- explicit project approval.

Use native Windows facilities for:

- credential protection;
- file picking;
- clipboard;
- notifications;
- high-contrast mode;
- text scaling;
- system theme;
- package identity;
- application lifecycle.

Produce an MSIX release.

An optional portable unpackaged build may be added when all security, update and path behaviors are documented.

Do not block the WinUI dispatcher thread with core polling, file parsing or network operations.

### 9.3 macOS client

Use:

- current stable Swift;
- strict Swift concurrency checking;
- SwiftUI for the application shell and normal views;
- AppKit for high-volume text editing, complex tables, menu behavior or platform integration where it is measurably better;
- generated Swift LinguaMesh Core wrapper;
- Keychain Services;
- security-scoped bookmarks where persistent user-selected file access is required.

Do not access core C functions directly throughout the application. Isolate all interop in one tested module.

Use native macOS facilities for:

- menu commands;
- keyboard shortcuts;
- drag-and-drop;
- file panels;
- system appearance;
- accessibility;
- app lifecycle;
- sandbox permissions;
- recent documents where appropriate.

Prepare:

- app bundle;
- entitlements;
- hardened runtime configuration;
- signing instructions;
- notarization instructions;
- DMG or another documented distribution format.

Do not claim an artifact is signed or notarized without valid evidence.

### 9.4 Linux client

Use:

- Rust;
- GTK 4 through gtk-rs;
- GLib and GIO;
- libadwaita where useful;
- direct typed calls to the underlying Rust application layer where possible;
- the same public application behavior exercised by FFI clients.

Do not fork or reimplement core behavior merely because the Linux client is written in Rust.

Support:

- Wayland;
- X11 where practical;
- XDG base directories;
- XDG desktop portals;
- Secret Service;
- desktop notifications;
- native file dialogs or portal dialogs;
- drag-and-drop;
- system theme;
- keyboard navigation.

Primary Linux distribution packaging should include Flatpak.

Additional AppImage, DEB or RPM output may be added after reproducibility and dependency handling are documented.

GTK and other LGPL system dependencies require a documented license-compliance review.

---

## 10. Provider Hub and Model Management

Implement a Provider Hub inspired by one-click model-switching applications.

Borrow interaction concepts, not unreviewed source code.

Do not copy provider presets, icons or code from another project without license and attribution review.

### 10.1 Provider profile

A provider profile must support:

- stable profile ID;
- user-visible name;
- provider preset ID;
- adapter type;
- base endpoint;
- API-key SecretRef;
- optional organization;
- optional project;
- optional deployment;
- optional region;
- optional account identifier;
- custom non-secret headers;
- secret custom headers represented by SecretRef;
- request timeout;
- connection timeout;
- streaming idle timeout;
- proxy settings;
- TLS settings;
- enabled state;
- selected default model;
- manually entered models;
- discovered models;
- last successful health check;
- last normalized failure category;
- user notes.

Do not put a credential value in ProviderProfile.

### 10.2 Provider catalog

Create a versioned provider catalog inside linguamesh-core.

The catalog must be data driven and schema validated.

A provider preset may define:

- stable preset ID;
- display name;
- adapter type;
- endpoint template;
- authentication fields;
- model-listing strategy;
- capability hints;
- endpoint path conventions;
- localhost behavior;
- safe non-secret default headers;
- provider documentation link;
- catalog schema version.

The bundled catalog must contain no secrets.

A catalog update must never silently change:

- active provider;
- user endpoint;
- active model;
- custom headers;
- TLS policy;
- routing profile.

An optional remote catalog update must be:

- user initiated or explicitly enabled;
- signed or checksum pinned;
- schema validated;
- size limited;
- rollback capable;
- safely ignored if invalid.

### 10.3 Required provider protocol families

Before the first stable release, support:

1. Generic OpenAI-compatible Chat Completions.
2. OpenAI Responses-style operation where configured.
3. Anthropic Messages.
4. Google Gemini generate-content APIs.
5. Azure OpenAI deployment endpoints.
6. Ollama.
7. Generic local OpenAI-compatible servers, including LM Studio-style servers.

Design extension points for specialized cloud authentication and signing without coupling them to translation-domain code.

Do not hard-code current marketing model names into business logic.

### 10.4 Model discovery

Use this precedence:

1. provider-native model-listing endpoint;
2. protocol-compatible model-listing endpoint;
3. bundled catalog;
4. manually entered model ID.

Clearly identify the source of every model entry:

- discovered;
- catalog;
- manual.

A transient discovery failure must not delete a manually configured model.

### 10.5 Connection testing

A connection test must:

- be explicit;
- use the least expensive supported endpoint;
- avoid a paid generation request where possible;
- be cancellable;
- return typed diagnostics;
- never expose the API key;
- not run automatically for every profile on application startup.

### 10.6 One-click switching

The client must allow one deliberate action to switch the active provider and model.

The operation must:

- update state atomically;
- preserve the previous valid state if validation fails;
- remember each provider's last model;
- not copy credentials between providers;
- not perform an inference request merely to switch;
- show which provider will receive the next request.

---

## 11. Unified Routing

### 11.1 Routing modes

Support:

- Manual: exact provider profile and model.
- Ordered profile: user-defined ordered candidates.
- Automatic: deterministic ranking of eligible candidates.

Automatic routing must be opt-in.

### 11.2 Routing constraints

A routing profile may constrain:

- local-only operation;
- remote-provider prohibition;
- provider allowlist;
- provider denylist;
- model allowlist;
- model denylist;
- streaming support;
- context capacity;
- structured output;
- document capability;
- source or target language preferences;
- quality tier;
- latency preference;
- cost preference;
- privacy sensitivity;
- maximum estimated request size;
- explicit fallback permission.

### 11.3 Explainable routing

Every automatic routing decision must be inspectable.

Record:

- eligible candidates;
- rejected candidates;
- rejection reasons;
- ranking inputs;
- selected candidate;
- fallback candidate order.

Do not expose credentials in routing diagnostics.

### 11.4 Fallback

Fallback must be off by default for privacy-sensitive operations and document jobs.

When enabled:

- use only the user-approved fallback chain;
- inform the user that another provider may receive content;
- do not retry after cancellation;
- do not automatically retry invalid credentials on unrelated providers;
- avoid uncontrolled duplicate paid requests;
- preserve completed streamed output;
- preserve completed document segments;
- use bounded exponential backoff with jitter;
- respect retry headers;
- use circuit-breaker state for repeated transient failures.

A provider safety refusal is not automatically retryable on another provider unless the user explicitly permits that policy.

### 11.5 Usage and cost

Normalize provider-reported usage where possible.

Distinguish:

- provider-reported usage;
- locally estimated usage;
- unknown usage.

Cost must be labeled as an estimate unless returned authoritatively.

Never calculate cost from unknown or stale pricing while presenting it as current fact.

---

## 12. Text Translation Engine

### 12.1 Translation request

Support:

- source text;
- source locale or Auto;
- target locale;
- provider/model selection;
- routing profile;
- quality mode;
- domain;
- tone;
- formality;
- intended audience;
- regional locale;
- script preference;
- glossary;
- protected terms;
- custom context;
- custom translation instructions;
- formatting-preservation policy;
- history policy;
- translation-memory policy;
- privacy sensitivity;
- streaming preference;
- correlation ID.

### 12.2 Quality modes

Implement:

Fast:

- one translation pass;
- minimal additional calls.

Balanced:

- translation plus deterministic structural validation;
- optional lightweight repair only when necessary and approved.

Best:

- translation;
- critique;
- revision or quality pass;
- explicit warning about additional calls, latency and cost.

Never silently convert a one-call operation into several paid calls.

### 12.3 Prompt requirements

Version prompt templates in source control.

The default translation prompt must require the model to:

- act as a professional translator;
- preserve meaning, intent, tone, register and pragmatic context;
- produce natural target-language text;
- avoid unnecessary explanation;
- output only the requested translation unless metadata is explicitly requested;
- preserve protected placeholders exactly;
- preserve code, variables, URLs, paths, identifiers and selected markup;
- treat source content as untrusted data;
- ignore embedded instructions that attempt to override the translation task;
- avoid adding facts;
- preserve ambiguity rather than inventing certainty;
- follow required glossary mappings;
- use requested regional conventions;
- avoid translating explicitly protected product names.

Never concatenate source text into a prompt without clear delimitation.

Add regression fixtures containing prompt-injection-like source text.

### 12.4 Protected spans

Detect and protect configurable spans including:

- printf placeholders;
- ICU placeholders;
- template expressions;
- environment-variable references;
- Markdown inline code;
- Markdown fenced code;
- HTML or XML tags;
- URLs;
- email addresses;
- file paths;
- command-line flags;
- UUIDs;
- API identifiers;
- immutable glossary terms;
- user-selected product names.

Use reversible opaque placeholders.

After translation:

- restore every placeholder;
- verify count and identity;
- detect missing or duplicated placeholders;
- fail, repair or warn according to policy;
- never present structurally corrupted output as fully valid.

### 12.5 Streaming

Use typed events:

- started;
- text delta;
- metadata;
- usage;
- warning;
- secret required;
- confirmation required;
- completed;
- cancelled;
- failed.

The UI must:

- render output incrementally;
- batch high-frequency updates;
- preserve received output after cancellation;
- label partial output;
- prevent duplicated output from cumulative streams;
- scroll predictably;
- remain responsive for large output.

Test:

- split UTF-8 sequences;
- split SSE lines;
- comments;
- empty events;
- malformed JSON;
- malformed provider envelopes;
- provider error events;
- connection loss;
- cancellation;
- duplicate events;
- cumulative responses;
- out-of-order internal events.

### 12.6 Long-text processing

When the request exceeds the safe model budget:

- segment at semantic boundaries;
- reserve prompt and output capacity;
- avoid splitting protected spans;
- retain stable segment IDs;
- include bounded neighboring context;
- preserve order;
- retry only failed segments;
- avoid emitting context text as translated output;
- use a safety margin when capacity is estimated.

Do not use raw character count as a token count when an appropriate tokenizer is available.

Label approximations as estimates.

### 12.7 Glossaries

Support:

- source term;
- required target term;
- source locale;
- target locale;
- case sensitivity;
- whole-word behavior;
- immutable behavior;
- domain;
- priority;
- notes;
- enabled state.

Support CSV import and export.

Design for future TBX support.

Detect conflicting glossary rules before inference.

### 12.8 Translation memory

Provide optional local translation memory.

Cache identity must include:

- normalized source text;
- source locale;
- target locale;
- relevant translation options;
- glossary version;
- protected-span policy;
- prompt-template version;
- quality mode;
- provider/model when semantically required.

Do not reuse a cached result when relevant inputs differ.

Users must be able to:

- disable translation memory;
- inspect entries;
- export entries;
- delete individual entries;
- clear all entries.

---

## 13. Document Translation Engine

Document translation is a first-class core capability.

### 13.1 Required format roadmap

Plain and structured text:

- TXT
- Markdown
- HTML
- JSON
- CSV
- SRT
- WebVTT

Office and publication:

- DOCX
- PPTX
- XLSX
- EPUB

PDF:

- text-based PDF extraction;
- page-aware translation;
- translated PDF where reliable;
- alternative DOCX or HTML export when high-fidelity PDF reconstruction is unavailable;
- honest fidelity warnings.

OCR:

- optional plugin architecture;
- scanned PDF and image OCR may be beta;
- retain page coordinates or page references;
- never present OCR output as error free.

Do not list a format as supported merely because the file picker accepts it.

### 13.2 Document codec interface

Define a codec interface equivalent to:

    inspect(source, options)
    extract(source, options, cancellation)
    reconstruct(manifest, translated_segments, options, cancellation)
    validate(output)

A document codec must not make an LLM request directly.

The translation orchestrator invokes codecs and translation services separately.

### 13.3 Canonical pipeline

Use this sequence:

1. obtain a platform FileLease;
2. identify file type using extension, signature and content;
3. validate size and readability;
4. inspect archive or document structure safely;
5. create a manifest;
6. extract ordered translatable segments;
7. identify non-translatable content;
8. protect placeholders and structural tokens;
9. estimate the request workload;
10. obtain explicit confirmation when cost or fallback policy requires it;
11. persist a resumable job;
12. translate segments in bounded batches;
13. validate every translated segment;
14. retry only retryable failures;
15. reconstruct into a temporary output;
16. validate structural integrity;
17. atomically finalize the output;
18. produce a translation report;
19. clean temporary resources;
20. leave the source unchanged.

Never overwrite a source file by default.

An overwrite operation, if later implemented, must require a separate explicit confirmation and backup strategy.

### 13.4 Segment model

A document segment should contain:

- stable segment ID;
- document order;
- parent structure ID;
- source text;
- source locale if known;
- style reference;
- formatting reference;
- neighboring context references;
- protected spans;
- translatable flag;
- segment kind;
- page, slide, sheet, paragraph, cell or cue location;
- byte count;
- character count;
- estimated token count;
- checksum;
- state;
- retry count;
- error category.

### 13.5 Job states

Support:

- queued;
- inspecting;
- awaiting confirmation;
- ready;
- translating;
- pause requested;
- paused;
- cancel requested;
- cancelled;
- reconstructing;
- validating;
- completed;
- completed with warnings;
- failed.

Pause is permitted between segments or batches.

Do not claim an already submitted provider request has paused unless the provider operation has actually stopped.

Persist enough state to resume after an application restart.

Do not retransmit completed segments unless the user explicitly restarts the job or validation proves that the segment must be regenerated.

### 13.6 Format-specific requirements

TXT:

- detect encoding safely;
- preserve encoding where practical;
- use UTF-8 for new output when encoding is ambiguous;
- preserve line endings where practical.

Markdown:

- preserve front matter;
- preserve fenced code;
- preserve inline code;
- preserve URLs and link destinations;
- translate visible link text according to policy;
- preserve lists, headings and tables.

HTML:

- parse structurally;
- never process HTML using only regular expressions;
- translate eligible text nodes;
- optionally translate selected attributes;
- preserve tags, scripts, styles, IDs, data attributes and links;
- disable external entity resolution;
- render previews safely.

JSON:

- preserve syntax;
- preserve keys by default;
- preserve numbers, booleans and null;
- translate selected string values;
- support include and exclude path rules;
- preserve escaping.

CSV:

- preserve delimiter;
- preserve quoting;
- preserve row count;
- preserve column order;
- allow selected columns;
- avoid translating numeric and identifier columns unless selected.

SRT and WebVTT:

- preserve timestamps;
- preserve cue IDs;
- preserve ordering;
- validate cue structure;
- provide configurable subtitle line-length warnings;
- provide reading-speed warnings;
- never alter timing automatically without a dedicated option.

DOCX:

- preserve package structure;
- preserve styles;
- preserve relationships;
- preserve images;
- preserve hyperlinks;
- preserve tables;
- preserve headers and footers;
- preserve notes and non-text content;
- translate eligible paragraphs and table cells;
- minimize unnecessary text-run fragmentation;
- document tracked-change and comment behavior;
- never execute macros.

PPTX:

- preserve slides;
- preserve layouts;
- preserve themes;
- preserve images;
- preserve animations and relationships;
- preserve notes unless translation is enabled;
- translate text frames and tables;
- report possible text overflow;
- do not resize or reposition content without an explicit policy.

XLSX:

- preserve formulas;
- preserve numbers;
- preserve date values;
- preserve cell formatting;
- preserve charts;
- preserve workbook relationships;
- translate selected string cells;
- optionally translate selected comments;
- never translate formulas;
- do not translate worksheet names by default;
- support sheet and range selection.

EPUB:

- preserve package metadata;
- preserve manifest;
- preserve spine;
- preserve navigation;
- preserve resources;
- preserve CSS;
- preserve internal links;
- translate eligible HTML text;
- update language metadata for the output;
- validate the final EPUB archive.

PDF:

- distinguish text pages from image-only pages;
- preserve page association;
- preserve extraction coordinates where available;
- report uncertain reading order;
- do not promise pixel-identical reconstruction;
- provide an alternative structured output when direct reconstruction is unreliable;
- retain page-level warnings.

### 13.7 Archive and parser security

For ZIP-based formats:

- reject path traversal;
- reject absolute paths;
- reject invalid normalized paths;
- enforce compressed-size limits;
- enforce uncompressed-size limits;
- enforce file-count limits;
- enforce per-entry limits;
- detect suspicious compression ratios;
- use isolated temporary directories;
- never extract directly into shared user directories;
- clean temporary data on success, failure and cancellation;
- preserve unknown package parts without executing them.

For XML:

- disable external entities;
- disable external DTD resolution;
- limit nesting depth;
- limit node count;
- limit attribute size;
- limit text size.

Reject or clearly classify:

- encrypted documents;
- password-protected documents;
- corrupted archives;
- unsupported macro-enabled files;
- unsupported digital-signature scenarios.

Do not silently strip macros, signatures or protected content.

### 13.8 Output

Default naming:

    <original-base-name>.<target-bcp47-tag>.<extension>

Resolve collisions using a deterministic suffix.

Generate a translation report containing:

- source identifier;
- output identifier;
- source and target locales;
- provider and model;
- routing decision;
- translation preset;
- glossary version;
- application version;
- core version;
- prompt-template version;
- segment counts;
- completed count;
- skipped count;
- retried count;
- failed count;
- warnings;
- provider-reported or estimated usage;
- start time;
- completion time.

Do not place API keys or unnecessary full source text in reports.

---

## 14. Native User Experience

Required primary areas:

1. Onboarding
2. Text Translation
3. Document Translation
4. Providers and Models
5. Routing Profiles
6. Translation Presets
7. Glossaries
8. Translation History
9. Translation Memory
10. Settings
11. Diagnostics
12. Privacy
13. Open-Source Licenses
14. About

### 14.1 Text workspace

Provide:

- source-language selector with Auto;
- target-language selector;
- language swap;
- source editor;
- streamed result editor;
- provider/model selector;
- routing-profile selector;
- quality selector;
- glossary selector;
- tone;
- formality;
- domain;
- translate;
- stop;
- retry;
- copy;
- clear;
- export;
- partial-output indicator;
- provider identity;
- usage information;
- localized typed errors;
- character count;
- estimated token count where useful.

For large desktop text, use platform-native high-performance text controls when normal declarative controls fail established performance budgets.

### 14.2 Document workspace

Provide:

- file picker;
- desktop drag-and-drop;
- Android document picker;
- file inspection summary;
- format warnings;
- size warnings;
- source and target locales;
- output format;
- output location;
- provider/model or routing profile;
- glossary;
- preset;
- workload estimate;
- explicit fallback status;
- queue;
- per-job progress;
- per-file progress;
- pause;
- resume;
- cancel;
- retry;
- failure details;
- output-open action;
- translation report.

### 14.3 Platform conventions

Android:

- touch-friendly layout;
- adaptive navigation;
- correct back behavior;
- safe-area and keyboard handling;
- no desktop-only interactions.

Desktop:

- native menu bar or application menu behavior;
- keyboard shortcuts;
- resizable panes;
- drag-and-drop;
- context menus;
- native file dialogs;
- system clipboard behavior;
- focus restoration;
- accessible minimum window size.

### 14.4 Themes

Support:

- system;
- light;
- dark;
- high contrast where supported;
- reduced motion;
- text scaling;
- native accent behavior where practical.

---

## 15. Localization

The linguamesh-l10n repository is the canonical localization source.

### 15.1 Source format

Create a typed, versioned, platform-neutral message schema.

Every message must include:

- stable key;
- canonical English value;
- description;
- placeholder definitions;
- plural or select variants;
- platform applicability;
- accessibility context where relevant;
- status;
- source revision.

Support platform-specific messages when native UI conventions require different wording.

### 15.2 Generated resources

Generate:

Android:

- strings.xml;
- plurals;
- typed access helpers where useful.

Windows:

- RESW or the current supported native resource format;
- generated identifiers.

macOS:

- XCStrings or the current supported String Catalog format;
- generated identifiers.

Linux:

- PO and MO resources;
- gettext integration;
- generated key validation.

Generated resources may be committed when this improves reproducibility, but CI must verify that they match the canonical source.

### 15.3 Runtime switching

All clients must support changing the UI locale without losing active source text or document-job state.

A full process restart must not be the only supported locale-switch mechanism.

Use a typed localization abstraction when a platform's default API cannot reload resources safely at runtime.

### 15.4 Required official locale packs

Before 1.0, include at least:

- English
- Simplified Chinese
- Traditional Chinese
- Spanish
- French
- German
- Japanese
- Korean
- Portuguese for Brazil
- Russian
- Arabic
- Hindi

Use English as fallback.

Support right-to-left layout.

Use BCP 47 identifiers.

Use locale-aware:

- dates;
- times;
- numbers;
- percentages;
- file sizes;
- pluralization;
- language names.

Do not construct sentences by concatenating independently translated fragments.

### 15.5 Community localization

Design a data-only community locale-pack format.

It must:

- contain no executable code;
- declare locale and direction;
- declare compatibility;
- validate against known keys;
- validate placeholders;
- fall back to English;
- be removable;
- not overwrite the canonical English source;
- identify machine-generated draft translations.

Do not describe machine-generated UI text as professionally reviewed.

---

## 16. Accessibility

Target applicable WCAG 2.2 AA principles.

All native clients must address:

- screen-reader semantics;
- icon labels;
- keyboard-only desktop use;
- logical focus order;
- visible focus;
- text scaling;
- high contrast;
- large touch targets;
- status announcements;
- accessible progress;
- accessible errors;
- RTL;
- reduced motion;
- non-color state indicators.

Use platform-native accessibility inspection tools.

Automated accessibility checks are required but do not replace manual review.

---

## 17. Persistence

The Rust core owns the main SQLite database.

Suggested logical storage includes:

- schema_metadata
- app_domain_settings
- provider_profiles
- model_descriptors
- active_model_selection
- routing_profiles
- routing_candidates
- translation_presets
- glossaries
- glossary_terms
- translation_history
- translation_memory
- document_jobs
- document_segments
- document_outputs
- usage_records
- provider_health_state

Never store actual credentials in SQLite.

Use explicit schema migrations.

Test migrations from every supported prior schema.

Use transactions for multi-record changes.

Use stable IDs.

Use WAL or another documented SQLite mode selected through measurement and platform validation.

Provide user controls for:

- history off;
- incognito mode;
- clear history;
- clear translation memory;
- delete provider;
- delete document-job metadata;
- delete temporary files;
- export non-secret settings;
- reset local data.

Do not claim database encryption at rest unless an implemented and tested encryption system exists.

---

## 18. Privacy and Security

Create and maintain:

- threat model;
- privacy model;
- data-flow diagram;
- trust-boundary diagram;
- secure-coding checklist;
- incident-response guidance.

Threats include:

- API-key leakage;
- log leakage;
- malicious custom endpoints;
- provider redirects;
- prompt injection inside source content;
- malicious model output;
- ZIP bombs;
- path traversal;
- XML external entities;
- parser resource exhaustion;
- malformed SSE;
- malformed Protobuf;
- oversized provider responses;
- corrupted reconstruction;
- insecure temporary files;
- local database disclosure;
- clipboard exposure;
- crash-report leakage;
- automatic fallback data disclosure;
- remote catalog tampering;
- malicious locale packs;
- dependency compromise;
- FFI memory corruption;
- use-after-free;
- stale native core artifacts.

Security requirements:

- telemetry off by default;
- no translation content in telemetry;
- no keys in telemetry;
- no keys in logs;
- no content logging in release builds;
- redacted diagnostics;
- explicit provider identity before transmission;
- HTTPS for remote endpoints;
- HTTP permitted for loopback endpoints;
- explicit warning and confirmation for non-loopback HTTP;
- no credential-bearing cross-origin redirects;
- no global TLS-verification bypass;
- bounded response sizes;
- cancellable network requests;
- secure temporary directories;
- cleanup after failures;
- no arbitrary remote HTML in a privileged context;
- no execution of provider output;
- no executable locale packs;
- secret scanning in every repository;
- dependency and license scanning;
- explicit remote-provider fallback consent.

Source text must be treated as untrusted data, not instructions.

---

## 19. Error Model

Define typed, localizable error categories:

- authentication;
- authorization;
- quota exhausted;
- rate limited;
- invalid endpoint;
- DNS failure;
- TLS failure;
- proxy failure;
- network unavailable;
- timeout;
- stream interrupted;
- model unavailable;
- unsupported capability;
- context limit exceeded;
- malformed provider response;
- provider refusal;
- cancellation;
- invalid configuration;
- secret unavailable;
- secure storage unavailable;
- ABI incompatible;
- protocol incompatible;
- database migration failed;
- document unreadable;
- document encrypted;
- document corrupt;
- unsupported format;
- extraction failed;
- segment validation failed;
- reconstruction failed;
- output validation failed;
- output write failed;
- insufficient disk space;
- invalid imported data;
- internal failure.

Preserve safe technical context.

Do not expose:

- API keys;
- authorization headers;
- cookies;
- signed query strings;
- source-document content unless explicitly included by the user in a diagnostic export.

Every user-facing error should provide an actionable next step when possible.

---

## 20. Performance Requirements

High performance must be measured, not assumed.

### 20.1 Core performance principles

- no unbounded channels;
- no unbounded response buffering;
- no whole-document loading when streaming is possible;
- bounded concurrency;
- cancellation propagation;
- incremental parsing;
- incremental reconstruction where possible;
- efficient UTF-8 handling;
- avoid unnecessary string copies;
- use file handles rather than transferring large buffers through FFI;
- use memory mapping only when safe and measured;
- batch small stream events;
- keep provider and document work off UI threads;
- use release-mode benchmarks;
- profile before adding unsafe optimization.

### 20.2 UI performance

Normal user interaction should target the display refresh rate.

No UI-thread operation should perform:

- network I/O;
- database migration;
- document extraction;
- document reconstruction;
- tokenization;
- provider stream parsing;
- raw event polling.

Establish and document platform-specific reference hardware and budgets for:

- cold startup;
- warm startup;
- idle memory;
- provider-profile loading;
- first visible stream delta after the core emits it;
- sustained streaming;
- large-text editing;
- document inspection;
- cancellation latency;
- document reconstruction;
- application shutdown;
- job restoration.

A significant performance regression against an established baseline must fail or warn in CI according to the documented policy.

### 20.3 Platform measurement

Android:

- Macrobenchmark;
- startup benchmark;
- Baseline Profiles;
- frame timing;
- memory profiling.

Windows:

- ETW;
- Windows Performance Recorder and Analyzer;
- Visual Studio profiling;
- native heap diagnostics.

macOS:

- Instruments;
- signposts;
- XCTest metrics;
- memory graph.

Linux:

- Criterion for core;
- perf;
- hyperfine;
- Valgrind or sanitizers where useful;
- GTK frame and main-loop diagnostics.

Core:

- Criterion benchmarks;
- allocator metrics where necessary;
- flame graphs;
- throughput and memory tests.

Never publish invented performance numbers.

---

## 21. Testing Strategy

### 21.1 Rust unit and property tests

Test:

- routing;
- candidate filtering;
- request construction;
- prompt delimitation;
- protected spans;
- glossary rules;
- token budgeting;
- text chunking;
- retry classification;
- cancellation;
- usage normalization;
- translation-memory identity;
- file naming;
- document ordering;
- migrations;
- error mapping;
- protocol versioning.

Use property tests for structural invariants where appropriate.

### 21.2 Provider contract tests

Provide a local fake provider.

Test:

- model discovery;
- normal responses;
- SSE;
- newline-delimited streams;
- fragmented lines;
- split UTF-8;
- malformed events;
- provider error envelopes;
- rate limits;
- retry headers;
- timeouts;
- disconnects;
- cancellation;
- cumulative output;
- incremental output;
- usage events;
- response-size limits.

Normal CI must not require paid provider credentials.

Live-provider tests must be opt-in and excluded from default CI.

### 21.3 FFI tests

Test:

- ABI version negotiation;
- invalid pointers;
- invalid lengths;
- incompatible protocol versions;
- buffer ownership;
- repeated shutdown;
- cancellation races;
- event polling during shutdown;
- panic containment;
- concurrent operations;
- host-response ordering;
- secret request flow;
- file-lease expiration.

Use:

- sanitizers;
- fuzzing;
- memory checkers;
- ABI compatibility checks.

### 21.4 Document tests

Maintain small legally redistributable fixtures.

Test every supported format for:

- inspection;
- extraction;
- segment ordering;
- protected spans;
- reconstruction;
- structural validation;
- source preservation;
- collision-safe output;
- cancellation;
- pause and resume;
- process-restart recovery;
- malformed input;
- path traversal;
- XML entity attacks;
- compression bombs;
- parser limits.

Use structural assertions instead of byte equality when metadata is nondeterministic.

### 21.5 Native client tests

Android:

- Kotlin unit tests;
- Compose UI tests;
- instrumentation tests;
- JNI bridge tests;
- WorkManager restoration tests;
- accessibility tests;
- macrobenchmarks.

Windows:

- native unit tests;
- core-wrapper tests;
- WinUI view-model tests;
- UI automation;
- high-contrast tests;
- keyboard tests;
- packaging smoke tests.

macOS:

- XCTest;
- XCUITest;
- Swift concurrency tests;
- core-wrapper tests;
- VoiceOver-oriented checks;
- sandbox and bookmark tests;
- package smoke tests.

Linux:

- Rust tests;
- GTK component tests;
- headless or virtual-display UI tests;
- portal abstraction tests;
- Wayland/X11 smoke tests;
- Flatpak smoke tests.

### 21.6 Cross-repository conformance

Create shared behavior scenarios that every client executes against the same fake provider and compatible core release.

Test at least:

- first provider configuration;
- streamed translation;
- cancellation;
- invalid key;
- one-click model switch;
- local model;
- glossary enforcement;
- document job;
- job restoration;
- locale switching;
- RTL;
- incognito mode;
- incompatible core detection.

---

## 22. Continuous Integration

Every repository must have its own GitHub Actions workflows.

### 22.1 Project repository CI

Validate:

- workspace manifest;
- release manifest;
- known repository set;
- global-goal revision;
- compatibility matrix;
- documentation links;
- release checksums;
- cross-repository status.

### 22.2 Core CI

Run:

- formatting;
- Clippy;
- unit tests;
- property tests;
- integration tests;
- fake-provider tests;
- document tests;
- migration tests;
- ABI tests;
- fuzz smoke tests;
- license scan;
- dependency vulnerability scan;
- secret scan;
- Android artifact build;
- Windows artifact build;
- macOS artifact build;
- Linux artifact build.

### 22.3 Client CI

Each client must run:

- formatting;
- static analysis;
- unit tests;
- UI tests appropriate to the platform;
- localization validation;
- core compatibility check;
- release build;
- packaging smoke test;
- dependency/license review;
- secret scan.

### 22.4 Cross-repository CI

Use scheduled or explicitly triggered integration workflows to validate the versions in release-manifest.toml.

Do not automatically test arbitrary untrusted pull-request code using privileged credentials.

Do not make production credentials available to public-fork workflows.

---

## 23. Release Engineering

Prepare release flows for:

Android:

- APK;
- AAB;
- checksums;
- GitHub Release;
- optional future F-Droid metadata.

Windows:

- MSIX;
- optional portable package;
- checksums;
- symbol package.

macOS:

- application bundle;
- DMG or documented alternative;
- signing;
- notarization;
- checksums.

Linux:

- Flatpak;
- source archive;
- optional AppImage, DEB or RPM;
- checksums.

Core:

- source tag;
- AAR;
- Windows native package;
- XCFramework;
- Linux crate or library;
- headers;
- symbols;
- checksums;
- SBOM;
- third-party notices.

Localization:

- source bundle;
- generated platform bundles;
- compatibility metadata.

Use semantic versions.

Maintain human-readable changelogs.

Do not fabricate signatures or notarization.

Unsigned artifacts must be labeled clearly.

Do not publish prerelease artifacts as stable.

---

## 24. Open-Source Requirements

Every first-party repository is MIT licensed.

Maintain, where applicable:

- README.md
- LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- PRIVACY.md
- CHANGELOG.md
- THIRD_PARTY_NOTICES.md
- AGENTS.md
- REPOSITORY_ROLE.md
- release documentation
- testing documentation
- architecture documentation
- issue templates
- pull-request template
- CODEOWNERS

The central project documentation must explain:

- repository topology;
- local workspace bootstrap;
- supported platforms;
- provider architecture;
- document support;
- fidelity limitations;
- privacy model;
- secure storage model;
- ABI model;
- version compatibility;
- release train;
- how to add a provider preset;
- how to add a provider adapter;
- how to add a document codec;
- how to add a locale;
- how to report a vulnerability.

Do not use provider trademarks or logos in a way that implies endorsement.

Avoid dependencies with:

- AGPL;
- SSPL;
- non-commercial clauses;
- source-available restrictions;
- incompatible static-linking obligations.

GPL or LGPL dependencies require an explicit compliance review.

System GTK dependencies may be accepted when distribution obligations are documented.

---

## 25. Codex Repository Protocol

At the beginning of every task:

1. read the applicable AGENTS.md chain;
2. read REPOSITORY_ROLE.md;
3. read the pinned global goal;
4. inspect git status;
5. inspect current implementation status;
6. preserve user-authored changes;
7. identify the smallest valid vertical slice;
8. create or update an ExecPlan when work is multi-stage, cross-repository, migration-heavy, security-sensitive or likely to span several sessions;
9. record assumptions;
10. implement production code and tests;
11. run relevant validation commands;
12. update documentation;
13. update implementation status with evidence;
14. report exactly what changed and what was actually run.

Do not:

- discard unrelated user work;
- use destructive Git commands without authorization;
- force push;
- modify external repositories without authorization;
- commit or push unless explicitly requested;
- expose credentials;
- hide failing tests;
- disable security checks to obtain a passing build;
- replace real behavior with placeholders;
- mark a platform complete when only scaffolded;
- mark a document format complete when only extraction or only reconstruction works;
- claim local platform builds that were not run;
- copy unreviewed generated code from unrelated projects;
- add a production dependency without maintenance and license review.

For cross-repository changes:

1. create or reference one central change identifier;
2. define the compatibility transition;
3. update core contracts first when required;
4. release or build a prerelease SDK;
5. update clients;
6. run conformance tests;
7. update the central release manifest;
8. document rollback.

Use subagents only for clearly independent workstreams.

Do not merge subagent output blindly. Review and validate it.

---

## 26. Definition of Done

A feature is complete only when:

1. it is implemented rather than merely scaffolded;
2. shared behavior resides in the correct repository;
3. the native client follows platform conventions;
4. errors are typed and localized;
5. cancellation works;
6. secrets are protected;
7. privacy impact is reviewed;
8. persistence migrations exist when needed;
9. tests cover important behavior;
10. relevant documentation is updated;
11. platform build or CI evidence exists;
12. source documents cannot be overwritten accidentally;
13. no known critical failure is hidden behind success UI;
14. performance-sensitive paths have measurement evidence;
15. cross-repository compatibility is recorded;
16. implementation status contains evidence rather than unsupported checkboxes.

---

## 27. Delivery Milestones

### Milestone 0 — Project and repository foundation

Deliver locally:

- linguamesh-project;
- workspace manifest;
- release-manifest schema;
- global goal;
- AGENTS.md;
- PLANS.md;
- repository-role templates;
- global ADR structure;
- threat-model skeleton;
- bootstrap scripts;
- exact proposed gh commands;
- local sibling-repository layout.

Do not create remote repositories unless authorized.

### Milestone 1 — Rust core text-translation vertical slice

Deliver:

- Cargo workspace;
- domain model;
- engine;
- stable command and event protocol;
- C ABI skeleton;
- generic OpenAI-compatible adapter;
- fake streaming provider;
- model listing;
- manual model entry;
- real SSE parsing;
- cancellation;
- typed errors;
- SQLite migrations;
- CLI reference client;
- provider catalog;
- unit and integration tests.

The CLI must be able to:

- configure a fake or OpenAI-compatible endpoint;
- list or set a model;
- submit text;
- display streamed output;
- cancel;
- receive typed errors.

No paid key may be required.

### Milestone 2 — Native SDK artifacts

Deliver:

- Android AAR and Kotlin wrapper;
- Windows native package and C++ wrapper;
- macOS XCFramework and Swift wrapper;
- Linux crate integration;
- ABI negotiation;
- event polling;
- host secret flow;
- file-lease abstraction;
- conformance tests;
- artifact checksums.

### Milestone 3 — Four native client vertical slices

Each native client must support:

- launch;
- onboarding;
- provider profile creation;
- secure credential storage;
- fake-provider connection;
- model selection;
- text translation;
- streamed output;
- cancellation;
- typed localized errors;
- active provider/model switching;
- theme;
- locale switching;
- diagnostics.

A scaffold or static mock does not satisfy this milestone.

### Milestone 4 — Provider Hub and routing

Deliver:

- required provider protocol families;
- data-driven provider presets;
- model discovery;
- local-model support;
- one-click switching;
- routing profiles;
- explicit fallback consent;
- usage normalization;
- provider diagnostics;
- import/export without secrets.

### Milestone 5 — Translation quality

Deliver:

- glossaries;
- protected spans;
- long-text chunking;
- translation presets;
- Fast, Balanced and Best modes;
- translation memory;
- history;
- incognito mode;
- prompt-version regression suite.

### Milestone 6 — Document translation

Implement incrementally:

1. TXT and Markdown.
2. HTML, JSON, CSV, SRT and WebVTT.
3. DOCX.
4. PPTX and XLSX.
5. EPUB.
6. text-based PDF.
7. optional OCR plugin.

For every completed format:

- extraction works;
- reconstruction works;
- validation works;
- source remains unchanged;
- fixture tests pass;
- limitations are documented;
- UI advertises the actual support level.

### Milestone 7 — Localization and accessibility

Deliver:

- linguamesh-l10n;
- platform generators;
- required locale packs;
- runtime locale switching;
- RTL;
- pseudo-localization;
- placeholder validation;
- accessibility review;
- keyboard support;
- native screen-reader checks.

### Milestone 8 — Hardening and stable release

Deliver:

- completed threat model;
- privacy model;
- performance baselines;
- migration tests;
- fuzzing;
- parser hardening;
- cross-repository CI;
- release packaging;
- checksums;
- SBOM;
- third-party notices;
- stable release manifest;
- verified documentation.

---

## 28. Mandatory Acceptance Scenarios

### Scenario 1 — Core CLI translation

The Rust CLI connects to the fake provider, selects a model, streams text, displays deltas and completes successfully.

### Scenario 2 — Native client translation

Each of the four native clients performs the same fake-provider translation using a compatible core release.

### Scenario 3 — Secure provider profile

A user stores an API key through native secure storage. The core persists only a SecretRef. No log, database row or diagnostic file contains the key.

### Scenario 4 — Local model

A user selects a loopback Ollama or compatible endpoint and translates without sending content to a remote provider.

### Scenario 5 — One-click switch

A user switches provider and model. The next request uses the new selection, while the old provider secret remains isolated.

### Scenario 6 — Cancellation

A user cancels a streamed request. The core cancels the transport where supported, retains partial output, emits one cancelled terminal event and does not retry.

### Scenario 7 — Routing fallback

A user explicitly enables fallback. A retryable primary failure occurs. The approved fallback is selected, the decision is recorded and no unapproved provider receives content.

### Scenario 8 — Invalid credential

A provider returns an authentication failure. The client displays an actionable localized error without exposing the key.

### Scenario 9 — Glossary and protected terms

Required terms and placeholders survive translation and structural validation.

### Scenario 10 — DOCX translation

A DOCX containing paragraphs, tables, images and links is translated. The output opens, non-text content remains, eligible text is translated and the source is unchanged.

### Scenario 11 — Spreadsheet safety

Selected XLSX string cells are translated. Formulas, numbers, dates and unselected cells remain unchanged.

### Scenario 12 — Interrupted job

A document job is interrupted. On restart, it restores completed segments and resumes from incomplete work.

### Scenario 13 — RTL

The UI switches to Arabic. Layout, focus, menus, controls and text direction remain usable.

### Scenario 14 — Incognito mode

Translation succeeds without persisting source text, result text, history or translation-memory data.

### Scenario 15 — Malicious archive

A traversal or decompression-bomb fixture is rejected without writing outside the temporary workspace.

### Scenario 16 — Core incompatibility

A client detects an incompatible ABI and refuses to continue with a clear error rather than crashing.

### Scenario 17 — Offline behavior

A remote provider request fails promptly when offline. Source text and job state remain intact.

### Scenario 18 — Output safety

No document workflow overwrites the source by default, including failure and cancellation paths.

### Scenario 19 — Clean bootstrap

A contributor follows documented bootstrap commands and obtains reproducible core and supported-host validation without commercial credentials.

### Scenario 20 — Stable release train

The central release manifest identifies compatible, tested versions of the core, localization bundle and all four clients.

---

## 29. Initial Execution Instruction

Begin implementation now.

First determine:

- current directory;
- existing repositories;
- current git status;
- host operating system;
- available toolchains;
- whether remote repository creation has been explicitly authorized.

If no LinguaMesh repositories exist:

1. create a local linguamesh-workspace directory;
2. initialize linguamesh-project locally;
3. save this goal as PROJECT_GOAL.md;
4. create a concise AGENTS.md;
5. create PLANS.md;
6. create workspace-manifest.toml;
7. create release-manifest.toml schema;
8. create architecture and ADR directories;
9. create bootstrap scripts;
10. initialize the six sibling implementation repositories locally;
11. add MIT licenses and repository-role files;
12. add a pinned global-goal snapshot to each repository;
13. create initial CI workflows;
14. implement Milestone 1 in linguamesh-core;
15. run formatting, linting and tests;
16. demonstrate the fake-provider streamed translation through the CLI;
17. update implementation status with exact commands and results.

After the core vertical slice:

1. define the stable ABI;
2. generate native SDK wrappers;
3. scaffold buildable native clients;
4. implement the fake-provider text-translation slice in every platform client;
5. build locally only for toolchains available on the host;
6. rely on platform CI for unavailable platforms;
7. never claim an unavailable local build was run;
8. continue through the delivery milestones.

If existing LinguaMesh work is present:

1. preserve all user changes;
2. compare the current architecture to this goal;
3. create a gap analysis;
4. identify shared UI framework code that must be replaced;
5. create a staged native migration plan;
6. preserve working behavior during migration;
7. implement the smallest high-value vertical slice;
8. do not delete the old implementation until native replacement behavior and migration evidence exist.

If remote repository creation is not authorized:

- do not call gh repo create;
- create docs/GITHUB_BOOTSTRAP.md containing exact proposed gh commands;
- continue all local implementation work.

If remote repository creation is authorized:

- create public repositories under the authorized owner;
- use the exact canonical repository names;
- apply the MIT license;
- set useful descriptions;
- use main as the default branch;
- do not publish empty repositories when a local initial commit can be prepared first.

The first verified checkpoint is complete only when the Rust CLI performs a real streamed translation against the local fake provider, supports cancellation, stores no credential in plaintext, and passes automated tests.

The project is not complete until every mandatory acceptance scenario passes and the central release manifest references compatible stable releases of all required repositories.
