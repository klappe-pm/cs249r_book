---
title: Differential Privacy
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Differential privacy
taxonomy_id: mlsys.differential-privacy
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Differential Privacy

A parameterized bound on changes in output distributions under a specified neighboring-dataset relation.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.10 Differential Privacy#^sec-security-privacy-differential-privacy-8c2b|V2-13.10 Differential Privacy]] — Differential privacy. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/13_security_privacy/13_security_privacy.qmd#L3817).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides a formal guarantee for [[02 Concepts/Qualities/Security & Privacy/Privacy Requirements|Privacy Requirements]]. **Condition:** The guarantee bounds output-distribution change under a declared neighboring relation and accounting parameters; it does not establish every privacy requirement.

- Bounds the advantage of [[02 Concepts/Qualities/Security & Privacy/Membership Inference|Membership Inference]]. **Condition:** At the unit defined by the neighboring-dataset relation; the bound weakens as epsilon and delta grow.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DP.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
