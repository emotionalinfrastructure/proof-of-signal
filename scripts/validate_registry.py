#!/usr/bin/env python3
"""Deterministic conformance checks for the EII Public Provenance Registry."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
INDEX_JSON = ROOT / "registry-index.json"
INDEX_SCHEMA = ROOT / "registry-index.schema.json"
INDEX_MD = ROOT / "REGISTRY-INDEX.md"

SHA1_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
RECORD_ID_RE = re.compile(r"^EII-(WPR|APR|RPR|TPR|OPR|HPR)-[A-Za-z0-9._-]+$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path):
    if not path.is_file():
        fail(f"required file is missing: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_schema(instance: dict, schema: dict) -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    if errors:
        for error in errors:
            location = ".".join(str(p) for p in error.absolute_path) or "<root>"
            print(f"SCHEMA ERROR [{location}]: {error.message}", file=sys.stderr)
        raise SystemExit(1)


def validate_logical_invariants(registry: dict) -> None:
    records = registry.get("records", [])
    ids = [r["record_id"] for r in records]
    if len(ids) != len(set(ids)):
        fail("duplicate record_id values detected")

    for record in records:
        rid = record["record_id"]
        if not RECORD_ID_RE.fullmatch(rid):
            fail(f"invalid record_id: {rid}")
        if record["record_type"] != rid.split("-")[1]:
            fail(f"record_type does not match record_id for {rid}")
        if not SHA1_RE.fullmatch(record["commit_sha"]):
            fail(f"commit_sha is not a 40-character lowercase hexadecimal Git SHA for {rid}")

        path = ROOT / record["verification_path"]
        if not path.is_file():
            fail(f"verification_path does not exist for {rid}: {record['verification_path']}")

        text = path.read_text(encoding="utf-8")
        if rid not in text:
            fail(f"verification record does not contain its record_id: {rid}")
        if "Evidence Boundary" not in text and "Evidentiary Boundary" not in text:
            fail(f"verification record lacks an evidence-boundary section: {rid}")

        digests = re.findall(r"\b[0-9a-f]{64}\b", text)
        if not digests:
            fail(f"verification record contains no SHA-256 digest: {rid}")
        for digest in digests:
            if not SHA256_RE.fullmatch(digest):
                fail(f"invalid SHA-256 digest in verification record {rid}: {digest}")

        status = record["supersession"]["status"]
        if status == "Superseded" and not record["supersession"]["superseded_by"]:
            fail(f"superseded record must identify superseded_by: {rid}")
        if status == "Active" and record["supersession"]["superseded_by"]:
            fail(f"active record cannot identify superseded_by: {rid}")


def validate_markdown_sync(registry: dict) -> None:
    if not INDEX_MD.is_file():
        fail("REGISTRY-INDEX.md is missing")
    md = INDEX_MD.read_text(encoding="utf-8")

    for record in registry["records"]:
        required_tokens = [
            record["record_id"],
            record["publication_date"],
            record["commit_sha"],
            record["verification_path"],
            record["controlling_schema"]["id"],
            record["controlling_schema"]["version"],
            record["supersession"]["status"],
        ]
        for token in required_tokens:
            if token not in md:
                fail(f"REGISTRY-INDEX.md is out of sync for {record['record_id']}: missing {token!r}")

    md_ids = set(re.findall(r"\bEII-(?:WPR|APR|RPR|TPR|OPR|HPR)-[A-Za-z0-9._-]+\b", md))
    json_ids = {r["record_id"] for r in registry["records"]}
    extra_ids = md_ids - json_ids
    if extra_ids:
        fail(f"REGISTRY-INDEX.md contains record IDs absent from registry-index.json: {sorted(extra_ids)}")


def main() -> int:
    registry = load_json(INDEX_JSON)
    schema = load_json(INDEX_SCHEMA)
    validate_schema(registry, schema)
    validate_logical_invariants(registry)
    validate_markdown_sync(registry)
    print(f"PASS: registry conformance checks succeeded for {len(registry['records'])} record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
