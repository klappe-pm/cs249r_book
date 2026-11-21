---
title: Safety Filter
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Safety filter
taxonomy_id: mlsys.safety-filter
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Safety Filter

A runtime component that passes a proposed action when it is certified safe and otherwise replaces it with a minimally different safe action.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.08 The Minimal Intervention Principle and Optimization Filters#^sec-enforcement-minimal-intervention|V4-12.08 The Minimal Intervention Principle and Optimization Filters]] — Runtime safety filter. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/12_enforcement/12_enforcement.qmd#L1603).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Implements [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]. **Condition:** The filter must run independently of, and with authority over, the component it constrains.

- Uses [[02 Concepts/System Types/Embodied & Physical Systems/Model Predictive Control|Model Predictive Control]]. **Condition:** For predictive safety filters that solve a constrained finite-horizon problem to find the nearest safe action.

- Constrains the commanded actions of [[02 Concepts/System Types/Embodied & Physical Systems/Vision Language Action Model|Vision Language Action Model]]. **Condition:** When the filter runs on every action at control rate with authority over the learned policy.

- Bounds contact force at the actuator through [[02 Concepts/System Types/Embodied & Physical Systems/Impedance and Force Control|Impedance and Force Control]]. **Condition:** When the filter's safe action is expressed as a force or stiffness limit rather than a position correction.

- Certifies candidate actions against sets computed by [[02 Concepts/Qualities/Safety & Assurance/Reachability Analysis|Reachability Analysis]]. **Condition:** When the filter's safe set is the complement of the backward reachable set of the failure region.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: shield; shielding; action shield.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
