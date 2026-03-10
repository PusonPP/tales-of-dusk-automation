---
artifact_id: SPEC-0001
artifact_type: approved_spec
version: 1.0.0
status: approved
project_id: tales-of-dusk-automation
workflow_thread_id: bootstrap-phase3
author_role: TechnicalLead
created_at: 2026-03-09T00:30:00Z
updated_at: 2026-03-09T00:30:00Z
supersedes: null
related_artifacts:
  - BRF-0001
  - PRP-0001
  - RVW-0001
---

# Approved Spec: Protocol Schema and Shared Workflow State Baseline

## Approved Objective

Define the initial protocol and schema baseline required for the automated development workflow so that future LangGraph orchestration, Codex task generation, QA gating, and acceptance logic can operate on stable, explicit, machine-readable structures.

## Constraints

- The current accepted Godot Phase 2 runtime skeleton must remain intact.
- This scope must not introduce gameplay features or content design.
- The workflow must retain explicit artifact boundaries instead of using one monolithic generic schema.
- The schema layer must be serializable and suitable for future automated validation.
- The protocol must support future rollback, approval, and supersession behavior.
- No execution graph implementation is included in this scope.

## Functional Scope

This approved scope includes:

- defining canonical artifact types,
- defining canonical artifact headers,
- defining canonical artifact lifecycle states,
- defining canonical versioning expectations,
- defining canonical stage flow,
- defining machine-readable schemas for protocol artifacts,
- defining one canonical shared workflow state model,
- creating example artifacts that demonstrate early-stage workflow flow,
- adding protocol validation tests.

## Technical Mapping

The following repository areas are in scope:

- `docs/protocols/`
- `docs/templates/`
- `docs/examples/`
- `automation/langgraph/schemas/`
- `automation/langgraph/tests/`
- `automation/scripts/validate_protocols.py`

The schema layer must include:

- canonical enums,
- shared common models,
- workflow state model,
- artifact-specific schema models,
- minimal validation tests.

## Non-goals

The following are explicitly out of scope:

- LangGraph runtime graph implementation
- Codex live execution integration
- GitHub Actions workflow implementation
- automated markdown front matter parsing
- repository-wide artifact registry service
- gameplay feature implementation
- scene structure changes to the accepted Godot skeleton

## Acceptance Criteria

### AC-001
A canonical protocol document exists describing artifact types, lifecycle states, versioning, storage rules, and traceability rules.

### AC-002
A canonical workflow stage machine document exists describing valid stage order, allowed transitions, forbidden transitions, and rollback rules.

### AC-003
A machine-readable `WorkflowState` schema exists and validates successfully.

### AC-004
Artifact-specific schema files exist for:
- Design Brief
- Proposal
- Review
- Approved Spec
- Codex Task
- QA Report
- Acceptance Report
- Change Request

### AC-005
At least one minimal example artifact chain exists and is consistent with the protocol.

### AC-006
Local schema tests pass.

### AC-007
The accepted Godot runtime skeleton from Phase 2 is not broken by this scope.

## Required Tests

- Import and instantiate `WorkflowState`
- Validate canonical artifact header model
- Validate at least one artifact-specific schema instance
- Confirm local protocol validation script runs successfully
- Confirm existing Godot project structure remains unchanged in required runtime baseline areas

## Open Risks

- Future real workflow execution may reveal missing schema fields.
- Future change-request handling may require richer compatibility metadata.
- Future CI integration may impose stricter validation on example artifact headers.

## Approval Note

This specification is approved for Phase 3 implementation.  
Any attempt to extend this scope into executable agent graph logic, live Codex execution, or CI automation must be treated as a later phase and requires a new upstream proposal/review/spec chain.