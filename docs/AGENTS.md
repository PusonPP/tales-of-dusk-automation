# AGENTS.md

## Scope

This file governs work inside the documentation subtree:

```text
docs/
```

It refines the repository-root `AGENTS.md` with **documentation, protocol artifact, architecture record, template, and example-specific rules**.

If any instruction conflicts with the repository root `AGENTS.md`, the stricter rule wins.

If any instruction conflicts with accepted architecture records, protocol documents, or protected workflow baselines, those repository governance documents win.

---

## Mission of This Subtree

This subtree contains the repository’s documentation layer.

Its purpose is to store and evolve:

* architecture records,
* protocol definitions,
* artifact templates,
* example artifacts,
* workflow-generated artifacts,
* accepted design/review/spec/task/QA/acceptance records.

This subtree is **not** a casual notes area.

All work here must assume:

* documents are first-class production artifacts,
* documentation changes can change workflow authority,
* examples must not silently become production truth,
* templates and protocol text must remain aligned with schemas,
* architecture history must remain auditable.

Treat this subtree as workflow infrastructure, not prose decoration.

---

## Current Accepted Documentation Baseline

The repository currently has accepted documentation baselines from earlier phases.

### Accepted Architecture Layer

The repository contains accepted architecture records for:

* Phase 2 runtime baseline,
* Phase 3 protocol/state scope,
* Phase 4 minimal orchestrator acceptance,
* Phase 5 Codex entry scope.

These records are not disposable notes.

### Accepted Protocol Layer

The repository has accepted protocol documents defining:

* artifact semantics,
* lifecycle states,
* versioning rules,
* stage-machine semantics,
* rollback logic,
* approval discipline.

These documents are currently authoritative workflow sources of truth.

### Accepted Template Layer

The repository has canonical template files for:

* Design Brief
* Proposal
* Review
* Approved Spec
* Codex Task
* QA Report
* Acceptance Report
* Change Request

These templates are expected to remain semantically aligned with protocol and schema expectations.

### Accepted Example Layer

The repository has example artifact chains used to validate the workflow and protocol baseline.

These examples are fixture artifacts, not gameplay specifications.

---

## Source-of-Truth Files for This Subtree

Before modifying documentation in this subtree, consult at minimum:

### Root Governance

* repository root `AGENTS.md`

### Architecture Records

* `docs/architecture/001_phase2_godot_skeleton_accepted.md`
* `docs/architecture/002_phase3_protocol_state_scope.md`
* `docs/architecture/003_phase4_minimal_orchestrator_accepted.md`
* `docs/architecture/004_phase5_codex_entry_scope.md`

### Protocol Documents

* `docs/protocols/automation_protocol.md`
* `docs/protocols/workflow_stage_machine.md`

### Schema Layer

* `automation/langgraph/schemas/`
* especially:

  * `enums.py`
  * `common.py`
  * `items.py`
  * `workflow_state.py`

If a documentation edit would contradict these sources, stop and surface the conflict.

---

## Documentation Operating Principle

This subtree must evolve under a “documentation is policy” principle.

That means:

1. preserve meaning before style,
2. preserve traceability before brevity,
3. preserve explicitness before elegance,
4. preserve history before convenience,
5. preserve protocol/schema alignment before wording preference.

Do not rewrite documents in ways that accidentally change workflow authority.

---

## Hard Documentation Rules

### Rule 1: Do not silently change protocol meaning

A wording change that alters:

* artifact semantics,
* lifecycle status meaning,
* stage transitions,
* traceability expectations,
* approval meaning,
* supersession meaning,

is not an editorial cleanup.
It is a workflow policy change.

### Rule 2: Do not silently change architecture record meaning

Architecture records are historical acceptance/scope documents.
Do not rewrite them casually to “match current understanding” without preserving explicit history.

### Rule 3: Do not let examples become production truth

Example artifacts exist to validate the protocol and workflow chain.
They must not be silently treated as final production game design or implementation authority.

### Rule 4: Do not let templates drift away from schemas

Templates are for humans/agents to author artifacts, while schemas are for machine validation.
They must remain semantically aligned.

### Rule 5: Do not silently supersede artifacts

If a document replaces a prior artifact meaningfully, that should be explicit through metadata/status/versioning, not hidden through overwrite.

### Rule 6: Do not destroy auditability for readability

Shorter text is not better if it erases provenance, scope boundaries, or decision history.

### Rule 7: Prefer explicit metadata

Header fields, artifact identity, status, version, and related artifact references are required structure, not optional decoration.

### Rule 8: Do not add workflow authority through documentation convenience

Do not write docs that imply new implementation authority, branch authority, or automation authority unless that is explicitly approved.

---

## Subtree Layout Meaning

The documentation subtree is currently expected to contain areas such as:

