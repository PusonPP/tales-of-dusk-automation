# Workflow Stage Machine

## 1. Purpose

This document defines the canonical stage machine for the Tales of Dusk automated development workflow.

Its purpose is to ensure that:
- workflow stages advance in a controlled and auditable order,
- agent outputs are consumed only when they are valid for the next stage,
- implementation cannot begin without approved upstream artifacts,
- QA and acceptance act as explicit gates rather than informal checks,
- change requests re-enter the workflow through controlled rollback paths,
- human approval points are explicit and resumable.

This stage machine is the repository-level source of truth for:
- canonical workflow stages,
- stage entry conditions,
- stage exit conditions,
- allowed transitions,
- forbidden transitions,
- rollback rules,
- approval gates,
- release-readiness rules.

This document complements, but does not replace:
- `docs/protocols/automation_protocol.md`
- machine-readable schemas in `automation/langgraph/schemas/`
- future LangGraph graph implementation

If any implementation conflicts with this stage machine, this document wins unless a newer approved version supersedes it.

---

## 2. Canonical Workflow Stages

The canonical stage flow is:

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

These stage names are canonical and should match machine-readable enums and workflow code.

---

## 3. Stage Definitions

### 3.1 `brief_intake`

#### Purpose

Normalize user input into a structured and bounded problem statement.

#### Typical producers

* `BriefInterpreter`

#### Typical outputs

* `Design Brief`

#### Entry conditions

* a new user request exists,
* or a major new workflow thread is started,
* or a change request has triggered re-entry into early planning.

#### Exit conditions

* a valid `Design Brief` exists,
* required non-negotiables are captured,
* obvious out-of-scope items are identified,
* success conditions for the next stage are present.

#### Allowed next stages

* `proposal`

#### Forbidden direct transitions

* `approved_spec`
* `codex_tasking`
* `implementation`
* `qa`
* `acceptance`
* `release_ready`

#### Notes

This stage is not for solving the entire design. It is for correctly framing the problem.

---

### 3.2 `proposal`

#### Purpose

Generate one or more structured proposed directions based on the brief.

#### Typical producers

* `GameDirector`
* `SystemDesigner`
* `TechnicalLead`
* `ScopeController`

#### Typical outputs

* `Proposal`

#### Entry conditions

* an active valid `Design Brief` exists,
* no unresolved blocker prevents proposal generation.

#### Exit conditions

* at least one valid `Proposal` exists,
* assumptions are explicit,
* alternatives have been considered where relevant,
* recommendation is stated clearly.

#### Allowed next stages

* `review`

#### Allowed rollback targets

* `brief_intake`

#### Forbidden direct transitions

* `codex_tasking`
* `implementation`
* `qa`
* `acceptance`
* `release_ready`

#### Notes

A proposal is not executable authority. It must be reviewed before becoming implementation input.

---

### 3.3 `review`

#### Purpose

Perform structured critique and decision-making on upstream artifacts.

#### Typical producers

* `Reviewer`
* `TechnicalLead`
* `ScopeController`
* `AcceptanceReviewer`
* `QAValidator` (when applicable)

#### Typical outputs

* `Review`

#### Entry conditions

* a target artifact exists for review,
* the target artifact is complete enough to review.

#### Exit conditions

One of the following must be true:

* review outcome is `approve`,
* review outcome is `revise`,
* review outcome is `reject`.

#### Allowed next stages

* `approved_spec` if outcome is `approve`
* `proposal` if outcome is `revise`
* `brief_intake` if the problem framing itself must be reconsidered
* workflow stop / human intervention if outcome is `reject`

#### Allowed rollback targets

* `proposal`
* `brief_intake`

#### Forbidden direct transitions

* `implementation`
* `qa`
* `acceptance`
* `release_ready`

#### Notes

Review is a gate, not a suggestion layer. A review outcome must explicitly control what happens next.

---

### 3.4 `approved_spec`

#### Purpose

Convert reviewed direction into an approved implementation contract.

#### Typical producers

* `TechnicalLead`
* `SystemDesigner`
* `ScopeController`

#### Typical outputs

