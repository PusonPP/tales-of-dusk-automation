# 010 Phase 8 Single Room Loop Scope

## Purpose

Record the scope boundary for Phase 8 of the Tales of Dusk automated development workflow repository.

Phase 8 exists to establish the first real runtime gameplay-facing loop built on top of the accepted Godot runtime skeleton and the accepted Godot data-definition layer.

Its purpose is to connect the existing placeholder room scene to real `ChapterDef`, `RoomDef`, and `UnitDef` content so that the project can execute one bounded room cycle from entry to result.

Phase 8 does **not** attempt to implement the full game.  
It introduces a single-room minimal loop only.

This record prevents another common failure mode: trying to build full combat, progression, and multi-room runtime systems before the project has successfully completed one controlled, data-driven room loop.

---

## Phase 8 Mission

The mission of Phase 8 is:

- connect `ChapterDef` and `RoomDef` to the current runtime flow,
- replace the current hardcoded placeholder room entry with data-backed room entry,
- upgrade the current `room_test` runtime shell into a real single-room loop controller,
- support a bounded `Preview -> Deploy -> Combat -> Result` flow using the accepted room-state structure,
- support a minimal deploy choice using existing `UnitDef` resources,
- support a deterministic and intentionally simplified combat resolution,
- write the room result back into `GameSession`,
- preserve the accepted runtime skeleton while proving the first real room loop works.

Phase 8 is a **single-room runtime loop phase**, not a full gameplay systems phase.

---

## Why Phase 8 Exists

The repository already has:

- a Phase 1 repository foundation,
- a Phase 2 accepted Godot runtime skeleton,
- a Phase 3 accepted workflow protocol/state baseline,
- a Phase 4 accepted minimal LangGraph orchestrator,
- a Phase 5 accepted bounded Codex entry layer,
- a Phase 6 accepted minimal CI baseline,
- a Phase 7 accepted Godot data-definition layer.

However, the runtime still lacks a real gameplay-facing loop that actually consumes the new data layer.

Without Phase 8:

- `ChapterDef` remains mostly authored but not consumed,
- `RoomDef` remains mostly descriptive,
- `UnitDef` remains mostly static data,
- `room_test` remains a placeholder state-cycle scene,
- the project still cannot prove that one real room can be entered, resolved, and completed in a data-driven way.

Phase 8 exists to solve that by delivering the first accepted single-room runtime loop.

---

## Accepted Scope for Phase 8

Phase 8 is explicitly in scope for the following work.

### 1. Data-Backed Room Entry

Phase 8 defines the first runtime flow where the game enters a room based on accepted chapter/room data rather than using a placeholder hardcoded room identity only.

This includes:

- loading a chapter definition,
- identifying at least one room from that chapter,
- recording the selected room in `GameSession`,
- entering the accepted room runtime scene with real room data available.

---

### 2. Minimal Chapter Map to Room Handoff

Phase 8 upgrades the existing Chapter Map handoff so that it no longer behaves as a purely hardcoded transition.

This includes:

- using accepted chapter data,
- setting starting supply using chapter data,
- selecting a first room from chapter data,
- handing the current room context to `GameSession`,
- routing into the accepted room scene.

This handoff must remain bounded and must not turn Chapter Map into a full progression system yet.

---

### 3. Single-Room Preview Phase

Phase 8 upgrades the Preview phase of the room loop to use real `RoomDef` content.

This includes displaying data such as:

- room display name,
- room preview text,
- room rewards,
- room wave count or equivalent simple summary,
- current run supply context where relevant.

This phase should prove that room data is now being consumed by the runtime.

---

### 4. Minimal Deploy Phase

Phase 8 defines a small deploy-selection interaction using the accepted `UnitDef` data layer.

This includes:

- presenting a small allowed unit selection set,
- using real unit definitions,
- showing or using supply cost,
- storing selected units in a bounded runtime form,
- keeping the deploy phase small and deterministic.

This phase is not intended to be a spatial placement system.

---

### 5. Deterministic Combat Resolution

Phase 8 defines a minimal and deterministic room-resolution method that can stand in for real combat.

This includes:

- a bounded resolution rule,
- use of currently available room/wave/unit information where appropriate,
- a clear victory/failure outcome,
- no real-time battle simulation,
- no AI/pathfinding-based combat.

The goal is to prove the room loop, not to build the final combat model.

---

### 6. Result Phase and Session Writeback

Phase 8 defines the first accepted result writeback from room resolution into `GameSession`.

This includes:

- storing whether the room was cleared,
- applying room rewards on success where appropriate,
- updating supply and/or core shard values where appropriate,
- exposing a result summary,
- allowing bounded continuation such as returning to the Chapter Map.

This is the first accepted room-result integration step.

---

### 7. Minimal UI Additions for the Loop

Phase 8 may add only the UI necessary to support the single-room loop.

This includes room-scene UI such as:

- preview labels,
- deploy summary labels,
- selection buttons,
- resolve button,
- result summary labels,
- return/retry controls.

