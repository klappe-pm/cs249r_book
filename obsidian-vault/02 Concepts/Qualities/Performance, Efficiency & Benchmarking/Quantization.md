---
title: Quantization
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Quantization
taxonomy_id: mlsys.quantization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Quantization

Representing values using a reduced discrete set with a specified encoding and approximation rule.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-quantization-precision-cd46|V1-10.04 Numerical Precision Changing How Values Are Stored]] — Quantization. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/10_model_compression.qmd#L3499).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Lowers the numerical precision of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]]. **Condition:** The encoding, scale, and rounding rule determine the approximation.

- Requires re-evaluation of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Quality and calibration must be evaluated for the resulting deployed system.

- Can encode values in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Block Scaled Number Formats|Block Scaled Number Formats]]. **Condition:** Hardware or kernels support the block-scaled element and scale formats.

- Raises throughput per accelerator, cutting [[02 Concepts/Qualities/Sustainability & Cost/Cost per Token|Cost per Token]]. **Condition:** When the lower precision keeps quality acceptable and the serving stack has kernels for it.

- Shrinks the bytes of stored weights, activations, or caches in [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** When tensors are stored in the reduced format rather than only computed in it; dequantization buffers and scale factors add back a small share.

- Cuts bytes moved and energy per multiply-accumulate, lowering [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]. **Condition:** The target hardware has low-precision datapaths; dequantization overhead must not dominate.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
