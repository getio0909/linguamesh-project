#!/usr/bin/env python3
"""在不修改工作区的情况下演练可逆的 release manifest pin 回滚。"""

from __future__ import annotations

import argparse
import copy
import re
import subprocess
import tempfile
import tomllib
from pathlib import Path


REVISION_PATTERN = re.compile(r"^[0-9a-f]{40,64}$")
COMPONENT_HEADER = re.compile(r"^\[components\.[^\]]+\]$", re.MULTILINE)
SOURCE_LINE = re.compile(r'(?m)^(source_revision\s*=\s*)"([^"]+)"\s*$')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rehearse a manifest-only release rollback without changing repository files."
    )
    parser.add_argument("--manifest", type=Path, default=Path("release-manifest.toml"))
    parser.add_argument("--component", required=True)
    parser.add_argument("--target-revision", required=True)
    parser.add_argument("--repository", type=Path, required=True)
    return parser.parse_args()


def fail(message: str) -> None:
    raise SystemExit(f"Rollback rehearsal failed: {message}")


def component_block(text: str, component: str) -> tuple[int, int, str]:
    header = f"[components.{component}]"
    start = text.find(header)
    if start < 0:
        fail(f"component is missing: {component}")
    next_match = COMPONENT_HEADER.search(text, start + len(header))
    end = next_match.start() if next_match else len(text)
    return start, end, text[start:end]


def main() -> int:
    args = parse_args()
    manifest = args.manifest.resolve()
    repository = args.repository.resolve()
    target = args.target_revision
    if not REVISION_PATTERN.fullmatch(target):
        fail("target revision must be a hexadecimal commit digest")
    if not manifest.is_file():
        fail(f"manifest does not exist: {manifest}")
    if not repository.is_dir():
        fail(f"repository does not exist: {repository}")

    commit_check = subprocess.run(
        ["git", "-C", str(repository), "cat-file", "-e", f"{target}^{{commit}}"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if commit_check.returncode != 0:
        fail(f"target revision is not present as a commit: {target}")

    original_text = manifest.read_text(encoding="utf-8")
    start, end, block = component_block(original_text, args.component)
    source_match = SOURCE_LINE.search(block)
    if source_match is None:
        fail(f"component has no source_revision: {args.component}")
    current = source_match.group(2)
    if current == target:
        fail("target revision is already active")
    updated_block = SOURCE_LINE.sub(
        lambda match: f'{match.group(1)}"{target}"', block, count=1
    )
    updated_text = original_text[:start] + updated_block + original_text[end:]

    with tempfile.TemporaryDirectory(prefix="linguamesh-rollback-") as temporary:
        temporary_manifest = Path(temporary) / manifest.name
        temporary_manifest.write_text(updated_text, encoding="utf-8")
        with manifest.open("rb") as stream:
            original = tomllib.load(stream)
        with temporary_manifest.open("rb") as stream:
            rehearsed = tomllib.load(stream)

    expected = copy.deepcopy(original)
    expected["components"][args.component]["source_revision"] = target
    if rehearsed != expected:
        fail("rehearsed manifest changes more than the selected component pin")
    if rehearsed.get("status") != "unreleased":
        fail("rollback rehearsal may not change release status")

    print("Rollback rehearsal: valid")
    print(f"Component: {args.component}")
    print(f"Current revision: {current}")
    print(f"Target revision: {target}")
    print("Manifest-only rehearsal complete; no repository files were modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