UI additions must remain bounded and functional.

---

### 8. Smoke/CI Extension Where Necessary

If the new single-room loop introduces new protected files or new phase metadata expectations, Phase 8 may extend the repository smoke/CI baseline accordingly.

This should remain structural rather than engine-runtime-driven.

---

## Explicitly Out of Scope for Phase 8

The following are **not** part of Phase 8.

### 1. Real-Time Combat System

Phase 8 does **not** include:

- real-time enemy movement,
- attack timing simulation,
- collision-based combat,
- pathfinding,
- targeting systems,
- animation-driven battle logic,
- projectile systems,
- final combat balance.

Combat remains intentionally simplified and deterministic.

---

### 2. Spatial Unit Deployment

Phase 8 does **not** include:

- battlefield placement,
- drag-and-drop unit placement,
- tile-based deployment zones,
- lane logic,
- formation systems,
- deployment validation on map space.

The deploy phase is selection-based only.

---

### 3. Multi-Room Progression

Phase 8 does **not** include:

- moving through all chapter rooms in sequence,
- room graph traversal,
- branching room paths,
- persistent room progression,
- chapter completion loop,
- boss unlock logic.

Only one room loop is required.

---

### 4. Save Integration

Phase 8 does **not** include:

- save schema changes,
- persistent chapter/room progress,
- restoring room state from disk,
- unlock persistence,
- long-term run persistence.

All room-loop state remains runtime/session-level only.

---

### 5. New Autoloads

Phase 8 does **not** introduce new global Autoload singletons.

That means:
- no `CombatSystem` autoload,
- no `RoomManager` autoload,
- no `DataRegistry` autoload,
- no new global runtime service layer.

All integration should remain within current accepted boundaries.

---

### 6. New Room Scene Architecture

Phase 8 does **not** replace the accepted room scene baseline with a different runtime scene architecture.

That means:
- the accepted `room_test.tscn` path remains the current room execution scene,
- Phase 8 should upgrade the accepted room scene rather than bypass it with a parallel system.

---

### 7. Godot CI Runtime Execution

Phase 8 does **not** require:

- Godot executable installation in CI,
- scene execution under CI,
- runtime input playback in CI,
- engine-level automated scene tests.

Phase 8 remains verified through local editor/runtime checks plus the existing minimal structural CI gate.

---

### 8. Remote Codex Activation

Phase 8 does **not** activate remote Codex workflows.

The accepted Phase 5/6 boundary still holds:
- no `OPENAI_API_KEY` activation in GitHub Actions
- no `openai/codex-action@v1` runtime usage
- no billed remote Codex execution

---

## Canonical Deliverables of Phase 8

Phase 8 is considered complete only if the following deliverables exist.

### Runtime Integration Changes
A bounded set of runtime script changes that connect chapter data, room data, and room result writeback into the existing runtime skeleton.

### Room Loop Controller Upgrade
The accepted room scene controller upgraded from a placeholder state rotator into a real single-room loop controller.

### Session Integration Update
A bounded `GameSession` update sufficient to carry current room state and room result information.

### Data Access Update
A bounded `DataCatalog` or equivalent explicit loader update sufficient to support room-loop runtime access.

### UI Adjustments
Minimal room-scene UI additions required to support the loop.

### Architecture Record
This scope record.

---

## Required Constraints During Phase 8

The following constraints apply throughout Phase 8.

### Constraint 1
Phase 8 must preserve the accepted runtime skeleton from Phase 2.

### Constraint 2
Phase 8 must consume the accepted data layer from Phase 7 rather than reinventing content definitions.

### Constraint 3
Phase 8 must not introduce new Autoloads casually.

### Constraint 4
Phase 8 must keep the loop bounded to one room.

### Constraint 5
Phase 8 must keep combat deterministic and simplified.

### Constraint 6
Phase 8 must not silently expand into progression, save, or full combat architecture.

### Constraint 7
Phase 8 must preserve the accepted `Preview -> Deploy -> Combat -> Result` phase order.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established:

- canonical Godot project root,
- canonical main scene path,
- accepted scene flow,
- accepted Autoload set,
- accepted room phase order.

Phase 8 must preserve those baselines.

The room loop introduced here should operate inside the accepted runtime shell, not replace it.

### Relationship to Phase 3

Phase 3 established repository workflow governance.

Phase 8 remains subordinate to those governance rules and must not broaden runtime/system authority implicitly.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 8 does not alter the accepted orchestration baseline directly, but it creates a more concrete gameplay/runtime target for future task-generation and automation work.

### Relationship to Phase 5

Phase 5 established bounded Codex entry.

Phase 8 may be implemented locally under controlled rules, but it does not authorize broader Codex autonomy or remote activation.

### Relationship to Phase 6

Phase 6 established the accepted minimal CI baseline.

Phase 8 should preserve and, where necessary, extend that structural baseline without requiring engine-runtime CI execution.

### Relationship to Phase 7

