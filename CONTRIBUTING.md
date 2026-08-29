# Contributing to the EII Public Provenance Registry

This repository is a controlled provenance registry. Changes SHOULD preserve evidence integrity, chronology, status discipline, and reproducibility.

## Admission workflow

A new active provenance record SHALL follow this sequence:

1. Freeze the exact artifact version intended for the record.
2. Compute SHA-256 from the exact archived bytes.
3. Preserve the canonical artifact in a controlled archive.
4. Create the provenance record using `REGISTRY-SCHEMA.md`.
5. Evaluate AC-01 through AC-15 and resolve every applicable failure.
6. Commit the provenance record publicly.
7. Add the admitted record to `REGISTRY-INDEX.md` and `registry-index.json`.
8. Confirm that the human-readable and machine-readable indexes agree.
9. Validate `registry-index.json` against `registry-index.schema.json`.
10. Preserve material corrections through Git history rather than silently obscuring them.

## Commit conventions

Preferred commit prefixes:

- `docs:` documentation and provenance-record changes
- `feat:` new registry capability or machine-readable control
- `fix:` correction of an error or inconsistency
- `chore:` maintenance that does not alter evidentiary meaning

Commit messages SHOULD identify the affected record or control where practical.

## Prohibited practices

Contributors SHALL NOT knowingly:

- reuse an old digest for modified bytes;
- label candidate work as validated without supporting evidence;
- imply institutional endorsement without documentary support;
- publish restricted or sensitive evidence merely to make a hash verifiable;
- remove historical records to create a misleading chronology;
- treat Git timestamps as independent proof of originality or legal ownership; or
- allow the Markdown and JSON registry indexes to materially diverge.

## Corrections

Errors SHOULD be corrected promptly. Material corrections SHALL remain visible in Git history. When an error changes artifact identity, maturity, digest, scope, or evidentiary meaning, the correction SHOULD explain the affected field and preserve the prior state through repository history.

## Controlling documents

- `README.md` defines repository purpose.
- `REGISTRY-SCHEMA.md` defines conformance and admission requirements.
- `REGISTRY-INDEX.md` is the canonical human-readable ledger.
- `registry-index.json` is the machine-readable companion ledger.
- `registry-index.schema.json` defines structural validation for the JSON ledger.

When these documents conflict, `REGISTRY-SCHEMA.md` controls provenance-entry requirements, while Git history preserves the record of any subsequent correction.
