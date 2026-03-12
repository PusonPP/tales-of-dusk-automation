# 007 Phase 6 Minimal CI Accepted

## Purpose

Record the acceptance of Phase 6, which established the first minimal GitHub Actions quality gate for the Tales of Dusk automated development workflow repository.

This document freezes the currently accepted CI baseline so that later task generation, approval-gated execution, remote Codex activation, richer validation, and delivery automation can build on a stable and explicitly governed quality gate.

Phase 6 does not introduce a full CI/CD pipeline.  
Instead, it introduces the first accepted automatic repository validation layer.

---

## Scope of Acceptance

Phase 6 acceptance covers the following minimal CI baseline only:

- one accepted GitHub Actions workflow for repository validation
- one accepted repository smoke-check script
- one accepted Python dependency installation baseline for automation validation
- one accepted automatic validation chain for protocol/state/orchestrator continuity
- one accepted CI trigger posture for selected branches and relevant repository paths
- one accepted conservative permission posture for the CI workflow
- proof that the workflow can run successfully on GitHub Actions

This acceptance does **not** include:

- remote OpenAI API usage
- activation of Codex GitHub Action workflows
- remote review execution
- remote implementation execution
- Godot headless runtime validation in CI
- Godot export/build jobs
- full artifact parsing pipelines
- task-generation automation
- approval-gated implementation handoff
- release packaging or deployment automation

---

## Accepted Minimal CI Baseline

The repository now contains an accepted minimal CI baseline with the following characteristics.

### Accepted CI Workflow

The accepted workflow file is:

```text
.github/workflows/ci_minimal.yml
````

This is the canonical Phase 6 CI entry point.

It is accepted as the first automatic validation workflow for this repository.

### Accepted CI Support Script

The accepted repository smoke-check script is:

```text
automation/scripts/ci_repo_smoke.py
```

This script is part of the accepted CI baseline and is intended to validate the continued presence of critical repository files and baseline references.

### Accepted Dependency Baseline

The accepted dependency file for this workflow is:

```text
automation/requirements.txt
```

Its formatting and installability are part of the accepted CI baseline.

### Accepted Local Validation Chain Reused by CI

The accepted CI workflow relies on the same local validation chain already established in earlier phases, including:

* protocol/state validation
* minimal orchestrator execution
* repository smoke checks
* pytest for automation-layer tests

This reuse is intentional and accepted.

---

## Accepted CI Validation Surface

The accepted minimal CI workflow validates all of the following:

### 1. Protocol and Workflow-State Baseline

The workflow runs the protocol/state validation script to confirm that the accepted schema and workflow-state layer still load correctly.

### 2. Minimal Orchestrator Baseline

The workflow runs the minimal orchestrator local runner to confirm that the accepted happy path still reaches:

```text
codex_tasking
```

This preserves the accepted Phase 4 orchestration baseline under CI conditions.

### 3. Repository Smoke Baseline

The workflow runs the repository smoke script to confirm that critical accepted files and baseline snippets still exist.

This helps detect:

* missing baseline files
* stale phase metadata
* missing workflow assets
* loss of accepted protected references

### 4. Automation Test Baseline

The workflow runs pytest for the automation subtree to confirm that current schema/state/orchestrator tests still pass.

This is the accepted initial automated validation surface.

---

## Accepted Trigger Posture

The accepted trigger posture for the minimal CI workflow includes:

* `workflow_dispatch`
* selected `push` events
* selected `pull_request` events
* path filtering for relevant repository areas

This trigger strategy is accepted because it is:

* bounded
* practical
* low-noise
* aligned with the repository’s current maturity

The accepted trigger posture is part of the CI baseline and must not be silently broadened without review.

---

## Accepted Permission Posture

The accepted permission posture for the minimal CI workflow is:

```text
contents: read
```

This conservative permission level is part of the accepted CI baseline.

The workflow is not accepted as requiring repository write authority.

---

## Accepted Python Environment Baseline

The accepted Python setup posture for the minimal CI baseline is:

* Python 3.11
* pip-based dependency installation
* dependency installation from `automation/requirements.txt`
* no requirement for GPU or engine runtime installation
* no requirement for OpenAI API configuration

This is sufficient for the minimal CI baseline.

---

## Accepted Non-Activation Boundary

Phase 6 acceptance explicitly preserves the current non-activation boundary for remote Codex execution.

That means the following remain intentionally **not activated**:

* `OPENAI_API_KEY` usage in GitHub Actions
* `openai/codex-action@v1`
* remote Codex prompt execution
* billed API-backed workflow runs

This is consistent with the accepted Phase 5 strategy and remains part of the accepted Phase 6 baseline.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton.

Phase 6 does not yet run Godot-based engine validation in CI, but it helps protect the Phase 2 baseline structurally through repository smoke checks and continued repository discipline.

### Relationship to Phase 3

Phase 3 established the protocol, artifact, schema, and workflow-state baseline.

Phase 6 now provides the first automatic GitHub-side quality gate protecting that baseline.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 6 protects that accepted baseline by executing the minimal orchestrator as part of CI.

### Relationship to Phase 5

Phase 5 established the bounded Codex entry layer.

Phase 6 does not activate that remote Codex layer, but it preserves the repository structures, prompts, workflow files, and governance assumptions introduced by Phase 5.

---

## What Was Explicitly Validated

Phase 6 acceptance is based on the following validated repository behavior.

### Structural Validation

The repository contains:

* the minimal CI workflow file
* the smoke-check script
* the dependency baseline
* the accepted automation validation scripts
* the accepted orchestration test layer
* the accepted architecture record for Phase 6 scope

### Local Validation Before CI

Before CI acceptance, the repository demonstrated successful local execution of:

* `python -m automation.scripts.validate_protocols`
* `python -m automation.scripts.run_minimal_orchestrator`
* `python -m automation.scripts.ci_repo_smoke`
* `pytest automation\langgraph\tests -q`

These local checks were part of the Phase 6 readiness proof.

### GitHub Actions Validation

The minimal CI workflow was successfully executed in GitHub Actions.

This proves that:

* repository checkout works
* Python environment setup works
* dependency installation works
* protocol/state validation works in CI
* minimal orchestrator execution works in CI
* smoke-check execution works in CI
* automation tests pass in CI

This is the key evidence that elevates Phase 6 from local-only readiness to accepted CI baseline.

---

## Known Limitations at Acceptance Time

This acceptance intentionally preserves several known limitations.

### CI Limitations

* no remote Codex execution
* no OpenAI API-backed workflow activity
* no remote review workflow activation
* no remote implementation workflow activation
* no build matrix
* no release automation
* no deployment jobs

### Runtime Limitations

* no Godot engine installation in CI
* no Godot headless import/test
* no scene execution through Godot in CI
* no export/build validation

### Validation Limitations

* smoke-checks remain structural rather than fully semantic
* orchestrator validation remains fixture-driven
* automation tests remain relatively narrow compared to a future full pipeline

These limitations are acceptable because Phase 6 only aims to establish the first automatic quality gate.

---

## Why This Baseline Is Accepted

Phase 6 is accepted because it establishes the first successful GitHub-native repository validation loop without prematurely activating costly or complex systems.

Specifically, it provides:

* one accepted CI workflow
* one accepted smoke-check script
* one accepted Python validation baseline
* one accepted automatic gate for protocol/state/orchestrator continuity
* one accepted conservative permission posture
* one accepted non-activation boundary for remote Codex execution

This is sufficient for:

* protecting the accepted repository baseline
* reducing regression risk
* validating automation-layer continuity on push/PR
* preparing for later task-generation and gated-execution phases
* supporting future CI/CD expansion

without prematurely expanding authority or cost.

---

## Baseline Protection Rules

The following rules apply after this acceptance.

### Rule 1

Later workflow phases must treat the minimal CI workflow as the active accepted repository quality gate unless superseded.

### Rule 2

Any change to the following requires explicit review and likely a change request:

* CI trigger posture
* CI permission posture
* dependency installation assumptions
* smoke-check baseline assertions
* Python version baseline
* orchestrator execution expectations in CI
* the non-activation boundary for remote Codex execution

### Rule 3

Later phases may expand CI, but should not silently break the accepted Phase 6 validation chain.

### Rule 4

Remote Codex activation remains outside the accepted Phase 6 baseline unless explicitly accepted later.

---

## Relationship to Later Phases

Later phases may add:

* Approved Spec -> Codex Task generation automation
* gated implementation handoff
* approval-aware execution control
* remote Codex workflow activation
* Godot headless validation in CI
* export/build jobs
* richer PR gates
* release automation

Those later phases should build on the accepted minimal CI baseline established here rather than bypassing it.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it
* CI scope is intentionally expanded through controlled workflow review
* remote Codex execution becomes part of the accepted CI baseline in a later phase
* the repository adopts a newer accepted quality-gate baseline

Until then, this document is the canonical accepted CI baseline record for Phase 6.

---

## Status

Recommended status for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as an active architecture acceptance record for the current minimal CI baseline.