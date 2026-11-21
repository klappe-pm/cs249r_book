---
title: On Device Neural Accelerator
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Edge_Embedded_Hardware
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: On-device neural accelerator
taxonomy_id: mlsys.edge-npu
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# On Device Neural Accelerator

An accelerator integrated in mobile or embedded silicon for low-precision neural inference, usually supporting a restricted set of operators.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Edge & Embedded Hardware Subject|Edge & Embedded Hardware]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires supported low [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]]. **Condition:** The accelerator implements only specific integer or reduced-precision formats.

- Is one block of [[02 Concepts/Stack/Hardware & Accelerators/Heterogeneous Mobile SoC|Heterogeneous Mobile SoC]]. **Condition:** The SoC exposes the NPU alongside CPU, GPU, and DSP under shared memory and power.

- Reduces [[02 Concepts/Qualities/Sustainability & Cost/Energy per Inference|Energy per Inference]]. **Condition:** The model's operators and precisions are supported, so inference avoids CPU fallback.

- Accepts only fixed-point operator graphs lowered by [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Integer Only Inference|Integer Only Inference]]. **Condition:** For NPUs that support only integer operators.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: NPU.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
