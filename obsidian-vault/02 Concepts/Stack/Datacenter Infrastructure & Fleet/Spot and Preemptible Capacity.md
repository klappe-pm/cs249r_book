---
title: Spot and Preemptible Capacity
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Capacity_Planning_Multi_Tenancy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Spot and preemptible capacity
taxonomy_id: mlsys.spot-capacity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Spot and Preemptible Capacity

Discounted compute that the provider may reclaim at short notice, usable by workloads that tolerate interruption.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning & Multi Tenancy Subject|Capacity Planning & Multi Tenancy]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Exposes workloads to [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Job Preemption|Job Preemption]]. **Condition:** The provider reclaims capacity on short notice.

- Can lower [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Interruption overhead is smaller than the price discount.

- Reduces [[02 Concepts/Qualities/Sustainability & Cost/Total Cost of Ownership|Total Cost of Ownership]]. **Condition:** When workloads tolerate preemption through checkpointing or elasticity so the discount is not lost to rework.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
