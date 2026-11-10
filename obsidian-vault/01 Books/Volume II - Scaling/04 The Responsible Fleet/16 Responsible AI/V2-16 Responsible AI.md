---
title: V2-16 Responsible AI
type: Chapter
volume: 2
chapter: 16
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/16_responsible_ai/16_responsible_ai.qmd
source_anchor: sec-responsible-ai
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/16_responsible_ai/16_responsible_ai.html
---

# V2-16 Responsible AI

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-responsible-ai

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-16) for this chapter

![[90 Assets/Volume II/16 Responsible AI/Cover Responsible AI Blueprint Labeled a21c77e73e.webp]]

*Fleet governance overlay wrapping data, training, serving, monitoring, policy, fairness, privacy, audit, accountability, and incident response.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.01 Purpose|V2-16.01 Purpose]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.02 The Governance Imperative|V2-16.02 The Governance Imperative]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.03 The Governance and Assurance Lifecycle|V2-16.03 The Governance and Assurance Lifecycle]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.04 Core Principles and the ML Lifecycle|V2-16.04 Core Principles and the ML Lifecycle]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.05 Architectural Trade-Offs|V2-16.05 Architectural Trade-Offs]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.06 Fairness and Bias Mitigation|V2-16.06 Fairness and Bias Mitigation]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.07 Privacy and Data Governance|V2-16.07 Privacy and Data Governance]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.08 Explainability and Transparency|V2-16.08 Explainability and Transparency]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.09 AI Safety, Robustness, and Generative Controls|V2-16.09 AI Safety, Robustness, and Generative Controls]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.10 Accountability, Governance, and Sociotechnical Dynamics|V2-16.10 Accountability, Governance, and Sociotechnical Dynamics]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.11 Governing Responsible AI at Fleet Scale|V2-16.11 Governing Responsible AI at Fleet Scale]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.12 Fallacies and Pitfalls|V2-16.12 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.13 Summary|V2-16.13 Summary]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.14 Self-Check Answers|V2-16.14 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.15 Source References|V2-16.15 Source References]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.16 Footnotes|V2-16.16 Footnotes]]

Next: [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16.01 Purpose|V2-16.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/16_responsible_ai/16_responsible_ai.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/16_responsible_ai/16_responsible_ai.html#sec-responsible-ai). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Responsible AI/Contestability and Recourse|Contestability and Recourse]]
- [[02 Concepts/Qualities/Responsible AI/Fairness Criteria|Fairness Criteria]]
- [[02 Concepts/Qualities/Responsible AI/Fairness Criteria Incompatibility|Fairness Criteria Incompatibility]]
- [[02 Concepts/Qualities/Safety & Assurance/Safety Case|Safety Case]]

## Related Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; Fleet stack; Governance as the fleet control plane.
- [[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training|V2-06 Distributed Training]] — Alignment training co-location.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Overload containment.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — Participation selection.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Evaluation contract; Dependency-aware registry; Hierarchical fleet alerting.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy|V2-13 Security & Privacy]] — Privacy techniques by excluded observer; Differential privacy; Privacy budget account; Leakage through authorized outputs.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Adversarial robustness for a named threat model; Shift taxonomy; Per-request competence contract.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI|V2-15 Sustainable AI]] — Sustainability measurement contract.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/16_responsible_ai/responsible_ai_concepts.yml)

<!-- Semantic Navigation: End -->
