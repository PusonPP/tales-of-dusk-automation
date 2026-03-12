# AGENTS.md

## Mission

This repository is not a generic game project.

It is the controlled automation workspace for building and evolving:

- a Godot 4 runtime project,
- a LangGraph-based workflow orchestration layer,
- a Codex-constrained implementation pipeline,
- a GitHub Actions-based validation and delivery gate,
- a multi-artifact protocol for design, review, implementation, QA, and acceptance.

All work in this repository must respect that this is a **governed workflow system**, not an unconstrained code sandbox.

The primary project is:

- **Project ID:** `tales-of-dusk-automation`

The primary technical stack is:

- **Engine:** Godot 4
- **Workflow Orchestration:** LangGraph
- **Implementation Agent:** Codex
- **CI/CD Gate:** GitHub Actions
- **Primary Local Platform:** Windows
- **Preferred Scriptable CLI Environment:** WSL

---

## Repository Operating Principle

This repository follows a controlled progression:

```text
Approved protocol/state baseline
-> accepted orchestration baseline
-> bounded Codex entry
-> bounded task generation
-> bounded implementation
-> QA
-> acceptance
-> stable baseline update
```

Do not treat repository access as authority to invent or expand scope.

Access does not imply permission.

A file being visible does not mean it may be modified.

A prompt asking for implementation does not override repository governance.

---

## Current Accepted Repository Baselines

The repository currently has accepted baselines from earlier phases.

### Accepted Phase 2 Runtime Baseline

The Godot runtime skeleton is accepted and protected.

Canonical project root:

```text
game/tales-of-dusk/
```

Canonical main scene path:

```text
res://scenes/boot/boot.tscn
```

Accepted scene flow:

```text
Boot -> Title -> Chapter Map -> Room Test
```

Accepted required Autoloads:

* `EventBus`
* `GameSession`
* `SaveSystem`
* `SceneRouter`

Accepted canonical room phase order:

```text
Preview -> Deploy -> Combat -> Result
```

These are protected runtime invariants.

### Accepted Phase 3 Protocol Baseline

The repository has accepted protocol/state definitions, including:

* protocol documents
* artifact templates
* example artifacts
* machine-readable schemas
* shared `WorkflowState`

These are the authoritative workflow artifact and state contracts.

### Accepted Phase 4 Orchestration Baseline

The repository has an accepted minimal LangGraph orchestrator that can advance the example artifact chain to `codex_tasking`.

This graph is deterministic and fixture-driven.
It is protected as the current accepted orchestration baseline.

### Phase 5 Scope

Codex entry may now be connected in controlled local and remote ways, but this does **not** grant unrestricted autonomous implementation authority.

---

## Source-of-Truth Documents

Before making decisions, consult these repository sources of truth.

### Architecture Records

* `docs/architecture/001_phase2_godot_skeleton_accepted.md`
* `docs/architecture/002_phase3_protocol_state_scope.md`
* `docs/architecture/003_phase4_minimal_orchestrator_accepted.md`
* `docs/architecture/004_phase5_codex_entry_scope.md`

### Protocol Documents

* `docs/protocols/automation_protocol.md`
* `docs/protocols/workflow_stage_machine.md`

### Shared Workflow State and Schemas

* `automation/langgraph/schemas/workflow_state.py`
* `automation/langgraph/schemas/`
* `automation/langgraph/graphs/minimal_orchestrator.py`

If any instruction, prompt, or assumption conflicts with the above documents, the repository documents win.

---

## Repository Layout

The high-level repository layout is:

```text
.
├─ game/
│  └─ tales-of-dusk/
├─ automation/
│  ├─ langgraph/
│  ├─ codex/
│  └─ scripts/
├─ docs/
│  ├─ architecture/
│  ├─ protocols/
│  ├─ templates/
│  ├─ examples/
│  ├─ briefs/
│  ├─ proposals/
│  ├─ reviews/
│  ├─ approved_specs/
│  ├─ codex_tasks/
│  ├─ qa_reports/
│  ├─ acceptance_reports/
│  └─ change_requests/
└─ .github/
   ├─ workflows/
   └─ codex/
      └─ prompts/
```

### Repository Area Meanings

#### `game/tales-of-dusk/`

Godot runtime project.
Protected baseline.
Do not treat this as a free-form refactor target.

#### `automation/`

Workflow code, graph code, schema code, validation utilities, Codex-facing automation scaffolding.

#### `docs/`

Protocol artifacts, architecture records, examples, and workflow-generated documentation.

#### `.github/`

Remote automation entry workflows, Codex prompt assets, future CI/CD gate logic.

---

## Protected Baselines

The following are protected and must not be changed casually.

### Protected Runtime Baselines

* `game/tales-of-dusk/project.godot`
* main scene path
* accepted scene flow
* accepted Autoload names
* accepted room phase order
* root runtime script ownership boundaries

### Protected Workflow Baselines

