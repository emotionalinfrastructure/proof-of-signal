# EII Registry Conformance Test Matrix

**Document ID:** EII-REG-TEST-001  
**Version:** 1.1  
**Status:** Active test-control record  
**Controlling specification:** `EII-REG-SCHEMA-001 v1.0`  
**Validator:** `scripts/validate_registry.py`  
**Fixture corpus:** `tests/fixtures/`  
**Adversarial suite:** `tests/test_registry_conformance.py`  
**CI workflow:** `.github/workflows/registry-conformance.yml`  
**Current confirmed CI evidence:** Registry Conformance run `33281261448`, run #6, conclusion `success`  
**Evidence commit:** `5208697a4ebcf2a76d54639d25c605197d9d8e6f`

---

## 1. Purpose

This matrix maps executable registry controls to the acceptance criteria defined by `EII-REG-SCHEMA-001`. Version 1.1 incorporates the fixture-driven validator expansion for AC-03, AC-05, AC-06, AC-13, and AC-14 and preserves the distinction between controls demonstrated in CI and controls that still depend on unavailable archive bytes, semantic judgment, external evidence, or additional engineering.

A test marked **Direct** exercises the identified acceptance criterion or a concrete machine-testable component of it. A test marked **Supporting** contributes evidence to the criterion but does not fully determine it. A criterion marked **Automated with boundary** has deterministic enforcement for the represented control surface while retaining an explicit external or semantic limitation. A criterion marked **Partial** or **Manual** SHALL NOT be represented as fully automated.

The terms **SHALL** and **SHALL NOT** are normative within this test-control record.

---

## 2. Current CI Evidence

The current confirmed execution is GitHub Actions **Registry Conformance run #6**, run ID `33281261448`, against commit `5208697a4ebcf2a76d54639d25c605197d9d8e6f`.

The job `Validate registry controls` completed successfully. Both executable control stages completed with conclusion `success`:

1. `Run deterministic registry conformance checks`
2. `Run fixture-driven fail-closed tests`

The workflow checked out full Git history with `fetch-depth: 0`, allowing AC-13 chronology controls to resolve historical commits rather than operate against a shallow clone.

This execution demonstrates that the current live registry passed the implemented deterministic controls and that the controlled fixture suite produced the expected positive and fail-closed behavior. It SHALL NOT be represented as independent certification or as evidence that controls outside the implemented surface have been tested.

**CI verification:** https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33281261448

---

## 3. Fixture-Driven Automated Test Matrix

