---
title: Inference Time Search
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Inference-time search
taxonomy_id: mlsys.inference-time-search
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Inference Time Search

Exploring a tree of partial solutions, as in beam or tree search, guided by a scorer, to find a higher-quality output.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03.03 Three Axes of Test-Time Compute#^sec-vol3-test-time-compute-computation-allocation|V3-03.03 Three Axes of Test-Time Compute]] — Test-time search. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/03_test_time_compute/03_test_time_compute.qmd#L147).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Uses for pruning [[02 Concepts/Lifecycle/Deployment & Serving/Process Reward Model|Process Reward Model]]. **Condition:** Holds for searches that score partial solutions before completion.

- Multiplies per-query compute in [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Holds in proportion to the number of expanded and scored nodes.

- Shares partial-solution state through [[02 Concepts/Lifecycle/Deployment & Serving/Prefix Caching|Prefix Caching]]. **Condition:** Applies when branches share prompt and partial-solution prefixes on one server.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
