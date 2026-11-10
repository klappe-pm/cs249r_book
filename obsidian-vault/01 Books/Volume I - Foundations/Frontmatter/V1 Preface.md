---
title: V1 Preface
type: Frontmatter
volume: 1
chapter: 0
publication_status: Released
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol1/frontmatter/about.qmd
source_anchor: sec-about
source_mode: Source-Correlated Published HTML
tags:
- Type/Frontmatter
- Book/Volume_1
rendered_source_url: https://mlsysbook.ai/vol1/frontmatter/about.html
---

# V1 Preface

[[Home|Home]] · [[01 Books/Volume I - Foundations/Volume 1 Overview|Volume Overview]]

^sec-about

## Who This Book Is For

^sec-book-book-74a2

A model that trains cleanly in a research notebook can still run out of memory on a server, miss its latency budget under live traffic, or cost ten times more to serve than the application can afford. Most readers will not become hardware architects or compiler writers, yet every practitioner who builds, trains, optimizes, or deploys a model makes choices whose outcome depends on the system beneath the code.

This book explains *how* machine learning systems work, from the mathematics that define a neural network to the hardware that runs it and the engineering trade-offs that make it fast and reliable. It builds that foundation for engineers meeting ML systems for the first time, practicing engineers who want to understand what happens below the framework API, and researchers who need to reason about runtime, memory, and deployment.

## Prerequisites

^sec-book-prerequisites-1a4b

Readers should bring two prerequisites:

- **Programming**: Fluency in Python, including functions, classes, and basic array manipulation with NumPy.
- **Mathematics**: Comfort with linear algebra, basic calculus, and probability at the introductory university level.

Two additional areas help but are not required:

- **Computer systems**: Prior familiarity with caches, memory bandwidth, and processor organization is useful, though the optimization and hardware chapters build every physical mechanism from first principles.
- **Machine learning basics**: Prior exposure to supervised learning gives helpful context, though Part II develops the required modeling foundations from the ground up.

Because the book derives both the hardware mechanisms and the modeling foundations from first principles, readers with Python and undergraduate mathematics can follow every quantitative argument end to end.

## Why a Systems Textbook

^sec-book-systems-textbook-76ff

