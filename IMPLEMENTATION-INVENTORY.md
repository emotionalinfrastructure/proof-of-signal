# EII Code-versus-Spec Implementation Inventory

**Document ID:** EII-REG-IMPL-001  
**Version:** 1.0  
**Status:** Active implementation-control inventory  
**Controlling specification:** `EII-REG-SCHEMA-001 v1.0`  
**Architecture:** `EII-REG-ARCH-001 v1.0`  
**Coverage authority:** `TEST-MATRIX.md`  
**Repository:** `emotionalinfrastructure/proof-of-signal`

---

## 1. Purpose

This inventory separates requirements that exist only as written governance from requirements represented in machine-readable constraints, executable validation, adversarial tests, and continuous integration. Its purpose is to prevent architectural intent from being mistaken for implemented software behavior.

A requirement may occupy more than one implementation level. The highest level listed does not erase lower-level dependencies or remaining evidence boundaries.

---

## 2. Implementation Levels

| Level | Meaning |
|---|---|
| **Documentation Only** | Requirement exists as prose, policy, checklist, or human-review instruction. No deterministic software currently establishes the substantive condition. |
| **Machine-Readable** | All or part of the requirement is represented in a structured schema or canonical machine-readable registry field. |
| **Executable** | Repository code deterministically evaluates at least one material component and can return failure. |
| **Adversarially Tested** | Controlled positive/negative tests exercise the implemented control and demonstrate expected pass/fail behavior. |
| **CI-Enforced** | The executable control is invoked by the Registry Conformance GitHub Actions workflow when the relevant governed surface triggers the workflow. |

`CI-Enforced` means first-party automated enforcement of the implemented condition. It does not mean independent certification, external assurance, regulatory compliance, empirical validation, or complete satisfaction of requirements that retain manual components.

---

## 3. Acceptance-Criterion Implementation Inventory

| AC | Requirement | Documentation Only | Machine-Readable | Executable | Adversarially Tested | CI-Enforced | Exact Current Boundary |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| **AC-01** | Unique conformant Record ID | ✓ | ✓ | ✓ | ✓ | ✓ | Format, record-type consistency, uniqueness, and verification-record ID presence are executable. Semantic appropriateness of the selected logical identity remains a governance judgment. |
| **AC-02** | Scope clearly defines represented artifacts or period | ✓ | ✓ |  |  |  | Registry fields structurally carry scope-related information, but semantic clarity, completeness, and correctness of scope are not deterministically evaluated. |
| **AC-03** | Exact artifact filenames correspond to hashed files | ✓ |  | ✓ | ✓ | ✓ | Artifact Register parser requires exact basename-only, unique filenames. Fixture tests reject paths and duplicates. Correspondence to external/restricted archive bytes cannot be established when those bytes are unavailable to the validator. |
| **AC-04** | Maturity does not exceed evidence | ✓ | ✓ | ✓ | ✓ | ✓ | Allowed maturity vocabulary is machine constrained and invalid vocabulary is rejected. Whether the selected allowed state is substantively supported by evidence remains manual. |
| **AC-05** | SHA-256 computed from every exact archived artifact | ✓ |  | ✓ | ✓ | ✓* | `verify_artifact_bytes()` recomputes SHA-256 and fails on byte mismatch when artifact bytes are available. Fixture bytes prove the mechanism. `*` Live/restricted artifact archives not present in CI cannot be recomputed, so global live-record integrity remains partial. |
| **AC-06** | Digest is 64 lowercase hexadecimal SHA-256 | ✓ | ✓ | ✓ | ✓ | ✓ | JSON/schema constraints and Artifact Register parsing enforce digest syntax. Malformed-digest fixtures fail closed. This establishes format, not truth of the declared digest unless bytes are recomputed under AC-05. |
| **AC-07** | Exact hashed files preserved in controlled archive | ✓ |  |  |  |  | Archive preservation is currently an operational/manual control. Public CI cannot prove continued existence or byte identity of artifacts held only in restricted/external archives. |
| **AC-08** | Sufficient instructions for independent digest comparison | ✓ | ✓ | ✓ | Partial | ✓* | Verification-path existence and related record structure are executable. `*` CI enforces implemented structural components, but semantic sufficiency and usability of the instructions remain human-reviewed. |
| **AC-09** | Explicit evidence boundary | ✓ |  | ✓ | Partial | ✓* | Validator requires an Evidence Boundary/Evidentiary Boundary heading. `*` CI enforces presence, not substantive completeness or adequacy of the boundary language. |
| **AC-10** | No material claim exceeds available evidence | ✓ | ✓ | Partial | Partial | ✓* | Maturity vocabulary and supersession-state contradictions are constrained. `*` CI enforces those deterministic components only. Substantive claim-evidence alignment remains manual. |
| **AC-11** | No unsupported institutional relationship claim | ✓ |  |  |  |  | No deterministic resolver currently establishes whether a sponsorship, endorsement, validation, adoption, partnership, appointment, or approval claim is supported by documentary evidence. |
| **AC-12** | No unjustified sensitive/restricted information | ✓ |  |  |  |  | Privacy/security rules are documented. No comprehensive deterministic secret/PII/sensitive-content scanning control is currently implemented in Registry Conformance CI. |
| **AC-13** | Completed provenance record committed publicly | ✓ | ✓ | ✓ | ✓ | ✓ | Validator requires the indexed Git commit to resolve and the verification record path to exist at that commit. Full-history CI supports this check. Publication-date-to-Git-time semantics and initial-publication-versus-current-revision separation remain unresolved. |
| **AC-14** | Published record linked from active registry index | ✓ | ✓ | ✓ | ✓ | ✓ | JSON/Markdown record-set equality and indexed family, maturity, date, schema, commit, supersession status, and verification path are compared. Additional canonical surfaces, if introduced, require separate synchronization controls. |
| **AC-15** | Final mismatch, maturity, claim, link, metadata review | ✓ | ✓ | Partial | Partial | ✓* | Multiple deterministic defect classes are CI-enforced. `*` Semantic claim review, external evidence assessment, privacy judgment, and other non-deterministic final-review functions remain manual. |

