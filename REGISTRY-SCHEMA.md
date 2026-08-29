# EII Public Provenance Registry Schema

**Document ID:** EII-REG-SCHEMA-001  
**Version:** 1.0  
**Status:** Active registry control specification  
**Effective date:** 2026-08-28  
**Maintainer:** Emotional Infrastructure Institute  
**Repository:** `emotionalinfrastructure/proof-of-signal`

---

## 1. Purpose

This specification defines the minimum record-control requirements for entries admitted to the Emotional Infrastructure Institute (EII) Public Provenance Registry.

The registry exists to preserve reproducible relationships among substantive artifacts, controlled versions, cryptographic identifiers, archives, and public Git history. This specification governs **provenance records**. It does not establish scientific validity, institutional approval, standards adoption, intellectual-property ownership, or legal priority.

The keywords **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are normative requirements within this repository.

---

## 2. Conformance

A provenance entry is **conformant** only when every applicable SHALL requirement in this specification is satisfied.

A record that fails a mandatory requirement SHALL NOT be labeled `Published` or added to the active registry table as conformant. It MAY be retained as `Draft`, `Incomplete`, or `Historical` when its status is explicit.

Conformance applies to the provenance record itself. It SHALL NOT be represented as validation of the underlying research, framework, instrument, software, policy, or organization.

---

## 3. Required Provenance Chain

Every conformant record SHALL preserve the following logical chain:

```text
Artifact
   ↓
Canonical Version
   ↓
SHA-256 Digest
   ↓
Evidence Record
   ↓
Controlled Archive
   ↓
Public Git Commit
```

No stage SHALL be described as proving more than the evidence produced by that stage can support.

---

## 4. Mandatory Record Metadata

Every provenance record SHALL contain the following metadata.

| Field | Requirement | Example |
|---|---|---|
| Record ID | SHALL be unique | `EII-WPR-2026-08-28` |
| Record title | SHALL identify the record class and period/object | `Weekly Research Provenance Record` |
| Record version | SHALL identify the schema-controlled revision | `1.0` |
| Record status | SHALL use an approved registry state | `Published` |
| Reporting or reference date | SHALL use ISO 8601 date format | `2026-08-28` |
| Maintainer | SHALL identify the responsible person or organizational unit | `Emotional Infrastructure Institute` |
| Artifact scope | SHALL describe what is represented | `Selected artifacts materially advanced during the reporting period` |
| Integrity algorithm | SHALL be `SHA-256` unless this specification is formally revised | `SHA-256` |
| Artifact register | SHALL enumerate every artifact represented by the record | See Section 7 |
| Evidence boundary | SHALL state what the record does and does not establish | See Section 10 |
| Public commit | SHALL exist before status becomes `Published` | Git commit SHA |

A record MAY include additional fields where they improve traceability, but optional metadata SHALL NOT replace mandatory metadata.

---

## 5. Record Identifier Convention

Registry record identifiers SHALL use the following structure:

```text
EII-[CLASS]-[REFERENCE]
```

Approved initial record classes are:

| Code | Record Class |
|---|---|
| `WPR` | Weekly Provenance Record |
| `APR` | Artifact Provenance Record |
| `RPR` | Research Provenance Record |
| `TPR` | Technical Provenance Record |
| `OPR` | Organizational Provenance Record |
| `HPR` | Historical Provenance Record |

A weekly record SHALL use:

```text
EII-WPR-YYYY-MM-DD
```

Example:

```text
EII-WPR-2026-08-28
```

A record identifier SHALL NOT be reused for a different logical record.

Corrections to a record SHOULD preserve the original Record ID and increment the record version. A substantively different provenance object SHALL receive a new Record ID.

---

## 6. Artifact Naming Convention

Where EII controls the filename, a canonical research or governance artifact SHOULD follow:

```text
EII-[PROGRAM]-[ARTIFACT]-[DESCRIPTOR]_vMAJOR.MINOR.ext
```

Example:

```text
EII-TIO-PILOT-001_Observatory_Pilot_Validation_Protocol_v0.2.pdf
```

Legacy artifacts, externally produced files, source evidence, and files whose names cannot reasonably be changed MAY retain their original filenames. The provenance record SHALL preserve the exact hashed filename.

