---
title: Data Governance
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Contracts_Versioning_Lineage
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data governance
taxonomy_id: mlsys.data-governance
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Governance

Policies, roles, and controls that decide who may collect, access, use, and share which data, for which purposes, and under what accountability.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Contracts, Versioning & Lineage Subject|Data Contracts, Versioning & Lineage]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets policy for [[02 Concepts/Lifecycle/MLOps & Operations/Data Retention|Data Retention]]. **Condition:** Retention periods follow purpose and legal obligations.

- Depends on traceability from [[02 Concepts/Lifecycle/Data Engineering/Data Lineage|Data Lineage]]. **Condition:** Accountability for which data reached which model must be demonstrable.

- Enforces access decisions through [[02 Concepts/Qualities/Security & Privacy/Authorization|Authorization]]. **Condition:** Access policies are encoded as enforceable permissions.

- Enforces terms recorded in [[02 Concepts/Lifecycle/Data Engineering/Data and Model Licensing|Data and Model Licensing]]. **Condition:** Access and use decisions must respect license obligations.

- Requires [[02 Concepts/Qualities/Security & Privacy/PII Detection and De Identification|PII Detection and De Identification]]. **Condition:** Data contains personal information subject to regulation.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data stewardship.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
