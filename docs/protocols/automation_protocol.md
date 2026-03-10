# Automation Protocol

## 1. Purpose

This document defines the canonical document protocol for the Tales of Dusk automated development workflow.

Its purpose is to ensure that:
- every agent produces auditable artifacts,
- every artifact has a stable identity and lifecycle,
- every workflow stage consumes explicit inputs and produces explicit outputs,
- Codex only receives approved and bounded implementation tasks,
- QA and acceptance decisions are traceable,
- future iterations evolve from prior approved artifacts instead of restarting from scratch.

This protocol is the repository-level source of truth for:
- workflow document types,
- shared metadata fields,
- artifact lifecycle states,
- artifact versioning rules,
- naming and storage conventions,
- approval and supersession rules,
- traceability across design, implementation, QA, and acceptance.

---

## 2. Scope

This protocol applies to all workflow-generated artifacts inside this repository, including but not limited to:

- `Design Brief`
- `Proposal`
- `Review`
- `Approved Spec`
- `Codex Task`
- `QA Report`
- `Acceptance Report`
- `Change Request`

This protocol governs:
- human-authored artifacts,
- agent-authored artifacts,
- mixed human/agent reviewed artifacts.

This protocol does **not** define:
- the concrete LangGraph graph implementation,
- the concrete Codex execution runtime,
- GitHub Actions workflow code,
- the final game design itself.

Those are defined elsewhere, but they must conform to this protocol.

---

## 3. Core Principles

### 3.1 Documents are first-class production artifacts
Documents are not optional notes. They are part of the production system and must be versioned, reviewed, and traceable.

### 3.2 No implementation without approved specification
No implementation task may be issued to Codex unless there is an active `Approved Spec` covering the requested scope.

### 3.3 No silent scope expansion
If a request changes scope, constraints, architecture, save compatibility, UI flow, or system boundaries, a `Change Request` must be created before implementation continues.

### 3.4 Small, reviewable increments
Artifacts should support narrow, reviewable progress rather than broad and ambiguous redesign.

### 3.5 Every artifact must be traceable
Each artifact must identify:
- what it is,
- who produced it,
- what it depends on,
- what it supersedes,
- what workflow thread it belongs to.

### 3.6 Machine-readable before automation
Any artifact intended to be consumed by workflow code must have a machine-readable structure compatible with repository schemas.

---

## 4. Canonical Artifact Types

The workflow uses the following canonical artifact types.

### 4.1 Design Brief
Defines the initial interpreted problem statement based on user input.

Purpose:
- normalize the user’s high-level request,
- freeze non-negotiables,
- identify what is in scope and out of scope,
- establish success conditions for the next phase.

Typical producer:
- `BriefInterpreter`

Typical consumers:
- `GameDirector`
- `ScopeController`
- `SystemDesigner`
- `TechnicalLead`

---

### 4.2 Proposal
Defines one concrete proposed direction, usually before approval.

Purpose:
- turn a brief into an actionable direction,
- expose assumptions,
- compare alternatives,
- make recommendations while surfacing risk.

Typical producer:
- `GameDirector`
- `SystemDesigner`
- `TechnicalLead`
- `ScopeController`

Typical consumers:
- reviewers
- approvers
- decision nodes in LangGraph

---

### 4.3 Review
Captures structured critique of another artifact.

Purpose:
- identify blocking issues,
- identify non-blocking issues,
- determine whether revision is required,
- produce a clear review decision.

Typical producer:
- `Reviewer`
- `TechnicalLead`
- `AcceptanceReviewer`
- `QAValidator`

Typical consumers:
- original artifact owner
- approval nodes
- escalation logic

---

### 4.4 Approved Spec
Defines the approved implementation contract for a bounded scope.

Purpose:
- convert proposals and reviews into a stable, approved contract,
- define scope, constraints, non-goals, and acceptance criteria,
- become the authoritative input for implementation task generation.

Typical producer:
- `TechnicalLead`
- `SystemDesigner`
- `ScopeController`

Typical consumers:
- `CodexTaskWriter`
- `CodexImplementer`
- `QAValidator`
- `AcceptanceReviewer`

---

### 4.5 Codex Task
Defines one bounded implementation order sent to Codex.

Purpose:
- translate approved spec into a narrow executable task,
- specify allowed files and forbidden files,
- define acceptance criteria and verification steps,
- reduce overreach and architecture drift.

Typical producer:
- `CodexTaskWriter`
- `TechnicalLead`

Typical consumers:
- `CodexImplementer`
- `CodeReviewer`
- `QAValidator`

---

### 4.6 QA Report
Captures test execution results against implemented work.

Purpose:
- record what was tested,
- record pass/fail outcomes,
- classify bugs and regressions,
- determine readiness for acceptance review.

Typical producer:
- `QAValidator`

