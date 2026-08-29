# EII Registry Conformance Test Matrix

**Document ID:** EII-REG-TEST-001  
**Version:** 1.0  
**Status:** Active test-control record  
**Controlling specification:** `EII-REG-SCHEMA-001 v1.0`  
**Validator:** `scripts/validate_registry.py`  
**Adversarial suite:** `tests/test_registry_conformance.py`  
**CI workflow:** `.github/workflows/registry-conformance.yml`  
**Current confirmed CI evidence:** Registry Conformance run `33277143817`, run #3, conclusion `success`  
**Evidence commit:** `976dd80c7ce89cc3858110d07e423a0d563ccb56`

---

## 1. Purpose

This matrix maps executable registry controls to the acceptance criteria defined by `EII-REG-SCHEMA-001`. Its purpose is to make conformance coverage inspectable rather than imply that a passing CI run proves requirements that have not actually been automated.

A test marked **Direct** exercises the identified acceptance criterion or a concrete machine-testable component of it. A test marked **Supporting** contributes evidence to the criterion but does not fully determine it. A criterion marked **Manual / Partial** still requires human review or additional engineering before it can be represented as completely automated.

The terms **SHALL** and **SHALL NOT** are normative within this test-control record.

---

## 2. Current CI Evidence

The current confirmed execution is GitHub Actions **Registry Conformance run #3**, run ID `33277143817`, against commit `976dd80c7ce89cc3858110d07e423a0d563ccb56`.

The job `Validate registry controls` completed successfully. Both executable control stages completed with conclusion `success`:

1. `Run deterministic registry conformance checks`
2. `Run adversarial fail-closed tests`

This execution demonstrates that the current registry passed the implemented validator and that the current adversarial suite passed. It SHALL NOT be represented as independent certification or as evidence that unimplemented control classes have been tested.

**CI verification:** https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33277143817

---

## 3. Automated Test Matrix

| Test / Control | AC Mapping | Coverage | Injected or Evaluated Failure Condition | Expected Behavior | Current CI Evidence |
|---|---|---|---|---|---|
| `test_baseline_registry_passes_current_validator` | AC-01, AC-02, AC-04, AC-06, AC-08, AC-09, AC-13, AC-14, AC-15 components | Supporting | Current controlled registry is evaluated without mutation | No exception; baseline validator stages complete | Run #3: adversarial suite `success` |
| `test_malformed_commit_hash_fails_closed` | AC-13, AC-15 | Direct | `commit_sha` replaced with non-SHA value `xyz` | JSON Schema validation exits nonzero through `SystemExit` | Run #3: adversarial suite `success` |
| `test_duplicate_record_id_fails_closed` | AC-01, AC-15 | Direct | Second record uses an already admitted `record_id` | Logical-invariant validation exits nonzero | Run #3: adversarial suite `success` |
| `test_invalid_maturity_state_fails_closed` | AC-04, AC-10, AC-15 | Direct for allowed vocabulary; Supporting for evidentiary defensibility | Maturity replaced with unapproved state `Certified` | JSON Schema validation exits nonzero | Run #3: adversarial suite `success` |
| `test_missing_verification_record_fails_closed` | AC-08, AC-13, AC-14, AC-15 | Direct for verification-path existence | Registry points to a nonexistent provenance record | Logical-invariant validation exits nonzero | Run #3: adversarial suite `success` |
| `test_markdown_json_divergence_fails_closed` | AC-14, AC-15 | Direct | Canonical Markdown ledger contains a commit SHA inconsistent with JSON registry | Markdown synchronization validation exits nonzero | Run #3: adversarial suite `success` |
| `test_superseded_without_successor_fails_closed` | AC-10, AC-15 | Direct for implemented supersession invariant | Record state is `Superseded` while `superseded_by` is empty | Logical-invariant validation exits nonzero | Run #3: adversarial suite `success` |
| `test_active_record_with_successor_fails_closed` | AC-10, AC-15 | Direct for implemented supersession invariant | Record remains `Active` while identifying a `superseded_by` successor | Logical-invariant validation exits nonzero | Run #3: adversarial suite `success` |
| `test_verification_record_without_sha256_fails_closed` | AC-05, AC-06, AC-08, AC-15 | Direct for digest presence; Supporting for exact-byte provenance | Verification record contains no 64-character SHA-256 digest | Logical-invariant validation exits nonzero | Run #3: adversarial suite `success` |
| JSON Schema validation in `validate_schema()` | AC-01, AC-04, AC-06, AC-13, AC-15 components | Direct / Supporting | Registry violates structural types, enums, patterns, required fields, URI/date formats, or Git SHA format | Validator emits `SCHEMA ERROR` and exits nonzero | Run #3: deterministic validator `success` |
| Duplicate-ID invariant in `validate_logical_invariants()` | AC-01 | Direct | More than one JSON record has the same Record ID | `ERROR: duplicate record_id values detected`; exit nonzero | Run #3: deterministic validator `success` |
| Record ID / record type invariant | AC-01, AC-15 | Direct | Record ID is malformed or `record_type` conflicts with Record ID class | Exit nonzero | Run #3: deterministic validator `success` |
| Verification-path existence invariant | AC-08, AC-14, AC-15 | Direct | `verification_path` does not resolve to a repository file | Exit nonzero | Run #3: deterministic validator `success` |
| Record-ID-in-verification invariant | AC-01, AC-15 | Supporting | Verification record does not contain the Record ID it purports to represent | Exit nonzero | Run #3: deterministic validator `success` |
| Evidence-boundary heading invariant | AC-09, AC-15 | Supporting | Verification record contains neither `Evidence Boundary` nor `Evidentiary Boundary` section heading | Exit nonzero | Run #3: deterministic validator `success` |
| SHA-256-presence invariant | AC-05, AC-06, AC-08 | Supporting | Verification record contains no 64-character lowercase hexadecimal digest | Exit nonzero | Run #3: deterministic validator `success` |
| Supersession-state invariants | AC-10, AC-15 | Supporting | `Superseded` lacks successor, or `Active` improperly identifies successor | Exit nonzero | Run #3: deterministic validator `success` |
| Markdown required-token synchronization | AC-14, AC-15 | Direct for indexed fields | Markdown index omits JSON Record ID, publication date, commit SHA, verification path, schema ID/version, or supersession status | Exit nonzero | Run #3: deterministic validator `success` |
| Markdown extra-record detection | AC-14, AC-15 | Direct | Markdown ledger contains an EII provenance Record ID absent from JSON | Exit nonzero | Run #3: deterministic validator `success` |

