# AGENTS.md

## Scope

This file governs work inside the automation subtree:

```text
automation/
```

It refines the repository-root `AGENTS.md` with **workflow orchestration, schema, state, validation, and Codex-entry-specific rules**.

If any instruction conflicts with the repository root `AGENTS.md`, the stricter rule wins.

If any instruction conflicts with accepted architecture records, protocol documents, or protected workflow baselines, those repository governance documents win.

---

## Mission of This Subtree

This subtree contains the automation layer for the repository.

Its purpose is to support and evolve:

* workflow protocol enforcement,
* machine-readable artifact schemas,
* shared workflow state,
* LangGraph orchestration logic,
* local validation utilities,
* future Codex task generation and execution scaffolding.

This subtree is **not** a place for unconstrained experimental automation.

All work here must assume:

* the repository is governed by explicit workflow phases,
* automation is subordinate to protocol and architecture,
* automation changes can alter repository authority boundaries,
* small-looking automation changes may have large systemic consequences.

Treat this subtree as infrastructure, not convenience scripting.

---

## Current Accepted Automation Baseline

The repository currently has the following accepted automation baselines.

### Accepted Phase 3 Baseline

The repository has accepted:

* protocol documents,
* artifact templates,
* example artifacts,
* canonical enums,
* common schema models,
* item schema models,
* artifact-specific schema models,
* canonical `WorkflowState`,
* minimal validation utilities and tests.

### Accepted Phase 4 Baseline

The repository has accepted:

* one minimal LangGraph graph,
* one accepted node module,
* one accepted local graph runner,
* one accepted happy path terminating in `codex_tasking`,
* one accepted minimal checkpointer strategy.

### Phase 5 Scope

Phase 5 may connect Codex entry paths, but automation changes still must not grant unrestricted autonomous implementation authority.

---

## Source-of-Truth Files for This Subtree

Before modifying automation files, consult at minimum:

### Architecture

* `docs/architecture/002_phase3_protocol_state_scope.md`
* `docs/architecture/003_phase4_minimal_orchestrator_accepted.md`
* `docs/architecture/004_phase5_codex_entry_scope.md`

### Protocol

* `docs/protocols/automation_protocol.md`
* `docs/protocols/workflow_stage_machine.md`

### Root Governance

* repository root `AGENTS.md`

### Shared State and Schemas

* `automation/langgraph/schemas/workflow_state.py`
* `automation/langgraph/schemas/`

If an automation change conflicts with those files, stop and surface the conflict.

---

## Automation Operating Principle

This subtree must evolve under a “protocol-first, state-first, graph-second, execution-last” principle.

That means:

1. preserve protocol meaning,
2. preserve schema meaning,
3. preserve accepted workflow state semantics,
4. preserve accepted graph stage semantics,
5. prefer deterministic bounded behavior,
6. avoid hidden authority expansion.

Do not optimize for cleverness at the cost of repository control.

---

## Hard Automation Rules

### Rule 1: Do not silently change protocol meaning

If a code change alters the meaning of:

* artifact types,
* artifact lifecycle statuses,
* stage semantics,
* traceability rules,
* supersession rules,
* approval assumptions,

then it is not a small code tweak.
It is a protocol change and must be treated as such.

### Rule 2: Do not silently change `WorkflowState` semantics

`WorkflowState` is part of the current accepted workflow contract.

Do not casually:

* rename fields,
* repurpose fields,
* remove fields,
* inject runtime-only objects,
* change stage meaning,
* change state assumptions,

without explicit justification and schema discipline.

### Rule 3: Do not turn deterministic graph behavior into model-driven behavior casually

The accepted Phase 4 graph is deterministic and fixture-driven.

Do not silently introduce:

* live LLM calls,
* dynamic proposal generation,
* live review generation,
* autonomous content writing,
* hidden network dependency,

unless explicitly approved by later-phase scope.

### Rule 4: Do not grant Codex more authority than the repository has approved

Codex-facing automation must remain subordinate to:

* approved scope,
* task boundaries,
* file boundaries,
* branch safety,
* human oversight.

Automation code must not assume “if Codex can run, it can implement anything.”

### Rule 5: Do not introduce hidden persistence semantics

A small change to checkpointing, state shape, or resume behavior can change workflow meaning.

Do not introduce durable persistence, cross-session assumptions, or hidden restore behavior casually.

### Rule 6: Prefer bounded, inspectable graph logic

Workflow routing must remain explicit and reviewable.

### Rule 7: Tests must follow automation changes

Meaningful changes to schema, state, graph routing, or validation utilities should be accompanied by tests or validation updates.

### Rule 8: Avoid speculative framework expansion