| Test / Control | AC Mapping | Coverage | Evaluated Condition | Expected Behavior | Current CI Evidence |
|---|---|---|---|---|---|
| `test_valid_artifact_register_parses` | AC-03, AC-06 | Direct | Controlled Artifact Register contains two unique basename-only filenames and valid lowercase SHA-256 values | Register parses and returns both structured rows | Run #6: fixture-driven suite `success` |
| `test_ac03_path_instead_of_exact_filename_fails_closed` | AC-03 | Direct | Artifact field contains a path instead of an exact basename | Parser exits nonzero | Run #6: fixture-driven suite `success` |
| `test_ac03_duplicate_filename_fails_closed` | AC-03 | Direct | Artifact Register repeats the same filename | Parser exits nonzero | Run #6: fixture-driven suite `success` |
| `test_ac06_malformed_digest_fails_closed` | AC-06 | Direct | Artifact Register contains a digest that is not exactly 64 lowercase hexadecimal characters | Parser exits nonzero | Run #6: fixture-driven suite `success` |
| `test_ac05_exact_fixture_bytes_recompute_successfully` | AC-05, AC-06 | Direct for available controlled bytes | SHA-256 is recomputed from exact controlled fixture artifact bytes and compared with registered digest | Verification completes without exception | Run #6: fixture-driven suite `success` |
| `test_ac05_byte_change_fails_closed` | AC-05 | Direct for available controlled bytes | One controlled artifact is modified after the registered digest is established | Recomputed digest mismatch exits nonzero | Run #6: fixture-driven suite `success` |
| `test_fixture_registry_and_index_are_structurally_conformant` | AC-01, AC-04, AC-14, AC-15 components | Supporting / Direct | Controlled registry JSON and Markdown index fixture describe the same record state | Schema and Markdown synchronization validation complete | Run #6: fixture-driven suite `success` |
| `test_stronger_ac14_family_divergence_fails_closed` | AC-14 | Direct | Markdown artifact-family value differs from JSON registry | Synchronization validation exits nonzero | Run #6: fixture-driven suite `success` |
| `test_stronger_ac14_maturity_divergence_fails_closed` | AC-04, AC-14 | Direct for index synchronization | Markdown maturity differs from JSON registry | Synchronization validation exits nonzero | Run #6: fixture-driven suite `success` |
| `test_ac13_commit_and_record_path_resolve_in_git_history` | AC-13 | Direct for Git-object chronology | Controlled Git repository contains both the indexed commit and verification record at that commit | Git chronology validation completes | Run #6: fixture-driven suite `success` |
| `test_ac13_unknown_commit_fails_closed` | AC-13 | Direct | Indexed commit SHA does not resolve as a commit in repository history | Git chronology validation exits nonzero | Run #6: fixture-driven suite `success` |
| `test_ac13_record_absent_at_commit_fails_closed` | AC-13 | Direct | Commit resolves, but the claimed verification record did not exist at that commit | Git chronology validation exits nonzero | Run #6: fixture-driven suite `success` |
| `test_live_registry_still_passes_non_git_controls` | AC-01, AC-03, AC-04, AC-06, AC-08, AC-09, AC-10, AC-14, AC-15 components | Supporting | Current live registry is evaluated against schema, logical invariants, Artifact Register parsing, and Markdown synchronization | Validation completes without exception | Run #6: fixture-driven suite `success` |
| `parse_artifact_register()` | AC-03, AC-06 | Direct | Verification record lacks Artifact Register, contains malformed rows, path-based filenames, duplicate filenames, or malformed SHA-256 values | Validator exits nonzero | Run #6: deterministic validator `success` |
| `verify_artifact_bytes()` | AC-05, AC-06 | Direct when archive bytes are locally available | Controlled artifact is missing or recomputed SHA-256 differs from registered digest | Validator exits nonzero | Run #6: fixture tests exercise positive and negative byte verification |
| `validate_git_chronology()` | AC-13 | Direct for repository-resolvable chronology | Indexed Git commit fails to resolve or verification path did not exist at indexed commit | Validator exits nonzero | Run #6: deterministic validator `success` |
| `validate_markdown_sync()` | AC-14, AC-15 | Direct for indexed fields | Markdown and JSON differ in record set, artifact family, maturity, publication date, controlling schema, commit SHA, supersession status, or verification path | Validator exits nonzero | Run #6: deterministic validator `success` |

---

## 4. Acceptance-Criterion Coverage Register

