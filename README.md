# Emotional Infrastructure Institute

## Public Provenance Registry

**Repository:** `emotionalinfrastructure/proof-of-signal`  
**Maintainer:** Brittany Wright, Founder, Emotional Infrastructure Institute  
**Primary function:** Artifact integrity, chronology, version traceability, and public research provenance  
**Integrity method:** SHA-256 and Git commit history

---

### Registry Purpose

This repository is the public provenance registry of the **Emotional Infrastructure Institute (EII)**. It preserves controlled records linking selected research, governance, technical, and organizational artifacts to cryptographic identifiers and dated Git history.

The registry is designed to answer a narrow set of verifiable questions:

1. What artifact was recorded?
2. Which version or file state was represented?
3. What cryptographic identifier corresponds to that exact file?
4. When was the integrity record committed publicly?
5. What development status and evidentiary boundary applied at that time?

The repository is therefore an **evidence-management and provenance surface**, not a substitute for peer review, empirical validation, standards adoption, institutional approval, regulatory assessment, or legal adjudication.

---

## Provenance Model

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

Each completed registry entry should preserve enough information for an independent reviewer to identify the represented artifact, reproduce its cryptographic digest from the corresponding file, and determine the status asserted at the time of publication.

---

## Registry

| Reporting Period | Record | Integrity Method | Status |
|---|---|---|---|
| 2026-08-28 | [`EII-WPR-2026-08-28`](weekly-proof/2026-08-28.md) | SHA-256 | Published |

Additional records will be added as controlled provenance packages are completed.

---

## What a Registry Record Contains

A professional EII provenance record may contain:

| Field | Function |
|---|---|
| **Record ID** | Stable identifier for the provenance record |
| **Reporting period** | Time boundary associated with the recorded work |
| **Artifact name** | Exact filename or controlled artifact identifier |
| **Version/status** | Development state represented by the record |
| **SHA-256** | Cryptographic digest of the exact file bytes |
| **Evidence boundary** | Explicit statement of what the record does and does not establish |
| **Git history** | Public chronology of the registry entry and subsequent revisions |

Where appropriate, records may also identify supporting archives, specifications, validation packages, implementation artifacts, or related evidence records.

---

## Verification

SHA-256 digests are used to identify exact file states. To verify an artifact:

```bash
sha256sum <filename>
```

On macOS:

```bash
shasum -a 256 <filename>
```

Compare the resulting digest with the value recorded in the corresponding registry entry. A matching digest indicates that the file being examined is byte-for-byte identical to the file represented by that cryptographic identifier.

A hash mismatch means the file is different. It does not, by itself, determine why the file differs or whether the difference is authorized.

---

## Evidentiary Boundary

This registry uses cryptographic integrity records and Git history as **provenance evidence with defined limits**.

A matching SHA-256 digest can establish that two file instances are byte-for-byte identical. Git history can establish repository chronology and show that particular content was committed to this repository at a recorded point in its history.

These mechanisms do **not**, independently, establish:

- originality or novelty;
- priority of authorship;
- ownership of intellectual property;
- truth of claims contained inside an artifact;
- causation or hidden system behavior;
- empirical or scientific validity;
- institutional sponsorship, endorsement, or approval;
- regulatory compliance;
- standards-body adoption;
- production readiness; or
- legal entitlement or liability.

Those determinations require evidence and procedures appropriate to the specific claim being evaluated.

---

## Research and Governance Context

**Emotional Infrastructure™** is a governance framework for AI-mediated trust environments. The work examines how automated and adaptive communication systems can shape trust, reliance, interpretation, disclosure, consent, and decision-making across repeated interactions, and how those effects can be made more visible, reviewable, contestable, and accountable.

EII's broader research and implementation work includes longitudinal AI interaction governance, disclosure architecture, consent boundaries, auditability, human review pathways, behavioral-signal governance, trust receipts, and mechanisms for preserving human agency in AI-assisted environments.

Artifacts represented in this registry may exist at different maturity levels. A registry entry therefore records development status explicitly rather than treating publication, hashing, or repository inclusion as evidence that an artifact has been validated or adopted.

---

## Historical Repository Notice

This repository originated in 2025 under the name **Proof of Signal** and contains legacy material from an earlier stage of development. Some historical files or commits may use terminology, interpretations, or claims that are **not part of EII's current research position**.

The repository's current function is narrower and more rigorous: preservation of artifact integrity, chronology, version lineage, and public provenance.

Historical material is retained as part of the repository record. Its presence should not be interpreted as current endorsement of every statement contained in earlier versions. Current EII positions should be determined from the latest controlled records and current publications.

---

## Record-Control Principles

EII provenance records follow five operating principles:

**Integrity.** Hashes identify exact artifact states rather than general document titles.

**Traceability.** Records connect artifacts, versions, integrity identifiers, archives, and public chronology.

**Status discipline.** Candidate, draft, pilot, validated, adopted, and deployed states are not treated as interchangeable.

**Claim discipline.** The evidentiary meaning of a hash, timestamp, commit, test, or research artifact is stated narrowly and explicitly.

**Preservation.** Historical records are preserved without allowing superseded claims to silently define the Institute's current position.

---

## Current Registry Entry

### EII-WPR-2026-08-28

The first controlled weekly record under the professionalized registry documents selected artifacts from the week ending August 28, 2026, including Observatory pilot-validation materials and organizational planning artifacts.

**Record:** [`weekly-proof/2026-08-28.md`](weekly-proof/2026-08-28.md)

The Observatory materials represented by that record remain at the controlled pre-execution / human-execution gate. Formal evaluator observations and empirical validation remain pending.

---

## About the Emotional Infrastructure Institute

The **Emotional Infrastructure Institute** develops research, governance methods, evaluation instruments, and implementation approaches for AI-mediated trust environments. Its work focuses on disclosure, consent, auditability, human review, contestability, behavioral-signal governance, and longitudinal accountability.

The Institute's operating objective is to translate governance problems into mechanisms that can be documented, tested, evaluated, and improved without overstating the maturity or evidentiary status of the underlying work.

---

### Repository Status

`ACTIVE PROVENANCE REGISTRY`

Last structural revision: **2026-08-28**

---

**Emotional Infrastructure Institute**  
*Governance infrastructure for AI-mediated trust, human agency, and longitudinal accountability.*
