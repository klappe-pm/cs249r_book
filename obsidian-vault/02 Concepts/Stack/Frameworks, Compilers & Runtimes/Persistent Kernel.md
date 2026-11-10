---
title: Persistent Kernel
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Persistent kernel
taxonomy_id: mlsys.persistent-kernel
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Persistent Kernel

A long-running kernel that stays resident on the device and executes many operators, or a whole forward pass, from an in-kernel work queue.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Removes per-operator launch overhead from [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** Small-batch, latency-bound workloads made of many short kernels.

- Is an alternative way to remove launch overhead to [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Captured Graph Replay|Captured Graph Replay]]. **Condition:** Persistent kernels also overlap work across operator boundaries inside one launch.

- Keeps one kernel resident rather than merging operations as in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Both reduce host launches for repeated work.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: megakernel; mega-kernel; persistent megakernel.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
