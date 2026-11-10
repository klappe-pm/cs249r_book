---
title: Expert Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Expert parallelism
taxonomy_id: mlsys.expert-parallel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Expert Parallelism

Placing different experts of a mixture-of-experts layer on different devices and exchanging routed tokens among them.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires [[02 Concepts/Stack/Parallelism & Distributed Execution/All to All Exchange|All to All Exchange]]. **Condition:** Tokens are dispatched to and gathered from experts on other devices.

- Distributes the experts of [[02 Concepts/Foundations/Models & Architectures/Mixture of Experts|Mixture of Experts]]. **Condition:** Experts do not fit, or run too slowly, on one device.

- Is one dimension of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** MoE layers place experts across devices alongside data and tensor parallelism.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: EP.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
