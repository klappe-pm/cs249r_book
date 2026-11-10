---
title: State Space Sequence Model
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: State-space sequence model
taxonomy_id: mlsys.state-space-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# State Space Sequence Model

Sequence models built on discretized linear state-space recurrences, trainable in parallel and run with constant-size state per step at inference.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Updates its state through [[02 Concepts/Foundations/Models & Architectures/Recurrent Computation|Recurrent Computation]]. **Condition:** When the state update runs step by step at inference.

- Is an alternative to [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** Both serve as the sequence-mixing layer; state-space layers trade exact long-range lookup for linear cost and fixed state.

- Eliminates the growing [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** Inference carries a constant-size state per layer instead of keys and values for every prior token.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SSM; Mamba; S4.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
