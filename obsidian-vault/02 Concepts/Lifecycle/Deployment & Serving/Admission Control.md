---
title: Admission Control
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Admission control
taxonomy_id: mlsys.admission
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Admission Control

Accepting, delaying, or rejecting work according to capacity, policy, and service constraints.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Admits work against a known [[02 Concepts/Foundations/Quantitative System Models/Service Capacity|Service Capacity]]. **Condition:** Limits must be expressed in resources relevant to the workload.

- Bounds by shedding excess load [[02 Concepts/Foundations/Quantitative System Models/Queueing Delay|Queueing Delay]]. **Condition:** Holds when rejected work is not retried immediately into the same queue.

- Implements load shedding for [[02 Concepts/Qualities/Reliability & Fault Tolerance/Graceful Degradation|Graceful Degradation]]. **Condition:** Holds when shedding low-priority work keeps the remaining requests within their SLO.

- Caps per-client work to blunt [[02 Concepts/Qualities/Security & Privacy/Resource Exhaustion Attack|Resource Exhaustion Attack]]. **Condition:** When per-client quotas and token or step limits are enforced.

- Sheds the excess load that sustains [[02 Concepts/Qualities/Reliability & Fault Tolerance/Metastable Failure|Metastable Failure]]. **Condition:** When early rejection lowers admitted load below the degraded system's recovery threshold long enough to break the feedback loop.

- Caps the number of concurrent sequences whose state must stay resident in [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** When admission is based on projected KV memory rather than request count alone.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: load shedding; rate limiting.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
