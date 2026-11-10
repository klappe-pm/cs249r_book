---
title: Data Dependency Debt
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Contracts_Versioning_Lineage
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data dependency debt
taxonomy_id: mlsys.data-dependency
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Dependency Debt

Undeclared, unstable, or underused input signals on which a model depends, which can change or break its behavior silently.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Contracts, Versioning & Lineage Subject|Data Contracts, Versioning & Lineage]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Amplifies [[02 Concepts/Lifecycle/MLOps & Operations/Entanglement|Entanglement]]. **Condition:** Holds when unstable or unused inputs remain in a model whose behavior depends jointly on all inputs.

- Can propagate [[02 Concepts/Lifecycle/Data Engineering/Data Cascade|Data Cascade]]. **Condition:** Downstream consumers depend on undeclared upstream signals.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