Typical consumers:
- `AcceptanceReviewer`
- `TechnicalLead`
- `CodexTaskWriter`

---

### 4.7 Acceptance Report
Captures final scope acceptance decision.

Purpose:
- record the acceptance decision for a specific scope,
- determine whether the artifact chain may proceed,
- authorize merge/release readiness or force rework.

Typical producer:
- `AcceptanceReviewer`

Typical consumers:
- workflow gate logic
- release manager
- branch merge decision process

---

### 4.8 Change Request
Defines requested change against an existing approved baseline.

Purpose:
- capture user-requested or internally required change,
- assess compatibility impact,
- prevent hidden redesign,
- route the workflow back into review/spec phases when needed.

Typical producer:
- user proxy node
- `ScopeController`
- `TechnicalLead`
- `AcceptanceReviewer`

Typical consumers:
- review stage
- impact analysis stage
- proposal/spec generation stage

---

## 5. Required Artifact Header

Every protocol artifact must begin with a machine-readable header.

Recommended format: YAML front matter.

Example:

```yaml
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
```

### 5.1 Required header fields

| Field                | Required | Meaning                                                    |
| -------------------- | -------- | ---------------------------------------------------------- |
| `artifact_id`        | yes      | Stable unique artifact identifier                          |
| `artifact_type`      | yes      | Canonical artifact type                                    |
| `version`            | yes      | Semantic version string                                    |
| `status`             | yes      | Current lifecycle state                                    |
| `project_id`         | yes      | Project identifier                                         |
| `workflow_thread_id` | yes      | Workflow execution thread identifier                       |
| `author_role`        | yes      | Producing role or node                                     |
| `created_at`         | yes      | UTC timestamp of first creation                            |
| `updated_at`         | yes      | UTC timestamp of latest update                             |
| `supersedes`         | yes      | Prior artifact ID if replacing older artifact, else `null` |
| `related_artifacts`  | yes      | List of linked artifact IDs                                |

### 5.2 Header rules

* Header fields must be complete.
* Timestamps must use UTC ISO 8601 format.
* `artifact_type` must match one canonical type exactly.
* `artifact_id` must be stable after creation.
* `version` must change whenever meaningful content changes.
* `supersedes` must be populated when a newer artifact replaces an older one.

---

## 6. Artifact Lifecycle States

The canonical lifecycle states are:

* `draft`
* `in_review`
* `approved`
* `rejected`
* `superseded`
* `implemented`
* `archived`

### 6.1 Meaning of each state

#### `draft`

Artifact exists but has not entered formal review.

#### `in_review`

Artifact is under active review and must not be treated as final input to downstream implementation unless explicitly allowed.

#### `approved`

Artifact is accepted for downstream use.

#### `rejected`

Artifact is not approved and must not be used for downstream implementation.

#### `superseded`

Artifact was valid historically but has been replaced by a newer version or newer artifact.

#### `implemented`

The implementation corresponding to this artifact has been completed.

#### `archived`

Artifact is retained for history but no longer active in workflow decision making.

### 6.2 Lifecycle rules

* A `Codex Task` must not enter `approved` unless its parent `Approved Spec` is already `approved`.
* A `QA Report` with unresolved blocking failures must not allow downstream acceptance.
* A rejected artifact may remain in history but must not be used as active source of truth.
* Superseded artifacts must remain stored for auditability.

---

## 7. Versioning Rules

All artifacts use semantic versioning:

* `major.minor.patch`

### 7.1 Major version change

Increase major version when:

* scope changes,
* architecture changes,
* constraints materially change,
* acceptance criteria materially change,
* compatibility assumptions change.

Example:

* `1.2.3` -> `2.0.0`

### 7.2 Minor version change

Increase minor version when:

* approved scope is expanded without invalidating prior structure,
* new sections or fields are added,
* more explicit detail is added without changing prior meaning.

Example:

* `1.2.3` -> `1.3.0`

### 7.3 Patch version change

Increase patch version when:

* wording is clarified,
* formatting is corrected,
* metadata is corrected,
* no meaningful behavioral or scope meaning changes.

Example:

* `1.2.3` -> `1.2.4`

### 7.4 Versioning discipline

* Do not overwrite meaning without changing version.
* Do not create a new artifact ID when only a version change is needed.
* Create a new artifact only when it represents a distinct artifact role or distinct workflow output.

---

## 8. Artifact Naming Convention

### 8.1 Artifact IDs

Recommended prefixes:

* `BRF-` for Design Brief
* `PRP-` for Proposal
* `RVW-` for Review
* `SPEC-` for Approved Spec
* `CTX-` for Codex Task
* `QAR-` for QA Report
* `ACC-` for Acceptance Report
* `CR-` for Change Request

Examples:

* `BRF-0001`
* `PRP-0003`
* `SPEC-0010`
* `CTX-0042`

