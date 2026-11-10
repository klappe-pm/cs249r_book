---
title: Timing Jitter
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Timing jitter
taxonomy_id: mlsys.timing-jitter
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Timing Jitter

Variation in the period or completion time of a periodic sensing, inference, or control task, which degrades a controller designed for a fixed sample interval even when every deadline is met, so real-time budgets bound the spread of completion times and not only their worst case.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Degrades, by varying the sample interval of, [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]. **Condition:** When the controller's gains assume a fixed period and the actual release or completion time varies.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sampling jitter; control-loop jitter; period jitter; input-output jitter.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
