---
title: Synchronous vs. Asynchronous Training
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Synchronous vs. asynchronous training
taxonomy_id: mlsys.sync-async-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Synchronous vs. Asynchronous Training

Choosing whether workers apply an update only after every gradient for a step is combined, or apply updates independently on possibly stale parameters.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a design choice within [[02 Concepts/Stack/Parallelism & Distributed Execution/Data Parallelism|Data Parallelism]]. **Condition:** Replicas train on different examples and must coordinate updates.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: synchronous SGD; asynchronous SGD; async SGD.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
