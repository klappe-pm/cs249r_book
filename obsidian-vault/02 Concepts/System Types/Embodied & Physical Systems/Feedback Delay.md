---
title: Feedback Delay
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Feedback delay
taxonomy_id: mlsys.feedback-delay
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Feedback Delay

The total delay around the sense-compute-communicate-actuate loop, which erodes a controller's stability margin and adds motion before any response can begin, so it must be budgeted end to end rather than stage by stage.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/01 Machine Anatomy/04 The Nervous System/V4-04.04 Multi-Rate Cadences#^sec-nervous-time-constants-phase-lag|V4-04.04 Multi-Rate Cadences]] — Feedback-loop delay. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/04_nervous/04_nervous.qmd#L448).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits the stability margin of [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]. **Condition:** Delay can reduce stability margins; the effect depends on sampling and dynamics.

- Shrinks [[02 Concepts/Qualities/Safety & Assurance/Stopping Envelope|Stopping Envelope]]. **Condition:** Delay adds motion before braking; braking authority and uncertainty also matter.

- Bounds, through human reaction time, [[02 Concepts/Qualities/Responsible AI/Authority Handover|Authority Handover]]. **Condition:** Takeover is safe only if human reaction and re-orientation time fits within the remaining safety margin.

- Spends, at a rate set by the loop's bandwidth, [[02 Concepts/System Types/Embodied & Physical Systems/Loop Stability Margin|Loop Stability Margin]]. **Condition:** Each unit of delay costs phase in proportion to the crossover frequency.

- Destabilizes stiff contact under [[02 Concepts/System Types/Embodied & Physical Systems/Impedance and Force Control|Impedance and Force Control]]. **Condition:** When commanded stiffness is high and the loop delay is long relative to the contact dynamics.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
