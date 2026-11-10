---
title: Sycophancy Evaluation
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluating_Generative_Agentic_Systems
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sycophancy evaluation
taxonomy_id: mlsys.sycophancy-evaluation
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sycophancy Evaluation

Measuring how often a model abandons a correct answer or endorses a user's mistaken claim under pushback, authority cues, or social pressure, usually across several turns, so that agreement-seeking is measured separately from task accuracy.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluating Generative & Agentic Systems Subject|Evaluating Generative & Agentic Systems]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Surfaces agreement-seeking learned as a form of [[02 Concepts/Lifecycle/Training & Adaptation/Reward Hacking|Reward Hacking]]. **Condition:** When preference training rewarded user approval and the evaluation shows agreement rising while task correctness falls for the same behavior.

- Is a kind of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Robustness Evaluation|Robustness Evaluation]]. **Condition:** When the perturbation is conversational pressure rather than input corruption.

- Scores free-form multi-turn answers with [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Based Grading|Model Based Grading]]. **Condition:** When responses are open-ended, so a flip cannot be read off a fixed label.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: sycophancy benchmark; persuasion robustness evaluation; rebuttal flip rate; agreement-seeking evaluation.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
