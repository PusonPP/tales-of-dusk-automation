# 000 Repo Foundation

## Purpose
Freeze the repository layout, branch policy, and baseline tooling before any gameplay implementation starts.

## Decisions
- Godot 4 is the runtime engine.
- LangGraph is the workflow orchestrator.
- Codex is the constrained implementation agent.
- GitHub Actions is the CI gate.
- Windows is the primary local development platform.
- Repository is split into /game, /automation, /docs, /.github.
- Gameplay is not implemented before workflow skeleton exists.

## Consequences
- All future work must fit the repository structure.
- Docs become first-class artifacts.
- Agent outputs are versioned.
- Codex tasks must reference approved specs.