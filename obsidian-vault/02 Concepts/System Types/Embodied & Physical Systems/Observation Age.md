---
title: Observation Age
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Observation age
taxonomy_id: mlsys.observation-age
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Observation Age

Elapsed time between a physical observation and its use in a decision.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/08 Sensor Perception/V4-08.05 Bounding Observation Age#^sec-perception-age-budget|V4-08.05 Bounding Observation Age]] — Observation age. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/08_perception/08_perception.qmd#L958).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Inflates the uncertainty of [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** State can evolve between capture and use; propagation depends on the plant and disturbances.

- Is measurable across sensors only under [[02 Concepts/System Types/Embodied & Physical Systems/Sensor Time Synchronization|Sensor Time Synchronization]]. **Condition:** Observation age can be computed only when capture and use timestamps share a synchronized clock.

- Quantifies one dimension of [[02 Concepts/System Types/Agentic Systems/Context Staleness|Context Staleness]]. **Condition:** Observations carry acquisition timestamps.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
