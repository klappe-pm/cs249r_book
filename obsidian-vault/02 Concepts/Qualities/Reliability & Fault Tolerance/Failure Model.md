---
title: Failure Model
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Failure_Models_Retries_Degradation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Failure model
taxonomy_id: mlsys.failure-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Failure Model

The declared classes of faults and timing assumptions under which a mechanism is analyzed.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Models, Retries & Degradation Subject|Failure Models, Retries & Degradation]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the guarantees of [[02 Concepts/Stack/Parallelism & Distributed Execution/Replicated Log Consensus|Replicated Log Consensus]]. **Condition:** Fault classes, membership, quorum availability, and timing assumptions bound the agreement claim.

- Determines the recovery requirements for [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]]. **Condition:** Recovery semantics must cover the faults and state dependencies actually assumed.

- Bounds planned recovery in [[02 Concepts/Lifecycle/MLOps & Operations/Incident Response|Incident Response]]. **Condition:** A design's recovery guarantees are limited to its declared faults and assumptions; operations may also encounter unmodeled incidents.

- Selects candidate scenarios for [[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Injection|Failure Injection]]. **Condition:** Injected faults instantiate selected assumptions; realistic timing, combinations, observation criteria, and containment must be declared.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
