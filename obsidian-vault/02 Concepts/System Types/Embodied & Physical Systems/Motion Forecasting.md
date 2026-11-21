---
title: Motion Forecasting
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Motion forecasting
taxonomy_id: mlsys.motion-forecasting
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Motion Forecasting

Predicting the future trajectories of other moving agents, usually as several weighted hypotheses, from their tracked history and the map, so a planner can avoid where they will be rather than where they are.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Takes agent histories from [[02 Concepts/System Types/Embodied & Physical Systems/Multi Object Tracking|Multi Object Tracking]]. **Condition:** When surrounding agents are tracked with persistent identities over time.

- Conditions predicted trajectories on the lanes and free space in the [[02 Concepts/System Types/Embodied & Physical Systems/mAP Representation|mAP Representation]]. **Condition:** When a prior or online map supplies road or room structure.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: behavior prediction; trajectory prediction; agent motion prediction.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
