---
title: Device Initiated Communication
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Collective_Communication
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Device-initiated communication
taxonomy_id: mlsys.device-initiated-communication
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Device Initiated Communication

Communication in which kernels on the accelerator issue and synchronize inter-device transfers themselves, without a host call per exchange, allowing fine-grained fusion of compute and communication at the cost of explicit ordering and completion handling.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Collective Communication Subject|Collective Communication]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses direct remote-memory transport [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Remote Direct Memory Access|Remote Direct Memory Access]]. **Condition:** For inter-node transfers over a device-initiated RDMA path.

- Reduces per-exchange host orchestration [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** When device-side communication replaces repeated host launches or host-issued communication operations.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GPU-initiated communication; accelerator-initiated communication.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
