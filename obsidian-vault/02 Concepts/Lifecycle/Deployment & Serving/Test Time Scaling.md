---
title: Test Time Scaling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Test-time scaling
taxonomy_id: mlsys.test-time-scaling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Test Time Scaling

The empirical relation between inference compute spent per query and output quality, used to allocate compute between model size and inference.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Extends to inference compute [[02 Concepts/Foundations/Quantitative System Models/Empirical Scaling Laws|Empirical Scaling Laws]]. **Condition:** Holds within task families where extra samples or reasoning steps improve accuracy; gains saturate and vary by difficulty.

- Sets the quality gained per unit of [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Holds whenever additional per-query compute is billed or consumes shared serving capacity.

- Uses search guided by [[02 Concepts/Lifecycle/Deployment & Serving/Verifier|Verifier]]. **Condition:** Applies to the search-based way of spending inference compute, as opposed to sequential revision.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
