---
title: Certified Robustness by Randomized Smoothing
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Threat_Models_Adversarial_Attacks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Certified robustness by randomized smoothing
taxonomy_id: mlsys.randomized-smoothing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Certified Robustness by Randomized Smoothing

Classifying many noise-perturbed copies of an input and taking the majority vote, which yields a provable radius within which no adversarial perturbation can change the prediction, at the cost of many inferences per input.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Threat Models & Adversarial Attacks Subject|Threat Models & Adversarial Attacks]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provably bounds [[02 Concepts/Qualities/Security & Privacy/Adversarial Evasion|Adversarial Evasion]]. **Condition:** Perturbations are within the certified radius.

- Trades inference cost for certified guarantees against [[02 Concepts/Qualities/Security & Privacy/Adversarial Training|Adversarial Training]]. **Condition:** A provable bound is required rather than empirical robustness.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: randomized smoothing; certified defense.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
