---
title: Data Contract
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Contracts_Versioning_Lineage
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data contract
taxonomy_id: mlsys.data-contract
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Contract

A specification of schema, semantics, validity rules, and availability for data exchanged between components.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Contracts, Versioning & Lineage Subject|Data Contracts, Versioning & Lineage]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.05 Stage Ownership and Hand-Offs#^sec-ml-workflow-stage-interface-specification-ae3c|V1-03.05 Stage Ownership and Hand-Offs]] — Stage interface contract. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/03_ml_lifecycle/03_ml_lifecycle.qmd#L946).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specifies the validity criteria for [[02 Concepts/Lifecycle/Data Engineering/Data Quality|Data Quality]]. **Condition:** A schema check alone cannot establish semantic correctness or task fitness.

- Makes explicit and versions [[02 Concepts/Lifecycle/Data Engineering/Data Dependency Debt|Data Dependency Debt]]. **Condition:** Holds when every model input is consumed through a declared, owned contract rather than an ad hoc signal.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
