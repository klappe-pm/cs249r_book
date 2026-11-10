---
title: Pruning
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Pruning
taxonomy_id: mlsys.pruning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Pruning

Removing weights, neurons, channels, or other structures judged unimportant from a network, usually followed by fine-tuning to recover quality.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Produces [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Sparsity|Sparsity]]. **Condition:** When pruning removes individual weights, leaving an irregular zero pattern whose speedup depends on sparse-execution support.

- Reduces [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When the pruned weights are stored in a compressed or smaller dense form rather than as explicit zeros.

- Relies on, to turn zeros into wall-clock speedup, [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Sparse Tensor Kernels|Sparse Tensor Kernels]]. **Condition:** Sparsity is high enough to overcome irregular access.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
