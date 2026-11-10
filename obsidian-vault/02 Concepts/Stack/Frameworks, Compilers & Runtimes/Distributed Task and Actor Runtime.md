---
title: Distributed Task and Actor Runtime
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Distributed task and actor runtime
taxonomy_id: mlsys.task-actor-runtime
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Distributed Task and Actor Runtime

A runtime exposing stateless remote tasks and stateful actors as future-returning calls scheduled across a cluster; implementations add a shared object store and lineage-based recovery.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Orchestrates [[02 Concepts/Lifecycle/Training & Adaptation/RL Rollout Generation|RL Rollout Generation]]. **Condition:** Applies when rollout workers, trainers, and reward models run as separate stateful actors exchanging data through the runtime.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: actor model runtime; Ray-style runtime.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
