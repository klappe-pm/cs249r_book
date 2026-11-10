---
title: Worst Case Execution Time
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Worst-case execution time
taxonomy_id: mlsys.wcet
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Worst Case Execution Time

A justified execution-time upper bound under specified hardware and execution assumptions.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/13 Workload Placement/V4-13.08 Empirical Verification of Silicon Isolation#^sec-placement-testing-separation|V4-13.08 Empirical Verification of Silicon Isolation]] — Worst-case execution time. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/13_placement/13_placement.qmd#L1627).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Contributes to bounding [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** Execution-time bounds alone do not include all queueing, scheduling, sensing, and transport delays.

- Takes observed samples, as evidence but not as a bound, from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Profiling|Profiling]]. **Condition:** When a measurement-based bound is argued from execution traces plus analysis of unobserved states.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: WCET.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