* canonical artifact types
* canonical workflow stages
* `WorkflowState` semantics
* accepted minimal LangGraph happy path
* protocol document meaning
* branch discipline

### Protected Safety Baselines

* `main` is not a default write target
* no silent scope expansion
* no hidden architecture migration
* no implementation without bounded task context

Any proposed change to a protected baseline must be treated as high-risk and usually requires a `Change Request` plus review.

---

## Hard Rules

### Rule 1: No silent scope expansion

Do not add gameplay systems, architectural responsibilities, artifact semantics, CI behavior, or repository workflow capabilities unless explicitly approved.

### Rule 2: No implementation without upstream authority

Do not perform real implementation work unless the repository has an appropriate upstream chain such as:

* approved scope/specification
* bounded task framing
* allowed file boundaries
* acceptance criteria

### Rule 3: No direct `main` implementation by default

Do not target `main` directly for implementation work unless explicitly instructed and repository policy clearly permits it.

Default assumption:

* work belongs on `integration` or `task/*`

### Rule 4: No architecture rewrites without review

Do not rewrite runtime architecture, workflow architecture, or repository structure because “it seems cleaner”.

### Rule 5: No hidden save/runtime boundary changes

Any change affecting:

* save behavior,
* runtime baseline flow,
* scene routing,
* autoload boundaries,
* workflow state meaning

must be treated as sensitive.

### Rule 6: Prefer narrow diffs

Prefer bounded, reviewable, minimal changes over broad refactors.

### Rule 7: Do not infer authority from visibility

Seeing files is not permission to change them.

### Rule 8: Respect repository-phase discipline

Do not prematurely implement later-phase behavior just because earlier infrastructure now exists.

---

## Branch Rules

### Accepted Branch Roles

#### `main`

Stable baseline only.
Should remain the current accepted repository baseline.

#### `integration`

Integration branch for accepted or near-accepted phase work prior to stable merge.

#### `task/*`

Bounded implementation or workflow task branches.

#### `hotfix/*`

Emergency targeted fixes.

#### `spike/*`

Short-lived experiments.
Not a stable baseline.

### Branch Expectations

* Prefer working on `integration` or `task/*`
* Do not assume permission to change branch policy
* Do not silently rebase or rewrite shared history
* Do not assume merge authority

### Default Codex Branch Posture

If branch policy is ambiguous, assume:

* read/review only,
* or write only to a bounded non-main working branch.

---

## Spec-Before-Change Rule

For implementation-oriented work, follow this order:

```text
Design Brief
-> Proposal
-> Review
-> Approved Spec
-> Codex Task
-> Implementation
-> QA
-> Acceptance
```

### Do not skip this rule for:

* runtime code changes
* workflow code changes
* schema changes
* CI changes
* architecture changes

### Exception posture

If a change is extremely small, you may still be expected to stay within repository constraints and document exactly what changed and why.
Small size does not authorize hidden scope expansion.

---

## Change Request Rule

A `Change Request` is required before proceeding if the requested work materially affects:

* gameplay scope
* system boundaries
* save compatibility
* workflow stage semantics
* accepted runtime invariants
* CI/CD trust boundaries
* branch safety assumptions
* Codex authority boundaries

If a request appears to change a protected baseline, stop and surface that need explicitly.

Do not silently “just update it”.

---

## Allowed and Forbidden Work by Default

### Default Allowed Work

Without explicit higher-level approval, the safest default work categories are:

* repository summarization
* repository audit
* architecture review
* protocol review
* workflow analysis
* bounded documentation edits
* bounded schema fixes
* bounded test fixes aligned to accepted behavior
* bounded prompt-file improvements
* bounded local tooling improvements

### Default Forbidden Work

Without explicit approval, do **not** do the following:

* add or remove Autoloads
* change the main scene path
* rewrite `SceneRouter`
* redesign room phase order
* change accepted workflow stage semantics
* change `WorkflowState` meaning without schema/version discipline
* introduce wide gameplay implementation
* change branch safety assumptions
* add broad CI write authority
* grant Codex unrestricted implementation authority

---

## File-Scope Guidance

### Usually Safe-to-Touch Areas

These may be modified if the task clearly justifies it and the scope is bounded:

* `docs/protocols/`
* `docs/templates/`
* `docs/examples/`
* `automation/langgraph/schemas/`
* `automation/langgraph/tests/`
* `automation/scripts/`
* `.github/codex/prompts/`

### Sensitive Areas

Treat these as sensitive and higher review risk:

* `.github/workflows/`
* `game/tales-of-dusk/project.godot`
* `game/tales-of-dusk/scenes/boot/`
* `game/tales-of-dusk/scripts/autoload/`
* `automation/langgraph/graphs/`
* `automation/langgraph/schemas/workflow_state.py`

### Highly Sensitive Areas

Do not modify casually:

* branch policy assumptions
* root `AGENTS.md`
* protected architecture records
* accepted protocol semantics
* accepted workflow stage machine semantics

