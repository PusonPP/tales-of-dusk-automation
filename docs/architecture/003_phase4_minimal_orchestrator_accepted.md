# 003 Phase 4 Minimal Orchestrator Accepted

## Purpose

Record the acceptance of Phase 4, which established the first minimal LangGraph orchestrator for the Tales of Dusk automated development workflow repository.

This document freezes the current accepted orchestration baseline so that later Codex task generation, approval gates, QA gating, remote automation entry points, and CI/CD integration can build on a stable workflow core rather than on informal assumptions.

Phase 4 does not introduce a full autonomous production system.  
Instead, it introduces the first accepted executable workflow graph that can consume the protocol/state baseline defined in Phase 3 and advance a minimal artifact chain in a controlled way.

---

## Scope of Acceptance

Phase 4 acceptance covers the following workflow orchestration baseline only:

- creation of the first executable LangGraph workflow graph,
- use of the canonical `WorkflowState` model as shared state,
- registration of minimal workflow nodes,
- definition of explicit stage transitions,
- definition of at least one conditional route,
- use of a minimal checkpointer,
- validation that the graph can advance a minimal example artifact chain,
- validation that the graph can terminate in `codex_tasking` on the approved happy path.

This acceptance does **not** include:

- live LLM generation,
- live Codex repository modification,
- markdown front matter parsing,
- interrupt/resume approval flow,
- repository write automation,
- GitHub Actions execution of the graph,
- automatic artifact registry management,
- gameplay system implementation,
- changes to the accepted Godot runtime skeleton.

---

## Accepted Orchestration Baseline

The repository now contains an accepted minimal orchestration baseline with the following characteristics.

### Shared State Model

The accepted orchestration graph uses:

```text
automation/langgraph/schemas/workflow_state.py
```

as the canonical shared workflow state model.

The accepted graph treats this state model as the primary contract for:

* current workflow stage,
* active artifact IDs,
* artifact history,
* blockers,
* open risks,
* approval requirements,
* repository context,
* runtime invariants.

### Accepted Graph Entry Point

The accepted graph builder is:

```text
automation/langgraph/graphs/minimal_orchestrator.py
```

This file is the current canonical minimal workflow graph entry point.

### Accepted Node Module

The accepted node implementation module is:

```text
automation/langgraph/nodes/minimal_orchestrator_nodes.py
```

This file is the current canonical node set for the minimal graph.

### Accepted Local Runner

The accepted local graph runner is:

```text
automation/scripts/run_minimal_orchestrator.py
```

This script provides the current local execution entry point for the Phase 4 minimal graph.

### Accepted Test File

The accepted workflow graph test file is:

```text
automation/langgraph/tests/test_minimal_orchestrator.py
```

This file is the canonical minimal automated test for graph progression.

---

## Accepted Graph Purpose

The accepted minimal graph exists to prove that the repository’s Phase 3 protocol and schema foundation can be consumed by an executable orchestrator.

Specifically, it proves that the repository can now support:

* deterministic workflow node execution,
* state mutation through graph progression,
* controlled routing based on state and artifact-derived decisions,
* promotion of workflow stage from planning toward `codex_tasking`,
* minimal checkpointer-backed execution.

This graph is intentionally narrow and deterministic.
It is not yet intended to simulate the full multi-role autonomous workflow.

---

## Accepted Minimal Happy Path

The accepted happy-path progression is:

```text
validate_repo_baseline
-> load_design_brief
-> register_proposal
-> register_review
-> register_approved_spec
-> promote_to_codex_tasking
```

This path is the current accepted baseline demonstration of protocol-aware orchestration.

The resulting accepted terminal workflow stage for the happy path is:

```text
codex_tasking
```

---

## Accepted Conditional Routing

Phase 4 acceptance requires the graph to include real routing logic rather than only a linear sequence.

The accepted minimal graph includes the following conditional routing points.

### Baseline Validation Route

After validating required repository files and baseline assumptions, the graph routes to either:

* `load_design_brief` if no blockers exist
* `halt_on_blocker` if blockers exist

### Review Outcome Route

After registering the review artifact, the graph routes to either:

* `register_approved_spec` if the review outcome is `approve`
* `rollback_stop` if the review outcome does not approve progression

This routing behavior is now part of the accepted Phase 4 orchestration baseline.

---

## Accepted Example Artifact Chain

The accepted graph currently depends on the repository example chain defined in:

* `docs/examples/BRF-0001_bootstrap-protocols_v1.0.0.md`
* `docs/examples/PRP-0001_protocol-schema_v1.0.0.md`
* `docs/examples/RVW-0001_protocol-schema_v1.0.0.md`
* `docs/examples/SPEC-0001_protocol-schema_v1.0.0.md`

This is an accepted repository bootstrap chain for orchestration testing only.

These example artifacts are **not** accepted as game design content.
They are accepted only as workflow/protocol validation fixtures.

---

## Accepted Runtime Invariants Consumed by the Graph

The accepted graph consumes runtime invariants from `WorkflowState`, including at minimum:

* main scene path
* title scene path
* chapter map scene path
* room test scene path
* required Autoload list
* canonical room phase order

