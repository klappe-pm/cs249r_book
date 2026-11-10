---
title: Structured Pruning
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Model_Compression
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Structured pruning
taxonomy_id: mlsys.structured-pruning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Structured Pruning

Pruning whole channels, filters, heads, or layers so that the remaining model stays dense and runs faster without sparse-execution support.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model Compression Subject|Model Compression]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes#^sec-model-compression-pruning-d1cb|V1-10.03 Structural Optimization Changing What the Model Computes]] — Weight sparsity. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/10_model_compression.qmd#L642).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Pruning|Pruning]]. **Condition:** When the pruned unit is a whole channel, filter, head, or layer rather than an individual weight.

- Reduces dense-hardware [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Execution Time|Execution Time]]. **Condition:** When whole channels, filters, or heads are removed so the remaining layers are smaller dense operations.

- Removes whole units for dense hardware instead of the fine per-group pattern of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/N M Structured Sparsity|N M Structured Sparsity]]. **Condition:** Both aim at real speedup from pruning; structured pruning needs no sparse-engine support but usually costs more quality at equal parameter reduction, N:M needs a matrix engine with the matching sparse instruction.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
