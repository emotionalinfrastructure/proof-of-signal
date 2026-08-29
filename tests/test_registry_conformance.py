#!/usr/bin/env python3
"""Adversarial tests for the EII provenance-registry validator.

The suite verifies that malformed or inconsistent registry states fail closed.
It uses only Python's standard unittest framework plus the jsonschema dependency
already required by scripts/validate_registry.py.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_registry.py"

spec = importlib.util.spec_from_file_location("eii_registry_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class RegistryConformanceAdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline_registry = json.loads(
            (REPO_ROOT / "registry-index.json").read_text(encoding="utf-8")
        )
        cls.schema = json.loads(
            (REPO_ROOT / "registry-index.schema.json").read_text(encoding="utf-8")
        )
        cls.baseline_markdown = (REPO_ROOT / "REGISTRY-INDEX.md").read_text(
            encoding="utf-8"
        )
        cls.baseline_verification = (
            REPO_ROOT / cls.baseline_registry["records"][0]["verification_path"]
        ).read_text(encoding="utf-8")

    def registry(self) -> dict:
        return copy.deepcopy(self.baseline_registry)

    def assert_fails(self, fn, *args) -> None:
        with self.assertRaises(SystemExit) as ctx:
            fn(*args)
        self.assertNotEqual(ctx.exception.code, 0)

    def make_temp_root(
        self,
        registry: dict,
        *,
        markdown: str | None = None,
        verification_text: str | None = None,
        create_verification: bool = True,
    ):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "registry-index.json").write_text(
            json.dumps(registry, indent=2), encoding="utf-8"
        )
        (root / "registry-index.schema.json").write_text(
            json.dumps(self.schema, indent=2), encoding="utf-8"
        )
        (root / "REGISTRY-INDEX.md").write_text(
            self.baseline_markdown if markdown is None else markdown,
            encoding="utf-8",
        )

        if create_verification:
            for record in registry["records"]:
                path = root / record["verification_path"]
                path.parent.mkdir(parents=True, exist_ok=True)
                text = (
                    self.baseline_verification
                    if verification_text is None
                    else verification_text
                )
                # Ensure cloned records have their own ID in the test fixture.
                source_id = self.baseline_registry["records"][0]["record_id"]
                text = text.replace(source_id, record["record_id"])
                path.write_text(text, encoding="utf-8")
        return temp, root

    def test_baseline_registry_passes_current_validator(self) -> None:
        registry = self.registry()
        validator.validate_schema(registry, self.schema)
        validator.validate_logical_invariants(registry)
        validator.validate_markdown_sync(registry)

    def test_malformed_commit_hash_fails_closed(self) -> None:
        registry = self.registry()
        registry["records"][0]["commit_sha"] = "xyz"
        self.assert_fails(validator.validate_schema, registry, self.schema)

    def test_duplicate_record_id_fails_closed(self) -> None:
        registry = self.registry()
        duplicate = copy.deepcopy(registry["records"][0])
        duplicate["verification_path"] = "weekly-proof/duplicate.md"
        registry["records"].append(duplicate)

        temp, root = self.make_temp_root(registry)
        self.addCleanup(temp.cleanup)
        with patch.object(validator, "ROOT", root):
            self.assert_fails(validator.validate_logical_invariants, registry)

    def test_invalid_maturity_state_fails_closed(self) -> None:
        registry = self.registry()
        registry["records"][0]["artifact_maturity"] = ["Certified"]
        self.assert_fails(validator.validate_schema, registry, self.schema)

    def test_missing_verification_record_fails_closed(self) -> None:
        registry = self.registry()
        registry["records"][0]["verification_path"] = "weekly-proof/missing.md"

        temp, root = self.make_temp_root(registry, create_verification=False)
        self.addCleanup(temp.cleanup)
        with patch.object(validator, "ROOT", root):
            self.assert_fails(validator.validate_logical_invariants, registry)

    def test_markdown_json_divergence_fails_closed(self) -> None:
        registry = self.registry()
        record = registry["records"][0]
        divergent_markdown = self.baseline_markdown.replace(
            record["commit_sha"], "0" * 40
        )

        temp, root = self.make_temp_root(registry, markdown=divergent_markdown)
        self.addCleanup(temp.cleanup)
        temp_index = root / "REGISTRY-INDEX.md"
        with patch.object(validator, "INDEX_MD", temp_index):
            self.assert_fails(validator.validate_markdown_sync, registry)

    def test_superseded_without_successor_fails_closed(self) -> None:
        registry = self.registry()
        record = registry["records"][0]
        record["supersession"]["status"] = "Superseded"
        record["supersession"]["superseded_by"] = []

        temp, root = self.make_temp_root(registry)
        self.addCleanup(temp.cleanup)
        with patch.object(validator, "ROOT", root):
            self.assert_fails(validator.validate_logical_invariants, registry)

    def test_active_record_with_successor_fails_closed(self) -> None:
        registry = self.registry()
        record = registry["records"][0]
        record["supersession"]["status"] = "Active"
        record["supersession"]["superseded_by"] = ["EII-WPR-2099-01-01"]

        temp, root = self.make_temp_root(registry)
        self.addCleanup(temp.cleanup)
        with patch.object(validator, "ROOT", root):
            self.assert_fails(validator.validate_logical_invariants, registry)

    def test_verification_record_without_sha256_fails_closed(self) -> None:
        registry = self.registry()
        no_digest = "# EII-WPR-2026-08-28\n\n## Evidence Boundary\nDefined limits.\n"

        temp, root = self.make_temp_root(registry, verification_text=no_digest)
        self.addCleanup(temp.cleanup)
        with patch.object(validator, "ROOT", root):
            self.assert_fails(validator.validate_logical_invariants, registry)


if __name__ == "__main__":
    unittest.main(verbosity=2)
