---
title: Threat Modeling
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Threat_Models_Adversarial_Attacks
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Threat modeling
taxonomy_id: mlsys.threat-model
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Threat Modeling

Specifying adversaries, assets, interfaces, capabilities, and failure consequences.

## Browsing Home

[[02 Concepts/Qualities/Security & Privacy/Threat Models & Adversarial Attacks Subject|Threat Models & Adversarial Attacks]] → [[02 Concepts/Qualities/Security & Privacy/Security & Privacy Index|Security & Privacy]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Scopes the attack surfaces considered for [[02 Concepts/Qualities/Security & Privacy/Data Poisoning|Data Poisoning]]. **Condition:** The adversary's ability to modify training inputs or signals must be specified.

- Scopes the attack surfaces considered for [[02 Concepts/Qualities/Security & Privacy/Adversarial Evasion|Adversarial Evasion]]. **Condition:** The adversary's knowledge, perturbations, and target behavior must be specified.

- Selects attack cases for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Robustness Evaluation|Robustness Evaluation]]. **Condition:** Tests exercise a declared adversary and interface; passing selected attacks does not establish universal robustness.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
