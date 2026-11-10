---
title: Weight Only Quantization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Weight-only quantization
taxonomy_id: mlsys.weight-only-quantization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Weight Only Quantization

Storing weights at low bit width while computing in higher-precision activations, cutting memory traffic for bandwidth-bound decoding, with error-compensating or activation-aware rounding.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is commonly produced by [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Post Training Quantization|Post Training Quantization]]. **Condition:** For GPTQ- and AWQ-class methods applied after training.

- Reduces [[02 Concepts/Lifecycle/Deployment & Serving/Time per Output Token|Time per Output Token]]. **Condition:** When small-batch decoding is memory-bandwidth-bound and dequantization is fused into the matrix multiply.

- Sidesteps [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Activation Outliers|Activation Outliers]]. **Condition:** Because activations stay in higher precision, outlier channels never enter a low-bit activation range.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: W4A16; GPTQ; AWQ; codebook weight quantization; vector quantization of weights; additive quantization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
