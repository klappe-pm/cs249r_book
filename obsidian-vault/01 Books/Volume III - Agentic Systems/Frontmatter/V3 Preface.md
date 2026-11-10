---
title: V3 Preface
type: Frontmatter
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/frontmatter/about.qmd
source_anchor: sec-vol3-about
source_mode: Repository QMD
tags:
- Type/Frontmatter
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/frontmatter/about.html
---

# V3 Preface

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-about

## Who This Book Is For

^sec-vol3-about-audience

This book is for senior undergraduates and beginning graduate students in computer science and computer engineering who are taking a course on agentic machine learning systems, and for practicing engineers who build, operate, or evaluate agents. It is written for the engineer who has watched an agent demonstration succeed. That engineer now has to ship a system that carries delegated work to an accepted result, day after day, without deleting the wrong directory, looping until a budget runs out, or reporting success on a task it never finished.

The reader should understand foundation-model prompting and token generation and be comfortable with software systems, including APIs, state, concurrency, and process isolation. This book is self-contained and assumes no prior machine learning systems course. It develops agentic concepts where they are first used and derives the serving-cost relationships needed to reason about agent workloads without requiring accelerator microarchitecture or fleet-scale training.

## Why an Agentic Systems Textbook

^sec-vol3-about-why

A reasonable engineer might look at the current wave of agent demonstrations and ask a skeptical question. *Is agentic machine learning a systems discipline with durable principles, or a collection of framework wrappers, prompt templates, and API glue that will be rewritten next year?*

The skepticism is fair. Much of what is written about agents concerns surface choices, such as a framework’s abstractions, a persona in a system prompt, or a ten-line loop that looks impressive in a demonstration and fails under real workloads. Those choices change every few months. What does not change is the engineering problem underneath them.

A single model call reads a context and returns a proposal. By itself, the call neither executes that proposal nor establishes whether it satisfies the task. An agent puts that call inside a loop. The loop runs for many turns, carries state from one turn to the next, and turns approved proposals into edits, commands, queries, and messages that affect the environment. Each of those departures adds exposure beyond an isolated call, and each fails in its own way. A long loop compounds small errors and can run without advancing. Carried state overflows the context, goes stale, or contradicts itself. Actions leak data, repeat when a timeout hides whether they ran, or cannot be undone. The model cannot close any of these exposures by itself, because its proposal grants no authority and its self-report is insufficient evidence of success. The closure has to come from the machine built around it.

This book teaches how to design, measure, and improve that machine. Its central question is what a delegated task needs around a foundation model to produce a result supported by the required evidence. Readers should leave able to decide when a fixed workflow suffices and when a model-directed loop earns its added cost, what memory, tools, and runtime that loop requires, how to show that it works, and when changing the model or adding agents is worth the price.

## The Trajectory and Its Exposures

^sec-vol3-about-mental-model

The unit of engineering in this book is the **trajectory**, the ordered record of one delegated task’s execution. It holds what the model saw on each turn, what it proposed, what the runtime did with the proposal, and what came back. Accuracy on a single call is not the measure of an agentic system. The measure is whether trajectories reach results that meet the task’s acceptance standard, supported by evidence independent of the model’s self-report, and at what cost in turns, tokens, seconds, and dollars.

Three exposures describe how far a task departs from a single model call, and the book calls them **H·S·A**. Each axis captures one dimension along which a delegated loop accumulates risk beyond a stateless request:

- **Horizon** is how many turns the trajectory runs, and so how long errors have to compound and how much can go wrong between the start and the result.
- **State** is what the task carries from one turn to the next, from nothing, through the context window and a sandboxed workspace, to durable state that outlives the session or is shared beyond it.
- **Authority** is what the task may do to the world through its tools, from read access, which can still leak, to irreversible external actions such as a payment or a production migration.

Closure is not a fourth exposure, but the runtime’s answer to the three. Under the **invariant closure principle**, runtime mechanisms enforce named bounds (such as resource limits and permitted access) under stated assumptions, whereas independent checks supply evidence for the completion properties they cover. Making a check deterministic or protecting it from modification keeps that evidence sound without making its coverage complete, and while instructions or fine-tuning can improve the model’s proposals, neither replaces runtime enforcement. Higher exposure along any axis therefore demands stronger mechanical boundaries and a stricter acceptance standard. The introduction develops the three exposures, the principle, and the forms of evidence that can stand behind a claim that a task is done.

