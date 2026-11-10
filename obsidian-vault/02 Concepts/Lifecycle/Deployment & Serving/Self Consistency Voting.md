---
title: Self Consistency Voting
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Self-consistency voting
taxonomy_id: mlsys.self-consistency
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Self Consistency Voting

Sampling multiple reasoning paths and returning the most frequent final answer.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Requires sampling diversity from [[02 Concepts/Lifecycle/Deployment & Serving/Decoding and Sampling Controls|Decoding and Sampling Controls]]. **Condition:** For the sampled-reasoning-path procedure, diversity comes from stochastic decoding; repeated deterministic greedy generation with the same model and prompt produces the same path.

- Multiplies generation cost in [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Cost scales with the number of sampled reasoning paths.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: majority voting.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