---

## 4. Requirement-Level Detail

### 4.1 Record identity and metadata

**Implemented in code:** Record-ID syntax, approved record classes, uniqueness, record-type consistency, selected required fields, Git SHA structure, verification paths, and structured registry values.

**Still specification/manual:** Whether a new Record ID represents the correct logical object; whether prose metadata accurately describes the real-world artifact or reporting period.

### 4.2 Artifact identity

**Implemented in code:** Artifact Register parsing; basename-only exact filename form; duplicate filename rejection; SHA-256 syntax validation.

**Adversarial evidence:** Controlled fixtures demonstrate rejection of path-based filenames, duplicate filenames, and malformed digests.

**Still specification/manual:** For artifacts outside the validator's accessible archive, the system cannot independently establish that the recorded filename and digest correspond to the retained external file.

### 4.3 Artifact byte integrity

**Implemented in code:** SHA-256 recomputation using exact bytes supplied to `verify_artifact_bytes()`; deterministic mismatch failure.

**Adversarial evidence:** Valid fixture bytes pass. Modified fixture bytes fail closed.

**Still bounded:** Live artifacts that are not available in the repository or CI environment are not automatically byte-recomputed. A declared hash for such an artifact remains provenance evidence subject to archive verification, not CI-proven exact-byte identity.

### 4.4 Maturity and claim discipline

**Implemented in machine-readable controls:** Approved maturity vocabulary and structural states.

**Implemented in code/tests:** Invalid maturity values and selected contradictory state relationships are rejected.

**Still specification/manual:** Evidence sufficiency for `Candidate`, `Pilot`, `Evaluated`, `Validated`, `Adopted`, `Deployed`, or other substantively meaningful states cannot be inferred from the label alone. Substantive overclaim detection remains human-governed.

### 4.5 Archive preservation

**Documentation only:** The specification requires preservation of exact hashed files in a controlled archive and distinguishes private archives from public repository storage.

**Not currently implemented:** No automated archive inventory, retention monitor, restricted-storage connector, or continuous byte-preservation check establishes AC-07 across external archives.

### 4.6 Reproducibility

**Implemented in code:** Verification-path existence, provenance-record structure, digest parsing, and other machine-inspectable prerequisites.

**Still manual:** Whether an independent reviewer could actually follow the prose instructions without missing context remains a usability and semantic-review question.

### 4.7 Evidence boundaries

**Implemented in code:** Required evidence-boundary section heading.

**Still manual:** Whether the boundary correctly addresses the risks of a particular artifact and avoids all material overinterpretation.

### 4.8 Institutional claims

**Documentation only:** Institutional relationships require evidence supporting the exact relationship claimed.

**Not currently implemented:** The repository has no trusted external evidence resolver capable of determining whether a named institution has actually sponsored, approved, adopted, validated, appointed, or endorsed an artifact or person.

### 4.9 Privacy and security

**Documentation only at the substantive level:** Sensitive and restricted evidence rules exist in `REGISTRY-SCHEMA.md` and `SECURITY.md`.

**Not currently implemented:** No comprehensive automated scanner currently establishes absence of credentials, private keys, protected records, intimate personal information, or other context-dependent sensitive material. Future deterministic scanning would still require a manual residual-risk boundary.

### 4.10 Git chronology

**Implemented in code:** `validate_git_chronology()` verifies that each indexed Git commit resolves and that the claimed verification path existed in that commit.

**Adversarial evidence:** Tests cover valid local Git history, nonexistent commits, and records absent from a claimed commit.

