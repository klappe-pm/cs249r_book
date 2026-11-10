---
title: Fidelity Adaptive Serving
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Batching_Admission_Autoscaling
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fidelity-adaptive serving
taxonomy_id: mlsys.fidelity-adaptive-serving
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fidelity Adaptive Serving

Meeting a latency target under rising load by switching requests to a cheaper variant of the same model, such as a lower-precision copy, a pruned subnetwork, or fewer layers, so capacity is bought with controlled quality loss instead of queueing or rejection.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Batching, Admission & Autoscaling Subject|Batching, Admission & Autoscaling]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a kind of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Graceful Degradation|Graceful Degradation]]. **Condition:** When the degraded mode is a cheaper model variant rather than a feature cut.

- Obtains its cheaper variants from [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Weight Only Quantization|Weight Only Quantization]]. **Condition:** When the fallback variant is a lower-precision copy of the same weights.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: accuracy scaling under load; model switching under load; quality-elastic serving; runtime precision switching.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
