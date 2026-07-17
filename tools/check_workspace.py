import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    print("Validation failed: Python 3.11 or newer is required.", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the LinguaMesh coordination workspace.")
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--require-repositories", action="store_true")
    arguments = parser.parse_args()

    project_root = Path(arguments.project_root).resolve()
    workspace_root = project_root.parent
    canonical = [
        "linguamesh-project",
        "linguamesh-core",
        "linguamesh-l10n",
        "linguamesh-android",
        "linguamesh-windows",
        "linguamesh-macos",
        "linguamesh-linux",
    ]
    required_files = [
        ".gitignore",
        "AGENTS.md",
        "PROJECT_GOAL.md",
        "PLANS.md",
        "README.md",
        "LICENSE",
        "REPOSITORY_ROLE.md",
        "SECURITY.md",
        "PRIVACY.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "ROADMAP.md",
        "IMPLEMENTATION_STATUS.md",
        "COMPATIBILITY.md",
        "THIRD_PARTY_NOTICES.md",
        "CHANGELOG.md",
        "workspace-manifest.toml",
        "release-manifest.toml",
        "schemas/release-manifest.schema.json",
        "docs/TESTING.md",
        "docs/RELEASING.md",
        "docs/GITHUB_BOOTSTRAP.md",
        "docs/security/data-flow.md",
        "docs/security/trust-boundaries.md",
        "tools/bootstrap.sh",
        "tools/bootstrap.ps1",
        "tools/check-workspace.sh",
        "tools/check-workspace.ps1",
        "tools/check_workspace.py",
        ".github/workflows/validate.yml",
        ".github/workflows/cross-repository.yml",
        ".github/CODEOWNERS",
    ]
    required_directories = [
        "docs/architecture",
        "docs/adr",
        "docs/rfc",
        "docs/releases",
        "docs/security",
        ".github/ISSUE_TEMPLATE",
        "templates/repository",
    ]
    errors: list[str] = []

    for relative in required_files:
        if not (project_root / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    for relative in required_directories:
        if not (project_root / relative).is_dir():
            errors.append(f"Missing required directory: {relative}")

    ignore_file = project_root / ".gitignore"
    if ignore_file.is_file():
        first_rule = ignore_file.read_text(encoding="utf-8").splitlines()[0:1]
        if first_rule != [".codex/"]:
            errors.append(".codex/ must be the first ignore rule.")

    workspace_file = project_root / "workspace-manifest.toml"
    release_file = project_root / "release-manifest.toml"
    schema_file = project_root / "schemas/release-manifest.schema.json"
    if not workspace_file.is_file() or not release_file.is_file() or not schema_file.is_file():
        return report(errors)

    with workspace_file.open("rb") as stream:
        workspace = tomllib.load(stream)
    repositories = workspace.get("repositories", [])
    names = [entry.get("name") for entry in repositories]
    paths = [entry.get("path") for entry in repositories]
    if names != canonical:
        errors.append(f"Workspace repository order or set is invalid: {names}")
    if paths != canonical:
        errors.append(f"Workspace repository paths are invalid: {paths}")
    if len(set(names)) != len(names):
        errors.append("Workspace repository names must be unique.")
    if any(entry.get("required") is not True for entry in repositories):
        errors.append("Every canonical repository must be required.")

    goal_digest = hashlib.sha256((project_root / "PROJECT_GOAL.md").read_bytes()).hexdigest()
    goal_revision = f"sha256:{goal_digest}"
    if workspace.get("global_goal_revision") != goal_revision:
        errors.append("Workspace manifest global-goal revision does not match PROJECT_GOAL.md.")

    with release_file.open("rb") as stream:
        release = tomllib.load(stream)
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    if schema.get("properties", {}).get("schema_version", {}).get("const") != 1:
        errors.append("Release schema does not declare schema version 1.")
    if release.get("schema_version") != 1:
        errors.append("Release manifest schema version must be 1.")
    if release.get("status") not in {"unreleased", "prerelease", "stable", "withdrawn"}:
        errors.append("Release manifest status is invalid.")
    if release.get("global_goal_revision") != goal_revision:
        errors.append("Release manifest global-goal revision does not match PROJECT_GOAL.md.")

    expected_components = {
        "core": "linguamesh-core",
        "localization": "linguamesh-l10n",
        "android": "linguamesh-android",
        "windows": "linguamesh-windows",
        "macos": "linguamesh-macos",
        "linux": "linguamesh-linux",
    }
    components = release.get("components", {})
    if set(components) != set(expected_components):
        errors.append(f"Release component set is invalid: {sorted(components)}")
    semver = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
    checksum = re.compile(r"^[a-f0-9]{64}$")
    for component_name, repository_name in expected_components.items():
        component = components.get(component_name, {})
        if component.get("repository") != repository_name:
            errors.append(f"Release component {component_name} has the wrong repository.")
        if not semver.fullmatch(str(component.get("version", ""))):
            errors.append(f"Release component {component_name} has an invalid version.")
        if not component.get("source_revision"):
            errors.append(f"Release component {component_name} lacks a source revision.")
        compatibility_key = "minimum_compatible_version" if component_name in {"core", "localization"} else "minimum_compatible_core"
        if not semver.fullmatch(str(component.get(compatibility_key, ""))):
            errors.append(f"Release component {component_name} has an invalid minimum compatible version.")
        for artifact in component.get("artifacts", []):
            if not artifact.get("name") or not artifact.get("url") or not checksum.fullmatch(str(artifact.get("sha256", ""))):
                errors.append(f"Release component {component_name} has invalid artifact metadata.")

    if release.get("status") == "stable":
        if not release.get("known_limitations"):
            errors.append("A stable release must explicitly record known limitations, including none.")
        for component_name, component in components.items():
            if "dev" in str(component.get("version", "")) or not component.get("artifacts"):
                errors.append(f"Stable component {component_name} cannot use a development version or empty artifacts.")
            if not re.fullmatch(r"[a-f0-9]{40,64}", str(component.get("source_revision", ""))):
                errors.append(f"Stable component {component_name} must pin a source revision digest.")

    compatibility_text = (project_root / "COMPATIBILITY.md").read_text(encoding="utf-8")
    if goal_revision not in compatibility_text:
        errors.append("Compatibility documentation has a stale global-goal revision.")
    compatibility_labels = {
        "core": "Core",
        "localization": "Localization",
        "android": "Android client",
        "windows": "Windows client",
        "macos": "macOS client",
        "linux": "Linux client",
    }
    for component_name, component in components.items():
        expected_row = f"| {compatibility_labels[component_name]} | `{component.get('version', '')}` |"
        if expected_row not in compatibility_text:
            errors.append(f"Compatibility documentation omits the {component_name} version.")
    abi_major = release.get("contracts", {}).get("abi_major")
    if f"ABI `{abi_major}`" not in compatibility_text:
        errors.append("Compatibility documentation omits the release ABI major.")
    for contract_name in ["provider_catalog_version", "localization_schema_version"]:
        contract_version = release.get("contracts", {}).get(contract_name)
        if f"`{contract_version}`" not in compatibility_text:
            errors.append(f"Compatibility documentation omits {contract_name}.")

    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for markdown in project_root.rglob("*.md"):
        if ".codex" in markdown.parts or ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_target = target.split("#", 1)[0]
            if file_target and not (markdown.parent / file_target).resolve().exists():
                errors.append(f"Broken Markdown link in {markdown.relative_to(project_root)}: {target}")

    secret_patterns = [
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        re.compile(r"AIza[0-9A-Za-z_-]{30,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    excluded_parts = {".git", ".codex", "build", "dist"}
    for path in project_root.rglob("*"):
        if not path.is_file() or any(part in excluded_parts for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in secret_patterns:
            if pattern.search(text):
                errors.append(f"Potential credential material detected in {path.relative_to(project_root)}.")
                break

    if arguments.require_repositories:
        sibling_required = [
            "AGENTS.md",
            "REPOSITORY_ROLE.md",
            "GLOBAL_GOAL.md",
            "LICENSE",
            "SECURITY.md",
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
        ]
        for repository_name in canonical:
            repository_path = workspace_root / repository_name
            if not repository_path.is_dir():
                errors.append(f"Missing canonical repository directory: {repository_name}")
                continue
            for relative in sibling_required:
                if repository_name == "linguamesh-project" and relative == "GLOBAL_GOAL.md":
                    continue
                if not (repository_path / relative).is_file():
                    errors.append(f"Missing {repository_name}/{relative}")
            if repository_name != "linguamesh-project":
                goal_reference = repository_path / "GLOBAL_GOAL.md"
                if goal_reference.is_file() and goal_digest not in goal_reference.read_text(encoding="utf-8"):
                    errors.append(f"Stale global-goal revision in {repository_name}/GLOBAL_GOAL.md")

    return report(errors, arguments.require_repositories)


def report(errors: list[str], require_repositories: bool = False) -> int:
    if errors:
        for error in errors:
            print(f"Validation failed: {error}", file=sys.stderr)
        return 1
    print("Workspace manifest: valid")
    print("Global-goal revision: valid")
    print("Release manifest and compatibility matrix: valid")
    print("Documentation links: valid")
    print("Credential signature scan: clean")
    if require_repositories:
        print("Canonical repository layout and goal pins: valid")
    print("Workspace validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
