# EII Registry Conformance CI Execution Evidence

**Document ID:** EII-REG-CI-001  
**Version:** 1.1  
**Status:** Canonical CI execution record  
**Current workflow:** Registry Conformance v1.4  
**Repository:** `emotionalinfrastructure/proof-of-signal`  
**Evidence type:** First-party automated execution evidence

---

## 1. Purpose

This record preserves verified GitHub Actions execution evidence for the EII Registry Conformance control plane while maintaining prior successful executions as immutable historical provenance.

Version 1.1 advances the current canonical execution reference from Registry Conformance v1.3 / run #9 to Registry Conformance v1.4 / run #10. Run #9 remains recorded below as historical evidence and is not overwritten, recharacterized, or treated as evidence for controls introduced after v1.3.

This record is bounded to the automated controls actually executed during each identified run.

---

## 2. Current Canonical Execution: Workflow v1.4 / Run #10

| Field | Verified value |
|---|---|
| Repository | `emotionalinfrastructure/proof-of-signal` |
| Workflow | `Registry Conformance` |
| Workflow path | `.github/workflows/registry-conformance.yml` |
| Workflow version represented by commit | `v1.4` |
| Head branch | `main` |
| Head commit | `404e509eba958166c264636e0376d2b619880666` |
| Commit message | `ci: govern canonical CI execution evidence` |
| Trigger event | `push` |
| Workflow run number | `10` |
| Workflow run ID | `33282520547` |
| Run attempt | `1` |
| Run status | `completed` |
| Run conclusion | `success` |
| Run started | `2026-08-30T00:06:19Z` |
| Run updated/completed | `2026-08-30T00:06:28Z` |
| Check suite ID | `90195986792` |

### 2.1 Job evidence

| Field | Verified value |
|---|---|
| Job name | `Validate registry controls` |
| Job ID | `99179974414` |
| Job status | `completed` |
| Job conclusion | `success` |
| Workflow run ID | `33282520547` |

### 2.2 Step outcomes

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

The two substantive executable stages were:

```text
python scripts/validate_registry.py
python -m unittest -v tests.test_registry_conformance
```

Both concluded `success`.

This establishes that the repository state checked out for commit `404e509eba958166c264636e0376d2b619880666` did not trigger a failure under the deterministic controls implemented by the validator at that state and that the adversarial/unit test suite completed successfully for the defect classes represented by that suite.

---

## 3. Workflow v1.4 Control-Surface Significance

Workflow v1.4 added `CI-EVIDENCE.md` to both the `pull_request.paths` and `push.paths` controlled surfaces. The workflow therefore responds to changes to its canonical execution-evidence record in addition to the previously governed architecture, implementation inventory, specification, registry indexes, JSON Schema, governance documents, test matrix, provenance records, validator implementation, tests, fixtures, and workflow definition.

The successful execution of run #10 establishes that GitHub Actions accepted and executed the v1.4 workflow definition at commit `404e509eba958166c264636e0376d2b619880666`, and that its deterministic validator and fixture-driven fail-closed test stages completed successfully.

This does not make the workflow impossible to bypass by every repository mutation. Path-trigger coverage and branch/ruleset enforcement are distinct controls. No branch-protection or repository-ruleset conclusion is made by this record unless separately verified.

---

## 4. Historical Execution Provenance

Prior successful execution evidence SHALL remain distinguishable from the current canonical execution rather than being overwritten.

### 4.1 Historical record: Workflow v1.3 / Run #9

| Field | Historical verified value |
|---|---|
| Workflow version | `v1.3` |
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
| Job name | `Validate registry controls` |
| Job ID | `99179612435` |
| Job conclusion | `success` |
| Deterministic validator | `success` |
| Fixture-driven fail-closed tests | `success` |

Run #9 is evidence for workflow v1.3 at its identified repository state. It SHALL NOT be retroactively treated as execution evidence for the v1.4 addition of `CI-EVIDENCE.md` to the trigger surface.

### 4.2 Execution lineage

```text
v1.3
  commit: 2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21
  run:    #9 / 33282383199
  result: success
        |
        | workflow control surface expanded
        v
v1.4
  commit: 404e509eba958166c264636e0376d2b619880666
  run:    #10 / 33282520547
  result: success
```

This lineage records progression of the control plane without erasing the execution state that preceded it.

---

## 5. Reproducibility Links

### Current canonical v1.4 evidence

Workflow run #10:  
`https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33282520547`

Evidence commit:  
`https://github.com/emotionalinfrastructure/proof-of-signal/commit/404e509eba958166c264636e0376d2b619880666`

### Historical v1.3 evidence

Workflow run #9:  
`https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33282383199`

Historical evidence commit:  
`https://github.com/emotionalinfrastructure/proof-of-signal/commit/2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21`

### Current control surfaces

Workflow definition:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/.github/workflows/registry-conformance.yml`

Deterministic validator:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/scripts/validate_registry.py`

Adversarial test suite:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/tests/test_registry_conformance.py`

Test-control matrix:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/TEST-MATRIX.md`

