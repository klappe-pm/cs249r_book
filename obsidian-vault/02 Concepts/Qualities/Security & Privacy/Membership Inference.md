---
title: Membership Inference
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Membership inference
taxonomy_id: mlsys.membership-inference
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Membership Inference

Inferring whether a specific record was in a model's training data from the model's outputs or parameters.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Measures [[02 Concepts/Qualities/Security & Privacy/Privacy Leakage|Privacy Leakage]]. **Condition:** When attack advantage over a baseline is used as an empirical estimate of record-level leakage.

- Audits whether removed records still influence a model after [[02 Concepts/Qualities/Security & Privacy/Machine Unlearning|Machine Unlearning]]. **Condition:** When attack advantage on the forgotten records, compared with a model retrained without them, is used as the empirical test of forgetting.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
