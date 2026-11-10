---
title: Expert Replication and Placement
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Parallelization_Planning_Placement
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Expert replication and placement
taxonomy_id: mlsys.expert-placement
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Expert Replication and Placement

Assigning mixture-of-experts experts to devices, and replicating frequently routed ones, to balance per-device token load under skewed routing.

## Browsing Home

[[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelization Planning & Placement Subject|Parallelization Planning & Placement]] → [[02 Concepts/Stack/Parallelism & Distributed Execution/Parallelism & Distributed Execution Index|Parallelism & Distributed Execution]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a placement decision within [[02 Concepts/Stack/Parallelism & Distributed Execution/Expert Parallelism|Expert Parallelism]]. **Condition:** Experts are distributed across devices.

- Relieves overloaded devices that become [[02 Concepts/Stack/Parallelism & Distributed Execution/Stragglers|Stragglers]]. **Condition:** Routing concentrates tokens on a few experts.

- Balances load in the system rather than the model as in [[02 Concepts/Foundations/Models & Architectures/Load Balancing Loss|Load Balancing Loss]]. **Condition:** Routing remains skewed despite training-time balancing.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: expert load balancing; redundant experts.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
