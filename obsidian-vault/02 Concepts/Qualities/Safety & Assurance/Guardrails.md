---
title: Guardrails
type: concept
tags:
- Type/Concept
- Group/Qualities
- Topic/Runtime_Assurance_Safety_Filters
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Guardrails
taxonomy_id: mlsys.guardrails
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Guardrails

Runtime checks on model inputs and outputs that detect and block, rewrite, or escalate content or actions violating a stated safety policy.

## Browsing Home

[[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance & Safety Filters Subject|Runtime Assurance & Safety Filters]] → [[02 Concepts/Qualities/Safety & Assurance/Safety & Assurance Index|Safety & Assurance]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Partially detects [[02 Concepts/Qualities/Security & Privacy/Prompt Injection|Prompt Injection]]. **Condition:** Classifier guardrails are probabilistic and can be evaded, so they do not replace authority boundaries.

- Is a content-level form of [[02 Concepts/Qualities/Safety & Assurance/Runtime Assurance|Runtime Assurance]]. **Condition:** Applies when the safe set is a content or action policy rather than a physical state region.

- Partially mitigates [[02 Concepts/Qualities/Security & Privacy/Jailbreak|Jailbreak]]. **Condition:** Input and output classifiers catch known patterns but can be evaded by novel or obfuscated prompts.

- Produces [[02 Concepts/Qualities/Safety & Assurance/Over Refusal|Over Refusal]]. **Condition:** When a safety check or refusal policy incorrectly blocks a benign request.

- Adds classifier passes on the request path to [[02 Concepts/Lifecycle/Deployment & Serving/Tail Latency|Tail Latency]]. **Condition:** When input and output checks run synchronously before the response is released; streaming output checks shift the cost to time-to-last-token.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: content safety filter; safety classifier.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
