---
title: V2-15 Sustainable AI
type: Chapter
volume: 2
chapter: 15
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/15_sustainable_ai/15_sustainable_ai.qmd
source_anchor: sec-sustainable-ai
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/15_sustainable_ai/15_sustainable_ai.html
---

# V2-15 Sustainable AI

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-sustainable-ai

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-15) for this chapter

![[90 Assets/Volume II/15 Sustainable AI/Cover Sustainable AI Blueprint Labeled 339e34ba25.webp]]

*Sustainable fleet cutaway connecting compute racks to power delivery, cooling loops, grid sources, carbon accounting, efficiency controls, and lifecycle management.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.01 Purpose|V2-15.01 Purpose]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.02 The Energy Ceiling|V2-15.02 The Energy Ceiling]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.03 The Scale of Environmental Impact|V2-15.03 The Scale of Environmental Impact]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.04 Exponential Growth Vs. Physical Constraints|V2-15.04 Exponential Growth Vs. Physical Constraints]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.05 Energy Measurement and Modeling|V2-15.05 Energy Measurement and Modeling]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.06 Carbon Footprint Calculation|V2-15.06 Carbon Footprint Calculation]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.07 Data Center Energy and Resource Consumption|V2-15.07 Data Center Energy and Resource Consumption]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.08 Training Vs. Inference Energy Analysis|V2-15.08 Training Vs. Inference Energy Analysis]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.09 Hardware Lifecycle and E-Waste|V2-15.09 Hardware Lifecycle and E-Waste]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.10 Mitigation Strategies|V2-15.10 Mitigation Strategies]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.11 Policy, Regulation, and the Path Forward|V2-15.11 Policy, Regulation, and the Path Forward]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.12 Fallacies and Pitfalls|V2-15.12 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.13 Summary|V2-15.13 Summary]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.14 Self-Check Answers|V2-15.14 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.15 Source References|V2-15.15 Source References]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.16 Footnotes|V2-15.16 Footnotes]]

Next: [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15.01 Purpose|V2-15.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/15_sustainable_ai/15_sustainable_ai.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/15_sustainable_ai/15_sustainable_ai.html#sec-sustainable-ai). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Sustainability & Cost/Carbon Aware Scheduling|Carbon Aware Scheduling]]
- [[02 Concepts/Qualities/Sustainability & Cost/Embodied Carbon|Embodied Carbon]]
- [[02 Concepts/Qualities/Sustainability & Cost/Lifecycle Carbon|Lifecycle Carbon]]
- [[02 Concepts/Qualities/Sustainability & Cost/Operating Energy|Operating Energy]]
- [[02 Concepts/Qualities/Sustainability & Cost/Operational Carbon|Operational Carbon]]
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Power Usage Effectiveness|Power Usage Effectiveness]]

## Related Themes

- [[03 Themes/Energy and Cost|Energy and Cost]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Scaling laws as the demand curve; Compute-optimal allocation; Energy accounting boundary; Fleet Law.
- [[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure|V2-02 Compute Infrastructure]] — Rack power wall; Cooling class and heat removal; Capacity and bandwidth are separate tests.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Data-movement energy per boundary.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Parallelism plan as joint placement; Expert parallelism.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Young-Daly checkpoint interval; Fleet failure rate.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Interruption economics; Utilization tiers.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency|V2-09 Fleet Efficiency]] — ML goodput; Reproducible measurement contract.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Prefill-decode interference and chunked prefill; SLO goodput and the serving tax; Serving cost dominance.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Background adaptation admission; FedAvg under sampling and non-IID data.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Lifecycle TCO.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Adversarial robustness for a named threat model; Generative reliability.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/15_sustainable_ai/sustainable_ai_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI|V2-16 Responsible AI]] — Contestability and remedy.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/15_sustainable_ai/sustainable_ai_concepts.yml)

<!-- Semantic Navigation: End -->