* `Approved Spec`

#### Entry conditions

* a reviewed proposal exists,
* review outcome permits advancement,
* blockers from review have been resolved or accepted.

#### Exit conditions

* an `Approved Spec` exists and is marked approved,
* scope is explicit,
* constraints are explicit,
* non-goals are explicit,
* acceptance criteria are explicit,
* required tests are identified.

#### Allowed next stages

* `codex_tasking`

#### Allowed rollback targets

* `review`
* `proposal`

#### Forbidden direct transitions

* `implementation`
* `qa`
* `acceptance`
* `release_ready`

#### Notes

This is the last stage before executable work packaging. No implementation should begin without it.

---

### 3.5 `codex_tasking`

#### Purpose

Translate approved scope into one bounded implementation order for Codex.

#### Typical producers

* `CodexTaskWriter`
* `TechnicalLead`

#### Typical outputs

* `Codex Task`

#### Entry conditions

* an active approved `Approved Spec` exists,
* the requested implementation scope is bounded,
* file scope boundaries are known,
* acceptance criteria are available.

#### Exit conditions

* a valid `Codex Task` exists,
* allowed files are explicit,
* forbidden files are explicit,
* verification steps are explicit,
* reviewer role is defined.

#### Allowed next stages

* `implementation`

#### Allowed rollback targets

* `approved_spec`
* `review`

#### Forbidden direct transitions

* `qa`
* `acceptance`
* `release_ready`

#### Notes

A Codex Task is the only artifact type that may directly instruct implementation work.

---

### 3.6 `implementation`

#### Purpose

Execute the bounded implementation described by the active Codex Task.

#### Typical producers

* `CodexImplementer`
* human implementer if used manually under the same protocol

#### Typical outputs

* changed files
* implementation notes
* candidate build / candidate commit

#### Entry conditions

* a valid `Codex Task` exists,
* task boundaries are explicit,
* no unresolved approval gate blocks execution.

#### Exit conditions

* implementation work is complete for the active task,
* required outputs exist,
* changed files remain within allowed scope,
* implementation is ready for QA.

#### Allowed next stages

* `qa`

#### Allowed rollback targets

* `codex_tasking`
* `approved_spec`

#### Forbidden direct transitions

* `acceptance`
* `release_ready`

#### Notes

Implementation completion does not mean acceptance. QA must still validate it.

---

### 3.7 `qa`

#### Purpose

Test the implemented work against the approved spec and task acceptance criteria.

#### Typical producers

* `QAValidator`

#### Typical outputs

* `QA Report`

#### Entry conditions

* implementation output exists,
* build or runnable target exists where required,
* testable scope is defined.

#### Exit conditions

* a valid `QA Report` exists,
* pass/fail results are recorded,
* blocking failures are classified,
* regression notes are recorded if relevant.

#### Allowed next stages

* `acceptance` if no unresolved blocking failures remain
* `codex_tasking` if implementation rework is required
* `approved_spec` if the issue reveals spec-level mismatch
* `review` if the issue reveals design/decision conflict

#### Allowed rollback targets

* `implementation`
* `codex_tasking`
* `approved_spec`
* `review`

#### Forbidden direct transitions

* `release_ready`

#### Notes

QA is a gate. Unresolved blocking failures must prevent acceptance.

---

### 3.8 `acceptance`

#### Purpose

Perform final decision-making on whether scoped work is accepted as a stable baseline.

#### Typical producers

* `AcceptanceReviewer`

#### Typical outputs

* `Acceptance Report`

#### Entry conditions

* QA has been completed,
* required evidence has been collected,
* no unresolved blocking failure remains unless explicitly waived.

#### Exit conditions

One of the following must be true:

* decision is `approve`,
* decision is `revise`,
* decision is `reject`.

#### Allowed next stages

* `release_ready` if decision is `approve`
* `codex_tasking` if decision is `revise`
* `approved_spec` or `review` if the issue is upstream and structural
* workflow stop / human escalation if decision is `reject`

#### Allowed rollback targets

* `qa`
* `codex_tasking`
* `approved_spec`
* `review`

