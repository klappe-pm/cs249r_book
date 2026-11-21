---
title: Numerical Precision
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Numerical_Formats_Precision
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Numerical precision
taxonomy_id: mlsys.precision
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Numerical Precision

The representable values and arithmetic behavior of a numerical format.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Formats & Precision Subject|Numerical Formats & Precision]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.04 Numerical Precision Changing How Values Are Stored#^sec-model-compression-performance-gains-0656|V1-10.04 Numerical Precision Changing How Values Are Stored]] — Weight precision. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/10_model_compression/10_model_compression.qmd#L5168).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets storage width within [[02 Concepts/Lifecycle/Training & Adaptation/Training State|Training State]]. **Condition:** Different state components can use different formats.

- Affects [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Stability|Numerical Stability]]. **Condition:** Range, rounding, accumulation, and intermediate representation all matter.

## Themes

- [[03 Themes/Accuracy and Efficiency|Accuracy and Efficiency]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: number format; floating-point format; FP32; FP16; BF16; bfloat16; FP8; FP4.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
