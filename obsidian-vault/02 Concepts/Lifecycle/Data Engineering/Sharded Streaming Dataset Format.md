---
title: Sharded Streaming Dataset Format
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sharded streaming dataset format
taxonomy_id: mlsys.streaming-dataset-format
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sharded Streaming Dataset Format

Organizing training examples into sequentially readable shard files so workers can stream records from remote storage with few small-object reads and bounded local staging.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the sequential-shard form of [[02 Concepts/Lifecycle/Data Engineering/Dataset Storage Layout|Dataset Storage Layout]]. **Condition:** When small records are packed into large files read sequentially from object storage or remote file systems.

- Streams contiguous byte ranges from [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Object Storage|Object Storage]]. **Condition:** When shards live in object storage rather than on a local file system.

- Supports sharded, resumable reads for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** When the loader also checkpoints shard assignment, record progress, and shuffle state.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: shard streaming; WebDataset-style shards.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
