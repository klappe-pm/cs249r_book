---
title: OS Memory Pressure and Paging
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Runtime_Execution_Dispatch
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: OS memory pressure and paging
taxonomy_id: mlsys.os-memory-pressure
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# OS Memory Pressure and Paging

How an operating system reclaims memory from a model process under pressure, by evicting file-backed pages, swapping or compressing memory, or killing the app, which shows up as page thrashing, latency spikes, or abrupt termination.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Runtime Execution & Dispatch Subject|Runtime Execution & Dispatch]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enforces [[02 Concepts/Stack/Hardware & Accelerators/On Device Memory Budget|On Device Memory Budget]]. **Condition:** The OS kills or pages out apps that exceed their memory limit.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: page thrashing; low-memory killer; memory reclamation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