---

## 4. Acceptance-Criterion Coverage Register

| Acceptance Criterion | Requirement | Current Automation State | Evidence / Gap |
|---|---|---|---|
| **AC-01 Identity** | Unique conformant Record ID | **Automated** | JSON pattern, record-type consistency, duplicate detection, verification-record ID check |
| **AC-02 Scope** | Record clearly defines represented artifacts or period | **Manual / Partial** | Required registry fields provide structural scope signals, but semantic clarity of scope is not machine-evaluated |
| **AC-03 Exact filenames** | Every artifact uses exact filename corresponding to hashed file | **Manual / Not yet byte-verified** | Current validator does not parse artifact tables and recompute hashes from archived files |
| **AC-04 Maturity** | Defensible maturity not exceeding evidence | **Partial** | Allowed maturity vocabulary is automated; whether evidence actually supports the selected maturity remains a claim-review task |
| **AC-05 Integrity** | SHA-256 computed from every exact archived artifact | **Partial** | Digest presence is checked; recomputation against controlled artifact bytes is not yet implemented |
| **AC-06 Digest format** | Valid 64-character lowercase SHA-256 | **Partial** | Verification records are scanned for valid 64-character lowercase digest tokens; full artifact-register parsing is not yet implemented |
| **AC-07 Archive** | Exact hashed files preserved in controlled archive | **Manual / Not automated** | Repository cannot currently verify existence and byte identity of restricted/external controlled archives |
| **AC-08 Reproducibility** | Sufficient instructions for independent digest comparison | **Partial** | Verification path and digest presence are automated; semantic sufficiency of instructions remains manual |
| **AC-09 Evidence boundary** | Explicit statement of evidentiary limits | **Partial** | Section-heading presence is automated; substantive completeness of the boundary remains manual |
| **AC-10 Claim discipline** | No material statement exceeds evidence | **Manual / Partial** | Maturity vocabulary and supersession logic are constrained; substantive claim review remains human-governed |
| **AC-11 Institutional boundary** | No unsupported institutional relationship claims | **Manual** | No deterministic institutional-claim evidence resolver exists |
| **AC-12 Privacy and security** | No unjustified sensitive/restricted information | **Manual** | Automated secret/PII scanning is not currently part of registry CI |
| **AC-13 Public chronology** | Completed record committed publicly | **Partial** | Git SHA structure and indexed commit value are checked; validator does not currently query GitHub to prove the SHA exists or is the actual publication commit |
| **AC-14 Registry indexing** | Published record linked from active registry index | **Automated for current index surfaces** | Markdown/JSON synchronization and verification-path existence are enforced |
| **AC-15 Final review** | Check mismatch, maturity, claims, links, metadata | **Partial** | Multiple deterministic defect classes are automated; semantic and external-evidence review remains manual |

