---
title: DP SGD
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: DP-SGD
taxonomy_id: mlsys.dp-sgd
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# DP SGD

Stochastic gradient descent with per-example gradient clipping and calibrated noise, with privacy loss tracked across steps by an accountant.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.10 Differential Privacy#^sec-security-privacy-privacy-budget-composition-edbe|V2-13.10 Differential Privacy]] — Privacy budget. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/13_security_privacy/13_security_privacy.qmd#L4067).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Qualities/Security & Privacy/Differential Privacy|Differential Privacy]]. **Condition:** When clipping norm, noise multiplier, sampling rate, and step count are tracked by a privacy accountant.

- Mitigates [[02 Concepts/Qualities/Security & Privacy/Model Inversion|Model Inversion]]. **Condition:** For reconstruction of individual training records; inference of population-level attributes is not bounded by DP.

- Bounds the per-example memorization behind [[02 Concepts/Qualities/Security & Privacy/Training Data Extraction|Training Data Extraction]]. **Condition:** When the privacy budget is small enough to limit each example's influence, at a utility cost.

- Tracks its noise multiplier, sampling rate, and step count through [[02 Concepts/Qualities/Security & Privacy/Privacy Budget and Accounting|Privacy Budget and Accounting]]. **Condition:** At every optimizer step; the accountant decides when training must stop.

- Adds per-example gradient computation and clipping to [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]. **Condition:** When per-example gradient and clipping overhead is not offset by fewer optimization steps or faster kernels at the same declared quality target.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: differentially private SGD.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
