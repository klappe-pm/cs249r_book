---
title: Rail Optimized Topology
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Rail-optimized topology
taxonomy_id: mlsys.rail-optimized
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Rail Optimized Topology

A fabric design connecting the same-index accelerator of every node to a common leaf switch, keeping most collective traffic within one switch hop.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shapes the group-to-rail placement of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** When parallel groups are placed so their peers share a rail, keeping most of their collective traffic within one leaf switch.

- Is a kind of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]. **Condition:** Same-index accelerators across nodes share a leaf switch.

- Relies for cross-rail traffic on [[02 Concepts/Stack/Hardware & Accelerators/Scale Up Interconnect|Scale Up Interconnect]]. **Condition:** Traffic between different rails is forwarded through the node's scale-up domain.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
