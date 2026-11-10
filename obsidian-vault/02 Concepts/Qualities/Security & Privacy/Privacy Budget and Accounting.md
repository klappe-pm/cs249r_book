---
title: Privacy Budget and Accounting
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Privacy_Leakage_Differential_Privacy
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Privacy budget and accounting
taxonomy_id: mlsys.privacy-budget
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Privacy Budget and Accounting

A declared bound on cumulative privacy loss across releases involving overlapping individuals, tracked through composition accounting to constrain further releases.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Privacy Leakage & Differential Privacy Subject|Privacy Leakage & Differential Privacy]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the accounting side of [[02 Concepts/Qualities/Security & Privacy/Differential Privacy|Differential Privacy]]. **Condition:** When several releases or training steps on the same data must be composed into one guarantee.

- Caps how many times private data can be reused by [[02 Concepts/Lifecycle/MLOps & Operations/Retraining|Retraining]]. **Condition:** When each retraining run spends from a fixed budget rather than resetting it.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: privacy accountant; epsilon-delta budget; privacy loss composition; moments accountant; RDP accountant.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
