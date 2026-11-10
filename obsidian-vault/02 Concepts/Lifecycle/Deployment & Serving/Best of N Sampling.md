---
title: Best of N Sampling
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Best-of-n sampling
taxonomy_id: mlsys.best-of-n
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Best of N Sampling

Generating n candidate outputs and returning the one ranked highest by a scorer or verifier.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Multiplies generation cost in [[02 Concepts/Qualities/Sustainability & Cost/Cost per Useful Outcome|Cost per Useful Outcome]]. **Condition:** Generation cost scales roughly linearly with n unless prefixes are shared.

- Is an alternative to [[02 Concepts/Lifecycle/Deployment & Serving/Self Consistency Voting|Self Consistency Voting]]. **Condition:** Both spend parallel samples; best-of-n needs a scorer while self-consistency needs answers that can be voted on.

- Requires candidate diversity from [[02 Concepts/Lifecycle/Deployment & Serving/Decoding and Sampling Controls|Decoding and Sampling Controls]]. **Condition:** For repeated generation with the same model and prompt when stochastic token selection supplies candidate diversity; deterministic greedy decoding with unchanged inputs repeats the same output.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
