---
title: Normalization Layers
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Normalization layers
taxonomy_id: mlsys.normalization-layer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Normalization Layers

Layers that rescale activations using batch, layer, or root-mean-square statistics to stabilize and speed training of deep networks.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Improves [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Stability|Numerical Stability]]. **Condition:** Activation statistics would otherwise drift with depth or batch composition.

- Mitigates [[02 Concepts/Lifecycle/Training & Adaptation/Training Instability|Training Instability]]. **Condition:** Deep networks whose activation scales would otherwise drift with depth or batch composition.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: BatchNorm; LayerNorm; RMSNorm.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
