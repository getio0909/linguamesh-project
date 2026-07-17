# Native Boundary

The shared core exposes a stable C ABI to Android, Windows, and macOS; Linux calls the same Rust application behavior directly where possible. The ABI uses opaque handles, fixed-width primitives, explicit buffer ownership, result codes, and versioned Protocol Buffer envelopes. Rust structs, allocator details, panics, exceptions, and UI objects never cross the boundary.

Commands and events carry protocol version, operation ID, correlation ID, message type, and ordered sequence metadata. Large files use a `FileLease` rather than protocol payloads. The core owns its asynchronous runtime and a bounded event queue. Clients poll from a dedicated non-UI context and marshal UI updates to the native UI thread.

The conceptual lifecycle is create, query version, submit, poll event, send host response, cancel, shut down, destroy, and free buffers. Every operation emits exactly one completed, cancelled, or failed terminal event. Cancellation retains and labels partial output; malformed or truncated streams fail.

All pointers, lengths, protocol versions, ownership transitions, shutdown races, and panic paths require tests. Kotlin, C++, and Swift wrappers provide automatic ownership. Startup rejects unknown ABI majors and displays an actionable compatibility error.
