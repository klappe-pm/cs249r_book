---
title: Quantization Aware Training
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Quantization-aware training
taxonomy_id: mlsys.quantization-aware-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Quantization Aware Training

Training or fine-tuning with simulated quantization in the forward pass so the model adapts to reduced precision, in contrast to post-training quantization.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-quantization-precision-cd46|V1-10.04 Numerical Precision Changing How Values Are Stored]] — Quantization. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/10_model_compression.qmd#L3499).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Simulates during training [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization|Quantization]]. **Condition:** When training models the rounding of the format the model will deploy in.

- Is an alternative to [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Post Training Quantization|Post Training Quantization]]. **Condition:** QAT recovers more accuracy at low bit widths but needs a training run; PTQ needs only a calibration set.

- Makes accurate, by simulating rounding and requantization during training, [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Integer Only Inference|Integer Only Inference]]. **Condition:** When the simulated quantization matches the deployed integer arithmetic and requantization rules.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: QAT.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
