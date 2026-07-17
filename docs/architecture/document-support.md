# Document Support and Fidelity

A format is supported only after inspection, extraction, translation orchestration, reconstruction, output validation, source-preservation tests, cancellation/recovery tests, security fixtures, and native UI integration all pass.

## Canonical pipeline

The platform grants a bounded `FileLease`. The core verifies type, size, readability, archive structure, and parser limits; creates a manifest with stable ordered segment IDs; protects structural spans; persists resumable work; translates bounded batches; reconstructs to a temporary destination; validates; and atomically finalizes a distinct output. The source is never overwritten by default.

Codecs expose `inspect`, `extract`, `reconstruct`, and `validate`; they never make model requests. ZIP-based formats reject traversal, absolute paths, suspicious compression, excessive entries, and resource-limit violations. XML processing disables external entities and DTD resolution.

## Delivery levels

The roadmap proceeds through TXT/Markdown; HTML/JSON/CSV/subtitles; DOCX; PPTX/XLSX; EPUB; and text-based PDF. OCR remains an optional beta plugin. `IMPLEMENTATION_STATUS.md` is the authoritative record of what actually works.

PDF reading order and reconstruction may be uncertain; direct translation must not be advertised as pixel-identical. The product should offer structured HTML or DOCX output when reliable PDF reconstruction is unavailable. Office formats preserve relationships and non-text assets but must disclose limitations for macros, signatures, tracked changes, comments, animation, and text overflow.
