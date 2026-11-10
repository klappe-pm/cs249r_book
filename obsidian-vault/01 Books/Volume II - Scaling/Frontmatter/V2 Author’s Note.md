---
title: V2 Author’s Note
type: Frontmatter
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/frontmatter/author_note.qmd
source_anchor: authors-note
source_mode: Source-Correlated Published HTML
tags:
- Type/Frontmatter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/frontmatter/author_note.html
---

# V2 Author’s Note

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^authors-note

When a new model is announced, the world looks at the model. It almost never looks at the fleet.

Behind many frontier models, however, stand thousands of accelerators held in lockstep across a network where one slow link can stall the whole run, cooled by systems that move megawatts of heat, kept alive by protocols that treat failure not as an exception but as a scheduled event. None of this fits in the announcement. The model gets the paper. The fleet gets a footnote, if that.

This book is an argument that the fleet deserves more than a footnote. We have built vast distributed systems before, but none quite like this one, because none of the others had to be right about two things at once. The telephone network had to stay available; it never had to converge. The internet had to deliver the packet; it never had to preserve the gradient inside it. A fleet has to do both. It must move data the way any distributed system does, and it must keep the mathematics of learning intact while it moves. A node that drops out does not only cost capacity; it can break the synchronization a training step depends on and force a rollback that wastes work since the most recent checkpoint. That double obligation, computational and statistical, sustained at the scale of a small campus, is the engineering this book makes visible.

The obligation does not end when training does. A model that cannot be trained is an idea, not a system. A model that cannot be served is a research result, not a product. A model that cannot be governed is a liability, not an asset. At every stage, from the first allocated node to the last served request, the fleet decides what is possible and what remains imagined.

The problem under every chapter is easy to state and hard to solve: what it takes to build not one machine learning system but a thousand, make them work as one, and run them responsibly. I believe that is a defining engineering problem of this generation, and that the people who take it on, the ones who rarely get the headline, deserve a book that treats it as one.

— Vijay Janapa Reddi\
Cambridge, Massachusetts\
2026

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/frontmatter/author_note.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/frontmatter/author_note.html#authors-note). Rendering provenance is recorded in the import manifest.
