---
title: Software Pipelining
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Software pipelining
taxonomy_id: mlsys.software-pipelining
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Software Pipelining

Scheduling independent operations from different loop iterations to overlap, such as loading the next tile while computing the current one, hiding latency at the cost of extra live state and buffering.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Issues the multi-stage copies it overlaps through [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Asynchronous Data Movement|Asynchronous Data Movement]]. **Condition:** On hardware with asynchronous copy support.

- Allocates two or more stage buffers in [[02 Concepts/Stack/Hardware & Accelerators/On Chip SRAM and Scratchpads|On Chip SRAM and Scratchpads]]. **Condition:** So loads for the next iteration do not overwrite operands the current iteration still reads.

- Overlaps the loads and compute of successive tiles from [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tiling|Tiling]]. **Condition:** When a kernel's loop iterates over tiles staged through on-chip memory.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: multi-stage pipelining; kernel double buffering.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
