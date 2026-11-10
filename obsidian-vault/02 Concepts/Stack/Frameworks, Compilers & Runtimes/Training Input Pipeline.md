---
title: Training Input Pipeline
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Data_Loading_Input_Pipelines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Training input pipeline
taxonomy_id: mlsys.input-pipeline
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Training Input Pipeline

The read, decode, transform, shuffle, and prefetch stages that deliver batches to accelerators; when slower than compute, they cause data stalls.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Data Loading & Input Pipelines Subject|Data Loading & Input Pipelines]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/01 Foundations/04 Data Engineering/V1-04.11 Storage and Delivery#^sec-data-engineering-ml-storage-requirements-performance-1b0d|V1-04.11 Storage and Delivery]] — Input pipeline. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/04_data_engineering/04_data_engineering.qmd#L4266).

- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.05 The Data Pipeline Equation#^sec-storage-pipeline-equation|V2-04.05 The Data Pipeline Equation]] — Input pipeline. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/04_data_storage/04_data_storage.qmd#L2185).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reads through the nearer tiers of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage Tiering and Caching|Storage Tiering and Caching]]. **Condition:** Working sets fit in nearer tiers or are prefetched.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data echoing.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
