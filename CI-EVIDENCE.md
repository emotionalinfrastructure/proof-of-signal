# EII Registry Conformance CI Execution Evidence

**Document ID:** EII-REG-CI-001  
**Version:** 1.2  
**Status:** Canonical CI execution record  
**Current workflow:** Registry Conformance v1.4  
**Repository:** `emotionalinfrastructure/proof-of-signal`  
**Evidence type:** First-party automated execution evidence

---

## 1. Purpose

This record preserves verified GitHub Actions execution evidence for the EII Registry Conformance control plane while maintaining prior successful executions as historical provenance.

Version 1.2 advances the canonical execution reference to Registry Conformance v1.4 / run #11 because that run directly exercised the newly governed `CI-EVIDENCE.md` trigger path. Runs #9 and #10 remain preserved as historical execution lineage and SHALL NOT be overwritten or retroactively treated as evidence for controls that did not yet exist at those repository states.

This record is bounded to the automated controls actually executed during each identified run.

---

## 2. Current Canonical Execution: Workflow v1.4 / Run #11

| Field | Verified value |
|---|---|
| Repository | `emotionalinfrastructure/proof-of-signal` |
| Workflow | `Registry Conformance` |
| Workflow path | `.github/workflows/registry-conformance.yml` |
| Workflow version | `v1.4` |
| Triggered control artifact | `CI-EVIDENCE.md` |
| Head branch | `main` |
| Head commit | `b2802ed508af8c6ab055b53f07aca8b44ad0e95d` |
| Commit message | `docs: advance canonical CI evidence to v1.4 run 10` |
| Trigger event | `push` |
| Workflow run number | `11` |
| Workflow run ID | `33282600271` |
| Run attempt | `1` |
| Run status | `completed` |
| Run conclusion | `success` |
| Run started | `2026-08-30T00:08:14Z` |
| Run updated/completed | `2026-08-30T00:08:29Z` |
| Check suite ID | `90196177087` |

### 2.1 Job evidence

| Field | Verified value |
|---|---|
| Job name | `Validate registry controls` |
| Job ID | `99180177120` |
| Job status | `completed` |
| Job conclusion | `success` |
| Workflow run ID | `33282600271` |

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

---

## 3. Direct Trigger-Path Validation

Run #11 is the first verified execution in which the triggering commit modified `CI-EVIDENCE.md` itself after workflow v1.4 added that file to both `pull_request.paths` and `push.paths`.

The observed execution chain was:

```text
CI-EVIDENCE.md modification
        |
        v
push to main
        |
        v
v1.4 path trigger matched
        |
        v
Registry Conformance executed
        |
        +--> deterministic validator: success
        |
        +--> fixture-driven fail-closed tests: success
        |
        v
workflow run #11: success
```

This provides direct operational evidence for the tested push-trigger path. It establishes that a change to `CI-EVIDENCE.md` at commit `b2802ed508af8c6ab055b53f07aca8b44ad0e95d` caused Registry Conformance v1.4 to execute and complete successfully.

The evidence does not establish that every possible repository mutation is forced through this workflow. Path-trigger behavior and non-bypassable branch or repository policy enforcement are separate controls.

---

## 4. Historical Execution Lineage

Prior executions remain separately attributable to their original repository states.

### 4.1 Workflow v1.4 / Run #10

| Field | Historical verified value |
|---|---|
| Workflow version | `v1.4` |
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
| Job name | `Validate registry controls` |
| Job ID | `99179974414` |
| Job conclusion | `success` |
| Deterministic validator | `success` |
| Fixture-driven fail-closed tests | `success` |

Run #10 established that the v1.4 workflow definition itself executed successfully after adding `CI-EVIDENCE.md` to the controlled trigger surface. It did not yet directly exercise a change to `CI-EVIDENCE.md`.

### 4.2 Workflow v1.3 / Run #9

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

Run #9 is evidence only for workflow v1.3 at its identified state. It SHALL NOT be retroactively treated as evidence for the v1.4 `CI-EVIDENCE.md` trigger.

### 4.3 Execution lineage

```text
v1.3
  commit: 2a9d1043dfd0b5fd485a14e5bbfadfd8a0e65a21
  run:    #9 / 33282383199
  result: success
        |
        | architecture + implementation inventory governed
        v
v1.4
  commit: 404e509eba958166c264636e0376d2b619880666
  run:    #10 / 33282520547
  result: success
        |
        | CI-EVIDENCE.md added to trigger surface
        v
v1.4 direct trigger-path validation
  commit: b2802ed508af8c6ab055b53f07aca8b44ad0e95d
  run:    #11 / 33282600271
  result: success
```

