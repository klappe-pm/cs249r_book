---
title: Kernel Fusion
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Kernel fusion
taxonomy_id: mlsys.fusion
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Kernel Fusion

Combining compatible operations to reduce intermediate materialization or dispatch.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.04 Execution from Graphs to Kernels#^sec-ml-frameworks-hybrid-approaches-jit-compilation-8954|V1-07.04 Execution from Graphs to Kernels]] — Kernel fusion. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/07_frameworks/07_frameworks.qmd#L1251).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can reduce [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** Fewer launches can reduce host work, depending on the original execution boundary.

- Raises, by keeping intermediates on chip instead of round-tripping them through device memory, [[02 Concepts/Foundations/Quantitative System Models/Arithmetic Intensity|Arithmetic Intensity]]. **Condition:** When the fused operations are memory-bound elementwise or reduction kernels whose intermediates would otherwise be written to and read back from device memory.

- Folds into a matrix-multiply epilogue the [[02 Concepts/Foundations/Models & Architectures/Activation Function|Activation Function]]. **Condition:** When the nonlinearity is elementwise, so it can be applied to tile outputs before they are written to memory.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