### 8.2 File naming pattern

Recommended file pattern:

```text
<artifact_id>_<slug>_v<version>.md
```

Example:

```text
BRF-0001_bootstrap-protocols_v1.0.0.md
SPEC-0004_room-state-machine_v1.1.0.md
CTX-0008_room-state-ui-hookup_v1.0.0.md
```

### 8.3 Slug rules

* lowercase
* words separated with hyphens
* short but descriptive
* no spaces
* no non-ASCII punctuation

---

## 9. Storage Rules

Artifacts must be stored in the appropriate repository folders.

### 9.1 Canonical storage locations

| Artifact Type     | Directory                  |
| ----------------- | -------------------------- |
| Design Brief      | `docs/briefs/`             |
| Proposal          | `docs/proposals/`          |
| Review            | `docs/reviews/`            |
| Approved Spec     | `docs/approved_specs/`     |
| Codex Task        | `docs/codex_tasks/`        |
| QA Report         | `docs/qa_reports/`         |
| Acceptance Report | `docs/acceptance_reports/` |
| Change Request    | `docs/change_requests/`    |

### 9.2 Protocol and template locations

* Protocol definitions go in `docs/protocols/`
* Reusable blank templates go in `docs/templates/`
* Sample artifacts go in `docs/examples/`

### 9.3 No relocation without migration note

If an artifact path changes, the repository must preserve traceability through:

* updated references,
* migration note,
* or a redirect/reference record.

---

## 10. Required Traceability

Every downstream artifact must reference its upstream source artifacts.

### 10.1 Minimum traceability requirements

* A `Proposal` must reference the `Design Brief` it answers.
* A `Review` must reference the artifact it reviews.
* An `Approved Spec` must reference the `Proposal` and relevant `Review` artifacts it resolves.
* A `Codex Task` must reference the `Approved Spec` it operationalizes.
* A `QA Report` must reference the `Codex Task` and build under test.
* An `Acceptance Report` must reference the `Approved Spec`, `QA Report`, and relevant implementation evidence.
* A `Change Request` must reference the currently active approved baseline it proposes to change.

### 10.2 Traceability rule

No artifact may be treated as valid workflow input if its upstream dependency is ambiguous.

---

## 11. Approval Rules

### 11.1 Approval authority

Each artifact type must have a defined approval role.

Recommended baseline:

| Artifact Type     | Typical Approver                |
| ----------------- | ------------------------------- |
| Design Brief      | GameDirector / ScopeController  |
| Proposal          | ScopeController / TechnicalLead |
| Review            | role-dependent                  |
| Approved Spec     | TechnicalLead + ScopeController |
| Codex Task        | TechnicalLead                   |
| QA Report         | QAValidator                     |
| Acceptance Report | AcceptanceReviewer              |
| Change Request    | ScopeController / TechnicalLead |

### 11.2 Approval requirements

An artifact is only approved when:

* it is complete,
* required fields are present,
* upstream references are valid,
* blockers are addressed or explicitly waived,
* approval is explicitly recorded.

### 11.3 Implicit approval is forbidden

Silence is not approval.
Lack of response is not approval.
A downstream stage may not infer approval unless an explicit approval record exists.

---

## 12. Supersession Rules

When a newer artifact replaces an older one:

* the newer artifact must reference the older artifact in `supersedes`,
* the older artifact status should become `superseded`,
* downstream workflows must use the newest active approved artifact.

### 12.1 When to supersede

Supersession is appropriate when:

* a brief is materially updated,
* a proposal is revised after review,
* an approved spec is replaced by a newer approved version,
* a codex task is re-issued because prior task scope is invalidated.

### 12.2 When not to supersede

Do not supersede merely for:

* spelling corrections,
* formatting only,
* trivial metadata clean-up.

Use patch versioning instead.

---

## 13. Codex Tasking Protocol

A `Codex Task` is the only artifact type allowed to directly instruct Codex implementation.

### 13.1 A Codex Task must include

* background,
* current context,
* current phase,
* explicit objective,
* explicit non-goals,
* allowed files,
* forbidden files,
* acceptance criteria,
* verification steps,
* reviewer role.

### 13.2 A Codex Task must not

* invent new gameplay outside approved scope,
* modify architecture beyond approved boundaries,
* silently change save data shape,
* silently change UI flow,
* expand file scope without approval.

### 13.3 Codex input dependency rule

A `Codex Task` must reference:

* one active `Approved Spec`,
* any relevant prior `Codex Task`,
* any blocking `QA Report` if it is a rework task.

---

## 14. QA and Acceptance Protocol

### 14.1 QA Report minimum contents

A `QA Report` must record:

* build under test,
* scenarios tested,
* pass results,
* failures,
* severity classification,
* reproduction steps,
* regression notes.

### 14.2 Severity levels

Canonical severities:

