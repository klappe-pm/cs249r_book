---
title: Simplex Architecture
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Simplex architecture
taxonomy_id: mlsys.simplex-architecture
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Simplex Architecture

Pairing an unverified high-performance controller with a verified safety controller and a decision module that switches to the safety controller before safety is lost.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]. **Condition:** Switching must occur while the verified controller can still recover the state.

- Falls back toward [[02 Concepts/Qualities/Safety & Assurance/Minimal Risk Condition|Minimal Risk Condition]]. **Condition:** Holds when the safety controller's goal is to reach a defined minimal-risk state rather than continue the mission.

- Requires [[02 Concepts/System Types/Embodied & Physical Systems/Mixed Criticality Partitioning|Mixed Criticality Partitioning]]. **Condition:** The verified safety controller and decision module must keep their timing even when the complex controller overruns.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
