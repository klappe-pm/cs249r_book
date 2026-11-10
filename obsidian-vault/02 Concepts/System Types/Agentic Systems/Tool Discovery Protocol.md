---
title: Tool Discovery Protocol
type: concept
tags:
- Type/Concept
- Group/System_Types
- Topic/Tool_Use_Action_Interfaces
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Tool discovery protocol
taxonomy_id: mlsys.model-context-protocol
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Tool Discovery Protocol

A shared client-server interface through which agent hosts discover the tools, resources, and prompts external services expose, with their schemas, reducing custom integration.

## Browsing Home

[[02 Concepts/System Types/Agentic Systems/Tool Use & Action Interfaces Subject|Tool Use & Action Interfaces]] → [[02 Concepts/System Types/Agentic Systems/Agentic Systems Index|Agentic Systems]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Standardizes tool discovery for [[02 Concepts/System Types/Agentic Systems/Function Calling|Function Calling]]. **Condition:** Discovering a tool through a protocol does not grant authority to use it.

- Widens the surface for [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** When tool descriptions and results from third-party servers enter the model's context as if trusted.

- Uses [[02 Concepts/Qualities/Security & Privacy/Authorization|Authorization]]. **Condition:** When servers require scoped, delegated credentials before exposing tools or resources.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: Model Context Protocol; MCP.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
