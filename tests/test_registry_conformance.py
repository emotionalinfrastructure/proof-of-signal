#!/usr/bin/env python3
"""Fixture-driven adversarial tests for EII registry conformance controls."""

from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES = REPO_ROOT / "tests" / "fixtures"
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_registry.py"

spec = importlib.util.spec_from_file_location("eii_registry_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class RegistryFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads((REPO_ROOT / "registry-index.schema.json").read_text())
        cls.fixture_registry = json.loads(
            (FIXTURES / "registry" / "valid-registry.json").read_text()
        )

    def assert_fails(self, fn, *args) -> None:
        with self.assertRaises(SystemExit) as ctx:
            fn(*args)
        self.assertNotEqual(ctx.exception.code, 0)

    def fixture_text(self, relative: str) -> str:
        return (FIXTURES / relative).read_text(encoding="utf-8")

    def test_valid_artifact_register_parses(self) -> None:
        rows = validator.parse_artifact_register(self.fixture_text("records/valid-record.md"))
        self.assertEqual([r["filename"] for r in rows], ["fixture-alpha.txt", "fixture-beta.txt"])
        self.assertEqual(len(rows), 2)

    def test_ac03_path_instead_of_exact_filename_fails_closed(self) -> None:
        self.assert_fails(
            validator.parse_artifact_register,
            self.fixture_text("records/invalid-path-filename.md"),
        )

    def test_ac03_duplicate_filename_fails_closed(self) -> None:
        self.assert_fails(
            validator.parse_artifact_register,
            self.fixture_text("records/invalid-duplicate-filename.md"),
        )

    def test_ac06_malformed_digest_fails_closed(self) -> None:
        self.assert_fails(
            validator.parse_artifact_register,
            self.fixture_text("records/invalid-bad-digest.md"),
        )

    def test_ac05_exact_fixture_bytes_recompute_successfully(self) -> None:
        rows = validator.parse_artifact_register(self.fixture_text("records/valid-record.md"))
        validator.verify_artifact_bytes(rows, FIXTURES / "artifacts")

    def test_ac05_byte_change_fails_closed(self) -> None:
        rows = validator.parse_artifact_register(self.fixture_text("records/valid-record.md"))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for source in (FIXTURES / "artifacts").iterdir():
                shutil.copy2(source, root / source.name)
            (root / "fixture-alpha.txt").write_text("tampered fixture alpha\n", encoding="utf-8")
            self.assert_fails(validator.verify_artifact_bytes, rows, root)

    def test_fixture_registry_and_index_are_structurally_conformant(self) -> None:
        registry = copy.deepcopy(self.fixture_registry)
        validator.validate_schema(registry, self.schema)
        validator.validate_markdown_sync(
            registry, FIXTURES / "registry" / "valid-index.md"
        )

    def test_stronger_ac14_family_divergence_fails_closed(self) -> None:
        registry = copy.deepcopy(self.fixture_registry)
        with tempfile.TemporaryDirectory() as tmp:
            bad_index = Path(tmp) / "index.md"
            text = self.fixture_text("registry/valid-index.md").replace(
                "Fixture governance artifact", "Different artifact family"
            )
            bad_index.write_text(text, encoding="utf-8")
            self.assert_fails(validator.validate_markdown_sync, registry, bad_index)

    def test_stronger_ac14_maturity_divergence_fails_closed(self) -> None:
        registry = copy.deepcopy(self.fixture_registry)
        with tempfile.TemporaryDirectory() as tmp:
            bad_index = Path(tmp) / "index.md"
            text = self.fixture_text("registry/valid-index.md").replace(
                "| Candidate |", "| Pilot |"
            )
            bad_index.write_text(text, encoding="utf-8")
            self.assert_fails(validator.validate_markdown_sync, registry, bad_index)

    def test_ac13_commit_and_record_path_resolve_in_git_history(self) -> None:
        registry = copy.deepcopy(self.fixture_registry)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "records").mkdir(parents=True)
            shutil.copy2(FIXTURES / "records" / "valid-record.md", root / "records" / "valid-record.md")
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Fixture Runner"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "fixture@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(root), "add", "records/valid-record.md"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "fixture provenance"], check=True)
            sha = subprocess.check_output(
                ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
            ).strip()
            registry["records"][0]["commit_sha"] = sha
            validator.validate_git_chronology(registry, root)

    def test_ac13_unknown_commit_fails_closed(self) -> None:
        registry = copy.deepcopy(self.fixture_registry)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            self.assert_fails(validator.validate_git_chronology, registry, root)

    def test_ac13_record_absent_at_commit_fails_closed(self) -> None:
        registry = copy.deepcopy(self.fixture_registry)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.name", "Fixture Runner"], check=True)
            subprocess.run(["git", "-C", str(root), "config", "user.email", "fixture@example.invalid"], check=True)
            (root / "unrelated.txt").write_text("unrelated\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "unrelated.txt"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-q", "-m", "unrelated"], check=True)
            sha = subprocess.check_output(
                ["git", "-C", str(root), "rev-parse", "HEAD"], text=True
            ).strip()
            registry["records"][0]["commit_sha"] = sha
            self.assert_fails(validator.validate_git_chronology, registry, root)

    def test_live_registry_still_passes_non_git_controls(self) -> None:
        registry = json.loads((REPO_ROOT / "registry-index.json").read_text())
        validator.validate_schema(registry, self.schema)
        validator.validate_logical_invariants(registry, REPO_ROOT)
        validator.validate_markdown_sync(registry, REPO_ROOT / "REGISTRY-INDEX.md")


if __name__ == "__main__":
    unittest.main(verbosity=2)
