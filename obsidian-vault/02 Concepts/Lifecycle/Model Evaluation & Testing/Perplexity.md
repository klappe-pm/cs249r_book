---
title: Perplexity
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluating_Generative_Agentic_Systems
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Perplexity
taxonomy_id: mlsys.perplexity
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Perplexity

The exponentiated average negative log-likelihood per token of held-out text, measuring how well a language model predicts that text.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluating Generative & Agentic Systems Subject|Evaluating Generative & Agentic Systems]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a likelihood-based case of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Metrics|Evaluation Metrics]]. **Condition:** Models that assign token probabilities.

- Evaluates held-out performance of [[02 Concepts/Lifecycle/Training & Adaptation/Causal Language Modeling|Causal Language Modeling]]. **Condition:** Held-out text is free of training contamination.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
