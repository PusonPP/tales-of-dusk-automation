# 009 Phase 7 Godot Data Layer Accepted

## Purpose

Record the acceptance of Phase 7, which established the first formal Godot data-definition layer for the Tales of Dusk automated development workflow repository.

This document freezes the currently accepted runtime data-layer baseline so that later room-loop implementation, deploy/combat integration, chapter progression, save integration, editor tooling, and richer CI validation can build on an explicit and governed data-definition model rather than on ad hoc code-local assumptions.

Phase 7 does not introduce full gameplay execution.  
Instead, it introduces the first accepted data-definition baseline for the Godot runtime project.

---

## Scope of Acceptance

Phase 7 acceptance covers the following runtime data-layer baseline only:

- a canonical directory structure for Godot runtime data definitions
- a script layer for custom Resource-based data model classes
- a resource-asset layer for concrete `.tres` authored definitions
- a minimal sample asset set sufficient to prove the data layer is real
- a bounded loading helper for initial data access
- extension of the repository smoke-check baseline so the data layer becomes protected
- proof that the data layer is recognized by Godot and remains compatible with the accepted runtime skeleton

This acceptance does **not** include:

- real combat execution
- real deploy placement execution
- enemy AI
- room progression runtime logic
- chapter progression runtime logic
- save/load integration for the data layer
- new Autoloads
- broad runtime architecture redesign
- Godot headless CI runtime execution
- full content authoring coverage

---

## Accepted Godot Data-Layer Baseline

The repository now contains an accepted Godot data-definition baseline with the following characteristics.

### Accepted Data Script Layer

The accepted runtime data-model script directory is:

```text
game/tales-of-dusk/scripts/data/
```

The accepted initial custom Resource classes include at minimum:

```text
unit_def.gd
enemy_spawn_def.gd
wave_def.gd
room_def.gd
chapter_def.gd
data_catalog.gd
```

These files form the accepted initial runtime data-model layer.

### Accepted Data Asset Layer

The accepted runtime definition asset directory is:

```text
game/tales-of-dusk/data/defs/
```

Its accepted initial structure includes:

```text
units/
waves/
rooms/
chapters/
```

These directories are now part of the accepted runtime baseline.

### Accepted Data-Layer Direction

The accepted implementation direction for the runtime data layer is:

* Godot custom `Resource` classes
* exported fields for editor-visible authoring
* `.tres` files for concrete definitions
* bounded explicit loading through a small helper
* no new global Autoload introduced for data access

This direction is now part of the protected Phase 7 baseline.

---

## Accepted Initial Definition Set

The accepted initial runtime definition set includes the following data-model concepts.

### Unit Definition

A `UnitDef` resource is accepted for defining:

* unit identity
* display name
* description
* supply cost
* placeholder unit stats
* future presentation hooks such as scene/icon references

### Enemy Spawn Definition

An `EnemySpawnDef` resource is accepted for defining:

* enemy type identity
* count
* spawn interval

### Wave Definition

A `WaveDef` resource is accepted for defining:

* wave identity
* start delay
* a bounded list of enemy-spawn definitions

### Room Definition

A `RoomDef` resource is accepted for defining:

* room identity
* room type
* room preview text
* supply reward
* core-shard reward
* room wave list

### Chapter Definition

A `ChapterDef` resource is accepted for defining:

* chapter identity
* chapter display name
* starting supply
* ordered room list

This definition set is accepted as sufficient for the initial runtime data layer.

---

## Accepted Initial Sample Asset Set

The accepted minimal sample asset set includes concrete `.tres` definitions proving the data layer is real.

At minimum, the accepted repository baseline includes sample assets such as:

### Units

* `unit_guard.tres`
* `unit_archer.tres`

### Waves

* `wave_room01_a.tres`
* `wave_room02_a.tres`

### Rooms

* `room_01.tres`
* `room_02.tres`
* `room_boss.tres`

### Chapters

* `chapter_01.tres`

This sample asset set is intentionally small, but it is accepted as sufficient to establish a real data baseline.

These assets are not intended to represent complete production content coverage.

---

## Accepted Loader Baseline

The accepted minimal data-loading entry is:

```text
game/tales-of-dusk/scripts/data/data_catalog.gd
```

This loader direction is accepted because it is:

* explicit
* bounded
* easy to reason about
* consistent with the repository’s current maturity
* less risky than introducing a global data registry too early

### Accepted Loader Role

The current accepted loader role is limited to:

* loading the initial chapter definition
* loading the initial default unit set
* acting as a clear first data-access entry point

This is accepted as sufficient for the data-definition phase.

### Explicit Non-Authorization

This acceptance does **not** authorize:

* a broad dynamic asset-discovery framework
* a global runtime content manager
* a new Autoload-based data service
* a hidden content registry layer

Those remain later-phase decisions.

---

## Relationship to Earlier Phases

### Relationship to Phase 2

Phase 2 established the accepted Godot runtime skeleton:

* canonical project root
* canonical main scene path
* accepted scene flow
* accepted Autoload set
* accepted room phase order

Phase 7 does not replace those baselines.

Instead, Phase 7 adds a formal data-definition layer that future runtime behavior may later consume.

The accepted Phase 2 runtime baseline remains protected.

### Relationship to Phase 3

Phase 3 established workflow governance:

