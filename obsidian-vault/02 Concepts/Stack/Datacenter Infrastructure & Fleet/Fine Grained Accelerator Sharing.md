---
title: Fine Grained Accelerator Sharing
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Capacity_Planning_Multi_Tenancy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Fine-grained accelerator sharing
taxonomy_id: mlsys.fine-grained-accelerator-sharing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Fine Grained Accelerator Sharing

Scheduling co-located workloads on one accelerator in small units of a kernel, so latency-sensitive work can preempt background work quickly and interference stays bounded.

## Browsing Home

[[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Capacity Planning & Multi Tenancy Subject|Capacity Planning & Multi Tenancy]] → [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Infrastructure & Fleet Index|Datacenter Infrastructure & Fleet]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the sub-kernel scheduling form of [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Accelerator Sharing and Partitioning|Accelerator Sharing and Partitioning]]. **Condition:** When co-located workloads need tighter latency isolation than whole-kernel time slicing gives and more flexibility than fixed hardware partitions.

- Bounds the slowdown of latency-sensitive work from [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Performance Interference|Performance Interference]]. **Condition:** When the scheduler can preempt or throttle best-effort kernels within a kernel's execution.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sub-kernel GPU sharing; kernel-slice preemption.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