A filename recorded beside a SHA-256 digest SHALL correspond to the exact file bytes used to generate that digest.

Renaming a file without modifying its bytes does not alter its SHA-256 digest, but the registry SHOULD document the canonical filename used for the controlled archive.

---

## 7. Mandatory Artifact Register

Every conformant provenance record SHALL contain an artifact register.

Each artifact entry SHALL contain:

| Field | Requirement |
|---|---|
| Exact filename | Mandatory |
| Artifact type | Mandatory |
| Version or maturity state | Mandatory |
| SHA-256 digest | Mandatory |
| Inclusion rationale or scope relationship | Mandatory when not obvious from the record title |

Recommended format:

```markdown
| Artifact | Type | Status | SHA-256 |
|---|---|---|---|
| `example_v0.1.pdf` | Research protocol | Candidate | `64-character lowercase hexadecimal digest` |
```

A record SHALL NOT list an artifact as integrity-verified unless the digest was computed from the exact archived file represented by the entry.

---

## 8. Maturity States

Artifact maturity SHALL be represented independently from provenance-record publication status.

Approved artifact maturity states are:

| State | Meaning |
|---|---|
| `Draft` | Active development; content may materially change |
| `Candidate` | Coherent version prepared for structured review or testing |
| `Pre-execution` | Procedures/specification prepared but formal execution has not begun |
| `Pilot` | Controlled feasibility or validation activity is underway or completed as explicitly stated |
| `Evaluated` | Defined evaluation has been completed; results and limitations SHALL be identified |
| `Validated` | Validation criteria defined in advance have been satisfied and supporting evidence is available |
| `Adopted` | A specifically identified organization or authority has formally adopted the artifact |
| `Deployed` | Artifact or implementation is operating in the stated production context |
| `Superseded` | Replaced by a later controlled version |
| `Withdrawn` | Removed from active use while retained for provenance |
| `Historical` | Preserved for chronology but not presented as current EII position |

### 8.1 Maturity Control

A maturity state SHALL NOT be assigned solely because an artifact was:

- uploaded to GitHub;
- hashed;
- publicly posted;
- discussed by another person;
- submitted for review;
- included in an archive; or
- referenced by an AI system.

`Validated`, `Adopted`, and `Deployed` SHALL require affirmative evidence appropriate to those states.

When evidence is insufficient, the lower defensible maturity state SHALL be used.

---

## 9. Provenance Record Status

Registry-record status SHALL use one of the following values:

| Status | Meaning |
|---|---|
| `Draft` | Record is being assembled and is not registry-final |
| `Incomplete` | One or more mandatory controls are unresolved |
| `Published` | Record satisfies the applicable acceptance criteria and has a public Git commit |
| `Corrected` | Published record was amended without replacing its logical identity |
| `Superseded` | Replaced by a newer provenance record |
| `Withdrawn` | No longer active but retained for history |
| `Historical` | Legacy record retained outside current conformance expectations |

`Published` describes the provenance record only. It SHALL NOT be interpreted as `Validated`, `Adopted`, or `Deployed` status for any underlying artifact.

---

## 10. Hash Requirements

### 10.1 Algorithm

Every canonical artifact admitted to a conformant record SHALL have a SHA-256 digest computed from the exact file bytes preserved in the controlled archive.

The digest SHALL be represented as 64 lowercase hexadecimal characters.

Example format:

```text
3fe43f4410a6dbc2a7f6b93c6247cedf3a14b892146fdb86f338cd416b68359e
```

### 10.2 Manifest

A multi-artifact provenance package SHALL include a manifest in the following form:

```text
<sha256>  <exact filename>
```

Two spaces SHOULD separate the digest and filename for compatibility with common checksum-manifest conventions.

### 10.3 Revisions

Any byte-level modification to an artifact SHALL produce a new SHA-256 digest.

A modified artifact SHALL NOT continue to be represented by the previous digest.

If the modification constitutes a controlled revision, the artifact version SHOULD be incremented and a new provenance entry or corrected record SHALL document the relationship.

### 10.4 Verification

A conformant record SHALL provide enough information for an independent party to reproduce the digest comparison.

