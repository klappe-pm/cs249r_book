---
title: Data Validation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Validation_Feature_Engineering
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data validation
taxonomy_id: mlsys.data-validation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Validation

Automated checks of incoming data against expected schema, value ranges, and distributions before it is used for training or serving.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Validation & Feature Engineering Subject|Data Validation & Feature Engineering]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enforces [[02 Concepts/Lifecycle/Data Engineering/Data Contract|Data Contract]]. **Condition:** The contract's schema and validity rules must be machine-checkable.

- Flags unexpected [[02 Concepts/Lifecycle/Data Engineering/Missing Data|Missing Data]]. **Condition:** Requires declared expectations on completeness per feature.

- Checks [[02 Concepts/Lifecycle/Data Engineering/Data Quality|Data Quality]]. **Condition:** Covers only the properties the checks encode, not semantic correctness.

- Flags undeclared [[02 Concepts/Lifecycle/Data Engineering/Schema Evolution|Schema Evolution]]. **Condition:** Holds when incoming data is compared against the expected schema version.

- Catches early defects that start [[02 Concepts/Lifecycle/Data Engineering/Data Cascade|Data Cascade]]. **Condition:** Checks run at ingestion and between stages.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
