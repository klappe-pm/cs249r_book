---
title: Mixed Precision Training
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Numerical_Formats_Precision
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Mixed-precision training
taxonomy_id: mlsys.mixed-precision
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Mixed Precision Training

Training with multiple numerical formats and explicit handling of their range and accumulation behavior.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Formats & Precision Subject|Numerical Formats & Precision]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires managing [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Stability|Numerical Stability]]. **Condition:** Loss scaling or wider accumulation is useful only for the relevant numerical regime.

- Reduces activation and gradient bytes in [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Activations and gradients are stored in 16-bit formats while a master copy of weights stays in higher precision.

- Gains throughput from [[02 Concepts/Stack/Hardware & Accelerators/Matrix Engine|Matrix Engine]]. **Condition:** The matrix engine supports the reduced input formats with wider accumulation.

- Lowers the bytes moved per operation for operands held in the reduced format, shifting a kernel's position in [[02 Concepts/Foundations/Quantitative System Models/Compute Bound vs. Memory Bound|Compute Bound vs. Memory Bound]]. **Condition:** When the reduced format is applied to the operands that dominate traffic; master weights and accumulators keep full width, and attainable arithmetic throughput changes with the format as well.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
