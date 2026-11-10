---
title: Shadow Deployment
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Versioning_Rollout_Rollback
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Shadow deployment
taxonomy_id: mlsys.shadow-deployment
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Shadow Deployment

Running a candidate model on live traffic without serving its outputs, to compare it against the production model.

## Browsing Home

[[02 Concepts/Lifecycle/MLOps & Operations/Versioning, Rollout & Rollback Subject|Versioning, Rollout & Rollback]] → [[02 Concepts/Lifecycle/MLOps & Operations/MLOps & Operations Index|MLOps & Operations]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the zero-exposure stage before [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]. **Condition:** Holds when candidate outputs can be compared without user exposure; shadowing cannot measure effects of users reacting to the new model.

- Can expose [[02 Concepts/Lifecycle/Data Engineering/Training Serving Skew|Training Serving Skew]]. **Condition:** Holds when shadow outputs are compared with offline predictions on the same inputs.

- Duplicates inference cost in [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Holds for the shadow period because every mirrored request runs on both models.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: shadow mode.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
