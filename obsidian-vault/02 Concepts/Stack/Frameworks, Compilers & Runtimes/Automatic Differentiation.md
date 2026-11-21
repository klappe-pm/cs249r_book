---
title: Automatic Differentiation
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/ML_Frameworks_Programming_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Automatic differentiation
taxonomy_id: mlsys.autodiff
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Automatic Differentiation

Computing derivatives by composing local derivative rules through an execution graph.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/ML Frameworks & Programming Models Subject|ML Frameworks & Programming Models]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.05 Differentiation Automatic Gradient Computation#^sec-ml-frameworks-differentiation-problem-8b8a|V1-07.05 Differentiation Automatic Gradient Computation]] — Reverse-mode autodiff. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/07_frameworks/07_frameworks.qmd#L2149).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Produces the gradients consumed by [[02 Concepts/Lifecycle/Training & Adaptation/Optimization Algorithm|Optimization Algorithm]]. **Condition:** Optimizer state and update rules are separate from differentiation.

- Traverses [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Computation Graph|Computation Graph]]. **Condition:** Derivatives are composed in reverse over recorded operations.

- Retains forward activations, increasing [[02 Concepts/Foundations/Workloads & Requirements/Memory Footprint|Memory Footprint]]. **Condition:** Reverse-mode differentiation stores intermediates from the forward pass for use in the backward pass.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
