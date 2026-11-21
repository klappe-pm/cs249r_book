---
title: V2-08 Fleet Orchestration
type: Chapter
volume: 2
chapter: 8
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/08_fleet_orchestration/08_fleet_orchestration.qmd
source_anchor: sec-fleet-orchestration
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/08_fleet_orchestration/08_fleet_orchestration.html
---

# V2-08 Fleet Orchestration

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-fleet-orchestration

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-08) for this chapter

![[90 Assets/Volume II/08 Fleet Orchestration/Cover Fleet Orchestration Blueprint Labeled 80a3208e87.webp]]

*Scheduler control-plane blueprint where queued jobs are placed onto topology-aware accelerator capacity with preemption, recovery, and policy constraints.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.01 Purpose|V2-08.01 Purpose]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.02 The Scheduling Problem|V2-08.02 The Scheduling Problem]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.03 Distributed Scheduling Complexity|V2-08.03 Distributed Scheduling Complexity]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.04 Scheduling Objectives and Their Conflicts|V2-08.04 Scheduling Objectives and Their Conflicts]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.05 Core Allocation Constraints|V2-08.05 Core Allocation Constraints]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.06 Orchestration Paradigms|V2-08.06 Orchestration Paradigms]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.07 Topology-Aware Scheduling|V2-08.07 Topology-Aware Scheduling]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.08 Elastic Scheduling|V2-08.08 Elastic Scheduling]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.09 Cost Optimization|V2-08.09 Cost Optimization]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.10 Custom ML Schedulers|V2-08.10 Custom ML Schedulers]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.11 Serving Capacity in the Shared Fleet|V2-08.11 Serving Capacity in the Shared Fleet]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.12 Multi-Tenancy and Quotas|V2-08.12 Multi-Tenancy and Quotas]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.13 Debugging Cluster Utilization|V2-08.13 Debugging Cluster Utilization]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.14 Fallacies and Pitfalls|V2-08.14 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.15 Summary|V2-08.15 Summary]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.16 Self-Check Answers|V2-08.16 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.17 Source References|V2-08.17 Source References]]
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.18 Footnotes|V2-08.18 Footnotes]]

Next: [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08.01 Purpose|V2-08.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/08_fleet_orchestration/08_fleet_orchestration.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/08_fleet_orchestration/08_fleet_orchestration.html#sec-fleet-orchestration). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Dominant Resource Fairness|Dominant Resource Fairness]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Gang Scheduling|Gang Scheduling]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Topology Aware Placement|Topology Aware Placement]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Naming the efficiency measure; Scaling laws as the demand curve; CAP choice under partition.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Bandwidth hierarchy dictates placement.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — Bisection bandwidth and topology economics; Traffic-matched topology; Silent fabric waste.
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Checkpoint storm; Data stall ratio; Checkpoint write path.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Hierarchical collectives.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Pipeline parallelism bubble; Sharded data parallelism; Critical batch size; Synchronization models and stragglers; Scaling efficiency and the scaling wall; Alignment training co-location.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Fleet failure rate; Recovery-time budget and fencing; Young-Daly checkpoint interval; Elastic recovery invariants; Gray failure detection.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/08_fleet_orchestration/fleet_orchestration_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — ML goodput; Fleet profiling by hierarchy and sampling.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Phase-aware autoscaling and cold start; KV cache as admission budget; Token-denominated tenant isolation.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Staged rollout exposure budget; Lifecycle TCO; Utilization as the economic invariant; Hierarchical fleet alerting.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Security controls priced on a C3 axis.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/08_fleet_orchestration/fleet_orchestration_concepts.yml)

<!-- Semantic Navigation: End -->
