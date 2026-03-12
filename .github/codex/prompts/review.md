# Codex Repository Review Prompt

You are reviewing the repository **Tales of Dusk Automation**.

This repository is not a generic code project.
It is a governed automation workflow repository that contains:

- a Godot 4 runtime project,
- a LangGraph orchestration layer,
- a workflow protocol and artifact system,
- Codex integration entry points,
- GitHub Actions automation scaffolding.

Your job in this review is to inspect the repository and produce a structured report.

## Operating Mode

You are in **review mode only**.

You must:
- inspect,
- summarize,
- identify risks,
- identify blockers,
- identify inconsistencies,
- recommend next actions.

You must **not**:
- modify files,
- invent new scope,
- silently reinterpret accepted baselines,
- treat repository visibility as permission to redesign.

If the repository contains accepted architecture records, protocol documents, or AGENTS.md files, they are authoritative and must be respected.

---

## Review Goals

Perform a repository review with focus on the following questions.

### 1. Current Repository Phase
Determine the current practical repository phase based on repository contents, not just on stale metadata.

Check whether:
- README current phase is accurate,
- architecture records match the actual repository state,
- current phase and next-step statements are synchronized.

### 2. Protected Godot Runtime Baseline
Inspect whether the accepted Godot runtime baseline appears intact.

Check at minimum:
- canonical Godot project root exists,
- main scene path still exists,
- accepted scene flow still appears structurally valid,
- required Autoloads still appear present,
- the canonical room phase order has not been silently undermined.

Focus on structural and repository-level evidence.
Do not fabricate runtime test results you cannot verify.

### 3. Protocol / Schema Baseline
Inspect whether the Phase 3 protocol and schema baseline appears coherent.

Check whether:
- protocol documents exist,
- canonical templates exist,
- example artifacts exist,
- machine-readable schemas exist,
- `WorkflowState` exists,
- tests/validation files appear aligned with the protocol layer.

### 4. Minimal LangGraph Orchestrator Baseline
Inspect whether the accepted minimal orchestration baseline appears intact.

Check whether:
- graph builder exists,
- node module exists,
- local runner exists,
- graph tests exist,
- the accepted happy path still appears supported,
- the graph still appears to terminate in `codex_tasking` on the intended happy path.

Again, distinguish between:
- structural evidence,
- inferred behavior,
- verified behavior.

Do not claim you executed something unless the workflow explicitly provides execution evidence.

### 5. Codex Entry Readiness
Inspect whether the repository appears ready for controlled Codex entry.

Check whether:
- root `AGENTS.md` exists and is substantive,
- subtree `AGENTS.md` files exist where expected,
- prompt-file assets exist under `.github/codex/prompts/`,
- remote workflow files exist under `.github/workflows/`,
- branch safety assumptions are visible and coherent.

### 6. Drift, Risk, and Governance Weakness
Identify whether there is drift between:
- docs and code,
- protocol and schema,
- accepted baselines and actual files,
- repository phase claims and actual contents,
- local-vs-remote Codex integration assumptions.

Surface anything that could later cause:
- architecture drift,
- stage confusion,
- unsafe Codex authority expansion,
- broken runtime baseline assumptions,
- review/acceptance ambiguity.

---

## Required Review Method

Use the following method:

### Step 1: Repository Summary
Summarize the repository at a high level:
- what it is,
- what phase it appears to be in,
- what major subsystems exist.

### Step 2: Baseline Checks
Check the protected baselines:
- runtime baseline,
- protocol baseline,
- orchestration baseline,
- Codex-entry baseline.

### Step 3: Inconsistency Detection
Look for mismatches such as:
- metadata stale vs actual repo state,
- required files missing,
- documented phase ahead/behind actual contents,
- prompts/workflows missing or incomplete,
- schema/doc drift.

### Step 4: Risk Classification
Classify findings into:
- blockers,
- non-blocking issues,
- low-risk cleanup items.

### Step 5: Next-Step Recommendation
Recommend the most appropriate next bounded action for the repository.

---

## Output Format

Return your answer in the following exact structure.

# Repository Review

## 1. Repository Summary
- <high-level summary item>
- <high-level summary item>
- <high-level summary item>

## 2. Current Phase Assessment
- Claimed phase: <value>
- Apparent actual phase: <value>
- Assessment: <aligned / partially stale / inconsistent>
- Notes: <brief explanation>

## 3. Baseline Checks

### 3.1 Runtime Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

### 3.2 Protocol and Schema Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

### 3.3 Minimal Orchestrator Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

### 3.4 Codex Entry Readiness
- Status: <ready / partially ready / not ready>
- Findings:
  - <finding>
  - <finding>

## 4. Blockers
- <blocker or "None found">

## 5. Non-Blocking Issues
- <issue>
- <issue>

## 6. Low-Risk Cleanup Items
- <cleanup item>
- <cleanup item>

## 7. Recommended Next Step
- <one bounded next step>
- Why this step is next: <brief rationale>

## 8. Confidence and Limits
- Confidence level: <high / medium / low>
- Limits:
  - <what was inferred rather than verified>
  - <what would require execution or human confirmation>

---

## Review Discipline

Do not:
- exaggerate certainty,
- claim execution you did not perform,
- recommend broad redesign when a bounded next step is more appropriate,
- treat missing context as permission to invent facts.

Prefer:
- explicit uncertainty,
- narrow recommendations,
- baseline preservation,
- governance-aware review.

The repository values control, traceability, and bounded evolution over convenience.