```text
docs/
├─ architecture/
├─ protocols/
├─ templates/
├─ examples/
├─ briefs/
├─ proposals/
├─ reviews/
├─ approved_specs/
├─ codex_tasks/
├─ qa_reports/
├─ acceptance_reports/
└─ change_requests/
```

### `docs/architecture/`

Architecture records and accepted scope/baseline records.
High sensitivity.
History-bearing.

### `docs/protocols/`

Canonical workflow policy documents.
Very high sensitivity.

### `docs/templates/`

Canonical authoring templates for workflow artifacts.
Sensitive and schema-aligned.

### `docs/examples/`

Example/fixed artifact chains for validation and demonstration.
Must not silently become normative production content.

### `docs/briefs/`

Actual Design Brief artifacts.

### `docs/proposals/`

Actual Proposal artifacts.

### `docs/reviews/`

Actual Review artifacts.

### `docs/approved_specs/`

Actual Approved Spec artifacts.

### `docs/codex_tasks/`

Actual Codex Task artifacts.

### `docs/qa_reports/`

Actual QA reports.

### `docs/acceptance_reports/`

Actual acceptance decisions.

### `docs/change_requests/`

Actual change request artifacts.

---

## Metadata Rules

### All Workflow Artifacts Require Structured Headers

Where protocol requires it, workflow artifacts must carry machine-readable metadata headers.

At minimum, preserve fields such as:

* `artifact_id`
* `artifact_type`
* `version`
* `status`
* `project_id`
* `workflow_thread_id`
* `author_role`
* `created_at`
* `updated_at`
* `supersedes`
* `related_artifacts`

### Do Not Omit Required Metadata for Convenience

If a document becomes shorter by removing metadata, that is usually the wrong tradeoff.

### Timestamps Should Remain Explicit

Do not replace precise timestamps with vague references if the artifact is meant to be traceable.

---

## Versioning Rules for Documents

### Respect Semantic Versioning Intent

When documents are versioned, preserve the meaning of:

* major version = material semantic change
* minor version = additive or scope-extending change without invalidating structure
* patch version = wording/clarity/metadata fixes without semantic change

### Do Not Change Meaning Without Version Awareness

If document meaning changes, version discipline should reflect that.

### Do Not Spawn New Artifact IDs Casually

A revised artifact is not automatically a new artifact.
Respect the identity/supersession model established by protocol.

---

## Architecture Record Rules

### Architecture Records Are Historical Decisions

Treat files in `docs/architecture/` as formal acceptance/scope records, not mutable summaries.

### Preserve Historical Context

Do not rewrite a record to make the past look cleaner or more current than it was.

### If a Later Record Replaces an Earlier Assumption

Create a new record or explicit supersession, rather than rewriting older records as if they always said the newer thing.

### High-Risk Changes

Changes to accepted architecture records should be treated as sensitive and usually require explicit human review.

---

## Protocol Document Rules

### Protocol Docs Are Policy

Files in `docs/protocols/` define repository workflow policy.

Do not casually:

* rewrite stage meanings,
* alter artifact type definitions,
* alter approval conditions,
* alter rollback logic,
* alter supersession rules,
* alter storage rules,
* alter traceability rules.

### Protocol Meaning Must Match Schema Meaning

If protocol docs say one thing and schemas encode another, that is a defect.
Do not ignore it.

### Resolve Drift Explicitly

When protocol and schema disagree, fix the disagreement explicitly and update whichever side is intended to be authoritative.

---

## Template Rules

### Templates Are Authoring Contracts

Templates are not just stylistic examples.
They define how future human/agent-authored documents should be structured.

### Keep Templates Semantically Stable

Do not casually reorder or remove important sections if doing so would weaken clarity or traceability.

### Templates Must Remain Compatible With Protocol and Schema

A template should not encourage fields or semantics that schemas cannot represent.

### Do Not Over-Simplify Templates

Reducing a template to a minimal note-style format may destroy later workflow usefulness.

---

## Example Artifact Rules

### Examples Exist to Validate the Workflow

Files in `docs/examples/` are repository fixtures.

### Do Not Treat Examples as Production Specs

An example Approved Spec is not automatically the live production approved spec.

### Keep Examples Internally Coherent

Related example artifacts should remain chain-consistent:

* brief references make sense,
* proposal references brief,
* review references proposal,
* approved spec references prior artifacts.

### Update Examples Carefully

If protocol meaning changes and examples must evolve, do so deliberately and keep the chain coherent.

---

## Workflow Artifact Rules

### Workflow Artifact Directories Matter

Actual workflow artifacts should be stored in the correct canonical directories.

Do not casually place a real `Approved Spec` in `docs/examples/` or a fake review in `docs/proposals/`.

### Artifact Chains Must Be Traceable

Downstream artifacts should reference upstream artifacts appropriately.

### Keep Role Intent Clear

