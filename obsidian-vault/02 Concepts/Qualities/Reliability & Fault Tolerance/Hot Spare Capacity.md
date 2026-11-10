---
title: Hot Spare Capacity
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Checkpointing_Elastic_Recovery
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hot-spare capacity
taxonomy_id: mlsys.hot-spare-capacity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hot Spare Capacity

Idle, pre-provisioned accelerators or nodes reserved to replace failed workers, reducing the delay of acquiring replacement resources at the cost of reserved capacity.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Checkpointing & Elastic Recovery Subject|Checkpointing & Elastic Recovery]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Raises, by shortening node-replacement waits, the [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]. **Condition:** When reduced recovery and rework losses exceed the reserve time charged to the same goodput denominator.

- Holds idle capacity that lowers fleet [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** When fleet utilization counts the reserved idle spares in its capacity denominator.

- Replaces a failed worker instead of shrinking the job, unlike [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Elastic Training|Elastic Training]]. **Condition:** When both replacement at the original world size and continuation at a reduced world size are feasible recovery choices.

- Uses the failure interval summarized by [[02 Concepts/Qualities/Reliability & Fault Tolerance/Mean Time Between Failures|Mean Time Between Failures]]. **Condition:** When sizing converts component or job MTBF into a failure-arrival model and combines it with repair or replenishment times, failure correlations, and an acceptable spare-exhaustion probability.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: spare nodes; standby accelerators.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
