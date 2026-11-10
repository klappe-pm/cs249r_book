---
title: V2-03 Network Fabrics
type: Chapter
volume: 2
chapter: 3
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/03_network_fabrics/03_network_fabrics.qmd
source_anchor: sec-network-fabrics
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/03_network_fabrics/03_network_fabrics.html
---

# V2-03 Network Fabrics

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-network-fabrics

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-03) for this chapter

![[90 Assets/Volume II/03 Network Fabrics/Cover Network Fabrics Blueprint Labeled 45b41920e2.webp]]

*Isometric network fabric map connecting accelerator racks through elevated fabric layers with synchronization paths and a congestion constraint.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.01 Purpose|V2-03.01 Purpose]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.02 The Synchronization Backbone|V2-03.02 The Synchronization Backbone]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.03 How ML Networking Inverts Data-Center Assumptions|V2-03.03 How ML Networking Inverts Data-Center Assumptions]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.04 Level 1 Wire and Link|V2-03.04 Level 1 Wire and Link]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.05 Level 2 Transport and the Performance Model|V2-03.05 Level 2 Transport and the Performance Model]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.06 Level 3 Switch and Topology|V2-03.06 Level 3 Switch and Topology]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.07 Level 4 Fabric Behavior, Congestion, and Routing|V2-03.07 Level 4 Fabric Behavior, Congestion, and Routing]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.08 Level 5 Cluster Design and Case Studies|V2-03.08 Level 5 Cluster Design and Case Studies]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.09 Network Virtualization|V2-03.09 Network Virtualization]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.10 Monitoring and Debugging|V2-03.10 Monitoring and Debugging]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.11 Network Technologies That Move the Ceiling|V2-03.11 Network Technologies That Move the Ceiling]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.12 Fallacies and Pitfalls|V2-03.12 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.13 Summary|V2-03.13 Summary]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.14 Self-Check Answers|V2-03.14 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.15 Source References|V2-03.15 Source References]]
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.16 Footnotes|V2-03.16 Footnotes]]

Next: [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03.01 Purpose|V2-03.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/03_network_fabrics.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/03_network_fabrics/03_network_fabrics.html#sec-network-fabrics). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Adaptive Routing|Adaptive Routing]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Alpha Beta Communication Model|Alpha Beta Communication Model]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Bisection Bandwidth|Bisection Bandwidth]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Datacenter Congestion Control|Datacenter Congestion Control]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Network Topology|Network Topology]]

## Related Themes

- [[03 Themes/Scaling and Coordination|Scaling and Coordination]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Scaling laws as the demand curve; Synchronous tight coupling.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Bandwidth hierarchy dictates placement; Node aggregates private memories; Physical failure domains.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/network_fabrics_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage|V2-04 Data Storage]] — Checkpoint write path.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Collective contracts; Ring AllReduce and the bandwidth bound; Exposed communication under overlap; Ring-tree crossover; Hierarchical collectives.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Parallelism plan as joint placement; Expert parallelism; Sparse embedding sharding.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Gray failure detection.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Topology-aware placement.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/03_network_fabrics/network_fabrics_concepts.yml)

<!-- Semantic Navigation: End -->
