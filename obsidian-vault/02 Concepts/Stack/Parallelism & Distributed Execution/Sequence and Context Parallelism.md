---
title: Sequence and Context Parallelism
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sequence and context parallelism
taxonomy_id: mlsys.sequence-parallel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sequence and Context Parallelism

Partitioning activations along the sequence dimension across devices, exchanging keys, values, or partial results so long sequences fit.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Extends the feasible [[02 Concepts/Foundations/Models & Architectures/Context Window|Context Window]]. **Condition:** Activation or attention memory for one sequence exceeds one device.

- Is one dimension of [[02 Concepts/Stack/Parallelism & Distributed Execution/Hybrid Parallelism|Hybrid Parallelism]]. **Condition:** Long-sequence training adds a sequence axis to the parallel mapping.

- Exchanges keys and values through [[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication|Collective Communication]]. **Condition:** Blocks of keys and values circulate among devices while attention is computed.

- Partitions activations along the sequence to lower the per-device [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Only activation memory shrinks; parameters and optimizer state are unaffected.

## Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: context parallelism; ring attention; sequence parallelism.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