* `low`
* `medium`
* `high`
* `critical`

### 14.3 Blocking rule

A blocking failure is any issue that:

* breaks the core stage objective,
* violates approved acceptance criteria,
* causes scene or flow failure,
* causes data loss or corrupted behavior,
* invalidates a required invariant.

Blocking failures must be resolved before acceptance.

### 14.4 Acceptance rule

An `Acceptance Report` may only approve scope when:

* relevant QA artifacts exist,
* blocking issues are resolved or explicitly waived,
* scope matches approved spec,
* evidence has been reviewed.

---

## 15. Change Request Protocol

A `Change Request` is mandatory when an active baseline is being changed in a meaningful way.

### 15.1 Trigger conditions

A `Change Request` must be created if any of the following changes:

* core gameplay loop,
* system boundaries,
* data model,
* save compatibility,
* UI flow,
* technical architecture,
* scope size,
* acceptance criteria,
* resource structure that affects workflow assumptions.

### 15.2 A Change Request must include

* requested change,
* reason,
* affected systems,
* compatibility risks,
* scope impact,
* approval requirement.

### 15.3 Change Request routing

A valid `Change Request` routes workflow back to:

* proposal,
* review,
* or approved spec generation,

depending on impact severity.

A `Change Request` must not directly trigger implementation without re-approval.

---

## 16. Machine-Readable Schema Policy

This repository requires that protocol artifacts be representable by machine-readable schemas.

### 16.1 Source of truth

Human-readable markdown and machine-readable schema must agree.

### 16.2 Schema validation

The automation layer should validate:

* header completeness,
* canonical enum values,
* required sections/fields,
* reference integrity where feasible.

### 16.3 Schema evolution

Schema changes must be versioned and recorded.
A schema change that invalidates prior artifact assumptions is a major change.

---

## 17. Workflow Stage Contract

The document protocol supports the following canonical stage flow:

```text
brief_intake
-> proposal
-> review
-> approved_spec
-> codex_tasking
-> implementation
-> qa
-> acceptance
-> release_ready
```

### 17.1 Mandatory stage constraints

* No `codex_tasking` without active `approved_spec`
* No `acceptance` with unresolved blocking QA failures
* No major change may bypass `proposal`/`review`
* No release-ready status without acceptance decision

### 17.2 Interrupt and human approval

If a workflow requires human approval:

* the state must record that requirement,
* the pending artifact must remain traceable,
* resume must continue from the correct stage with the same thread context.

---

## 18. Auditability and History

### 18.1 History preservation

Historical artifacts must not be silently deleted if they have participated in workflow decisions.

### 18.2 Audit record requirement

At minimum, the repository must preserve:

* artifact identity,
* version,
* status,
* producer role,
* linked dependencies,
* supersession chain.

### 18.3 Deletion policy

Artifacts already used in workflow decisions should be superseded or archived, not simply removed.

---

## 19. Minimal Compliance Checklist

An artifact is protocol-compliant only if all of the following are true:

* it has a valid header,
* it uses a canonical artifact type,
* it has a valid lifecycle status,
* it is stored in the proper directory,
* it references upstream dependencies where required,
* it follows versioning rules,
* it can be consumed by workflow participants without ambiguity.

---

## 20. Initial Repository Baseline

For this repository, the current baseline assumptions are:

* project id: `tales-of-dusk-automation`
* primary engine: `Godot 4`
* orchestration layer: `LangGraph`
* implementation agent: `Codex`
* CI gate: `GitHub Actions`
* local primary platform: `Windows`
* current runtime skeleton includes:

  * boot scene,
  * title scene,
  * chapter map scene,
  * room test scene,
  * autoloads: `EventBus`, `GameSession`, `SaveSystem`, `SceneRouter`

These baseline assumptions may evolve, but any meaningful change must follow this protocol.

---

## 21. Example Artifact Header

```yaml
artifact_id: SPEC-0001
artifact_type: approved_spec
version: 1.0.0
status: approved
project_id: tales-of-dusk-automation
workflow_thread_id: bootstrap-phase3
author_role: TechnicalLead
created_at: 2026-03-09T00:00:00Z
updated_at: 2026-03-09T00:00:00Z
supersedes: null
related_artifacts:
  - BRF-0001
  - PRP-0001
  - RVW-0001
```

---

## 22. Enforcement Rule

If a workflow artifact conflicts with this protocol, this protocol wins unless a newer approved protocol version explicitly supersedes it.

If automation code, prompts, or manual workflow behavior rely on undocumented assumptions that are inconsistent with this protocol, those assumptions must be corrected rather than silently preserved.

---

## 23. Document Status

This protocol becomes active once committed to the repository and referenced by the workflow state/schema layer.

Recommended initial status:

* version: `1.0.0`
* status: `approved`

Until superseded, this document is the canonical protocol definition for repository workflow artifacts.