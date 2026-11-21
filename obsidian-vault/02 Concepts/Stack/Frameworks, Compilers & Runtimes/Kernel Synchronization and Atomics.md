---
title: Kernel Synchronization and Atomics
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Kernel_GPU_Programming_Model
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Kernel synchronization and atomics
taxonomy_id: mlsys.kernel-synchronization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Kernel Synchronization and Atomics

The barriers, memory fences, and atomic read-modify-write operations through which threads of a kernel coordinate access to shared data, where barrier stalls and contended atomics serialize work that the thread hierarchy otherwise runs in parallel.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel & GPU Programming Model Subject|Kernel & GPU Programming Model]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Coordinates threads at the scopes defined by [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Thread Hierarchy|Thread Hierarchy]]. **Condition:** When threads of a block or warp share on-chip memory and must order their accesses.

- Introduces order-dependent floating-point results through contended [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Nondeterminism|Numerical Nondeterminism]]. **Condition:** When partial sums are combined with atomic adds whose completion order varies from run to run.

- Serializes contended updates, bounding achieved [[02 Concepts/Stack/Hardware & Accelerators/Compute Throughput|Compute Throughput]]. **Condition:** When many threads atomically update the same address, as in histogram, scatter-add, or gradient-aggregation kernels.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: thread-block barrier; __syncthreads; atomic operations; atomic reduction; warp synchronization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
