#!/usr/bin/env python3
"""Deterministic conformance checks for the EII Public Provenance Registry."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
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
ARTIFACT_ROW_RE = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([0-9a-f]+)`\s*\|$"
)


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
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    if errors:
        for error in errors:
            location = ".".join(str(p) for p in error.absolute_path) or "<root>"
            print(f"SCHEMA ERROR [{location}]: {error.message}", file=sys.stderr)
        raise SystemExit(1)


def parse_artifact_register(text: str) -> list[dict[str, str]]:
    """Parse and strictly validate the Markdown Artifact Register.

    AC-03: artifact filenames must be exact, basename-only, and unique.
    AC-06: every parsed artifact row must carry one lowercase SHA-256 digest.
    """
    heading = re.search(r"^#{2,4}\s+Artifact Register\s*$", text, flags=re.MULTILINE)
    if not heading:
        fail("verification record lacks an Artifact Register section")

    lines = text[heading.end():].splitlines()
    rows: list[dict[str, str]] = []
    in_table = False
    for raw in lines:
        line = raw.strip()
        if line.startswith("### ") or line.startswith("## "):
            break
        if not line:
            continue
        if line.startswith("| Artifact "):
            in_table = True
            continue
        if in_table and re.fullmatch(r"\|(?:\s*:?-+:?\s*\|){4}", line):
            continue
        if in_table and line.startswith("|"):
            match = ARTIFACT_ROW_RE.fullmatch(line)
            if not match:
                fail(f"malformed Artifact Register row: {line}")
            filename, artifact_type, status, digest = match.groups()
            if Path(filename).name != filename or filename in {".", ".."}:
                fail(f"artifact filename must be an exact basename, not a path: {filename}")
            if not SHA256_RE.fullmatch(digest):
                fail(f"invalid SHA-256 digest for artifact {filename}")
            rows.append(
                {
                    "filename": filename,
                    "type": artifact_type.strip(),
                    "status": status.strip(),
                    "sha256": digest,
                }
            )

    if not rows:
        fail("Artifact Register contains no artifact rows")
    filenames = [row["filename"] for row in rows]
    if len(filenames) != len(set(filenames)):
        fail("Artifact Register contains duplicate artifact filenames")
    return rows


def verify_artifact_bytes(rows: list[dict[str, str]], archive_root: Path) -> None:
    """Recompute SHA-256 for exact artifact bytes when a controlled archive is available."""
    for row in rows:
        path = archive_root / row["filename"]
        if not path.is_file():
            fail(f"archived artifact is missing: {row['filename']}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != row["sha256"]:
            fail(f"SHA-256 mismatch for archived artifact: {row['filename']}")


def validate_logical_invariants(registry: dict, root: Path | None = None) -> None:
    root = ROOT if root is None else root
    records = registry.get("records", [])
    ids = [r["record_id"] for r in records]
    if len(ids) != len(set(ids)):
        fail("duplicate record_id values detected")

    all_ids = set(ids)
    for record in records:
        rid = record["record_id"]
        if not RECORD_ID_RE.fullmatch(rid):
            fail(f"invalid record_id: {rid}")
        if record["record_type"] != rid.split("-")[1]:
            fail(f"record_type does not match record_id for {rid}")
        if not SHA1_RE.fullmatch(record["commit_sha"]):
            fail(f"commit_sha is not a 40-character lowercase hexadecimal Git SHA for {rid}")

        path = root / record["verification_path"]
        if not path.is_file():
            fail(f"verification_path does not exist for {rid}: {record['verification_path']}")

        text = path.read_text(encoding="utf-8")
        if rid not in text:
            fail(f"verification record does not contain its record_id: {rid}")
        if "Evidence Boundary" not in text and "Evidentiary Boundary" not in text:
            fail(f"verification record lacks an evidence-boundary section: {rid}")

        parse_artifact_register(text)

        status = record["supersession"]["status"]
        supersedes = record["supersession"]["supersedes"]
        superseded_by = record["supersession"]["superseded_by"]
        if status == "Superseded" and not superseded_by:
            fail(f"superseded record must identify superseded_by: {rid}")
        if status == "Active" and superseded_by:
            fail(f"active record cannot identify superseded_by: {rid}")
        for related in supersedes + superseded_by:
            if related == rid:
                fail(f"record cannot supersede or be superseded by itself: {rid}")
            if related not in all_ids:
                fail(f"supersession relationship points to unknown record {related}: {rid}")


def git_object_exists(root: Path, object_spec: str) -> bool:
    result = subprocess.run(
        ["git", "-C", str(root), "cat-file", "-e", object_spec],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def validate_git_chronology(registry: dict, root: Path | None = None) -> None:
    """Strengthen AC-13 by resolving each indexed commit and record path in Git history."""
    root = ROOT if root is None else root
    if not (root / ".git").exists():
        fail("Git chronology validation requires a Git working tree")
    for record in registry["records"]:
        rid = record["record_id"]
        commit = record["commit_sha"]
        if not git_object_exists(root, f"{commit}^{{commit}}"):
            fail(f"indexed Git commit does not resolve for {rid}: {commit}")
        if not git_object_exists(root, f"{commit}:{record['verification_path']}"):
            fail(
                f"verification record did not exist at indexed Git commit for {rid}: "
                f"{record['verification_path']}"
            )


def parse_markdown_ledger(md: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    pattern = re.compile(
        r"^\| `(?P<id>EII-(?:WPR|APR|RPR|TPR|OPR|HPR)-[^`]+)` "
        r"\| (?P<family>[^|]+?) \| (?P<maturity>[^|]+?) \| `(?P<date>\d{4}-\d{2}-\d{2})` "
        r"\| `(?P<schema>EII-REG-SCHEMA-001 v[^`]+)` "
        r"\| \[`(?P<sha>[0-9a-f]{40})`\]\([^)]*\) "
        r"\| (?P<status>[^|]+?) \| \[`(?P<path>[^`]+)`\]\([^)]*\) \|$",
        flags=re.MULTILINE,
    )
    for match in pattern.finditer(md):
        data = match.groupdict()
        rid = data.pop("id")
        if rid in rows:
            fail(f"REGISTRY-INDEX.md contains duplicate ledger row: {rid}")
        rows[rid] = data
    return rows


def validate_markdown_sync(registry: dict, index_md: Path | None = None) -> None:
    index_md = INDEX_MD if index_md is None else index_md
    if not index_md.is_file():
        fail("REGISTRY-INDEX.md is missing")
    md = index_md.read_text(encoding="utf-8")
    ledger = parse_markdown_ledger(md)
    json_ids = {r["record_id"] for r in registry["records"]}
    if set(ledger) != json_ids:
        missing = sorted(json_ids - set(ledger))
        extra = sorted(set(ledger) - json_ids)
        fail(f"Markdown/JSON record-set divergence; missing={missing}, extra={extra}")

    for record in registry["records"]:
        rid = record["record_id"]
        row = ledger[rid]
        expected_family = "; ".join(record["artifact_family"])
        expected_maturity = " / ".join(record["artifact_maturity"])
        expected = {
            "family": expected_family,
            "maturity": expected_maturity,
            "date": record["publication_date"],
            "schema": f"{record['controlling_schema']['id']} v{record['controlling_schema']['version']}",
            "sha": record["commit_sha"],
            "status": record["supersession"]["status"],
            "path": record["verification_path"],
        }
        for field, value in expected.items():
            if row[field].strip() != value:
                fail(
                    f"REGISTRY-INDEX.md is out of sync for {rid}: "
                    f"field {field!r} expected {value!r}, found {row[field].strip()!r}"
                )


def main() -> int:
    registry = load_json(INDEX_JSON)
    schema = load_json(INDEX_SCHEMA)
    validate_schema(registry, schema)
    validate_logical_invariants(registry)
    validate_markdown_sync(registry)
    validate_git_chronology(registry)
    print(f"PASS: registry conformance checks succeeded for {len(registry['records'])} record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
