# EII Public Provenance Registry Governance

**Document ID:** EII-REG-GOV-001  
**Version:** 1.0  
**Status:** Active  
**Effective date:** 2026-08-28

## Purpose

This document defines stewardship and change control for the EII Public Provenance Registry. It governs the registry infrastructure itself, not the scientific or legal merits of artifacts represented within it.

## Authority and maintenance

The Emotional Infrastructure Institute maintains the registry and its controlling documents. Registry maintenance SHALL preserve chronology, evidence boundaries, artifact identity, and the distinction between provenance and validation.

## Control hierarchy

For active registry operations:

1. `REGISTRY-SCHEMA.md` controls provenance-record conformance and admission.
2. `REGISTRY-INDEX.md` controls the human-readable list of admitted records.
3. `registry-index.json` mirrors the admitted record set for machine consumption.
4. `registry-index.schema.json` controls structural validation of the JSON representation.
5. Individual provenance records contain the artifact-specific evidence state.
6. `README.md` provides public orientation and SHALL NOT override normative schema requirements.

## Change classes

**Editorial change:** wording, formatting, or navigation change that does not alter evidentiary meaning or conformance requirements.

**Control change:** modification to required metadata, accepted states, evidence boundaries, acceptance criteria, integrity requirements, or registry behavior.

**Record correction:** modification to an admitted record because information was incomplete, inaccurate, or no longer current.

**Supersession:** replacement of an artifact or provenance record by a later controlled object while preserving the earlier chronology.

## Versioning

Control documents SHALL use explicit versions. Material control changes SHALL increment the applicable version. Editorial changes MAY retain the same version when they do not change normative meaning, but Git history SHALL preserve the revision.

## Admission authority

A record SHALL enter the active registry only after applicable acceptance criteria under the controlling schema have been evaluated. Admission means the provenance record is structurally and evidentially fit for registry inclusion. It does not mean the underlying artifact is validated, adopted, compliant, or externally endorsed.

## Conflict resolution

When two active registry representations conflict, the discrepancy SHALL be treated as a defect. The maintainer SHALL inspect Git history and the underlying provenance record, identify the defensible state, correct the affected control surfaces, and preserve the correction in repository history.

The most recent commit SHALL NOT automatically be assumed correct merely because it is newer.

## Historical preservation

Legacy material MAY remain in repository history even when it does not satisfy current registry requirements. Historical preservation SHALL NOT silently elevate superseded terminology or claims into current EII positions.

## Security and privacy

Registry transparency SHALL be balanced against legitimate privacy, confidentiality, research-integrity, and security requirements. Restricted evidence MAY be represented through controlled identifiers and cryptographic digests without publication of the underlying material.

## Review cadence

The control layer SHOULD be reviewed whenever:

- a new record class is introduced;
- a new integrity mechanism is proposed;
- automation is added;
- a material inconsistency is discovered;
- a provenance dispute reveals an ambiguity in the schema; or
- accumulated operational experience shows that an acceptance criterion is not sufficiently testable.

## Governance boundary

This governance document establishes internal repository controls. It SHALL NOT be described as external certification, legal registration, standards-body recognition, institutional approval, or independent assurance.
