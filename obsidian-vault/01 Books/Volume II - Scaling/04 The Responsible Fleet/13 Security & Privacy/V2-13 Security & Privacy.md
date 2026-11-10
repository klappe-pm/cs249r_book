---
title: V2-13 Security & Privacy
type: Chapter
volume: 2
chapter: 13
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/13_security_privacy/13_security_privacy.qmd
source_anchor: sec-security-privacy
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/13_security_privacy/13_security_privacy.html
---

# V2-13 Security & Privacy

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-security-privacy

[Lecture slides](https://mlsysbook.ai/slides/vol2.html#ch-13) for this chapter

![[90 Assets/Volume II/13 Security Privacy/Cover Security Privacy Blueprint Labeled e184aca419.webp]]

*Security and privacy boundary chamber separating data, model weights, runtime, users, and audit logs into protected and untrusted zones.*

## Chapter Sections

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.01 Purpose|V2-13.01 Purpose]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.02 The Expanded Attack Surface|V2-13.02 The Expanded Attack Surface]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.03 Security and Privacy Foundations|V2-13.03 Security and Privacy Foundations]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.04 Learning from Security Breaches|V2-13.04 Learning from Security Breaches]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.05 Systematic Threat Analysis and Risk Assessment|V2-13.05 Systematic Threat Analysis and Risk Assessment]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.06 Model-Specific Attack Vectors|V2-13.06 Model-Specific Attack Vectors]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.07 Fleet-Internal Trust Boundaries|V2-13.07 Fleet-Internal Trust Boundaries]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.08 Hardware-Level Security Vulnerabilities|V2-13.08 Hardware-Level Security Vulnerabilities]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.09 Comprehensive Defense Architectures|V2-13.09 Comprehensive Defense Architectures]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.10 Differential Privacy|V2-13.10 Differential Privacy]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.11 Selecting and Sequencing Defenses|V2-13.11 Selecting and Sequencing Defenses]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.12 Fallacies and Pitfalls|V2-13.12 Fallacies and Pitfalls]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.13 Summary|V2-13.13 Summary]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.14 Self-Check Answers|V2-13.14 Self-Check Answers]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.15 Source References|V2-13.15 Source References]]
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.16 Footnotes|V2-13.16 Footnotes]]

Next: [[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13.01 Purpose|V2-13.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/13_security_privacy/13_security_privacy.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/13_security_privacy/13_security_privacy.html#sec-security-privacy). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Security & Privacy/Data Poisoning|Data Poisoning]]
- [[02 Concepts/Qualities/Security & Privacy/Differential Privacy|Differential Privacy]]
- [[02 Concepts/Qualities/Security & Privacy/DP SGD|DP SGD]]

## Related Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/00 Introduction/01 Introduction/V2-01 Introduction|V2-01 Introduction]] — Fleet Law; C3 taxonomy; Fleet stack; Governance as the fleet control plane.
- [[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics|V2-03 Network Fabrics]] — RDMA reliable-delivery contract.
- [[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication|V2-05 Collective Communication]] — Ring AllReduce and the bandwidth bound; Gradient compression with error feedback.
- [[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance|V2-07 Fault Tolerance]] — Silent data corruption verification; Young-Daly checkpoint interval.
- [[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration|V2-08 Fleet Orchestration]] — Serving envelope and accelerator sharing.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale|V2-10 Serving at Scale]] — Overload containment.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence|V2-11 Edge Intelligence]] — FedAvg under sampling and non-IID data; Secure aggregation.
- [[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale|V2-12 ML Operations at Scale]] — Staged rollout exposure budget; ML platform as a product.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/13_security_privacy/security_privacy_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI|V2-14 Robust AI]] — Adversarial transferability; Adversarial robustness for a named threat model; Layered poisoning defense; Shift taxonomy.
- [[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI|V2-16 Responsible AI]] — Assurance case.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/13_security_privacy/security_privacy_concepts.yml)

<!-- Semantic Navigation: End -->
