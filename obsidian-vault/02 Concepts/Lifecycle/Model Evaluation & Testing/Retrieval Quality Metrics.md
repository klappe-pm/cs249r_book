---
title: Retrieval Quality Metrics
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Metrics_Calibration_Uncertainty
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Retrieval quality metrics
taxonomy_id: mlsys.retrieval-metrics
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Retrieval Quality Metrics

Measures of a retriever's ranked results against relevance judgments, such as recall at k, mean reciprocal rank, and normalized discounted cumulative gain, which show the retrieval depth and ranking quality a downstream reranker or generator can rely on.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Metrics, Calibration & Uncertainty Subject|Metrics, Calibration & Uncertainty]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the ranked-list family of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** When outputs are ranked candidate lists judged against relevance labels.

- Scores the ranked results of [[02 Concepts/Lifecycle/Deployment & Serving/Retrieval|Retrieval]]. **Condition:** When relevance judgments exist for the query set; judged pools miss relevant unjudged records.

- Quantifies, as recall against exact search, the approximation loss of [[02 Concepts/Lifecycle/Deployment & Serving/Approximate Nearest Neighbor Search|Approximate Nearest Neighbor Search]]. **Condition:** When ground-truth neighbors are computed by exhaustive search on the same corpus.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: recall@k; precision@k; nDCG; mean reciprocal rank; MRR; retrieval hit rate.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
