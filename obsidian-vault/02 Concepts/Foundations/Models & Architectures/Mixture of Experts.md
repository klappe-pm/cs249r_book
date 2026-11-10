---
title: Mixture of Experts
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Sparse_Conditional_Computation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Mixture of experts
taxonomy_id: mlsys.mixture-of-experts
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Mixture of Experts

An architecture in which a learned router activates a small subset of expert subnetworks per token, decoupling total parameter count from per-token compute.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Sparse & Conditional Computation Subject|Sparse & Conditional Computation]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces relative to total parameters [[02 Concepts/Foundations/Models & Architectures/Active Parameters|Active Parameters]]. **Condition:** Each token is routed to only a small subset of experts.

- Still requires storing all experts within [[02 Concepts/Stack/Hardware & Accelerators/Memory Capacity|Memory Capacity]]. **Condition:** Every expert must be resident somewhere in the system even if inactive for a token.

- Replaces the dense sublayer with routed experts as an alternative to [[02 Concepts/Foundations/Models & Architectures/Feed Forward Block|Feed Forward Block]]. **Condition:** When a block's feed-forward sublayer is implemented as several routed experts instead of one dense network.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MoE.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
