---
title: Real Time Scheduling
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Real-time scheduling
taxonomy_id: mlsys.real-time-scheduling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Real Time Scheduling

Assigning processor time to periodic and sporadic tasks so that each meets its deadline, with schedulability established by analysis.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.06 Real-Time Command Transport and Bus Determinism#^sec-nervous-deterministic-fieldbuses|V4-04.06 Real-Time Command Transport and Bus Determinism]] — Response-time bound. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/04_nervous/04_nervous.qmd#L1323).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Takes as input [[02 Concepts/System Types/Embodied & Physical Systems/Worst Case Execution Time|Worst Case Execution Time]]. **Condition:** Schedulability results are valid only if WCET bounds hold on the deployed platform.

- Bounds [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Rate-monotonic scheduling guarantees deadlines only when processor utilization stays below the Liu-Layland bound.

- Bounds, through fixed priorities and periodic release, [[02 Concepts/System Types/Embodied & Physical Systems/Timing Jitter|Timing Jitter]]. **Condition:** When the control task has the highest priority or is released by a timer rather than by a best-effort scheduler.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: rate-monotonic; EDF; response-time analysis; hard real-time deadline.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
