---
title: Feed Forward Block
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Feed-forward block
taxonomy_id: mlsys.feed-forward-block
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Feed Forward Block

The per-position subnetwork of learned projections and a nonlinearity paired with attention in each Transformer block, which in most architectures holds the largest share of a dense model's parameters, executes as large matrix multiplications, and is the sublayer that mixture-of-experts routing replaces.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the position-wise sublayer paired with attention in each block of [[02 Concepts/Foundations/Models & Architectures/Transformer|Transformer]]. **Condition:** In standard Transformer blocks, where each block alternates an attention sublayer and a feed-forward sublayer under residual connections.

- Executes its projections as [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Matrix Multiplication|Matrix Multiplication]]. **Condition:** The projections are dense GEMMs over all tokens, so in dense Transformers they dominate parameter count and prefill compute; gated variants add a third projection.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: FFN; MLP block; position-wise feed-forward network; feed-forward sublayer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