#### Forbidden direct transitions

* `implementation` without going back through tasking
* skipping directly to a new unrelated stage

#### Notes

Acceptance determines whether the current work may become the next stable baseline.

---

### 3.9 `release_ready`

#### Purpose

Mark the scoped work as ready to merge into the stable baseline or continue to the next approved iteration.

#### Typical producers

* workflow gate
* release manager
* acceptance-controlled merge logic

#### Typical outputs

* merge recommendation
* stable baseline update
* next iteration entry point

#### Entry conditions

* an approved `Acceptance Report` exists,
* no blocking issue remains,
* baseline update is authorized.

#### Exit conditions

* stable baseline is updated,
* or next workflow thread begins from the accepted baseline.

#### Allowed next stages

* new `brief_intake`
* new `change_request` path
* workflow completion

#### Allowed rollback targets

* `acceptance`

#### Forbidden direct transitions

* none in principle, but this stage should not silently bypass prior gates

#### Notes

This is not the stage where design is invented. It is the stage where accepted work becomes part of the project baseline.

---

## 4. Mandatory Transition Rules

The following transition rules are mandatory.

### Rule 1

No workflow may enter `codex_tasking` without an active approved `Approved Spec`.

### Rule 2

No workflow may enter `implementation` without an active valid `Codex Task`.

### Rule 3

No workflow may enter `acceptance` without at least one relevant `QA Report`.

### Rule 4

No workflow may enter `release_ready` with unresolved blocking QA failures.

### Rule 5

No major design or scope change may bypass `proposal` and `review`.

### Rule 6

No direct user-requested change may silently modify an active baseline without a `Change Request` if the change is meaningful.

### Rule 7

No stage may infer approval implicitly. Approval must be explicit.

### Rule 8

Rollback is permitted only to a meaningful upstream stage, not to arbitrary midpoints without traceability.

---

## 5. Allowed Transition Matrix

| From             | Allowed To                                                        |
| ---------------- | ----------------------------------------------------------------- |
| `brief_intake`   | `proposal`                                                        |
| `proposal`       | `review`, `brief_intake`                                          |
| `review`         | `approved_spec`, `proposal`, `brief_intake`                       |
| `approved_spec`  | `codex_tasking`, `review`, `proposal`                             |
| `codex_tasking`  | `implementation`, `approved_spec`, `review`                       |
| `implementation` | `qa`, `codex_tasking`, `approved_spec`                            |
| `qa`             | `acceptance`, `codex_tasking`, `approved_spec`, `review`          |
| `acceptance`     | `release_ready`, `codex_tasking`, `approved_spec`, `review`, `qa` |
| `release_ready`  | new `brief_intake`, change-driven re-entry                        |

Any transition not listed above is forbidden unless a future approved version of this document changes the rules.

---

## 6. Forbidden Transition Examples

The following are explicitly forbidden:

* `brief_intake -> implementation`
* `proposal -> implementation`
* `proposal -> qa`
* `review -> implementation`
* `approved_spec -> qa`
* `codex_tasking -> acceptance`
* `implementation -> release_ready`
* `qa -> release_ready`
* `change_request -> implementation` without re-entry through planning/review/spec stages

These examples are not exhaustive. The transition matrix is authoritative.

---

## 7. Entry and Exit Gate Logic

### 7.1 Stage entry gate

A stage may only begin if:

* required upstream artifacts exist,
* required approval states exist,
* blockers do not forbid entry,
* the transition is allowed by this document.

### 7.2 Stage exit gate

A stage may only be considered complete if:

* required outputs exist,
* outputs pass minimum completeness rules,
* required decisions are explicit,
* downstream stage inputs are satisfiable.

### 7.3 Failure to satisfy gate conditions

If entry or exit conditions are not met:

* the workflow must remain at the current stage,
* or roll back to a valid upstream stage,
* or request human intervention.

---

## 8. Rollback Rules

Rollback is not failure by itself. It is a controlled correction mechanism.

### 8.1 Valid rollback triggers

Rollback is appropriate when:

* review finds unresolved structural issues,
* QA finds blocking failures,
* acceptance finds scope mismatch,
* a change request invalidates prior assumptions,
* required approval is missing,
* implementation output violates allowed file boundaries,
* architecture drift is detected.

### 8.2 Rollback targets

Rollback must target the earliest stage that can properly resolve the problem.

Examples:

* wording ambiguity -> `proposal`
* insufficient scope boundary -> `approved_spec`
* file scope issue in Codex task -> `codex_tasking`
* QA failure from wrong implementation -> `codex_tasking` or `implementation`
* design contradiction revealed by QA -> `review`
* user-requested feature expansion -> `proposal` or `review`

### 8.3 Invalid rollback behavior

The workflow must not:

* silently overwrite active artifacts,
* skip rollback records,
* pretend downstream work is still valid if upstream assumptions changed materially.

---

## 9. Human Approval and Interrupts

This workflow is autonomous but controlled. Certain conditions require human approval.

### 9.1 Human approval triggers

Human approval should be required when:

* save schema changes,
* branch policy changes,
* CI privilege changes,
* architecture boundary changes,
* autoload/global state expansion,
* scope expansion beyond current approved limits,
* compatibility risk becomes high or critical,
* approval responsibility is explicitly assigned by protocol.

### 9.2 Interrupt behavior

When human approval is required:

* the workflow must set a pending interrupt,
* the current stage must be recorded,
* the reason must be explicit,
* resume must continue from the correct stage after approval.

### 9.3 No silent bypass

Human approval requirements must not be bypassed by retrying the same stage with hidden changes.

---

## 10. Change Request Routing

A `Change Request` is not a normal forward stage. It is a re-entry trigger.

### 10.1 Change Request effect

When a valid `Change Request` is created, the workflow must determine its impact level and route back accordingly.

### 10.2 Recommended routing by impact

#### Low-impact change

Examples:

* wording clarification,
* small bounded UI polish,
* non-structural presentation adjustment

Recommended re-entry:

* `approved_spec`
* or `codex_tasking`

#### Medium-impact change

Examples:

* new bounded feature within current architecture,
* revised acceptance criteria,
* content or room flow adjustment with limited system impact

Recommended re-entry:

* `proposal`
* `review`
* then `approved_spec`

#### High-impact or critical change

Examples:

* core loop change,
* save compatibility impact,
* architecture restructuring,
* major scope change,
* Godot runtime baseline change

Recommended re-entry:

* `brief_intake`
* or `proposal`
* followed by full `review` and new `approved_spec`

### 10.3 Prohibited behavior

A change request must not directly trigger implementation unless the workflow explicitly re-establishes a valid approved spec and codex task.

---

## 11. QA Gate Rules

### 11.1 QA is mandatory for executable work

Any implementation that affects runtime behavior, workflow infrastructure, repository policy, or delivery correctness must pass through QA before acceptance.

### 11.2 Blocking QA failures

A QA failure is blocking if it:

* breaks required stage objectives,
* violates approved acceptance criteria,
* causes scene flow failure,
* causes state corruption,
* causes unapproved file scope drift,
* breaks required runtime invariants,
* introduces regression in an accepted baseline.

### 11.3 Non-blocking QA issues

A QA issue may be non-blocking if it:

* does not violate current acceptance criteria,
* does not destabilize baseline behavior,
* is explicitly documented,
* has a planned remediation path.

### 11.4 Acceptance dependency

Acceptance must not proceed on incomplete or ambiguous QA evidence.

---

## 12. Acceptance Gate Rules

### 12.1 Acceptance authority

Acceptance is the stage that decides whether scoped work becomes baseline-ready.

### 12.2 Acceptance inputs

Acceptance should review at minimum:

* relevant `Approved Spec`
* relevant `Codex Task`
* implementation evidence
* `QA Report`
* any open risk relevant to the scoped work

### 12.3 Acceptance outcomes

Acceptance must explicitly output one of:

* `approve`
* `revise`
* `reject`

### 12.4 Outcome effects

#### Approve

* may proceed to `release_ready`

#### Revise

* must return to `codex_tasking`, `approved_spec`, or `review` depending on issue source

