---
title: Single- vs. Multi Controller Execution
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Single- vs. multi-controller execution
taxonomy_id: mlsys.single-vs-multi-controller
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Single- vs. Multi Controller Execution

Whether one coordinating process issues work to all devices or every host runs the same program independently, trading orchestration flexibility against dispatch scalability.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a design axis of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Distributed Task and Actor Runtime|Distributed Task and Actor Runtime]]. **Condition:** A single controller simplifies heterogeneous pipelines but must keep per-step dispatch off the critical path to scale.

- Sets where per-step dispatch cost falls in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** One controller issuing work to many devices must keep dispatch asynchronous and off the critical path.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
