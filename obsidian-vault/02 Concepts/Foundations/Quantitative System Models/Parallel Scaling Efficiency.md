---
title: Parallel Scaling Efficiency
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Amdahl_s_Law_Scaling_Efficiency
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Parallel scaling efficiency
taxonomy_id: mlsys.parallel-efficiency
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Parallel Scaling Efficiency

Achieved speedup divided by the factor of added resources, measuring how much additional hardware turns into useful progress.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Amdahl's Law & Scaling Efficiency Subject|Amdahl's Law & Scaling Efficiency]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01.06 The C³ Taxonomy and Foundations of Scale#^sec-vol2-introduction-fleet-law|V2-01.06 The C³ Taxonomy and Foundations of Scale]] — Distributed step time. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/01_introduction/01_introduction.qmd#L2744).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Measures [[02 Concepts/Foundations/Quantitative System Models/Strong Scaling|Strong Scaling]]. **Condition:** Problem size is fixed while resources grow.

- Measures [[02 Concepts/Foundations/Quantitative System Models/Weak Scaling|Weak Scaling]]. **Condition:** Work per resource is fixed while resources and problem size grow.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: scaling efficiency.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
