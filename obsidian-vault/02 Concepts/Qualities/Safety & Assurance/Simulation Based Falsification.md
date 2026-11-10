---
title: Simulation Based Falsification
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Safety_Verification_Validation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Simulation-based falsification
taxonomy_id: mlsys.falsification
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Simulation Based Falsification

Searching scenario parameters, often guided by temporal-logic robustness, to find counterexamples that violate a safety specification.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Safety Verification & Validation Subject|Safety Verification & Validation]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Searches the parameter space of [[02 Concepts/Qualities/Safety & Assurance/Scenario Based Testing|Scenario Based Testing]]. **Condition:** Found counterexamples are only as realistic as the scenario model and simulator.

- Enables [[02 Concepts/Qualities/Safety & Assurance/Rare Event Safety Validation|Rare Event Safety Validation]]. **Condition:** Failure regions found by falsification can seed importance sampling for failure-probability estimates.

- Is an alternative to [[02 Concepts/Qualities/Safety & Assurance/Formal Verification|Formal Verification]]. **Condition:** For systems too complex for formal proof, where searching for counterexamples replaces proving their absence.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
