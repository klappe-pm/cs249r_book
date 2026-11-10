---
title: Input Prefetching
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Data_Loading_Input_Pipelines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Input prefetching
taxonomy_id: mlsys.input-prefetching
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Input Prefetching

Preparing upcoming batches in background workers and buffers while the accelerator processes the current batch, overlapping input delivery with computation.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Data Loading & Input Pipelines Subject|Data Loading & Input Pipelines]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.05 The Data Pipeline Equation#^sec-storage-pipelining|V2-04.05 The Data Pipeline Equation]] — Prefetching. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/04_data_storage.qmd#L2522).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a stage within [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** Batches are prepared ahead of consumption.

- Raises accelerator utilization by hiding input latency behind [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Input preparation would otherwise stall compute.

- Overlaps loading with compute in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Side Data Loading|Host Side Data Loading]]. **Condition:** Worker processes prepare batches ahead of the training step.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data prefetching; prefetch buffer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
