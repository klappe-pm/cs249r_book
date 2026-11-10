---
title: Model Predictive Control
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Motion_Planning_Control
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model predictive control
taxonomy_id: mlsys.model-predictive-control
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Predictive Control

Repeatedly solving a finite-horizon constrained optimal control problem from the current state and applying only the first input.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Motion Planning & Control Subject|Motion Planning & Control]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Can use as its prediction model a [[02 Concepts/System Types/Embodied & Physical Systems/Learned World Model|Learned World Model]]. **Condition:** Plans exploit model errors, so performance depends on accuracy in the regions the optimizer visits.

- Requires a solver WCET within its control period, i.e. a [[02 Concepts/System Types/Embodied & Physical Systems/Worst Case Execution Time|Worst Case Execution Time]]. **Condition:** Holds when each optimization must finish within the control period; warm starts and horizon length trade quality for time.

- Is a form of [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Control|Feedback Control]]. **Condition:** Re-solving from each new state estimate closes the loop.

- Encodes as input constraints [[02 Concepts/System Types/Embodied & Physical Systems/Actuator Limits|Actuator Limits]]. **Condition:** Limits are known and modeled.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: MPC (control).

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
