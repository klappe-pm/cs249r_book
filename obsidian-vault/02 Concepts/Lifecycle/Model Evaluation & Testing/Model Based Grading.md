---
title: Model Based Grading
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluating_Generative_Agentic_Systems
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Model-based grading
taxonomy_id: mlsys.llm-judge
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Model Based Grading

Using a language model to score or compare generated outputs against a rubric, with its own biases and error rates to be measured.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluating Generative & Agentic Systems Subject|Evaluating Generative & Agentic Systems]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Must be calibrated against [[02 Concepts/Lifecycle/Model Evaluation & Testing/Human Evaluation|Human Evaluation]]. **Condition:** Holds whenever model-graded scores are used as evidence; judges show position, length, and self-preference biases.

- Can flag [[02 Concepts/Lifecycle/Model Evaluation & Testing/Hallucination|Hallucination]]. **Condition:** Holds when the judge sees the source evidence and its error rate has been measured against people.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: LLM-as-judge.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
