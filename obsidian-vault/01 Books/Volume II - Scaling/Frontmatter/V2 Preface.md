---
title: V2 Preface
type: Frontmatter
volume: 2
chapter: 0
publication_status: Preview
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol2/frontmatter/about.qmd
source_anchor: sec-about
source_mode: Source-Correlated Published HTML
tags:
- Type/Frontmatter
- Book/Volume_2
rendered_source_url: https://mlsysbook.ai/vol2/frontmatter/about.html
---

# V2 Preface

[[Home|Home]] · [[01 Books/Volume II - Scaling/Volume 2 Overview|Volume Overview]]

^sec-about

## Who This Book Is For

^sec-vol2-about-audience

This book is for anyone who understands machine learning on a single machine and now faces the challenge of making it work at scale. The problems of scale are not the problems of a single node, only bigger. They are qualitatively different: networks partition, hardware fails as a statistical certainty, and the societal impact of every design decision is amplified by millions of users.

The assumed foundation is what an introductory ML systems course or equivalent experience supplies, with no particular prior textbook required. The advanced scope here is the transition from that single node to a coordinated fleet. That scope ranges from designing the physical substrate of an AI data center, to scaling training beyond the limits of a single accelerator, to reasoning about what happens when a production fleet serves a global user base. Throughout, the focus is on the physics of distribution, the invariants that govern every fleet-scale ML system regardless of the framework, the model, or the era.

## Prerequisites

^sec-vol2-about-prerequisites

Readers should bring the following background:

