# 008 Phase 7 Godot Data Layer Scope

## Purpose

Record the scope boundary for Phase 7 of the Tales of Dusk automated development workflow repository.

Phase 7 exists to establish the first formal Godot data-definition layer for the runtime project.

Its purpose is to move the runtime baseline from a purely code-driven placeholder structure toward a controlled, explicit, data-driven definition model using Godot Resources and repository-managed data assets.

Phase 7 does **not** attempt to implement full gameplay systems.  
It introduces the data layer only.

This record prevents another common failure mode: attempting to build combat, room progression, or content pipelines before the project has stable runtime data definitions.

---

## Phase 7 Mission

The mission of Phase 7 is:

- define the first canonical Godot runtime data models,
- establish a stable directory structure for runtime definitions,
- introduce custom `Resource`-based data classes,
- create a minimal set of real `.tres` data assets,
- establish a small data-loading entry path,
- extend repository validation so the data layer becomes part of the protected baseline,
- do all of the above without broad gameplay-system implementation,
- do all of the above without breaking the accepted runtime skeleton.

Phase 7 is a **data-definition phase**, not a gameplay-execution phase.

---

## Why Phase 7 Exists

The repository already has:

- a Phase 1 repository foundation,
- a Phase 2 accepted Godot runtime skeleton,
- a Phase 3 accepted protocol/schema/state baseline,
- a Phase 4 accepted minimal LangGraph orchestrator,
- a Phase 5 accepted bounded Codex entry layer,
- a Phase 6 accepted minimal GitHub Actions quality gate.

However, the runtime project still lacks a formal data-definition layer.

Without Phase 7, the runtime remains structurally fragile because important future concepts such as:

- units,
- waves,
- rooms,
- chapters,
- spawn composition,
- content sequencing,

would either remain implicit in code or be introduced ad hoc during gameplay implementation.

Phase 7 exists to solve that by introducing a stable, repository-visible, Godot-native data-definition baseline.

---

## Accepted Scope for Phase 7

Phase 7 is explicitly in scope for the following work.

### 1. Data Layer Directory Structure

Phase 7 defines the initial canonical directory structure for runtime data definitions.

This includes:

- a script layer for data model classes
- a resource asset layer for concrete definition files

This structure should make it clear which files are:
- type definitions
- instance data assets

---

### 2. Godot Resource-Based Data Models

Phase 7 defines the first custom Godot `Resource` classes used as runtime data definitions.

These classes are expected to model at least the minimal vertical-slice content structure needed for later work.

At minimum, Phase 7 may define data classes such as:

- `UnitDef`
- `EnemySpawnDef`
- `WaveDef`
- `RoomDef`
- `ChapterDef`

The accepted implementation mechanism is Godot custom Resources.

---

### 3. Minimal Sample Data Assets

Phase 7 defines the first concrete data assets using `.tres` files.

These data assets are expected to prove that:

- the custom resource classes are usable,
- the runtime data layer is no longer merely theoretical,
- the project now has a real authored content baseline.

These sample assets are not intended to represent a complete game database.  
They are intended to establish the baseline.

---

### 4. Minimal Data Loading Entry

Phase 7 may define a small and explicit loading helper for the sample data assets.

This loader should remain simple and bounded.

Its purpose is to:
- provide a canonical loading entry for the first data assets,
- prove that the data layer is consumable,
- avoid forcing later phases to guess how runtime definitions should initially be accessed.

---

### 5. CI/Smoke Baseline Extension

Phase 7 includes extending the repository smoke-check baseline so that the new data-definition files become part of the repository’s protected baseline.

This ensures that:
- missing data scripts are caught,
- missing sample assets are caught,
- the Phase 7 data layer becomes part of the minimal CI guardrail.

---

## Explicitly Out of Scope for Phase 7

The following are **not** part of Phase 7.

### 1. Gameplay Execution Systems

Phase 7 does **not** include:

- combat execution
- deploy execution
- enemy AI
- damage systems
- battle simulation
- wave runtime scheduling
- unit runtime behavior implementation
- room progression execution
- chapter runtime progression logic

These are later-phase systems.

---

### 2. New Autoloads

