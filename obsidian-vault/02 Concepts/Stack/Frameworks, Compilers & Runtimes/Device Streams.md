---
title: Device Streams
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Device streams
taxonomy_id: mlsys.device-streams
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Device Streams

Ordered queues of device work that the host enqueues asynchronously, with events expressing dependencies and allowing overlap across queues.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enables [[02 Concepts/Stack/Parallelism & Distributed Execution/Communication Overlap|Communication Overlap]]. **Condition:** Communication and computation are issued on independent streams with correct event dependencies.

- Hides, through asynchronous enqueue, exposed [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** The host can run ahead of the device, so launch work overlaps device execution until queues drain.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: CUDA streams.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
