---
title: Amdahl's Law
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Amdahl_s_Law_Scaling_Efficiency
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Amdahl's law
taxonomy_id: mlsys.amdahls-law
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Amdahl's Law

The bound that overall speedup from accelerating part of an execution is limited by the fraction left unaccelerated.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Amdahl's Law & Scaling Efficiency Subject|Amdahl's Law & Scaling Efficiency]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.02 Anatomy of an Accelerator#^sec-hardware-acceleration-ai-hardware-acceleration-fundamentals-9b28|V1-11.02 Anatomy of an Accelerator]] — Accelerated fraction. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/11_hw_acceleration/11_hw_acceleration.qmd#L67).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Parameterizes [[02 Concepts/Foundations/Quantitative System Models/Serial Fraction|Serial Fraction]]. **Condition:** The unaccelerated fraction is measured on the same workload as the speedup.

- Bounds speedup under [[02 Concepts/Foundations/Quantitative System Models/Strong Scaling|Strong Scaling]]. **Condition:** Problem size is fixed while resources grow.

- Bounds [[02 Concepts/Foundations/Quantitative System Models/Parallel Scaling Efficiency|Parallel Scaling Efficiency]]. **Condition:** The unparallelized fraction is fixed while workers are added to a fixed-size problem.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