---

## 5. Reproducibility Links

### Current canonical direct trigger-path evidence

Workflow run #11:  
`https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33282600271`

Evidence commit:  
`https://github.com/emotionalinfrastructure/proof-of-signal/commit/b2802ed508af8c6ab055b53f07aca8b44ad0e95d`

### Historical v1.4 evidence

Workflow run #10:  
`https://github.com/emotionalinfrastructure/proof-of-signal/actions/runs/33282520547`

Historical evidence commit:  
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

For historical reproduction, reviewers SHOULD inspect repository files at the relevant evidence commit rather than assume current `main` remains byte-identical to an earlier evaluated state.

---

## 6. Assurance Boundary

The current canonical evidence supports the following bounded determination:

> A commit modifying `CI-EVIDENCE.md` directly triggered Registry Conformance workflow v1.4. GitHub Actions executed run #11 for commit `b2802ed508af8c6ab055b53f07aca8b44ad0e95d`; the `Validate registry controls` job completed successfully; and both the deterministic registry conformance step and fixture-driven fail-closed test step completed successfully.

Runs #10 and #9 separately establish successful execution for their respective earlier workflow states.

These executions do **not** independently establish:

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
| Run #11 exists for commit `b2802ed...` | Verified fact |
| The triggering commit modified `CI-EVIDENCE.md` | Verified fact from repository change history |
| Run #11 was triggered by a push to `main` | Verified fact |
| Run #11 completed successfully | Verified fact |
| Job `Validate registry controls` completed successfully | Verified fact |
| Deterministic registry validation succeeded | Verified fact |
| Fixture-driven fail-closed tests succeeded | Verified fact |
| The `CI-EVIDENCE.md` push-trigger path operated successfully for this tested commit | Verified technical execution fact |
| Every possible `CI-EVIDENCE.md` mutation will always trigger successfully | Not established by one execution |
| CI is non-bypassable through repository policy | Not established by this evidence |
| Every EII requirement is automated | Unsupported by this evidence |
| The registry is independently certified | Unsupported by this evidence |
| Underlying EII research is empirically validated by CI | Unsupported by this evidence |

---

## 8. Verification Procedure

An independent reviewer can inspect the direct trigger-path evidence as follows:

1. Inspect commit `b2802ed508af8c6ab055b53f07aca8b44ad0e95d` and confirm `CI-EVIDENCE.md` was modified.
2. Open workflow run `33282600271` and confirm the head SHA is `b2802ed508af8c6ab055b53f07aca8b44ad0e95d`.
3. Confirm workflow name `Registry Conformance`, run number `11`, event `push`, status `completed`, and conclusion `success`.
4. Open `Validate registry controls` and confirm job ID `99180177120` completed successfully.
5. Confirm `Run deterministic registry conformance checks` concluded successfully.
6. Confirm `Run fixture-driven fail-closed tests` concluded successfully.
7. Inspect workflow v1.4 at the relevant repository state and confirm `CI-EVIDENCE.md` is included in the governed push path surface.
8. Inspect validator, tests, fixtures, test matrix, implementation inventory, and architecture at the same evidence state before drawing conclusions about scope.
9. Inspect runs #10 and #9 independently when reconstructing historical workflow evolution.

The reviewer SHALL NOT infer controls absent from the implementation state associated with the relevant evidence commit.

---

## 9. Canonical Determination

**Registry Conformance workflow v1.4 has direct trigger-path execution evidence for `CI-EVIDENCE.md` at commit `b2802ed508af8c6ab055b53f07aca8b44ad0e95d`.**

Current canonical supporting evidence:

```text
Workflow: Registry Conformance v1.4
Trigger artifact: CI-EVIDENCE.md
Run: #11
Run ID: 33282600271
Commit: b2802ed508af8c6ab055b53f07aca8b44ad0e95d
Job: Validate registry controls
Job ID: 99180177120
Run conclusion: success
Deterministic validator: success
Fixture-driven fail-closed tests: success
```

Historical predecessor, v1.4 definition execution:

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

Historical predecessor, v1.3 execution:

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
| `1.2` | v1.4 / run #11 | Recorded the first direct trigger-path validation of `CI-EVIDENCE.md` and retained runs #9 and #10 as historical execution lineage. |
