---
title: Model Hardware Co Design
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Aware_Model_Design
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model-hardware co-design
taxonomy_id: mlsys.model-hardware-co-design
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Hardware Co Design

Jointly choosing model architecture and hardware or kernel design so that each exploits the other's structure.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Hardware Aware Model Design Subject|Hardware Aware Model Design]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can shift outward [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Accuracy Efficiency Frontier|Accuracy Efficiency Frontier]]. **Condition:** When model structure and hardware or kernels are designed together rather than one being fixed while the other is tuned.

- Jointly specifies [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Execution Architecture|Accelerator Execution Architecture]]. **Condition:** When the accelerator's dataflow, precision support, or memory hierarchy is a design variable alongside the model.

- Enables [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/N M Structured Sparsity|N M Structured Sparsity]]. **Condition:** When the sparsity pattern is chosen to match a sparse matrix-engine instruction, as with 2:4 sparsity on sparse tensor cores.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
