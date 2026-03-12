# 004 Phase 5 Codex Entry Scope

## Purpose

Record the scope boundary for Phase 5 of the Tales of Dusk automated development workflow repository.

Phase 5 exists to connect Codex to the repository through controlled local and remote entry points without yet granting unrestricted autonomous implementation authority.

Its purpose is to establish:

- repository-aware Codex entry behavior,
- Codex-facing rule layers,
- local Codex operating paths,
- remote GitHub-based Codex operating paths,
- prompt-file assets for repeatable Codex usage,
- safety boundaries for future implementation work.

This record prevents another common failure mode: connecting Codex to a repository before the repository has explicit workflow protocols, shared state semantics, graph structure, and repository-level operating constraints.

---

## Phase 5 Mission

The mission of Phase 5 is:

- define how Codex is allowed to enter the repository workflow,
- define where Codex reads repository rules from,
- define which local execution modes are accepted,
- define which remote execution modes are accepted,
- define reusable prompt-file assets for Codex,
- define what Codex may and may not do at this phase,
- define how future Codex-backed work will remain subordinate to approved specs, task boundaries, and repository safety rules.

Phase 5 is a **Codex entry integration phase**, not a full autonomous execution phase.

---

## Why Phase 5 Exists

The repository already has:

- a Phase 1 repository foundation,
- a Phase 2 accepted Godot runtime skeleton,
- a Phase 3 protocol and schema baseline,
- a Phase 4 accepted minimal LangGraph orchestrator.

However, the workflow still lacks a controlled way for Codex to interact with the repository.

Without Phase 5, Codex usage would remain ad hoc and unstable:
- prompts would not be standardized,
- repository rules would not be layered properly,
- local and remote execution modes would diverge,
- write authority would be ambiguous,
- branch safety would be unclear,
- future automation would risk bypassing protocol and review discipline.

Phase 5 exists to create one accepted Codex entry layer before any real Codex implementation authority expands further.

---

## Accepted Scope for Phase 5

Phase 5 is explicitly in scope for the following work.

### 1. Root and Subtree Codex Rule Layers

Phase 5 defines and/or strengthens Codex-facing repository rules using `AGENTS.md`.

This includes:

- the repository root `AGENTS.md`,
- subtree-specific `AGENTS.md` files,
- clear protected baseline declarations,
- branch safety expectations,
- implementation boundary expectations,
- output contract expectations for Codex work.

The purpose of this layer is to ensure that Codex does not operate against the repository as if it were an unstructured codebase.

---

### 2. Local Codex Entry Definition

Phase 5 defines the accepted local Codex entry paths.

This includes:

- Codex app as the primary local Windows-facing entry point,
- Codex CLI in WSL as the preferred terminal/scriptable local entry path,
- repository-root launch expectations,
- local prompt usage expectations,
- local safety expectations,
- local smoke validation procedures.

Phase 5 may document these paths and test them manually.

---

### 3. Remote Codex Entry Definition

Phase 5 defines the accepted remote Codex entry path through GitHub Actions.

This includes:

- manual review-only Codex action workflows,
- manual task entry workflows with bounded safety settings,
- repository prompt-file usage,
- artifact return/output expectations,
- repository secret requirements,
- default runner and sandbox assumptions.

The purpose of this layer is to create a controlled remote Codex entry point without yet granting broad autonomous write authority.

---

### 4. Prompt-File Asset Layer

Phase 5 defines repository-stored prompt files for repeatable Codex usage.

This includes prompt-file assets such as:

- repository review prompts,
- repository audit prompts,
- future implementation-task prompt shells.

The purpose of prompt files is to reduce ad hoc prompt drift and make remote/manual Codex invocation reproducible.

---

### 5. Codex Safety Baseline

Phase 5 defines the default Codex safety posture for this repository.

This includes:

- no direct write authority to `main`,
- no silent architecture rewrites,
- no hidden scope expansion,
- no implementation work without approved upstream spec and bounded task context,
- no default dangerous sandbox settings,
- preference for manual dispatch and explicit target branch selection,
- preference for review-first operation before write-first operation.

This is a core accepted boundary of Phase 5.

---

## Explicitly Out of Scope for Phase 5

The following are **not** part of Phase 5.

### 1. Full Autonomous Codex Implementation Pipeline

Phase 5 does **not** yet grant Codex broad autonomous write authority across the repository.

That means Phase 5 does not include:

- automatic repository-wide implementation runs,
- direct implementation against `main`,
- unattended multi-step write workflows,
- automatic merge approval,
- autonomous architectural migration,
- automatic large-scope gameplay implementation.

---

### 2. Full Codex Task Generation Automation

Phase 5 does **not** yet solve the full pipeline from `Approved Spec` to generated `Codex Task` to executed implementation.

That belongs to a later phase.

