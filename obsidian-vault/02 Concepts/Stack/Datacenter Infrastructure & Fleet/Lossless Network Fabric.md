---
title: Lossless Network Fabric
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Network_Fabrics
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Lossless network fabric
taxonomy_id: mlsys.lossless-fabric
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Lossless Network Fabric

A network that avoids packet drops through credit-based or priority flow control, as RDMA transports expect, at the risk of head-of-line blocking.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Fabrics Subject|Network Fabrics]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides drop-free transport for [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Remote Direct Memory Access|Remote Direct Memory Access]]. **Condition:** The RDMA transport performs poorly under packet loss, as with RoCE.

- Requires [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Congestion Control|Datacenter Congestion Control]]. **Condition:** Priority flow control alone spreads congestion and pauses; end-to-end rate control keeps queues short.

- Can inflate [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Pause frames cause head-of-line blocking that delays unrelated flows under congestion.

- Applies pause-based flow control per priority class through [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Traffic Classes and QoS|Network Traffic Classes and QoS]]. **Condition:** When the fabric is made lossless with priority flow control, as in RoCE, rather than with credit-based link flow control.

- Can cause, through pause frames that stop a whole port or class, [[02 Concepts/Foundations/Quantitative System Models/Head of Line Blocking|Head of Line Blocking]]. **Condition:** When priority flow control pauses all traffic in a class because one downstream queue is congested.

- Can propagate pause frames into stalls that look healthy to some observers, a form of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Gray Failure|Gray Failure]]. **Condition:** Priority flow control enabled end to end; a single paused queue can block unrelated flows.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: PFC.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
