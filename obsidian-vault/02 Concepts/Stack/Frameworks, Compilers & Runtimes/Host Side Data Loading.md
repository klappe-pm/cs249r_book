---
title: Host Side Data Loading
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Data_Loading_Input_Pipelines
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Host-side data loading
taxonomy_id: mlsys.host-data-loader
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Host Side Data Loading

Reading, decoding, augmenting, and collating examples on host CPU worker processes and staging batches in pinned memory so that a single machine's accelerators are not left waiting for input.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Data Loading & Input Pipelines Subject|Data Loading & Input Pipelines]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the single-machine stage of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** Examples are decoded and collated on the training host.

- Bounds accelerator utilization through [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Resource Utilization|Resource Utilization]]. **Condition:** Per-batch preprocessing time approaches the accelerator step time.

- Stages decoded batches in page-locked regions of [[02 Concepts/Stack/Hardware & Accelerators/Host Memory Tier|Host Memory Tier]]. **Condition:** When batches are copied to the device by DMA from pinned host buffers.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: data loader; DataLoader workers; pinned memory.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
