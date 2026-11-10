---
title: V2-09 Fleet Efficiency
type: Chapter
volume: 2
chapter: 9
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/09_performance_engineering/09_performance_engineering.qmd
source_anchor: sec-performance-engineering
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/09_performance_engineering/09_performance_engineering.html
---

# V2-09 Fleet Efficiency

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-performance-engineering

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-09) for this chapter

![[90 Assets/Volume II/09 Performance Engineering/Cover Performance Engineering Blueprint Labeled 4087598c28.webp]]

*Fleet efficiency workbench where a fleet workload is measured, the capacity it loses before, during, and inside its running steps is charged to scheduling, runtime, and the program, and the program's share is recovered.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.01 Purpose|V2-09.01 Purpose]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.02 Where Fleet Capacity Goes|V2-09.02 Where Fleet Capacity Goes]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.03 ML Goodput|V2-09.03 ML Goodput]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.04 Measuring Goodput|V2-09.04 Measuring Goodput]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.05 Scheduling Goodput|V2-09.05 Scheduling Goodput]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.06 Runtime Goodput|V2-09.06 Runtime Goodput]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.07 Program Goodput|V2-09.07 Program Goodput]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.08 Recovering Program Goodput|V2-09.08 Recovering Program Goodput]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.09 The Whole Fleet|V2-09.09 The Whole Fleet]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.10 Trading Between Factors|V2-09.10 Trading Between Factors]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.11 Fallacies and Pitfalls|V2-09.11 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.12 Summary|V2-09.12 Summary]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.13 Self-Check Answers|V2-09.13 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.14 Source References|V2-09.14 Source References]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.15 Footnotes|V2-09.15 Footnotes]]

Next: [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09.01 Purpose|V2-09.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/09_performance_engineering/09_performance_engineering.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/09_performance_engineering/09_performance_engineering.html#sec-performance-engineering). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Model FLOPS Utilization|Model FLOPS Utilization]]
- [[02 Concepts/Qualities/Performance, Efficiency & Benchmarking/Training Goodput|Training Goodput]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Naming the efficiency measure.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Capacity and bandwidth are separate tests; Plan on sustained throughput.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Data stall ratio.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Exposed communication under overlap.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Synchronization models and stragglers; Scaling efficiency and the scaling wall.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Young-Daly checkpoint interval; Recovery-time budget and fencing; Gray failure detection.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Gang scheduling; Utilization tiers; Interruption economics.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/09_performance_engineering/performance_engineering_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — SLO goodput and the serving tax; KV cache as admission budget; Phase-aware autoscaling and cold start.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/09_performance_engineering/performance_engineering_concepts.yml)

<!-- Semantic Navigation: End -->
