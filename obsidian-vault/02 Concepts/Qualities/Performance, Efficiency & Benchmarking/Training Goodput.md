---
title: Training Goodput
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Profiling_Utilization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training goodput
taxonomy_id: mlsys.training-goodput
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Goodput

The fraction of allocated accelerator time that produces retained training progress, after losses to scheduling, failures, restarts, and lost work.

## Browsing Home

[[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling & Utilization Subject|Profiling & Utilization]] → [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Performance, Efficiency & Benchmarking Index|Performance, Efficiency & Benchmarking]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.03 ML Goodput#^sec-performance-engineering-goodput-factors|V2-09.03 ML Goodput]] — ML goodput. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/09_performance_engineering/09_performance_engineering.qmd#L195).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]. **Condition:** For a fixed model, data, and quality target, since lost and redone work lengthens wall-clock time.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ML goodput.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
