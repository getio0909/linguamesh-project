# Repository Topology

The workspace is a federated polyrepository without Git submodules. `workspace-manifest.toml` is the canonical inventory; sibling directories share one parent.

```text
linguamesh-workspace/
├── linguamesh-project/
├── linguamesh-core/
├── linguamesh-l10n/
├── linguamesh-android/
├── linguamesh-windows/
├── linguamesh-macos/
└── linguamesh-linux/
```

`linguamesh-project` owns policy, architecture, compatibility, and release coordination. `linguamesh-core` owns shared non-UI behavior and SDK artifacts. `linguamesh-l10n` owns canonical message data and native resource generation. Each client repository owns only its native application and platform services.

Cross-repository changes use a central change identifier, define the compatibility transition, update core contracts first, validate generated SDKs and clients, and update `release-manifest.toml` only after conformance evidence exists. Every code repository pins the global-goal revision it implements.

Run `tools/bootstrap.sh` to clone missing siblings without replacing existing directories. Run `tools/check-workspace.sh --require-repositories` when validating a complete local workspace.