Two relations quantify these obligations throughout the book. **Horizon compounding** is the decay of reliability over unchecked turns. If each of ${H}$ sequential turns is correct independently with probability $1-{\epsilon}$ and nothing checks them, the task succeeds with probability $(1-{\epsilon})^{{H}}$. **Cost per accepted task**, ${C_{\text{eff}}}$, charges every attempt, failed ones included, to the tasks that meet their acceptance standard, and so states what a mechanism is worth in the unit the task cares about.

Four recurring workloads, each bound by a different exposure, keep the argument concrete. A repair agent that fixes a defect in an isolated working copy over a long horizon is the running example in every chapter. A research agent that reads untrusted sources, a remediation agent whose actions on production systems can be irreversible, and a support agent that serves many short interactive sessions at once return wherever the repair agent cannot exercise a constraint. A mechanism that is central for one of these workloads can be pure overhead for another, which is why the book prices mechanisms against a workload rather than ranking them in the abstract. That pricing and exposure framework sets the order in which the book constructs the system.

## What This Book Covers

^sec-vol3-about-covers

The book builds understanding in dependency order: **model, memory, tools, runtime, measure, learn, scale**. Each part adds responsibilities that the preceding material prepares the reader to evaluate. This teaching sequence is not a requirement to deploy every mechanism. When an agent fails, a related ordering governs the response. The **intervention ladder** ranks remedies by cost and reversibility. Once a failure is attributed to a measured cause, changes to context, to tools and their schemas, and to runtime control come before changes to the model’s weights. Weight changes are reserved for the failure that survives the earlier rungs, and they are made only on evidence that the change helps. The ladder is a default order rather than a sequence every failure must climb, and [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15.03 Capability Gap Diagnosis#^sec-vol3-flywheel-intervention-order|Sec — V3-15.03 Capability Gap Diagnosis]] develops it.

Before the seven parts begin, [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction#^sec-vol3-intro|Sec — V3-01 Introduction]] defines the agentic system and the trajectory, names the fail-plausible faults that make agents hard to trust, states the invariant closure principle, and turns a task into a contract. Along the horizon, state, and authority axes, it shows how to judge the runtime responsibilities a workload requires, when a fixed workflow suffices over a model-directed loop, and how the subsystems fit into a single architectural map:

- **Part I: The Model** studies the component every agent is built around through a single call. [[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model#^sec-vol3-foundation-model|Sec — V3-02 The Foundation Model]] establishes what a call reads, returns, and costs, and why its output is a proposal the runtime must check rather than a result. [[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute#^sec-vol3-test-time-compute|Sec — V3-03 Test-Time Compute]] asks when longer reasoning, additional candidates, or check-and-revise rounds improve the selected result within a bounded budget, and what evidence supports accepting it.
- **Part II: Agent Memory** governs the state exposure. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering#^sec-vol3-context-engineering|Sec — V3-04 Context Engineering]] decides what each call sees under a fixed budget, [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management#^sec-vol3-kv-cache|Sec — V3-05 KV Cache Management]] prices what holding that context costs in the serving system, and [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory#^sec-vol3-long-term-memory|Sec — V3-06 Long-Term Memory]] governs what persists across sessions and returns only through retrieval.
- **Part III: Tool Use** governs the authority exposure. [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling#^sec-vol3-tool-calling|Sec — V3-07 Tool Calling]] separates proposal validation, authorization, dispatch, and evidence of the resulting effect, including cases where a timeout leaves the outcome uncertain. [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes#^sec-vol3-sandboxes|Sec — V3-08 Agent Sandboxes]] bounds the reach of executing code, while [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security#^sec-vol3-security|Sec — V3-09 Agent Security]] addresses how untrusted information can misuse otherwise legitimate access.
- **Part IV: The Agent Runtime** governs the horizon exposure. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness#^sec-vol3-agent-harness|Sec — V3-10 The Agent Harness]] runs the loop under budgets and approvals, [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution#^sec-vol3-durable-execution|Sec — V3-11 Durable Execution]] preserves progress across stated failure conditions, and [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery#^sec-vol3-failure-recovery|Sec — V3-12 Failure Recovery]] chooses among repair, compensation, containment, and escalation. [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation#^sec-vol3-evaluation|Sec — V3-13 Agent Evaluation]] measures the whole single-agent system and establishes the evidence needed to judge later learning and scaling decisions, and the part ends with [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents#^sec-vol3-operations|Sec — V3-14 Operating Agents]], which traces, diagnoses, and stages the release of a configuration on live work.
- **Part V: Learning from Trajectories** changes model behavior when evaluation justifies that intervention; it does not replace the runtime’s boundaries. [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation#^sec-vol3-trajectory-curation|Sec — V3-15 Trajectory Curation]] decides when a failure warrants changing the weights at all, then selects and prepares records for different learning objectives, including demonstrations of recovery. [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/16 Trajectory Fine-Tuning/V3-16 Trajectory Fine-Tuning#^sec-vol3-fine-tuning|Sec — V3-16 Trajectory Fine-Tuning]] teaches behavior from those records, and [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/17 Reinforcement Learning from Verifiable Rewards/V3-17 Reinforcement Learning from Verifiable Rewards#^sec-vol3-rlvr|Sec — V3-17 Reinforcement Learning from Verifiable Rewards]] optimizes against verifiable rewards while examining the limits and protection of the reward checks.
- **Part VI: Agents at Scale** multiplies all three exposures. [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18 Multi-Agent Coordination#^sec-vol3-multi-agent|Sec — V3-18 Multi-Agent Coordination]] splits a task across agents only when the coordination pays for itself, and [[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19 Agent Economics#^sec-vol3-agent-economics|Sec — V3-19 Agent Economics]] prices and provisions agents per accepted task.
- **Part VII: Synthesis** follows a production incident-remediation task through the system in [[01 Books/Volume III - Agentic Systems/07 Synthesis/20 Conclusion/V3-20 Conclusion#^sec-vol3-conclusion|Sec — V3-20 Conclusion]]. It ends at the specification boundary, where defining success, judging whether the evidence is sufficient, and answering for the result stay with the engineer.

Reference appendices collect material that supports the chapters without interrupting them. Together they supply the mathematical background, the inference cost derivations behind the book’s serving estimates, the distributed-state guarantees behind durable execution and coordination, a reference architecture, typed tool interfaces, a failure taxonomy, and a glossary.

## How to Read This Book

^sec-vol3-about-reading

The book is written to be read in order. Each chapter uses only ideas introduced earlier in the book or defined where they appear, and each owns its concepts, so a mechanism is taught once and cited afterward. Every chapter opens with the agent problem it solves, introduces the mechanism as the answer to that problem, and closes with a summary and a handoff to the next chapter. Classical systems ideas, such as write-ahead logs, compensating transactions, idempotency keys, and capabilities, appear where they are the real engineering, introduced as the fix for an agent failure rather than as a lesson in their own right.

Readers with a particular role can weight their reading after the introduction. Engineers who build serving and execution infrastructure will lean on the chapters covering the model, the KV cache, sandboxes, durable execution, and economics. Engineers who build agent platforms will focus on context engineering, tool calling, security, the harness, failure recovery, evaluation, operations, and multi-agent coordination. Researchers and post-training teams will concentrate on the model, test-time compute, evaluation, and all of Part V. None of these emphases removes the prerequisites established by earlier chapters, so every path begins with [[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01 Introduction#^sec-vol3-intro|Sec — V3-01 Introduction]] and ends with [[01 Books/Volume III - Agentic Systems/07 Synthesis/20 Conclusion/V3-20 Conclusion#^sec-vol3-conclusion|Sec — V3-20 Conclusion]].

These dependencies divide the book into a core systems sequence and an optional post-training branch ([[01 Books/Volume III - Agentic Systems/Frontmatter/V3 Preface#^fig-vol3-chapter-dependencies|Fig — V3 Preface]]). Because the detailed test-time compute and post-training methods ([[01 Books/Volume III - Agentic Systems/01 The Model/03 Test-Time Compute/V3-03 Test-Time Compute#^sec-vol3-test-time-compute|Sec — V3-03 Test-Time Compute]] and Part V) branch off the core path without blocking Part VI or the conclusion, a course on building and operating agents can follow the core sequence alone. A course on post-training keeps that branch and still needs Parts I through IV beneath it, because [[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation#^sec-vol3-trajectory-curation|Sec — V3-15 Trajectory Curation]] starts from the evidence that [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation#^sec-vol3-evaluation|Sec — V3-13 Agent Evaluation]] defines and [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents#^sec-vol3-operations|Sec — V3-14 Operating Agents]] retains.

![[90 Assets/Volume III/Shared Figures/Chapter Dependency Map ca77e9afae.svg]]

**Chapter Dependency Map**: Each arrow points from a chapter to a later chapter that builds on its results, derived from the book’s cross-references with transitive links omitted. Solid chapters form the core path the conclusion builds on; the dashed branch through test-time compute and Part V can be skipped by a course that does not cover post-training.

^fig-vol3-chapter-dependencies

### Marginal Navigation Pointers

^sec-vol3-about-margin-pointers

The margins carry unnumbered **marginal navigation pointers** that trace dependencies between chapters without interrupting the flow of the prose:

- **`↩` Backward pointer:** Directs the reader back to the earlier chapter where a contract, check, or cost model was established.
- **`↪` Forward pointer:** Directs the reader ahead to the later chapter, or to the appendix, where the current idea is developed, measured, or enforced.
- **`⇄` Contrast:** Marks a place where two chapters treat the same problem differently, so the comparison is visible at a glance.

A pointer only orients the reader to where a related obligation or derivation lives. When a sentence’s argument depends directly on another chapter, the cross-reference stays in the body text so the main narrative remains self-contained.

## What This Book Is Not

^sec-vol3-about-not

Because the book focuses on the durable engineering of agentic systems, several adjacent topics lie outside its scope. First, it is not a prompt-engineering guide: prompts matter, but the runtime treats them as one assembled input and never relies on a prompt instruction where a mechanical check is possible. Nor is it a tutorial for any specific agent framework, protocol implementation, or model provider, or a leaderboard of this year’s models and benchmarks, which appear only as cited examples of a general technique or evaluation method. At the hardware layer, the text leaves accelerator microarchitecture to other works and develops only the serving relationships an agent engineer needs (such as how prompt processing differs from output generation and when shared-prefix reuse saves work, with full derivations in the appendix). Finally, the book covers software agents that act through tools on digital systems; agents that act on the physical world raise distinct control and safety problems outside its scope.

## A Note on Durability

^sec-vol3-about-durability

Frameworks, protocols, and model weights will change, some of them before this book reaches print. The text therefore emphasizes the ideas that survive those changes. These include the trajectory as the unit of work, the three exposures and the closure against them, the separation between a model that proposes and a runtime that decides, and the discipline of measuring before changing anything. Current protocols and systems appear throughout to make the ideas concrete, but the principles stand independently of any vendor or tool. Where a question is still open, such as how best to evaluate systems that act or how to structure an agent’s long-term memory, the book says so and presents the question as an open problem rather than a settled method.

## An Open-Source Textbook

^sec-vol3-about-open-source

This book is open source. Its full text, figures, and build system are available at [mlsysbook.ai/git](https://mlsysbook.ai/git), and contributions are welcome from every reader. That openness is deliberate. Agentic systems are being worked out in public, across research laboratories, open-source projects, and engineering teams worldwide. A textbook for so young a field should be available to everyone building it, regardless of geography or institutional affiliation.

Readers help most by fixing an error, suggesting a clearer explanation, adding a worked example, or reporting where a claim no longer holds. Issues and pull requests provide the mechanism for that collaboration.

## A Living Textbook

^sec-vol3-about-living

A printed textbook is finished on the day it goes to press. This field is not, and neither is my understanding of it. As an educator, I want readers to have the best explanation I can give, so I keep revising the online edition as systems change and as teaching shows me a clearer way to explain an idea. The principles in this book are chosen to last. The examples, numbers, and explanations around them are what change. Each release carries a version number, and its [release notes](https://github.com/harvard-edge/cs249r_book/releases) record what changed, so a course or a citation can point to a fixed version.

## Prerequisites

^sec-vol3-about-prerequisites

Readers should be comfortable with:

- working familiarity with foundation models, including prompting and autoregressive token generation;
- computer systems fundamentals, including processes, memory, file systems, and networking;
- basic distributed systems concepts, including remote calls, failure, and consistency;
- undergraduate probability; and
- programming in Python or another modern language.

Deeper study of operating systems, databases, or computer security helps, but the book explains how the systems mechanisms it uses apply to agent workloads. Readers who want more background on how machine learning systems are built and served can find it in *Introduction to Machine Learning Systems*, which this book does not assume.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/frontmatter/about.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/frontmatter/about.html#sec-vol3-about). Rendering provenance is recorded in the import manifest.
