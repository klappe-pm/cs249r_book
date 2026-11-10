---
title: V3 Reference Architecture
type: Reference
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/appendices/app_a_reference_architecture.qmd
source_anchor: sec-vol3-app-reference-architecture
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/appendices/app_a_reference_architecture.html
---

# V3 Reference Architecture

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-app-reference-architecture

This appendix is a reference for assigning responsibilities across an agentic machine learning system. Its maps connect task requirements to state owners, interfaces, and evidence obligations, so a design review can identify missing ownership without prescribing a particular implementation stack. The chapters teach the mechanisms; this reference helps a reader locate their boundaries and check the assumptions connecting them.

## How to Use This Appendix

^how-to-use-this-appendix

Consult the entry matching the design decision or missing record. Each section names the component or artifact it governs and points back to the chapter where the trade-off is derived:

- When a responsibility has no clear owner, [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^sec-vol3-app-ref-arch-mapping|section 1.1]] maps it to a logical component.
- When deciding which mechanisms a task requires, [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^sec-vol3-app-ref-arch-profiles|section 1.2]] links contract conditions to design obligations.
- When an operation crosses component boundaries, [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^sec-vol3-app-ref-arch-turn|section 1.3]] traces the records needed at each handoff.
- When choosing an execution boundary, [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^sec-vol3-app-ref-arch-actuation|section 1.6]] collects the compatibility and isolation questions.
- When deciding where information lives and who may change it, [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^sec-vol3-app-ref-arch-memory|section 1.5]] distinguishes state ownership and reconstruction contracts.
- When placing components or investigating a deployment symptom, [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^sec-vol3-app-ref-arch-blueprint|section 1.12]] identifies assumptions and measurements to check.

The maps describe logical responsibilities. One process may implement several rows; distributing a row across services does not remove its ownership requirement.

## The Component Map

^sec-vol3-app-ref-arch-mapping

A design can contain a tool gateway yet leave retry ownership undefined. Naming a component therefore does not establish its contract. The responsibilities in [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^tbl-vol3-app-ref-arch-matrix|table 1]] identify the records or decisions that need an owner when that function is present.

