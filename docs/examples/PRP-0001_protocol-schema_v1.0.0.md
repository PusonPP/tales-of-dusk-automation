---
artifact_id: PRP-0001
artifact_type: proposal
version: 1.0.0
status: draft
project_id: tales-of-dusk-automation
workflow_thread_id: bootstrap-phase3
author_role: TechnicalLead
created_at: 2026-03-09T00:10:00Z
updated_at: 2026-03-09T00:10:00Z
supersedes: null
related_artifacts:
  - BRF-0001
---

# Proposal: Protocol Schema and Shared Workflow State Baseline

## Proposal Summary

Establish a two-layer protocol system for the automation workflow:

1. Human-readable protocol documents in `docs/protocols/` and `docs/templates/`
2. Machine-readable Pydantic schemas in `automation/langgraph/schemas/`

This proposal recommends defining all early-stage artifact types and one canonical `WorkflowState` model before implementing the LangGraph execution graph.

## Based On

- `BRF-0001`

## Assumptions

- The repository will continue to use Python as the automation language for LangGraph and validation tools.
- Future LangGraph nodes will exchange structured state rather than passing raw markdown text directly.
- The workflow will require explicit stage gating, rollback, and traceability from the beginning.
- The current accepted Godot skeleton is stable enough to serve as a runtime baseline while protocol work proceeds.

## Alternatives Considered

### Alternative A: Markdown-only workflow
Use only markdown documents without machine-readable schemas.

**Why not chosen:**
This would be faster initially, but it would create ambiguity once LangGraph nodes, Codex task generation, and QA gating need structured data.

### Alternative B: Build LangGraph graph first, define protocol later
Start implementing graph nodes immediately and define schemas retroactively.

**Why not chosen:**
This increases the risk of hidden assumptions and inconsistent data shapes across nodes.

### Alternative C: Single monolithic schema for all artifact types
Use one large general-purpose schema for all artifacts.

**Why not chosen:**
This would weaken type boundaries and make validation less precise.

## Recommendation

Adopt the two-layer system:

- markdown templates for human readability and repository traceability,
- Pydantic models for machine validation,
- one canonical `WorkflowState` model for stage-aware orchestration.

This creates a stable foundation for later LangGraph graph construction and Codex task automation.

## Scope Impact

- Adds protocol documentation and schema files.
- Adds validation and test surface for automation infrastructure.
- Does not alter the current Godot runtime skeleton.
- Does not yet create executable agent behavior.

## Technical Impact

- Introduces `automation/langgraph/schemas/`
- Introduces protocol templates and example artifacts
- Introduces repository-level stage semantics
- Enables later automation steps to validate artifact structure programmatically

## Known Risks

- The initial schema set may require refactoring once real execution nodes exist.
- Some fields may prove either too narrow or too broad after the first few real workflow iterations.
- Early examples may need migration if protocol versioning rules evolve.