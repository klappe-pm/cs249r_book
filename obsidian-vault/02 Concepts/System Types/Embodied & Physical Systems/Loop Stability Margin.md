---
title: Loop Stability Margin
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Loop stability margin
taxonomy_id: mlsys.loop-stability-margin
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Loop Stability Margin

The allowed gain or phase variation before a specified feedback loop becomes unstable, used to budget delay and model uncertainty around an operating point.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Caps the achievable bandwidth and gain of [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]. **Condition:** When the controller is tuned to keep a stated margin under the worst-case delay and plant variation.

- Takes its plant model from [[02 Concepts/System Types/Embodied & Physical Systems/System Identification|System Identification]]. **Condition:** When an identified plant response is combined with a specified controller to compute the margin.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: phase margin; gain margin; stability margin.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
