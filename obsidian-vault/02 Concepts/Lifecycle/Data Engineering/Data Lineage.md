---
title: Data Lineage
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Contracts_Versioning_Lineage
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data lineage
taxonomy_id: mlsys.lineage
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Lineage

Recorded dependencies that identify the sources and transformations of a dataset or artifact.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Contracts, Versioning & Lineage Subject|Data Contracts, Versioning & Lineage]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.04 The Retrieval Contract#^sec-vol3-persistent-result-envelope|V3-06.04 The Retrieval Contract]] — Source provenance. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/06_long_term_memory/06_long_term_memory.qmd#L181).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reveals undeclared and underused [[02 Concepts/Lifecycle/Data Engineering/Data Dependency Debt|Data Dependency Debt]]. **Condition:** Lineage must be captured at the feature or column level and compared against what the model actually consumes.

- References immutable [[02 Concepts/Lifecycle/Data Engineering/Dataset Versioning|Dataset Versioning]]. **Condition:** Lineage is only replayable if the referenced datasets are versioned.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
