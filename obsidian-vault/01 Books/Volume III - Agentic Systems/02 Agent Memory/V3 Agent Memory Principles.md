---
title: V3 Agent Memory Principles
type: Part
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/parts/memory_principles.qmd
source_anchor: agent-memory-principles
source_mode: Repository QMD
tags:
- Type/Part
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/parts/memory_principles.html
---

# V3 Agent Memory Principles

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^agent-memory-principles

Part I priced a bounded model call and asked when additional reasoning, candidates, or checks improve the selected result. Continuing a trajectory across turns requires deciding which information reaches the next call. In the repair task, the earlier failure trace describes one source version, the candidate patch changes that version, and the latest test covers only the conditions it exercised. Carrying all three forward without their relationships can mislead the next decision even when they fit in the context window. Part II addresses the state exposure of H·S·A by separating the selected context from its derived attention state and from information retained outside the session. Within a session (${S}_1$), the runtime supplies working context while the serving system retains reusable computation, whereas durable sources and records (${S}_3$) outlive that session and must be retrieved to enter a later call. Between those two sits task-local workspace state (${S}_2$), whose execution and persistence requirements the sandbox workspace ([[01 Books/Volume III - Agentic Systems/03 Tool Use/08 Agent Sandboxes/V3-08.07 The Agent Workspace#^sec-vol3-sandboxes-cow|Sec — V3-08.07 The Agent Workspace]]) and trajectory checkpoints ([[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.05 Checkpoints#^sec-vol3-persistence-checkpointing|Sec — V3-11.05 Checkpoints]]) take up later. Because these three classes of state have different owners and validity conditions, they are not levels of one cache, and every turn begins by budgeting what fits in the call’s working set.

**Invariant**: A model’s nominal context limit bounds how much input a call can accept, not the quality of decisions made from it. The runtime selects the next call’s instructions, tool declarations, task state, and observations under that limit, and every token assigned to one role is unavailable to the others. When inputs and outputs share a context limit ${S_{\max}}$, reserving output allowance ${K_{\max}}$ gives the planning bound

$$
{S_{\text{system}}} + {S_{\text{tools}}} + {S_{\text{state}}} + {S_{\text{obs}}} \le {S_{\max}} - {K_{\max}}
$$

 Fitting within the bound does not guarantee that the selected material supports the next decision.

**Implication**: Every schema or log token displaces evidence. Measure context policies on the intended workload and preserve output headroom when setting the input budget. Compaction must protect the exact fields the current task requires and distinguish information retained in the prompt from information available only through a later read. A shorter representation is useful only if the next decision remains adequate. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.03 The Working-Set Decision#^sec-vol3-context-engineering-decision|Sec — V3-04.03 The Working-Set Decision]] develops the partition ([[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.03 The Working-Set Decision#^eq-vol3-context-budget-partition|Eq — V3-04.03 The Working-Set Decision]]), and [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.04 Usable Working Context#^sec-vol3-context-engineering-physics|Sec — V3-04.04 Usable Working Context]] gives the full treatment.

^pri-vol3-attention-working-set

What the runtime selects, the serving system must turn into attention state. Retaining that computation can reduce repeated work, but its validity differs from the relevance of the information it encodes.

**Invariant**: For the causal full-attention decoder considered here, reusable key-value state depends on the exact preceding token sequence and compatible model inputs and configuration, including positions and attention masks. A changed token prevents ordinary prefix reuse from that position onward, and matching tokens permit reuse only when compatible cached state remains available. Holding that state costs, for ${N_L}$ layers of ${H_{\text{KV}}}$ key-value heads of dimension ${d_{\text{head}}}$ stored at ${s_{\text{elem}}}$ bytes per element,

$$
{m_{\text{token}}} = 2 \cdot {N_L} \cdot {H_{\text{KV}}} \cdot {d_{\text{head}}} \cdot {s_{\text{elem}}}
$$

 bytes per retained token.

**Implication**: One volatile field early in the prompt forfeits reuse of everything after it, so the measured token-weighted prefix hit rate ${\rho_{\text{prefix}}}$ ([[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.06 Prefix Caching Across Turns#^eq-hprefix|Eq — V3-05.06 Prefix Caching Across Turns]]), not the count of potential matches, sets the saving. Keep stable material ahead of frequently changing material where the request format and task permit, without preserving obsolete information merely to retain a cache hit. The serving system can share, retain, offload, or recompute derived state according to resource costs. Losing cached tensors loses reusable computation rather than task knowledge when the inputs and configuration needed to reconstruct them remain available. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management#^sec-vol3-kv-cache|Sec — V3-05 KV Cache Management]] develops both quantities ([[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.03 The Footprint of Retained Attention State#^eq-mem-token|Eq — V3-05.03 The Footprint of Retained Attention State]]), with the reuse contract in [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05.06 Prefix Caching Across Turns#^sec-vol3-kvcache-radix-tree|Sec — V3-05.06 Prefix Caching Across Turns]].

^pri-vol3-prefix-coherence

Information that must outlive a session belongs in an external store, and returning a record to the model requires selecting it and supplying its contents, not merely retaining its location. The same record can remain useful as history while losing support for a claim about the current environment. Managing both requires identifying which source and conditions a claim depends on.

**Invariant**: A staged excerpt, summary, retrieval result, or index entry does not supersede the designated source for the claim it represents. Durable information re-enters the model only when it is retrieved and staged into context, and a retrieval score ranks candidates without establishing that a record is current, authoritative for the claim, or permitted for this task. If a derived entry ${c}$ was supported by its source from generation ${g_{\text{birth}}}({c})$ until a relevant change at ${g_{\text{death}}}({c})$, a query that requires generation ${g_q}$ may use it only if

$$
\text{IsValid}({c}, {g_q}) = \big({g_{\text{birth}}}({c}) \le {g_q} < {g_{\text{death}}}({c})\big)
$$

 A later change invalidates an observation as evidence about the present without making the historical observation false. Source provenance does not itself grant action permission or establish task acceptance.

**Implication**: Every read from durable storage, whether the runtime pre-stages it or the model requests it through a search tool, needs a contract that bounds access, returned content, resource use, and the required freshness. A source version check establishes whether a retrieved claim remains supported; a cache hit or an index entry does not establish freshness, and age limits can trigger a refresh but do not prove it. Removing unsupported claims or refusing to use them can also reduce the stale-support rate ${\epsilon_{\text{stale}}}$ ([[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.09 Evaluating Context Policies#^eq-vol3-stale-support|Eq — V3-04.09 Evaluating Context Policies]]). Track the dependencies of current claims, refresh, remove, or explicitly mark unsupported current-state claims, and retain historical evidence when needed. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04.08 Context Invalidation#^sec-vol3-context-engineering-context-rot|Sec — V3-04.08 Context Invalidation]] treats the prompt, and [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.04 The Retrieval Contract#^sec-vol3-persistent-governance|Sec — V3-06.04 The Retrieval Contract]] and [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.10 Storage Invalidation#^sec-vol3-persistent-invalidation|Sec — V3-06.10 Storage Invalidation]] treat durable stores ([[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06.10 Storage Invalidation#^eq-vol3-index-validity|Eq — V3-06.10 Storage Invalidation]]).

^pri-vol3-source-authority

Together, these three principles separate what the prompt carries, what the serving engine caches, and what durable storage backs. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/04 Context Engineering/V3-04 Context Engineering#^sec-vol3-context-engineering|Sec — V3-04 Context Engineering]] decides which information each call sees and how to keep that working context bounded and applicable. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/05 KV Cache Management/V3-05 KV Cache Management#^sec-vol3-kv-cache|Sec — V3-05 KV Cache Management]] follows the selected tokens into the serving system and prices holding their attention state across turns, forks, and tool waits. [[01 Books/Volume III - Agentic Systems/02 Agent Memory/06 Long-Term Memory/V3-06 Long-Term Memory#^sec-vol3-long-term-memory|Sec — V3-06 Long-Term Memory]] governs what outlives the session and how stored records return to a task under freshness checks. Selecting valid information still supplies no permission to act on it; Part III develops the tool and execution boundaries through which proposals affect the environment.

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/parts/memory_principles.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/parts/memory_principles.html#agent-memory-principles). Rendering provenance is recorded in the import manifest.
