---
title: Dataset Shuffling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Data_Loading_Input_Pipelines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dataset shuffling
taxonomy_id: mlsys.dataset-shuffling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dataset Shuffling

Randomizing the order in which training examples are visited, by a full permutation or an approximate buffered shuffle over sharded files, trading the randomness that stochastic optimization assumes against the sequential reads that storage delivers cheaply.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Data Loading & Input Pipelines Subject|Data Loading & Input Pipelines]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the ordering stage of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** When examples are read in a randomized order rather than in stored order.

- Shuffles shards, then records within a buffer, from [[02 Concepts/Lifecycle/Data Engineering/Sharded Streaming Dataset Format|Sharded Streaming Dataset Format]]. **Condition:** When the corpus is stored as sharded files so a two-level shuffle approximates a global permutation.

- Breaks, unless its seed and shard order are recorded, [[02 Concepts/Lifecycle/MLOps & Operations/Experiment Reproducibility|Experiment Reproducibility]]. **Condition:** When runs must visit examples in the same order to be compared.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: shuffle buffer; global shuffle; epoch shuffle; shard shuffle.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
