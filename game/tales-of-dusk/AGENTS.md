# AGENTS.md

## Scope

This file governs work inside the Godot runtime project subtree:

```text
game/tales-of-dusk/
```

It refines the repository-root `AGENTS.md` with **Godot-specific runtime, scene, script, input, and project-structure rules**.

If any instruction conflicts with the repository root `AGENTS.md`, the stricter rule wins.

If any instruction conflicts with accepted architecture records, protocol documents, or protected runtime baselines, those repository governance documents win.

---

## Mission of This Subtree

This subtree contains the runtime Godot 4 project for Tales of Dusk.

The goal of work in this subtree is **not** unrestricted gameplay invention.
The goal is to evolve the runtime project in a controlled way, consistent with:

* accepted repository phase boundaries,
* accepted runtime invariants,
* approved scope/specification,
* bounded task constraints,
* later QA and acceptance review.

All work in this subtree must assume:

* this runtime is part of a governed automation workflow,
* runtime changes are subject to workflow discipline,
* scene/script changes are high-impact compared with documentation-only edits.

---

## Current Accepted Runtime Baseline

The following runtime assumptions are currently protected.

### Project Root

Canonical Godot project root:

```text
game/tales-of-dusk/
```

### Main Scene

Canonical main scene path:

```text
res://scenes/boot/boot.tscn
```

### Accepted Scene Flow

Current accepted minimal scene flow:

```text
Boot -> Title -> Chapter Map -> Room Test
```

### Accepted Required Autoloads

The currently accepted required Autoloads are:

* `EventBus`
* `GameSession`
* `SaveSystem`
* `SceneRouter`

These names are part of the current protected runtime baseline.

### Accepted Room Phase Order

The accepted canonical room phase order is:

```text
Preview -> Deploy -> Combat -> Result
```

This order is currently treated as a protected runtime invariant.

### Accepted Runtime Nature

The current runtime is still a controlled skeleton/baseline.
It is not yet a complete gameplay implementation.

Do not assume runtime incompleteness gives permission to redesign protected flow casually.

---

## Source-of-Truth Files for This Subtree

Before modifying runtime files, consult at minimum:

### Architecture

* `docs/architecture/001_phase2_godot_skeleton_accepted.md`
* `docs/architecture/003_phase4_minimal_orchestrator_accepted.md`
* `docs/architecture/004_phase5_codex_entry_scope.md`

### Workflow / Protocol

* `docs/protocols/automation_protocol.md`
* `docs/protocols/workflow_stage_machine.md`

### Runtime-Aware Shared State

* `automation/langgraph/schemas/workflow_state.py`

### Root Governance

* repository root `AGENTS.md`

If a runtime edit would contradict these documents, stop and surface the conflict.

---

## Runtime Operating Principle

This runtime subtree must be evolved under a “preserve baseline first” principle.

That means:

1. preserve accepted scene flow,
2. preserve accepted Autoload identities,
3. preserve accepted room phase semantics,
4. preserve clear scene/script ownership,
5. prefer bounded additions over broad refactors,
6. avoid implicit architecture drift.

Do not optimize for elegance at the cost of repository control.

---

## Hard Runtime Rules

### Rule 1: Do not change the main scene path casually

Do not change:

```text
res://scenes/boot/boot.tscn
```

without explicit upstream approval.

### Rule 2: Do not silently change scene flow

Do not silently change:

```text
Boot -> Title -> Chapter Map -> Room Test
```

Any structural routing change is high-risk and should be treated as architecture-sensitive.

### Rule 3: Do not rename required Autoloads

Do not rename, remove, or repurpose:

* `EventBus`
* `GameSession`
* `SaveSystem`
* `SceneRouter`

without explicit approval.

### Rule 4: Do not add new Autoloads casually

Adding a new Autoload is not a minor convenience.
It changes global runtime boundaries and should be treated as sensitive.

### Rule 5: Do not change room phase order casually

The canonical phase order:

```text
Preview -> Deploy -> Combat -> Result
```

must not be silently rewritten or reinterpreted.

### Rule 6: Do not hide runtime refactors inside “small fixes”

A small bugfix must remain a small bugfix.
Do not use it to rewire scene ownership, routing, global state, or architecture.

### Rule 7: Prefer narrow scene/script changes

Keep runtime changes local and reviewable.

### Rule 8: Do not mix speculative gameplay design into unrelated runtime tasks

This subtree is not permission to invent new mechanics unless the task explicitly includes them.

---

## Engine and Language Rules

### Godot Version Assumption

This subtree is for Godot 4.

Do not introduce assumptions from Unity, Unreal, or Godot 3-era project structure unless explicitly justified.

