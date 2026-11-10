---
title: Continuous Batching
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Continuous batching
taxonomy_id: mlsys.continuous-batching
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Continuous Batching

Scheduling at each generation iteration so finished sequences leave and new requests join a running batch.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13.10 LLM Serving#^sec-model-serving-continuous-batching-8bb6|V1-13.10 LLM Serving]] — Continuous batching. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/13_model_serving/13_model_serving.qmd#L4866).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/Lifecycle/Deployment & Serving/Request Batching|Request Batching]]. **Condition:** Applies to iterative generation, where requests finish at different steps.

- Increases [[02 Concepts/Lifecycle/Deployment & Serving/SLO Goodput|SLO Goodput]]. **Condition:** Holds when KV memory admits enough concurrent sequences; interference between prefill and decode can raise latency.

- Relies on dynamic allocation from [[02 Concepts/Lifecycle/Deployment & Serving/Paged KV Allocation|Paged KV Allocation]]. **Condition:** Holds for vLLM-style engines where sequences join and leave each iteration.

- Admits and retires requests each iteration to avoid [[02 Concepts/Foundations/Quantitative System Models/Head of Line Blocking|Head of Line Blocking]]. **Condition:** When finished sequences would otherwise wait for the longest sequence in a static batch before new work is admitted.

## Themes

- [[03 Themes/Latency and Throughput|Latency and Throughput]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: iteration-level batching; in-flight batching.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
