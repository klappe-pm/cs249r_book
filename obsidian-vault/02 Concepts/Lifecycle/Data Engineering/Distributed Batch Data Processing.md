---
title: Distributed Batch Data Processing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Distributed batch data processing
taxonomy_id: mlsys.batch-data-processing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Distributed Batch Data Processing

Transforming bounded datasets with dataflow engines that partition records across workers, shuffle between stages, and re-execute failed tasks, for large-scale preprocessing and feature generation.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Executes at corpus scale [[02 Concepts/Lifecycle/Data Engineering/Dataset Deduplication|Dataset Deduplication]]. **Condition:** Applies when the corpus exceeds one machine, so near-duplicate detection is partitioned and shuffled across workers.

- Executes [[02 Concepts/Lifecycle/Data Engineering/Feature Backfill|Feature Backfill]]. **Condition:** Backfills over long histories run as bounded batch jobs whose logic must match the serving feature definition.

- Prunes reads through [[02 Concepts/Lifecycle/Data Engineering/Dataset Storage Layout|Dataset Storage Layout]]. **Condition:** Holds for columnar, partitioned layouts with statistics.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MapReduce; Spark-style dataflow.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
