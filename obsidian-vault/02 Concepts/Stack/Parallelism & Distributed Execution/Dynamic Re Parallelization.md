---
title: Dynamic Re Parallelization
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dynamic re-parallelization
taxonomy_id: mlsys.dynamic-resharding
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dynamic Re Parallelization

Redistributing model weights among devices at runtime so successive phases, such as generation and training or prefill and decode, each run under a better parallel layout.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Moves weight shards with [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Layouts differ between phases.

- Realizes [[02 Concepts/Lifecycle/Training & Adaptation/Policy Weight Synchronization|Policy Weight Synchronization]]. **Condition:** Training and generation share the same devices.

- Remaps shards across [[02 Concepts/Stack/Parallelism & Distributed Execution/Device Mesh|Device Mesh]]. **Condition:** Each phase uses a different mesh layout.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: parameter reallocation; runtime resharding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
