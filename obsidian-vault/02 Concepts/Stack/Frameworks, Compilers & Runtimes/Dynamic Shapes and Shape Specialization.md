---
title: Dynamic Shapes and Shape Specialization
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Dynamic shapes and shape specialization
taxonomy_id: mlsys.dynamic-shapes
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Dynamic Shapes and Shape Specialization

Handling inputs whose tensor dimensions vary across calls by specializing compiled code per shape, padding into buckets, or compiling with symbolic dimensions.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a concern within [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Compilation|Graph Compilation]]. **Condition:** Input dimensions vary across calls to a compiled function.

- Restricts reuse of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Captured Graph Replay|Captured Graph Replay]]. **Condition:** Captured graphs are valid only for the shapes recorded at capture time.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: symbolic shapes; shape bucketing; shape recompilation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
