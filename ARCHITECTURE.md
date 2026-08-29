# EII Public Provenance Registry Architecture

**Document ID:** EII-REG-ARCH-001  
**Version:** 1.0  
**Status:** Active architecture description  
**System:** EII Public Provenance Registry  
**Controlling specification:** `EII-REG-SCHEMA-001`  
**Related controls:** `REGISTRY-INDEX.md`, `registry-index.json`, `registry-index.schema.json`, `TEST-MATRIX.md`, `RECORD-TEMPLATE.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`  
**Executable controls:** `scripts/validate_registry.py`, `tests/test_registry_conformance.py`, `.github/workflows/registry-conformance.yml`

---

## 1. Purpose

The EII Public Provenance Registry is a controlled evidence system for establishing inspectable relationships among an artifact, its exact-byte cryptographic digest, its provenance record, its registry entry, and the public Git history in which that evidence is recorded.

The architecture is designed to convert selected provenance requirements from descriptive policy into executable controls. It separates specification, evidence, enforcement, and continuous verification so that a governance rule is not treated as technically enforced merely because it appears in documentation.

The registry does not establish authorship, originality, intellectual-property ownership, empirical validity, regulatory compliance, institutional approval, or external certification. Its technical purpose is narrower: preserve and expose evidence about identified artifact states, detect defined integrity and consistency failures, and maintain a publicly inspectable change history.

---

## 2. Architectural Principles

The registry SHALL maintain separation between governance requirements and the software that evaluates those requirements. It SHALL distinguish artifact evidence from claims made about that evidence. Machine-readable and human-readable registry surfaces SHALL remain synchronized for fields subject to deterministic validation. Automated controls SHALL fail closed for defined nonconformant states. A passing automated check SHALL be interpreted only within the scope of the controls actually implemented and tested.

Where an acceptance criterion cannot be fully automated, the system SHALL identify the remaining manual or evidentiary boundary rather than silently treating partial automation as complete conformance.

---

## 3. Four-Layer Control Architecture

### 3.1 Layer One: Specification

The specification layer defines what a conformant registry state is intended to mean.

Primary components:

- `REGISTRY-SCHEMA.md`
- `registry-index.schema.json`
- `GOVERNANCE.md`
- `SECURITY.md`
- `CONTRIBUTING.md`
- `RECORD-TEMPLATE.md`

`REGISTRY-SCHEMA.md` is the human-readable normative control specification. It defines record structure, evidence expectations, acceptance criteria, integrity requirements, claim boundaries, supersession behavior, and conformance concepts.

`registry-index.schema.json` converts selected structural requirements into machine-enforceable JSON constraints. It can reject invalid required fields, enumerations, formats, identifiers, and other representational defects before higher-order logical validation occurs.

`GOVERNANCE.md`, `SECURITY.md`, and `CONTRIBUTING.md` define the operating environment around the registry: authority, change control, correction procedures, security boundaries, and controlled contribution practices. `RECORD-TEMPLATE.md` provides the standardized structure from which future provenance records are constructed.

The specification layer answers:

> What SHALL a valid registry state contain, and what rules govern its creation and maintenance?

It does not itself prove that those rules have been followed.

### 3.2 Layer Two: Evidence and Registry State

The evidence layer contains the actual provenance assertions and the indexes through which those assertions are exposed.

Primary components:

- `weekly-proof/**` and future admitted provenance-record families
- artifact registers embedded in provenance records
- SHA-256 digests associated with exact artifact filenames
- `registry-index.json`
- `REGISTRY-INDEX.md`
- controlled artifact archives when available
- Git commits containing public provenance states

A provenance record identifies the artifact set being represented, records the relevant maturity and evidentiary boundary, associates exact filenames with SHA-256 values, and supplies verification information.

`registry-index.json` is the structured registry surface consumed by automated validation. `REGISTRY-INDEX.md` is the human-readable ledger. Deterministic synchronization controls compare the two surfaces so that material indexed fields cannot diverge without causing validation failure.

The evidence layer answers:

> What exact artifact state is being represented, where is its provenance record, and what integrity and chronology evidence accompanies it?

A SHA-256 digest identifies exact bytes with extremely high collision resistance. It does not independently establish who authored those bytes, when the underlying intellectual work began, whether the content is true, or whether a third party has accepted it.

