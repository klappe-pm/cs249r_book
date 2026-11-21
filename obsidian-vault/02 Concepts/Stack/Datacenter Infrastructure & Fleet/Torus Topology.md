---
title: Torus Topology
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Torus topology
taxonomy_id: mlsys.torus-topology
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Torus Topology

A fabric in which accelerator nodes form a multidimensional grid with wraparound links to fixed neighbors rather than tiers of switches, so neighbor and ring traffic can run at link rate while global exchanges are routed hop by hop with lower bisection bandwidth that depends on dimensions, routing, and contention.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a kind of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]. **Condition:** When endpoints connect to neighbors directly, without a switch hierarchy.

- Is an alternative to [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Fat Tree (Clos) Topology|Fat Tree (Clos) Topology]]. **Condition:** Both connect accelerator nodes at scale; a torus saves switch cost and suits ring collectives, while a non-oversubscribed Clos fat-tree with suitable routing gives uniform bisection bandwidth for arbitrary traffic.

- Can be reconfigured and routed around failed nodes by [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Optical Circuit Switching|Optical Circuit Switching]]. **Condition:** When torus links pass through an optical circuit switch so slices of a pod can be joined into different torus shapes, as in TPU pods.

- Bounds, through multi-hop routing and lower bisection bandwidth, [[02 Concepts/Stack/Parallelism & Distributed Execution/All to All Exchange|All to All Exchange]]. **Condition:** When exchange traffic crosses many torus hops rather than staying among neighbors.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: torus; 2D torus; 3D torus.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
