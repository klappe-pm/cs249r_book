---
title: Replication and Failover
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Replication and failover
taxonomy_id: mlsys.replication-failover
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Replication and Failover

Maintaining redundant replicas of a service or state and redirecting work to a healthy replica when one fails.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Raises [[02 Concepts/Qualities/Reliability & Fault Tolerance/Availability|Availability]]. **Condition:** When replica failures are independent and failover completes faster than the outage it masks.

- Requires [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]. **Condition:** When a failed-over primary may still be alive, so stale writers must be fenced to avoid split brain.

- Increases [[02 Concepts/Qualities/Sustainability & Cost/Total Cost of Ownership|Total Cost of Ownership]]. **Condition:** Redundant replicas add capital and operating cost in proportion to the replication factor.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
