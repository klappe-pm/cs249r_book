---
title: Mechanistic Interpretability
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Explainability_Documentation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Mechanistic interpretability
taxonomy_id: mlsys.mechanistic-interpretability
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Mechanistic Interpretability

Investigating how a network's internal representations and computations produce behavior through analysis and interventions, to test explanations at the level of internal components.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Explainability & Documentation Subject|Explainability & Documentation]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Explains internal computation rather than input contributions, unlike [[02 Concepts/Qualities/Responsible AI/Feature Attribution|Feature Attribution]]. **Condition:** Both aim at understanding a decision; attribution scores inputs, mechanistic methods inspect representations and need model access.

- Fits linear probes from [[02 Concepts/Foundations/Models & Architectures/Linear Models|Linear Models]]. **Condition:** For probing, where a linear classifier on activations tests whether a property is linearly represented.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: probing classifiers; activation patching; sparse autoencoder features; circuit analysis.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