Phase 7 established the accepted Godot data-definition layer.

Phase 8 is the first phase that must consume that accepted data layer in real runtime behavior.

It therefore depends directly on Phase 7.

---

## Relationship to Later Phases

Later phases may build on the Phase 8 single-room loop by adding:

- multi-room progression
- richer deploy systems
- more sophisticated combat resolution
- wave execution logic
- save integration
- chapter progression UI
- room completion progression
- runtime editor tooling
- engine-level CI/runtime tests

Those later phases should build on the accepted Phase 8 room-loop baseline rather than skipping directly to large-scale runtime redesign.

---

## Accepted Runtime Direction

The accepted runtime direction for Phase 8 is:

- Chapter Map selects a chapter,
- runtime resolves a first room from chapter data,
- `GameSession` records the current room context,
- `room_test` acts as the current room execution scene,
- Preview reads `RoomDef`,
- Deploy reads available `UnitDef` choices,
- Combat resolves deterministically,
- Result writes rewards back to session state,
- user can return to Chapter Map after the room result.

This is the accepted single-room loop direction.

---

## Minimal Accepted Single-Room Loop

The minimal accepted single-room loop for Phase 8 is:

```text
Chapter Map
-> select/start Chapter 01
-> resolve first room from chapter data
-> enter Room Test scene
-> Preview
-> Deploy
-> Combat Resolve
-> Result
-> Back to Chapter Map
```

This loop is intentionally small and explicit.

---

## Minimal Accepted Session State Expansion

The accepted bounded `GameSession` expansion for Phase 8 may include fields such as:

* current room index
* selected unit IDs
* last room victory flag
* last room reward values

This is accepted only insofar as it supports the single-room loop.

This phase does **not** authorize broad session-state redesign.

---

## Minimal Accepted Deploy Direction

The accepted deploy direction is:

* choose from a small predefined set of units,
* consume or validate supply cost,
* store the selection,
* do not spatially place units.

This is sufficient for the single-room loop baseline.

---

## Minimal Accepted Combat Direction

The accepted combat direction is:

* deterministic
* simplified
* bounded
* explicit
* not real-time

It is acceptable for combat resolution to be intentionally crude at this phase as long as it is:

* data-aware,
* reproducible,
* understandable,
* sufficient to advance the room loop.

---

## Minimal Accepted Result Direction

The accepted result direction is:

* compute room success/failure,
* apply room rewards on success where appropriate,
* update current session values,
* expose a result summary,
* allow bounded loop exit back to Chapter Map.

This is sufficient for the first accepted room loop.

---

## What Was Intended to Be Validated by Phase 8

Phase 8 is intended to prove all of the following:

* the accepted data layer is now actually consumed by runtime code,
* the placeholder room scene can become a real room loop controller,
* a real room can be previewed, resolved, and completed,
* the runtime can write room results back into session state,
* the project now has one true gameplay-facing loop rather than only placeholders.

---

## Known Limitations at Acceptance Time

This scope intentionally preserves several limitations.

### Runtime Limitations

* only one bounded room loop is required
* combat remains simplified
* deployment remains non-spatial
* room progression remains minimal
* chapter progression remains incomplete

### Data Limitations

* content coverage remains intentionally small
* only the initial accepted chapter/room/unit definitions are expected to be used
* the room loop does not imply final content scale

### Save/Progression Limitations

* no persistence is required
* no final progression model is required
* no save compatibility work is required

### CI Limitations

* no Godot engine execution in CI
* no remote runtime simulation
* only structural CI continuity is required

These limitations are acceptable because Phase 8 focuses on the first real room loop, not the full game runtime.

---

## Why This Scope Is Correct

Phase 8 is the correct next step because it is the first point where the accepted runtime skeleton and the accepted data-definition layer can be proven together in real runtime behavior.

Without this phase:

* data definitions remain mostly authored but not consumed,
* room phases remain largely placeholder,
* later progression and combat work would still lack a proven minimal loop.

With this phase, the project gains:

* one true data-backed room cycle,
* one real session writeback example,
* one clearer basis for later combat/progression work,
* one stronger runtime target for future automation and implementation tasks.

This makes later development more stable and more concrete.

---

## Baseline Protection Rules

The following rules apply after Phase 8 is accepted.

### Rule 1

The accepted single-room loop becomes part of the protected runtime baseline.

### Rule 2

Later phases may extend the room loop, but should not casually replace the accepted single-room direction without explicit review.

### Rule 3

A single-room loop does not authorize full multi-room progression or final combat architecture.

### Rule 4

Future save integration, progression systems, or richer combat systems must be accepted explicitly rather than assumed from the existence of the Phase 8 loop.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it,
* the single-room loop direction is intentionally changed through controlled review,
* a later phase adopts a newer accepted runtime loop baseline.

Until then, this document is the canonical scope record for Phase 8 single-room loop work.

---

## Status

Recommended metadata for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as the authoritative scope boundary for Phase 8 work in this repository.