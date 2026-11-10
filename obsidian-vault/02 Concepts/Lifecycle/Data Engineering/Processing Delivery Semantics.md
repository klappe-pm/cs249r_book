---
title: Processing Delivery Semantics
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Processing delivery semantics
taxonomy_id: mlsys.delivery-semantics
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Processing Delivery Semantics

The guarantee a data pipeline gives about how often each record takes effect (at most once, at least once, or effectively once) under retries, replays, and failures, and the idempotent or transactional sinks that achieve it.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Achieves effectively-once results with [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]. **Condition:** Records may be redelivered after failures.

- Is a guarantee of [[02 Concepts/Lifecycle/Data Engineering/Stream Processing|Stream Processing]]. **Condition:** The pipeline retries or replays records after failures.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: exactly-once processing; at-least-once delivery; duplicate events.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