### 3.3 Layer Three: Deterministic Enforcement

The enforcement layer evaluates registry state against machine-testable requirements.

Primary component:

- `scripts/validate_registry.py`

The validator currently performs multiple classes of control. It validates `registry-index.json` against the JSON Schema; checks record identity and record-type relationships; verifies uniqueness constraints; resolves verification paths; parses Artifact Registers; enforces basename-only and unique artifact filenames; validates lowercase 64-character SHA-256 syntax; checks evidence-boundary presence; validates supersession invariants; compares Markdown registry fields against JSON registry fields; and resolves indexed Git commits and provenance-record paths in repository history.

When controlled artifact bytes are available to the validator, `verify_artifact_bytes()` recomputes SHA-256 from those bytes and compares the result against the declared Artifact Register digest. This provides deterministic exact-byte integrity checking within the available archive boundary.

A defined violation SHALL produce a nonzero process exit. This is the fail-closed boundary used by continuous integration.

The enforcement layer answers:

> Does the current machine-inspectable state satisfy the deterministic controls that have actually been implemented?

It does not determine substantive research validity, legal ownership, institutional endorsement, or requirements that remain explicitly manual.

### 3.4 Layer Four: Adversarial Testing and Continuous Enforcement

The fourth layer verifies that the enforcement mechanism itself behaves correctly and ensures that relevant repository changes automatically invoke it.

Primary components:

- `tests/fixtures/**`
- `tests/test_registry_conformance.py`
- `TEST-MATRIX.md`
- `.github/workflows/registry-conformance.yml`

The fixture set supplies controlled valid and invalid evidence states. The test suite uses those fixtures to prove that known-valid conditions pass and defined malformed conditions are rejected. Current adversarial classes include malformed digests, modified artifact bytes, duplicate filenames, path-based filenames, Markdown/JSON divergence, invalid registry states, Git chronology failures, and provenance records absent from their claimed historical commits.

`TEST-MATRIX.md` maps those executable controls to the acceptance criteria in `EII-REG-SCHEMA-001`. It distinguishes Direct, Supporting, Partial, Manual, and bounded automation states so that test coverage itself is auditable.

The GitHub Actions workflow invokes deterministic validation and fixture-driven tests when the controlled repository surface changes. The workflow monitors registry specifications, indexes, control documents, provenance records, validator code, test code, fixtures, and the workflow definition itself.

The fourth layer answers:

> Does the validator reject the failure states it claims to reject, and are those controls automatically executed when the governed repository surface changes?

---

## 4. Architectural Flow

The system can be represented as the following control path:

```text
Artifact Creation
      |
      v
Canonical Artifact State
      |
      v
SHA-256 Generation
      |
      v
Artifact Register
(filename + status + digest)
      |
      v
Provenance Record
(scope + maturity + evidence boundary + verification data)
      |
      v
Registry Admission
      |
      +-----------------------------+
      |                             |
      v                             v
registry-index.json          REGISTRY-INDEX.md
      |                             |
      +-------------+---------------+
                    |
                    v
         Deterministic Validator
                    |
          +---------+---------+
          |                   |
          v                   v
   Structural Rules      Logical / Git Rules
          |                   |
          +---------+---------+
                    |
                    v
           Adversarial Test Suite
                    |
                    v
             GitHub Actions CI
                    |
             +------+------+
             |             |
          PASS            FAIL
             |             |
             v             v
   Public Git Evidence   Change rejected /
   remains inspectable   correction required
```

This flow is directional. Public provenance is the output of a controlled evidence process, not a substitute for the controls that precede it.

---

## 5. End-to-End Execution Path

### 5.1 Artifact creation and canonicalization

A substantive artifact is created or revised. Before provenance is recorded, the artifact state intended for preservation SHOULD be frozen as the canonical version for that evidence event. The filename used in the provenance record SHALL correspond to the represented artifact and SHALL be recorded as an exact basename under the current Artifact Register rules.

The registry architecture does not currently prescribe a universal canonicalization algorithm for every binary or document format. Therefore the hash represents the exact bytes supplied at the hashing stage, not an abstract semantic version of the document.

### 5.2 SHA-256 generation

