# 002 Phase 3 Protocol and State Scope

## Purpose

Record the scope boundary for Phase 3 of the Tales of Dusk automated development workflow repository.

Phase 3 exists to define the protocol layer and shared workflow state layer that later automation phases will rely on.  
Its role is to establish the canonical document contract, artifact lifecycle model, stage control semantics, and machine-readable state/schema foundation for the future LangGraph/Codex/GitHub Actions workflow.

This record prevents a common failure mode: trying to build executable orchestration before the repository has a stable protocol and state contract.

---

## Phase 3 Mission

The mission of Phase 3 is:

- define the canonical workflow document protocol,
- define canonical artifact types and lifecycle states,
- define canonical workflow stage semantics,
- define machine-readable schema models for workflow artifacts,
- define one shared workflow state model for LangGraph orchestration,
- create minimal example artifacts proving that the protocol chain is coherent,
- create minimal validation utilities and tests for the schema layer.

Phase 3 is a **workflow infrastructure phase**, not a gameplay phase.

---

## Why Phase 3 Exists

The repository already has:

- a Phase 1 repository foundation,
- a Phase 2 accepted Godot runtime skeleton.

However, later automation phases require more than a runnable Godot project. They require a formal contract for:

- what artifacts exist,
- how artifacts are identified,
- how artifacts evolve,
- what stage the workflow is in,
- what approvals are required,
- what information is allowed to reach Codex,
- when the workflow must stop, roll back, or request human approval.

Without this layer, future automation would rely on implicit conventions, unstable prompts, and hidden assumptions.

Phase 3 exists to eliminate that ambiguity.

---

## Accepted Scope for Phase 3

Phase 3 is explicitly in scope for the following work.

### 1. Protocol Documentation

Phase 3 defines repository-level protocol documents, including:

- artifact type definitions,
- artifact lifecycle states,
- artifact versioning rules,
- traceability rules,
- storage rules,
- approval rules,
- supersession rules,
- workflow stage flow rules,
- rollback rules,
- interrupt / human approval rules.

This includes, at minimum:

- `docs/protocols/automation_protocol.md`
- `docs/protocols/workflow_stage_machine.md`

---

### 2. Artifact Templates

Phase 3 defines reusable template files for canonical workflow artifacts.

This includes templates for:

- Design Brief
- Proposal
- Review
- Approved Spec
- Codex Task
- QA Report
- Acceptance Report
- Change Request

These templates are human-readable authoring guides and repository conventions.

---

### 3. Machine-Readable Schema Layer

Phase 3 defines machine-readable schema models for workflow artifacts.

This includes:

- canonical enums,
- shared common models,
- reusable item models,
- artifact-specific schema classes,
- one canonical workflow state model.

This schema layer is intended to be used later by LangGraph nodes, validation tools, and workflow automation logic.

---

### 4. Shared Workflow State Model

Phase 3 defines the canonical `WorkflowState` model used to represent:

- current workflow stage,
- active artifact IDs,
- artifact history,
- open risks,
- blockers,
- human approval requirements,
- repository context,
- runtime invariants.

This is the state contract that later orchestration must obey.

---

### 5. Example Artifacts

Phase 3 defines minimal example artifacts that demonstrate a valid early-stage chain such as:

- Design Brief
- Proposal
- Review
- Approved Spec

These examples are not game content.  
They exist to validate the protocol itself.

---

### 6. Validation Utilities and Tests

Phase 3 includes minimal local validation capability for the protocol/schema layer.

This includes:

- local schema validation scripts,
- basic pytest coverage for state and schema import/validation,
- proof that the initial protocol/state layer can be instantiated and checked locally.

---

## Explicitly Out of Scope for Phase 3

The following are **not** part of Phase 3.

### 1. LangGraph Runtime Graph Implementation

Phase 3 does **not** build the actual LangGraph graph.

That means Phase 3 does not include:

- real node graph construction,
- edge routing logic,
- graph compilation,
- checkpoint persistence behavior,
- live interrupt/resume flow,
- threaded workflow execution.

Those belong to the next phase.

---

### 2. Live Codex Execution

Phase 3 does **not** execute Codex against the repository.

That means Phase 3 does not include:

- automatic code generation,
- automated file modifications by Codex,
- live Codex task dispatch,
- repository write actions performed by Codex,
- Codex-in-CI execution.

Phase 3 may define the `Codex Task` artifact, but it does not run it.

---

### 3. GitHub Actions Automation Logic

Phase 3 does **not** build CI automation yet.

That means Phase 3 does not include:

- workflow YAML for validation jobs,
- artifact validation in CI,
- Codex GitHub Action integration,
- Godot smoke tests in CI,
- release/build/export jobs.

Those are later-phase concerns.

---

### 4. Gameplay Feature Development

Phase 3 does **not** implement gameplay systems.

That means it does not include:

- deployment logic,
- combat logic,
- waves,
- chapter progression,
- save progression design,
- room data loading,
- balancing,
- content production,
- environment interactions,
- final UI flow.

---

### 5. Runtime Skeleton Restructuring

Phase 3 does **not** intentionally restructure the accepted Phase 2 Godot baseline.

That means it should not change:

- main scene path,
- accepted scene flow,
- accepted required Autoloads,
- accepted room phase order,
- accepted project root assumptions,

unless a separate controlled review explicitly justifies that change.

---

## Canonical Deliverables of Phase 3

Phase 3 is considered complete only if the following deliverables exist.

### Protocol Documents
- `docs/protocols/automation_protocol.md`
- `docs/protocols/workflow_stage_machine.md`

