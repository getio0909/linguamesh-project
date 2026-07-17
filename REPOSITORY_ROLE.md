# Repository Role

`linguamesh-project` is the authoritative coordination repository for LinguaMesh. It owns:

- the global goal, roadmap, architecture, ADRs, RFCs, and project policies;
- the canonical repository set and local-workspace bootstrap process;
- ABI, protocol, provider-catalog, localization, and client compatibility records;
- release-train manifests, release evidence, and cross-repository status.

It does not own production provider adapters, document codecs, native SDK implementations, localization data, or platform UI code. Those changes belong in the corresponding sibling repository.

Before project work, read `AGENTS.md`, `PROJECT_GOAL.md`, `PLANS.md`, and `IMPLEMENTATION_STATUS.md`; preserve unrelated changes; and update manifests only with evidence from compatible revisions.