* protocol documents
* artifact semantics
* state/schema baseline
* workflow discipline

Phase 7 remains subordinate to that governance model.
The runtime data layer introduced here becomes part of the repository’s protected baseline and should be handled with the same governance discipline.

### Relationship to Phase 4

Phase 4 established the accepted minimal LangGraph orchestrator.

Phase 7 does not change the accepted orchestration baseline, but it gives future workflow and implementation phases a more formal runtime content structure to target.

### Relationship to Phase 5

Phase 5 established controlled Codex entry.

Phase 7 does not grant Codex broad authority to redesign the runtime.
It only expands the accepted runtime baseline with formal data-definition files.

### Relationship to Phase 6

Phase 6 established the accepted minimal CI baseline.

Phase 7 extends that baseline by making the data-layer files part of the repository’s structurally protected file set through the smoke-check layer.

---

## What Was Explicitly Validated

Phase 7 acceptance is based on the following validated repository behavior.

### Structural Validation

The repository contains:

* the accepted data script directory
* the accepted data asset directories
* the accepted sample `.tres` definitions
* the accepted minimal data loader
* the accepted architecture scope record for Phase 7

### Local Validation

The repository demonstrated successful local execution of the existing validation chain without breaking earlier accepted baselines:

* `python -m automation.scripts.validate_protocols`
* `python -m automation.scripts.run_minimal_orchestrator`
* `python -m automation.scripts.ci_repo_smoke`
* `pytest automation\langgraph\tests -q`

This proves the data-layer addition did not break the accepted automation baseline.

### Godot Editor Validation

The runtime data layer was validated manually in the Godot editor sufficiently to confirm that:

* the custom Resource classes are recognized
* `.tres` assets can be opened
* exported fields are visible
* the sample asset set is editor-recognizable
* no obvious script-binding failure was introduced by the data-layer baseline

This is sufficient for Phase 7 acceptance.

### CI Validation

The repository’s minimal CI workflow continued to pass after the data-layer files were added.

This proves that the new data-layer files are now compatible with the current minimal CI baseline.

---

## Accepted CI Extension

Phase 7 acceptance includes extension of the minimal smoke-check baseline so that the data layer becomes part of the repository’s protected file inventory.

This means the CI baseline now protects at minimum:

* data-model scripts
* sample definition assets
* current phase metadata expectations related to the accepted repository state

This is an accepted expansion of the minimal CI baseline introduced in Phase 6.

---

## Known Limitations at Acceptance Time

This acceptance intentionally preserves several known limitations.

### Data Coverage Limitations

* the sample content set is intentionally small
* the authored `.tres` assets are not a full production database
* balancing is not the goal of this phase
* wave and room content remain minimal

### Runtime Integration Limitations

* the accepted runtime loop is not yet fully driven by the data layer
* room execution still remains largely placeholder-based
* chapter progression runtime logic is not yet implemented
* the loader remains a simple access helper

### Save and Progression Limitations

* no save schema update is accepted at this phase
* no persistent progression logic is accepted
* no full runtime content-progression state is accepted

### CI Limitations

* no Godot engine execution is run in CI
* no Godot headless validation of `.tres` loading occurs in CI
* the data layer is protected structurally, not engine-validated remotely

These limitations are acceptable because Phase 7 only aims to establish the data-definition baseline.

---

## Why This Baseline Is Accepted

Phase 7 is accepted because it converts one of the repository’s explicit non-negotiable design constraints into real project structure:

* data-driven definitions are mandatory

Specifically, Phase 7 provides:

* one accepted runtime data-script layer
* one accepted definition-asset directory structure
* one accepted minimal sample asset set
* one accepted explicit loading entry
* one accepted CI protection extension
* one accepted distinction between “data definitions exist” and “gameplay systems are implemented”

This is sufficient for:

* future single-room loop work
* future deploy/combat integration
* future chapter progression wiring
* future save integration
* future richer content authoring
* future Godot/runtime CI expansion

without prematurely implementing those later systems.

---

## Baseline Protection Rules

The following rules apply after this acceptance.

### Rule 1

The accepted data-model scripts and sample `.tres` files are now part of the protected runtime baseline.

### Rule 2

Later phases may extend the data layer, but should not casually replace the accepted Resource-based direction without explicit review.

### Rule 3

Adding a data layer does not authorize broad runtime redesign or gameplay execution work.

### Rule 4

Future phases that integrate the data layer into runtime execution, save behavior, or CI must do so explicitly rather than assuming Phase 7 already approved those capabilities.

---

## Relationship to Later Phases

Later phases may build on this accepted baseline by adding:

* room-loop execution driven by `RoomDef`
* unit selection and deployment driven by `UnitDef`
* combat result calculation informed by room/wave data
* chapter progression driven by `ChapterDef`
* save integration for progression and unlocks
* richer editor/runtime tooling for data authoring
* Godot runtime CI validation

Those later phases should build on the accepted Phase 7 data baseline rather than re-inventing runtime content definitions ad hoc.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it
* the runtime data-definition strategy is intentionally changed through controlled review
* a later phase adopts a newer accepted runtime data-layer baseline

Until then, this document is the canonical accepted runtime data-layer record for Phase 7.

---

## Status

Recommended status for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as an active architecture acceptance record for the current Godot data-layer baseline.