This means the graph is now aware of the accepted repository runtime baseline established in Phase 2.

However, Phase 4 does **not** give the graph authority to rewrite those invariants or alter the accepted Godot baseline.

---

## Accepted Checkpointer Baseline

The accepted minimal graph uses a minimal checkpointer approach based on:

```text
InMemorySaver
```

This is accepted for the current phase because Phase 4 only needs lightweight local orchestration validation.

Phase 4 does **not** yet accept:

* persistent production checkpoint storage,
* cross-session durable resume,
* remote workflow state persistence,
* long-running interrupt/resume execution.

Those are future-phase concerns.

---

## What Was Explicitly Validated

Phase 4 acceptance is based on the following validated assumptions and checks.

### Structural Validation

The repository contains:

* a graph builder module,
* a node module,
* a local runner,
* a graph test file,
* the shared workflow state schema used by the graph.

### Execution Validation

The graph can be built and compiled successfully.

The graph can be invoked locally from the repository.

The happy path can progress from an initial `WorkflowState` to a terminal state where:

* `current_stage == codex_tasking`
* `design_brief` is registered
* `proposal` is registered
* `review` is registered
* `approved_spec` is registered
* `blockers == []`

### Automated Validation

Minimal test coverage exists and passes for the accepted orchestration baseline.

This includes:

* graph progression assertions
* state mutation expectations
* basic workflow state validation inherited from earlier tests

---

## Known Limitations at Acceptance Time

This acceptance intentionally preserves several known limitations.

### Orchestration Limitations

* the graph is deterministic and fixture-driven
* no live model calls are made
* no proposal/review/spec content is generated dynamically
* no markdown front matter is parsed into structured schema objects
* the graph relies on simple repository example artifacts
* review outcome extraction is minimal and repository-specific

### Approval Limitations

* no interrupt/resume human approval flow exists yet
* no explicit human approval node exists yet
* no durable approval checkpointing exists yet

### Codex Limitations

* the graph terminates at `codex_tasking`
* no real Codex task dispatch occurs yet
* no repository modification is triggered by the graph

### Integration Limitations

* no GitHub Actions invocation of the graph exists yet
* no remote execution path exists yet
* no CI gating consumes graph output yet

These limitations are acceptable because Phase 4 only aims to establish the first accepted executable orchestration core.

---

## Why This Baseline Is Accepted

Phase 4 is accepted because it successfully converts the Phase 3 protocol/state layer into the first executable workflow graph.

Specifically, it establishes:

* one accepted minimal orchestration graph,
* one accepted node set,
* one accepted local graph runner,
* one accepted graph happy path,
* one accepted conditional routing baseline,
* one accepted graph checkpointer strategy for local validation,
* one accepted link between protocol artifacts and executable orchestration behavior.

This is sufficient for:

* Phase 5 Codex entry integration,
* later approval/interrupt design,
* later task generation automation,
* later CI/CD workflow integration,
* later graph expansion into more realistic multi-role flow.

without prematurely introducing live autonomous execution.

---

## Baseline Protection Rules

The following rules apply after this acceptance.

### Rule 1

Later workflow phases must treat this minimal graph as the active orchestration baseline unless a newer approved architecture record supersedes it.

### Rule 2

Any change to the following requires explicit review and likely a change request:

* shared workflow state semantics,
* accepted happy-path terminal stage,
* accepted node responsibilities,
* accepted routing semantics,
* accepted fixture chain assumptions,
* accepted checkpointer baseline.

### Rule 3

Later phases may extend the graph, but should not silently break the accepted Phase 4 happy path.

### Rule 4

If later work discovers that the accepted graph baseline is incomplete or inconsistent, the correction must be recorded rather than silently assumed.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton.

Phase 4 does not replace that runtime baseline.
Instead, it consumes selected runtime invariants as part of workflow state awareness.

The graph must not silently modify or invalidate the accepted Phase 2 runtime assumptions.

### Relationship to Phase 3

Phase 3 established:

* canonical workflow document protocol,
* workflow stage semantics,
* artifact lifecycle rules,
* machine-readable schema layer,
* shared workflow state baseline.

Phase 4 depends directly on those outputs and is accepted only because it successfully consumes them in executable form.

---

## Relationship to Later Phases

### Phase 5

Phase 5 may connect Codex local and remote work entry points, but should treat the accepted Phase 4 graph as the current orchestration core.

Phase 5 may add Codex entry integration, but should not silently replace the Phase 4 graph with a materially different execution model.

### Later Phases

Later phases may add:

* Codex task generation nodes,
* interrupt/resume approval gates,
* persistent checkpointing,
* CI/CD-triggered orchestration,
* richer artifact loading/parsing,
* more realistic multi-role orchestration,
* validation against live repository state and generated artifacts.

Any such expansion should supersede this baseline only when explicitly approved.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it,
* the orchestration graph is intentionally restructured through controlled review,
* the repository adopts a newer accepted orchestration baseline.

Until then, this document is the canonical accepted orchestration baseline for Phase 4.

---

## Status

Recommended status for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as an active architecture acceptance record for the current repository orchestration baseline.