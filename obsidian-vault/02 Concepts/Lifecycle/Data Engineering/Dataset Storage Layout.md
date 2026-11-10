---
title: Dataset Storage Layout
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dataset storage layout
taxonomy_id: mlsys.dataset-storage-layout
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dataset Storage Layout

Organization of stored dataset records, columns, partitions, and metadata that determines which data an access reads or decodes.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Sets the I/O required by [[02 Concepts/Lifecycle/Data Engineering/Data Ingestion|Data Ingestion]]. **Condition:** Effects depend on access pattern, projection/filtering, encoding, storage medium, and caching; a layout does not guarantee higher throughput.

- Sets the read and decode cost of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** Record grouping, compression, and columnar layout decide how many bytes each batch must fetch and decode.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
