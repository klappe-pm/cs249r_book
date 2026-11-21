---
title: Rule Based Graph Rewriting
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Compilers_Kernel_Optimization
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Rule-based graph rewriting
taxonomy_id: mlsys.rule-based-graph-rewriting
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Rule Based Graph Rewriting

Applying hand-written semantics-preserving transformations to a computation graph, such as constant folding, dead-code elimination, operator substitution, and algebraic simplification.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Compilers & Kernel Optimization Subject|ML Compilers & Kernel Optimization]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a pass family within [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Graph Compilation|Graph Compilation]]. **Condition:** The compiler applies pattern-based passes before lowering.

- Is the hand-written counterpart to [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Tensor Graph Superoptimization|Tensor Graph Superoptimization]]. **Condition:** Both seek semantics-preserving graph transformations; one uses fixed rules, the other searched rewrites.

- Exposes fusible patterns for [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Kernel Fusion|Kernel Fusion]]. **Condition:** Canonicalization places compatible operators adjacent in the graph.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: constant folding; algebraic simplification; operator substitution; graph optimization passes; graph rewriting.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
