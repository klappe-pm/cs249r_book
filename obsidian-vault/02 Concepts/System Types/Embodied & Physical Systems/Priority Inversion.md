---
title: Priority Inversion
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Priority inversion
taxonomy_id: mlsys.priority-inversion
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Priority Inversion

A high-priority task blocked on a resource held by a lower-priority task while a medium-priority task preempts the holder, so the high-priority task's blocking time is unbounded and can exceed its deadline unless the scheduler bounds it.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Breaks the guarantees of [[02 Concepts/System Types/Embodied & Physical Systems/Real Time Scheduling|Real Time Scheduling]]. **Condition:** Tasks of different priorities share a lock or resource.

- Can unboundedly extend [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** No priority inheritance protocol is in place.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
