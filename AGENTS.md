# AGENTS.md

## Mission
This repository is for building and evolving the automated game development workflow and the Godot 4 implementation of Tales of Dusk.

## Hard Rules
1. Do not invent gameplay features outside approved specs.
2. Do not modify files outside the allowed scope of the current task.
3. Do not rewrite architecture without an approved architecture review.
4. Always preserve data-driven design.
5. Always keep the room loop intact: Preview -> Deploy -> Combat -> Result.
6. Never hardcode unit/enemy/chapter balancing data into gameplay scripts when it belongs in definitions/resources.
7. Any save-data change must be explicitly declared.
8. Any UI flow change must be explicitly declared.
9. Prefer small diffs over broad refactors.
10. If uncertain, stop at the narrowest safe implementation.

## Required Outputs For Any Implementation Task
- Summary of what changed
- Files changed
- Risks introduced
- What was intentionally not changed
- Manual verification steps

## Repository Boundaries
- /game: runtime game implementation
- /automation: orchestration and task generation
- /docs: source-of-truth documents
- /.github: CI and Codex workflow assets

## Forbidden Without Approval
- Save schema changes
- Branch policy changes
- CI privilege changes
- Global singleton/autoload expansion
- Prompt template rewrites
- Deleting docs history

## Workflow Principle
Approved spec -> Codex task -> implementation -> QA report -> acceptance decision