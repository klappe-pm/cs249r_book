---
title: Recurrent Computation
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Architecture_Building_Blocks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Recurrent computation
taxonomy_id: mlsys.recurrence
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Recurrent Computation

Computation that updates a hidden state step by step over a sequence, creating sequential dependencies that limit parallelism across time.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Architecture Building Blocks Subject|Architecture Building Blocks]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adds sequential dependence to [[02 Concepts/Foundations/Quantitative System Models/Serial Fraction|Serial Fraction]]. **Condition:** Each step depends on the previous hidden state, preventing parallelism across time steps.

- Is an alternative to [[02 Concepts/Foundations/Models & Architectures/Attention|Attention]]. **Condition:** Both mix information across sequence positions; recurrence keeps fixed state but serializes time, attention parallelizes but grows cost with length.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: RNN; LSTM.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
