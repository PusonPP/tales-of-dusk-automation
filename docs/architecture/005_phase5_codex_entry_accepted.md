# 005 Phase 5 Codex Entry Accepted

## Purpose

Record the acceptance of Phase 5, which established the first controlled Codex entry layer for the Tales of Dusk automated development workflow repository.

This document freezes the currently accepted Codex-entry baseline so that later task generation, approval-gated execution, QA automation, and CI/CD integration can build on an explicit and governed entry model rather than on ad hoc local usage or unsafe remote assumptions.

Phase 5 does not grant Codex unrestricted implementation authority.  
Instead, it establishes the accepted local and remote entry surfaces, repository rule-discovery behavior, prompt-file assets, and safety boundaries that future phases must respect.

---

## Scope of Acceptance

Phase 5 acceptance covers the following Codex-entry baseline only:

- repository-level Codex rule layers via `AGENTS.md`
- subtree-specific Codex rule layers
- repository-stored prompt assets for repeatable Codex usage
- at least one accepted local Codex entry path
- accepted remote GitHub workflow entry definitions
- a conservative safety baseline for Codex entry
- proof that Codex can read repository rules and operate in bounded review mode
- proof that local Codex usage does not imply silent write authority

This acceptance does **not** include:

- full autonomous Codex implementation
- automatic repository-wide write execution
- automatic PR merge or release authority
- automatic generation and execution of real Codex Tasks
- interrupt/resume approval flow inside LangGraph
- full CI/CD quality gate enforcement for Codex output
- mandatory activation of remote API-backed workflows
- direct write operations against `main`

---

## Accepted Codex Entry Baseline

The repository now contains an accepted Codex-entry baseline with the following characteristics.

### Root Rule Layer

The accepted root Codex rule file is:

```text
AGENTS.md
```

This file defines repository-wide constraints for:

* baseline protection
* branch safety
* implementation authority boundaries
* protocol-first workflow discipline
* review expectations
* output expectations
* human approval triggers

This file is part of the accepted repository governance baseline.

### Subtree Rule Layers

The accepted subtree-specific rule files are:

```text
game/tales-of-dusk/AGENTS.md
automation/AGENTS.md
docs/AGENTS.md
```

These files refine root governance for:

* Godot runtime work
* automation/schema/graph work
* protocol/documentation/artifact work

These subtree rule files are part of the accepted Codex-entry baseline and must be treated as authority-bearing rule layers, not optional notes.

### Prompt Asset Layer

The accepted repository prompt assets are:

```text
.github/codex/prompts/review.md
.github/codex/prompts/repo_audit.md
.github/codex/prompts/implement_from_task.md
```

These prompt files are versioned repository assets and define repeatable Codex entry behavior.

They are not disposable prompt scratchpads.

### Remote Workflow Entry Definitions

The accepted remote Codex workflow entry files are:

```text
.github/workflows/codex_manual_review.yml
.github/workflows/codex_manual_task.yml
```

These files define the current accepted remote entry shape for Codex under a bounded and conservative safety posture.

### Phase Metadata Intention

Phase 5 acceptance assumes the repository phase messaging is updated so that:

* current phase reflects Phase 5
* next step reflects the later task-generation / gated-execution phase

Stale repository phase metadata is considered inconsistent with accepted Phase 5 completion.

---

## Accepted Local Codex Entry

Phase 5 acceptance requires at least one real local Codex entry path that is usable and governed.

### Accepted Local Entry Path

The currently accepted local entry path is:

* **Codex app on Windows**

This is accepted as the first practical local Codex entry surface for this repository.

### What Was Validated

Local Codex usage was validated in bounded review mode through behavior such as:

* repository structure summary
* current phase and protected baseline explanation
* root-rule interpretation
* minimal orchestrator review
* approval-before-write behavior for a proposed documentation-only cleanup

### What This Validation Proves

This local validation proves that Codex can:

* open the repository at repository-root scope
* read and apply repository governance
* perform review-only analysis without modifying files
* propose a bounded change without executing it before explicit approval

This is sufficient for accepting the first local Codex entry layer.

### What Local Validation Does Not Yet Prove

This acceptance does **not** prove:

* full implementation-task execution authority
* broad repository write safety under unattended conditions
* completion of WSL CLI entry
* correctness of future Codex task dispatch
* approval-gated implementation handoff inside LangGraph

Those are later-phase concerns.

---

## Accepted Remote Codex Entry Definition

Phase 5 acceptance includes the **definition** of a remote Codex entry layer, but not mandatory activation of that layer.

### Accepted Remote Entry Model

The accepted remote entry model is:

* GitHub Actions-based Codex invocation
* manual dispatch first
* prompt-file-driven first
* conservative sandbox and safety defaults
* no broad autonomous write authority

### Accepted Remote Workflow Intention

The remote review workflow is intended for:

* read-only repository review
* repository audit
* bounded Codex output generation as uploaded workflow artifacts

The remote task workflow is intended for:

* future bounded Codex task execution entry
* still under controlled branch and safety assumptions
* not yet treated as broad autonomous repository implementation

### Acceptance Under Deferred Activation

This repository currently accepts a **prepared-but-not-activated** remote entry state if:

* workflow YAML exists,
* prompt assets exist,
* safety posture is conservative,
* remote activation is intentionally deferred,
* missing secret configuration is an explicit choice rather than an untracked omission.

This is an accepted Phase 5 boundary.

### What Is Explicitly Deferred

This acceptance explicitly defers:

* adding `OPENAI_API_KEY` repository secret
* running remote Codex workflows live
* billing-bearing remote action execution
* remote write validation
* CI quality gate integration downstream of Codex output

