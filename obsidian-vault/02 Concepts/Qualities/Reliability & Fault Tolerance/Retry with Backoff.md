---
title: Retry with Backoff
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Retry with backoff
taxonomy_id: mlsys.retry-backoff
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Retry with Backoff

Reissuing a failed request after increasing, typically jittered, delays and within a retry budget, so that transient faults recover without overloading dependencies.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]]. **Condition:** Retrying an operation with external effects is safe only when the operation is idempotent or deduplicated.

- Damps the retry amplification that sustains [[02 Concepts/Qualities/Reliability & Fault Tolerance/Metastable Failure|Metastable Failure]]. **Condition:** When retries are jittered and capped by a retry budget.

- Treats as its failure signal the expiry of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Timeouts and Deadline Propagation|Timeouts and Deadline Propagation]]. **Condition:** When a retry is issued on timeout rather than on an explicit error; the retry budget and the deadline must be set together.

## Themes

- [[03 Themes/Reliability and Recovery|Reliability and Recovery]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
