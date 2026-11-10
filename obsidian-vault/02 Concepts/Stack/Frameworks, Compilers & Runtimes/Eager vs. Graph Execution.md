---
title: Eager vs. Graph Execution
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Eager vs. graph execution
taxonomy_id: mlsys.eager-execution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Eager vs. Graph Execution

The choice between running each operation as the host program issues it and building a whole graph first for later optimization and execution.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Incurs per-operation [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Host Dispatch Overhead|Host Dispatch Overhead]]. **Condition:** Each operation is launched separately from the host program.

- Forecloses cross-operation [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Each operation is launched as the host issues it, so no compiler sees neighboring operations.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: define-by-run.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
