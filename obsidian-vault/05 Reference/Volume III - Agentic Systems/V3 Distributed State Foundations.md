---
title: V3 Distributed State Foundations
type: Reference
volume: 3
chapter: 0
publication_status: In Development
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: books/vol3/backmatter/appendix_systems.qmd
source_anchor: sec-vol3-appendix-systems
source_mode: Source-Correlated Published HTML
tags:
- Type/Reference
- Book/Volume_3
rendered_source_url: https://mlsysbook.ai/vol3/backmatter/appendix_systems.html
---

# V3 Distributed State Foundations

[[Home|Home]] · [[01 Books/Volume III - Agentic Systems/Volume 3 Overview|Volume Overview]]

^sec-vol3-appendix-systems

An agent runtime relies on distributed systems guarantees when it records intent, calls a tool, or hands work to another worker. This appendix provides histories, boundary comparisons, and failure examples for interpreting those guarantees without assuming that a local transaction governs an entire task. The chapters retain the agent-specific admission, persistence, and compensation protocols.

## How to Use This Appendix

^how-to-use-this-appendix

Use the observed ambiguity to select the relevant background. Each entry isolates one distributed-systems guarantee that agent runtimes rely on when recording intent, dispatching tools, or handing work across workers:

- When timestamps appear to disagree about which operation happened first, [[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^sec-vol3-appendix-systems-order|section 1.1]] distinguishes causal order from an enforced operation order.
- When a design claims that an update is atomic or durable, [[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^sec-vol3-appendix-systems-boundaries|section 1.2]] identifies the state and failures the claim must cover.
- When recovery invokes transactions, sagas, or a write-ahead log, [[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^sec-vol3-appendix-systems-transactions|section 1.3]] separates their guarantees.
- When a reply is lost, [[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^sec-vol3-appendix-systems-retries|section 1.4]] distinguishes repeated execution, repeated effects, and result recovery.
- When a replacement worker takes ownership, [[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^sec-vol3-appendix-systems-fencing|section 1.5]] explains how the resource excludes a stale holder.

These distinctions help interpret, but do not replace, the endpoint’s actual contract. The main-text chapters referenced in each section specify the additional runtime protocols required for end-to-end safety.

## Histories and Operation Order

^sec-vol3-appendix-systems-order

Two workers read the same configuration version and independently prepare replacements. Sorting their log entries by wall-clock timestamp does not decide which replacement may publish. The clocks may differ, and even perfectly ordered observations would not prevent both workers from acting on the old version.

A causal history records dependencies rather than inferring them from timestamps. Lamport’s happened-before relation includes a process’s local event order, message transmission before its receipt, and the transitive consequences of those relationships. Events unrelated by this relation are concurrent. A logical clock preserves the implication from causal precedence to increasing clock values, but the converse does not hold; unequal logical timestamps need not establish a causal relationship ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-lamport1978time|Lamport 1978]]).

An endpoint can impose a stronger contract on its operations. Under linearizability, each completed operation appears to take effect at one point between invocation and response, consistently with the object’s sequential specification. If one operation returns before another starts, that order must be respected. Overlapping operations can take either order if their results fit that specification. The original correctness condition ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-herlihy1990linearizability|Herlihy and Wing 1990]]) concerns observable histories, not synchronized clocks.

For the configuration example, suppose the endpoint provides a linearizable conditional update that compares an expected version and replaces the value and version together. When both workers supply the same old version, one update succeeds and advances the version, so the other cannot also succeed against that stale precondition. That guarantee holds only if versions never cycle back to an old identifier and every conflicting writer goes through the enforcing boundary, since a separate read followed by an unconditional write does not implement this operation.

The comparison protects only what it covers. If publication also depends on a changing permission record elsewhere, checking the configuration version alone leaves that permission unchecked at publication. Operation order therefore needs an explicit state boundary, not merely an ordering label.

## Guarantee Boundaries

^sec-vol3-appendix-systems-boundaries

A service can commit a database update while a notification sent to another service remains undelivered. Calling the update a transaction does not place the notification inside it. The guarantee comparison in [[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^tbl-vol3-appendix-systems-guarantees|table 1]] separates claims that often appear together but answer different failure questions.

| Property                | What the contract specifies                                   | What does not follow                                   |
|:------------------------|:--------------------------------------------------------------|:-------------------------------------------------------|
| Atomicity               | Which changes commit or abort together                        | Unrelated remote effects participate                   |
| Isolation               | Which concurrent observations and interleavings are permitted | Every isolation level gives serial execution semantics |
| Durability              | Which acknowledged changes survive which failures             | Every copy or failure domain survives                  |
| Application consistency | Which state constraints each committed transition preserves   | The store understands whether a task result is correct |

Table 1: **Distinct Transaction Guarantees**: Each property requires a declared boundary; none supplies the other properties by its name alone.

