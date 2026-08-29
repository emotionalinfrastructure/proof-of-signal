# Security and Integrity Reporting

The EII Public Provenance Registry is an evidence-management repository. Integrity defects can include incorrect hashes, mismatched filenames, broken verification paths, exposed restricted information, misleading maturity states, or inconsistencies between human-readable and machine-readable registry surfaces.

## Reportable issues

Please report issues involving:

- a recorded digest that does not match the represented artifact;
- an incorrect or misleading provenance relationship;
- accidental publication of confidential, private, or security-sensitive information;
- machine-readable registry data that materially disagrees with `REGISTRY-INDEX.md`;
- a broken verification path that prevents inspection of an admitted public record; or
- a material claim that exceeds the evidence identified by the record.

## Public disclosure caution

Do not publish credentials, private keys, authentication tokens, personal records, exploit details that create unnecessary risk, or restricted research evidence in a public issue solely to demonstrate a problem.

Where a concern involves sensitive information, provide only the minimum information necessary to identify the affected repository object and preserve evidence of the problem through an appropriate restricted channel.

## Integrity response

Confirmed registry-integrity defects SHOULD be corrected through visible Git history. Corrections SHALL NOT silently erase the earlier public state when preserving that state is lawful and does not create an ongoing privacy or security risk.

## Scope boundary

This policy addresses repository integrity and responsible disclosure. It is not a representation that EII provides a security-certification program or that artifacts in the registry have undergone independent security assessment.
