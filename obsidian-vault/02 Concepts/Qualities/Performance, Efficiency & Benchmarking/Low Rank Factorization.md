---
title: Low Rank Factorization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Low-rank factorization
taxonomy_id: mlsys.low-rank-factorization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Low Rank Factorization

Approximating a weight matrix or tensor by a product of smaller factors of reduced rank to cut parameters and operations.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces the cost of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** When weight matrices are well approximated at a rank much smaller than their dimensions and the smaller products still run efficiently.

- Reduces [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When the chosen rank is much smaller than the matrix dimensions and the factored model keeps acceptable accuracy.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: low-rank approximation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