| Logical component      | Responsibility                                                      | Boundary to verify                                                            | Teaching location                                                                                                                    |
|:-----------------------|:--------------------------------------------------------------------|:------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Model service          | Produce a response under a declared invocation configuration        | Response status and usage do not certify task acceptance                      | **[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02 The Foundation Model#^sec-vol3-foundation-model\|The Foundation Model]]**         |
| Context assembler      | Select the inputs delivered to each call                            | Source, applicability, and trust survive selection and transformation         | **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering#^sec-vol3-context-engineering\|Context Engineering]]** |
| Serving memory         | Manage derived attention state and optional prefix reuse            | Reuse requires compatible, available state and permitted sharing              | **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management#^sec-vol3-kv-cache\|KV Cache Management]]**                                  |
| Durable stores         | Retain sources, memory records, and retrieval indexes               | Derived records preserve their source bindings and validity policy            | **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory#^sec-vol3-long-term-memory\|Long-Term Memory]]**             |
| Tool gateway           | Mediate dispatch and correlate returned evidence                    | Arguments, authority, preconditions, and repeat semantics are separate checks | **[[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling#^sec-vol3-tool-calling\|Tool Calling]]**                             |
| Isolation envelope     | Enforce the execution boundary                                      | Resource reach and lifetime match the declared threat model                   | **[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes#^sec-vol3-sandboxes\|Agent Sandboxes]]**                                   |
| Harness                | Own control state, admission, and outstanding work                  | Stopping continuation does not settle existing effects or charges             | **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10 The Agent Harness#^sec-vol3-agent-harness\|The Agent Harness]]**                     |
| Trajectory log         | Preserve recovery-required decisions and evidence                   | Acknowledgment satisfies the failure domain promised before dispatch          | **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11 Durable Execution#^sec-vol3-durable-execution\|Durable Execution]]**         |
| Recovery policy        | Select permitted responses to incomplete or failed work             | Unresolved operations and residual duties retain owners                       | **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12 Failure Recovery#^sec-vol3-failure-recovery\|Failure Recovery]]**             |
| Evaluation             | Assess declared criteria with scoped evidence                       | Checks cover stated properties rather than all possible outcomes              | **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13 Agent Evaluation#^sec-vol3-evaluation\|Agent Evaluation]]**                               |
| Release control        | Retain diagnostic evidence and stage exposure to live work          | Stopping admission does not settle effects the candidate already released     | **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/14 Operating Agents/V3-14 Operating Agents#^sec-vol3-operations\|Operating Agents]]**                   |
| Optional learning path | Admit records for a stated training use and assess changed behavior | Operational logs do not automatically qualify as training data                | **[[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation#^sec-vol3-trajectory-curation\|Trajectory Curation]]** |
| Optional delegation    | Assign bounded work and reconcile child outcomes                    | Delegation preserves authority limits, accounting, and responsibility         | **[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18 Multi-Agent Coordination#^sec-vol3-multi-agent\|Multi-Agent Coordination]]**                    |

Table 1: **Responsibility Map**: Logical components, their owned decisions, and the boundaries to check when those functions belong in a design. Rows do not prescribe separate services.

^tbl-vol3-app-ref-arch-matrix

For each applicable row, record the actual owner, its inputs and outputs, and the assumptions under which its boundary holds. Information-flow policy also crosses the rows: a permitted read can still disclose sensitive data through a later output or tool call. **[[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.07 Information-Flow Policy#^sec-vol3-security-taint-tracking|Information-Flow Policy]]** develops the provenance and permitted-flow checks needed at those handoffs. No single row establishes end-to-end correctness.

## Selecting Responsibilities from the Task Contract

^sec-vol3-app-ref-arch-profiles

A short task can issue an irreversible action, while a long task can remain disposable and read-only. Horizon alone cannot select durability or recovery mechanisms. H·S·A identifies exposures to examine; the adopted task contract determines permitted effects, failure tolerance, resource limits, and completion evidence (**[[01 Books/Volume III - Agentic Systems/00 Introduction/01 Introduction/V3-01.05 The H·S·A Exposure Space#^sec-vol3-intro-hsa|The H·S·A Exposure Space]]**). Each contract condition in [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^tbl-vol3-app-ref-arch-profiles|table 2]] therefore triggers a conditional design obligation rather than prescribing a minimum stack for an exposure level.

| Contract condition                              | Design obligation                                              | Evidence or assumption to record                                               |
|:------------------------------------------------|:---------------------------------------------------------------|:-------------------------------------------------------------------------------|
| Iteration consumes bounded resources            | Enforce admission and stopping conditions outside model output | Units, per-call limits, reserved liability, and finalization allowance         |
| Work must survive a stated failure              | Retain the record and artifacts needed to recover              | Failure domain, acknowledgment rule, retention, and ownership transfer         |
| Later decisions reuse observations              | Preserve source bindings and applicability conditions          | Source version or freshness policy; treatment of unavailable evidence          |
| The task executes generated code                | Choose and enforce an execution boundary                       | Reachable interfaces, credentials, isolation assumptions, and reset contract   |
| The task writes shared state                    | Check current authority and concurrency conditions             | Target identity, version precondition, and source-side conflict behavior       |
| A dispatched effect can outlive its caller      | Preserve operation identity and reconcile its outcome          | Endpoint repeat contract, settlement evidence, and owner of an unknown result  |
| An effect cannot be fully undone                | Bound admission and retain residual duties                     | Required approval, permitted partial outcomes, and escalation responsibility   |
| Success requires more than a plausible response | Protect and apply the acceptance criteria                      | Evidence coverage, uncertainty, and authority to adopt the verdict             |
| Work is delegated or used for training          | Add the corresponding supervision or data-admission contract   | Child authority and liabilities, or intended learning use and split boundaries |

Table 2: **Contract-Driven Design Obligations**: Conditions that make particular responsibilities necessary. Several conditions can apply to one operation; none uniquely determines a deployment topology.

^tbl-vol3-app-ref-arch-profiles

Apply the rows to operations and retained records, not merely to a task’s largest exposure label. A local patch needs a workspace boundary; publishing it adds source-side authorization and concurrency requirements. Publication does not imply that reversal is safe, available, or equivalent to undoing its consequences. If the task does not permit publication, withholding that capability removes the need to manage that particular effect without removing obligations for local execution and evidence.

## One Turn Through the Architecture

^sec-vol3-app-ref-arch-turn

A tool-using turn in a crash-recoverable task provides a bounded interface check. Assume that the harness owns admission, the endpoint exposes an operation contract, and the runtime retains the inputs required for its promised recovery. The sequence below follows one admitted model call and one proposed external operation; answer-only turns, parallel calls, and approval waits take different paths.

1.  **Admit the turn.** The harness considers a `READY` trajectory, checks current grants and control state, and reserves the proposed bounded liability against actual consumption and existing reservations while preserving finalization resources. Admitted work moves to `CALLING_MODEL` (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.05 Trajectory States#^sec-vol3-controlplane-statemachine|Trajectory States]]**).
2.  **Assemble the context.** The assembler selects applicable source material and observations within the input budget. Record the delivered input or retained artifact references needed by the recovery contract; a hash identifies content but cannot reconstruct missing bytes.
3.  **Call the model.** The model service receives the call with an output ceiling and a deadline, reuses the cached prefix where it can (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.06 Prefix Caching Across Turns#^sec-vol3-kvcache-radix-tree|Prefix Caching Across Turns]]**), and returns a proposal with a stop reason and token usage (**[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.06 The Invocation Contract#^sec-vol3-foundation-model-contract|The Invocation Contract]]**). The log records the reply.
4.  **Validate and grant.** The tool gateway validates the proposal and applies runtime policy to the session, target, operation, and current preconditions. A discovered descriptor does not confer permission (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.05 Interoperable Tool Discovery#^sec-vol3-tool-calling-mcp|Interoperable Tool Discovery]]**). Calls requiring approval go to the approval gate before dispatch (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.08 Approval Gates#^sec-vol3-controlplane-hitl|Approval Gates]]**).
5.  **Write intent, then dispatch.** The trajectory log makes the intent durable under the declared storage failure domain before dispatch (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.04 Durable Intent Before Dispatch#^sec-vol3-persistence-wal|Durable Intent Before Dispatch]]**). Where the workflow supplies a compensating operation, its recovery plan is recorded as well (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.04 The Trajectory Saga Pattern#^sec-vol3-sagas-architecture|The Trajectory Saga Pattern]]**). The gateway dispatches under the task’s enforced grant and execution limits, preserving a logical operation identity where the endpoint supports that retry contract (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials#^sec-vol3-sandboxes-least-privilege|Capabilities and Credentials]]**, **[[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.06 Retrying Uncertain Actions#^sec-vol3-tool-calling-idempotency|Retrying Uncertain Actions]]**).
6.  **Wait without holding more than needed.** The harness moves the trajectory to `WAITING_TOOL`. The serving memory decides whether the trajectory’s attention state stays resident, is evicted and recomputed, or is offloaded for the length of the wait (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kvcache-swapping|Paused-State Policies]]**).
7.  **Record the outcome and shape the observation.** The gateway correlates returning evidence with its call, preserving known results, partial effects, or unresolved status. Late outcomes can matter for reconciliation even when they should not resume the model. The log records this disposition and the bounded observation (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.07 Observation Stream Truncation#^sec-vol3-tool-calling-streaming|Observation Stream Truncation]]**).
8.  **Check progress and continue.** Recovery compares task-scoped observations with recent history to assess possible nonprogress (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.07 Semantic Watchdogs#^sec-vol3-sagas-watchdogs|Semantic Watchdogs]]**). The harness applies its guarded continuation or finalization decision. Evaluation assesses acceptance under the declared criteria, including any required residual-duty evidence; its final verdict need not be available when finalization begins (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.03 The Task Acceptance Contract#^sec-vol3-evaluation-contract|The Task Acceptance Contract]]**).

At each handoff, the receiving owner needs an identity, applicable version, and disposition, not merely a text description of the preceding step. Diagnostic spans can correlate observed calls and outcomes, but only the records and artifacts covered by the durability contract support promised recovery. A final acceptance decision can occur after this turn and can require evidence from outside its trace.

## The Model Service

^sec-vol3-app-ref-arch-processor

An interrupted response needs a different disposition from a complete proposal. The invocation contract therefore identifies the model and call configuration, input format, output limit, status, and available usage evidence (**[[01 Books/Volume III - Agentic Systems/01 The Model/02 The Foundation Model/V3-02.06 The Invocation Contract#^sec-vol3-foundation-model-contract|The Invocation Contract]]**). Deadlines and cancellation specify what the client can stop admitting or consuming and what termination the provider confirms. A local timeout does not prove that generation stopped or that its charge is settled. Token usage is one accounting input; task budgets can also constrain money, elapsed time, tool work, and other resources.

Prefix caching is an optional performance facility rather than a correctness requirement. If it is available, record compatibility, sharing, residency, and routing assumptions before relying on its savings. Session affinity can improve reuse but can also concentrate load; a changed prefix can reduce hits without changing the task’s validity. **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.06 Prefix Caching Across Turns#^sec-vol3-kvcache-radix-tree|Prefix Caching Across Turns]]** supplies the reuse conditions, while **[[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-kv-cache|The Size of the Attention State]]** supplies the memory-sizing model. Behavioral suitability still requires task-level evaluation independently of this interface contract.

## Context and Memory

^sec-vol3-app-ref-arch-memory

When a cached summary or workspace edit is mistaken for an authoritative record, later turns act on unverified state because an agent’s information lives across stores with different writers, lifetimes, and validity rules. The architecture must assign a single component owner to each state class ([[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^tbl-vol3-app-ref-arch-memory|table 3]]) and distinguish every derived copy from its source (principle [[01 Books/Volume III - Agentic Systems/02 Agent Memory/V3 Agent Memory Principles#^pri-vol3-source-authority|6]]). The persistent-record roles in **[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.03 Persistent Records#^tbl-vol3-memory-tiers|Roles of persistent records]]** further distinguish the claims and evidence retained in durable stores.

| State class              |  Level  | Component that owns it      | Who may write                             | Validity and maintenance contract                                      |
|:-------------------------|:-------:|:----------------------------|:------------------------------------------|:-----------------------------------------------------------------------|
| **Working context**      | ${S}_1$ | Context assembler           | Runtime assembles; the model consumes it  | Selection and validity policy apply to each delivered call             |
| **Attention state**      | ${S}_1$ | Serving memory              | Serving engine, derived from model inputs | Reconstruction needs retained inputs and compatible configuration      |
| **Workspace artifacts**  | ${S}_2$ | Workspace owner             | Tools under granted execution authority   | Lifetime, reset, and any checkpoint binding are explicit               |
| **Source artifacts**     | ${S}_3$ | The owning system           | Owners and granted tool writes            | Authoritative; change only through explicit writes                     |
| **Trajectory log**       | ${S}_3$ | Runtime history owner       | Authorized runtime writers                | Authoritative history remains reconstructible for promised retention   |
| **Agent-written memory** | ${S}_3$ | Durable stores (write path) | The model proposes; the runtime admits    | Admission, correction, supersession, expiry, and deletion by policy    |
| **Retrieval indexes**    | ${S}_3$ | Durable stores (indexer)    | Authorized indexing path                  | Freshness is explicit; rebuilding needs retained sources and procedure |

Table 3: **State Classes by Owner**: Where each class of agent state lives in the reference architecture, who may write it, and what keeps it consistent with the world.

^tbl-vol3-app-ref-arch-memory

Three architectural rules follow from the table. First, a trajectory log records the events captured under its durability and retention contract; it does not establish every claim made in a logged response. Second, reconstruction requires retained inputs and a compatible reconstruction procedure. An index can be rebuilt from available sources, but a preference or observation cannot be recovered merely because an agent originally wrote it. Losing its only retained evidence can change later behavior. Third, the model proposes writes through mediated tools; workspace containment and memory admission enforce different boundaries on those operations. The context assembler selects from these records, and the retrieval contract (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.04 The Retrieval Contract#^sec-vol3-persistent-governance|The Retrieval Contract]]**) governs how durable information re-enters a call, preserving its applicability, provenance, and retrieval limitations.

## Tools and Sandboxes

^sec-vol3-app-ref-arch-actuation

Validating a tool call’s JSON arguments at the gateway does not stop the executed binary from reading host credentials or opening an unauthorized socket once it starts running. To cover both boundaries, the tool gateway mediates requests and returning evidence while the isolation envelope constrains execution reach. At the request boundary, the gateway validates arguments, applies session policy and action-time checks, dispatches permitted calls, and returns bounded observations; its retry behavior depends on operation semantics and the endpoint’s supported identity, effect, and result contract, since a timeout may remain unresolved and a key alone does not make repetition safe (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07 Tool Calling#^sec-vol3-tool-calling|Tool Calling]]**). Inside the execution boundary, the envelope enforces the implementation’s permitted resource access, credentials, workspace effects, network reach, and resource use (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08 Agent Sandboxes#^sec-vol3-sandboxes|Agent Sandboxes]]**), because neither a grant nor a descriptor enforces those limits merely by naming them.

Envelope choice depends on required interfaces, the threat model, and the configured enforcement boundary. Rather than assigning universal timings or ranking isolation strength by product name, the comparison in [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^tbl-vol3-app-ref-arch-sandboxes|table 4]] pairs each envelope class with the compatibility and resource questions developed in **[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.06 Choosing an Isolation Envelope#^sec-vol3-sandboxes-envelope-choice|Envelope selection]]**.

| Envelope                | Shared or trusted components                                                | Compatibility and resource questions                                                        |
|:------------------------|:----------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| Shared-kernel container | Host kernel and configured isolation controls                               | Which host interfaces, identities, mounts, and devices remain reachable?                    |
| User-space kernel       | Interposed application-kernel implementation and its host interface         | Does the toolchain use supported interfaces, and what does its actual I/O cost?             |
| MicroVM                 | Guest kernel, VMM/hypervisor boundary, configured devices and host services | What initialization, guest residency, I/O, and reset costs does the deployment incur?       |
| Restricted bytecode     | Execution runtime and exposed host imports                                  | Can the workload target this format, and are memory, execution, and import effects bounded? |

Table 4: **Envelope decision factors**: Startup, steady execution, residency, and teardown must be measured for the workload and configuration. Shared baseline memory is an implementation-dependent optimization, not a universal property of an envelope type.

^tbl-vol3-app-ref-arch-sandboxes

Provisioning also depends on lifetime policy, because a warm lease, a fresh restore, and a verified reset are different events. Pool capacity therefore needs an explicit reserve, replenishment concurrency, admission policy, and memory budget; average arrival rate alone does not establish that an environment is ready when needed (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.09 Sandbox Pools and Reset#^sec-vol3-sandboxes-pooling|Sandbox Pools and Reset]]**).

Supporting services enforce distinct boundaries around the envelope: a credential broker withholds selected secrets from the guest and checks authorized use even though task data and returned observations may still be sensitive (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.05 Capabilities and Credentials#^sec-vol3-sandboxes-credential-brokering|Credential brokering]]**), whereas egress controls constrain actual routes, destinations, and supported request semantics even when permitted requests can still carry inappropriate disclosures (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.08 Egress Control#^sec-vol3-sandboxes-network|Egress Control]]**). To govern those remaining cases, the security layer pairs these service controls with provenance and information-flow policy (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/09 Agent Security/V3-09.07 Information-Flow Policy#^sec-vol3-security-taint-tracking|Information-Flow Policy]]**).

## The Harness

^sec-vol3-app-ref-arch-orchestration

If a model-proposed plan update could directly grant authority, release a budget reservation, or mark an unknown effect settled, the agent could rewrite its own runtime constraints mid-run. To keep control state outside the model’s reach, the harness record connects an admitted call to its trajectory identity, current version, grants, budgets, pending work, and retained artifacts (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.04 The Trajectory Record#^sec-vol3-controlplane-acb|The Trajectory Record]]**), and every writer of that record must pass through guarded transitions.

The control interface distinguishes holding new work from terminating existing work. Pause, cancellation, approval, and resume each need an explicit disposition for outstanding calls and liabilities. An authenticated late result may settle an effect without becoming eligible input to an obsolete continuation. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/10 The Agent Harness/V3-10.05 Trajectory States#^sec-vol3-controlplane-statemachine|Trajectory States]]** supplies the transition guards; the reference-design question is which owner applies them when control requests and results arrive concurrently.

## The Durable Log and the Trace

^sec-vol3-app-ref-arch-observability

A surviving event record is useful only if the required history and referenced artifacts also survive. The recovery interface specifies the authoritative history, acknowledgment rule, compatible checkpoint boundary, retained bytes, and ownership-transfer mechanism. An incomplete replica cannot establish that an absent intent was never dispatched. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.06 Resuming a Trajectory#^sec-vol3-persistence-migration|Resuming a Trajectory]]** develops the validation and fencing needed before a new owner admits work.

Diagnostic traces have a different contract. Sampling or redaction can be acceptable for measurement while making a record insufficient for recovery. For each retained field, distinguish its recovery, replay, and diagnostic uses, with the completeness and lifetime promised for each (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.09 Log Retention and State Compaction#^sec-vol3-persistence-compaction|Log Retention and State Compaction]]**). One storage service can support several uses, but its most permissive sampling policy must not silently determine all of them.

## Recovery

^sec-vol3-app-ref-arch-recovery

An unknown tool outcome enters recovery as an unresolved operation, not as a failed call that can automatically be repeated. The recovery interface needs operation identity, available source evidence, permitted repeat behavior, and the owner of any remaining duty. Where compensation is supported, record its template and binding rule before forward dispatch; bind returned resource identities only from adequate evidence (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.04 The Trajectory Saga Pattern#^sec-vol3-sagas-architecture|The Trajectory Saga Pattern]]**).

Recovery also consumes authority and resources. Its contract specifies which retries, revised proposals, cleanup, or escalation remain permitted after normal model-directed admission stops. Progress detectors and dependency breakers can limit further work without establishing the fate of prior effects. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.08 Tool Circuit Breakers#^sec-vol3-sagas-containment|Tool Circuit Breakers]]** supplies those containment boundaries.

## Evaluation

^sec-vol3-app-ref-arch-evaluation

A trajectory that exits cleanly and prints “all tests passed” in its final message has not established task acceptance. An acceptance result instead requires an explicit binding to the task contract, candidate version, checks, and evidence scope. Record the evaluator’s authority to publish that result and the uncertainty or residual duties it leaves. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/13 Agent Evaluation/V3-13.03 The Task Acceptance Contract#^sec-vol3-evaluation-contract|The Task Acceptance Contract]]** defines the distinction between local checks and task acceptance; a completed trace alone satisfies neither.

The evaluation boundary protects grading logic and authoritative results from the acting agent and from candidate code executed during grading. Read-only test storage does not prevent in-process interference. Shared isolation infrastructure is possible under explicit credentials, execution, and observation boundaries; the fixture description must still state which production behaviors it omits.

## The Learning Loop

^sec-vol3-app-ref-arch-learning

Feeding raw operational logs straight into supervised fine-tuning trains the policy to imitate failed retries, stale-context guesses, and evaluation tasks leaked from held-out splits. Training is optional, and when a system learns from its trajectories, the data interface must bind each admitted artifact to its source, transformations, intended use, and split policy (**[[01 Books/Volume III - Agentic Systems/05 Learning from Trajectories/15 Trajectory Curation/V3-15 Trajectory Curation#^sec-vol3-trajectory-curation|Trajectory Curation]]**). A recovery log, an accepted task, and a usable policy target are different objects; none automatically qualifies as another.

The return path identifies the changed model and the behavioral evidence supporting its release. A changed policy may alter trajectory length, state use, and requested effects without acquiring additional authority. The existing runtime bounds still apply, and the release decision needs renewed evaluation rather than an assumption that training improves every task.

## Deployment and the Fleet

^sec-vol3-app-ref-arch-blueprint

A logical component map does not prescribe machine pools. A model service may be remote or local; a harness worker may retain live state while relying on durable records for recovery. Hardware virtualization is one possible isolation boundary, not a property of every sandbox. Placement should name the trusted components, reachable services, failure domains, and credentials rather than equating separate hosts or networks with adequate protection.

Resources held throughout a trajectory depend on its lifetime, not merely the duration of one model call. Under stable flow, Little’s law relates mean live trajectories to admitted arrival rate and mean lifetime (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.07 Capacity for Trajectories#^sec-vol3-agent-economics-capacity|Capacity for Trajectories]]**; **[[05 Reference/Volume III - Agentic Systems/V3 Inference Cost Foundations#^sec-vol3-appendix-inference-queueing|Queueing for Trajectories]]**). That product is not a hard admission limit or a guarantee against reserve exhaustion: bursts, variability, outstanding work, and reclamation require additional accounting. Across agents, typed task envelopes carry scoped authority and budgets (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.05 Typed Task Envelopes#^sec-vol3-multiagent-contracts|Typed Task Envelopes]]**), reservations account for concurrent spending (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.08 Spending Governance#^sec-vol3-agent-economics-governance|Spending Governance]]**), and cancellation requires supervision of the work and effects it reaches (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/18 Multi-Agent Coordination/V3-18.08 Bounding In-Flight Work#^sec-vol3-multiagent-backpressure|Bounding In-Flight Work]]**).

Use [[05 Reference/Volume III - Agentic Systems/V3 Reference Architecture#^tbl-vol3-app-ref-arch-failures|table 5]] to form diagnostic hypotheses, not to assign causes from symptoms alone. The same observed delay or cost increase can originate in several components; measurement must distinguish them before an intervention is justified.

| Symptom                                              | Pool            | Candidate explanation                                                           | Evidence to compare                                                                     | Relevant responsibility                                                                                                                                                                   |
|:-----------------------------------------------------|:----------------|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Calls queue while accelerators sit idle**          | Model service   | Residency pressure, admission policy, or input starvation                       | Resident state, runnable requests, queue reasons, and available service                 | Serving memory and admission (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.08 Paused-State Policies#^sec-vol3-kvcache-swapping\|Paused-State Policies]]**)                                              |
| **Cost per turn rises without longer contexts**      | Model service   | Reduced prefix reuse, longer outputs, or a changed route or tariff              | Cached input share, output usage, model route, and applicable prices                    | Call accounting and context layout (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.05 Staging the Next Invocation#^sec-vol3-context-engineering-staging\|Staging the Next Invocation]]**) |
| **Trajectories busy but going nowhere**              | Harness         | Activity without established task progress                                      | Repeated actions and state as signals, not proof of nonprogress                         | Recovery: progress detection (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.07 Semantic Watchdogs#^sec-vol3-sagas-watchdogs\|Semantic Watchdogs]]**)                                  |
| **Sandbox leases time out under bursts**             | Sandbox hosts   | Ready reserve exhausted under the configured replenishment and admission policy | Standby empty; queued admissions and restores                                           | Isolation envelope: pool sizing (**[[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.09 Sandbox Pools and Reset#^sec-vol3-sandboxes-pooling\|Sandbox Pools and Reset]]**)                                      |
| **Duplicate external effects after a restart**       | Harness and log | Missing intent, unsafe retry, or ineffective endpoint deduplication             | Authoritative intent history, logical operation identities, and endpoint effect records | Intent ordering and settlement (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.04 Durable Intent Before Dispatch#^sec-vol3-persistence-wal\|Durable Intent Before Dispatch]]**)                  |
| **A failing dependency drains budgets**              | Tool gateway    | Repeated admissions from one or several retry owners                            | Dependency-scoped outcomes and attempts grouped by logical operation and owner          | Retry ownership and containment (**[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.08 Tool Circuit Breakers#^sec-vol3-sagas-containment\|Tool Circuit Breakers]]**)                          |
| **Retrieved facts contradict the workspace**         | Durable stores  | Stale retrieval, a changed workspace, or incompatible claim scopes              | Source versions, applicability, retrieval time, and workspace changes                   | Record validity (**[[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.10 Storage Invalidation#^sec-vol3-persistent-invalidation\|Storage Invalidation]]**)                                     |
| **Spending exceeds limits across a delegation tree** | Fleet           | Missing reservations, underestimated liability, or unreconciled late charges    | Actual, reserved, and newly admitted liability under the same accounting boundary       | Spending governance (**[[01 Books/Volume III - Agentic Systems/06 Agents at Scale/19 Agent Economics/V3-19.08 Spending Governance#^sec-vol3-agent-economics-governance\|Spending Governance]]**)                                 |

Table 5: **Deployment Diagnostic Leads**: Candidate explanations and evidence to compare before attributing a symptom. The rows identify investigation boundaries, not unique causes or automatic remedies.

^tbl-vol3-app-ref-arch-failures

## Summary

^sec-vol3-app-ref-arch-summary

The reference is complete for a particular design when each applicable obligation has an owner, an interface, and stated assumptions. Components can be combined, distributed, or omitted when the task does not require their function. The remaining review is about the boundaries between them: preserved identities and evidence, current authority, resource liability, and responsibility for unresolved work.

Back to top

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/appendices/app_a_reference_architecture.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/appendices/app_a_reference_architecture.html#sec-vol3-app-reference-architecture). Rendering provenance is recorded in the import manifest.
