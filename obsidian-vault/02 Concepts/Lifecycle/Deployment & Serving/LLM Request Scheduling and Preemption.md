---
title: LLM Request Scheduling and Preemption
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: LLM request scheduling and preemption
taxonomy_id: mlsys.llm-request-scheduling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# LLM Request Scheduling and Preemption

Ordering, prioritizing, and preempting in-flight generation requests at iteration granularity, swapping or recomputing their KV state, to meet latency targets and fairness goals.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reorders requests inside [[02 Concepts/Lifecycle/Deployment & Serving/Continuous Batching|Continuous Batching]]. **Condition:** Scheduling decisions occur at each generation iteration.

- Shapes [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Long and short generations share capacity under load.

- Sets, through its prefill-versus-decode priority, how long a new request waits for [[02 Concepts/Lifecycle/Deployment & Serving/Time to First Token|Time to First Token]]. **Condition:** Continuous-batching engines where prefill and decode share iterations.

- Preempts in-flight requests by evicting or swapping blocks, bounding resident [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Continuous-batching engines with preemption; recompute-on-resume costs prefill time.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: request preemption; iteration-level scheduling.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