Do not add agent servers, tool registries, task dispatch frameworks, registry services, or general workflow abstractions “for future-proofing” unless they are explicitly in scope.

---

## Subtree Layout Meaning

The automation subtree is currently expected to contain areas such as:

```text
automation/
├─ langgraph/
│  ├─ schemas/
│  ├─ nodes/
│  ├─ graphs/
│  ├─ tests/
│  └─ checkpoints/
├─ codex/
│  ├─ templates/
│  └─ policies/
└─ scripts/
```

### `automation/langgraph/schemas/`

Canonical machine-readable data model layer.
High sensitivity.

### `automation/langgraph/nodes/`

Node implementations for orchestration logic.
Sensitive.

### `automation/langgraph/graphs/`

Graph builders and route composition.
High sensitivity.

### `automation/langgraph/tests/`

Validation of schema and graph behavior.
Should evolve with automation changes.

### `automation/langgraph/checkpoints/`

Checkpoint-related local assets or placeholders.
Do not treat as production persistence without explicit approval.

### `automation/codex/`

Codex-facing templates or policy helpers.
Should remain subordinate to repository protocol.

### `automation/scripts/`

Local utility entry points and validation runners.
Should remain narrow and explicit.

---

## Schema Rules

### Schema Layer Is a Contract

Files under:

```text
automation/langgraph/schemas/
```

define repository automation contracts, not loose helper structures.

### Use Explicit Pydantic Models

Prefer:

* clear fields,
* explicit types,
* serializable values,
* `extra="forbid"` unless there is a deliberate reason otherwise.

### No Runtime Objects in Schema

Do not put the following into schema/state objects:

* Godot node instances
* open file handles
* network clients
* process objects
* callable functions
* arbitrary opaque objects

Keep schema/state values serializable and workflow-safe.

### Structure Over Free-Form Blobs

Do not replace structured models with raw dictionaries or long free-form strings unless absolutely justified.

### Schema Meaning Changes Require Discipline

If you materially change a schema’s meaning:

* update tests,
* update documentation,
* consider schema/version implications,
* surface compatibility impact explicitly.

---

## Workflow State Rules

### `WorkflowState` Is Shared Workflow Memory

It is the accepted state contract for orchestration.

It should capture:

* stage,
* active artifact references,
* history,
* blockers,
* risks,
* approval requirements,
* repository context,
* runtime invariants.

### Do Not Inflate State Into a Dumping Ground

Do not use `WorkflowState` as a place to store:

* arbitrary logs,
* huge markdown bodies,
* unrelated convenience flags,
* secret operational state,
* experimental garbage fields.

### Keep Stage Semantics Stable

`current_stage` must remain aligned with the canonical stage machine.

Do not casually invent new stage meanings in implementation code only.

---

## Graph Rules

### Preserve Accepted Stage Order

The accepted canonical order is controlled by protocol and architecture records.

Graph code must not silently permit forbidden transitions.

### Routing Must Be Explicit

Conditional routing should be understandable and reviewable.

Avoid hidden magic behavior or overly implicit graph branching.

### Do Not Collapse All Logic Into One Node

Keep responsibilities separated enough that:

* blockers are inspectable,
* routing is understandable,
* state changes remain attributable.

### Do Not Over-Abstract Prematurely

Avoid introducing large orchestration frameworks when the repository only needs bounded graph evolution.

### Protect the Accepted Happy Path

The current accepted minimal happy path must not be silently broken.

If the graph changes meaningfully, document it and test it.

---

## Validation Script Rules

### Validation Scripts Must Be Narrow

Scripts under:

```text
automation/scripts/
```

should do one explicit job each.

### Prefer Module-Style Execution

Where appropriate, scripts should be runnable as Python modules from repository root.

### Do Not Hide Write Operations

A script named “validate” or “check” must not perform unexpected repository mutations.

### Validation Output Should Be Human-Useful

Validation scripts should make it clear:

* what was checked,
* whether it passed,
* what failed if not.

---

## Codex-Automation Rules

### Codex Integration Is Controlled

This subtree may prepare Codex entry and tasking, but must not silently grant Codex broad autonomy.

### No Real Task Execution Without Authority

Do not wire actual write-capable Codex execution into repository flow without:

* accepted branch policy,
* explicit safety assumptions,
* task boundary discipline,
* review of remote/local execution path.

### Prompt Assets Are Versioned Inputs

Prompt templates and policy helpers are repository assets.
Do not treat them as disposable scratch text.

### Codex Task Generation Must Stay Bounded

When later phases generate Codex tasks, they must remain tightly scoped and traceable to approved specs.

---

## Safe Default Work in This Subtree

Without higher-level explicit approval, safer kinds of work here include:

* protocol/schema clarification,
* adding or refining tests,
* bounded graph bug fixes,
* improving deterministic routing,
* fixing import/path issues,
* improving validation scripts,
* strengthening prompt-file discipline,
* clarifying automation documentation,
* small tooling fixes aligned with accepted semantics.

---

## Sensitive Work in This Subtree

Treat the following as sensitive and higher review risk:

* changing `WorkflowState`,
* changing stage enum values,
* changing graph routing semantics,
* changing blocker logic,
* changing checkpointer assumptions,
* changing protocol/schema correspondence,
* introducing model calls,
* introducing real Codex execution,
* changing remote automation trust assumptions.

---

## Default Forbidden Work in This Subtree

Without explicit approval, do **not**:

* introduce live model dependencies into accepted deterministic graph paths,
* add broad autonomous task execution,
* convert validation scripts into hidden mutators,
* rewrite schema layer into generic untyped blobs,
* add production persistence assumptions,
* broaden Codex authority,
* bypass protocol/state discipline,
* treat example artifacts as production truth,
* create hidden branch-writing behavior.

---

## Review Guidance for Automation Changes

When reviewing changes under this subtree, prioritize the following questions:

### 1. Did the change preserve protocol meaning?

Check whether artifact and stage semantics remain aligned with the docs.

### 2. Did the change preserve `WorkflowState` meaning?

Check whether fields still mean what the repository assumes they mean.

### 3. Did the graph remain explicit?

Check whether routes, blockers, and state updates are still inspectable.

### 4. Did the change expand authority?

Check whether Codex, workflow code, or scripts gained more power than intended.

### 5. Did tests follow the change?

Check whether schema and graph behavior are still validated.

### 6. Did the change introduce hidden external dependency?

Check for silent network calls, hidden model use, or unapproved tooling assumptions.

### 7. Did the change preserve accepted happy path behavior?

Check whether the currently accepted graph still reaches the intended stage on the valid example chain.

---

## Output Contract for Automation Work

For any meaningful automation modification or review, include all of the following:

### Summary

What changed in the automation subtree.

### Files Changed

Exact automation files touched.

### Risks Introduced

Any protocol, state, graph, or authority risk introduced.

### Intentionally Not Changed

What important automation areas were left untouched.

### Manual Verification Steps

How a human should verify the result.

For example, verification may include:

* run schema validation script,
* run pytest for automation tests,
* run minimal orchestrator,
* inspect stage result,
* inspect blockers,
* confirm no unexpected file writes occurred.

---

## Manual Verification Expectations

When automation behavior is affected, expected manual verification should usually include relevant checks such as:

* `python -m automation.scripts.validate_protocols`
* `pytest automation\langgraph\tests -q`
* `python -m automation.scripts.run_minimal_orchestrator`
* confirm accepted happy path still reaches `codex_tasking`
* confirm blockers behave as expected when routing fails
* confirm no protected runtime baseline was touched unintentionally

Do not claim automation stability without corresponding checks.

---

## Human Approval Triggers in This Subtree

Stop and require explicit human approval if the work would affect:

* canonical workflow stage semantics,
* `WorkflowState` meaning,
* artifact protocol meaning,
* Codex authority boundaries,
* checkpoint/persistence meaning,
* remote execution trust model,
* CI/CD safety assumptions,
* automatic repository write behavior.

If in doubt, escalate rather than improvising.

---

## What This Subtree Is Not

Do not treat `automation/` as:

* an experimental AI sandbox,
* a place to build autonomous behavior just because it is possible,
* a dumping ground for generic utilities,
* a place where examples become production logic,
* an excuse to bypass repository governance.

It is a protected infrastructure subtree inside a governed automation repository.

---

## Practical Default Operating Mode for This Subtree

Unless the task explicitly authorizes more:

* inspect first,
* preserve protocol meaning,
* preserve `WorkflowState`,
* preserve accepted graph behavior,
* keep scripts narrow,
* keep authority bounded,
* prefer deterministic behavior,
* document any compatibility or authority risk clearly.

If uncertain whether a change is “small” or “workflow-semantic”, treat it as workflow-semantic.

---

## Conflict Resolution Rule

If there is conflict between:

* a convenience refactor,
* a clever workflow abstraction,
* a new agent idea,
* a prompt asking for more automation,
* or a temptation to “just wire it up now”,

and:

* protocol documents,
* accepted workflow state semantics,
* accepted graph baseline,
* root `AGENTS.md`,
* architecture records,

then the protected workflow baseline wins.

---

## Final Operating Instruction

Inside this subtree, correctness of workflow meaning comes first.

Preserve protocol discipline.

Preserve state discipline.

Preserve bounded authority.

Do not casually expand automation power.

When in doubt, keep the automation layer explicit, deterministic, and reviewable.