A matching digest establishes byte-for-byte identity with the hashed file state. It SHALL NOT be described as proving the truth, originality, authorship, validity, legality, or quality of the artifact's contents.

---

## 11. Controlled Archive Requirements

Every artifact represented by a `Published` record SHALL have a controlled archived copy preserved outside the prose of the registry entry.

The archive SHALL preserve the exact bytes from which the recorded digest was generated.

The archive location MAY be private where public distribution would create confidentiality, privacy, security, licensing, or research-integrity concerns.

A private archive SHALL NOT prevent publication of a provenance record when the public record can identify the artifact and digest without exposing restricted content.

A provenance record SHALL NOT imply that GitHub itself contains the underlying artifact unless the artifact is actually present in the repository.

---

## 12. Evidence Boundary

Every `Published` record SHALL include an explicit evidentiary boundary.

At minimum, the boundary SHALL communicate that cryptographic hashes and Git history may support evidence of exact file identity and repository chronology but do not independently establish:

1. originality or novelty;
2. priority of authorship;
3. intellectual-property ownership;
4. truth of claims inside an artifact;
5. causation or hidden system behavior;
6. empirical or scientific validity;
7. institutional sponsorship, endorsement, or approval;
8. regulatory compliance;
9. standards-body adoption;
10. production readiness; or
11. legal entitlement or liability.

Where an artifact creates additional risk of misinterpretation, the record SHALL add artifact-specific boundaries.

---

## 13. Claim Classification

Statements in a provenance record SHALL be distinguishable as one of the following where classification is material:

| Classification | Definition |
|---|---|
| `Verified fact` | Directly supported by inspectable evidence |
| `Interpretation` | Reasoned reading of verified information |
| `Reasonable inference` | Conclusion supported indirectly but not established as fact |
| `Unsupported claim` | Assertion lacking sufficient supporting evidence |
| `Unknown` | Evidence does not permit a defensible determination |
| `Proposal` | Normative or design recommendation not represented as an observed fact |

A registry entry SHALL NOT convert interpretation, repetition, emotional intensity, coincidence, symbolism, persuasive language, or AI-generated language into verified evidence.

Unsupported claims SHOULD be removed from active provenance records unless their presence is necessary to document historical material. When retained for historical reasons, they SHALL be labeled accordingly.

---

## 14. Institutional and External Claims

A provenance record SHALL NOT state or imply institutional sponsorship, appointment, partnership, approval, adoption, validation, or endorsement without documentary evidence supporting the exact relationship claimed.

Participation, discussion, submission, review, membership, affiliation, employment, and formal institutional endorsement SHALL NOT be treated as interchangeable states.

External validation SHALL identify, where disclosure is appropriate:

- the validating party;
- the object evaluated;
- the evaluation method or authority;
- the date;
- the scope of the determination; and
- material limitations.

---

## 15. Sensitive and Restricted Evidence

The public registry SHALL NOT expose confidential participant information, authentication credentials, private keys, security secrets, protected educational records, medical information, intimate personal material, or other information whose disclosure would create unjustified privacy or security risk.

Sensitive source evidence MAY be represented through a cryptographic digest and controlled internal identifier without publishing the underlying content.

Redaction SHALL produce a different file and therefore a different SHA-256 digest from the unredacted source.

The registry SHALL distinguish between the digest of an original restricted artifact and the digest of any public redacted derivative.

---

## 16. Corrections and Supersession

Published provenance records SHALL NOT be silently rewritten in a way that obscures material changes.

Corrections SHALL use Git history to preserve the earlier state and SHOULD explain material changes in the commit message or record revision note.

When an artifact is superseded:

1. the earlier artifact SHALL remain identifiable;
2. its original digest SHALL remain preserved;
3. the later artifact SHALL receive its own digest;
4. the relationship SHOULD be documented as `Supersedes` / `Superseded by`; and
5. the earlier record SHALL NOT be rewritten to imply that the later artifact existed at the earlier date.

---

## 17. Acceptance Criteria

A provenance record SHALL satisfy all applicable criteria below before it is designated `Published`.

### AC-01 — Identity

The record has a unique conformant Record ID.

### AC-02 — Scope

The record clearly defines the artifacts or reporting period represented.

### AC-03 — Exact filenames

