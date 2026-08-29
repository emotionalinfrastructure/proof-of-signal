# Emotional Infrastructure Institute

## Public Provenance Registry

**Repository:** `emotionalinfrastructure/proof-of-signal`  
**Maintainer:** Brittany Wright, Founder, Emotional Infrastructure Institute  
**Primary function:** Artifact integrity, chronology, version traceability, and public research provenance  
**Integrity method:** SHA-256 and Git commit history

---

### Registry Purpose

This repository is the public provenance registry of the **Emotional Infrastructure Institute (EII)**. It preserves controlled records linking selected research, governance, technical, and organizational artifacts to cryptographic identifiers and dated Git history.

The registry is designed to answer a narrow set of verifiable questions: what artifact was recorded, which version was represented, what cryptographic identifier corresponds to the exact file, when the integrity record entered public Git history, and what maturity and evidentiary boundaries applied at that time.

The repository is an **evidence-management and provenance surface**, not a substitute for peer review, empirical validation, standards adoption, institutional approval, regulatory assessment, or legal adjudication.

---

## Registry Control Surface

| Control | Function |
|---|---|
| [`REGISTRY-SCHEMA.md`](REGISTRY-SCHEMA.md) | Normative admission, maturity, hashing, evidence-boundary, and acceptance requirements |
| [`REGISTRY-INDEX.md`](REGISTRY-INDEX.md) | Canonical human-readable ledger of admitted provenance records |
| [`registry-index.json`](registry-index.json) | Machine-readable companion registry |
| [`registry-index.schema.json`](registry-index.schema.json) | JSON Schema for structural validation of the machine-readable registry |
| [`RECORD-TEMPLATE.md`](RECORD-TEMPLATE.md) | Controlled starting template for future provenance records |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Admission workflow, commit conventions, and correction controls |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Registry stewardship, hierarchy, versioning, and change control |
| [`SECURITY.md`](SECURITY.md) | Integrity-defect and sensitive-disclosure guidance |

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
   ↓
Registry Index
```

Each admitted registry entry is intended to preserve enough information for an independent reviewer to identify the represented artifact, reproduce its cryptographic digest from the corresponding file when that file is available, inspect its stated maturity, and understand the limits of the evidence being presented.

---

## Active Registry

| Reporting Period | Record | Integrity Method | Status |
|---|---|---|---|
| 2026-08-28 | [`EII-WPR-2026-08-28`](weekly-proof/2026-08-28.md) | SHA-256 | Published |

The authoritative master ledger is maintained in [`REGISTRY-INDEX.md`](REGISTRY-INDEX.md). Automated consumers SHOULD use [`registry-index.json`](registry-index.json) and validate its structure against [`registry-index.schema.json`](registry-index.schema.json).

---

## Verification

SHA-256 digests identify exact file states. A verifier with access to a represented artifact can compute its digest and compare the result with the value recorded in the corresponding provenance record.

Linux:

```bash
sha256sum <filename>
```

macOS:

```bash
shasum -a 256 <filename>
```

A matching digest indicates that the file being examined is byte-for-byte identical to the file represented by that cryptographic identifier. A mismatch establishes only that the bytes differ; it does not determine why they differ or whether the difference is authorized.

---

## Evidentiary Boundary

This registry uses cryptographic integrity records and Git history as **provenance evidence with defined limits**.

A matching SHA-256 digest can establish byte-for-byte identity. Git history can establish repository chronology and show that particular content appeared in this repository at a recorded point in its history.

These mechanisms do **not**, independently, establish originality, novelty, priority of authorship, intellectual-property ownership, truth of claims contained inside an artifact, causation or hidden system behavior, empirical validity, institutional sponsorship or approval, regulatory compliance, standards-body adoption, production readiness, or legal entitlement.

Those determinations require evidence and procedures appropriate to the claim being evaluated.

---

## Research and Governance Context

**Emotional Infrastructure™** is a governance framework for AI-mediated trust environments. The work examines how automated and adaptive communication systems can shape trust, reliance, interpretation, disclosure, consent, and decision-making across repeated interactions, and how those effects can be made more visible, reviewable, contestable, and accountable.

EII's broader work includes longitudinal AI interaction governance, disclosure architecture, consent boundaries, auditability, human review pathways, behavioral-signal governance, trust receipts, and mechanisms for preserving human agency in AI-assisted environments.

Artifacts represented in this registry may exist at different maturity levels. Registry inclusion therefore records provenance and status rather than treating publication, hashing, or repository inclusion as evidence that an artifact has been validated or adopted.

---

## Historical Repository Notice

This repository originated in 2025 under the name **Proof of Signal** and contains legacy material from an earlier stage of development. Some historical files or commits may use terminology, interpretations, or claims that are **not part of EII's current research position**.

The repository's current function is narrower and more rigorous: preservation of artifact integrity, chronology, version lineage, and public provenance.

Historical material is retained as part of the repository record. Its presence should not be interpreted as current endorsement of every statement contained in earlier versions. Current EII positions should be determined from the latest controlled records and current publications.

---

## Record-Control Principles

**Integrity.** Hashes identify exact artifact states rather than general document titles.

**Traceability.** Records connect artifacts, versions, integrity identifiers, archives, public chronology, and registry status.

**Status discipline.** Draft, candidate, pre-execution, pilot, evaluated, validated, adopted, and deployed states are not interchangeable.

**Claim discipline.** The evidentiary meaning of a hash, timestamp, commit, test, or research artifact is stated narrowly and explicitly.

**Preservation.** Historical records remain traceable without allowing superseded claims to silently define current EII positions.

**Machine consistency.** Human-readable and machine-readable registry surfaces are expected to represent the same admitted record set.

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

Control baseline: **EII-REG-SCHEMA-001 v1.0**  
Last structural revision: **2026-08-28**

---

**Emotional Infrastructure Institute**  
*Governance infrastructure for AI-mediated trust, human agency, and longitudinal accountability.*
