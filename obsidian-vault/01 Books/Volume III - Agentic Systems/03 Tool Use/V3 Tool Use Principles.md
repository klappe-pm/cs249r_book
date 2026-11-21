---
title: V3 Tool Use Principles
type: Part
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/parts/tool_use_principles.qmd
source_anchor: tool-use-principles
source_mode: Repository QMD
tags:
- Type/Part
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/parts/tool_use_principles.html
---

# V3 Tool Use Principles

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^tool-use-principles

Part II separated the information selected for each call, reusable attention computation, and persistent records governed across sessions. Its policies already assumed operations that read sources and update records. Part III develops those operations: how a proposal becomes a permitted effect, how far the executing code can reach, and how untrusted information can redirect an agent using otherwise valid tools. These are the interface, containment, and adversarial-defense responsibilities that govern the authority exposure of H·S·A. Authority covers what an action can read and send as well as what it can change: a read-only tool that brings a customer record into context can disclose private data without mutating the source. Every tool call therefore begins at a mediated boundary that validates and authorizes the proposed action before anything executes.

**Invariant**: A tool call reaches the environment only after the runtime validates the proposal against its declared interface, checks applicable action preconditions, and authorizes it under the session’s grants and resource limits. A server’s advertisement supplies a tool description, not permission for this session to invoke it. The full treatment appears in [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.04 Tool Interface Schemas#^sec-vol3-tool-calling-schemas|Sec — V3-07.04 Tool Interface Schemas]] and [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.05 Interoperable Tool Discovery#^sec-vol3-tool-calling-mcp|Sec — V3-07.05 Interoperable Tool Discovery]].

**Implication**: The runtime binds a discovered interface to the policy it enforces; the endpoint still enforces its own access boundary. Constrained decoding can restrict supported output structure, but it replaces neither host validation nor authorization. A mutation that depends on an unchanged source version needs that precondition enforced with the mutation, not merely checked during an earlier read, because a read-then-write race stays open until the endpoint checks the expected version at application. Rejected proposals return structured diagnostics, and returning observations preserve outcome and omission information within their payload bounds.

^pri-vol3-strict-action-abi

Validation and authorization decide whether a call may be dispatched. They say nothing about what the runtime should do when the dispatch times out.

**Invariant**: A timeout alone does not establish whether a mutating effect occurred or whether an earlier attempt can still commit. The request may be lost, delayed, still executing, partially applied, or completed without a delivered reply. Under independent request and reply delivery outcomes, if requests are lost with probability ${q_{\text{req}}}$ and replies with probability ${q_{\text{rep}}}$, one blind retry of a non-idempotent operation without deduplication duplicates its effect with probability

$$
{p_{\text{dup}}} = (1-{q_{\text{req}}})\, {q_{\text{rep}}}\, (1-{q_{\text{req}}})
$$

 When request loss is rare, the duplicate rate tracks the reply-loss rate almost one for one.

**Implication**: Before repeating an action, establish that repetition is safe under its operation semantics or the endpoint’s deduplication contract. A stable logical-operation identity must be bound to the actual effect and retained result; a token or host-side lease alone supplies no such guarantee. An unchanged-state probe cannot exclude a delayed first attempt. Without sufficient evidence or enforcement, the effect remains unresolved and the runtime withholds a blind retry, preserving the uncertainty for reconciliation or escalation. [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.06 Retrying Uncertain Actions#^sec-vol3-tool-calling-idempotency|Sec — V3-07.06 Retrying Uncertain Actions]] develops the settlement rules and prices the duplicate path.

^pri-vol3-exactly-once-settlement

Even an authorized call with a sound retry contract can execute faulty or untrusted code, including code proposed by the model. Moreover, untrusted input can redirect an operation within whatever reach the call is given, requiring mechanical containment beneath the model’s instructions.

**Invariant**: Permission to invoke a tool does not bound the resources its implementation can reach or consume, and text from an observation, a reader model, or stored memory cannot grant authority or establish its own trust. The runtime enforces the task’s execution envelope and information-flow policy with metadata and decisions outside the model’s control. For a grant ${\Gamma}=({\mathcal{R}_{\Gamma}},\mathcal{O}_{\Gamma},{\phi_{\Gamma}},{t_{\text{exp}}})$ of rights ${\mathcal{R}_{\Gamma}}$, objects $\mathcal{O}_{\Gamma}$, condition predicate ${\phi_{\Gamma}}$, and expiry time ${t_{\text{exp}}}$, a proposed access ${r}$ is admitted at time ${t}$ only if

$$
\text{admit}({r}, {\Gamma}, {t}) \iff \text{authentic}({\Gamma}) \land {r}.\text{op} \in {\mathcal{R}_{\Gamma}} \land {r}.\text{target} \sqsubseteq \mathcal{O}_{\Gamma} \land {\phi_{\Gamma}}({r}) \land {t} < {t_{\text{exp}}}
$$

 and an operation that sends data onward is dispatched only if the applicable policy admits its recipient and use on the joined confidentiality and integrity labels, or under a separately authenticated, use-scoped decision.

**Implication**: Reach is bounded by the envelope rather than by what the model complies with. Choose an envelope by the code and interfaces it must support, the components it shares and trusts, the task’s authority, and measured resource costs. Deriving a narrower grant does not revoke a broader one still held. Track integrity provenance separately from confidentiality and preserve dependencies through extraction, summarization, and reuse. Endorsement for a protected use and declassification for an authorized release require their own policy and evidence. A workspace can preserve task-local changes across turns, but reuse requires supervised teardown and restoration of the declared mutable state. Ending an environment does not undo external effects or establish task acceptance. Evaluate these controls under a stated threat model, including useful task completion and false blocks. [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials#^sec-vol3-sandboxes-least-privilege|Sec — V3-08.05 Capabilities and Credentials]] develops the grant verdict ([[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials#^eq-vol3-capability-verdict|Eq — V3-08.05 Capabilities and Credentials]]), [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.03 The Agent Threat Model#^sec-vol3-sandboxes-blast-radius|Sec — V3-08.03 The Agent Threat Model]] the envelope, and [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security#^sec-vol3-security|Sec — V3-09 Agent Security]] the information-flow form ([[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.07 Information-Flow Policy#^eq-vol3-flow-dispatch|Eq — V3-09.07 Information-Flow Policy]]).

^pri-vol3-zero-trust-sandboxing

Together, these three principles govern how a proposal crosses into the environment, how uncertain outcomes settle, and how execution and data flow stay contained beneath the model. [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling#^sec-vol3-tool-calling|Sec — V3-07 Tool Calling]] specifies the mediated request and returning observation, including the conditions for safe repetition when an effect is uncertain. [[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes#^sec-vol3-sandboxes|Sec — V3-08 Agent Sandboxes]] enforces scoped grants, execution envelopes, workspace continuity, governed egress, and reset, with their resource and provisioning trade-offs. [[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09 Agent Security#^sec-vol3-security|Sec — V3-09 Agent Security]] defends against adversarial influence, unauthorized information flow, and confused deputy delegation across those interfaces. Each of these controls governs one call, one envelope, or one dispatch, and none decides whether the trajectory should propose again. The jobs, leases, approvals, and uncertain effects they leave behind need a single owner, and Part IV composes them into supervision and recovery of the whole trajectory.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/parts/tool_use_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/parts/tool_use_principles.html#tool-use-principles). Rendering provenance is recorded in the import manifest.
