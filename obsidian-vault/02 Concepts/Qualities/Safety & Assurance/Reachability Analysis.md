---
title: Reachability Analysis
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
- Context/Background
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Reachability analysis
taxonomy_id: mlsys.reachability-analysis
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Reachability Analysis

Computing the set of states a system, or another agent in its workspace, can reach within a time horizon under its dynamics and bounded inputs or disturbances, used to prove a safe set invariant, to size clearance margins, and to screen proposed motions against where other agents could be.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

This is a background concept on which ML systems reasoning depends; that classification does not make it optional.

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Gives a set-based safety certificate as an alternative to [[02 Concepts/Qualities/Safety & Assurance/Control Barrier Function|Control Barrier Function]]. **Condition:** CBFs give local differentiable constraints; reachability gives the safe set itself at the cost of state-space computation.

- Propagates the [[02 Concepts/System Types/Embodied & Physical Systems/Physical Dynamics|Physical Dynamics]]. **Condition:** Always; the reachable set is defined by the dynamics model and the input and disturbance bounds.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: forward reachable set; backward reachable set; Hamilton-Jacobi reachability; reachable occupancy.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