Those remain optional or later-phase work.

---

## Accepted Safety Baseline

Phase 5 acceptance establishes the following Codex safety baseline.

### No Direct `main` Write Assumption

Codex is not accepted as a default direct writer to `main`.

### No Silent Authority Expansion

Codex must not infer implementation authority from repository access alone.

### Prompt Files Are Bounded Inputs

Prompt assets must remain repository-scoped, versioned, and bounded.

### Review-First Bias

The accepted default Codex posture is:

* inspect
* review
* summarize
* propose bounded next steps
* wait for approval before write behavior

### Conservative Remote Posture

Remote entry definitions should remain conservative by default, including:

* manual dispatch
* explicit target ref
* bounded permissions
* safe sandbox assumptions
* no unrestricted automation by default

### Upstream Authority Still Required

Codex entry does not override the need for:

* approved scope
* bounded task framing
* file boundary discipline
* acceptance criteria
* human oversight where required

This remains a core accepted repository safety assumption.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton.

Phase 5 does not authorize Codex to casually alter:

* main scene path
* accepted scene flow
* accepted Autoload set
* accepted room phase order
* protected runtime ownership boundaries

These remain protected baselines.

### Relationship to Phase 3

Phase 3 established:

* workflow protocol
* artifact types
* lifecycle rules
* stage-machine rules
* schema layer
* `WorkflowState`

Phase 5 does not override or bypass these contracts.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 5 does not replace it.
It only establishes the Codex entry layer that later phases may connect to approved task-generation and execution handoff logic.

---

## What Was Explicitly Validated

Phase 5 acceptance is based on the following validated repository realities.

### Structural Validation

The repository contains:

* root `AGENTS.md`
* subtree `AGENTS.md` files
* prompt-file assets
* remote workflow YAML definitions
* accepted Phase 5 scope architecture record
* prior accepted protocol/schema/orchestrator baselines

### Local Entry Validation

The local Codex app entry path demonstrated:

* repository-root awareness
* protected baseline awareness
* phase-aware reasoning
* review-only operation
* approval-before-write behavior

### Safety Validation

The accepted remote entry files do not by themselves grant uncontrolled repository authority.

The repository remains in a controlled Codex-entry posture rather than an autonomous execution posture.

### Phase-Boundary Validation

The repository has entered Phase 5 as a Codex-entry phase, while still preserving earlier accepted baselines from Phases 2–4.

---

## Known Limitations at Acceptance Time

This acceptance intentionally preserves several known limitations.

### Local Limitations

* WSL Codex CLI is not required to be accepted at this time
* local entry validation is focused on bounded review behavior
* broad write-mode validation is intentionally not accepted as baseline behavior

### Remote Limitations

* remote workflows may remain unexecuted
* repository secret configuration may remain intentionally absent
* no live billing-bearing remote Codex run is required for this acceptance
* remote output artifact handling is defined structurally, not yet operationally validated

### Tasking Limitations

* no full `Approved Spec -> Codex Task -> execution` automation loop exists yet
* `implement_from_task.md` exists as a prompt asset, not yet as proof of accepted broad implementation authority
* no approval-gated execution handoff exists yet

### CI/CD Limitations

* no downstream QA or acceptance gate consumes remote Codex output yet
* no build/export/release gate is connected to Codex workflows yet

These limitations are acceptable because Phase 5 only aims to establish the Codex entry baseline, not the full Codex execution pipeline.

---

## Why This Baseline Is Accepted

Phase 5 is accepted because it successfully introduces Codex into the repository in a controlled and governed way.

Specifically, it establishes:

* one accepted repository-wide rule layer for Codex
* three accepted subtree rule layers
* one accepted prompt-asset baseline
* one accepted local Codex entry path
* one accepted remote entry definition layer
* one accepted conservative Codex safety posture
* one accepted distinction between “Codex can enter” and “Codex may implement broadly”

This is sufficient for:

* Phase 6 task generation work
* later approval-gated execution handoff
* later remote activation if desired
* later CI/CD integration
* later expansion of Codex authority through explicit approval

without prematurely granting unsafe repository power.

---

## Baseline Protection Rules

The following rules apply after this acceptance.

### Rule 1

Later workflow phases must treat the current Codex rule files and prompt assets as part of the active baseline unless superseded.

### Rule 2

Any change to the following requires explicit review and likely a change request:

* root `AGENTS.md` authority boundaries
* subtree `AGENTS.md` scope rules
* accepted prompt-file intent
* accepted remote workflow safety posture
* default branch assumptions
* Codex write authority assumptions

### Rule 3

Later phases may expand Codex authority only explicitly, never implicitly.

### Rule 4

Remote activation is optional at Phase 5 and must not be misrepresented as already validated if it has not been run.

---

## Relationship to Later Phases

### Phase 6

Phase 6 may build the real handoff from accepted upstream artifacts toward bounded Codex task generation and gated implementation entry.

Phase 6 should consume the accepted Phase 5 entry layer rather than reinvent it.

### Later Phases

Later phases may add:

* actual Codex Task generation from Approved Spec
* interrupt/resume approval gates
* remote secret activation and live workflow execution
* branch-targeted write execution
* downstream QA and acceptance automation
* stronger CI/CD gating around Codex output

Any such expansion must explicitly supersede the current narrow Phase 5 Codex-entry assumptions.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it
* Codex authority is intentionally expanded through accepted workflow review
* remote activation becomes part of a later accepted baseline
* a later phase replaces the current bounded entry model with a newer accepted Codex integration baseline

Until then, this document is the canonical accepted Codex-entry baseline for Phase 5.

---

## Status

Recommended status for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as an active architecture acceptance record for the current Codex-entry baseline.