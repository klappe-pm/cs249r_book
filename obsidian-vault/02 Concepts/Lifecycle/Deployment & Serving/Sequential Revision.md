---
title: Sequential Revision
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Test_Time_Compute
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Sequential revision
taxonomy_id: mlsys.sequential-revision
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Sequential Revision

Refining an answer through successive model calls conditioned on earlier drafts and internal or external feedback, spending additional inference compute on dependent revisions.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Test Time Compute Subject|Test Time Compute]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Spends compute serially rather than in parallel samples as in [[02 Concepts/Lifecycle/Deployment & Serving/Best of N Sampling|Best of N Sampling]]. **Condition:** When one task's inference budget is allocated between dependent revisions and independent candidates.

- Benefits from external feedback supplied by [[02 Concepts/Lifecycle/Deployment & Serving/Verifier|Verifier]]. **Condition:** When the critique comes from a checker rather than the model's own judgment, which is often unreliable.

- Adds serial passes to [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** Each pass must finish before the next begins.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: self-refine; self-correction; reflection; iterative refinement.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
