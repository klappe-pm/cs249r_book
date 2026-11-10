---
title: Watchdog Timer
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Real_Time_Mixed_Criticality_Computing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Watchdog timer
taxonomy_id: mlsys.watchdog-timer
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Watchdog Timer

A timer that a monitored component must refresh within a deadline or window; expiry triggers a defined safe response such as reset or revoking control authority.

## Browsing Home

[[02 Concepts/System Types/Embodied & Physical Systems/Real Time & Mixed Criticality Computing Subject|Real Time & Mixed Criticality Computing]] → [[02 Concepts/System Types/Embodied & Physical Systems/Embodied & Physical Systems Index|Embodied & Physical Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a liveness mechanism within [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]. **Condition:** The monitored component can hang or stall.

- Triggers on expiry [[02 Concepts/Qualities/Safety & Assurance/Minimal Risk Condition|Minimal Risk Condition]]. **Condition:** A safe fallback state is defined.

- Reports a missed refresh deadline as a fault, revealing excess [[02 Concepts/System Types/Embodied & Physical Systems/Feedback Delay|Feedback Delay]]. **Condition:** The window is derived from the control period and the refresh is placed after actuation.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: heartbeat timeout; windowed watchdog; authority-expiry timer.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
