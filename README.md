# Tales of Dusk Automation

## 1. Project Purpose
This repository hosts the automated development workflow and Godot 4 implementation pipeline for Tales of Dusk.

## 2. Core Workflow Stack
- Engine: Godot 4
- Orchestration: LangGraph
- Coding Agent: Codex
- CI/CD: GitHub Actions
- Primary Local OS: Windows

## 3. Current Phase
Phase 7

## 4. Non-Negotiable Design Constraints
- Room loop: Preview -> Deploy -> Combat -> Result
- Dual economy: Supply (in-chapter), Core Shards (meta)
- Units do not carry across rooms
- Supply carries within chapter, resets on new chapter
- Vertical slice target: 1 chapter, ~8 rooms, boss finale
- Data-driven definitions are mandatory

## 5. Repository Layout
- /game: Godot project
- /automation: LangGraph + Codex workflow code
- /docs: briefs, specs, reviews, QA, acceptance, changes
- /.github: CI workflows and Codex prompt assets

## 6. Branch Policy
- main: stable
- integration: integration branch
- task/*: feature/task branches
- hotfix/*: urgent fixes
- spike/*: experiments

## 7. Tooling Baseline
- Windows local development
- Python 3.11
- Godot 4 stable
- Git + GitHub
- VS Code

## 8. Next Step
Phase 8