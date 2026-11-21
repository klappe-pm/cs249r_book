---
title: Fan Out Tail Amplification
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Latency_Throughput_Goodput
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fan-out tail amplification
taxonomy_id: mlsys.fan-out-tail-amplification
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fan Out Tail Amplification

The growth in a request's latency tail when it waits on many parallel subrequests, because the chance that at least one subrequest is slow rises with the fan-out.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Latency, Throughput & Goodput Subject|Latency, Throughput & Goodput]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Raises [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** When completion waits for all subrequests and their slow events are not perfectly coincident.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: tail at scale.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
