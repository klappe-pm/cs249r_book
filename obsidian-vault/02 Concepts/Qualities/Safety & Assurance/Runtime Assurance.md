---
title: Runtime Assurance
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Runtime assurance
taxonomy_id: mlsys.runtime-assurance
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Runtime Assurance

Monitoring and constraining execution using explicitly stated safety premises and fallback mechanisms.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

- [[01 Books/Volume IV - Physical AI/03 Running the Machine/12 Safety Enforcement/V4-12.08 The Minimal Intervention Principle and Optimization Filters#^sec-enforcement-minimal-intervention|V4-12.08 The Minimal Intervention Principle and Optimization Filters]] — Runtime safety filter. [Exact Source Passage](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol4/12_enforcement/12_enforcement.qmd#L1603).

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Checks proposed actions against [[02 Concepts/System Types/Embodied & Physical Systems/Trajectory Feasibility|Trajectory Feasibility]]. **Condition:** When the monitor's feasibility model, timing, and implementation assumptions hold; the guarantee is only as good as that model.

- Relies on qualified [[02 Concepts/System Types/Embodied & Physical Systems/State Estimation|State Estimation]]. **Condition:** State-dependent checks need valid observation timing and error bounds; the guarantee remains conditional on those premises.

- Can gate prospective [[02 Concepts/Qualities/Reliability & Fault Tolerance/Irreversible Effects|Irreversible Effects]]. **Condition:** Only when the mechanism mediates the relevant pre-actuation path with sufficient timing and authority. Detection can occur after an effect, and fallback can itself be irreversible.

- Checks the current state against [[02 Concepts/Qualities/Safety & Assurance/Stopping Envelope|Stopping Envelope]]. **Condition:** When the fallback is a stop and the monitor runs fast enough to trigger it before the state leaves the envelope.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
