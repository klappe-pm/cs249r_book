---
title: N M Structured Sparsity
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: N:M structured sparsity
taxonomy_id: mlsys.nm-sparsity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# N M Structured Sparsity

A fine-grained pattern keeping at most N nonzero values in every group of M, such as 2:4, that matrix engines can skip for real speedup.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires support in [[02 Concepts/Stack/Hardware & Accelerators/Matrix Engine|Matrix Engine]]. **Condition:** Speedup materializes only on matrix engines with sparse-operand instructions for the specific N:M ratio.

- Specializes [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Sparsity|Sparsity]]. **Condition:** Constrains sparsity to a fixed per-group pattern so hardware can index nonzeros with small metadata.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: 2:4 sparsity; semi-structured sparsity.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
