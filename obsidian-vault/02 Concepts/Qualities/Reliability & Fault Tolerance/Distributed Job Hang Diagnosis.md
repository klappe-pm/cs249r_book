---
title: Distributed Job Hang Diagnosis
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Hardware_Faults_Silent_Data_Corruption
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Distributed job hang diagnosis
taxonomy_id: mlsys.distributed-hang-diagnosis
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Distributed Job Hang Diagnosis

Detecting and localizing stalled distributed jobs through collective timeouts, heartbeats, per-rank progress traces, and node health checks, so faulty ranks can be isolated.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Hardware Faults & Silent Data Corruption Subject|Hardware Faults & Silent Data Corruption]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Identifies [[02 Concepts/Qualities/Reliability & Fault Tolerance/Gray Failure|Gray Failure]]. **Condition:** A slow or stuck rank stalls collectives without crashing.

- Flags stalls with [[02 Concepts/System Types/Embodied & Physical Systems/Watchdog Timer|Watchdog Timer]]. **Condition:** Collectives and ranks are expected to make progress within a timeout.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: collective timeout; NCCL watchdog; node health checks.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
