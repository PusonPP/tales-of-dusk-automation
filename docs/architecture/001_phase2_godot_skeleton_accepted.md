# 001 Phase 2 Godot Skeleton Accepted

## Purpose

Record the acceptance of Phase 2, which established the initial Godot 4 runtime skeleton for the Tales of Dusk automated development workflow repository.

This document freezes the current accepted runtime baseline so that later automation, protocol, schema, LangGraph, Codex, QA, and CI work can evolve from a stable foundation rather than from informal assumptions.

---

## Scope of Acceptance

Phase 2 acceptance covers the following baseline runtime skeleton only:

- creation of the Godot 4 project
- registration of required Autoload singletons
- definition of initial input actions
- creation of the minimal scene flow
- creation of the placeholder room-state skeleton
- confirmation that the accepted runtime baseline is suitable for later workflow automation phases

This acceptance does **not** include:

- actual gameplay implementation
- deployment logic
- enemy wave logic
- combat logic
- room data definitions
- chapter progression systems
- save compatibility guarantees beyond the current stub level
- LangGraph execution logic
- Codex execution integration
- GitHub Actions validation workflows

---

## Accepted Runtime Baseline

The repository now contains an accepted Godot runtime baseline with the following characteristics.

### Project Root

The accepted Godot project root is:

```text
game/tales-of-dusk/
```

This directory contains the active `project.godot` file and is the canonical runtime project root for Phase 2.

### Main Scene

The accepted main scene path is:

```text
res://scenes/boot/boot.tscn
```

### Accepted Scene Flow

The accepted minimal scene flow is:

```text
Boot -> Title -> Chapter Map -> Room Test
```

This flow is the current repository runtime baseline and must not be broken by later automation work without an explicit change request and re-approval.

---

## Accepted Scene Baseline

### Boot Scene

Accepted path:

```text
res://scenes/boot/boot.tscn
```

Accepted role:

* startup handoff scene
* minimal initialization handoff
* forwards runtime control to Title

Accepted script:

```text
res://scripts/core/boot.gd
```

### Title Scene

Accepted path:

```text
res://scenes/title/title.tscn
```

Accepted role:

* placeholder title screen
* entry point for Start Game
* placeholder Continue / Settings / Quit interface

Accepted script:

```text
res://scripts/ui/title_screen.gd
```

### Chapter Map Scene

Accepted path:

```text
res://scenes/chapter_map/chapter_map.tscn
```

Accepted role:

* placeholder chapter selection / chapter entry screen
* current bridge between Title and Room Test
* temporary stand-in for future chapter progression flow

Accepted script:

```text
res://scripts/ui/chapter_map.gd
```

### Room Test Scene

Accepted path:

```text
res://scenes/rooms/room_test.tscn
```

Accepted role:

* placeholder room runtime scene
* current test harness for the canonical room phase order
* temporary shell for future deployment, combat, and result logic

Accepted script:

```text
res://scripts/room/room_test.gd
```

---

## Accepted Runtime Invariants

The following runtime invariants are now considered part of the accepted baseline.

### Required Autoloads

The accepted required Autoloads are:

* `EventBus`
* `GameSession`
* `SaveSystem`
* `SceneRouter`

These names are part of the accepted baseline and later work must not silently rename, remove, or repurpose them.

### Room Phase Order

The accepted canonical room phase order is:

```text
Preview -> Deploy -> Combat -> Result
```

Phase 2 only establishes this as a placeholder state progression shell.
It does not yet imply final gameplay behavior for any phase.

### Input Actions

The accepted initial input actions are:

* `tod_confirm`
* `tod_back`
* `tod_debug_next_state`

These actions are part of the current baseline input contract for the runtime skeleton.

---

## Accepted Directory Baseline

The accepted runtime project currently assumes the following repository-relative Godot structure:

