---
title: Quantization Granularity
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Quantization granularity
taxonomy_id: mlsys.quantization-granularity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Quantization Granularity

The grouping of values that share quantization parameters, such as a scale and an optional zero point, from per tensor to per channel to small groups, trading approximation error against metadata and kernel cost.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a design choice within [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization|Quantization]]. **Condition:** When choosing scales for weights, activations, or caches.

- Isolates the range inflation from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Activation Outliers|Activation Outliers]]. **Condition:** When groups split along the outlier channels, per channel or finer.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: per-tensor quantization; per-channel quantization; group-wise quantization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
