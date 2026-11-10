---
title: Replicated Log Consensus
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Coordination_Consensus
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Replicated-log consensus
taxonomy_id: mlsys.consensus
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Replicated Log Consensus

Agreement on an ordered state history under specified timing and failure assumptions.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Coordination & Consensus Subject|Coordination & Consensus]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Maintains the epoch authority used by [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]. **Condition:** Resource-enforced epochs remain necessary; a consensus log alone does not fence effects.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Paxos; Raft.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