Phase 5 may prepare the entry layer, but it does not complete the full task generation-and-execution automation loop.

---

### 3. Full Human Approval Interrupt Flow

Phase 5 does **not** yet implement full interrupt/resume approval routing inside LangGraph for Codex execution gating.

That means Phase 5 does not include:

- persistent approval pauses,
- approval-aware thread resume,
- approval nodes inside the graph,
- complete human signoff routing for implementation release.

Those are later orchestration concerns.

---

### 4. CI/CD Quality Gate Integration for Codex Output

Phase 5 does **not** yet integrate Codex output with full CI/CD quality gates.

That means it does not yet include:

- automatic PR validation of Codex changes,
- automatic build/export test gating for Codex-produced changes,
- automatic merge gating based on Codex-produced artifacts,
- full integration with later GitHub Actions quality workflows.

Phase 5 may introduce GitHub Actions as a Codex entry point, but not yet as a full repository quality gate.

---

### 5. Gameplay/System Expansion

Phase 5 does **not** include gameplay/system implementation simply because Codex entry becomes available.

That means Phase 5 does not include:

- deployment system implementation,
- combat implementation,
- chapter logic,
- save compatibility design,
- environment systems,
- balancing,
- content generation.

Those remain governed by the upstream protocol and later implementation phases.

---

## Canonical Deliverables of Phase 5

Phase 5 is considered complete only if the following deliverables exist.

### Repository Rule Layer
- strengthened root `AGENTS.md`
- subtree rule files where needed, such as:
  - `game/tales-of-dusk/AGENTS.md`
  - `automation/AGENTS.md`
  - `docs/AGENTS.md`

### Prompt Assets
- `.github/codex/prompts/review.md`
- `.github/codex/prompts/repo_audit.md`
- `.github/codex/prompts/implement_from_task.md`

### Remote Entry Workflows
- `.github/workflows/codex_manual_review.yml`
- `.github/workflows/codex_manual_task.yml`

### Architecture Records
- acceptance record for Phase 4
- this Phase 5 scope record

### Metadata Synchronization
- repository status docs updated so that current phase and next step are not stale

---

## Required Constraints During Phase 5

The following constraints apply throughout Phase 5.

### Constraint 1
Codex entry must remain subordinate to the repository protocol and architecture baselines established in earlier phases.

### Constraint 2
Codex must not gain silent authority to modify protected runtime baselines or workflow baselines.

### Constraint 3
Codex entry must default to controlled, explicit, reviewable invocation rather than open-ended repository autonomy.

### Constraint 4
Prompt assets must live in the repository and be versioned.

### Constraint 5
Branch safety must remain explicit. `main` is not a default implementation target.

### Constraint 6
Remote Codex workflows must prefer conservative safety settings and clearly bounded repository access.

### Constraint 7
Codex entry must not silently replace or bypass the accepted minimal LangGraph orchestrator.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton.

Phase 5 does not authorize Codex to restructure that runtime baseline without explicit upstream approval.

The accepted runtime invariants remain protected.

### Relationship to Phase 3

Phase 3 established:

- protocol documents,
- artifact types,
- lifecycle states,
- workflow stage machine,
- schema layer,
- workflow state model.

Phase 5 must respect these definitions and not introduce Codex paths that bypass them.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 5 does not replace it.  
Instead, it prepares the conditions under which future Codex-related nodes or execution handoffs may safely integrate with that orchestration layer.

---

## Relationship to Later Phases

Phase 5 is a preparation phase for more capable future Codex-backed automation.

Later phases may add:

- approved-spec-driven task generation,
- structured Codex task dispatch,
- approval-gated Codex execution,
- CI/CD validation of Codex changes,
- richer remote workflow integration,
- PR review automation,
- eventually more autonomous implementation behavior.

Any such expansion must explicitly supersede the narrow Codex entry assumptions accepted here.

---

## Accepted Local Codex Entry Model

The accepted local Codex entry model for Phase 5 is:

### Primary Local Entry
- Codex app on Windows

### Preferred Terminal/Scriptable Entry
- Codex CLI in WSL

### Repository Root Expectation
Codex should be pointed at the repository root so that:
- root `.git` defines project scope,
- root `AGENTS.md` is discovered,
- subtree `AGENTS.md` files can be layered correctly,
- docs, automation, and runtime areas remain visible as one governed repository.

### Local Safety Expectation
Local usage should begin with:
- read/review/audit tasks,
- repository understanding tasks,
- rule-reading tasks,
- no large write operations before manual supervision proves stable.

---

## Accepted Remote Codex Entry Model

The accepted remote Codex entry model for Phase 5 is:

### Entry Path
- GitHub Actions using Codex GitHub Action

### Trigger Style
- manual dispatch first
- explicit target ref/branch first
- prompt-file-driven first