If a file claims to be an `Acceptance Report`, it must read like one and preserve its acceptance semantics.

### No Fake Finality

Do not mark documents as approved/accepted casually if they are only drafts or placeholders.

---

## Safe Default Work in This Subtree

Without higher-level explicit approval, safer kinds of work here include:

* improving wording clarity without changing semantics,
* fixing metadata omissions,
* tightening traceability links,
* aligning templates with existing schema meaning,
* adding missing template/example files,
* clarifying architecture record wording where meaning is preserved,
* updating README/project-phase metadata,
* improving documentation consistency.

---

## Sensitive Work in This Subtree

Treat the following as sensitive and higher review risk:

* changing protocol semantics,
* changing stage machine semantics,
* changing artifact lifecycle meanings,
* changing supersession/versioning rules,
* changing accepted architecture records,
* changing example chain semantics,
* changing required template structure,
* changing current-phase or next-step repository status messaging in misleading ways.

---

## Default Forbidden Work in This Subtree

Without explicit approval, do **not**:

* rewrite accepted architecture records to erase history,
* redefine workflow semantics casually,
* downgrade metadata discipline,
* collapse templates into vague prose,
* treat examples as real production authority,
* create documents that imply broader automation authority than approved,
* mark drafts as approved without basis,
* change documentation in ways that bypass schema/protocol discipline.

---

## Review Guidance for Documentation Changes

When reviewing changes under this subtree, prioritize the following questions:

### 1. Did the change preserve meaning?

Check whether protocol, architecture, or artifact semantics changed.

### 2. Did the change preserve traceability?

Check whether artifact relationships and metadata remain explicit.

### 3. Did the change preserve auditability?

Check whether history, scope boundaries, and status remain understandable.

### 4. Did the change preserve alignment with schema?

Check whether docs still match machine-readable model assumptions.

### 5. Did the change preserve template usefulness?

Check whether future human/agent authors could still produce valid artifacts from the templates.

### 6. Did the change accidentally expand authority?

Check whether wording now implies permissions or workflow transitions that were not previously accepted.

### 7. Did the change keep examples in their proper role?

Check whether examples remain examples and not accidental source-of-truth production documents.

---

## Output Contract for Documentation Work

For any meaningful documentation modification or review, include all of the following:

### Summary

What changed in the docs subtree.

### Files Changed

Exact documentation files touched.

### Risks Introduced

Any semantic, traceability, authority, or schema-alignment risk introduced.

### Intentionally Not Changed

What important documentation areas were left untouched.

### Manual Verification Steps

How a human should verify the result.

For example, verification may include:

* inspect metadata completeness,
* compare docs against schema,
* check example chain coherence,
* confirm current phase metadata is accurate,
* confirm no accepted architecture meaning was altered unintentionally.

---

## Manual Verification Expectations

When documentation behavior or policy meaning is affected, expected manual verification should usually include relevant checks such as:

* read protocol docs for semantic consistency,
* compare templates to expected schema fields,
* inspect example artifact chain for coherence,
* inspect architecture records for preserved historical meaning,
* confirm README phase metadata matches repository reality,
* confirm actual workflow docs still live in the right directories.

Do not claim documentation correctness without corresponding checks.

---

## Human Approval Triggers in This Subtree

Stop and require explicit human approval if the work would affect:

* workflow stage semantics,
* artifact lifecycle meaning,
* architecture record meaning,
* acceptance/approval meaning,
* branch or automation authority implied by docs,
* versioning/supersession policy,
* example chain semantics in ways that affect validation assumptions.

If in doubt, escalate rather than improvising.

---

## What This Subtree Is Not

Do not treat `docs/` as:

* an informal notes folder,
* a place to patch over design confusion with wording,
* a place to rewrite history,
* a place to smuggle in policy changes,
* a place where examples automatically become official truth.

It is a policy-bearing, history-bearing, workflow-bearing subtree inside a governed automation repository.

---

## Practical Default Operating Mode for This Subtree

Unless the task explicitly authorizes more:

* inspect first,
* preserve semantic meaning,
* preserve metadata,
* preserve traceability,
* preserve history,
* align docs with schema and protocol,
* avoid implying new authority,
* document any uncertainty clearly.

If uncertain whether a wording change is “editorial” or “semantic”, treat it as semantic.

---

## Conflict Resolution Rule

If there is conflict between:

* cleaner wording,
* shorter prose,
* a convenience simplification,
* a prompt asking for easier docs,
* or a desire to “make this read better”,

and:

* protocol meaning,
* architecture history,
* artifact traceability,
* schema alignment,
* repository governance,

then the protected documentation baseline wins.

---

## Final Operating Instruction

Inside this subtree, meaning comes before style.

Preserve history.

Preserve traceability.

Preserve protocol alignment.

Do not casually change workflow authority through wording.

When in doubt, keep the documentation explicit and auditable.