Phase 7 does **not** introduce new global Autoload singletons by default.

That means:
- no automatic `DataRegistry` autoload
- no global content manager singleton
- no new global runtime service just to hold data definitions

Data access should remain bounded and explicit.

---

### 3. Save Integration

Phase 7 does **not** integrate the new data layer into save/load persistence in a broad way.

That means:
- no full save schema changes
- no persistent chapter progression storage
- no persistent room-state serialization
- no broad save compatibility redesign

Those remain later concerns.

---

### 4. Chapter Map / Room Runtime Rebuild

Phase 7 does **not** rebuild the accepted runtime skeleton around the new data layer.

That means it does not include:
- replacing the current scene flow
- reauthoring scene routing around data definitions
- converting all current placeholder runtime behavior into fully data-driven execution
- changing the accepted minimal scene baseline

The accepted runtime skeleton from Phase 2 must remain intact.

---

### 5. Godot CI Runtime Execution

Phase 7 does **not** require:

- Godot executable installation in CI
- Godot headless resource loading tests
- scene execution under CI
- export/build jobs

The data layer should still be protected structurally through repository CI, but Phase 7 is not yet an engine-runtime CI phase.

---

### 6. Broad Content Authoring

Phase 7 does **not** require a complete content library.

It does not include:
- all rooms
- all chapters
- final enemy catalogs
- final balancing tables
- event scripting trees
- full deployment configuration coverage

Only the minimal sample asset set needed to establish the baseline is required.

---

## Canonical Deliverables of Phase 7

Phase 7 is considered complete only if the following deliverables exist.

### Data Model Scripts
A data-model script directory under the Godot runtime project, containing the accepted initial custom Resource classes.

### Data Asset Directories
A data-asset directory under the Godot runtime project for concrete `.tres` definitions.

### Minimal Sample Assets
A minimal but coherent sample asset set covering:
- units
- rooms
- waves
- chapters

### Minimal Data Loader
A bounded script that can load the initial sample data assets.

### CI Smoke Extension
The repository smoke-check layer updated so these files are protected by the existing minimal CI baseline.

### Architecture Record
This scope record.

---

## Required Constraints During Phase 7

The following constraints apply throughout Phase 7.

### Constraint 1
Phase 7 must preserve the accepted runtime skeleton from Phase 2.

### Constraint 2
Phase 7 must not introduce new Autoloads casually.

### Constraint 3
Phase 7 must prefer Godot-native Resource-based data modeling over ad hoc text or generic dictionaries.

### Constraint 4
Phase 7 must keep the initial data layer small and explicit.

### Constraint 5
Phase 7 must not silently expand into gameplay execution or runtime-system redesign.

### Constraint 6
Phase 7 must keep data loading bounded and understandable.

### Constraint 7
Phase 7 must extend existing CI protection rather than bypass it.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton:

- canonical project root
- canonical main scene path
- accepted scene flow
- accepted Autoload set
- accepted room phase order

Phase 7 must preserve those baselines.

The data layer introduced here is intended to support later runtime evolution, not to invalidate the accepted skeleton.

### Relationship to Phase 3

Phase 3 established protocol/state/schema governance for the repository workflow.

Phase 7 must remain subordinate to those workflow rules.

If Phase 7 introduces new protected runtime files, they should be reflected through repository discipline rather than bypassing it.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 7 does not alter the accepted orchestrator baseline, but may indirectly affect future task-generation and workflow planning by making runtime definitions more formal.

### Relationship to Phase 5

Phase 5 established controlled Codex entry.

Phase 7 may use Codex locally in bounded ways, but does not grant Codex broader runtime redesign authority.

### Relationship to Phase 6

Phase 6 established the accepted minimal CI baseline.

Phase 7 should extend that baseline by adding structural protection for the new data layer rather than replacing it.

---

## Relationship to Later Phases

Later phases may build on the Phase 7 data layer by adding:

- room execution driven by `RoomDef`
- wave spawning driven by `WaveDef`
- deployment options driven by `UnitDef`
- chapter progression driven by `ChapterDef`
- save integration for progression and unlocks
- richer content authoring workflows
- Godot runtime validation in CI
- editor tooling for definition authoring

