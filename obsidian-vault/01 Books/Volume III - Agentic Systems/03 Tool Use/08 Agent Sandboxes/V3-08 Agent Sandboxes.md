---
title: V3-08 Agent Sandboxes
type: Chapter
volume: 3
chapter: 8
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/08_sandboxes/08_sandboxes.qmd
source_anchor: sec-vol3-sandboxes
source_mode: Source-Correlated Published HTML
tags:
- Type/Chapter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/08_sandboxes/08_sandboxes.html
---

# V3-08 Agent Sandboxes

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-sandboxes

[Lecture slides](https://mlsysbook.ai/slides/vol3.html#ch-08) for this chapter

![[90 Assets/Volume III/08 Sandboxes/Cover Virtualization Blueprint Labeled 174499cf75.webp]]

*Blueprint for Agent Sandboxes.*

## Chapter Sections

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.01 Purpose|V3-08.01 Purpose]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.02 The Reach of Admitted Code|V3-08.02 The Reach of Admitted Code]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.03 The Agent Threat Model|V3-08.03 The Agent Threat Model]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.04 Limits of In-Process Restriction|V3-08.04 Limits of In-Process Restriction]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials|V3-08.05 Capabilities and Credentials]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.06 Choosing an Isolation Envelope|V3-08.06 Choosing an Isolation Envelope]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.07 The Agent Workspace|V3-08.07 The Agent Workspace]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.08 Egress Control|V3-08.08 Egress Control]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.09 Sandbox Pools and Reset|V3-08.09 Sandbox Pools and Reset]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.10 Fallacies and Pitfalls|V3-08.10 Fallacies and Pitfalls]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.11 Summary|V3-08.11 Summary]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.12 Historical Perspective and Further Reading|V3-08.12 Historical Perspective and Further Reading]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.13 Exercises|V3-08.13 Exercises]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.14 Source References|V3-08.14 Source References]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.15 Footnotes|V3-08.15 Footnotes]]

Next: [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.01 Purpose|V3-08.01 Purpose]]

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/08_sandboxes.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/08_sandboxes/08_sandboxes.html#sec-vol3-sandboxes). Rendering provenance is recorded in the import manifest.

<!-- Semantic Navigation: Begin -->

## Connected Concepts

Explicit upstream passage alignments:

- [[02 Concepts/Qualities/Security & Privacy/Authorization|Authorization]]
- [[02 Concepts/Qualities/Security & Privacy/Capability Based Authorization|Capability Based Authorization]]
- [[02 Concepts/Qualities/Security & Privacy/Execution Isolation|Execution Isolation]]
- [[02 Concepts/Qualities/Security & Privacy/Network Egress Control|Network Egress Control]]

## Related Themes

- [[03 Themes/Security and Trust|Security and Trust]]

## Earlier Connections

The source concept map records these touches connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction|V3-01 Introduction]] — Side-effect classes; Zero ambient authority; Invariant closure; Lighthouse workloads; Cost per accepted task; Horizon compounding.
- [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management|V3-05 KV Cache Management]] — Little's law.
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling|V3-07 Tool Calling]] — Complete mediation; Confused deputy; Action-time preconditions; Settlement before retry; Acknowledgment is not completion.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/sandboxes_concepts.yml)

## Continuing Connections

The source concept map records these previews connections. They are reading connections, not prerequisite requirements.

- [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security|V3-09 Agent Security]] — Structural prompt injection; Lethal trifecta; Security outcome measurement; Information-flow labels.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution|V3-11 Durable Execution]] — Checkpoint binding.
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation|V3-13 Agent Evaluation]] — Grader isolation; Task sampling and score intervals.
- [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17 Reinforcement Learning from Verifiable Rewards|V3-17 Reinforcement Learning from Verifiable Rewards]] — Faithful rollout records.

[Chapter Concept Map](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/08_sandboxes/sandboxes_concepts.yml)

<!-- Semantic Navigation: End -->
