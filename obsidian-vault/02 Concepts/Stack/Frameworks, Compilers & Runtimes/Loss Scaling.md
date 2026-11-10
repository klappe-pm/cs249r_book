---
title: Loss Scaling
type: concept
tags:
- Type/Concept
- Group/Stack
- Topic/Numerical_Formats_Precision
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
source_label: Loss scaling
taxonomy_id: mlsys.loss-scaling
taxonomy_status: draft
taxonomy_version: 0.4-draft
---

# Loss Scaling

Multiplying the loss before backpropagation so small gradients remain representable in reduced-precision formats, then unscaling before the optimizer step.

## Browsing Home

[[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Formats & Precision Subject|Numerical Formats & Precision]] → [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Frameworks, Compilers & Runtimes Index|Frameworks, Compilers & Runtimes]]

## Book Passages

These are explicitly recorded related passages from the upstream draft alignment; they do not certify complete coverage.

No explicit passage alignment is recorded for this concept. Subject reading pointers are available in its browsing home.

## Conditional Relationships

These are the taxonomy's draft editorial relationships. Read each relationship with its condition; an outgoing link is not a prerequisite claim.

- Is a component of [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Mixed Precision Training|Mixed Precision Training]]. **Condition:** Gradients would otherwise underflow in the reduced-precision format.

- Keeps small gradients representable, improving [[02 Concepts/Stack/Frameworks, Compilers & Runtimes/Numerical Stability|Numerical Stability]]. **Condition:** Reduced-precision gradient formats would otherwise underflow; overflow is detected and the step skipped.

- Keeps small gradients representable to limit [[02 Concepts/Lifecycle/Training & Adaptation/Training Instability|Training Instability]]. **Condition:** When low-precision gradients would otherwise underflow to zero or overflow to infinity.

## Source

[Canonical Taxonomy](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/taxonomy.yml) · [Passage Alignment](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/taxonomy/mlsysbook-alignment.yml)

Taxonomy definitions and relationship wording: CC BY 4.0, with attribution to the Machine Learning Systems curriculum by Vijay Janapa Reddi and contributors. The textbook retains its separate license.
