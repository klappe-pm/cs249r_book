---
title: Sequential Testing
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Evaluation_Design_Experiments
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sequential testing
taxonomy_id: mlsys.sequential-testing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sequential Testing

Experimental analysis that permits repeated looks at accumulating data while controlling error rates, unlike fixed-horizon tests.

## Browsing Home

[[02 Concepts/Lifecycle/Model Evaluation & Testing/Evaluation Design & Experiments Subject|Evaluation Design & Experiments]] → [[02 Concepts/Lifecycle/Model Evaluation & Testing/Model Evaluation & Testing Index|Model Evaluation & Testing]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Enables valid early stopping of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Online Experimentation|Online Experimentation]]. **Condition:** Holds when the analysis uses a sequential procedure; repeated peeking at fixed-horizon tests inflates false positives.

- Enables early stopping of a harmful stage in [[02 Concepts/Lifecycle/MLOps & Operations/Staged Rollout|Staged Rollout]]. **Condition:** Holds when the test's error guarantees allow continuous monitoring.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: SPRT; always-valid inference.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