### Template Files
- `docs/templates/design_brief.md`
- `docs/templates/proposal.md`
- `docs/templates/review.md`
- `docs/templates/approved_spec.md`
- `docs/templates/codex_task.md`
- `docs/templates/qa_report.md`
- `docs/templates/acceptance_report.md`
- `docs/templates/change_request.md`

### Example Artifacts
- at least one valid example chain in `docs/examples/`

### Schema Layer
- `automation/langgraph/schemas/enums.py`
- `automation/langgraph/schemas/common.py`
- `automation/langgraph/schemas/items.py`
- `automation/langgraph/schemas/workflow_state.py`
- artifact-specific schema files
- `automation/langgraph/schemas/__init__.py`

### Validation Layer
- minimal validation utility under `automation/scripts/`
- minimal test coverage under `automation/langgraph/tests/`

---

## Required Constraints During Phase 3

The following constraints apply throughout Phase 3.

### Constraint 1
Protocol definitions must remain consistent with the accepted repository baseline and current project reality.

### Constraint 2
Schema models must be serializable and validation-friendly.

### Constraint 3
Schema design must prefer explicitness over hidden conventions.

### Constraint 4
Protocol and schema work must not assume that a future graph implementation is already correct.

### Constraint 5
Human-readable templates and machine-readable schemas must agree semantically.

### Constraint 6
Phase 3 work must not silently extend into executable orchestration.

### Constraint 7
Phase 3 must preserve the accepted Phase 2 runtime baseline.

---

## Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton:

- canonical project root,
- canonical scene flow,
- canonical Autoload set,
- canonical room phase order.

Phase 3 depends on that accepted baseline and must treat it as an existing runtime invariant.

The protocol/state layer introduced in Phase 3 should reference that runtime baseline, not replace it.

Examples:
- `WorkflowState` may record runtime invariants,
- protocol rules may protect accepted paths and baseline assumptions,
- validation tools may use the Phase 2 baseline as expected repository structure.

---

## Relationship to Phase 4

Phase 4 will build the first actual LangGraph orchestration layer.

Phase 4 should consume Phase 3 outputs, not redefine them.

That means Phase 4 should reuse:

- protocol document rules,
- canonical artifact type semantics,
- lifecycle statuses,
- workflow stage definitions,
- `WorkflowState`,
- artifact schemas,
- validation assumptions established in Phase 3.

If Phase 4 discovers that Phase 3 assumptions are insufficient, it must extend or revise them through a controlled architecture/protocol update, not silently ignore them.

---

## Repository Areas In Scope

Phase 3 primarily affects the following repository areas:

```text
docs/protocols/
docs/templates/
docs/examples/
automation/langgraph/schemas/
automation/langgraph/tests/
automation/scripts/
```

These are the expected primary surfaces of change.

---

## Repository Areas Protected During Phase 3

The following repository areas should remain stable during Phase 3 except for minimal metadata updates:

```text
game/tales-of-dusk/project.godot
game/tales-of-dusk/scenes/
game/tales-of-dusk/scripts/
```

The Godot runtime skeleton is not the target of this phase.

Minor metadata synchronization may happen, but Phase 3 should not become a disguised gameplay or runtime refactor phase.

---

## Risks Recognized in Phase 3

### Risk 1: Over-specification

The protocol may become too rigid before real workflow execution reveals what is actually needed.

### Risk 2: Under-specification

The protocol may omit fields later required by real LangGraph nodes, Codex tasking, or QA gating.

### Risk 3: Drift Between Markdown and Schemas

Human-readable documents and machine-readable schemas may diverge unless kept aligned.

### Risk 4: Premature Automation Pressure

There may be pressure to start implementing LangGraph logic or Codex execution before the schema layer is stable.

### Risk 5: Hidden Runtime Coupling

Future automation may incorrectly assume runtime details not explicitly recorded as invariants.

These risks are acceptable within Phase 3 as long as they are documented and do not trigger hidden scope expansion.

---

## Acceptance Criteria for Phase 3

Phase 3 is accepted only if all of the following are true.

### AC-001

Canonical protocol documents exist and define artifact semantics and stage flow clearly.

### AC-002

Canonical template files exist for all initial artifact types.

### AC-003

Machine-readable schema files exist for the artifact layer and shared workflow state layer.

### AC-004

A valid `WorkflowState` can be instantiated locally.

### AC-005

Minimal example artifacts exist and match the intended workflow chain semantics.

### AC-006

Minimal schema validation and pytest checks pass locally.

### AC-007

Phase 2 runtime baseline remains intact.

### AC-008

No Phase 4 behavior has been silently implemented under the Phase 3 label.

---

## Non-Goals

To remove ambiguity, the following are explicit non-goals for Phase 3:

* “just start wiring LangGraph now”
* “just let Codex begin editing files now”
* “just add quick CI so later we don’t forget”
* “just implement a little gameplay while we’re here”
* “just restructure the runtime skeleton before automation starts”

Those are all outside this phase boundary.

---

## Phase 3 Decision

The repository will treat Phase 3 as a protocol-and-state-definition phase only.

Execution infrastructure is intentionally deferred.

This decision is made to maximize:

* clarity,
* traceability,
* future workflow stability,
* controlled evolution of the automation stack,
* protection against hidden architecture drift.

---

## Supersession Policy

This record remains active until it is superseded by a later approved architecture record that explicitly changes the scope boundary for protocol/state work or the order of subsequent automation phases.

Until then, it is the canonical scope record for Phase 3.

---

## Status

Recommended metadata for this architecture record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as the authoritative scope boundary for Phase 3 work in this repository.