---
title: Open Loop vs. Closed Loop Load
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Queueing_Capacity_Models
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Open-loop vs. closed-loop load
taxonomy_id: mlsys.open-closed-loop-load
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Open Loop vs. Closed Loop Load

A distinction between arrivals scheduled independently of responses and arrivals triggered by prior completions, which changes offered-load feedback and the queueing behavior a load test exposes.

## Browsing Home

[[02 Concepts/Foundations/Quantitative System Models/Queueing & Capacity Models Subject|Queueing & Capacity Models]] → [[02 Concepts/Foundations/Quantitative System Models/Quantitative System Models Index|Quantitative System Models]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets whether responses throttle the [[02 Concepts/Foundations/Quantitative System Models/Arrival Rate|Arrival Rate]]. **Condition:** Closed-loop clients cap concurrency at their own count, so arrival rate falls as latency rises; open-loop arrivals do not respond to latency.

- Changes, through response feedback and concurrency limits, the offered load behind [[02 Concepts/Foundations/Quantitative System Models/Latency Throughput Curve|Latency Throughput Curve]]. **Condition:** When generator concurrency, think time, and response feedback change offered arrivals, the measured curve must be interpreted under that load model; closed-loop tests can still reach saturation.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: open-loop load generator; closed-loop load generator; open versus closed system model.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
