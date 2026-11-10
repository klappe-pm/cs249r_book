---
title: Expert Routing
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Sparse_Conditional_Computation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Expert routing
taxonomy_id: mlsys.expert-routing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Expert Routing

The gating function that assigns each token to one or more experts, such as top-k softmax gating or expert-choice routing.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Sparse & Conditional Computation Subject|Sparse & Conditional Computation]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Determines token traffic in [[02 Concepts/Stack/Parallelism & Distributed Execution/All to All Exchange|All to All Exchange]]. **Condition:** Experts are placed on different devices from the tokens routed to them.

- Is the gating component of [[02 Concepts/Foundations/Models & Architectures/Mixture of Experts|Mixture of Experts]]. **Condition:** The layer routes each token to a small subset of experts.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: gating; router.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
