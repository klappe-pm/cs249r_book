---
title: Resource Quota
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Capacity_Planning_Multi_Tenancy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Resource quota
taxonomy_id: mlsys.resource-quota
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Resource Quota

A limit on the resources a tenant may hold or request, sometimes with guaranteed minimums and borrowing of idle capacity.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning & Multi Tenancy Subject|Capacity Planning & Multi Tenancy]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Partitions shared capacity within [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning|Capacity Planning]]. **Condition:** Shared capacity is divided among tenants with stated limits.

- Is a policy within [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Multi Tenancy|Multi Tenancy]]. **Condition:** Tenants share a cluster under stated limits and guarantees.

- Is an alternative to [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Dominant Resource Fairness|Dominant Resource Fairness]]. **Condition:** Both divide shared capacity among tenants; quotas are static limits, DRF adapts shares to demand.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
