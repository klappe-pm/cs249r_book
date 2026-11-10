---
title: Safety Case
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Safety_Cases_Standards_Certification
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Safety case
taxonomy_id: mlsys.safety-case
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Safety Case

A structured, reviewable argument, with its evidence, assumptions, and defeaters, that a defined system is acceptably safe for a stated use within a stated operating domain.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Safety Cases, Standards & Certification Subject|Safety Cases, Standards & Certification]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/04 Governing the Machine/16 Deployment Release/V4-16.04 Safety Cases and Claims#^sec-release-assurance-grammar|V4-16.04 Safety Cases and Claims]] — Safety case. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/16_release/16_release.qmd#L582).

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.03 The Governance and Assurance Lifecycle#^sec-responsible-ai-governance-assurance-lifecycle|V2-16.03 The Governance and Assurance Lifecycle]] — Assurance case. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/16_responsible_ai/16_responsible_ai.qmd#L110).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Argues over the premises and fallbacks of [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]. **Condition:** When runtime monitoring and fallback are part of the safety argument rather than an unargued numerical filter.

- Argues only over hazards from [[02 Concepts/Qualities/Safety & Assurance/Hazard Analysis|Hazard Analysis]]. **Condition:** A safety case is complete only relative to the hazards identified for its stated operating domain.

- Draws statistical evidence from [[02 Concepts/Qualities/Safety & Assurance/Rare Event Safety Validation|Rare Event Safety Validation]]. **Condition:** Bounds hold for the sampled operating distribution and configuration, not for unmodeled conditions.

- Draws coverage evidence from [[02 Concepts/Qualities/Safety & Assurance/Scenario Based Testing|Scenario Based Testing]]. **Condition:** When scenario coverage is traced to hazards and operating-domain conditions.

- Argues acceptability against [[02 Concepts/Qualities/Safety & Assurance/Risk Acceptance Criteria|Risk Acceptance Criteria]]. **Condition:** The top claim of a safety case is that residual risk is acceptable, which is undefined without the criteria.

## Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: assurance case; UL 4600 safety case.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
