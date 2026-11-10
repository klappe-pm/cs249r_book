---
title: Operational Design Domain
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hazard_Analysis_Operating_Domains
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Operational design domain
taxonomy_id: mlsys.operating-domain
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Operational Design Domain

The declared set of conditions, covering environment, inputs, actors, and system state, within which a system is designed to perform and outside which its safety claims and evidence do not apply.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Hazard Analysis & Operating Domains Subject|Hazard Analysis & Operating Domains]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.08 Collection Policy Coverage#^sec-data-policy-coverage|V4-05.08 Collection Policy Coverage]] — Operational design domain. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/05_data/05_data.qmd#L1132).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Bounds the claims in [[02 Concepts/Qualities/Safety & Assurance/Safety Case|Safety Case]]. **Condition:** Evidence must match the intended operating conditions and configuration.

- Scopes the relevant conditions for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Robustness Evaluation|Robustness Evaluation]]. **Condition:** The intended domain identifies relevant stresses and coupled corners, but finite selected tests do not exhaust continuous operating conditions.

- Scopes the scenario catalog of [[02 Concepts/Qualities/Safety & Assurance/Scenario Based Testing|Scenario Based Testing]]. **Condition:** Scenarios and parameter ranges are drawn from the declared operational design domain.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: ODD.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