### Preferred Runtime Language

Prefer:

* **GDScript**

unless there is explicit approved reason to introduce or expand another language.

Do not introduce C# or mixed-language runtime architecture casually.

### Script Style Priority

Prefer:

* clarity,
* boundedness,
* explicit node paths,
* stable ownership,
* minimal hidden global behavior.

Do not optimize for abstraction if it harms runtime traceability.

---

## Scene Rules

### Scene Ownership

Each major scene should have a clearly identifiable root node and root script ownership.

Do not spread top-level scene behavior across arbitrary child nodes without strong reason.

### Script Attachment Rule

When a scene has a primary controller script, that script should normally be attached to the **scene root node**, not to an arbitrary child, unless the task explicitly justifies otherwise.

This is especially important for:

* `boot.tscn`
* `title.tscn`
* `chapter_map.tscn`
* `room_test.tscn`

### No Hidden Child-Script Control

Do not accidentally attach controller scripts to visual-only child nodes such as:

* `ColorRect`
* `CenterContainer`
* `HBoxContainer`
* placeholder labels/buttons

unless that node is explicitly intended to own that behavior.

### Preserve Scene Path Stability

Do not casually move accepted baseline scenes to different paths.

Accepted scene locations currently include:

* `res://scenes/boot/boot.tscn`
* `res://scenes/title/title.tscn`
* `res://scenes/chapter_map/chapter_map.tscn`
* `res://scenes/rooms/room_test.tscn`

---

## Script Rules

### Root Script Ownership

Primary behavior for a scene belongs on the scene’s root control node or root runtime node unless explicitly designed otherwise.

### Do Not Break Existing Path Contracts

If a script depends on known node paths, do not rename or restructure nodes casually without updating all affected references and verifying behavior.

### Prefer Explicit Node Paths

Be explicit and predictable in node access.
Do not replace simple, clear paths with unnecessary indirection without real benefit.

### No Broad Utility Grab-Bag Files

Do not create vague “helper” or “manager” scripts that accumulate unrelated runtime responsibilities.

### No Silent Responsibility Expansion

Do not turn a small UI script into a scene router, save manager, and runtime coordinator at once.

---

## Autoload Rules

### Accepted Autoload Roles

The current baseline assumes the following rough roles:

* `EventBus`: global signal/event surface
* `GameSession`: runtime/session state
* `SaveSystem`: current save/load stub and save-facing runtime access
* `SceneRouter`: scene transition authority

### Do Not Collapse or Merge Roles Casually

Do not merge these into one monolithic global script.

### Do Not Expand Roles Without Approval

Do not casually turn `SceneRouter` into:

* gameplay controller,
* chapter progression authority,
* save migration service,
* UI state manager.

Do not casually turn `GameSession` into:

* universal registry of everything,
* content definition database,
* hidden god object.

### Autoload Additions Are Sensitive

Any new Autoload should be treated as:

* architecture-sensitive,
* review-worthy,
* rarely justified.

---

## Input Rules

### InputMap Is the Source of Truth

Input actions should be maintained through Godot’s `InputMap` / project settings conventions, not scattered hardcoded key assumptions.

### Accepted Current Inputs

The current accepted baseline input actions include:

* `tod_confirm`
* `tod_back`
* `tod_debug_next_state`

Do not rename or remove them casually.

### Adding Inputs

New inputs may be added only when clearly justified by scope.
Do not add speculative future controls just because they “might be useful later”.

---

## UI Rules

### Current UI Is Placeholder but Structured

The current baseline UI is functional placeholder UI.
That does not authorize arbitrary restructuring.

### Prefer Clear Hierarchy

For `Control`-based scenes, keep container hierarchy understandable and stable.

### Do Not Mix Scene Control and Decorative UI Arbitrarily

Decorative nodes should not silently become workflow-control nodes unless explicitly intended.

### Keep Navigation Predictable

Do not casually change button semantics or back-navigation behavior in accepted baseline scenes.

---

## Data and Resource Rules

### Do Not Hardcode Future Gameplay Data Into Random Scripts

If a task begins introducing real runtime data structures, prefer clear ownership and later data-driven design rather than scattering values across multiple runtime scripts.

### Respect Current Phase Boundaries

This subtree is not yet the phase for broad production data authoring.
Do not preemptively create large content datasets or balancing systems unless explicitly requested by upstream approved scope.

### Save-Sensitive Data Is High-Risk

Any change that affects save-facing runtime meaning is sensitive and should be surfaced explicitly.

---

## Safe Default Work in This Subtree

Without higher-level explicit approval, safer kinds of work here include:

* fixing incorrect script attachment,
* fixing broken node-path references,
* stabilizing accepted scene flow,
* bounded UI placeholder fixes,
* bounded Room Test state-shell fixes,
* preserving or clarifying runtime invariants,
* adding tests or validation notes related to accepted baseline behavior,
* documenting current runtime assumptions.

---

## Sensitive Work in This Subtree

Treat the following as sensitive and higher review risk:

* changing scene ownership boundaries,
* changing scene file paths,
* changing root node types,
* changing accepted navigation flow,
* adding/removing Autoloads,
* changing `SceneRouter` responsibilities,
* changing `GameSession` semantics,
* changing room phase order,
* changing save-facing behavior,
* changing accepted input action names.

These usually require upstream justification.

---

## Default Forbidden Work in This Subtree

Without explicit approval, do **not**:

* rewrite the runtime from scratch,
* redesign the game loop,
* bypass the accepted scene flow,
* add complex gameplay systems opportunistically,
* convert the project into a different language stack,
* reorganize the entire project tree,
* introduce hidden runtime state coupling,
* add broad architecture frameworks “for future-proofing”.

---

## Review Guidance for Runtime Changes

When reviewing changes under this subtree, prioritize the following questions:

### 1. Did the change preserve the accepted runtime baseline?

Check:

* scene flow,
* main scene path,
* Autoload set,
* room phase order.

### 2. Did the change stay within stated scope?

Was the change actually bounded, or did it smuggle in architecture drift?

### 3. Are script attachments correct?

Controller scripts should be attached to the intended owner nodes.

### 4. Are node paths still valid?

Any renamed/restructured nodes must be reflected in code.

### 5. Did the change create a new global coupling?

Watch for hidden dependencies between scenes, autoloads, and UI.

### 6. Did the change alter save/runtime meaning?

If yes, escalate review level.

### 7. Did the change preserve placeholder stability?

Even placeholder runtime shells are baselines and should remain predictable.

---

## Output Contract for Runtime Work

For any meaningful runtime modification or review, include all of the following:

### Summary

What changed in the runtime subtree.

### Files Changed

Exact runtime files touched.

### Risks Introduced

Any runtime, routing, state, save, or scene-coupling risk introduced.

### Intentionally Not Changed

What important runtime areas were left untouched.

### Manual Verification Steps

How a human should verify the runtime still behaves correctly.

For example, verification may include:

* run project,
* confirm Boot reaches Title,
* confirm Title reaches Chapter Map,
* confirm Chapter Map reaches Room Test,
* confirm Room Test can advance phase order,
* confirm back navigation works.

---

## Manual Verification Expectations

When runtime behavior is affected, expected manual verification should usually include relevant checks such as:

* project opens successfully in Godot,
* no broken script attachments,
* accepted Autoloads still load,
* accepted input actions still exist,
* accepted scene flow still works,
* Room Test still supports the accepted phase shell,
* no new obvious runtime errors are introduced.

Do not claim runtime stability without corresponding checks.

---

## Human Approval Triggers in This Subtree

Stop and require explicit human approval if the work would affect:

* main scene path,
* accepted scene flow,
* Autoload set,
* room phase order,
* save semantics,
* root project structure,
* language choice,
* broad gameplay architecture,
* CI-facing runtime assumptions.

If in doubt, escalate rather than improvising.

---

## What This Subtree Is Not

Do not treat `game/tales-of-dusk/` as:

* a casual sandbox,
* a dumping ground for future systems,
* a place to “just try a better architecture”,
* a free refactor target,
* an excuse to ignore repository-wide workflow discipline.

It is a protected runtime subtree inside a governed automation repository.

---

## Practical Default Operating Mode for This Subtree

Unless the task explicitly authorizes more:

* inspect first,
* preserve accepted scene flow,
* preserve accepted Autoloads,
* keep edits narrow,
* avoid hidden global coupling,
* favor root-owned scene control,
* document runtime-sensitive risks clearly.

If uncertain whether a change is “small” or “architecture-sensitive”, treat it as architecture-sensitive.

---

## Conflict Resolution Rule

If there is conflict between:

* a convenience runtime refactor,
* a speculative gameplay improvement,
* a prompt asking for broad changes,
* or a local simplification idea,

and:

* accepted runtime baseline,
* repository root `AGENTS.md`,
* architecture records,
* workflow protocol rules,

then the protected baseline wins.

---

## Final Operating Instruction

Inside this subtree, stability and clarity come first.

Preserve the accepted runtime baseline.

Do not casually expand authority.

Do not confuse placeholder status with permission to redesign.

When in doubt, keep the runtime bounded and surface the issue explicitly.