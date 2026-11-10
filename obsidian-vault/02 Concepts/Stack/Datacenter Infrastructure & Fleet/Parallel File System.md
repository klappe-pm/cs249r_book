---
title: Parallel File System
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Storage_Data_Delivery
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Parallel file system
taxonomy_id: mlsys.parallel-file-system
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Parallel File System

A distributed file system that stripes data across many storage servers to deliver aggregate bandwidth to many concurrent clients.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Storage & Data Delivery Subject|Storage & Data Delivery]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Supplies aggregate read bandwidth for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Training Input Pipeline|Training Input Pipeline]]. **Condition:** Many workers read training data concurrently from shared storage.

- Is an alternative to [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Object Storage|Object Storage]]. **Condition:** Both serve shared training data and checkpoints; file systems offer lower latency, object stores cheaper scalable capacity.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Lustre; GPFS.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
