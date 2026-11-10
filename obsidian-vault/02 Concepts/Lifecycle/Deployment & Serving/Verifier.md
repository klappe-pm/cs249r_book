---
title: Verifier
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Verifier
taxonomy_id: mlsys.verifier
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Verifier

A model or program that judges whether a candidate output or reasoning step is correct, used for selection, search, or reward.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.05 Verifying Candidates#^sec-vol3-test-time-compute-check-precision|V3-03.05 Verifying Candidates]] — Verifier precision. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/03_test_time_compute/03_test_time_compute.qmd#L705).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Precision bounds the gains of [[02 Concepts/Lifecycle/Deployment & Serving/Best of N Sampling|Best of N Sampling]]. **Condition:** Holds as n grows, since selection pressure increasingly exploits verifier errors.

- Imperfect checks can cause [[02 Concepts/Lifecycle/Training & Adaptation/Reward Hacking|Reward Hacking]]. **Condition:** Holds when a policy or search is optimized against a verifier with exploitable false positives.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: outcome reward model.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
