---
title: Decoding and Sampling Controls
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Decoding_Sampling_Structured_Output
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Decoding and sampling controls
taxonomy_id: mlsys.sampling-controls
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Decoding and Sampling Controls

Parameters and rules, such as greedy, temperature, top-k, and nucleus sampling, that determine how tokens are chosen from a model's distribution.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Decoding, Sampling & Structured Output Subject|Decoding, Sampling & Structured Output]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Temperature shapes [[02 Concepts/Lifecycle/Model Evaluation & Testing/Pass@k|Pass@k]]. **Condition:** For a fixed model, task set, sampling procedure, and correctness criterion; the preferred temperature depends on the evaluation setting and sample budget.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: temperature; top-k sampling; nucleus sampling; top-p; min-p; repetition penalty; greedy decoding.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
