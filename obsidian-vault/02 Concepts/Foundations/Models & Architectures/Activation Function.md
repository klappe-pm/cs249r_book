---
title: Activation Function
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Activation function
taxonomy_id: mlsys.activation-function
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Activation Function

The elementwise or gated nonlinearity applied between a network's linear layers, whose choice sets whether activations contain exact zeros, whether a block needs an extra gating projection, and how cheaply the operation fuses into the preceding matrix multiply.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the nonlinearity between the linear layers of [[02 Concepts/Foundations/Models & Architectures/Neural Networks|Neural Networks]]. **Condition:** When the architecture applies pointwise or gated nonlinearities between affine layers, as nearly all do; without them stacked linear layers collapse to one.

- Produces the exact zeros exploited by [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Contextual Activation Sparsity|Contextual Activation Sparsity]]. **Condition:** When the nonlinearity is ReLU-like; smooth activations such as GELU or SwiGLU need thresholding or prediction to find skippable units.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: nonlinearity; ReLU; GELU; SwiGLU; gated linear unit.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
