---
title: Tensor Graph Superoptimization
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tensor graph superoptimization
taxonomy_id: mlsys.graph-superoptimization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tensor Graph Superoptimization

Automatically generating and verifying semantics-preserving rewrites of tensor computation graphs or kernels, then searching the rewritten space under a cost model.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an optimization stage within [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Compilation|Graph Compilation]]. **Condition:** Rewrites are verified equivalent before code generation.

- Searches rewrites expressed in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compiler IR|ML Compiler IR]]. **Condition:** Graph- or kernel-level IR with defined operator semantics.

- Discovers new opportunities for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Search spans kernel and thread-block levels as well as the graph level.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: graph substitution; TASO-style superoptimization.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
