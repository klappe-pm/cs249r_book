---
title: Mixed Criticality Partitioning
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Mixed-criticality partitioning
taxonomy_id: mlsys.mixed-criticality
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Mixed Criticality Partitioning

Running functions of different assurance levels on shared hardware while preventing lower-criticality work from delaying or corrupting higher-criticality functions.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Protects the timing of [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]. **Condition:** Holds when the safety monitor shares hardware with learned components that can overrun or contend for memory.

- Requires temporal and spatial [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]. **Condition:** Shared caches, memory controllers, and buses can break isolation that address-space separation provides.

- Uses [[02 Concepts/System Types/Embodied & Physical Systems/Real Time Scheduling|Real Time Scheduling]]. **Condition:** Schedulability is analyzed with criticality-dependent WCET estimates for each task.

- Partitions time and resources so lower-criticality tasks cannot hold what high-criticality tasks need, preventing [[02 Concepts/System Types/Embodied & Physical Systems/Priority Inversion|Priority Inversion]]. **Condition:** Shared resources must have bounded access or be partitioned; priority inheritance still applies inside a partition.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