- **Single-machine ML systems**: Understanding of ML workflows, neural network training, model optimization, and deployment on a single machine. Readers should be comfortable reasoning about memory hierarchies, computational graphs, accelerator execution, and hardware-software interactions. **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy|The D·A·M Taxonomy]]** recaps the single-machine performance model (the iron law, arithmetic intensity, and the Roofline Model), the memory hierarchy, training memory per parameter, and transformer compute that later chapters assume.
- **Programming**: Fluency in Python, including functions, classes, and data manipulation with NumPy. Familiarity with at least one ML framework (PyTorch, TensorFlow, or JAX).
- **Mathematics**: Comfort with linear algebra, basic calculus, and probability at the undergraduate level. **[[05 Reference/Volume II - Scaling/V2 Reliability Foundations#^sec-appdx-reliability-foundations-probability-tools|Probability tools for failure analysis]]** restates the probability results that the failure analysis uses, and **[[05 Reference/Volume II - Scaling/V2 Inference Foundations#^sec-appdx-inference-scale-queuing-theory-batched-inference-bbf0|Queuing theory for batched inference]]** develops the queuing results that serving analysis uses.

The following background is helpful but not required:

- **Distributed systems**: Familiarity with networking concepts (TCP/IP, bandwidth, latency), parallelism, and basic distributed computing deepens understanding of the fleet infrastructure and training chapters.
- **Cloud infrastructure**: Experience with containerization and orchestration (Docker and Kubernetes) or cluster schedulers (Slurm) provides useful operational context.
- **Production engineering**: Understanding of monitoring, observability, and site reliability practices will enrich the deployment and operations chapters.

## Why a Fleet-Level Textbook

^sec-vol2-about-why-fleet

In 2012, training AlexNet took five to six days on two GPUs ([[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^ref-krizhevsky2012imagenet|Krizhevsky et al. 2012]]). By 2023, public GPT-4-class estimates placed frontier training at roughly 25,000 GPUs running for about three months ([[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^ref-semianalysisGPT4|Patel and Wong 2023]]); OpenAI did not disclose the actual hardware configuration ([[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^ref-openai2023gpt4|OpenAI et al. 2023]]). This is not the same engineering problem at a larger scale. It is a categorically different engineering problem.

On a single machine, performance is governed by the memory wall, the gap between processor speed and memory bandwidth. In a distributed cluster, a new limit emerges. Bisection bandwidth, the total bandwidth across the narrowest cut that divides the cluster into two halves, caps the throughput of any traffic that must cross that cut. Data no longer moves through local hierarchies alone; it traverses optical fabrics governed by the speed of light between racks and across continents. Hardware failures, rare enough on a single machine to be treated as exceptions, become routine statistical events at fleet scale. Long training runs must plan for interruptions rather than rely on every component remaining available until completion.

These are not operational annoyances. They are physical constraints, as fundamental and as permanent as the memory wall, Amdahl’s Law, or the energy cost of data movement. They require their own engineering discipline, built on the invariants this book develops:

- **The Empirical Scaling Law**: Within empirically validated regimes, model loss falls as a power law in training compute, data, or parameters, so each further improvement demands multiplicatively more resources. This is the pressure that moves machine learning from single machines onto fleets.
- **The Bisection Bandwidth Theorem**: For communication patterns that must cross the minimum bisection, throughput is bounded by that bisection bandwidth.
- **The Fleet Law**: Under fixed-work scaling, reduced per-node computation competes with communication and coordination costs, so adding workers does not guarantee proportional speedup.
- **The Young-Daly Checkpoint Interval**: The optimal checkpoint interval balances the cost of writing state against the expected cost of lost work due to failure.
- **Serving Cost Dominance**: For high-traffic production models, cumulative inference operational expenditure can exceed the one-time training cost, making serving efficiency a lifecycle optimization target.
- **The Fairness Impossibility Theorem**: With unequal group base rates and imperfect prediction, risk scores cannot satisfy groupwise calibration and equal mean scores across groups within both outcome classes simultaneously. Thresholded error-rate parity and demographic parity are distinct requirements with their own trade-offs.

If single-machine ML systems engineering asks *“what can one machine build?”*, then fleet-scale ML systems engineering asks *“what can a thousand machines build together, and at what cost to reliability, efficiency, and society?”* That final clause is what sets fleet-scale engineering apart. A single machine affects its user; a fleet affects everyone its outputs touch, across millions of decisions per second. At that scale, reliability, efficiency, and fairness stop being features and become engineering constraints as binding as bandwidth or power. A system that scales but cannot be trusted has not been engineered. It has only been enlarged.

This book develops that discipline. It follows the Hennessy and Patterson pedagogical model, extending the quantitative, principles-first approach to the distributed scale ([[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^ref-hennessy2011computer|Hennessy and Patterson 2011]]; [[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^ref-hennessy2019|Hennessy and Patterson 2019]], [[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^ref-patterson2017hardware|2017]]). Just as their work taught a generation to reason about processor performance from first principles, this book teaches the reader to reason about fleet performance, replacing intuition about distributed systems with measurement, and ad hoc scaling with engineering.

The architectural priorities and operational failure modes explored in these chapters did not originate in an academic vacuum. They were gathered directly from practitioners in industry, through technical exchanges at conferences, engineering meetups, and conversations with colleagues. These colleagues generously made the time to explain what breaks when scaling models across thousands of accelerators and what practicing systems engineers must understand.

Single-node foundations supply the bricks of those systems: tensors, kernels, memory hierarchies, and optimization loops. What breaks at fleet scale is rarely an individual brick, because a fleet is closer to an orchestra than to a larger wall. An orchestra is not simply many musicians playing at once. It needs a conductor, a score, precise synchronization, and the ability to recover when a player drops out, none of which governs a solo performer. A training cluster, a serving fleet, and an edge deployment are vastly different systems, but beneath them sit the same building blocks: parallelism strategies, collective communication primitives, checkpoint protocols, scheduling algorithms, and the trade-offs between throughput, latency, fault tolerance, and cost.

## What This Book Covers

^sec-vol2-about-covers

This book focuses on the machine learning fleet: coordinated machines that jointly train, serve, or maintain ML models. Warehouse-scale training clusters are one form; geographically distributed serving replicas and heterogeneous edge devices are others. Across these forms, communication and coordination couple local execution to fleet behavior, while reliability, resource budgets, and governance constrain the design. The scope is the fleet as it exists today and the governance of operating it at scale. Research-frontier topics such as fully autonomous fleet management, next-generation interconnects, neuromorphic computing at scale, and formal verification of fleet-level safety properties lie beyond it.

The content is organized into four parts:

- **Part I: The Fleet** builds the physical substrate of the AI data center from the ground up: the silicon and cooling of compute infrastructure, the network fabrics that connect thousands of accelerators, and the scalable data storage that feeds training pipelines.
- **Part II: Distributed ML** establishes the logic of distribution beyond a single machine: the collective communication primitives that synchronize gradients, the parallelism strategies (data, tensor, and pipeline) for training models too large for single devices, the fault tolerance mechanisms that ensure reliability when failure is routine, and the orchestration systems that manage the fleet.
- **Part III: The Fleet in Production** takes the trained model from the cluster to the world: fleet efficiency, which measures how much of a fleet’s capacity becomes useful work, serving at scale for millions of concurrent requests, edge intelligence across heterogeneous and federated devices, and the operational lifecycle required to manage production fleets.
- **Part IV: The Responsible Fleet** confronts the forces that determine whether the fleet serves its users or harms them: security and privacy, robust system design, environmental sustainability, and responsible engineering as constraints as fundamental as power density or bisection bandwidth.

These four parts trace a path through the fleet stack, a layered abstraction that organizes an ML system at distributed scale, from the physical facility up to its governance. The stack has eight rows grouped into four bands, and each band is one part of the book. At the base, the Infrastructure band (Part I) holds **Facility & Accelerators** and **Fabric & Storage**, the physical substrate. On top of that hardware, the Distribution band (Part II) adds **Distributed Execution** and **Reliability & Control** to manage parallel work, communication, scheduling, and recovery. Once a model can be trained reliably, the Serving band (Part III) provides **Runtime & Serving** and **Operations** to take models to users and manage the production lifecycle. At the top, the Governance band (Part IV) layers **Assurance** (security, privacy, and robustness) and **Governance & Sustainability** to turn trust, risk, policy, and environmental cost into engineering constraints. Each row provides an abstraction to the row above and consumes the row below. Engineering decisions in the Infrastructure band constrain what is possible in the bands above it, while governance requirements constrain choices throughout the stack. Privacy, acceptable risk, and environmental budgets enter the design from the beginning; Part IV develops their enforcement mechanisms after the infrastructure and operational dependencies are available.

Where the fleet stack locates responsibility, a second framework diagnoses cost. The C³ taxonomy divides the wall-clock time of distributed execution into Compute, Communication, and Coordination, and the Fleet Law turns that division into an equation for distributed step time. Every chapter applies this lens to its own layer of the stack. Three recurring workloads, the archetypes, keep the analysis concrete: a large dense language model (Archetype A), a recommendation model with very large embedding tables (Archetype B), and a model trained by federated learning across phone-class devices (Archetype C). Each stresses a different part of the fleet, and the chapters return to whichever one exposes their central constraint.

Each part builds on the previous one, so sequential reading is recommended. The reading paths below offer alternatives for readers with specific goals.

## Suggested Reading Paths

^sec-vol2-about-reading-paths

The chapters are ordered so that each can draw on everything before it, but not every chapter consumes the one immediately before it. A dependency map derived from the chapters’ own cross-references records which chapters build directly on which ([[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^fig-vol2-chapter-dependencies|figure P.1]]). An arrow in the map means the later chapter uses a model, mechanism, or constraint that the earlier one establishes. Two features of the map guide the choice of path. First, every chapter lies on a route to **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/17 Conclusion/V2-17 Conclusion#^sec-conclusion|Conclusion]]**, whose six principles cite every chapter of Parts I through IV, so no chapter is a dead end. Second, several dependencies cross part boundaries: distributed training builds on both the storage pipeline of **[[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage#^sec-data-storage|Data Storage]]** and the collectives of **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, and fleet efficiency (**[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency#^sec-performance-engineering|Fleet Efficiency]]**) builds on **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**. Consecutive chapters without an arrow mark a change of thread rather than a gap. **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, for example, builds on the fabric model of **[[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics#^sec-network-fabrics|Network Fabrics]]** rather than on the storage chapter that precedes it.

![[90 Assets/Volume II/Shared Figures/Chapter Dependency Map d2ee4f26e4.svg]]

Figure P.1: **Chapter Dependency Map**: Each arrow points from a chapter to a later chapter that builds on its results, derived from the book’s cross-references with transitive links omitted. Every chapter lies on the core path the conclusion builds on, so the map draws no optional branch. Book order is one valid reading order; a missing arrow between consecutive chapters means the later chapter does not directly consume the earlier one’s results.

^fig-vol2-chapter-dependencies

Each path below begins with the introduction, assumes the single-machine prerequisites listed earlier in this preface, and keeps every chapter that its destination depends on in the map:

- **The Complete Path** (all chapters, in sequence): Follows the causal chain of constraints that governs the ML fleet from first principles of distribution. After the introduction, progress through Parts I, II, III, and IV.
- **The Infrastructure Path** (physical fleet and orchestration): Focuses on Part I (**[[01 Books/Volume II - Scaling/01 The Fleet/02 Compute Infrastructure/V2-02 Compute Infrastructure#^sec-compute-infrastructure|Compute Infrastructure]]**, **[[01 Books/Volume II - Scaling/01 The Fleet/03 Network Fabrics/V2-03 Network Fabrics#^sec-network-fabrics|Network Fabrics]]**, **[[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04 Data Storage#^sec-data-storage|Data Storage]]**), then **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**. Before orchestration, use the collective traffic patterns in **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, the workload partitioning in **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]**, and the checkpoint/recovery model in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]** to establish what the scheduler must place, connect, and preserve.
- **The Scaling Path** (distributed training depth): Establishes the memory-capacity, network-bandwidth, and storage-throughput models in Part I before focusing on **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]**, **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**, and **[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency#^sec-performance-engineering|Fleet Efficiency]]**. Readers already comfortable estimating those limits can use Part I as a reference.
- **The Production Path** (deployment and operations): Uses Part I for fleet capacity and network constraints. It then establishes collective communication in **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]**, model partitioning in **[[01 Books/Volume II - Scaling/02 Distributed ML/06 Distributed Training/V2-06 Distributed Training#^sec-distributed-training-systems|Distributed Training]]**, failure and recovery in **[[01 Books/Volume II - Scaling/02 Distributed ML/07 Fault Tolerance/V2-07 Fault Tolerance#^sec-fault-tolerance-reliability|Fault Tolerance]]**, placement and isolation in **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**, and how much of the fleet’s capacity becomes useful work in **[[01 Books/Volume II - Scaling/03 The Fleet in Production/09 Fleet Efficiency/V2-09 Fleet Efficiency#^sec-performance-engineering|Fleet Efficiency]]**. Continue through **[[01 Books/Volume II - Scaling/03 The Fleet in Production/10 Serving at Scale/V2-10 Serving at Scale#^sec-inference-scale|Serving at Scale]]**, **[[01 Books/Volume II - Scaling/03 The Fleet in Production/11 Edge Intelligence/V2-11 Edge Intelligence#^sec-edge-intelligence|Edge Intelligence]]**, **[[01 Books/Volume II - Scaling/03 The Fleet in Production/12 ML Operations at Scale/V2-12 ML Operations at Scale#^sec-ops-scale|ML Operations at Scale]]**, and Part IV (**[[01 Books/Volume II - Scaling/04 The Responsible Fleet/13 Security & Privacy/V2-13 Security & Privacy#^sec-security-privacy|Security & Privacy]]**, **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/14 Robust AI/V2-14 Robust AI#^sec-robust-ai|Robust AI]]**, **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/15 Sustainable AI/V2-15 Sustainable AI#^sec-sustainable-ai|Sustainable AI]]**, and **[[01 Books/Volume II - Scaling/04 The Responsible Fleet/16 Responsible AI/V2-16 Responsible AI#^sec-responsible-ai|Responsible AI]]**).

## How to Read This Book

^sec-vol2-about-how-to-read

Across any of those reading paths, recurring visual cues in the margins orient the reader within the fleet stack. At every chapter opening, a margin figure highlights which rows of the stack the chapter addresses. The full stack below shows each row with its scope, grouped into the four parts of the book:

![[90 Assets/Volume II/Shared Figures/Fleet Stack dfae3bfd77.svg]]

*Stack of eight rows in four bands, labeled Part I Infrastructure, Part II Distribution, Part III Serving, and Part IV Governance from bottom to top. Rows from bottom: Facility and Accelerators, Fabric and Storage, Distributed Execution, Reliability and Control, Runtime and Serving, Operations, Assurance, and Governance and Sustainability, each with a short list of what it holds.*

The Roman numerals (I–IV) mark those four parts, while the row intensity marks emphasis. The stack uses one accent color throughout so that shade, not hue, carries the chapter-focus signal.

In the margin figures throughout the book, the intensity of each row reflects how strongly the chapter engages it. Brighter (higher intensity) marks the chapter’s primary focus; dimmer (lower intensity) marks contextual relevance as constraints propagate upward. Consider three chapters that illustrate how the emphasis shifts:

![[90 Assets/Volume II/Shared Figures/Margin Stack e7b38e246f.svg]]

*Fleet stack shaded for Compute Infrastructure: the bottom Facility row is brightest and the rows above fade toward the top.*

Compute Infrastructure

![[90 Assets/Volume II/Shared Figures/Margin Stack b5f508998b.svg]]

*Fleet stack shaded for Distributed Training: the Execution row is brightest, the Control row above it is moderately bright, and the other rows are dim.*

Distributed Training

![[90 Assets/Volume II/Shared Figures/Margin Stack fa29bbbf49.svg]]

*Fleet stack shaded for Responsible AI: the top Governance row is brightest, the Assurance row below it is strong, and the rows below fade toward the bottom.*

Responsible AI

In Compute Infrastructure, the bottom row dominates because the chapter is about silicon, power, cooling, and physical deployment. In Distributed Training, **Distributed Execution** is brightest while **Reliability & Control** remains visibly relevant because large training runs depend on scheduling and recovery. In Responsible AI, **Governance & Sustainability** is primary while **Assurance** stays strong because accountability depends on measurable trust and risk controls. The same stack tells three different stories, and in each one a decision made in one row ripples through the rows above and below it.

Small visual notes sit in the margins wherever a relationship is fastest to grasp by eye. They are reading aids, not figures to cite later. At fleet scale, this visual grammar makes bandwidth gaps, failure blast radius, checkpoint ratios, and edge-energy trade-offs visible without interrupting the argument. When a miniature uses a log scale, it says so inside the image.

![[90 Assets/Volume II/Shared Figures/Compute Infrastructure Cxl Bandwidth Gap 597f250188.svg]]

*Margin visual example: a log-scale bandwidth ladder comparing HBM3 with CXL over PCIe Gen5 and annotating the ratio.*

![[90 Assets/Volume II/Shared Figures/Network Fabrics Pfc Pause Blast 680be2b6e8.svg]]

*Margin visual example: a blast-radius fan showing one pause event propagating to multiple dependent flows.*

![[90 Assets/Volume II/Shared Figures/Data Storage Checkpoint Storm Write Time 36901fddf9.svg]]

*Margin visual example: a log-scale time ladder comparing the time for every replica to write its own checkpoint copy with the time to write one coordinated copy.*

![[90 Assets/Volume II/Shared Figures/Vol2 Sustainable AI Margin 004 50ccf8d4ea.svg]]

*Margin visual example: an energy ladder showing radio transmission dwarfing local arithmetic on a log scale.*

Alongside these visual miniatures, the margins carry unnumbered **marginal navigation pointers** that trace architectural dependencies across the fleet without interrupting the reading flow of the prose:

- **`↩︎` Backward pointer:** Directs the reader back to the earlier chapter where a physical limit, hardware contract, or analytical model was established.
- **`↪` Forward pointer:** Directs the reader ahead to the later chapter, or to the appendix, where the current idea is developed, measured, or enforced.
- **`⇄` Contrast:** Marks a place where two chapters treat the same problem differently, so the comparison is visible at a glance.

A pointer only orients. When a sentence depends on another chapter, the reference stays in the text.

The appendices are the last reading aid. Beyond the single-machine recap in **[[05 Reference/Volume II - Scaling/V2 Single-Machine Foundations#^sec-appdx-dam-taxonomy|The D·A·M Taxonomy]]**, they collect the diagnostic tables, the communication, reliability, and serving models, and the reference numbers the chapters use.

## Conventions

^sec-vol2-about-conventions

This book uses a small set of typographic conventions to mark what each piece of prose is doing.

### Bold Marks First Definitions

^sec-vol2-about-bold

A term in **bold** within body prose is its formal first introduction in the book. Each term receives this treatment exactly once. Subsequent appearances are unbolded; by then the term is part of the working vocabulary the chapter carries forward.

> The **Fleet Law** decomposes the time of one distributed step into local computation, exposed communication, and synchronization.

The bold is a contract: register this term because it will recur. A matching index entry in the back of the book points to the defining occurrence (under the `definition` subentry), providing a way to return to it. Key technical terms are also compiled in the glossary.

Bold also appears in a second, structural role: as a functional label at the start of an item inside a callout box or a summary bullet, for example **Recommendation**, **Trade-off**, or **Result**. In that context, the bold is scaffolding rather than a first definition.

### Italics Mark Specific Distinctions

^sec-vol2-about-italics

Italics are not used for general emphasis. Every italic span in this book performs one of five specific jobs:

- **Direct opposition**: *training* vs. *inference*, *allocated* vs. *productive* accelerator time.
- **Impossibility, stated as physical, mathematical, or logical law**: “a synchronous step *cannot* finish before its slowest worker does.”
- **Word used as word**: “the term *gradient* refers to a vector of partial derivatives.”
- **Titles of works**: *Computer Architecture: A Quantitative Approach*.
- **Thesis punchline**: A single italicized sentence that captures the controlling insight of a section, for example, *At scale, failure is the normal operating condition.*

An italicized word is performing one of these jobs. A word that is not italicized carries no implicit emphasis.

### Callouts Have Visual Identities That Match Their Job

^sec-vol2-about-callouts

Callout boxes are not decoration. Each type signals a specific kind of content, so the visual identity tells the reader what the box contains before they read it.

| Callout                 | Contains                                                                                                                                                     |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition**          | Formal definition of a key term, with its significance, distinction from the nearest neighbor concept, and a common pitfall                                  |
| **Example**             | Historical case or concrete scenario, structured as context, insight, and systems lesson                                                                     |
| **Systems Perspective** | Analytical observation or mathematical nuance that enriches the surrounding argument                                                                         |
| **Napkin Math**         | Worked calculation walked through step by step, with values computed inline from the book’s constants; intermediate tables and equations are the math itself |
| **Checkpoint**          | Self-check questions to verify understanding of the preceding section                                                                                        |
| **War Story**           | Documented engineering incident with a sourced failure mode, structured as context, failure, consequence, and lesson                                         |
| **Lighthouse**          | Recurring workloads characterized by a profile (parameters, FLOPs, dominant constraint), used as anchored case studies across multiple chapters              |
| **Principle**           | Canonical book principle or invariant referenced from later chapters                                                                                         |
| **Theorem**             | Formal, equation-backed result or bound, stated with its conditions and applied in later quantitative analysis                                               |
| **Key Takeaways**       | Four to seven most important results from a chapter, in summary form                                                                                         |
| **Learning Objectives** | Skills and concepts that readers should be able to explain or apply after completing the chapter                                                             |
| **What’s Next**         | Bridge from the chapter just ended to the chapter beginning, naming the open question the next chapter addresses                                             |

When a callout contains a table, figure, or equation, that artifact is part of the callout’s pedagogical unit, not decoration. A lighthouse’s profile *is* its characterization. A napkin math box’s intermediate tables *are* the worked math. Reading these as separated artifacts loses the teaching arc. Standalone reference tables, by contrast, sit between paragraphs as numbered artifacts the reader returns to through cross-references. Both forms are valid; the visual marker (callout vs. standalone) tells the reader which one they are looking at.

## A Learning Platform

^sec-vol2-about-platform

Whichever path readers choose, this book is one component of a broader learning ecosystem. The complete text, interactive notebooks, lecture slides, exercises, hands-on labs, and supplementary materials for every chapter are freely available at [mlsysbook.ai](https://mlsysbook.ai).

## An Open-Source Textbook

^sec-vol2-about-open-source

This book is built in the open. Its full text, figures, and build system live at [mlsysbook.ai/git](https://mlsysbook.ai/git), and contributions are welcome from every reader.

This is a deliberate choice. If AI engineering is to become a shared discipline rather than a collection of isolated practices, its foundational texts must be accessible to everyone. ML systems is a field shaped by practitioners across industry, academia, and the open-source community worldwide. A textbook covering this field should reflect that breadth and be available to all, regardless of geography or institutional affiliation.

Contributions from readers, whether fixing an error, suggesting a clearer explanation, adding a worked example, or proposing new content, have materially improved every chapter. Readers who find something that could be better are encouraged to open an issue or submit a pull request. This book improves because readers participate in building it.

## A Living Textbook

^sec-vol2-about-living

A printed textbook is finished on the day it goes to press. This field is not, and neither is my understanding of it. As an educator, I want readers to have the best explanation I can give, so I keep revising the online edition as systems change and as teaching shows me a clearer way to explain an idea. The principles in this book are chosen to last. The examples, numbers, and explanations around them are what change. Each release carries a version number, and its [release notes](https://github.com/harvard-edge/cs249r_book/releases) record what changed, so a course or a citation can point to a fixed version.

## Using This Book in a Course

^sec-vol2-about-course

This book grew out of CS249r at Harvard University and the [TinyML edX professional certificate](https://www.edx.org/professional-certificate/harvardx-tiny-machine-learning) program. That teaching reinforced an insight that shapes the curriculum here: bandwidth, energy, and failure set the limits on a microcontroller and on a data center alike, and what changes with scale is which limit binds. Because the physics is continuous while the engineering changes at each scale boundary, the book is structured to support a one-semester advanced course covering the full distributed ML systems stack, while allowing instructors to select individual parts for shorter modules:

- **Parts I–II** (The Fleet and Distributed ML) suit an advanced half-semester on distributed training infrastructure.
- **Parts III–IV** (The Fleet in Production and The Responsible Fleet) suit an applied half-semester on production ML at scale. Such a module should first review **[[01 Books/Volume II - Scaling/02 Distributed ML/05 Collective Communication/V2-05 Collective Communication#^sec-collective-communication|Collective Communication]]** and **[[01 Books/Volume II - Scaling/02 Distributed ML/08 Fleet Orchestration/V2-08 Fleet Orchestration#^sec-fleet-orchestration|Fleet Orchestration]]**, which fleet efficiency and serving build on ([[01 Books/Volume II - Scaling/Frontmatter/V2 Preface#^fig-vol2-chapter-dependencies|figure P.1]]).

For survey courses or executive programs, the four part introductions provide a condensed map of the constraints that govern fleet-scale ML systems. Their principle statements are previews; the chapters supply the assumptions, worked reasoning, and mechanisms needed to apply them.

Slides, assignments, and instructor materials for courses that use this book are available at [mlsysbook.ai](https://mlsysbook.ai).

## Copyright and Licensing

^sec-vol2-about-copyright

© Vijay Janapa Reddi and MIT Press. This work is distributed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0). The source is available at [mlsysbook.ai/git](https://mlsysbook.ai/git).

Back to top

## Source References

^source-references

Krizhevsky, Alex, Ilya Sutskever, and Geoffrey E. Hinton. 2012. “ImageNet Classification with Deep Convolutional Neural Networks.” *Advances in Neural Information Processing Systems (NeurIPS)* 25.

^ref-krizhevsky2012imagenet

Patel, Dylan, and Gerald Wong. 2023. *GPT-4 Architecture, Infrastructure, Training Dataset, Costs, Vision, MoE*. SemiAnalysis Blog.

^ref-semianalysisGPT4

OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, et al. 2023. “GPT-4 Technical Report.” *arXiv Preprint arXiv:2303.08774*, ahead of print. https://doi.org/10.48550/arXiv.2303.08774.

^ref-openai2023gpt4

Hennessy, J. L., and D. A. Patterson. 2011. *Computer Architecture: A Quantitative Approach*. Morgan Kaufmann.

^ref-hennessy2011computer

Hennessy, John L., and David A. Patterson. 2019. “A New Golden Age for Computer Architecture.” *Communications of the ACM* 62 (2): 48–60. https://doi.org/10.1145/3282307.

^ref-hennessy2019

Hennessy, John L., and David A. Patterson. 2017. *Computer Architecture: A Quantitative Approach*. 6th ed. Morgan Kaufmann.

^ref-patterson2017hardware

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol2/frontmatter/about.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol2/frontmatter/about.html#sec-about). Rendering provenance is recorded in the import manifest.
