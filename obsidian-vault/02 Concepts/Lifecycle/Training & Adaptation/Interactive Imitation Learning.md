---
title: Interactive Imitation Learning
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Learning_Paradigms
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Interactive imitation learning
taxonomy_id: mlsys.interactive-imitation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Interactive Imitation Learning

Imitation learning that queries an expert for corrective labels on states the learner's own policy visits and aggregates them into training data over rounds.

## Browsing Home

[[02 Concepts/Lifecycle/Training & Adaptation/Learning Paradigms Subject|Learning Paradigms]] → [[02 Concepts/Lifecycle/Training & Adaptation/Training & Adaptation Index|Training & Adaptation]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/02 Teaching the Machine/05 Physical Data/V4-05.04 Recovery and Compounding Error#^sec-data-curse-dimensionality-recoverability|V4-05.04 Recovery and Compounding Error]] — Recovery demonstrations. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/05_data/05_data.qmd#L116).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is an interactive form of [[02 Concepts/Lifecycle/Training & Adaptation/Imitation Learning|Imitation Learning]]. **Condition:** An expert can label states the learner visits.

- Trains on learner-visited states to counter [[02 Concepts/Lifecycle/Training & Adaptation/Compounding Error in Sequential Decisions|Compounding Error in Sequential Decisions]]. **Condition:** Expert corrections are available during data collection.

- Collects corrections as [[02 Concepts/System Types/Embodied & Physical Systems/Teleoperation Data|Teleoperation Data]]. **Condition:** Human operators supply corrective actions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: DAgger; dataset aggregation; recovery demonstrations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
