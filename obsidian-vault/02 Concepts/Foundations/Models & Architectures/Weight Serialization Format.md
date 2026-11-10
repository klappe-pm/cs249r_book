---
title: Weight Serialization Format
type: concept
tags:
- Type/Concept
- Group/Foundations
- Topic/Model_Artifacts_Formats
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Weight serialization format
taxonomy_id: mlsys.weight-serialization
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Weight Serialization Format

The on-disk encoding of a model's parameter tensors and metadata, governing load time, memory mapping, and safety of deserialization.

## Browsing Home

[[02 Concepts/Foundations/Models & Architectures/Model Artifacts & Formats Subject|Model Artifacts & Formats]] → [[02 Concepts/Foundations/Models & Architectures/Models & Architectures Index|Models & Architectures]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Persists the parameters of [[02 Concepts/Foundations/Models & Architectures/Model Artifact|Model Artifact]]. **Condition:** The artifact's weights are persisted for later loading.

- Determines exposure to [[02 Concepts/Qualities/Security & Privacy/Unsafe Model Deserialization|Unsafe Model Deserialization]]. **Condition:** Executable formats such as pickle run code on load; data-only formats such as safetensors do not.

- Sets weight-loading time in [[02 Concepts/Lifecycle/Deployment & Serving/Model Cold Start|Model Cold Start]]. **Condition:** Memory-mappable, zero-copy formats load faster than formats requiring full deserialization.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: safetensors; GGUF; pickle-based weights.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