Every artifact is identified by the exact filename corresponding to the hashed file.

### AC-04 — Maturity

Every artifact has a defensible maturity state that does not exceed available evidence.

### AC-05 — Integrity

A SHA-256 digest has been computed from every exact archived artifact.

### AC-06 — Digest format

Every digest is a valid 64-character lowercase hexadecimal SHA-256 value.

### AC-07 — Archive

The exact hashed files have been preserved in a controlled archive.

### AC-08 — Reproducibility

The record contains sufficient instructions for an independent digest comparison.

### AC-09 — Evidence boundary

The record explicitly states the limits of what its hashes and Git history establish.

### AC-10 — Claim discipline

No statement materially exceeds the evidence available to support it.

### AC-11 — Institutional boundary

No unsupported sponsorship, endorsement, validation, adoption, partnership, or approval claim appears in the record.

### AC-12 — Privacy and security

The public record contains no unjustified sensitive or restricted information.

### AC-13 — Public chronology

The completed provenance record has been committed to the public registry.

### AC-14 — Registry indexing

The record is linked from the repository registry index when it is intended to be part of the active registry.

### AC-15 — Final review

The record has been checked for filename/hash mismatch, maturity overstatement, unsupported claims, broken internal links, and material metadata omissions.

Failure of any applicable acceptance criterion SHALL block `Published` status until corrected.

---

## 18. Pre-Publication Conformance Checklist

Before publication, the maintainer SHALL be able to answer **YES** to every applicable item:

```text
[ ] Record ID is unique and correctly formatted.
[ ] Reporting/reference date is explicit.
[ ] Scope is defined.
[ ] Exact canonical filenames are recorded.
[ ] Artifact maturity states are evidence-supported.
[ ] SHA-256 was computed from the archived files.
[ ] Every digest is 64 lowercase hexadecimal characters.
[ ] Manifest filenames match the archived filenames exactly.
[ ] Exact hashed files are preserved.
[ ] Verification instructions are present.
[ ] Evidence boundary is present.
[ ] No unsupported institutional claims are present.
[ ] No maturity state exceeds available evidence.
[ ] Sensitive information has been excluded or appropriately controlled.
[ ] Corrections/supersession relationships are documented where applicable.
[ ] Public Git commit exists.
[ ] Active registry index is updated.
[ ] Final claim-discipline review is complete.
```

---

## 19. Minimum Conformant Record Template

```markdown
# [Record Title]

**Record ID:** EII-[CLASS]-[REFERENCE]  
**Version:** [version]  
**Status:** [Draft | Incomplete | Published | Corrected | Superseded | Withdrawn | Historical]  
**Reference date:** YYYY-MM-DD  
**Maintainer:** [maintainer]  
**Integrity method:** SHA-256

## Scope

[Define exactly what this record represents.]

## Artifact Register

| Artifact | Type | Maturity | SHA-256 |
|---|---|---|---|
| `filename.ext` | [type] | [state] | `[digest]` |

## Status

[State the actual maturity and unresolved limitations.]

## Verification

[Provide reproducible SHA-256 verification instructions.]

## Evidence Boundary

[State what the record establishes and what it does not establish.]

## Archive

[Identify the controlled archive without exposing restricted information.]

## Public Record

**Commit:** `[commit SHA]`
```

---

## 20. Governance of This Schema

Changes to this specification SHALL be version-controlled.

A material change to mandatory metadata, maturity definitions, integrity requirements, evidence boundaries, or acceptance criteria SHALL increment the schema version.

Earlier provenance records SHALL NOT be retroactively represented as having satisfied requirements that did not exist when those records were published. They MAY be reassessed against a newer schema if the reassessment is explicitly documented.

The current schema SHALL be the controlling reference for provenance records created after its effective date.

---

## 21. Conformance Statement

A record MAY state:

> **EII Registry Conformance:** This provenance record was reviewed against EII-REG-SCHEMA-001 and satisfied all applicable acceptance criteria at the time of publication.

That statement SHALL be used only after AC-01 through AC-15 have been evaluated and every applicable criterion has passed.

---

**Emotional Infrastructure Institute**  
*Public provenance, artifact integrity, claim discipline, and longitudinal research traceability.*