Those later phases should build on the Phase 7 data baseline rather than re-inventing the data layer ad hoc.

---

## Accepted Data-Layer Direction

The accepted implementation direction for the data layer is:

- Godot custom `Resource` classes
- exported fields for editor-visible authoring
- `.tres` resource assets for concrete definitions
- bounded, explicit loading via `ResourceLoader`
- repository-visible organization under the runtime subtree

This direction is accepted because it is Godot-native, inspector-friendly, and appropriate for gradual runtime evolution.

---

## Minimal Accepted Definition Set

The minimal accepted definition set for Phase 7 may include:

### Unit Definition
For deployable unit identity, cost, placeholder stats, and presentation hooks.

### Enemy Spawn Definition
For one bounded enemy-spawn entry.

### Wave Definition
For a bounded wave composed of one or more enemy-spawn definitions.

### Room Definition
For room identity, room type, preview text, rewards, and wave list.

### Chapter Definition
For chapter identity, starting supply, and room list.

This set is accepted as sufficient for the initial runtime data layer.

---

## Minimal Accepted Sample Asset Set

The minimal accepted sample asset set should be enough to prove that the data layer is real.

A reasonable accepted baseline is:

- at least two unit definitions
- at least two normal room definitions
- at least one boss room definition
- at least one chapter definition
- at least one or more wave/sample spawn definitions sufficient to connect room content coherently

This set is intentionally small.

---

## Minimal Accepted Loader Direction

The accepted initial loading direction is:

- a small explicit helper or catalog
- no broad registry framework
- no new Autoload
- no hidden dynamic discovery system

This is accepted because Phase 7 is about establishing the data layer, not solving the full content runtime architecture.

---

## What Was Intended to Be Validated by Phase 7

Phase 7 is intended to prove all of the following:

- the runtime now has a formal data-definition layer
- Godot custom Resources are usable for repository-managed runtime definitions
- authored `.tres` assets can exist as part of the runtime baseline
- the data layer can be loaded explicitly
- the repository CI baseline can protect the existence of the new data layer
- later gameplay/system phases no longer need to invent their content-definition model from scratch

---

## Known Limitations at Acceptance Time

This scope intentionally preserves several limitations.

### Data Limitations
- the initial data layer is small
- content coverage is intentionally incomplete
- balancing is not the goal
- data relationships remain minimal

### Runtime Limitations
- current placeholder runtime behavior is not yet fully driven by the data layer
- loading may remain mostly demonstrative at first
- execution systems are still deferred

### CI Limitations
- no Godot runtime loading tests in CI
- no engine-level validation of `.tres` consumption under CI
- only structural protection is required at this phase

These limitations are acceptable because Phase 7 focuses on definition, not full execution.

---

## Why This Scope Is Correct

Phase 7 is the correct next step because it converts one of the repository’s stated non-negotiable design constraints into concrete project structure:

- **data-driven definitions are mandatory**

Without this phase, later runtime and automation work would continue to rely on implicit content structure.

With this phase, the repository gains:

- explicit runtime content models
- real authored content assets
- a shared basis for later system implementation
- a more stable future task-generation target for workflow and Codex usage

This makes later runtime work safer and more consistent.

---

## Baseline Protection Rules

The following rules apply after Phase 7 is accepted.

### Rule 1
The new data-model scripts and sample data assets become part of the protected runtime baseline.

### Rule 2
Later phases may extend the data layer, but should not casually replace the accepted Resource-based direction without explicit review.

### Rule 3
Adding a data layer does not authorize runtime-system redesign.

### Rule 4
Future phases that integrate the data layer into save, CI, or live gameplay execution must do so explicitly rather than assuming Phase 7 already approved it.

---

## Supersession Policy

This record remains active until one of the following occurs:

- a later approved architecture record supersedes it
- the runtime data-layer strategy is intentionally changed through controlled review
- a later phase adopts a newer accepted data-definition baseline

Until then, this document is the canonical scope record for Phase 7 Godot data-layer work.

---

## Status

Recommended metadata for this record:

- version: `1.0.0`
- status: `accepted`

This document should be treated as the authoritative scope boundary for Phase 7 work in this repository.