---
title: Variable Length Parallelism Planning
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Variable-length parallelism planning
taxonomy_id: mlsys.variable-length-parallelism
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Variable Length Parallelism Planning

Choosing, for each training step, sequence or context parallel degrees and how packed documents are sharded across ranks from that step's sequence lengths and attention patterns, so ranks receive balanced attention work.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Varies the degree and layout of [[02 Concepts/Stack/Parallelism & Distributed Execution/Sequence and Context Parallelism|Sequence and Context Parallelism]]. **Condition:** When training sequence lengths vary widely within and across steps.

- Rebalances per-rank attention work to limit [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** When a few long documents would otherwise make some ranks finish each step much later than others.

- Chooses document-to-rank assignments in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Sequence Packing|Sequence Packing]]. **Condition:** When packed sequences are distributed across the ranks of a sequence-parallel group.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: dynamic context parallelism; workload-balanced sequence parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
