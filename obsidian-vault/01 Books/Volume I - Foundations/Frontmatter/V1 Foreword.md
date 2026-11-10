---
title: V1 Foreword
type: Frontmatter
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/frontmatter/foreword.qmd
source_anchor: foreword
source_mode: Source-Correlated Published HTML
tags:
- Type/Frontmatter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/frontmatter/foreword.html
---

# V1 Foreword

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^foreword

**David A. Patterson**\
Pardee Professor of Computer Science Emeritus\
University of California, Berkeley\
Distinguished Engineer, Google\
ACM A.M. Turing Award Laureate\
Berkeley, California

My career has been dedicated to understanding and improving the very foundations upon which computing operates – from the instruction set architectures that define processors to the storage systems that hold our data. I’ve seen firsthand how profound advancements are rarely about a single brilliant idea in isolation, but rather about the holistic integration of many ideas into a robust, efficient, and reliable system.

Today, we stand at another pivotal moment. Machine learning (ML) has transcended scientific curiosity to become a force reshaping industries, driving innovation, and transforming our daily lives. The intellectual power of the algorithms, the gains in accuracy, and the seemingly magical capabilities they unlock have rightly captured the world’s imagination.

One concern is that much of this progress has been achieved by a community that, through no fault of its own, was never taught to think in systems terms about what it was building. Engineers who can call `model.fit()` but cannot explain why training is slow. Researchers who tune hyperparameters without understanding the memory bandwidth constraints that make certain choices impractical. Practitioners who deploy models into production without a framework for reasoning about latency, throughput, or failure modes.

A brilliant algorithm, without a well-engineered system to support it, is like a powerful engine without a chassis and brakes. It won’t get you far, and it certainly won’t get you there reliably.

This gap is not a talent deficit. It is a curriculum deficit. The field has simply not had the textbooks it deserves. This book, *Introduction to Machine Learning Systems*, arrives precisely at the right time to illuminate this critical, often overlooked, dimension of the ML revolution.

## Why Systems Thinking Matters

^why-systems-thinking-matters

My career has leveraged the power of systems thinking. Identify the bottlenecks, understand the interactions between components, and design for performance, reliability, cost-effectiveness, and ease of use across the entire stack. You could not reach the conclusion from first principles alone. You had to think about the system.

ML systems demand exactly the same discipline. A neural network is not a mathematical abstraction floating free of physical constraints. It is a computation that must execute on silicon with finite memory bandwidth, finite power budgets, and finite communication capacity. Arithmetic intensity, the Roofline Model, and memory hierarchy effects are not advanced topics to be addressed after students learn the basics. They are the basics.

## Why ML Systems Deserve Serious Textbook Treatment

^why-ml-systems-deserve-serious-textbook-treatment

The purpose of a textbook is not just to catalog the current frontier. It is to provide the conceptual scaffolding that allows students to understand the frontier, and to advance it themselves. The neural network architectures covered in these pages will evolve. The hardware accelerators described will be superseded. But some fundamentals will not change. We will still have memory hierarchies and arithmetic intensity will still be a critical measure. The principles of pipelining, of latency versus throughput trade-offs, of quantization and precision reflect physical and mathematical realities that do not go out of date. Anyone who genuinely understands them will be able to reason about whatever new system the field produces next year or ten years from now.

I am also struck by the scope of what this book attempts. It is not enough to explain how training works; one must also address data engineering, model optimization, hardware acceleration, deployment, benchmarking, responsible AI, and sustainability. These are not separate topics bolted together for completeness. They are interconnected aspects of a single engineering discipline. A decision made at the data layer has implications for model behavior, which has implications for inference latency, which has implications for deployment cost, which has implications for the communities that can and cannot access the resulting system. The book correctly treats this integration as a first-class concern.

I am particularly pleased to see the quantitative methodology that runs through every chapter. Claims are backed by measurements. Trade-offs are expressed numerically. Students are taught to estimate, measure, and verify rather than to rely on their gut. The difference between an engineer and a dilettante is precisely this capacity for rigorous, measurement-grounded reasoning.

## Why Open Access Is Important for the Next Generation

^why-open-access-is-important-for-the-next-generation

I applaud the decision to make this invaluable resource freely available.

When I co-wrote *Computer Architecture: A Quantitative Approach* with John Hennessy, we debated how to make the material as accessible as possible. We lobbied our publisher to keep the price down and even came out with a low cost international student edition for sales outside North America. Those concerns have only grown more urgent as ML has become infrastructure—as consequential to the modern world as the electrical grid or the internet.

The decision to publish this book as a freely available educational resource is not a compromise. It is a statement of values. ML systems are being deployed in every sector of every economy on every continent. The engineers who build and maintain them will come from everywhere. If the foundational education required to do this work responsibly is available only to students at well-resourced institutions, we will contribute to an expertise gap that mirrors the societal concerns of who benefits from AI and who bears its costs.

What impresses me further is that this project has gone well beyond open access to a static text. The accompanying ecosystem—interactive laboratories, a build-from-scratch framework in TinyTorch, hardware deployment kits, instructor materials, a global network of adopting universities—reflects a familiar educational maxim: “I hear and I forget. I see and I remember. I do and I understand.”

The open-source model also makes the curriculum itself better. Errors get corrected. Examples get sharpened. New chapters emerge in response to what the field actually needs. As we found with *Computer Architecture: A Quantitative Approach*, a community of contributors that forms around a book can offer a form of quality assurance that no single author team, however expert, can match alone.

## A Final Word

^a-final-word

The field of computer architecture has a tradition I am proud of: we build things, measure them honestly, share what we learn, and revise our philosophies when the measurements demand it. We do not hide behind the complexity of our systems to avoid accountability for whether they actually work. We do not conflate novelty with progress. We debate, rigorously, about what matters and why.

Hopefully, ML systems engineering will follow this tradition. It needs the habits of mind that come from taking systems seriously: thinking about interactions, measuring at the right level of abstraction, being honest about trade-offs, and holding oneself accountable to real-world performance rather than benchmark folklore. This book embodies those habits.

*Introduction to Machine Learning Systems* is more than just a textbook; it is a clarion call for systems thinking in the age of AI, a guide for building robust ML applications, and a testament to the power of open education.

We are at an extraordinary moment. Over my career there has been a major breakthrough every decade: the microprocessor in the 1970s, the personal computer in the 1980s, the Internet in the 1990s, the smartphone in the 2000s, and AI in the 2010s. The first four changed business and society, yet AI looks likely to have the largest impact of them all.

The systems being built today will shape how intelligence is deployed, who benefits from it, and what it costs—in money, in energy, and in carbon footprint. We need the engineers who build those systems to have the best possible systems skills.

This book is a significant step toward making it possible for anyone to learn them.

David A. Patterson

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/frontmatter/foreword.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/frontmatter/foreword.html#foreword). Rendering provenance is recorded in the import manifest.
