# 006 Phase 6 Minimal CI Scope

## Purpose

Record the scope boundary for Phase 6 of the Tales of Dusk automated development workflow repository.

Phase 6 exists to establish the first minimal GitHub Actions quality gate for the repository.

Its purpose is to introduce a bounded, repeatable, repository-native validation layer that can automatically check whether key accepted baselines from earlier phases remain intact.

Phase 6 does **not** attempt to build the full delivery pipeline.  
It introduces a narrow CI baseline only.

This record prevents another common failure mode: expanding from local validation directly into broad CI/CD automation before the repository has a stable, low-risk quality gate.

---

## Phase 6 Mission

The mission of Phase 6 is:

- define the first minimal repository CI workflow,
- validate that the protocol/state/orchestration baseline is still intact,
- validate that the repository’s protected files and accepted structure still exist,
- provide an automatic quality gate for the automation layer,
- do all of the above without requiring OpenAI API usage,
- do all of the above without activating remote Codex execution,
- do all of the above without introducing broad runtime build/export complexity.

Phase 6 is a **minimal quality-gate phase**, not a full CI/CD phase.

---

## Why Phase 6 Exists

The repository already has:

- a Phase 1 repository foundation,
- a Phase 2 accepted Godot runtime skeleton,
- a Phase 3 accepted protocol/schema/state baseline,
- a Phase 4 accepted minimal LangGraph orchestrator,
- a Phase 5 accepted bounded Codex entry layer.

However, those phases are still primarily validated through:

- local manual inspection,
- local Python commands,
- local Codex review,
- structural repository checks.

Without Phase 6, the repository still lacks an automatic gate that can answer questions such as:

- did a commit accidentally break the protocol/state layer?
- did the minimal orchestrator stop running?
- did a protected baseline file disappear?
- did the repository metadata drift from the actual phase?
- did a PR quietly break the accepted automation baseline?

Phase 6 exists to reduce this risk with the smallest possible CI layer.

---

## Accepted Scope for Phase 6

Phase 6 is explicitly in scope for the following work.

### 1. Minimal GitHub Actions Workflow

Phase 6 defines one minimal CI workflow under:

```text
.github/workflows/
```

This workflow is intended to:

* run on `workflow_dispatch`,
* run on selected `push` events,
* run on selected `pull_request` events,
* check only the repository areas relevant to the accepted automation baseline.

This workflow should remain bounded and conservative.

---

### 2. Python-Based Validation Chain

Phase 6 includes a Python-based validation chain that runs in CI.

This includes checks such as:

* protocol/state validation,
* minimal orchestrator execution,
* repository smoke checks,
* pytest execution for automation-layer tests.

This is the accepted initial validation surface.

---

### 3. Repository Smoke Check

Phase 6 may define a repository smoke script to confirm that critical accepted files and required baseline snippets still exist.

This smoke check is intended to catch:

* missing protected files,
* stale phase metadata,
* loss of required automation files,
* loss of required runtime baseline references,
* obvious baseline drift.

This smoke script is accepted as a CI support tool.

---

### 4. Dependency Installation Baseline

Phase 6 includes standardization of the Python dependency file used by minimal CI.

This means:

* `automation/requirements.txt` must be installable in CI,
* dependency formatting must be conventional,
* CI setup should be simple and deterministic.

---

### 5. Bounded Trigger Strategy

Phase 6 may define limited CI triggers based on:

* branch filters,
* path filters,
* workflow dispatch.

The goal is to validate relevant repository changes without turning every change into a broad pipeline run.

---

## Explicitly Out of Scope for Phase 6

The following are **not** part of Phase 6.

### 1. OpenAI API / Remote Codex Activation

Phase 6 does **not** activate remote Codex execution.

That means Phase 6 does not include:

* adding `OPENAI_API_KEY` to GitHub secrets,
* running `openai/codex-action@v1`,
* paying API-billed remote Codex usage,
* remote review execution,
* remote implementation execution.

This is fully consistent with the accepted Phase 5 boundary under the current chosen approach.

