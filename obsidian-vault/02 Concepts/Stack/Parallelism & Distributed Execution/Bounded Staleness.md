---
title: Bounded Staleness
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Coordination_Consensus
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Bounded staleness
taxonomy_id: mlsys.bounded-staleness
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Bounded Staleness

A consistency model in which workers may compute on parameters up to a fixed number of updates old, trading freshness for less waiting.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Coordination & Consensus Subject|Coordination & Consensus]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces waiting on [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** Convergence tolerates updates computed on stale parameters within the bound.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: stale synchronous parallel.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
