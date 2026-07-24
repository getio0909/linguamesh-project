#!/usr/bin/env python3
"""验证 release manifest 回滚演练只修改临时副本。"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ReleaseRollbackTest(unittest.TestCase):
    def test_manifest_only_rehearsal(self) -> None:
        script = Path(__file__).with_name("rehearse-release-rollback.py")
        with tempfile.TemporaryDirectory(prefix="linguamesh-rollback-test-") as temporary:
            root = Path(temporary)
            repository = root / "repository"
            repository.mkdir()
            manifest = root / "release-manifest.toml"
            manifest.write_text(
                'status = "unreleased"\n\n'
                '[components.linux]\nsource_revision = "1111111111111111111111111111111111111111"\n',
                encoding="utf-8",
            )
            subprocess.run(["git", "-C", str(repository), "init", "--initial-branch=main"], check=True)
            subprocess.run(
                ["git", "-C", str(repository), "config", "user.email", "test@example.invalid"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repository), "config", "user.name", "Rollback Test"],
                check=True,
            )
            (repository / "marker.txt").write_text("fixture\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repository), "add", "marker.txt"], check=True)
            subprocess.run(["git", "-C", str(repository), "commit", "-m", "fixture"], check=True)
            target = subprocess.run(
                ["git", "-C", str(repository), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            before = manifest.read_bytes()
            result = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--manifest",
                    str(manifest),
                    "--component",
                    "linux",
                    "--target-revision",
                    target,
                    "--repository",
                    str(repository),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Rollback rehearsal: valid", result.stdout)
            self.assertEqual(manifest.read_bytes(), before)
            self.assertEqual((repository / "marker.txt").read_text(encoding="utf-8"), "fixture\n")


if __name__ == "__main__":
    unittest.main()