Implementation inventory:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/IMPLEMENTATION-INVENTORY.md`

Architecture:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/ARCHITECTURE.md`

CI evidence record:  
`https://github.com/emotionalinfrastructure/proof-of-signal/blob/main/CI-EVIDENCE.md`

For historical reproduction, reviewers SHOULD inspect repository files at the relevant evidence commit rather than assume current `main` remains byte-identical to the state evaluated by an earlier run.

---

## 6. Assurance Boundary

The current canonical execution evidence supports the following bounded determination:

> GitHub Actions executed Registry Conformance workflow v1.4 for commit `404e509eba958166c264636e0376d2b619880666`. Workflow run #10 completed successfully. The `Validate registry controls` job completed successfully. Both the deterministic registry conformance step and the fixture-driven fail-closed test step completed successfully.

The historical evidence separately establishes the equivalent bounded execution result for workflow v1.3 at commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21` through run #9.

Neither execution independently establishes:

1. complete automation of AC-01 through AC-15;
2. correctness of requirements outside the implemented validator;
3. byte verification of restricted or external artifacts unavailable to CI;
4. absence of every possible software defect;
5. comprehensive privacy or security assurance;
6. empirical or scientific validity of underlying research or artifacts;
7. originality, authorship priority, intellectual-property ownership, or legal entitlement;
8. institutional sponsorship, approval, endorsement, adoption, or validation;
9. regulatory compliance;
10. standards-body conformance or adoption;
11. production readiness of the broader Emotional Infrastructure architecture;
12. independent certification or third-party assurance; or
13. non-bypassable merge or push enforcement absent separately verified branch protection or repository rulesets.

A green CI result SHALL be interpreted only as evidence that the identified repository state passed the automated controls actually executed during that run.

---

## 7. Evidence Classification

| Evidence proposition | Classification |
|---|---|
| Workflow run #10 exists for commit `404e509...` | Verified fact |
| Run #10 was triggered by a push to `main` | Verified fact |
| Run #10 completed successfully | Verified fact |
| Job `Validate registry controls` completed successfully | Verified fact |
| Deterministic registry validation step succeeded | Verified fact |
| Fixture-driven fail-closed test step succeeded | Verified fact |
| Workflow v1.4 executed successfully for the tested repository state | Verified technical execution fact |
| Run #9 remains a distinct successful v1.3 historical execution | Verified fact |
| Every EII requirement is automated | Unsupported by this evidence |
| CI is non-bypassable through repository policy | Not established by this evidence |
| The registry is independently certified | Unsupported by this evidence |
| Underlying EII research is empirically validated by CI | Unsupported by this evidence |

---

## 8. Verification Procedure

An independent reviewer can inspect the current canonical execution as follows:

1. Open workflow run `33282520547` and confirm the head SHA is `404e509eba958166c264636e0376d2b619880666`.
2. Confirm workflow name `Registry Conformance`, run number `10`, event `push`, status `completed`, and conclusion `success`.
3. Open `Validate registry controls` and confirm job ID `99179974414` completed successfully.
4. Confirm `Run deterministic registry conformance checks` concluded successfully.
5. Confirm `Run fixture-driven fail-closed tests` concluded successfully.
6. Inspect commit `404e509eba958166c264636e0376d2b619880666` to establish the exact repository state evaluated by run #10.
7. Inspect workflow v1.4 at that commit and confirm `CI-EVIDENCE.md` is present in both the pull-request and push path-trigger surfaces.
8. Inspect validator, tests, fixtures, test matrix, implementation inventory, and architecture at that same commit before drawing conclusions about the scope of assurance.
9. For historical comparison, inspect run #9 and commit `2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21` independently rather than applying v1.4 controls retroactively.

The reviewer SHALL NOT infer controls absent from the implementation state associated with the relevant evidence commit.

---

## 9. Canonical Determination

**Registry Conformance workflow v1.4 is execution-confirmed for commit `404e509eba958166c264636e0376d2b619880666`.**

Current canonical supporting evidence:

```text
Workflow: Registry Conformance v1.4
Run: #10
Run ID: 33282520547
Commit: 404e509eba958166c264636e0376d2b619880666
Job: Validate registry controls
Job ID: 99179974414
Run conclusion: success
Deterministic validator: success
Fixture-driven fail-closed tests: success
```

Historical predecessor retained:

```text
Workflow: Registry Conformance v1.3
Run: #9
Run ID: 33282383199
Commit: 2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21
Job: Validate registry controls
Job ID: 99179612435
Run conclusion: success
Deterministic validator: success
Fixture-driven fail-closed tests: success
```

This is first-party automated execution evidence for the implemented conformance controls at the identified repository states. It SHALL NOT be represented as broader assurance than those executed controls support.

---

## 10. Revision History

| Version | Canonical workflow/run | Change |
|---|---|---|
| `1.0` | v1.3 / run #9 | Established the initial canonical CI execution record. |
| `1.1` | v1.4 / run #10 | Advanced the canonical reference to verified v1.4 execution and retained v1.3 / run #9 as historical provenance. |
