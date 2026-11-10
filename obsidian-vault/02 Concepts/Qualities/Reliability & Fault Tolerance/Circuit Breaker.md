---
title: Circuit Breaker
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Circuit breaker
taxonomy_id: mlsys.circuit-breaker
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Circuit Breaker

A client-side guard that stops sending requests to a failing dependency after an error threshold and probes it before resuming traffic.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds [[02 Concepts/Qualities/Reliability & Fault Tolerance/Retry with Backoff|Retry with Backoff]]. **Condition:** When the breaker's error threshold trips before retries saturate the failing dependency.

- Enables [[02 Concepts/Qualities/Reliability & Fault Tolerance/Graceful Degradation|Graceful Degradation]]. **Condition:** When an open breaker routes requests to a fallback response rather than returning errors.

- Cuts the request rate reaching a failing dependency, lowering its [[02 Concepts/Foundations/Quantitative System Models/Arrival Rate|Arrival Rate]]. **Condition:** While the breaker is open, which gives the overloaded dependency time to recover.

- Counts expirations as errors in [[02 Concepts/Qualities/Reliability & Fault Tolerance/Timeouts and Deadline Propagation|Timeouts and Deadline Propagation]]. **Condition:** When slow responses, not only explicit failures, trip the breaker.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
