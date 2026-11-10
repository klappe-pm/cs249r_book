---
title: Feature Attribution
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Explainability_Documentation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Feature attribution
taxonomy_id: mlsys.feature-attribution
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Feature Attribution

Post-hoc explanation assigning each input feature a contribution to a specific prediction.

## Browsing Home

[[02 Concepts/Qualities/Responsible AI/Explainability & Documentation Subject|Explainability & Documentation]] → [[02 Concepts/Qualities/Responsible AI/Responsible AI Index|Responsible AI]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Adds to [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Holds when explanations are computed on the request path; perturbation-based methods need many extra model evaluations.

- Detects [[02 Concepts/Lifecycle/Data Engineering/Data Leakage|Data Leakage]]. **Condition:** When a feature unavailable at prediction time dominates attributions.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SHAP; LIME; integrated gradients; saliency.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