---

### 2. Full Codex Task Generation Pipeline

Phase 6 does **not** yet generate, validate, and execute real Codex Tasks automatically.

It does not include:

* Approved Spec -> Codex Task generation automation,
* Codex execution handoff,
* implementation-approval gating,
* automated repository edits driven by workflow output.

That is a later phase.

---

### 3. Full Human Approval / Interrupt Orchestration

Phase 6 does **not** implement:

* interrupt/resume approval flow,
* human approval checkpoints in LangGraph,
* durable workflow pause/resume logic,
* manual approval integration in CI.

That remains later-phase orchestration work.

---

### 4. Godot Build / Export Pipeline

Phase 6 does **not** include:

* Godot export builds,
* release artifacts,
* packaging,
* installer generation,
* deployment jobs.

The accepted runtime baseline must remain intact, but Phase 6 is not yet a delivery pipeline.

---

### 5. Godot Headless Runtime Validation

Phase 6 does **not** yet require:

* Godot executable installation in CI,
* `--headless` project import,
* runtime scene execution in CI,
* Godot engine-based smoke tests.

These may be added in a later phase, but they are not required for the minimal CI baseline.

---

### 6. Broad Repository Build Matrix

Phase 6 does **not** include:

* multi-platform build matrices,
* multiple Python versions,
* multiple Godot versions,
* release promotion jobs,
* deployment environment integration.

The CI baseline should remain deliberately small.

---

## Canonical Deliverables of Phase 6

Phase 6 is considered complete only if the following deliverables exist.

### CI Workflow

* `.github/workflows/ci_minimal.yml`

### CI Support Script

* `automation/scripts/ci_repo_smoke.py`

### Dependency Baseline

* corrected `automation/requirements.txt`

### Optional Supporting Record

* this architecture scope record

These deliverables are sufficient for the accepted minimal CI baseline.

---

## Required Constraints During Phase 6

The following constraints apply throughout Phase 6.

### Constraint 1

Phase 6 must remain independent of remote OpenAI API execution.

### Constraint 2

Phase 6 must not activate remote Codex GitHub workflows.

### Constraint 3

Phase 6 must not silently broaden into build/export/release automation.

### Constraint 4

Phase 6 must preserve the accepted baselines from Phases 2–5.

### Constraint 5

Phase 6 should validate the current repository baseline, not redesign it.

### Constraint 6

Phase 6 should prefer deterministic local/CI checks over network-dependent intelligence.

### Constraint 7

Phase 6 should keep workflow permissions conservative.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton.

Phase 6 should protect that runtime baseline structurally, but it is not yet responsible for executing Godot-based runtime validation in CI.

### Relationship to Phase 3

Phase 3 established:

* protocol documents,
* artifact templates,
* example artifacts,
* schemas,
* shared workflow state.

Phase 6 should validate that this layer still exists and remains structurally coherent.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 6 should validate that:

* the graph still exists,
* it still runs locally in CI,
* it still reaches the accepted bounded terminal stage on the happy path.

### Relationship to Phase 5

Phase 5 established bounded Codex entry.

Phase 6 should not activate or bill remote Codex execution.
Instead, it should preserve that entry layer structurally while building the first independent CI quality gate.

---

## Relationship to Later Phases

Later phases may add:

* Codex Task generation automation,
* approval-gated implementation handoff,
* remote Codex workflow activation,
* Godot headless CI validation,
* export/build jobs,
* stronger PR quality gates,
* release automation.

Phase 6 does not do those things.
It creates the minimal quality gate they can later build upon.

---

## Accepted CI Validation Surface

The accepted minimal CI validation surface for Phase 6 includes the following checks.

### 1. Protocol/State Validation

Run the local protocol/state validation script.

Expected goal:

* confirm that the shared workflow state can still be instantiated,
* confirm that the protocol/schema baseline is still loadable.

### 2. Minimal Orchestrator Run

Run the minimal orchestrator local runner.

Expected goal:

