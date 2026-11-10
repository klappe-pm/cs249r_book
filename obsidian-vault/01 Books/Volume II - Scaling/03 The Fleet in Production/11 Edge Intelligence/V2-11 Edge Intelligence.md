---
title: V2-11 Edge Intelligence
type: Chapter
volume: 2
chapter: 11
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/11_edge_intelligence/11_edge_intelligence.qmd
source_anchor: sec-edge-intelligence
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/11_edge_intelligence/11_edge_intelligence.html
---

# V2-11 Edge Intelligence

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-edge-intelligence

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-11) for this chapter

![[90 Assets/Volume II/11 Edge Intelligence/Cover Edge Intelligence Blueprint Labeled 105fd8a04d.webp]]

*Cloud-to-edge blueprint where a central model reaches heterogeneous devices, private local data stays on device, and update streams return to aggregation.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.01 Purpose|V2-11.01 Purpose]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.02 The Edge Learning Paradigm|V2-11.02 The Edge Learning Paradigm]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.03 Why Learn on the Device|V2-11.03 Why Learn on the Device]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.04 Design Constraints|V2-11.04 Design Constraints]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.05 Model Adaptation|V2-11.05 Model Adaptation]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.06 Data Efficiency|V2-11.06 Data Efficiency]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.07 Federated Learning Algorithms|V2-11.07 Federated Learning Algorithms]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.08 Federated Learning Systems at Scale|V2-11.08 Federated Learning Systems at Scale]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.09 Continual Adaptation Under Edge Budgets|V2-11.09 Continual Adaptation Under Edge Budgets]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.10 Integrating the Edge Intelligence Pillars|V2-11.10 Integrating the Edge Intelligence Pillars]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.11 Production Integration|V2-11.11 Production Integration]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.12 Engineering Challenges and Mitigations|V2-11.12 Engineering Challenges and Mitigations]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.13 Fallacies and Pitfalls|V2-11.13 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.14 Summary|V2-11.14 Summary]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.15 Self-Check Answers|V2-11.15 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.16 Source References|V2-11.16 Source References]]
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.17 Footnotes|V2-11.17 Footnotes]]

Next: [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11.01 Purpose|V2-11.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/11_edge_intelligence.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/11_edge_intelligence/11_edge_intelligence.html#sec-edge-intelligence). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Stack/Parallelism & Distributed Execution/Client Selection|Client Selection]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Federated Averaging|Federated Averaging]]
- [[02 Concepts/Stack/Parallelism & Distributed Execution/Federated Learning|Federated Learning]]
- [[02 Concepts/Qualities/Security & Privacy/Secure Aggregation|Secure Aggregation]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; C3 taxonomy.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Capacity and bandwidth are separate tests; Rack power wall.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Gradient compression with error feedback.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Synchronization models and stragglers; Parallelism plan as joint placement.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Silent data corruption verification.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Feasibility before fairness.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Prefill-decode interference and chunked prefill; SLO goodput and the serving tax.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/edge_intelligence_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Dependency-aware registry; Staged rollout exposure budget.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Differential privacy; Privacy budget account; Poisoning as a bilevel attack; Leakage through authorized outputs; Breakdown point of the gradient mean.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Shift taxonomy.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/11_edge_intelligence/edge_intelligence_concepts.yml)

<!-- Semantic Navigation: End -->
