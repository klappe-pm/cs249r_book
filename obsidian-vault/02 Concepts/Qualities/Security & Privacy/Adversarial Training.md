---
title: Adversarial Training
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Threat_Models_Adversarial_Attacks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Adversarial training
taxonomy_id: mlsys.adversarial-training
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Adversarial Training

Training on adversarially perturbed inputs generated during training to increase robustness within a specified perturbation set.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Threat Models & Adversarial Attacks Subject|Threat Models & Adversarial Attacks]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Reduces success of [[02 Concepts/Qualities/Security & Privacy/Adversarial Evasion|Adversarial Evasion]]. **Condition:** Only within the perturbation set and threat model used to generate training adversaries.

- Trades off against clean [[02 Concepts/Lifecycle/Model Evaluation & Testing/Generalization|Generalization]]. **Condition:** Robust training typically costs clean accuracy and multiplies training compute by the cost of generating adversaries.

- Increases [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Time to Train|Time to Train]]. **Condition:** Each training step runs an inner attack, multiplying compute by roughly the number of attack steps.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
