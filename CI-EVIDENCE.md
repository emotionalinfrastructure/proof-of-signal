# EII Registry Conformance CI Execution Evidence

**Document ID:** EII-REG-CI-001  
**Version:** 1.0  
**Status:** Canonical CI execution record  
**Workflow:** Registry Conformance v1.3  
**Repository:** `emotionalinfrastructure/proof-of-signal`  
**Evidence type:** First-party automated execution evidence

---

## 1. Purpose

This record preserves the verified GitHub Actions execution evidence for Registry Conformance workflow v1.3 at commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21`.

Its purpose is to establish that the workflow was not merely written or committed: GitHub Actions executed the workflow against the identified repository state, the deterministic registry validator completed successfully, and the fixture-driven fail-closed test suite completed successfully.

This record is bounded to the automated controls actually executed during the identified run.

---

## 2. Execution Identity

| Field | Verified value |
|---|---|
| Repository | `emotionalinfrastructure/proof-of-signal` |
| Workflow | `Registry Conformance` |
| Workflow path | `.github/workflows/registry-conformance.yml` |
| Workflow version represented by commit | `v1.3` |
| Head branch | `main` |
| Head commit | `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21` |
| Commit message | `ci: govern architecture and implementation inventory` |
| Trigger event | `push` |
| Workflow run number | `9` |
| Workflow run ID | `33282383199` |
| Run attempt | `1` |
| Run status | `completed` |
| Run conclusion | `success` |
| Run started | `2026-08-30T00:02:56Z` |
| Run updated/completed | `2026-08-30T00:03:09Z` |
| Check suite ID | `90195635751` |

---

## 3. Job Evidence

The workflow produced the following verified job result:

| Field | Verified value |
|---|---|
| Job name | `Validate registry controls` |
| Job ID | `99179612435` |
| Job status | `completed` |
| Job conclusion | `success` |
| Workflow run ID | `33282383199` |

The successful job conclusion means that every required step in this job completed without returning a failure state.

---

## 4. Step Outcomes

| Step | Outcome |
|---|---|
| Set up job | `success` |
| Check out repository history | `success` |
| Set up Python | `success` |
| Install pinned validator dependency | `success` |
| Run deterministic registry conformance checks | `success` |
| Run fixture-driven fail-closed tests | `success` |
| Post Set up Python | `success` |
| Post Check out repository history | `success` |
| Complete job | `success` |

Two steps carry the primary conformance significance.

### 4.1 Deterministic registry validation

The workflow executed:

```text
python scripts/validate_registry.py
```

The step concluded `success`.

This establishes that the repository state at the workflow's checked-out commit did not trigger a failure under the deterministic controls implemented by `scripts/validate_registry.py` at that state.

### 4.2 Fixture-driven fail-closed testing

The workflow executed:

```text
python -m unittest -v tests.test_registry_conformance
```

The step concluded `success`.

This establishes that the adversarial/unit test suite completed successfully for the defect classes represented by that test suite at the identified commit.

---

## 5. Workflow v1.3 Control-Surface Significance

Workflow v1.3 expanded the controlled CI trigger surface to include both:

- `ARCHITECTURE.md`
- `IMPLEMENTATION-INVENTORY.md`

Those files were added to both `pull_request.paths` and the `push` path controls for `main`.

The workflow already governed the registry specification, registry indexes, JSON Schema, record template, contribution controls, governance and security documents, test matrix, weekly provenance records, validator code, test code, fixture corpus, and the workflow definition itself.

The successful run for commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21` therefore provides execution evidence that the v1.3 workflow definition was accepted by GitHub Actions and that its validator and adversarial-test stages completed successfully for that commit.

---

## 6. Reproducibility Links

### Workflow run

`https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33282383199`

### Evidence commit

`https://github.com/emotionalinfrastructure/proof-of-signal/commit/2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21`

### Workflow definition

`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/.github/workflows/registry-conformance.yml`

### Deterministic validator

`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/scripts/validate_registry.py`

### Adversarial test suite

`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/tests/test_registry_conformance.py`

### Test-control matrix

`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/TEST-MATRIX.md`

### Implementation inventory

`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/IMPLEMENTATION-INVENTORY.md`

### Architecture

`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/ARCHITECTURE.md`

For historical reproduction, reviewers SHOULD inspect files at the evidence commit rather than assume the current `main` branch remains byte-identical to the state evaluated by run #9.

---

## 7. Assurance Boundary

This execution evidence supports the following bounded determination:

> GitHub Actions executed Registry Conformance workflow v1.3 for commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21`. Workflow run #9 completed successfully. The `Validate registry controls` job completed successfully. Both the deterministic registry conformance step and the fixture-driven fail-closed test step completed successfully.

This evidence does **not** independently establish:

1. complete automation of AC-01 through AC-15;
2. correctness of requirements outside the implemented validator;
3. byte verification of restricted or external artifacts unavailable to the CI environment;
4. absence of every possible software defect;
5. comprehensive privacy or security assurance;
6. empirical or scientific validity of underlying research or artifacts;
7. originality, authorship priority, intellectual-property ownership, or legal entitlement;
8. institutional sponsorship, approval, endorsement, adoption, or validation;
9. regulatory compliance;
10. standards-body conformance or adoption;
11. production readiness of the broader Emotional Infrastructure architecture; or
12. independent certification or third-party assurance.

A green CI result SHALL be interpreted as evidence that the identified repository state passed the automated controls actually executed in that run, and no more.

---

## 8. Evidence Classification

| Evidence proposition | Classification |
|---|---|
| Workflow run #9 exists for the identified commit | Verified fact |
| Run #9 was triggered by a push to `main` | Verified fact |
| Run #9 completed successfully | Verified fact |
| Job `Validate registry controls` completed successfully | Verified fact |
| Deterministic registry validation step succeeded | Verified fact |
| Fixture-driven fail-closed test step succeeded | Verified fact |
| Workflow v1.3 is operational for the tested repository state | Reasonable technical determination supported by execution evidence |
| Every EII requirement is automated | Unsupported by this evidence |
| The registry is independently certified | Unsupported by this evidence |
| Underlying EII research is empirically validated by CI | Unsupported by this evidence |

---

## 9. Verification Procedure

An independent reviewer can reproduce the public evidence inspection as follows:

1. Open workflow run `33282383199` and confirm the head SHA is `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21`.
2. Confirm the workflow name is `Registry Conformance`, run number is `9`, event is `push`, status is `completed`, and conclusion is `success`.
3. Open the `Validate registry controls` job and confirm job ID `99179612435` completed successfully.
4. Confirm `Run deterministic registry conformance checks` concluded successfully.
5. Confirm `Run fixture-driven fail-closed tests` concluded successfully.
6. Inspect commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21` to establish the exact repository state associated with the execution.
7. Inspect the workflow, validator, tests, fixtures, `TEST-MATRIX.md`, `IMPLEMENTATION-INVENTORY.md`, and `ARCHITECTURE.md` at that commit when determining the actual scope of assurance.

The reviewer SHALL NOT infer controls that are absent from the implementation state associated with the evidence commit.

---

## 10. Canonical Determination

**Registry Conformance workflow v1.3 is execution-confirmed for commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21`.**

The canonical supporting GitHub Actions evidence is:

```text
Workflow: Registry Conformance
Run: #9
Run ID: 33282383199
Commit: 2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21
Job: Validate registry controls
Job ID: 99179612435
Run conclusion: success
Deterministic validator: success
Fixture-driven fail-closed tests: success
```

This is first-party automated execution evidence for the implemented conformance controls at the identified repository state. It SHALL NOT be represented as broader assurance than the executed controls support.
