---
title: Data Warehouse and Lakehouse
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Data_Pipelines_Storage_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Data warehouse and lakehouse
taxonomy_id: mlsys.lakehouse
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Data Warehouse and Lakehouse

Analytical stores of governed tables queried with SQL; a lakehouse adds transactional table formats over open files in object storage.

## Browsing Home

[[02 Concepts/Lifecycle/Data Engineering/Data Pipelines & Storage Formats Subject|Data Pipelines & Storage Formats]] → [[02 Concepts/Lifecycle/Data Engineering/Data Engineering Index|Data Engineering]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Stores table files in [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Object Storage|Object Storage]]. **Condition:** Lakehouse designs over open file formats.

- Provides snapshot time travel for [[02 Concepts/Lifecycle/Data Engineering/Dataset Versioning|Dataset Versioning]]. **Condition:** Table formats that retain prior snapshots.

- Stores data in columnar layouts such as [[02 Concepts/Lifecycle/Data Engineering/Dataset Storage Layout|Dataset Storage Layout]]. **Condition:** Open columnar formats such as Parquet.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data warehouse; data lake; lakehouse.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
