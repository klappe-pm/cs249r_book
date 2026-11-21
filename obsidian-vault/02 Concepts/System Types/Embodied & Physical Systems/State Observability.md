---
title: State Observability
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: State observability
taxonomy_id: mlsys.state-observability
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# State Observability

Whether distinct internal states can be distinguished through the available observations and model.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/18 Engineering Physical AI/V4-18.04 The Epistemic Frontier#^sec-frontier-observational-indistinguishability-sub|V4-18.04 The Epistemic Frontier]] — Observational indistinguishability. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/18_frontier/18_frontier.qmd#L902).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Limits [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** A low reported covariance does not by itself establish that the state is distinguishable.

- Bounds drift correction in [[02 Concepts/System Types/Embodied & Physical Systems/Simultaneous Localization and Mapping|Simultaneous Localization and Mapping]]. **Condition:** Absolute pose and heading are unobservable from relative measurements alone, so drift persists without loop closure or external references.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
