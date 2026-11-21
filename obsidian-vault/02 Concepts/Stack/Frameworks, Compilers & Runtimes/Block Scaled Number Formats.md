---
title: Block Scaled Number Formats
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Numerical_Formats_Precision
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Block-scaled number formats
taxonomy_id: mlsys.block-scaled-format
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Block Scaled Number Formats

Low-precision formats in which small blocks of values share a scale factor, extending dynamic range for FP8, FP6, FP4, or INT8 elements.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Formats & Precision Subject|Numerical Formats & Precision]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Extends the representable range, at fixed element bits, of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Precision|Numerical Precision]]. **Condition:** When values within each block have similar magnitude so one shared scale serves them all.

- Limits the range damage from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Activation Outliers|Activation Outliers]]. **Condition:** A shared scale per small block confines an outlier's effect to its own block.

- Fixes in hardware a fine-grained choice of [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Quantization Granularity|Quantization Granularity]]. **Condition:** When the number format itself carries one shared scale per small block.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MX; microscaling; MXFP8; FP8 with block scaling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
