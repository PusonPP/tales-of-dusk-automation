# Codex Repository Audit Prompt

You are auditing the repository **Tales of Dusk Automation**.

This repository is a governed automation workflow repository, not a generic codebase.

It contains:
- a Godot 4 runtime project,
- a LangGraph-based workflow orchestration layer,
- a protocol and artifact documentation system,
- a Codex entry layer,
- GitHub Actions workflow assets,
- repository governance rules via `AGENTS.md`.

Your task is to perform a **deep repository audit** and produce a structured audit report.

## Operating Mode

You are in **audit mode only**.

You must:
- inspect repository structure,
- inspect workflow/governance consistency,
- inspect risk surfaces,
- inspect phase alignment,
- inspect protected baseline integrity,
- inspect automation readiness,
- identify gaps, contradictions, and weaknesses.

You must **not**:
- modify files,
- generate implementation diffs,
- rewrite repository structure,
- invent accepted baselines that are not documented,
- assume successful runtime execution unless explicit evidence exists,
- broaden scope beyond audit and recommendation.

If repository documents, architecture records, protocol documents, schemas, or `AGENTS.md` files exist, they are authoritative constraints and must be treated as such.

---

## Audit Goals

Your audit must answer the following repository-level questions.

### 1. What does this repository currently contain?
Determine the real current state of the repository, including:
- runtime layer,
- protocol/documentation layer,
- schema/state layer,
- LangGraph orchestration layer,
- Codex entry layer,
- GitHub Actions layer,
- governance/rule layer.

### 2. What phase is the repository actually in?
Determine:
- claimed current phase,
- apparent actual phase,
- whether those are aligned,
- whether “next step” messaging is accurate.

### 3. Are accepted baselines intact?
Inspect whether previously accepted baselines appear to remain intact:
- Godot runtime baseline,
- protocol/state baseline,
- minimal orchestration baseline,
- bounded Codex entry assumptions.

### 4. Are there hidden inconsistencies?
Look for mismatches such as:
- README vs actual repo contents,
- architecture records vs actual repo contents,
- protocol docs vs schema design,
- templates vs schema expectations,
- examples vs protocol meaning,
- graph/state code vs stage-machine semantics,
- prompt files vs AGENTS rules,
- workflow YAML vs intended Codex safety posture.

### 5. Is the repository ready for the next phase?
Determine whether the repository appears ready to proceed to the next planned bounded phase, or whether it still has unresolved blockers.

### 6. What are the highest-risk areas?
Identify the areas most likely to cause future failures, such as:
- architecture drift,
- unclear Codex authority,
- stale metadata,
- drift between docs and code,
- branch-safety ambiguity,
- untested assumptions,
- protected baseline erosion.

---

## Audit Method

Use the following audit method.

### Step 1: Repository Mapping
Map the major repository areas:
- `game/`
- `automation/`
- `docs/`
- `.github/`

Determine what role each currently plays.

### Step 2: Governance Discovery
Read and apply:
- root `AGENTS.md`
- subtree `AGENTS.md` files if present
- architecture records
- protocol documents

Determine what rules the repository claims to follow.

### Step 3: Baseline Integrity Check
Check whether actual repository structure and files appear consistent with accepted baselines.

### Step 4: Workflow Integrity Check
Check whether workflow artifacts, schemas, state, graphs, prompts, and workflows appear consistent with each other.

### Step 5: Safety and Authority Check
Check whether Codex entry, branch assumptions, and remote workflow assets appear bounded and safe relative to repository rules.

### Step 6: Next-Phase Readiness Check
Decide whether the repository appears:
- ready,
- partially ready,
- or not ready

for the next bounded workflow phase.

---

## Required Audit Areas

You must explicitly cover all of the following areas.

### A. Runtime Baseline Audit
Check for evidence of:
- canonical Godot project root,
- main scene path,
- accepted scene layout,
- accepted runtime script areas,
- required Autoloads,
- accepted room phase order.

Important:
Do not claim successful runtime execution unless execution evidence is explicitly available.

### B. Protocol and Artifact Audit
Check for:
- protocol docs,
- artifact templates,
- example artifact chains,
- workflow artifact directories,
- metadata discipline,
- apparent traceability expectations.

### C. Schema and State Audit
Check for:
- canonical enums,
- common schema layer,
- item schema layer,
- artifact-specific schemas,
- `WorkflowState`,
- tests or validation around them.

