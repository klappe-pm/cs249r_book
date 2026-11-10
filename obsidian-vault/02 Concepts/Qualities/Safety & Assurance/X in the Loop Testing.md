---
title: X in the Loop Testing
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Safety_Verification_Validation
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: X-in-the-loop testing
taxonomy_id: mlsys.xil-testing
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# X in the Loop Testing

A qualification ladder that runs the real software, then real hardware, against simulated or recorded environments before physical trials.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Safety Verification & Validation Subject|Safety Verification & Validation]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Progressively tests [[02 Concepts/System Types/Embodied & Physical Systems/Simulation to Real Transfer|Simulation to Real Transfer]]. **Condition:** Each rung adds real software, timing, or hardware but still relies on simulated or recorded environments.

- Measures [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** When the real compute and hardware run in the loop, exposing timing that pure simulation omits.

- Is a kind of [[02 Concepts/Lifecycle/Model Evaluation & Testing/Integration Testing|Integration Testing]]. **Condition:** Each rung tests the assembled software or hardware against a simulated or recorded environment.

- Provides simulated loops for [[02 Concepts/Lifecycle/Model Evaluation & Testing/Closed Loop Policy Evaluation|Closed Loop Policy Evaluation]]. **Condition:** The environment model reacts to the system's actions.

- Exposes, on the real compute and bus, [[02 Concepts/System Types/Embodied & Physical Systems/Timing Jitter|Timing Jitter]]. **Condition:** When the real software and hardware run in the loop; pure simulation hides it.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: HIL; software-in-the-loop; hardware-in-the-loop.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
