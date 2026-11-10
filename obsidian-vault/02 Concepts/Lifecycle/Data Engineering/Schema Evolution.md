---
title: Schema Evolution
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Schema evolution
taxonomy_id: mlsys.schema-evolution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Schema Evolution

Changing a data schema while explicitly managing how existing data and producers or consumers remain interpretable and compatible.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires compatibility rules in [[02 Concepts/Lifecycle/Data Engineering/Data Contract|Data Contract]]. **Condition:** Contracts must identify producers/consumers, field meaning, allowed changes, defaults, and migration expectations; format-supported changes need not preserve application semantics.

- Uncoordinated changes can cause [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Holds when training and serving read different schema versions or interpret a changed field differently.

- Can break [[02 Concepts/Lifecycle/MLOps & Operations/Model and Feature Compatibility|Model and Feature Compatibility]]. **Condition:** A schema change is not mirrored in the model's feature transformations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
