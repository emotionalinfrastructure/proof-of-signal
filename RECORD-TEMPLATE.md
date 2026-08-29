# EII Provenance Record Template

> Copy this file to the appropriate record path. Replace every bracketed instruction before publication. A record containing unresolved bracketed instructions SHALL NOT be designated `Published`.

**Record ID:** `[EII-CLASS-REFERENCE]`  
**Version:** `[1.0]`  
**Status:** `[Draft | Incomplete | Published | Corrected | Superseded | Withdrawn | Historical]`  
**Reference date:** `[YYYY-MM-DD]`  
**Maintainer:** `[responsible person or unit]`  
**Controlling schema:** `EII-REG-SCHEMA-001 v1.0`  
**Integrity method:** `SHA-256`

---

## Scope

[Define exactly which artifacts, development period, or evidence object this record represents.]

## Artifact Register

| Artifact | Type | Maturity | SHA-256 | Inclusion Rationale |
|---|---|---|---|---|
| `[exact-filename.ext]` | `[type]` | `[approved maturity]` | `[64-character lowercase SHA-256]` | `[why this artifact is included]` |

## Development Status

[State what has actually been completed, what remains pending, and the highest maturity state supported by available evidence.]

## Verification

Compute the SHA-256 digest of the exact artifact and compare it with the Artifact Register.

Linux:

```bash
sha256sum <filename>
```

macOS:

```bash
shasum -a 256 <filename>
```

A matching digest verifies byte-for-byte identity with the file state represented by this record.

## Controlled Archive

**Archive identifier/location:** `[controlled archive reference]`

[State whether the archive is public or restricted. Do not expose sensitive information merely to provide an archive location.]

## Evidence Boundary

This record may support evidence of exact file identity and repository chronology. It does not independently establish originality, novelty, priority of authorship, intellectual-property ownership, truth of claims inside the artifact, causation, empirical validity, institutional approval, regulatory compliance, standards adoption, production readiness, or legal entitlement.

[Add artifact-specific boundaries when needed.]

## Supersession

**Status:** `[Active | Partially Superseded | Superseded | Withdrawn | Historical]`  
**Supersedes:** `[Record IDs or None]`  
**Superseded by:** `[Record IDs or None]`

## Conformance Review

```text
[ ] AC-01 Identity
[ ] AC-02 Scope
[ ] AC-03 Exact filenames
[ ] AC-04 Maturity
[ ] AC-05 Integrity
[ ] AC-06 Digest format
[ ] AC-07 Archive
[ ] AC-08 Reproducibility
[ ] AC-09 Evidence boundary
[ ] AC-10 Claim discipline
[ ] AC-11 Institutional boundary
[ ] AC-12 Privacy and security
[ ] AC-13 Public chronology
[ ] AC-14 Registry indexing
[ ] AC-15 Final review
```

## Public Record

**Commit SHA:** `[40-character Git commit SHA]`  
**Verification path:** `[repository/path/to/record.md]`

---

**EII Registry Conformance:** [Use the conformance statement defined by EII-REG-SCHEMA-001 only after every applicable acceptance criterion has passed.]
