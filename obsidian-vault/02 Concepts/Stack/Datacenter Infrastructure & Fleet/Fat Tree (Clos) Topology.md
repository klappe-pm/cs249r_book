---
title: Fat Tree (Clos) Topology
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fat-tree (Clos) topology
taxonomy_id: mlsys.fat-tree
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fat Tree (Clos) Topology

A multistage switch topology providing many equal-cost paths and, without oversubscription, full bisection bandwidth between endpoints.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can provide full [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Bisection Bandwidth|Bisection Bandwidth]]. **Condition:** Switch tiers are not oversubscribed.

- Is a kind of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]. **Condition:** The fabric is built from tiers of commodity switches.

- Lowers network cost within [[02 Concepts/Qualities/Sustainability & Cost/Total Cost of Ownership|Total Cost of Ownership]]. **Condition:** Identical commodity switches replace large high-radix core switches at equal bisection bandwidth.

- Is commonly built, to save cost, with [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Oversubscription|Network Oversubscription]]. **Condition:** When a fat-tree is built with fewer spine ports than leaf downlinks to save cost.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Clos.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