#### Reject

* must stop baseline advancement
* may require escalation or major replanning

---

## 13. Release-Ready Rules

### 13.1 Meaning

`release_ready` means the scoped work is ready to become part of the stable baseline.

### 13.2 Minimum requirements

To enter `release_ready`, all of the following must be true:

* acceptance decision is `approve`,
* required QA evidence exists,
* no unresolved blocking failure remains,
* required approvals are complete,
* active artifacts are internally consistent.

### 13.3 Stable baseline update

A release-ready result may:

* merge into `integration` as the new stage baseline,
* or merge from `integration` into `main` if the repository policy allows it,
* or become the accepted baseline for the next iteration thread.

### 13.4 No hidden instability

Release-ready must not be used as a cosmetic label for partially working or unverified output.

---

## 14. Artifact-State Consistency Rules

Workflow stage and artifact states must remain consistent.

### 14.1 Examples

* If stage is `approved_spec`, there must be an active approved spec artifact.
* If stage is `codex_tasking`, there must be an active approved spec available for task generation.
* If stage is `qa`, there must be a completed implementation candidate under test.
* If stage is `acceptance`, there must be QA evidence.
* If stage is `release_ready`, acceptance must already be approved.

### 14.2 Inconsistency handling

If workflow stage and artifact states disagree:

* workflow must halt,
* inconsistency must be recorded as blocker,
* rollback or manual correction must occur before continuation.

---

## 15. Repository-Specific Baseline Invariants

For the current repository baseline, the following runtime invariants are assumed to exist:

* main scene path: `res://scenes/boot/boot.tscn`
* title scene path: `res://scenes/title/title.tscn`
* chapter map scene path: `res://scenes/chapter_map/chapter_map.tscn`
* room test scene path: `res://scenes/rooms/room_test.tscn`
* required autoloads:

  * `EventBus`
  * `GameSession`
  * `SaveSystem`
  * `SceneRouter`
* current room phase order:

  * `Preview`
  * `Deploy`
  * `Combat`
  * `Result`

If a workflow change would invalidate these assumptions, a `Change Request` and upstream re-approval are required.

---

## 16. Minimal Compliance Checklist

The workflow is compliant with this stage machine only if:

* it uses the canonical stage names,
* it follows allowed transitions only,
* it blocks forbidden direct transitions,
* it requires approved spec before tasking,
* it requires codex task before implementation,
* it requires QA before acceptance,
* it requires acceptance before release-ready,
* it records rollback explicitly,
* it preserves traceability across stage changes,
* it records human approval requirements explicitly.

---

## 17. Example Stage Progression

A normal successful progression may look like this:

1. `brief_intake`

   * produce `BRF-0001`
2. `proposal`

   * produce `PRP-0001`
3. `review`

   * produce `RVW-0001` with decision `approve`
4. `approved_spec`

   * produce `SPEC-0001`
5. `codex_tasking`

   * produce `CTX-0001`
6. `implementation`

   * produce bounded repository changes
7. `qa`

   * produce `QAR-0001` with no blocking failures
8. `acceptance`

   * produce `ACC-0001` with decision `approve`
9. `release_ready`

   * mark scope ready for stable baseline update

A revision path may look like this:

1. `brief_intake`
2. `proposal`
3. `review`

   * decision `revise`
4. rollback to `proposal`
5. revised proposal
6. `review`
7. `approved_spec`
8. `codex_tasking`
9. `implementation`
10. `qa`

* blocking failure found

11. rollback to `codex_tasking`
12. revised task
13. `implementation`
14. `qa`
15. `acceptance`
16. `release_ready`

---

## 18. Enforcement Rule

If future LangGraph code, Codex task generation logic, manual workflow habits, or CI gates contradict this document, they must be corrected to conform to this stage machine unless a newer approved version supersedes it.

This document is the canonical workflow-stage authority for repository process control.

---

## 19. Initial Status

Recommended initial metadata for this document:

* version: `1.0.0`
* status: `approved`

Once committed and referenced by the schema/workflow layer, this document becomes active repository policy for workflow stage control.