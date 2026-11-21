---
title: Neural Network Verification
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Safety_Verification_Validation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Neural network verification
taxonomy_id: mlsys.neural-network-verification
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Neural Network Verification

Proving or refuting input-output properties of a trained network over a bounded input region, such as local robustness, using exact or bound-propagation methods.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Safety Verification & Validation Subject|Safety Verification & Validation]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Specializes [[02 Concepts/Qualities/Safety & Assurance/Formal Verification|Formal Verification]]. **Condition:** Exact methods scale poorly with network size; bound-propagation methods trade completeness for scale.

- Certifies absence, within a bounded region, of [[02 Concepts/Qualities/Security & Privacy/Adversarial Evasion|Adversarial Evasion]]. **Condition:** Holds only for the specified perturbation set, typically a norm ball around given inputs.

- Is a certified alternative to empirical [[02 Concepts/Lifecycle/Model Evaluation & Testing/Robustness Evaluation|Robustness Evaluation]]. **Condition:** For properties over input regions small enough for the verifier to scale.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
