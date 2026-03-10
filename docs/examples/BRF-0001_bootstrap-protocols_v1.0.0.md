---
artifact_id: BRF-0001
artifact_type: design_brief
version: 1.0.0
status: draft
project_id: tales-of-dusk-automation
workflow_thread_id: bootstrap-phase3
author_role: BriefInterpreter
created_at: 2026-03-09T00:00:00Z
updated_at: 2026-03-09T00:00:00Z
supersedes: null
related_artifacts: []
---

# Design Brief: Bootstrap Protocols and Workflow State

## Objective

Define the initial document protocol and shared workflow state model for the Tales of Dusk automated development workflow so that future LangGraph, Codex, and QA stages can operate on stable, auditable, machine-readable artifacts.

## High-level Inputs

- The repository already has a Phase 1 foundation and a Phase 2 Godot runtime skeleton.
- The workflow must support multi-role collaboration rather than a single LLM directly designing the full game.
- The workflow must be able to evolve the project across future iterations without restarting from scratch.
- The automation layer must be able to track stage progression, approvals, risks, blockers, and artifact history.
- The system must be compatible with Godot 4, Codex, LangGraph, GitHub Actions, and Windows as the local primary platform.

## Non-negotiables

- Protocol artifacts must be first-class repository assets.
- All core artifact types must have stable identities, lifecycle states, and versioning.
- The automation layer must use machine-readable schemas rather than relying on informal markdown alone.
- The workflow must preserve traceability across design, implementation, QA, and acceptance.
- No Codex implementation task may exist without an approved upstream specification.
- The current Godot runtime skeleton must not be broken while defining protocol and schema infrastructure.

## Out of Scope

- Implementing the full LangGraph graph runtime.
- Integrating live Codex execution.
- Writing GitHub Actions CI workflows for automation execution.
- Designing final game mechanics, content, balancing, or level structure.
- Implementing actual gameplay systems beyond the already accepted runtime skeleton.

## Success Conditions

- Canonical workflow document types are defined.
- Canonical artifact header fields and lifecycle states are defined.
- A machine-readable shared workflow state model exists.
- Example protocol artifacts can represent a valid early-stage workflow chain.
- The repository gains a clear contract for future Proposal, Review, Approved Spec, and Codex Task generation.

## Open Questions

- Whether all protocol artifacts should eventually be validated from YAML front matter directly.
- Whether artifact references should later be indexed in a separate registry file.
- Whether future workflow state should include build identifiers, commit hashes, and CI run references.
- Whether protocol validation should become part of a GitHub Actions check in a later phase.

## Known Risks

- Over-designing the protocol too early may slow down later implementation phases.
- Under-specifying artifact structure may cause workflow drift when LangGraph nodes are added.
- Schema changes in later phases may require version migration for existing example artifacts.