| Acceptance Criterion | Requirement | v1.1 Automation State | Evidence / Remaining Boundary |
|---|---|---|---|
| **AC-01 Identity** | Unique conformant Record ID | **Automated** | JSON pattern, record-type consistency, duplicate detection, verification-record ID check |
| **AC-02 Scope** | Record clearly defines represented artifacts or period | **Manual / Partial** | Structural scope fields exist, but semantic adequacy and completeness of represented scope remain human-reviewed |
| **AC-03 Exact filenames** | Every artifact uses exact filename corresponding to hashed file | **Automated with archive boundary** | Artifact Registers are parsed structurally; filenames must be basename-only and unique; path-based and duplicate names fail closed. Exact correspondence to a controlled archived file is deterministically testable when archive bytes are available, but the live restricted/external archive is not currently mounted in CI |
| **AC-04 Maturity** | Defensible maturity not exceeding evidence | **Partial** | Allowed vocabulary and Markdown/JSON synchronization are automated; whether evidence substantively supports the selected maturity remains a claim-review task |
| **AC-05 Integrity** | SHA-256 computed from every exact archived artifact | **Automated when controlled bytes are available** | `verify_artifact_bytes()` recomputes SHA-256 from exact bytes, rejects missing artifacts, and fails on byte changes. Fixture tests demonstrate both positive and tampered cases. Live weekly-proof artifact bytes are not stored in the public repository, so CI does not currently recompute those external archive hashes |
| **AC-06 Digest format** | Valid 64-character lowercase SHA-256 | **Automated** | Every parsed Artifact Register row must contain exactly one 64-character lowercase hexadecimal SHA-256 value; malformed rows and digests fail closed. When bytes are available, digest correctness is additionally tested through recomputation |
| **AC-07 Archive** | Exact hashed files preserved in controlled archive | **Manual / Not automated for external archive** | Byte-verification capability now exists, but CI cannot prove preservation of an archive it cannot access. Archive existence, retention, access control, and persistence remain outside the current public runner |
| **AC-08 Reproducibility** | Sufficient instructions for independent digest comparison | **Partial** | Verification-path existence, structured Artifact Register data, and digest mechanics are automated; semantic sufficiency of human verification instructions remains manual |
| **AC-09 Evidence boundary** | Explicit statement of evidentiary limits | **Partial** | Evidence-boundary heading presence is automated; substantive adequacy of the boundary remains human-reviewed |
| **AC-10 Claim discipline** | No material statement exceeds evidence | **Manual / Partial** | Maturity vocabulary and supersession invariants constrain some machine-testable overstatement pathways; substantive claims still require evidence review |
| **AC-11 Institutional boundary** | No unsupported institutional relationship claims | **Manual** | No deterministic resolver currently establishes whether an institutional relationship claim is supported by authoritative evidence |
| **AC-12 Privacy and security** | No unjustified sensitive/restricted information | **Manual** | Automated credential, secret, or PII scanning is not currently part of Registry Conformance CI |
| **AC-13 Public chronology** | Completed record committed publicly | **Automated for Git existence and path-at-commit; chronology-date semantics remain partial** | CI now checks full Git history, requires the indexed SHA to resolve as a commit, and requires the verification record to exist at that commit. It does not yet compare `publication_date` to commit timestamp, distinguish initial-publication commit from later controlled revision, or independently prove that a GitHub-visible commit was public at a particular historical instant beyond repository history |
| **AC-14 Registry indexing** | Published record linked from active registry index | **Automated for current Markdown/JSON index surfaces** | Record-set equality and field-level synchronization are enforced for artifact family, maturity, publication date, controlling schema, commit SHA, supersession status, and verification path. Remaining gap: the fenced YAML block in `REGISTRY-INDEX.md` is not independently parsed and compared, and external link availability is not tested |
| **AC-15 Final review** | Check mismatch, maturity, claims, links, metadata | **Partial** | Structural, integrity, chronology, and index-synchronization defect classes are increasingly automated; semantic claims, privacy review, archive controls, and external evidence remain manual |

---

## 5. Fail-Closed Contract

For automated conformance controls, a detected violation SHALL terminate validation with a nonzero process exit.

The deterministic validator uses `SystemExit(1)` for structural and logical failures. The fixture-driven suite asserts that controlled invalid states produce a nonzero `SystemExit`. GitHub Actions executes the validator and fixture suite without a failure-suppression directive; therefore a nonzero process result causes the CI job to fail.

A control that merely logs a warning while allowing a prohibited registry state to return exit code `0` SHALL NOT count as fail-closed coverage.

The prior run #5 is itself useful execution evidence for this contract: AC-13 failed when the workflow used a shallow checkout and could not resolve the indexed historical commit. The control was not weakened. The workflow was corrected to `fetch-depth: 0`, after which run #6 completed successfully.

---

## 6. Positive-Control Contract

The suite SHALL retain positive controls so an implementation that rejects every state cannot be misrepresented as a successful fail-closed validator.

Current positive controls include:

- `test_valid_artifact_register_parses`
- `test_ac05_exact_fixture_bytes_recompute_successfully`
- `test_fixture_registry_and_index_are_structurally_conformant`
- `test_ac13_commit_and_record_path_resolve_in_git_history`
- `test_live_registry_still_passes_non_git_controls`

Together, these controls demonstrate that the validator accepts defined conformant fixture states while rejecting specifically malformed states.

---

## 7. Current Adversarial Coverage

The fixture-driven suite currently evaluates the following defect classes:

1. path-based artifact identifiers where exact filenames are required;
2. duplicate Artifact Register filenames;
3. malformed SHA-256 digests;
4. exact artifact-byte tampering;
5. Markdown/JSON artifact-family divergence;
6. Markdown/JSON maturity divergence;
7. unknown Git commit references;
8. verification records absent from the claimed Git commit; and
9. live-registry regression against the strengthened non-Git controls.

The deterministic validator additionally enforces record identity, record-type consistency, verification-path existence, evidence-boundary presence, Artifact Register structure, supersession relationships, complete Markdown/JSON record-set equality, field-level index synchronization, and Git commit/path resolution.