In 1968, a NATO conference in Garmisch, Germany, helped establish *software engineering* as a distinct discipline amid concern that software systems had grown too complex for ad hoc programming ([[01 Books/Volume I - Foundations/Frontmatter/V1 Preface#^ref-naur1969softwareengineering|Naur and Randell 1969]]). Reliable software required its own principles, methods, and rigor. Decades later, Hennessy and Patterson put quantitative analysis at the center of computer architecture education, giving engineers a shared way to measure, predict, and improve processor performance ([[01 Books/Volume I - Foundations/Frontmatter/V1 Preface#^ref-patterson2017hardware|Hennessy and Patterson 2017]]). Both moments turned a craft of rules of thumb into a teachable engineering discipline.

Machine learning faces its own Garmisch moment. Computer science studies what is computable, and ML research studies what is learnable; AI engineering studies what is buildable given the physics of real hardware and real data. For the past decade, ML education has been dominated by *model-centric* thinking focused on discovering new algorithms and architectures. Yet an accurate model fails in practice if its data pipeline cannot keep accelerators fed, if its serving path misses its latency deadline, or if its energy bill exceeds the value of its predictions. I wrote this book to help close that gap by replacing guesswork with measurement and folklore with quantitative engineering principles.

Consider a box of LEGO bricks. The same interlocking pieces build a spaceship, a castle, or an entire city. The sets change; the bricks do not. ML systems work the same way. A convolutional network for image classification, a transformer for language generation, and a reinforcement learning agent for robotics serve different applications, yet beneath all of them sit the same building blocks: computational graphs, memory hierarchies, data pipelines, training loops, and the trade-offs among latency, throughput, and energy. Dominant frameworks have shifted from Theano to TensorFlow to PyTorch in under a decade, and hardware has evolved from repurposed graphics processors to purpose-built tensor accelerators, with new architectures arriving every year. Because software stacks and chips turn over so quickly, tool-specific advice ages fast, whereas an engineer who understands the underlying building blocks can reason about any system the field produces.

This book therefore treats ML systems engineering as a discipline built on quantitative bounds, cost models, and design principles rather than as a catalog of tools such as Kubernetes, PyTorch, and CUDA. Just as civil engineers calculate loads before choosing materials, ML systems engineers need explicit laws that reveal which resource limits performance before they rewrite code. Four ideas anchor this book:

- **The D·A·M taxonomy**: Every bottleneck lives in the data, the algorithm, or the machine, and relieving one can expose another.
- **The iron law of ML systems**: Across the D·A·M axes, workload time factors as $(\text{Samples/Task}) \times (\text{FLOPs/Sample}) \times (\text{Seconds/FLOP})$ and unpacks on hardware into data movement, computation, and overhead. Where stages run concurrently (such as transferring the next batch while computing the current one), the critical path governs elapsed time.
- **The bitter lesson**: General methods that exploit growing computation outpace hand-encoded expertise, which makes systems efficiency a lever of progress.
- **The energy-movement principle**: Fetching a value from off-chip memory can cost far more energy than computing with it, so per-event costs and event counts determine whether movement or computation dominates.

Each part adds its own governing principles, such as data gravity and Amdahl’s law, at the point where they first constrain a design. Together, the volume-wide anchors and part-level laws form a compact analytical toolkit that carries across every chapter.

## What This Book Covers

^sec-book-book-covers-180b

An engineer cannot diagnose why a thousand-GPU training cluster is stalling without first knowing how a single machine moves tensors through memory, feeds its data pipeline, and keeps its execution units busy. Even the largest warehouse-scale cluster is built out of individual compute nodes. This book therefore centers on the *single compute node*: one host with one to eight accelerators, each with its own discrete memory connected over a local link such as PCIe or NVLink. Multi-node execution enters only where it shapes single-node design; the distributed communication, scheduling, and fault-recovery problems that arise across a fleet build directly on the single-node foundations developed here.

The book is organized into four parts. Each part answers one question and hands the next part a concrete result:

- **Part I: Foundations of ML Systems** asks what is being built, under which constraints, and from what inputs. It develops the vocabulary, cost models, and end-to-end workflow that guide every ML project, from the traits that distinguish ML systems from traditional software to the data pipelines that feed them. It hands forward a design envelope and trustworthy data.
- **Part II: Development and Training** asks how a model computes, how it is structured, and how it learns. It connects mathematical foundations to working software and hardware through neural network computation, model architectures, execution frameworks, and training loops. It hands forward a trained model whose memory, compute, and wall-clock costs are known.
- **Part III: Optimization and Acceleration** asks how to make that model cheaper to train or serve and how to prove the gain. Its chapters follow the D·A·M taxonomy in order: data selection cuts the samples a run must process, model compression shrinks the algorithm, hardware acceleration maps the remaining work onto the machine, and benchmarking tests whether the speedup holds up under honest measurement. It hands forward verified evidence for a deployment decision.
- **Part IV: Deployment and Operations** asks whether the system survives real users, shifting data, and its obligations to society. It covers serving infrastructure, production monitoring and retraining, and the engineering controls needed to keep deployed systems fair, safe, and accountable. It hands forward the tools to run and defend a system in production.

An opening introduction frames this book through the D·A·M triad and the iron law, and a concluding synthesis brings the four parts back together into a coupled-budget methodology. Across all sixteen chapters, the progression follows a single system through its life, from problem formulation and data engineering through model construction, training, optimization, benchmarking, deployment, and operations, so readers can either traverse the full sequence or target the stages that match their immediate goals.

## Suggested Reading Paths

^sec-book-suggested-reading-paths-773b

Reading the chapters in order gives the most complete foundation, because each part hands a concrete artifact and cost model to the next. Readers coming in with specific goals can take a more focused route:

- **The Complete Path** (all chapters, in order): For engineers and researchers new to ML systems. Start with **[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01 Introduction#^sec-introduction|Introduction]]**, then read the four parts in sequence. This path builds every concept from first principles.
- **The ML Engineer’s Path** (systems depth for practitioners): For engineers who already train and deploy models in Python but want to understand what happens underneath the framework API. Skim Part I for shared vocabulary, then focus on **[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07 ML Frameworks#^sec-ml-frameworks|ML Frameworks]]**, **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training#^sec-model-training|Model Training]]**, **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration#^sec-hardware-acceleration|Hardware Acceleration]]**, **[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12 Benchmarking#^sec-benchmarking|Benchmarking]]**, and **[[01 Books/Volume I - Foundations/04 Deployment/13 Model Serving/V1-13 Model Serving#^sec-model-serving|Model Serving]]**.
- **The Optimization Path** (efficiency-focused): For engineers working on model compression, kernel performance, edge deployment, or tight latency budgets. After Part I, review Part II’s account of forward and backward passes, architecture costs, framework execution, and training bottlenecks before diving into Part III.

Whichever path a reader takes, [[01 Books/Volume I - Foundations/Frontmatter/V1 Preface#^fig-vol1-chapter-dependencies|figure P.1]] shows which earlier chapters each chapter depends on. Readers who already know a prerequisite topic can skip ahead; others can follow the incoming arrows back to fill in the background. Model training sits at the center of the map, drawing on both data engineering and ML frameworks while feeding both data selection and model compression. The longest dependency chain runs through Part III, where model compression feeds hardware acceleration and benchmarking closes the loop before deployment.

![[90 Assets/Volume I/Shared Figures/Chapter Dependency Map 5957362f83.svg]]

Figure P.1: **Chapter Dependency Map**: Each arrow points from a chapter to a later chapter that builds on its results, derived from the book’s cross-references with transitive links omitted. The introduction frames every chapter; the arrow from it marks the chapter that draws on it directly.

^fig-vol1-chapter-dependencies

## How to Read This Book

^sec-book-how-to-read-9d2e

The parts follow the lifecycle of a model rather than climbing the ML systems stack from the bottom, so each chapter touches several layers of that stack at once. The stack is modeled on the classical computer systems hierarchy. Each layer provides an interface to the layer above and builds on the layer below, from hardware at the bottom through frameworks, models, training, and serving, up to operations and applications at the top. Data runs alongside every layer like a system bus. Throughout the book, a recurring margin figure highlights which layers each chapter addresses:

![[90 Assets/Volume I/Shared Figures/ML Systems Stack 4b3d5b2a4f.svg]]

*Seven-layer ML systems stack: hardware, frameworks, models, training, serving, operations, and applications. A uniformly shaded data bar connects to every layer.*

The vertical data bar alongside the stack tracks a separate dimension from the horizontal layers. Its uniform shading reflects how central data is to the chapter as a whole, and the connecting wires mark which layers interact with data directly in that chapter’s context. Three chapters show how this profile shifts across the book:

![[90 Assets/Volume I/Shared Figures/Stack Hardware Acceleration 83a8c3202e.svg]]

*Hardware acceleration stack: hardware has the strongest shading, applications and operations are inactive, and the data bar is faint.*

HW Acceleration

![[90 Assets/Volume I/Shared Figures/Stack Training 8ebaf474dc.svg]]

*Training stack: training has the strongest shading, models, frameworks, and hardware are also emphasized, and the data bar has a moderate tint.*

Training

![[90 Assets/Volume I/Shared Figures/Stack Responsible Engineering 08b25c44f7.svg]]

*Responsible engineering stack: applications and operations have the strongest shading, hardware and frameworks are inactive, and the data bar has a moderate tint.*

Responsible Engr.

In **[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11 Hardware Acceleration#^sec-hardware-acceleration|Hardware Acceleration]]**, the layer intensity concentrates at the bottom of the stack while the data bar is faint: the chapter focuses on hardware mechanisms rather than dataset construction. In **[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08 Model Training#^sec-model-training|Model Training]]**, the middle layers glow and the data bar is moderately lit, reflecting that training consumes data but is about optimization. In **[[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15 Responsible Engineering#^sec-responsible-engineering|Responsible Engineering]]**, the top layers dominate and the data bar carries a moderate tint, because biased training data surfaces as biased applications even though several layers sit between them. The same stack tells three different stories, with data as an independent dimension.

The margins also carry small visual notes at the point where a relationship is easiest to understand by sight. These are not numbered figures to cite later; they are reading aids. A ladder makes an energy or latency scale gap visible, and a trend sketch shows direction. A roofline thumbnail shows whether memory bandwidth or compute throughput bounds performance, and a dominance bar shows which term controls total runtime. When a miniature uses a log scale, it says so inside the image.

![[90 Assets/Volume I/Shared Figures/Hw Acceleration Energy Ladder 7d22ba1797.svg]]

*Margin visual example: three horizontal orange bars on a log scale compare DRAM access at 640 pJ, FP32 multiplication at 3.7 pJ, and SRAM access at 0.5 pJ.*

![[90 Assets/Volume I/Shared Figures/Data Engineering Debt Compounding 9fccce6a5f.svg]]

*Margin visual example: two rising curves showing data debt diverging as the accumulation rate increases.*

![[90 Assets/Volume I/Shared Figures/Vol1 Benchmarking Margin 002 14cb326b13.svg]]

*Margin visual example: a roofline thumbnail showing a batch-size operating point moving toward the compute roof.*

![[90 Assets/Volume I/Shared Figures/Vol1 Benchmarking Margin 001 ca3d30ea35.svg]]

*Margin visual example: two stacked latency bars showing that component speedup only partly improves end-to-end latency.*

Alongside these visual notes, unnumbered **marginal navigation pointers** connect an idea to the chapter that establishes it or builds on it, without interrupting the prose:

- **`↩︎` Backward pointer:** Directs the reader back to the earlier chapter where a principle, constraint, or cost model was established.
- **`↪` Forward pointer:** Directs the reader ahead to the later chapter, or to the appendix, where the current idea is developed, measured, or enforced.
- **`⇄` Contrast:** Marks a place where two chapters treat the same problem differently, so the comparison is visible at a glance.

A pointer only orients; when a sentence depends on another chapter, the reference stays in the text. Together, the stack diagrams, miniature plots, and marginal pointers keep the system context visible in the margins, while a matching set of typographic and callout conventions organizes the main text.

## Conventions

^sec-about-conventions-1a2b

This book uses a small set of typographic and structural conventions so the reader can tell at a glance whether a passage is defining a term, stating a physical limit, or working through a quantitative example.

### Bold Marks First Definitions

^sec-about-bold-3c4d

A term in **bold** within body prose is its formal first introduction in the volume. Each term receives this treatment exactly once. Subsequent appearances are unbolded; by then the term is part of the working vocabulary the chapter carries forward.

> Every machine learning system has a **dual mandate**: it must manage statistical uncertainty and physical constraints simultaneously.

A matching index entry in the back of the book points to that defining occurrence (under the `definition` subentry), providing a direct way to return to it, and key technical terms are also compiled in the glossary.

Bold also appears in a second, structural role: as a functional label at the start of an item inside a callout box or a summary bullet, such as **Recommendation**, **Trade-off**, or **Result**. In that context, the bold is scaffolding rather than a first definition.

### Italics Carry Specific Rhetorical Jobs

^sec-about-italics-5e6f

Italics serve specific purposes rather than general emphasis. Common uses include:

- **Direct opposition**: *training* vs. *inference*, *logical* vs. *physical*.
- **Impossibility, stated as physical, mathematical, or logical law**: “sub-10 ms systems *cannot* use distant cloud infrastructure; physics forbids it.”
- **Word used as word**: “the term *gradient* refers to a vector of partial derivatives.”
- **Titles of works**: *Computer Architecture: A Quantitative Approach*.
- **Thesis punchline**: A single italicized sentence that captures the controlling insight of a section, for example, *Data is source code.*

Restricting bold and italics to these roles keeps sentence-level emphasis predictable, while larger pedagogical units are set off in dedicated callout boxes.

### Callouts Have Visual Identities That Match Their Job

^sec-about-callouts-7a8b

Callout boxes are not decoration. Each type signals a specific kind of content, so the visual identity announces what the box contains before the reader engages with it.

| Callout                 | Contains                                                                                                                                        |
|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**          | Formal definition of a key term, with its significance, distinction from the nearest neighbor concept, and a common pitfall                     |
| **Example**             | Historical case or concrete scenario, structured as context, insight, and systems lesson                                                        |
| **Systems Perspective** | Analytical observation or mathematical nuance that enriches the surrounding argument                                                            |
| **Napkin Math**         | Worked calculation with assumptions and intermediate steps shown explicitly; intermediate tables and equations are the math itself              |
| **Checkpoint**          | Self-check questions to verify understanding of the preceding section                                                                           |
| **War Story**           | Documented engineering incident with a sourced failure mode, structured as context, failure, consequence, and lesson                            |
| **Lighthouse**          | Recurring workloads characterized by a profile (parameters, FLOPs, dominant constraint), used as anchored case studies across multiple chapters |
| **Principle**           | Canonical book principle or invariant referenced from later chapters                                                                            |
| **Theorem**             | Formal, equation-backed result or bound, stated with its conditions and applied in later quantitative analysis                                  |
| **Key Takeaways**       | Four to seven most important results from a chapter, in summary form                                                                            |
| **Learning Objectives** | Skills and concepts that readers should be able to explain or apply after completing the chapter                                                |
| **What’s Next**         | Bridge from the chapter just ended to the chapter beginning, naming the open question the next chapter addresses                                |

When a callout contains a table, figure, or equation, that artifact is part of the callout’s pedagogical unit, not decoration. A lighthouse’s profile *is* its characterization. A napkin math box’s intermediate tables *are* the worked math. Reading these as separated artifacts loses the teaching arc. Standalone reference tables, by contrast, sit between paragraphs as numbered artifacts the reader returns to through cross-references. Both forms are valid; the visual marker (callout vs. standalone) tells the reader which one they are looking at.

## A Learning Platform

^sec-about-platform

Beyond the conventions on the page, this book is the reading spine of a broader learning ecosystem. The complete text, interactive notebooks, lecture slides, exercises, hands-on labs, and supplementary materials are freely available at [mlsysbook.ai](https://mlsysbook.ai), allowing readers to test the analytical models from each chapter in executable code.

## An Open-Source Textbook

^sec-about-open-source

This book is open source. The full text, figures, and build system are available at [mlsysbook.ai/git](https://mlsysbook.ai/git), and I invite every reader to contribute. That openness is deliberate. If AI engineering is to become a shared discipline rather than a collection of isolated practices, its foundational texts must be accessible to everyone. ML systems is a field shaped by practitioners across industry, academia, and the open-source community worldwide. A textbook covering this field should reflect that breadth and be available to all, regardless of geography or institutional affiliation.

Contributions from readers, whether fixing an error, suggesting a clearer explanation, adding a worked example, or proposing new content, have materially improved every chapter. Issues and pull requests provide the mechanism for that collaboration, and the same open materials support instructors adapting the book for classroom use.

## A Living Textbook

^sec-about-living

A printed textbook is finished on the day it goes to press. This field is not, and neither is my understanding of it. As an educator, I want readers to have the best explanation I can give, so I keep revising the online edition as systems change and as teaching shows me a clearer way to explain an idea. The principles in this book are chosen to last. The examples, numbers, and explanations around them are what change. Each release carries a version number, and its [release notes](https://github.com/harvard-edge/cs249r_book/releases) record what changed, so a course or a citation can point to a fixed version.

## Using This Book in a Course

^sec-book-using-book-course-f71c

The sixteen-chapter structure was developed and classroom-tested through CS249r at Harvard University and the [TinyML edX professional certificate](https://www.edx.org/professional-certificate/harvardx-tiny-machine-learning) program. Teaching systems principles across both kilobyte-scale microcontrollers and multi-accelerator servers showed that students learn fastest when a single analytical framework (memory bandwidth, compute throughput, and energy per operation) runs through every stage of the curriculum. *The physics scales; only the numbers change.*

An instructor teaching a one-semester course can keep the full sixteen-chapter arc while choosing how deeply to go inside each chapter. The core route below focuses on the engineering decisions every practitioner must be able to defend. It uses each chapter’s purpose, learning objectives, worked examples, fallacies, and checkpoints as the spine of the syllabus:

1.  **Part I (Foundations):** Ground the course in the iron law (**[[01 Books/Volume I - Foundations/00 Introduction/01 Introduction/V1-01.08 Iron Law of ML Systems#^sec-introduction-iron-law-ml-systems-c32a|Iron Law of ML Systems]]**), then show how workload constraints dictate system architecture (**[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.04 Analyzing Workloads#^sec-ml-systems-analyzing-workloads-cbb8|Analyzing Workloads]]** and **[[01 Books/Volume I - Foundations/01 Foundations/02 System Paradigms/V1-02.10 Choosing a Deployment Paradigm#^sec-ml-systems-comparative-analysis-paradigm-selection-bf66|Choosing a Deployment Paradigm]]**). Trace the six lifecycle stages (**[[01 Books/Volume I - Foundations/01 Foundations/03 ML Lifecycle/V1-03.05 Stage Ownership and Hand-Offs#^sec-ml-workflow-six-core-lifecycle-stages-00b0|Stage Ownership and Hand-offs]]**) from problem framing to holdout evaluation, and cover data collection, preprocessing pipelines, labeling, storage layout, and dataset health so students see how raw inputs become a reliable training feed.
2.  **Part II (Development and Training):** Follow a neural network from forward and backward math (**[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.04 Neural Network Fundamentals#^sec-neural-computation-neural-network-fundamentals-07e4|Neural Network Fundamentals]]**) to end-to-end execution (**[[01 Books/Volume I - Foundations/02 Development/05 Neural Computation/V1-05.06 Inference Pipeline#^sec-neural-computation-inference-pipeline-5372|Inference Pipeline]]**). Compare major architecture families by the operations they run, the state they store, and the data dependencies they impose. Then trace how frameworks lower a model graph into kernels, manage automatic differentiation and tensor memory, and execute a full training step (**[[01 Books/Volume I - Foundations/02 Development/07 ML Frameworks/V1-07.08 Anatomy of a Training Step#^sec-ml-frameworks-putting-together-anatomy-training-step-c7f1|Anatomy of a Training Step]]**), culminating in bottleneck diagnosis and single-node multi-GPU training (**[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.08 Scaling Training Systems#^sec-model-training-singlenode-multigpu-training-c87f|Single-node multi-GPU training]]**).
3.  **Part III (Optimization and Acceleration):** Teach students to optimize against measured bottlenecks across Data, Algorithm, and Machine. Start by scoring and pruning training data and deciding when a smaller dataset suffices (**[[01 Books/Volume I - Foundations/03 Optimization/09 Data Selection/V1-09.09 Choosing a Selection Strategy#^sec-data-selection-decision-framework-0261|Choosing a Selection Strategy]]**). Move to pruning, distillation, and quantization alongside the hardware formats they require. Map those compressed models onto compute units and memory hierarchies using the roofline model (**[[01 Books/Volume I - Foundations/03 Optimization/11 Hardware Acceleration/V1-11.07 Performance Bounds#^sec-hardware-acceleration-roofline-model-42ff|Performance Bounds]]**), kernel fusion, and compiler scheduling, and verify every claimed speedup with rigorous component, end-to-end, and power benchmarks (**[[01 Books/Volume I - Foundations/03 Optimization/12 Benchmarking/V1-12.10 Model and Data Evaluation#^sec-benchmarking-model-data-benchmarking-e0ca|Model and Data Evaluation]]**).
4.  **Part IV (Deployment and Operations):** Carry the verified model into production through request queuing, dynamic batching, serving runtimes, and cost modeling. Pair rollout and drift monitoring with the fairness, explainability, privacy, security, and energy controls summarized in **[[01 Books/Volume I - Foundations/04 Deployment/15 Responsible Engineering/V1-15.04 Responsible Engineering Across the Lifecycle#^sec-responsible-engineering-responsible-engineering-checklist-a038|Responsible Engineering Across the Lifecycle]]**. Close with the coupled-budget synthesis in **[[01 Books/Volume I - Foundations/04 Deployment/16 Conclusion/V1-16.02 The System Is the Model#^sec-synthesizing-ml-systems-ee10|The System Is the Model]]**, which ties the four parts back into a single engineering discipline.

Multi-node training (**[[01 Books/Volume I - Foundations/02 Development/08 Model Training/V1-08.08 Scaling Training Systems#^sec-model-training-scaling-beyond-single-node-a671|Scaling beyond a single node]]**), neural architecture search (**[[01 Books/Volume I - Foundations/03 Optimization/10 Model Compression/V1-10.03 Structural Optimization Changing What the Model Computes#^sec-model-compression-neural-architecture-search-cf12|Neural architecture search]]**), the clinical deployment case study (**[[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.10 Case Studies#^sec-ml-operations-clinaiops-case-study-5d5d|ClinAIOps case study]]**), and the appendix derivations work well as optional modules or project readings. Instructors teaching shorter terms or seminars can also split the book along its part boundaries:

- **Parts I–II** form an introductory half-semester on how ML systems are specified, built, and trained.
- **Parts III–IV** form an applied half-semester on optimizing, benchmarking, serving, and operating models in production.
- **The Part Introductions** alone offer a self-contained overview of the quantitative laws that govern ML systems for survey courses or executive seminars.

To support any of these formats, lecture slides, assignments, and instructor resources are available at [mlsysbook.ai](https://mlsysbook.ai).

Back to top

## Source References

^source-references

Naur, Peter, and Brian Randell, eds. 1969. *Software Engineering: Report of a Conference Sponsored by the NATO Science Committee, Garmisch, Germany, 7–11 October 1968*. Scientific Affairs Division, NATO.

^ref-naur1969softwareengineering

Hennessy, John L., and David A. Patterson. 2017. *Computer Architecture: A Quantitative Approach*. 6th ed. Morgan Kaufmann.

^ref-patterson2017hardware

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol1/frontmatter/about.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol1/frontmatter/about.html#sec-about). Rendering provenance is recorded in the import manifest.
