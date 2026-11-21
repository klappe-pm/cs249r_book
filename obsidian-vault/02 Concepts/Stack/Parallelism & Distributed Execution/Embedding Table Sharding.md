---
title: Embedding Table Sharding
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Embedding-table sharding
taxonomy_id: mlsys.embedding-table-sharding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Embedding Table Sharding

Partitioning very large sparse embedding tables row-, column-, or table-wise across devices, usually model-parallel beside data-parallel dense layers.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Makes trainable [[02 Concepts/Foundations/Models & Architectures/Deep Recommendation Model|Deep Recommendation Model]]. **Condition:** Embedding tables exceed one device's memory and must be partitioned across devices.

- Requires all-to-all [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Lookups for a batch touch rows held on other devices, so activations are exchanged.

- Is the model-parallel part of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** Dense layers are data-parallel while embedding tables are partitioned.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DLRM sharding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
