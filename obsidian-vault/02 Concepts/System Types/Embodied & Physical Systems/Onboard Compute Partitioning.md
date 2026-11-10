---
title: Onboard Compute Partitioning
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Onboard compute partitioning
taxonomy_id: mlsys.onboard-compute-partitioning
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Onboard Compute Partitioning

Assigning perception, planning, and control workloads to the CPUs, accelerators, and microcontrollers of a robot, or offloading them, so each meets its deadline and criticality level.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Respects [[02 Concepts/System Types/Embodied & Physical Systems/Mixed Criticality Partitioning|Mixed Criticality Partitioning]]. **Condition:** Safety-critical and best-effort tasks share hardware.

- Is execution placement on a robot [[02 Concepts/Foundations/Workloads & Requirements/Execution Placement|Execution Placement]]. **Condition:** Workloads can run on several onboard processors or be offloaded.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: onboard workload placement; robot compute offloading.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
