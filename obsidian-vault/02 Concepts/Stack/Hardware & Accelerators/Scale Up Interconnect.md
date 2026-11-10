---
title: Scale Up Interconnect
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Host_Device_Scale_Up_Interconnect
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Scale-up interconnect
taxonomy_id: mlsys.scale-up-interconnect
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Scale Up Interconnect

High-bandwidth links and switches, such as NVLink-class fabrics, joining accelerators within a node or rack into one tightly coupled domain.

## Browsing Home

[[02 Concepts/Stack/Hardware & Accelerators/Host Device & Scale Up Interconnect Subject|Host Device & Scale Up Interconnect]] → [[02 Concepts/Stack/Hardware & Accelerators/Hardware & Accelerators Index|Hardware & Accelerators]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the efficient group size of [[02 Concepts/Stack/Parallelism & Distributed Execution/Tensor Parallelism|Tensor Parallelism]]. **Condition:** Tensor-parallel collectives occur every layer and need the highest-bandwidth links.

- Forms the fastest tier of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]. **Condition:** The cluster topology is hierarchical, with a node or rack domain joined by a slower scale-out fabric.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