^tbl-vol3-appendix-systems-guarantees

Atomicity concerns the commit unit, whereas durability concerns persistence after commitment ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-gray1981transaction|Gray 1981]]). A process can recover from a crash using an intact local disk, yet lose that same history if the disk disappears permanently. Replication changes the survivable failure set only when the acknowledgment policy requires the relevant replicas to preserve the update. The word “durable” must therefore identify both the acknowledgment and the assumed failures.

Isolation concerns interference during concurrent execution. Serializable execution has the effect of some serial ordering of the participating transactions; it does not necessarily preserve their real-time order. A transaction operating at weaker isolation may observe a different class of histories. Even serializability cannot repair an incorrect transaction that violates the intended application rule when run alone. The engineer must establish both a correct state transition and the concurrency contract under which it runs.

For a workflow spanning independent endpoints, the boundary test is to identify which operations participate in one commit decision. Anything outside that set needs its own completion and recovery contract. Classical coordination mechanisms preserve this distinction.

## Classical Transaction Background

^sec-vol3-appendix-systems-transactions

A database crash can leave modified pages on disk while other modifications remain only in memory. A distributed workflow adds another difficulty: one participant may have committed while another has not received a decision. Transaction recovery addresses these cases only where the storage and participants implement the required protocol.

### Transactions and Two-Phase Commit

^transactions-and-two-phase-commit

When a workflow updates two independent stores, a crash after the first store commits can leave the second store aborted unless both stores first agree to hold their changes in a prepared state. Two-phase commit coordinates that atomic commit decision among participating resource managers. During preparation, each participant establishes that it can commit and preserves the required recovery state. A participant that votes to commit cannot then abort unilaterally merely because it stops hearing from the coordinator. The final decision determines whether the participants commit or abort ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-gray1981transaction|Gray 1981]]). Preparation is consequently a recovery obligation, not a readiness hint.

The protocol requires cooperating participants. Writing “prepare” into a runtime log does not enlist an unrelated service or make its effect reversible. Moreover, a prepared participant can have to wait when it cannot learn the decision. A design must account for this blocking and for the resources retained while waiting; an atomic decision is not a promise of bounded completion time.

### Sagas

^sagas

Holding database locks across a multi-minute tool call or human approval wait blocks every concurrent writer on the service. To avoid long-lived locks, a saga divides a long operation into separately committed transactions with compensating transactions for partial execution ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-garciamolina1987sagas|Garcia-Molina and Salem 1987]]). Intermediate effects can become visible because the whole sequence does not retain one transaction’s isolation. A reservation followed by cancellation illustrates the distinction: cancellation is a new state transition, not deletion of the earlier history.

The application must specify what compensation restores and what remains. Charges already incurred or observations by another client may survive it. The original saga abstraction relies on the system’s ability to execute the required compensations; a remote workflow must separately handle compensators that fail or remain uncertain. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/12 Failure Recovery/V3-12.04 The Trajectory Saga Pattern#^sec-vol3-sagas-architecture|The Trajectory Saga Pattern]]** develops the agent-specific obligation records and evidence needed for that case.

### Write-Ahead Logging

^write-ahead-logging

If a process crashes after overwriting a data page on disk but before recording what changed, recovery cannot tell whether the page holds the old state, the new state, or a torn mix of both. Write-ahead logging prevents that ambiguity by imposing an ordering between recovery information and persistent changes. Before a database writes a modified page to persistent storage, the log information needed to recover that change must be durable. Before it acknowledges a durable commit, the required transaction log prefix must survive the promised failures. This ordering permits recovery even when the data pages themselves have not all been flushed.

ARIES organizes recovery into analysis, redo, and undo ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-mohan1992aries|Mohan et al. 1992]]). Analysis reconstructs recovery state; redo repeats relevant logged history; undo removes effects of transactions designated for rollback while logging the undo work. Prepared transactions awaiting a commit decision must retain their unresolved status. ARIES’s page-oriented redo and support for logical undo are more general than restoring an old byte image for every operation. Transaction log chains help locate earlier records, but a particular record layout is an algorithm choice, not the definition of write-ahead logging.

A runtime’s durable intent borrows the ordering requirement, not the database’s control over remote state. Recovering a request record does not establish that the endpoint executed it. **[[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.04 Durable Intent Before Dispatch#^sec-vol3-persistence-wal|Durable Intent Before Dispatch]]** develops this distinction for trajectory dispatch; interpreting an uncertain reply additionally requires the endpoint’s repeat contract.

## Repetition and Result Recovery

^sec-vol3-appendix-systems-retries

A client times out after requesting a state change. The server may never have received the request, may still be executing it, or may have completed it and lost the reply. A timeout alone does not distinguish those histories. Remote procedure call protocols therefore separate retransmission handling from the caller’s knowledge of execution ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-birrell1984rpc|Birrell and Nelson 1984]]).