---

## 5. Fail-Closed Contract

For automated conformance controls, a detected violation SHALL terminate validation with a nonzero process exit.

The deterministic validator uses `SystemExit(1)` for logical and structural failures. The adversarial suite asserts that injected invalid states produce a nonzero `SystemExit`. GitHub Actions executes the validator and test suite without a failure-suppression directive; therefore a nonzero process result causes the CI job to fail.

A test that merely logs a warning while allowing a prohibited registry state to return exit code `0` SHALL NOT count as fail-closed coverage.

---

## 6. Positive-Control Contract

The suite SHALL retain at least one positive baseline test against the unmodified current registry. This prevents an implementation that rejects every state from being misrepresented as a successful fail-closed validator.

Current positive control:

`test_baseline_registry_passes_current_validator`

The baseline invokes schema validation, logical-invariant validation, and Markdown synchronization against the current controlled registry state.

---

## 7. Current Adversarial Coverage

The current suite intentionally injects the following defect classes:

1. malformed Git commit SHA;
2. duplicate Record ID;
3. unauthorized maturity vocabulary;
4. missing verification record;
5. Markdown/JSON registry divergence;
6. superseded record without successor;
7. active record with contradictory successor reference; and
8. verification record without SHA-256 evidence.

Passing these tests means the validator rejected each injected state in the test environment. It does not establish that every possible malformed state, semantic overclaim, archive failure, privacy defect, or adversarial input has been tested.

---

## 8. Coverage Gaps Requiring Further Engineering

The following controls remain material automation gaps:

- parse each verification record's Artifact Register into structured fields;
- validate every artifact digest rather than only detecting digest presence;
- recompute SHA-256 against repository-hosted canonical artifacts when available;
- distinguish restricted archives from missing archives through explicit archive metadata;
- verify that indexed Git commit SHAs resolve in repository history;
- verify that the identified commit actually contains the represented provenance record state;
- validate bidirectional supersession references across multiple records;
- enforce publication-date chronology against Git history;
- detect dangling `supersedes` and `superseded_by` Record IDs;
- add deterministic secret scanning for high-confidence credential patterns;
- validate that Markdown and JSON artifact-family and maturity values agree, not merely selected tokens;
- test malformed JSON, missing required root files, invalid verification URIs, and duplicate supersession relationships; and
- produce a machine-readable test-coverage report suitable for archival with CI evidence.

Until those controls exist, the corresponding acceptance criteria SHALL remain labeled `Partial`, `Manual`, or `Not automated` rather than being represented as fully covered.

---

## 9. CI Evidence Interpretation

A successful Registry Conformance workflow establishes that the checked repository state satisfied the automated controls and that the adversarial unit tests behaved as expected during that execution.

It does not establish that:

- all EII-REG-SCHEMA-001 acceptance criteria are fully automated;
- the underlying research artifacts are empirically valid;
- the registry has received independent assurance;
- the system is secure against every adversarial condition;
- an institution or standards body has approved the registry; or
- provenance evidence establishes intellectual-property ownership or priority.

These boundaries SHALL remain explicit wherever CI evidence is cited as part of a provenance determination.

---

## 10. Test-Control Update Rule

Whenever a validator rule, adversarial test, acceptance criterion, or CI execution path materially changes, this matrix SHALL be reviewed.

A new automated test SHOULD be mapped to at least one acceptance criterion and SHALL identify:

- the test or control identifier;
- the acceptance criterion affected;
- the defect or condition evaluated;
- whether coverage is Direct or Supporting;
- the expected pass/fail behavior; and
- the CI execution that demonstrates the test is operational.

A criterion SHALL NOT be upgraded to `Automated` solely because a test name references it. The executable behavior must materially evaluate the criterion.

---

## 11. Current Test-Control Determination

**Deterministic validator:** Operational  
**Positive baseline:** Passing  
**Adversarial suite:** Passing  
**Fail-closed behavior for defined test cases:** Demonstrated  
**Current confirmed CI run:** `33277143817`  
**Current confirmed CI conclusion:** `success`  
**Full AC-01 through AC-15 automation:** Not yet achieved

The current implementation therefore supports the narrower determination that **the EII registry has an operational deterministic conformance layer with demonstrated fail-closed behavior for the defect classes presently represented in its automated test suite**.

---

**Emotional Infrastructure Institute**  
*Executable provenance controls, auditable conformance coverage, and explicit evidence boundaries.*