Passing these tests means the validator rejected the represented invalid states and accepted the represented valid states. It does not establish exhaustive security, semantic correctness, external archive availability, or independent assurance.

---

## 8. Remaining Evidence and Automation Gaps

The v1.1 expansion closes several gaps identified in v1.0. The following remain material:

- make controlled live artifact bytes available to a trusted validation environment before representing AC-05 as live-registry byte verification;
- define machine-readable archive metadata distinguishing public, restricted, external, and unavailable archives;
- compare `publication_date` against the relevant Git commit timestamp under a defined chronology rule;
- distinguish `initial_publication_commit_sha` from `current_revision_commit_sha` so later controlled revisions do not overwrite publication chronology;
- parse and synchronize the fenced YAML registry block in `REGISTRY-INDEX.md` with both JSON and the Markdown ledger;
- validate bidirectional supersession relationships across multiple records and test partially superseded states;
- add explicit tests for dangling supersession IDs, self-reference, malformed JSON, missing required root files, invalid verification URIs, and duplicate Markdown ledger rows;
- add deterministic high-confidence secret/credential scanning without claiming comprehensive PII detection;
- verify external verification links where network-dependent CI is intentionally permitted;
- produce a machine-readable test-coverage report that maps test identifiers to acceptance criteria and CI execution evidence; and
- resolve schema chronology semantics for historical or pre-schema records before representing schema admission chronology more broadly than the evidence supports.

Until those controls exist, the corresponding acceptance criteria SHALL retain the boundary labels shown in Section 4.

---

## 9. CI Evidence Interpretation

A successful Registry Conformance workflow establishes that the checked repository state satisfied the implemented automated controls and that the fixture-driven tests behaved as expected during that execution.

It does not establish that:

- all EII-REG-SCHEMA-001 acceptance criteria are fully automated;
- inaccessible archive bytes were independently recomputed;
- semantic maturity or claim judgments are correct merely because vocabulary and synchronization checks pass;
- the underlying research artifacts are empirically valid;
- the registry has received independent assurance or certification;
- the system is secure against every adversarial condition;
- an institution or standards body has approved the registry; or
- provenance evidence establishes intellectual-property ownership, originality, or priority.

These boundaries SHALL remain explicit wherever CI evidence is cited as part of a provenance determination.

---

## 10. Test-Control Update Rule

Whenever a validator rule, fixture, automated test, acceptance criterion, or CI execution path materially changes, this matrix SHALL be reviewed.

A new automated test SHOULD be mapped to at least one acceptance criterion and SHALL identify:

- the test or control identifier;
- the acceptance criterion affected;
- the defect or condition evaluated;
- whether coverage is Direct, Supporting, or Automated with boundary;
- the expected pass/fail behavior;
- any external evidence dependency; and
- the CI execution that demonstrates the test is operational.

A criterion SHALL NOT be upgraded solely because a test name references it. The executable behavior must materially evaluate the criterion, and any evidence surface unavailable to the validator SHALL remain explicitly excluded from the automation claim.

---

## 11. Version 1.1 Control Determination

**Deterministic validator:** Operational  
**Controlled fixture corpus:** Operational  
**Positive controls:** Passing  
**Fixture-driven adversarial suite:** Passing  
**Fail-closed behavior for defined test cases:** Demonstrated  
**Current confirmed CI run:** `33281261448`  
**Current confirmed CI conclusion:** `success`  
**AC-03:** Automated with archive boundary  
**AC-05:** Automated when controlled bytes are available  
**AC-06:** Automated  
**AC-13:** Automated for Git existence and path-at-commit; date semantics remain partial  
**AC-14:** Automated for current Markdown/JSON index surfaces  
**Full AC-01 through AC-15 automation:** Not yet achieved

The current implementation supports the bounded determination that **the EII registry has an operational deterministic conformance layer with fixture-demonstrated exact-filename controls, SHA-256 format enforcement, exact-byte integrity verification when controlled bytes are available, Git-history commit/path verification, field-level Markdown/JSON synchronization, and fail-closed behavior for the defect classes represented in the current automated suite**.

---

**Emotional Infrastructure Institute**  
*Executable provenance controls, auditable conformance coverage, and explicit evidence boundaries.*
