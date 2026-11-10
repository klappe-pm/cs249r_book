---
title: V2-07 Fault Tolerance
type: Chapter
volume: 2
chapter: 7
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/07_fault_tolerance/07_fault_tolerance.qmd
source_anchor: sec-fault-tolerance-reliability
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/07_fault_tolerance/07_fault_tolerance.html
---

# V2-07 Fault Tolerance

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-fault-tolerance-reliability

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-07) for this chapter

![[90 Assets/Volume II/07 Fault Tolerance/Cover Fault Tolerance Blueprint Labeled c15e74e434.webp]]

*Fleet recovery blueprint showing a training path interrupted by a failed node, checkpoint state preserved, and work resumed through replacement workers.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.01 Purpose|V2-07.01 Purpose]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.02 Failure Analysis at Scale|V2-07.02 Failure Analysis at Scale]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.03 The Mathematics of Inevitable Failure|V2-07.03 The Mathematics of Inevitable Failure]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.04 Failure Taxonomy|V2-07.04 Failure Taxonomy]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.05 Hardware Faults at Fleet Scale|V2-07.05 Hardware Faults at Fleet Scale]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.06 Check-And-Verify Defenses Against Silent Data Corruption|V2-07.06 Check-And-Verify Defenses Against Silent Data Corruption]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.07 Software Faults|V2-07.07 Software Faults]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.08 The Cost of Failure|V2-07.08 The Cost of Failure]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.09 Checkpointing and Progress Preservation|V2-07.09 Checkpointing and Progress Preservation]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.10 Failure Detection and Recovery|V2-07.10 Failure Detection and Recovery]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.11 Elastic Recovery|V2-07.11 Elastic Recovery]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.12 Serving Fault Tolerance|V2-07.12 Serving Fault Tolerance]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.13 Graceful Degradation|V2-07.13 Graceful Degradation]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.14 Distributed Debugging and Observability|V2-07.14 Distributed Debugging and Observability]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.15 Fault Injection Tools and Frameworks|V2-07.15 Fault Injection Tools and Frameworks]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.16 Case Studies|V2-07.16 Case Studies]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.17 Fallacies and Pitfalls|V2-07.17 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.18 Summary|V2-07.18 Summary]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.19 Self-Check Answers|V2-07.19 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.20 Source References|V2-07.20 Source References]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.21 Footnotes|V2-07.21 Footnotes]]

Next: [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07.01 Purpose|V2-07.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/07_fault_tolerance/07_fault_tolerance.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/07_fault_tolerance/07_fault_tolerance.html#sec-fault-tolerance-reliability). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Consistent Checkpoint Cut|Consistent Checkpoint Cut]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Fencing|Fencing]]
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Mean Time Between Failures|Mean Time Between Failures]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Reliability gap; Fleet Law; Scaling laws as the demand curve; Synchronous tight coupling.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Physical failure domains.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Checkpoint write path; Checkpoint storm.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Sharded data parallelism; Critical batch size; Synchronization models and stragglers; Data-parallel update equivalence.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/07_fault_tolerance/fault_tolerance_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Interruption economics.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — KV cache as admission budget; Overload containment.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Participation selection.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Hierarchical fleet alerting.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Breakdown point of the gradient mean.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Distinguishing faults from shift; Robustness per failure class.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/07_fault_tolerance/fault_tolerance_concepts.yml)

<!-- Semantic Navigation: End -->
