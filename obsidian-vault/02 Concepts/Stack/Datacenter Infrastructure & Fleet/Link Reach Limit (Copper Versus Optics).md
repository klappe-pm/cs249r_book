---
title: Link Reach Limit (Copper Versus Optics)
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Link reach limit (copper versus optics)
taxonomy_id: mlsys.link-reach
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Link Reach Limit (Copper Versus Optics)

The maximum distance over which a link meets its signal-quality requirements for a specified medium and signaling scheme, constraining cabling, retiming, and the geometry of connected accelerator domains.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the physical extent of [[02 Concepts/Stack/Hardware & Accelerators/Scale Up Interconnect|Scale Up Interconnect]]. **Condition:** When scale-up links run over passive copper, so the domain must fit within copper reach, typically one or a few racks.

- Forces accelerators into few racks, raising [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Rack Power Density|Rack Power Density]]. **Condition:** When a scale-up domain must stay within copper reach rather than spreading across the floor.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: copper reach; electrical reach; optical reach; SerDes reach.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
