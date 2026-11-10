---
title: Reliability and Recovery
type: theme
tags:
- Type/Theme
- Theme/Reliability_and_Recovery
source_repository: https://github.com/klappe-pm/cs249r_book
source_commit: de87c0103806d7bfb1c677dbb77a2b92fa00c298
source_path: taxonomy/taxonomy.yml
editorial_scope: Curated Navigation Lens
---

# Reliability and Recovery

Connect recovery state, failure boundaries, replay, and production rollback without conflating local recovery with undone external effects.

This curated navigation lens is an editorial association, not a claim of dependency or equivalence.

## Concepts

- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Recovery Checkpoint|Recovery Checkpoint]] — A persisted state from which a specified computation can resume.
- [[02 Concepts/Stack/Datacenter Infrastructure & Fleet/Checkpoint IO|Checkpoint IO]] — Writing and reading large training-state snapshots, where storage bandwidth, asynchronous persistence, and sharded layout determine checkpoint cost.
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Optimal Checkpoint Interval|Optimal Checkpoint Interval]] — The checkpoint period that minimizes expected lost time, balancing checkpoint write cost against expected rework, approximately the square root of twice the write cost times MTBF.
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Asynchronous Checkpointing|Asynchronous Checkpointing]] — Snapshotting training state quickly to host memory and persisting it in the background so computation resumes before the durable write completes.
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Idempotency|Idempotency]] — A specified operation's repeated execution having the same intended effect as one execution.
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Retry with Backoff|Retry with Backoff]] — Reissuing a failed request after increasing, typically jittered, delays and within a retry budget, so that transient faults recover without overloading dependencies.
- [[02 Concepts/Foundations/Workloads & Requirements/Recovery Time and Point Objectives|Recovery Time and Point Objectives]] — Stated limits on how long restoring service may take (RTO) and how far recovered state may lag the state before the failure (RPO), which constrain checkpointing, replication, and failover design.
- [[02 Concepts/Qualities/Reliability & Fault Tolerance/Restart Free Failure Recovery|Restart Free Failure Recovery]] — Reconfiguring distributed training around surviving replicas of model and optimizer state so that the job resumes after supported worker failures without a full-job restart or durable-checkpoint reload, reducing recovery delay at the cost of redundancy and reconfiguration.
- [[02 Concepts/Lifecycle/MLOps & Operations/Rollback|Rollback]] — Returning to a previously accepted deployment configuration with compatible state.

## Connected Book Passages

- [[01 Books/Volume I - Foundations/04 Deployment/14 ML Operations/V1-14.05 Releasing Models#^sec-ml-operations-rollback-strategies-safety-mechanisms-7707|V1-14.05 Releasing Models]]
- [[01 Books/Volume II - Scaling/01 The Fleet/04 Data Storage/V2-04.07 Checkpoint Storage#^sec-storage-checkpointing|V2-04.07 Checkpoint Storage]]
- [[01 Books/Volume III - Agentic Systems/03 Tool Use/07 Tool Calling/V3-07.06 Retrying Uncertain Actions#^sec-vol3-tool-calling-operation-ids|V3-07.06 Retrying Uncertain Actions]]
- [[01 Books/Volume III - Agentic Systems/04 The Agent Runtime/11 Durable Execution/V3-11.05 Checkpoints#^sec-vol3-persistence-checkpointing|V3-11.05 Checkpoints]]

## Navigation

[[00 Navigation/Topic Index|Topic Index]]
