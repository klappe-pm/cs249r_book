---
title: Load Balancing Loss
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Sparse_Conditional_Computation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Load-balancing loss
taxonomy_id: mlsys.load-balancing-loss
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Load Balancing Loss

An auxiliary training objective that penalizes uneven token assignment across experts so routing stays balanced.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Sparse & Conditional Computation Subject|Sparse & Conditional Computation]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Regularizes toward balance [[02 Concepts/Foundations/Models & Architectures/Expert Routing|Expert Routing]]. **Condition:** The auxiliary loss weight is large enough to counter router collapse without dominating the task loss.

- Reduces hot-expert imbalance behind [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** Under expert parallelism, an overloaded expert's device finishes last and holds back the step.

- Is an auxiliary objective in training of [[02 Concepts/Foundations/Models & Architectures/Mixture of Experts|Mixture of Experts]]. **Condition:** Routing is learned and can otherwise collapse onto a few experts.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: auxiliary loss.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
