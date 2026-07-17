# Architecture Overview

LinguaMesh is a federated polyrepository suite with one provider-neutral Rust core and four independent native clients.

```text
Android Compose     Windows WinUI     macOS SwiftUI     Linux GTK 4
       |                  |                 |                 |
       +------ generated/native core boundary or Rust API ----+
                                  |
             domain, routing, translation, documents,
             persistence, providers, protocol, validation
                                  |
                provider transport and platform brokers
```

The clients own UI, lifecycle, accessibility, secure credential storage, file selection, permissions, notifications, clipboard, and platform preferences. The core owns every behavior that must remain consistent: request construction, provider adapters, routing, streaming, cancellation, text quality rules, document codecs, typed errors, SQLite state, and compatibility contracts.

The production design embeds the core as a native library. A daemon, localhost API, WebView shell, or shared cross-platform UI is not the default architecture. Android uses Kotlin and Jetpack Compose; Windows uses ISO C++, C++/WinRT, and WinUI 3; macOS uses SwiftUI with AppKit where justified; Linux uses Rust and GTK 4.

Credentials cross a just-in-time host-service boundary as one-operation secrets and are never normal domain data. Large document bodies cross through a versioned `FileLease`, not protocol-message buffers. Provider and document input is untrusted and bounded.

See the linked architecture documents for contract details. Durable changes require an ADR, and compatibility-breaking proposals require an RFC before implementation.
