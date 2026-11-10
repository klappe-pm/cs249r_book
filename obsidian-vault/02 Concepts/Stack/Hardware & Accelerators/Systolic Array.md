---
title: Systolic Array
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Accelerator_Architecture
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Systolic array
taxonomy_id: mlsys.systolic-array
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Systolic Array

A grid of processing elements that pass operands rhythmically to neighbors, performing matrix multiplication with high operand reuse and little register-file traffic.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Accelerator Architecture Subject|Accelerator Architecture]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Executes [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** Operand shapes are tiled to the array dimensions.

- Is a kind of [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Execution Architecture|Accelerator Execution Architecture]]. **Condition:** Processing elements pass operands to neighbors under a fixed schedule.

- Reduces [[02 Concepts/Foundations/Quantitative System Models/Data Movement Energy|Data Movement Energy]]. **Condition:** Operands are reused across processing elements instead of being refetched from register files or memory.

- Operates under a chosen [[02 Concepts/Stack/Hardware & Accelerators/Accelerator Dataflow|Accelerator Dataflow]]. **Condition:** The array keeps one operand stationary, such as weights, while others stream.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
