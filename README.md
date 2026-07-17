# LinguaMesh

Native, local-first LLM translation for text and documents.

This repository coordinates the LinguaMesh polyrepository workspace. It owns the project-wide architecture, policies, compatibility records, release train, and workspace automation; application and shared-core source code live in sibling repositories.

## Repository topology

| Repository | Responsibility |
| --- | --- |
| `linguamesh-project` | Architecture, policy, roadmap, manifests, and releases |
| `linguamesh-core` | Provider-neutral Rust engine, protocols, codecs, persistence, and SDK artifacts |
| `linguamesh-l10n` | Canonical messages, locale metadata, translations, and generators |
| `linguamesh-android` | Kotlin and Jetpack Compose client |
| `linguamesh-windows` | C++/WinRT and WinUI 3 client |
| `linguamesh-macos` | SwiftUI and AppKit client |
| `linguamesh-linux` | Rust and GTK 4 client |

The authoritative product and engineering specification is [`PROJECT_GOAL.md`](PROJECT_GOAL.md). See [`REPOSITORY_ROLE.md`](REPOSITORY_ROLE.md) before making changes and use [`PLANS.md`](PLANS.md) for cross-repository work.

## Bootstrap and validation

From this repository:

```sh
tools/bootstrap.sh --owner "$(gh api user --jq '.login')"
tools/check-workspace.sh
```

On PowerShell:

```powershell
./tools/bootstrap.ps1 -Owner (gh api user --jq '.login')
./tools/check-workspace.ps1
```

Bootstrap preserves existing sibling directories and clones only missing repositories. Validation needs no commercial provider credentials. Pass `--require-repositories` or `-RequireRepositories` when all sibling repositories must be present.

## Architecture and policies

- [`docs/architecture/overview.md`](docs/architecture/overview.md) describes repository boundaries, providers, documents, ABI, privacy, and extension points.
- [`COMPATIBILITY.md`](COMPATIBILITY.md) and [`release-manifest.toml`](release-manifest.toml) define the known-good release train.
- [`SECURITY.md`](SECURITY.md) explains vulnerability reporting and security boundaries.
- [`PRIVACY.md`](PRIVACY.md) describes local data, provider transmission, credentials, and diagnostics.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) contains the development and review workflow.

LinguaMesh is licensed under the [MIT License](LICENSE). No provider endorsement is implied.