Idempotence means that repeating an operation has the same effect on the specified state as applying it once, under the stated conditions. It does not require identical replies. An expected-version update can reject a repeat after an earlier success, protecting the state while leaving the caller uncertain which attempt succeeded. Conversely, a repeated “set” can overwrite an intervening writer even when setting the same value twice is idempotent in isolation.

Deduplication needs a stable logical operation identity and an enforcing record at the effect boundary. A restricted implementation can atomically commit a local mutation together with the operation’s identity and result. Repeated delivery of that identity then recovers the recorded result instead of repeating the mutation. If the record and effect commit independently, a crash between them recreates the ambiguity. Reusing an identity with different arguments must also be rejected or otherwise resolved by the declared contract.

Result retention bounds the guarantee. Once the endpoint discards the record, an old request must not silently become a new operation unless the contract permits that behavior. “Exactly once” is meaningful only with a stated effect boundary, identity scope, retention rule, and failure model; it does not imply eventual completion through indefinite outages. **[[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.06 Retrying Uncertain Actions#^sec-vol3-tool-calling-idempotency|Retrying Uncertain Actions]]** applies these distinctions to tool outcomes without treating a timeout as permission to repeat an effect.

## Leases and Fencing

^sec-vol3-appendix-systems-fencing

A worker pauses long enough to lose its lease. A replacement acquires ownership, but the old worker later resumes and sends a buffered write. The ownership service’s new grant does not itself stop that request at the resource.

A lease grants ownership for a bounded interval under a declared timing contract. A fencing token enables enforcement at the resource. One design attaches an authenticated ownership generation to requests and records the current generation at the resource. After the replacement’s generation is installed there, the resource rejects requests from older generations. The Chubby sequencer mechanism ([[05 Reference/Volume III - Agentic Systems/V3 Distributed State Foundations#^ref-burrows2006chubby|Burrows 2006]]) exemplifies resource-side validation of a lock generation.

We can test the handoff by delaying the old worker’s write until after installation of the new fence. Rejection demonstrates the intended exclusion for that trace. If the write arrives before installation, comparing generations alone cannot detect expiration of the old lease. That requires a lease-validity contract or a handoff protocol that establishes the fence before relying on exclusion.

The current holder can issue several distinct operations under the same generation; fencing does not deduplicate them. Nor does a larger integer establish authority unless the resource authenticates its grant. These distinctions keep ownership, repeat handling, and effect settlement separate. An implementation must enforce each guarantee where the corresponding state can change.

Back to top

## Source References

^source-references

Lamport, Leslie. 1978. “Time, Clocks, and the Ordering of Events in a Distributed System.” *Communications of the ACM* 21 (7): 558–65. https://doi.org/10.1145/359545.359563.

^ref-lamport1978time

Herlihy, Maurice P., and Jeannette M. Wing. 1990. “Linearizability: A Correctness Condition for Concurrent Objects.” *ACM Transactions on Programming Languages and Systems* 12 (3): 463–92. https://doi.org/10.1145/78969.78972.

^ref-herlihy1990linearizability

Gray, Jim. 1981. “The Transaction Concept: Virtues and Limitations.” *Proceedings of the Seventh International Conference on Very Large Data Bases (VLDB)* 7: 144–54.

^ref-gray1981transaction

Garcia-Molina, Hector, and Kenneth Salem. 1987. “Sagas.” *Proceedings of the 1987 ACM SIGMOD International Conference on Management of Data*, 249–59. https://doi.org/10.1145/38713.38742.

^ref-garciamolina1987sagas

Mohan, Chandrasekaran, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz. 1992. “ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging.” *ACM Transactions on Database Systems* 17 (1): 94–162. https://doi.org/10.1145/128765.128770.

^ref-mohan1992aries

Birrell, Andrew D., and Bruce Jay Nelson. 1984. “Implementing Remote Procedure Calls.” *ACM Transactions on Computer Systems* 2 (1): 39–59. https://doi.org/10.1145/2080.357392.

^ref-birrell1984rpc

Burrows, Mike. 2006. “The Chubby Lock Service for Loosely-Coupled Distributed Systems.” *USENIX Symposium on Operating Systems Design and Implementation (OSDI)*.

^ref-burrows2006chubby

## Source

[Repository Source](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/books/vol3/backmatter/appendix_systems.qmd) · [Original License](https://github.com/klappe-pm/cs249r_book/blob/de87c0103806d7bfb1c677dbb77a2b92fa00c298/LICENSE.md)

[Rendered Reading Snapshot](https://mlsysbook.ai/vol3/backmatter/appendix_systems.html#sec-vol3-appendix-systems). Rendering provenance is recorded in the import manifest.