**CI requirement:** Full repository history is checked out using `fetch-depth: 0` so historical commit resolution can function.

**Still unresolved:** The validator does not yet prove that the indexed publication date equals or correctly relates to Git commit time, and the current registry model does not fully separate initial-publication commit from later current-revision commit.

### 4.11 Registry synchronization

**Implemented in code:** JSON and Markdown registry record sets must match. For each record, artifact family, maturity, publication date, controlling schema, commit SHA, supersession status, and verification path are compared.

**Adversarial evidence:** Controlled family and maturity divergence fixtures fail closed, alongside existing index-divergence tests.

**Still bounded:** If YAML or another canonical registry representation becomes authoritative, it will require its own parser and cross-surface synchronization control.

### 4.12 Final review

**Partially executable:** Structural, identity, digest, path, Git, supersession, and index synchronization defects can block CI.

**Still manual:** Semantic accuracy, external evidence, substantive claim discipline, institutional assertions, privacy judgments, and other context-sensitive final-review functions.

---

## 5. Executable Components

The repository currently contains actual executable implementation, not only architecture prose.

| Component | Executable Function |
|---|---|
| `registry-index.schema.json` | Machine-validates structured registry fields, required properties, formats, patterns, and enumerations. |
| `scripts/validate_registry.py` | Performs deterministic structural, logical, Artifact Register, synchronization, and Git-history validation; exits nonzero on defined violations. |
| `tests/test_registry_conformance.py` | Executes positive and adversarial tests against validator behavior. |
| `tests/fixtures/**` | Supplies controlled known-valid and deliberately invalid inputs and exact artifact bytes. |
| `.github/workflows/registry-conformance.yml` | Executes validator and tests in GitHub Actions and propagates failures to CI status. |

These components constitute an executable provenance/conformance subsystem. They do not constitute a production AI-governance runtime and do not currently intercept, classify, constrain, or modify live AI-model behavior.

---

## 6. Specification-Only or Predominantly Manual Components

The following substantive areas remain primarily governance specification rather than implemented software behavior:

- semantic scope sufficiency under AC-02;
- evidence-supported maturity selection under AC-04;
- continuous controlled-archive preservation under AC-07;
- semantic sufficiency of verification instructions under AC-08;
- substantive completeness of evidence boundaries under AC-09;
- general claim-evidence alignment under AC-10;
- documentary verification of institutional/external claims under AC-11;
- comprehensive sensitive-information determination under AC-12;
- publication-date semantics and initial-publication/current-revision distinction under AC-13; and
- non-deterministic portions of final review under AC-15.

These requirements SHALL NOT be described as software-enforced until corresponding executable controls exist and their boundaries are tested.

---

## 7. CI Enforcement Boundary

Registry Conformance CI currently executes the deterministic validator and fixture-driven test suite. A green workflow run means the repository state satisfied the implemented checks during that execution.

It does not mean every SHALL in `REGISTRY-SCHEMA.md` has been automated. It does not establish that restricted archives were inspected when their bytes were unavailable. It does not establish substantive truth, originality, authorship, intellectual-property ownership, research validity, institutional approval, regulatory compliance, or external certification.

The implementation hierarchy SHALL therefore be read as:

```text
Documentation Only
        ↓
Machine-Readable
        ↓
Executable
        ↓
Adversarially Tested
        ↓
CI-Enforced
```

Movement downward in this hierarchy requires additional implementation evidence. Written intent alone SHALL NOT advance a requirement to a higher level.

---

## 8. Current Implementation Determination

The EII Public Provenance Registry is currently a hybrid governance-and-software system.

It contains a substantive written specification layer, machine-readable registry and schema surfaces, executable Python validation, controlled adversarial fixtures, executable unit tests, and GitHub Actions continuous enforcement. Several acceptance criteria are therefore genuinely implemented in code at bounded levels.

At the same time, significant requirements remain documentation-only or partially automated because they depend on external archives, semantic evidence evaluation, privacy judgment, institutional evidence, or other conditions not defensibly reducible to the current deterministic validator.

The correct current description is:

> **The repository contains an executable provenance and conformance-control subsystem with adversarially tested and CI-enforced controls for defined deterministic requirements, alongside governance requirements that remain manual or only partially automated.**

It SHALL NOT be described as a complete implementation of every EII governance requirement or as a production runtime implementation of the broader Emotional Infrastructure architecture.

---

## 9. Update Rule

This inventory SHALL be updated whenever a requirement moves between implementation levels, a new executable control is added, an adversarial test is introduced or removed, CI enforcement changes, or an existing automation boundary is materially narrowed or expanded.

No requirement SHALL be upgraded solely because implementation is planned, described in `ARCHITECTURE.md`, represented by a placeholder function, or named in a test. The repository SHALL contain functioning behavior and appropriate evidence before the higher implementation level is assigned.