```text
game/tales-of-dusk/
├─ project.godot
├─ scenes/
│  ├─ boot/
│  ├─ title/
│  ├─ chapter_map/
│  └─ rooms/
├─ scripts/
│  ├─ autoload/
│  ├─ core/
│  ├─ ui/
│  └─ room/
├─ data/
├─ art/
└─ audio/
```

This baseline may be expanded in later phases, but must not be arbitrarily reorganized without justification and review.

---

## What Was Explicitly Validated

Phase 2 acceptance is based on the following validated assumptions and checks.

### Structural Validation

The repository contains:

* a valid Godot project root
* a configured main scene
* registered Autoloads
* initial input map actions
* scene files at the expected accepted paths
* scene root scripts attached at the correct root nodes

### Flow Validation

The minimal accepted flow is expected to support:

* Boot automatically transferring control to Title
* Title entering Chapter Map through Start Game
* Chapter Map entering Room Test
* Room Test returning to Chapter Map
* Chapter Map returning to Title

### Placeholder State Validation

The Room Test scene is expected to support placeholder state advancement across:

* Preview
* Deploy
* Combat
* Result

with reset and back-navigation behavior available in the accepted placeholder shell.

---

## Known Limitations at Acceptance Time

This acceptance intentionally preserves several known limitations.

### Runtime Limitations

* no real deployment system exists yet
* no real combat system exists yet
* no real wave spawning system exists yet
* no real room data loading exists yet
* no chapter progression persistence exists yet
* no full save/load contract exists yet
* no environment interaction system exists yet

### Automation Limitations

* no LangGraph runtime graph exists yet
* no Codex task execution layer exists yet
* no automated protocol validation in CI exists yet
* no artifact registry exists yet

### UI Limitations

* UI is functional placeholder UI only
* layout polish is not part of this acceptance
* art direction rules are not yet enforced in runtime

These limitations are acceptable because Phase 2 only aimed to establish a stable runtime skeleton, not a feature-complete implementation.

---

## Why This Baseline Is Accepted

Phase 2 is accepted because it successfully creates a stable runtime starting point for later controlled automation work.

Specifically, it establishes:

* one canonical Godot project root
* one canonical main scene path
* one canonical minimal scene flow
* one accepted set of Autoloads
* one accepted placeholder room phase order
* one runtime baseline that future phases can reference explicitly

This is sufficient for:

* Phase 3 protocol and schema work
* future LangGraph state and node design
* future Codex task scoping
* future QA and acceptance gating
* future CI smoke testing

without forcing premature gameplay implementation.

---

## Baseline Protection Rules

The following rules apply after this acceptance.

### Rule 1

Later workflow phases must treat this runtime skeleton as the active baseline unless a newer approved architecture record supersedes it.

### Rule 2

Any change to the following requires explicit review and likely a change request:

* main scene path
* scene flow order
* required Autoloads
* room phase order
* Godot project root structure
* core runtime script ownership boundaries

### Rule 3

Later phases may extend the runtime skeleton, but should not silently destabilize the accepted baseline.

### Rule 4

If later work discovers that the accepted baseline is incomplete or inconsistent, the correction must be recorded rather than silently assumed.

---

## Relationship to Later Phases

This acceptance record exists to support later repository phases.

### Phase 3

Phase 3 may define protocol documents, artifact schemas, and workflow state models, but it should not break the accepted Godot runtime baseline.

### Phase 4 and Beyond

Future graph orchestration, Codex tasking, QA, and CI may rely on this record as a reference for:

* runtime invariants
* accepted paths
* baseline scene flow
* protected project assumptions

If later phases intentionally change those assumptions, a newer architecture decision record must supersede this document.

---

## Supersession Policy

This record remains active until one of the following occurs:

* a later approved architecture record supersedes it,
* the Godot runtime baseline is intentionally restructured through controlled workflow review,
* the repository adopts a newer accepted runtime baseline.

Until then, this document is the canonical accepted runtime baseline for Phase 2.

---

## Status

Recommended status for this record:

* version: `1.0.0`
* status: `accepted`

This document should be treated as an active architecture acceptance record for the current repository baseline.