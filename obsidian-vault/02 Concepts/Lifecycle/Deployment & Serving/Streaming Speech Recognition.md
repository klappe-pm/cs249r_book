---
title: Streaming Speech Recognition
type: concept
tags:
- Type/Concept
- Group/Lifecycle
- Topic/Serving_Architectures
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Streaming speech recognition
taxonomy_id: mlsys.streaming-asr
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Streaming Speech Recognition

Serving speech recognition incrementally: consuming audio in chunks and emitting partial transcripts within a fixed lag, with encoder state carried between chunks.

## Browsing Home

[[02 Concepts/Lifecycle/Deployment & Serving/Serving Architectures Subject|Serving Architectures]] → [[02 Concepts/Lifecycle/Deployment & Serving/Deployment & Serving Index|Deployment & Serving]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is the input stage of [[02 Concepts/Lifecycle/Deployment & Serving/Voice Interaction Pipeline|Voice Interaction Pipeline]]. **Condition:** Cascaded designs that transcribe speech before the language model.

- Runs in [[02 Concepts/Lifecycle/Deployment & Serving/On Device Inference Runtime|On Device Inference Runtime]]. **Condition:** On-device recognizers for privacy and latency.

- Is streaming inference over audio [[02 Concepts/Lifecycle/Deployment & Serving/Streaming Inference|Streaming Inference]]. **Condition:** Audio arrives in chunks and partial transcripts are emitted before the utterance ends.

## Search Terms

Upstream search terms may be related terms rather than exact synonyms: streaming ASR; on-device speech recognition.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
