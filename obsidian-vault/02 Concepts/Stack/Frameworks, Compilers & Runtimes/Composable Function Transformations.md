---
title: Composable Function Transformations
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Composable function transformations
taxonomy_id: mlsys.function-transformations
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Composable Function Transformations

Higher-order operations that map pure array functions to new functions, such as differentiation, vectorization, compilation, and sharding, and compose subject to each transformation's input, output, and tracing contract.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Exposes as a transform [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Automatic Differentiation|Automatic Differentiation]]. **Condition:** Holds when programs are pure functions so differentiation composes with vectorization and compilation.

- Relies on [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Tracing|Graph Tracing]]. **Condition:** For transformations implemented over a traced intermediate representation, such as JAX transformations; this is not a requirement for every transformation implementation.

- Exposes as a transform [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Compilation|Graph Compilation]]. **Condition:** Pure array functions are traced and handed to an XLA-style compiler.

- Realizes through a composable grad transformation [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Differentiable Programming|Differentiable Programming]]. **Condition:** Programs written as pure array functions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: grad/vmap/jit; functional transformations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
