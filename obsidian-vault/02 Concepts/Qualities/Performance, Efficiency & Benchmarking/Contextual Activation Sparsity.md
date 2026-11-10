---
title: Contextual Activation Sparsity
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Contextual activation sparsity
taxonomy_id: mlsys.activation-sparsity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Contextual Activation Sparsity

Skipping neurons, heads, or channels whose activations are predicted negligible for the current input, reducing per-token compute and weight reads at inference.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an input-dependent form of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Sparsity|Sparsity]]. **Condition:** The zero pattern changes per token.

- Skips work per input rather than permanently as in [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Pruning|Pruning]]. **Condition:** Static pruning removes the same weights for every input.

- Shortens [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** Decode is memory-bound and skipped weights need not be read.

- Skips the predicted-inactive neurons of [[02 Concepts/Foundations/Models & Architectures/Feed Forward Block|Feed Forward Block]]. **Condition:** When a hidden unit's activation is predicted near zero for the current token, so its weight rows need not be read or multiplied.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: dynamic activation sparsity; contextual sparsity.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
