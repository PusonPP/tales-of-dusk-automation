from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[2]


def require_file(rel_path: str) -> None:
    path = REPO_ROOT / rel_path
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {rel_path}")


def require_text(rel_path: str, required_snippets: list[str]) -> None:
    path = REPO_ROOT / rel_path
    text = path.read_text(encoding="utf-8")
    for snippet in required_snippets:
        if snippet not in text:
            raise AssertionError(
                f"Required snippet not found in {rel_path}: {snippet}"
            )


def main() -> int:
    required_files = [
        "README.md",
        "AGENTS.md",
        "automation/AGENTS.md",
        "docs/AGENTS.md",
        "game/tales-of-dusk/AGENTS.md",
        "docs/protocols/automation_protocol.md",
        "docs/protocols/workflow_stage_machine.md",
        "docs/architecture/005_phase5_codex_entry_accepted.md",
        "automation/langgraph/schemas/workflow_state.py",
        "automation/langgraph/graphs/minimal_orchestrator.py",
        "automation/scripts/validate_protocols.py",
        "automation/scripts/run_minimal_orchestrator.py",
        "game/tales-of-dusk/project.godot",
        ".github/workflows/codex_manual_review.yml",
        ".github/workflows/codex_manual_task.yml",
        ".github/codex/prompts/review.md",
        ".github/codex/prompts/repo_audit.md",
        ".github/codex/prompts/implement_from_task.md",
        "game/tales-of-dusk/scripts/data/unit_def.gd",
        "game/tales-of-dusk/scripts/data/enemy_spawn_def.gd",
        "game/tales-of-dusk/scripts/data/wave_def.gd",
        "game/tales-of-dusk/scripts/data/room_def.gd",
        "game/tales-of-dusk/scripts/data/chapter_def.gd",
        "game/tales-of-dusk/scripts/data/data_catalog.gd",
        "game/tales-of-dusk/data/defs/units/unit_guard.tres",
        "game/tales-of-dusk/data/defs/units/unit_archer.tres",
        "game/tales-of-dusk/data/defs/rooms/room_01.tres",
        "game/tales-of-dusk/data/defs/rooms/room_02.tres",
        "game/tales-of-dusk/data/defs/rooms/room_boss.tres",
        "game/tales-of-dusk/data/defs/chapters/chapter_01.tres",
        "game/tales-of-dusk/data/defs/waves/wave_room01_a.tres",
        "game/tales-of-dusk/data/defs/waves/wave_room02_a.tres",
    ]

    for rel_path in required_files:
        require_file(rel_path)

    require_text(
        "README.md",
        [
            "Phase 7",
            "Phase 8",
        ],
    )

    require_text(
        "game/tales-of-dusk/project.godot",
        [
            "run/main_scene=",
            "[autoload]",
            'EventBus=',
            'GameSession=',
            'SaveSystem=',
            'SceneRouter=',
            'tod_confirm=',
            'tod_back=',
            'tod_debug_next_state=',
        ],
    )

    print("CI repo smoke check OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())