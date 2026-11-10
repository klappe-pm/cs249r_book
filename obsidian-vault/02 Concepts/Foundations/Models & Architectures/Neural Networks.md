---
title: Neural Networks
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Families
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Neural networks
taxonomy_id: mlsys.neural-network
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Neural Networks

Parameterized compositions of differentiable operations used to learn representations and predictions.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Families Subject|Model Families]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is trained using [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Automatic Differentiation|Automatic Differentiation]]. **Condition:** For gradient-based learning with supported differentiable objectives and derivative rules.

- Determines the contents of [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** Execution requires compatible parameters, operators, and configuration. Training state can include additional data not needed for inference.

- Spends most compute in [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** Dense and attention layers dominate; small or irregular layers can be bound by other operations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