### D. Orchestration Audit
Check for:
- minimal graph builder,
- node module,
- local runner,
- graph tests,
- stage progression consistency,
- blocker/route logic,
- fit with stage-machine semantics.

### E. Codex Entry Audit
Check for:
- root and subtree `AGENTS.md`,
- Codex prompt assets,
- remote Codex workflow YAML files,
- evidence of local/remote entry strategy,
- bounded authority posture.

### F. Metadata and Phase Audit
Check whether:
- README phase is accurate,
- next-step messaging is accurate,
- architecture records match actual repository maturity.

---

## Risk Classification Rules

Classify findings into three levels:

### Blocker
A blocker is something that should prevent the repository from being considered ready for the next bounded phase.

Examples:
- missing required baseline files,
- missing protected rule layer,
- protocol/schema contradiction that breaks workflow assumptions,
- graph/state mismatch that invalidates orchestration meaning,
- unsafe Codex entry posture inconsistent with repository policy.

### Non-Blocking Issue
A non-blocking issue is something real and important, but not severe enough to stop phase progression immediately.

Examples:
- stale metadata,
- under-tested artifact-specific schemas,
- incomplete prompt coverage,
- weak cleanup of unused files,
- output formatting roughness.

### Low-Risk Cleanup
Low-risk cleanup includes polish and hygiene issues that should be fixed eventually but are not current governance threats.

Examples:
- inconsistent wording,
- missing minor docs sync,
- redundant repository artifacts,
- non-critical formatting inconsistencies.

---

## Output Format

Return your answer in the following exact structure.

# Repository Audit Report

## 1. Repository Identity
- Repository name: <value>
- Primary purpose: <value>
- Practical current shape: <short summary>

## 2. Current Phase Audit
- Claimed current phase: <value>
- Apparent actual phase: <value>
- Alignment: <aligned / partially stale / inconsistent>
- Notes: <brief explanation>

## 3. Repository Area Map

### 3.1 Runtime Layer
- Status: <present / partial / missing>
- Notes:
  - <finding>
  - <finding>

### 3.2 Protocol / Docs Layer
- Status: <present / partial / missing>
- Notes:
  - <finding>
  - <finding>

### 3.3 Schema / State Layer
- Status: <present / partial / missing>
- Notes:
  - <finding>
  - <finding>

### 3.4 Orchestration Layer
- Status: <present / partial / missing>
- Notes:
  - <finding>
  - <finding>

### 3.5 Codex Entry Layer
- Status: <present / partial / missing>
- Notes:
  - <finding>
  - <finding>

### 3.6 Remote Workflow Layer
- Status: <present / partial / missing>
- Notes:
  - <finding>
  - <finding>

## 4. Baseline Integrity Audit

### 4.1 Runtime Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

### 4.2 Protocol and State Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

### 4.3 Minimal Orchestrator Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

### 4.4 Codex Entry Baseline
- Status: <intact / partially at risk / inconsistent>
- Findings:
  - <finding>
  - <finding>

## 5. Drift and Consistency Findings
- <finding>
- <finding>
- <finding>

## 6. Blockers
- <blocker or "None found">

## 7. Non-Blocking Issues
- <issue>
- <issue>

## 8. Low-Risk Cleanup Items
- <cleanup item>
- <cleanup item>

## 9. Next-Phase Readiness
- Status: <ready / partially ready / not ready>
- Recommended next bounded phase: <value>
- Rationale: <brief explanation>

## 10. Highest-Risk Areas
- <risk area>
- <risk area>
- <risk area>

## 11. Recommended Immediate Actions
- <action 1>
- <action 2>
- <action 3>

## 12. Confidence and Limits
- Confidence level: <high / medium / low>
- Limits:
  - <what was inferred rather than verified>
  - <what would require runtime execution or human confirmation>

---

## Audit Discipline

Be explicit about uncertainty.

Do not fabricate successful execution.

Do not recommend broad redesign if a bounded next action is more appropriate.

Do not let repository familiarity blur governance boundaries.

Prefer:
- baseline preservation,
- protocol awareness,
- phase accuracy,
- bounded next steps,
- clear blocker identification.

This repository values:
- control,
- traceability,
- safety,
- bounded evolution,
- workflow discipline

over convenience or speed.