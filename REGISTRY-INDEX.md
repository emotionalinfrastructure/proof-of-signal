# EII Public Provenance Registry Index

**Document ID:** EII-REG-INDEX-001  
**Version:** 1.0  
**Status:** Active  
**Controlling specification:** [`EII-REG-SCHEMA-001`](REGISTRY-SCHEMA.md)  
**Maintainer:** Emotional Infrastructure Institute  
**Repository:** `emotionalinfrastructure/proof-of-signal`  
**Last updated:** 2026-08-28

---

## 1. Registry Function

This document is the canonical master index for provenance records admitted to the Emotional Infrastructure Institute (EII) Public Provenance Registry.

The index is designed for both human review and straightforward machine extraction. Each active row identifies a discrete provenance record, its artifact family, the maturity represented by that record, its publication date, the schema governing admission, the Git commit associated with publication or the current controlled revision, supersession state, and the direct verification record.

Inclusion in this index means that the provenance record has been admitted to the active registry. Inclusion SHALL NOT be interpreted as independent validation of the underlying research, artifact, framework, implementation, organization, or claim.

---

## 2. Canonical Registry Ledger

| Record ID | Artifact Family | Artifact Maturity | Publication Date | Schema | Commit SHA | Supersession | Verification |
|---|---|---|---|---|---|---|---|
| `EII-WPR-2026-08-28` | EII-TIO Observatory pilot validation; EII organizational planning | Candidate / Pre-execution | `2026-08-28` | `EII-REG-SCHEMA-001 v1.0` | [`c39d83d09e5dbb23ac8cb8c67fa2100df959a511`](https://github.com/emotionalinfrastructure/proof-of-signal/commit/c39d83d09e5dbb23ac8cb8c67fa2100df959a511) | Active | [`weekly-proof/2026-08-28.md`](weekly-proof/2026-08-28.md) |

---

## 3. Machine-Readable Registry Block

The fenced block below mirrors the canonical ledger using a stable, line-oriented YAML representation. It is intended to support lightweight parsing without making the Markdown table itself the only structured source.

```yaml
registry:
  id: EII-REG-INDEX-001
  version: "1.0"
  schema: EII-REG-SCHEMA-001
  schema_version: "1.0"
  updated: "2026-08-28"
  records:
    - record_id: EII-WPR-2026-08-28
      artifact_family:
        - EII-TIO Observatory pilot validation
        - EII organizational planning
      artifact_maturity:
        - Candidate
        - Pre-execution
      publication_date: "2026-08-28"
      controlling_schema: EII-REG-SCHEMA-001
      controlling_schema_version: "1.0"
      commit_sha: c39d83d09e5dbb23ac8cb8c67fa2100df959a511
      supersession_status: Active
      verification_record: weekly-proof/2026-08-28.md
```

The Markdown ledger and machine-readable block SHALL describe the same admitted record set. A material mismatch between them SHALL be treated as a registry defect and corrected before the index is represented as current.

---

## 4. Field Definitions

| Field | Definition |
|---|---|
| `record_id` | Unique registry identifier assigned under EII-REG-SCHEMA-001 |
| `artifact_family` | Research, technical, governance, organizational, or other controlled artifact family represented by the provenance record |
| `artifact_maturity` | Defensible maturity state of the underlying artifact or artifact set; not the publication status of the provenance record |
| `publication_date` | Date on which the provenance record entered the public registry |
| `controlling_schema` | Registry specification governing admission and interpretation |
| `controlling_schema_version` | Version of the controlling specification applied to the record |
| `commit_sha` | Git commit associated with publication or current controlled revision of the provenance record |
| `supersession_status` | Current relationship of the record to later registry records |
| `verification_record` | Repository path containing the artifact register, hashes, status language, verification instructions, and evidence boundary |

---

## 5. Supersession Vocabulary

The `supersession_status` field SHALL use one of the following values:

| Value | Meaning |
|---|---|
| `Active` | Current provenance record for the represented scope |
| `Partially Superseded` | Some, but not all, represented scope has been replaced by later controlled records |
| `Superseded` | Replaced by a later controlled provenance record |
| `Withdrawn` | Removed from active use while retained for chronology |
| `Historical` | Retained for provenance but not governed as a current active record |

When a record becomes `Superseded` or `Partially Superseded`, the index SHOULD identify the succeeding Record ID in an adjacent note or future dedicated relationship field.

---

## 6. Admission Rule

A provenance record SHALL NOT be added to the Canonical Registry Ledger until the maintainer has evaluated the applicable acceptance criteria in [`REGISTRY-SCHEMA.md`](REGISTRY-SCHEMA.md).

For records governed by EII-REG-SCHEMA-001 v1.0, admission requires satisfaction of applicable AC-01 through AC-15, including artifact identity, scope, exact filenames, defensible maturity, SHA-256 integrity, controlled archival preservation, reproducible verification, evidence boundaries, claim discipline, institutional boundaries, privacy/security review, public chronology, registry indexing, and final review.

If a mandatory criterion is unresolved, the record SHALL remain outside the active ledger or be clearly identified as nonconformant draft/historical material.

---

## 7. Index Update Rule

Every newly admitted provenance record SHALL trigger an update to this index.

An index update SHALL:

1. add the new Record ID to the Markdown ledger;
2. add the same record to the machine-readable block;
3. identify the controlling schema version;
4. record the relevant Git commit SHA;
5. identify the verification-record path;
6. update supersession relationships where applicable; and
7. update the `Last updated` date.

The index SHALL NOT silently remove earlier admitted records. Records leaving active status SHALL remain represented with an appropriate supersession or historical state unless removal is required for a documented legal, privacy, or security reason.

---

## 8. Integrity Interpretation

This index is a directory of provenance records. It does not reproduce every artifact hash. Cryptographic verification SHALL be performed against the artifact register contained in the linked verification record.

The relationship is:

```text
REGISTRY-INDEX.md
      ↓
Provenance Record
      ↓
Artifact Register
      ↓
SHA-256 Digest
      ↓
Controlled Artifact
```

A Git commit SHA identifies repository history. A SHA-256 artifact digest identifies exact artifact bytes. These identifiers serve different evidentiary functions and SHALL NOT be treated as interchangeable.

---

## 9. Historical Material

Files and commits predating the professional EII provenance registry MAY remain in repository history without appearing in the active ledger.

Absence from this index means only that the material has not been admitted as an active conformant provenance record under the controlling registry process. It SHALL NOT be interpreted as deletion of history or a determination regarding the underlying material's authorship, validity, ownership, or significance.

Historical materials MAY later receive an `HPR` record if preservation, classification, or clarification warrants formal registry treatment.

---

## 10. Current Registry State

**Active admitted records:** 1  
**Superseded records:** 0  
**Withdrawn records:** 0  
**Historical records admitted under schema:** 0  
**Controlling schema:** EII-REG-SCHEMA-001 v1.0

The first active record, `EII-WPR-2026-08-28`, preserves the integrity record for selected work from the week ending August 28, 2026. The underlying Observatory materials remain candidate/pre-execution work; their inclusion in this registry does not convert them into validated or institutionally adopted artifacts.

---

## 11. Registry Evidence Boundary

The registry index establishes an organized public directory of admitted provenance records and their repository chronology. It does not independently establish originality, novelty, priority of authorship, intellectual-property ownership, empirical validity, institutional sponsorship or approval, regulatory compliance, standards adoption, production readiness, causation, or legal entitlement.

Those determinations require evidence and procedures appropriate to the claim being evaluated.

---

**Emotional Infrastructure Institute**  
*Public provenance, artifact integrity, claim discipline, and longitudinal research traceability.*