A SHA-256 digest is generated from the exact artifact bytes. The resulting lowercase 64-character hexadecimal value is entered into the provenance record's Artifact Register.

Where the artifact bytes are available inside the controlled validation boundary, the validator can recompute the digest and compare it with the registered value. Where bytes remain in an external or restricted archive, the public repository can preserve the declared digest and verification instructions but cannot independently recompute bytes it does not possess.

### 5.3 Provenance-record construction

The provenance record is created using the controlled record structure. It identifies the record, represented artifact family, maturity state, Artifact Register, development status, evidence boundary, verification information, and applicable supersession state.

The record SHALL avoid interpreting a cryptographic digest as evidence of authorship, truth, originality, ownership, regulatory status, or institutional acceptance.

### 5.4 Registry admission

The record is added to the machine-readable and human-readable registry surfaces. Admission creates a discoverable relationship among the Record ID, artifact family, maturity, publication information, controlling schema, Git evidence, status, and verification path.

Admission is subject to the requirements and known boundaries documented by the controlling schema and test matrix. A record SHALL NOT be described as fully conformant merely because it appears in the index if applicable acceptance criteria remain unresolved or were not applicable at the time of publication.

### 5.5 Deterministic validation

`scripts/validate_registry.py` evaluates the repository state. Structural schema errors and implemented logical violations terminate validation with a nonzero exit status.

The validator currently evaluates identity, selected maturity constraints, Artifact Register structure, exact filename form, digest syntax, verification-path existence, evidence-boundary presence, supersession relationships, Markdown/JSON synchronization, and Git commit/path chronology. Exact-byte hash recomputation is available when controlled artifact bytes are supplied to the relevant verification function.

### 5.6 Adversarial validation

`tests/test_registry_conformance.py` evaluates the validator using controlled fixtures rather than intentionally damaging the live registry. A positive fixture establishes that the validator can accept a known-valid test state. Negative fixtures inject defined defects and assert that the validator terminates nonzero.

This positive-plus-negative structure is necessary because a validator that rejects every possible state would technically fail closed but would not be useful as a conformance mechanism.

### 5.7 Continuous integration enforcement

`.github/workflows/registry-conformance.yml` runs the deterministic validator and fixture-driven test suite in GitHub Actions. Full Git history is checked out because AC-13 chronology controls require historical commit resolution.

Changes to the governed control surface trigger the workflow. A nonzero validator or test result causes the job to fail. A passing run demonstrates that the checked repository state satisfied the automated controls executed in that run and that the included adversarial tests behaved as expected.

### 5.8 Public provenance

After the controlled material is committed, Git history provides a publicly inspectable chronology for the repository state. The registry links evidence records to Git commits and verification paths so another reviewer can inspect the represented public state.

Public Git chronology strengthens reproducibility and inspection. It does not transform the registry into a trusted timestamp authority, certification service, intellectual-property registry, or independent auditor.

---

## 6. Failure Model

The architecture uses fail-closed behavior for deterministic violations. If an implemented mandatory condition cannot be established, the validator SHALL return failure rather than infer conformance.

Examples include an invalid registry structure, duplicate Record ID, malformed artifact digest, duplicate artifact filename, filename containing a path, missing verification record, contradictory supersession relationship, Markdown/JSON mismatch, unresolved Git commit, or verification record absent from its indexed commit.

A CI failure is evidence that at least one implemented automated condition was not satisfied. The failure SHALL be investigated at the control that produced it. A failing control SHOULD be corrected by restoring the required state or correcting an erroneous control implementation. The control SHOULD NOT be weakened merely to obtain a green workflow result.

---

## 7. Trust Boundaries

### 7.1 Repository boundary

The public repository can deterministically inspect material available within its checkout and Git history. It cannot independently verify bytes stored only in an external restricted archive unless those bytes are deliberately supplied to a trusted validation environment.

### 7.2 Cryptographic boundary

SHA-256 supports exact-byte integrity comparison. The architecture does not treat hash possession or publication as proof of authorship, ownership, originality, truth, causation, or legal priority.

### 7.3 Git boundary

Git validation can establish that an object and path exist in accessible repository history. Additional controls are still required to distinguish initial-publication commit, later revision commit, reporting/reference date, and publication-date semantics with full rigor.

### 7.4 Automation boundary

