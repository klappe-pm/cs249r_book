---
title: Hardware Fault Injection
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Fault_Injection_Resilience_Testing
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Hardware fault injection
taxonomy_id: mlsys.hardware-fault-injection
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Hardware Fault Injection

Emulating hardware faults such as bit flips in weights, activations, or registers to measure how errors propagate to model outputs.

## Browsing Home

[[02 Concepts/Qualities/Reliability & Fault Tolerance/Fault Injection & Resilience Testing Subject|Fault Injection & Resilience Testing]] → [[02 Concepts/Qualities/Reliability & Fault Tolerance/Reliability & Fault Tolerance Index|Reliability & Fault Tolerance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Estimates model sensitivity to [[02 Concepts/Qualities/Reliability & Fault Tolerance/Silent Data Corruption|Silent Data Corruption]]. **Condition:** When the injected fault model, location, and rate approximate the hardware's actual failure modes.

- Is a kind of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Failure Injection|Failure Injection]]. **Condition:** When the injected faults are bit flips or stuck-at errors in model state rather than service-level faults.

- Measures the detection coverage of [[02 Concepts/Qualities/Reliability & Fault Tolerance/Algorithm Based Fault Tolerance|Algorithm Based Fault Tolerance]]. **Condition:** When injected faults hit the operations the checksums protect, at realistic rates and locations.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
