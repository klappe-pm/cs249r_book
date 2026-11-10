---
title: Local SGD
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelism_Strategies
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Local SGD
taxonomy_id: mlsys.local-sgd
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Local SGD

Data-parallel training in which workers take several local optimizer steps between parameter synchronizations, cutting communication frequency for low-bandwidth or geo-distributed settings.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism Strategies Subject|Parallelism Strategies]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a periodically synchronized form of [[02 Concepts/Stack/Parallelism & Distributed Execution/Data Parallelism|Data Parallelism]]. **Condition:** Workers hold full model replicas.

- Reduces communication by frequency rather than size as in [[02 Concepts/Stack/Parallelism & Distributed Execution/Gradient Compression|Gradient Compression]]. **Condition:** Bandwidth between workers is scarce.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: periodic model averaging; DiLoCo-style training; low-communication training.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