Automation is limited to requirements that can be represented deterministically. Claim discipline, institutional relationships, privacy judgments, substantive evidentiary sufficiency, and some archive questions continue to require human review unless and until a defensible deterministic control is implemented.

### 7.5 External-assurance boundary

Internal CI is first-party technical evidence. It SHALL NOT be described as independent certification, third-party assurance, standards-body approval, regulatory approval, or external audit.

---

## 8. Control-to-Layer Mapping

| Control Surface | Layer | Primary Function |
|---|---|---|
| `REGISTRY-SCHEMA.md` | Specification | Human-readable normative requirements |
| `registry-index.schema.json` | Specification / Enforcement | Machine-readable structural constraints |
| `GOVERNANCE.md` | Specification | Authority and change control |
| `SECURITY.md` | Specification | Security and disclosure boundaries |
| `CONTRIBUTING.md` | Specification | Controlled change procedure |
| `RECORD-TEMPLATE.md` | Specification | Standard provenance-record construction |
| `weekly-proof/**` | Evidence | Public provenance records |
| `registry-index.json` | Evidence | Machine-readable registry state |
| `REGISTRY-INDEX.md` | Evidence | Human-readable registry ledger |
| `scripts/validate_registry.py` | Enforcement | Deterministic conformance evaluation |
| `tests/fixtures/**` | Testing | Controlled valid and invalid states |
| `tests/test_registry_conformance.py` | Testing | Positive and adversarial validator verification |
| `TEST-MATRIX.md` | Testing / Assurance | Acceptance-criterion coverage accounting |
| `.github/workflows/registry-conformance.yml` | Continuous Enforcement | Automatic execution and failure propagation |
| Git commit history | Public Provenance | Inspectable repository chronology |

---

## 9. Acceptance-Criterion Relationship

The architecture is implementation support for `EII-REG-SCHEMA-001`; it does not replace the specification. `TEST-MATRIX.md` is the authoritative current mapping of acceptance criteria to executable tests and identified gaps.

The architecture SHALL therefore use the following interpretation rule:

> A requirement is automated only to the extent that an executable control evaluates the relevant condition and a corresponding test or reproducible execution demonstrates the control's behavior.

Documentation alone does not establish automation. A unit test name alone does not establish coverage. A passing CI run alone does not establish requirements that are outside the executed control set.

---

## 10. Current Known Gaps

The current architecture does not yet provide complete automation of AC-01 through AC-15. Material remaining boundaries include restricted-archive byte verification, semantic review of artifact scope, evidence-supported maturity assessment, substantive evidence-boundary review, unsupported institutional-claim detection, comprehensive privacy/PII review, initial-publication versus current-revision commit separation, publication-date validation against Git commit timestamps, stronger multi-record supersession testing, and three-way synchronization if additional canonical machine-readable representations are introduced.

These limitations are part of the architecture's control model. They SHALL remain visible until corresponding controls are implemented and tested.

---

## 11. Change-Control Requirements

A material architectural change SHALL be reflected in this document when it changes a layer boundary, canonical data flow, trust boundary, validator responsibility, test responsibility, CI enforcement surface, or public-provenance interpretation.

Changes to this document SHALL trigger Registry Conformance CI. Changes to executable behavior SHALL also update `TEST-MATRIX.md` when acceptance-criterion coverage changes.

A new control SHALL NOT silently broaden the claimed assurance level. The relevant evidence boundary and coverage classification SHALL be reviewed at the same time.

---

## 12. Architecture Determination

The EII Public Provenance Registry currently implements a four-layer control architecture:

**Specification → Evidence → Deterministic Enforcement → Adversarial Testing and Continuous Enforcement**

Public Git provenance surrounds that architecture as the inspectable chronology of controlled repository states.

The resulting system is more than a document archive because defined requirements are represented in executable validation and tested failure behavior. It remains a first-party provenance and conformance-control system rather than an independent certification or external assurance mechanism.

The intended control chain is:

**Artifact → Canonical State → SHA-256 → Artifact Register → Provenance Record → Registry Admission → Deterministic Validation → Adversarial Testing → CI Enforcement → Public Git Provenance**

Each transition has a distinct evidentiary purpose. No transition SHALL be interpreted as proving more than its underlying mechanism supports.
