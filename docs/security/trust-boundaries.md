# Trust-Boundary Diagram

```text
[User and native UI]
        |
        | versioned commands, events, host requests
        v
[Embedded Rust core]
   |          |           |
   |          |           +-- [Untrusted documents and generated output]
   |          +-------------- [Local database and private temporary storage]
   +------------------------- [Network transport]
                                  |
                                  +-- [Loopback provider]
                                  +-- [Remote provider and public network]

[Build source] -- [CI boundary] -- [artifact/signing/release systems]
```

The native/client boundary is memory- and version-sensitive. It uses opaque handles, explicit ownership, bounded polling, protocol negotiation, and panic containment. Platform host services are trusted only for the granted secret or file operation.

The parser boundary treats every byte as hostile and enforces type, size, depth, count, path, and time limits. The network boundary validates TLS and origins and never forwards authorization across an origin change. The CI boundary gives untrusted pull requests no production credentials or privileged publication permissions.

Every new provider, parser, locale pack, catalog update, platform permission, telemetry path, or release service must update this model before release.
