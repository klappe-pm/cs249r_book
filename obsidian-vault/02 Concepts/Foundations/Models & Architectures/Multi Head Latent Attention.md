---
title: Multi Head Latent Attention
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Long_Context_Efficient_Sequence_Models
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Multi-head latent attention
taxonomy_id: mlsys.multi-head-latent-attention
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Multi Head Latent Attention

Attention that caches one low-rank latent vector per token in place of per-head keys and values, reconstructing them or absorbing the up-projections into the query and output weights, which shrinks the KV cache and decode memory traffic.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Long Context & Efficient Sequence Models Subject|Long Context & Efficient Sequence Models]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Shrinks the per-token footprint of [[02 Concepts/Lifecycle/Deployment & Serving/KV Cache|KV Cache]]. **Condition:** When the latent and any decoupled positional components are smaller than the per-head keys and values they replace.

- Is an alternative KV-size lever to [[02 Concepts/Foundations/Models & Architectures/Grouped Query Attention|Grouped Query Attention]]. **Condition:** When an architecture chooses how to reduce cached attention state at design time.

- Is a variant of [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** When keys and values are produced from a shared compressed representation.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MLA; latent KV attention.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
