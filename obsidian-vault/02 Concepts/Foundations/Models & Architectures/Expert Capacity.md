---
title: Expert Capacity
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Sparse_Conditional_Computation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Expert capacity
taxonomy_id: mlsys.expert-capacity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Expert Capacity

The maximum number of tokens an expert processes per batch, set by a capacity factor; tokens beyond it are dropped or rerouted.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Sparse & Conditional Computation Subject|Sparse & Conditional Computation]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds assignments made by [[02 Concepts/Foundations/Models & Architectures/Expert Routing|Expert Routing]]. **Condition:** A fixed per-expert buffer is allocated per batch.

- Is a buffer-size parameter of [[02 Concepts/Foundations/Models & Architectures/Mixture of Experts|Mixture of Experts]]. **Condition:** Experts process fixed-size per-batch buffers so computation shapes stay static.

- Increases padded token volume in [[02 Concepts/Stack/Parallelism & Distributed Execution/All to All Exchange|All to All Exchange]]. **Condition:** A higher capacity factor allocates larger per-expert buffers that are exchanged whether or not they are full.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: capacity factor.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