* confirm that the accepted happy path still reaches `codex_tasking`,
* confirm that the accepted orchestration baseline is intact.

### 3. Repository Smoke Check

Run the repository smoke script.

Expected goal:

* confirm required files still exist,
* confirm phase metadata still matches current accepted phase,
* confirm protected baseline references still exist.

### 4. Pytest Automation Tests

Run pytest for the automation subtree.

Expected goal:

* confirm that basic schema/state/orchestrator tests still pass.

This validation surface is accepted as sufficient for the minimal CI baseline.

---

## Accepted CI Trigger Posture

The accepted CI trigger posture for Phase 6 is:

* manual dispatch allowed,
* push trigger allowed on selected branches,
* pull_request trigger allowed on selected branches,
* path filters allowed to reduce unrelated runs.

This posture is accepted because it is practical, bounded, and aligned with the current repository maturity.

---

## Accepted Permission Posture

The accepted minimal CI permission posture is:

* `contents: read`

The workflow should not require broad repository write permissions.

This is part of the accepted conservative CI baseline.

---

## Accepted Dependency Posture

The accepted Python dependency posture is:

* install from `automation/requirements.txt`
* use standard pip install flow
* prefer stable Python 3.11 in CI
* keep dependency set small and relevant to the accepted automation baseline

This is sufficient for the minimal CI phase.

---

## What Was Intended to Be Validated by Phase 6

Phase 6 is intended to prove all of the following:

* the repository can validate its automation baseline automatically,
* the accepted protocol/state layer still runs outside local manual use,
* the minimal graph still works under CI conditions,
* baseline drift can be caught automatically,
* the repository can support GitHub-native quality gating without invoking billed Codex execution.

---

## Known Limitations at Acceptance Time

This acceptance intentionally preserves several known limitations.

### CI Limitations

* no remote Codex action runs
* no OpenAI secret usage
* no billed API usage
* no remote review or task execution
* no durable workflow-state storage in CI
* no artifact parsing pipeline beyond current local checks

### Runtime Limitations

* no Godot binary installation in CI
* no headless project execution
* no export testing
* no asset/import verification through Godot itself

### Quality Limitations

* the smoke check is structural, not semantic-complete
* minimal orchestrator validation remains fixture-driven
* CI proves baseline continuity, not full repository correctness

These limitations are acceptable because Phase 6 only targets the first minimal CI quality gate.

---

## Why This Baseline Is Accepted

Phase 6 is accepted because it establishes the first automatic repository quality gate without prematurely activating costly or complex systems.

Specifically, it provides:

* one accepted GitHub Actions validation workflow,
* one accepted repository smoke-check script,
* one accepted Python validation chain,
* one accepted dependency installation baseline,
* one accepted bounded CI posture independent of remote Codex execution.

This is sufficient for:

* baseline protection,
* PR/push guardrails,
* future CI/CD expansion,
* future remote workflow activation readiness,
* future task-generation automation support.

without prematurely turning the repository into a full delivery pipeline.

---

## Baseline Protection Rules

The following rules apply after this acceptance.

### Rule 1

Later workflow phases must treat the minimal CI workflow as the current accepted quality-gate baseline unless superseded.

### Rule 2

Any change to the following requires explicit review and likely a change request:

* CI trigger strategy
* CI permission posture
* dependency installation baseline
* smoke-check baseline assertions
* minimal orchestrator CI expectations
* any move toward remote OpenAI/Codex activation

### Rule 3

Later phases may expand CI, but should not silently break the accepted minimal CI checks.

### Rule 4

Any future activation of remote Codex workflows must be treated as a separate step beyond this baseline unless explicitly accepted later.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it,
* CI scope is intentionally expanded through controlled review,
* remote Codex execution becomes an accepted CI concern in a later phase,
* the repository adopts a newer accepted quality-gate baseline.

Until then, this document is the canonical scope record for Phase 6 minimal CI work.

---

## Status

Recommended metadata for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as the authoritative scope boundary for Phase 6 work in this repository.