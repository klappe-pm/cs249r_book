---
title: Graph Compilation
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Graph compilation
taxonomy_id: mlsys.compilation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Graph Compilation

Transforming a model or execution graph into an executable representation.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can apply [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Only when semantics and execution dependencies permit combination.

- Takes as input a [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Computation Graph|Computation Graph]]. **Condition:** The compiler needs a captured graph rather than one operation at a time.

- Lowers through [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compiler IR|ML Compiler IR]]. **Condition:** Graph, tensor, and loop-level representations carry the program between passes.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: compilation breakeven; compile-time amortization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
