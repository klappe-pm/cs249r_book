---
title: Multi Tenancy
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Capacity_Planning_Multi_Tenancy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-tenancy
taxonomy_id: mlsys.multi-tenancy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Tenancy

Sharing infrastructure among teams, jobs, or customers under policies for allocation, isolation, priority, and accounting.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning & Multi Tenancy Subject|Capacity Planning & Multi Tenancy]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]. **Condition:** Tenants must not observe or disrupt one another's work.

- Can share devices through [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Accelerator Sharing and Partitioning|Accelerator Sharing and Partitioning]]. **Condition:** Tenant workloads are too small to saturate whole accelerators.

- Increases exposure to [[02 Concepts/Qualities/Security & Privacy/Side Channel Attack|Side Channel Attack]]. **Condition:** When tenants share accelerators, caches, memory, or interconnect whose contention is observable.

- Requires [[02 Concepts/Qualities/Sustainability & Cost/Cost Attribution|Cost Attribution]]. **Condition:** When shared infrastructure must be charged back to the teams or workloads that consume it.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
