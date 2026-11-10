---
title: Python GIL and Host Language Concurrency
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Python GIL and host-language concurrency
taxonomy_id: mlsys.python-gil
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Python GIL and Host Language Concurrency

In GIL-enabled CPython, the global interpreter lock serializes Python bytecode across threads, so ML host code achieves concurrency through native kernels that release the lock, multiple processes, or asynchronous I/O.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Serializes and adds to [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** Several Python threads issue work concurrently.

- Pushes preprocessing into worker processes in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Side Data Loading|Host Side Data Loading]]. **Condition:** Preprocessing runs in Python, so loaders use worker processes rather than threads.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: GIL; global interpreter lock.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