### Default Safety Posture
- read-only review workflow is preferred
- bounded workspace-write workflow may be introduced
- dangerous unrestricted settings are not the default accepted posture

### Output Model
Remote Codex runs should return review/task output as explicit workflow artifacts such as uploaded text artifacts rather than silently modifying repository history.

---

## Accepted Prompt Asset Baseline

Phase 5 accepts repository-stored prompt assets as the standard way to invoke repeatable Codex behavior.

At minimum, prompt assets should support:

### Review Prompt
Used for repository review, baseline checking, and risk identification.

### Repository Audit Prompt
Used for broader repository inspection and workflow-state-aware analysis.

### Implementation-Task Prompt Shell
Used later as the shell for bounded implementation execution, but not yet treated as an open implementation license.

Prompt assets must remain:
- versioned,
- reviewable,
- repository-visible,
- aligned with protocol and branch rules.

---

## Accepted Safety Baseline

The following safety assumptions are accepted as repository policy for Phase 5 Codex entry.

### 1. No direct `main` modification by default
Codex is not accepted as a direct default writer to `main`.

### 2. No implementation without upstream authority
Codex should not perform real implementation work without:
- approved upstream scope,
- bounded task framing,
- explicit file boundaries.

### 3. No hidden scope expansion
Codex may not infer wider authority from access alone.

### 4. Review-first bias
Repository review, audit, and controlled understanding tasks are the preferred first use cases.

### 5. Remote conservatism
Remote GitHub-based Codex entry should start conservative and remain explicitly constrained.

### 6. Human oversight remains required
Phase 5 does not treat Codex as an unsupervised autonomous maintainer.

---

## What Phase 5 Must Demonstrate

Phase 5 is accepted only if it demonstrates all of the following.

### 1. Repository-Aware Rule Discovery
Codex can be pointed at the repository and consistently read repository rules from `AGENTS.md`.

### 2. Stable Prompt Asset Usage
Codex can be invoked using repository-stored prompt files rather than ad hoc one-off prompts only.

### 3. Safe Local Entry
At least one local entry mode is established and practical.

### 4. Safe Remote Entry
At least one remote GitHub-based entry workflow exists and is bounded.

### 5. No Baseline Damage
The accepted Godot runtime baseline, protocol baseline, and minimal orchestrator baseline remain intact.

---

## Risks Recognized in Phase 5

### Risk 1: Prompt Drift
Prompt assets may diverge from repository protocol unless updated carefully.

### Risk 2: Rule Layer Inconsistency
Root and subtree `AGENTS.md` files may become inconsistent unless maintained together.

### Risk 3: Early Over-Trust in Codex
A functioning entry path may create pressure to grant broader repository authority too early.

### Risk 4: Remote Safety Misconfiguration
GitHub-based Codex entry may become too permissive if safety settings are loosened before quality gates exist.

### Risk 5: Branch Discipline Erosion
If users treat Codex as directly editing `main`, the repository loses one of its core safety assumptions.

These risks are acceptable only if Phase 5 stays within the narrow entry-scope boundary defined here.

---

## Acceptance Criteria for Phase 5

Phase 5 is accepted only if all of the following are true.

### AC-001
Repository-level and subtree-level Codex rule files exist and are coherent.

### AC-002
Prompt-file assets exist in the repository and support repeatable Codex entry.

### AC-003
At least one accepted local Codex entry path is documented and usable.

### AC-004
At least one accepted remote Codex GitHub workflow exists and is bounded.

### AC-005
Phase 5 does not silently expand into autonomous wide-scope repository implementation.

### AC-006
Protected baselines from Phases 2–4 remain intact.

### AC-007
The repository’s current phase metadata is synchronized and not stale.

---

## Non-Goals

To remove ambiguity, the following are explicit non-goals for Phase 5:

- “just let Codex implement features now”
- “just give Codex direct write access to main”
- “just auto-run Codex on every push”
- “just skip prompt files and use ad hoc manual prompts”
- “just trust Codex to infer architecture boundaries”
- “just turn remote workspace-write into unrestricted automation”

Those are outside this phase boundary.

---

## Phase 5 Decision

The repository will treat Phase 5 as a controlled Codex entry phase only.

Codex is now being integrated as a governed actor in the workflow, but not yet as an unrestricted implementation engine.

This decision is made to maximize:
- repository control,
- branch safety,
- protocol compliance,
- future auditability,
- safe gradual expansion of automation authority.

---

## Supersession Policy

This record remains active until it is superseded by a later approved architecture record that explicitly changes Codex authority, Codex safety assumptions, or Codex workflow integration scope.

Until then, it is the canonical scope record for Phase 5 work in this repository.

---

## Status

Recommended metadata for this architecture record:

- version: `1.0.0`
- status: `accepted`

This document should be treated as the authoritative scope boundary for Phase 5 Codex entry work in this repository.