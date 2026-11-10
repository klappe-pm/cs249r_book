---
title: Control Barrier Function
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Control barrier function
taxonomy_id: mlsys.control-barrier-function
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Control Barrier Function

A function whose sign defines a safe set and whose derivative condition yields input constraints that keep the system state inside that set.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Provides the certificate for [[02 Concepts/Qualities/Safety & Assurance/Safety Filter|Safety Filter]]. **Condition:** Guarantees depend on an accurate dynamics model, bounded disturbance, and a feasible filtering problem at each tick.

- Requires a model of [[02 Concepts/System Types/Embodied & Physical Systems/Physical Dynamics|Physical Dynamics]]. **Condition:** The barrier condition holds only under the modeled dynamics and bounded disturbance.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: CBF.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