---

## Review Guidance

When reviewing repository work, prioritize:

### 1. Baseline protection

Did the change break or quietly alter:

* runtime invariants,
* workflow invariants,
* protected branch assumptions,
* accepted phase boundaries?

### 2. Scope discipline

Did the change stay within its stated objective and non-goals?

### 3. File boundary discipline

Did the change remain within reasonable allowed file scope?

### 4. Traceability

Can the change be traced to:

* a phase objective,
* an architecture record,
* a spec/task context,
* a clearly stated repository need?

### 5. Test alignment

Were tests or validation updated where needed?
Did the change leave accepted behavior intact?

### 6. Hidden drift

Did the change introduce:

* architecture drift,
* semantic drift,
* undocumented workflow behavior,
* future maintenance hazards?

When uncertain, prefer surfacing blockers rather than pretending work is ready.

---

## Output Contract for Any Codex Work

For any meaningful analysis or implementation-oriented output, produce all of the following:

### 1. Summary

What was done.

### 2. Files Changed or Reviewed

Which repository areas were touched or inspected.

### 3. Risks Introduced

Any new risk, uncertainty, or scope sensitivity created by the work.

### 4. Intentionally Not Changed

What was explicitly left alone.

### 5. Manual Verification Steps

What a human should do to verify the result.

Do not produce vague “done” messages without these elements when work is substantial.

---

## Documentation Discipline

When creating or modifying workflow artifacts:

* preserve header completeness,
* preserve artifact identity and version meaning,
* preserve traceability,
* do not silently supersede artifacts,
* do not casually rewrite architecture history.

Examples, templates, and protocol docs must remain coherent with schemas.

Do not create “example” artifacts that secretly act as unofficial production specs.

---

## Schema Discipline

When touching `automation/langgraph/schemas/`:

* use explicit Pydantic models,
* prefer structure over free-form blobs,
* forbid extra fields unless there is a deliberate reason,
* keep schema meaning aligned with protocol documents,
* update tests when schema behavior changes,
* update schema/version assumptions when structural meaning changes.

Do not put runtime objects, clients, or non-serializable values into workflow state.

---

## Orchestration Discipline

When touching LangGraph graph code:

* preserve accepted stage ordering,
* preserve deterministic behavior unless a later phase explicitly introduces model-driven behavior,
* keep routing logic explicit,
* keep baseline blockers explicit,
* do not silently replace the accepted minimal graph with a materially different execution model.

If graph behavior changes meaningfully, document it.

---

## Prompt Asset Discipline

When touching `.github/codex/prompts/`:

* keep prompts bounded and task-specific,
* avoid vague or open-ended repository authority,
* align prompts with protocol and branch safety rules,
* prefer reproducible prompt-file usage over ad hoc one-off prompt text,
* keep prompts compatible with repository phase boundaries.

Prompt files are repository assets, not disposable scratch text.

---

## Remote Workflow Discipline

When touching `.github/workflows/`:

* prefer conservative permissions,
* prefer explicit manual dispatch for Codex entry at this phase,
* do not silently grant write authority,
* do not assume runner trust,
* do not use unsafe settings unless explicitly justified.

Remote automation is sensitive.
Treat workflow YAML as security-relevant infrastructure.

---

## Human Approval Triggers

Stop and require explicit human approval if work would affect:

* save compatibility
* accepted runtime baseline
* accepted workflow stage semantics
* branch safety policy
* Codex authority boundaries
* CI secret exposure risk
* broad repository refactors
* broad gameplay scope expansion

If a task is ambiguous and may cross one of these boundaries, surface the ambiguity clearly.

---

## What This Repository Is Not

Do not treat this repository as:

* a blank Godot prototype,
* a one-shot game jam project,
* an unconstrained LLM coding sandbox,
* a repo where prompts override architecture,
* a repo where examples are production truth,
* a repo where CI/CD should be expanded casually.

It is a governed automation workflow repository with a runtime project inside it.

---

## Practical Default Operating Mode

Unless a task explicitly authorizes more, the default operating mode is:

* inspect first,
* summarize repository constraints,
* identify scope,
* avoid protected baselines,
* propose bounded next actions,
* prefer review-first over write-first.

For remote Codex entry, the default accepted posture is:

* manual trigger,
* prompt-file based,
* conservative permissions,
* no direct `main` modification.

---

## Conflict Resolution Rule

If there is conflict between:

* an ad hoc prompt,
* an informal comment,
* a convenience refactor idea,
* or an assumption inferred from current files,

and:

* architecture records,
* protocol documents,
* workflow stage rules,
* protected baseline rules,
* explicit branch safety assumptions,

then the repository governance documents take priority.

---

## Final Operating Instruction

Be precise.

Be bounded.

Be explicit about uncertainty.

Do not silently expand authority.

Do not treat repository familiarity as approval.

When in doubt, preserve the accepted baseline and surface the issue instead of “helpfully” improvising across protected boundaries.
