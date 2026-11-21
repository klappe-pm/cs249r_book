---
title: Recursive State Filtering
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/State_Estimation_Localization_Mapping
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Recursive state filtering
taxonomy_id: mlsys.recursive-filtering
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Recursive State Filtering

Updating a state estimate and its uncertainty by alternating model-based prediction with measurement correction at each step.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/State Estimation, Localization & Mapping Subject|State Estimation, Localization & Mapping]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/09 Spatial Memory/V4-09.03 Estimating State from Dated Measurements#^sec-perception-state-estimation|V4-09.03 Estimating State from Dated Measurements]] — Belief state. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/09_memory/09_memory.qmd#L108).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** Kalman-family filters assume approximately Gaussian, well-modeled noise; violations make reported covariance overconfident.

- Predicts state with a model of [[02 Concepts/System Types/Embodied & Physical Systems/Physical Dynamics|Physical Dynamics]]. **Condition:** The prediction step propagates the estimate through modeled dynamics between measurements.

- Propagates the predicted state in the prediction step with [[02 Concepts/System Types/Embodied & Physical Systems/Odometry and Dead Reckoning|Odometry and Dead Reckoning]]. **Condition:** When odometry supplies the control input to a Kalman-family or particle filter.

- Applies each measurement at its [[02 Concepts/System Types/Embodied & Physical Systems/Capture Timing and Rolling Shutter|Capture Timing and Rolling Shutter]]. **Condition:** When measurements arrive out of order or late, the filter must correct at the capture epoch rather than at arrival.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Kalman filter; EKF; particle filter; filter consistency; NEES; NIS.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
