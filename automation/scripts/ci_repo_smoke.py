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
        # Root / governance
        "README.md",
        "AGENTS.md",
        "automation/AGENTS.md",
        "docs/AGENTS.md",
        "game/tales-of-dusk/AGENTS.md",

        # Protocol / architecture
        "docs/protocols/automation_protocol.md",
        "docs/protocols/workflow_stage_machine.md",
        "docs/architecture/005_phase5_codex_entry_accepted.md",
        "docs/architecture/006_phase6_minimal_ci_scope.md",
        "docs/architecture/007_phase6_minimal_ci_accepted.md",
        "docs/architecture/008_phase7_godot_data_layer_scope.md",
        "docs/architecture/009_phase7_godot_data_layer_accepted.md",
        "docs/architecture/010_phase8_single_room_loop_scope.md",

        # Automation baseline
        "automation/requirements.txt",
        "automation/langgraph/schemas/workflow_state.py",
        "automation/langgraph/graphs/minimal_orchestrator.py",
        "automation/scripts/validate_protocols.py",
        "automation/scripts/run_minimal_orchestrator.py",
        "automation/scripts/ci_repo_smoke.py",

        # Codex prompt / workflow assets (prepared but not activated)
        ".github/workflows/ci_minimal.yml",
        ".github/workflows/codex_manual_review.yml",
        ".github/workflows/codex_manual_task.yml",
        ".github/codex/prompts/review.md",
        ".github/codex/prompts/repo_audit.md",
        ".github/codex/prompts/implement_from_task.md",

        # Godot runtime baseline
        "game/tales-of-dusk/project.godot",
        "game/tales-of-dusk/scenes/boot/boot.tscn",
        "game/tales-of-dusk/scenes/title/title.tscn",
        "game/tales-of-dusk/scenes/chapter_map/chapter_map.tscn",
        "game/tales-of-dusk/scenes/rooms/room_test.tscn",
        "game/tales-of-dusk/scripts/autoload/EventBus.gd",
        "game/tales-of-dusk/scripts/autoload/GameSession.gd",
        "game/tales-of-dusk/scripts/autoload/SaveSystem.gd",
        "game/tales-of-dusk/scripts/autoload/SceneRouter.gd",
        "game/tales-of-dusk/scripts/ui/chapter_map.gd",
        "game/tales-of-dusk/scripts/room/room_test.gd",

        # Phase 7 data layer
        "game/tales-of-dusk/scripts/data/unit_def.gd",
        "game/tales-of-dusk/scripts/data/enemy_spawn_def.gd",
        "game/tales-of-dusk/scripts/data/wave_def.gd",
        "game/tales-of-dusk/scripts/data/room_def.gd",
        "game/tales-of-dusk/scripts/data/chapter_def.gd",
        "game/tales-of-dusk/scripts/data/data_catalog.gd",

        "game/tales-of-dusk/data/defs/units/unit_guard.tres",
        "game/tales-of-dusk/data/defs/units/unit_archer.tres",
        "game/tales-of-dusk/data/defs/waves/wave_room01_a.tres",
        "game/tales-of-dusk/data/defs/waves/wave_room02_a.tres",
        "game/tales-of-dusk/data/defs/rooms/room_01.tres",
        "game/tales-of-dusk/data/defs/rooms/room_02.tres",
        "game/tales-of-dusk/data/defs/rooms/room_boss.tres",
        "game/tales-of-dusk/data/defs/chapters/chapter_01.tres",
    ]

    for rel_path in required_files:
        require_file(rel_path)

    # README phase metadata
    # This version assumes:
    # Current Phase = Phase 7
    # Next Step = Phase 8
    require_text(
        "README.md",
        [
            "Phase 7 - Godot data layer definition",
            "Phase 8 - Single room minimal gameplay loop",
        ],
    )

    # Godot project baseline
    require_text(
        "game/tales-of-dusk/project.godot",
        [
            "run/main_scene=",
            "[autoload]",
            "EventBus=",
            "GameSession=",
            "SaveSystem=",
            "SceneRouter=",
            "tod_confirm",
            "tod_back",
            "tod_debug_next_state",
        ],
    )

    # Chapter Map must now be data-backed, not hardcoded to a fake room id only
    require_text(
        "game/tales-of-dusk/scripts/ui/chapter_map.gd",
        [
            "DEFAULT_CHAPTER_ID",
            "DataCatalog.load_chapter",
            "DataCatalog.get_first_room_id_for_chapter",
            "GameSession.start_chapter",
            "GameSession.begin_room",
            "SceneRouter.go_to_room_test",
        ],
    )

    # GameSession must contain the minimal room-loop session state
    require_text(
        "game/tales-of-dusk/scripts/autoload/GameSession.gd",
        [
            "current_room_index",
            "selected_unit_ids",
            "last_room_victory",
            "last_room_reward_supply",
            "last_room_reward_core_shards",
            "func begin_room(",
            "func set_selected_units(",
            "func apply_room_result(",
        ],
    )

    # DataCatalog must support explicit loading for chapter / room / unit access
    require_text(
        "game/tales-of-dusk/scripts/data/data_catalog.gd",
        [
            "const CHAPTER_PATHS",
            "const ROOM_PATHS",
            "const UNIT_PATHS",
            "func load_chapter(",
            "func load_room_by_id(",
            "func load_unit_by_id(",
            "func load_default_units(",
            "func get_first_room_id_for_chapter(",
        ],
    )

    # room_test.gd must now implement the bounded single-room loop
    require_text(
        "game/tales-of-dusk/scripts/room/room_test.gd",
        [
            "MAX_DEPLOY_UNITS",
            "func _enter_preview(",
            "func _enter_deploy(",
            "func _enter_combat(",
            "func _enter_result(",
            "DataCatalog.load_room_by_id",
            "DataCatalog.load_default_units",
            "GameSession.apply_room_result",
            "SceneRouter.go_to_chapter_map",
        ],
    )

    # room_test.tscn must contain the required nodes for the minimal loop UI
    require_text(
        "game/tales-of-dusk/scenes/rooms/room_test.tscn",
        [
            'node name="LblRoomTitle"',
            'node name="LblRoomPreview"',
            'node name="LblSupply"',
            'node name="LblReward"',
            'node name="BtnStartDeploy"',
            'node name="BtnSelectGuard"',
            'node name="BtnSelectArcher"',
            'node name="LblDeploySummary"',
            'node name="BtnStartCombat"',
            'node name="LblCombatSummary"',
            'node name="BtnResolveCombat"',
            'node name="LblResultSummary"',
            'node name="BtnBackToMap"',
        ],
    )

    # Phase 7 sample defs should remain coherent and present
    require_text(
        "game/tales-of-dusk/data/defs/chapters/chapter_01.tres",
        [
            'chapter_id = &"chapter_01"',
            "starting_supply",
        ],
    )

    require_text(
        "game/tales-of-dusk/data/defs/rooms/room_01.tres",
        [
            'room_id = &"room_01"',
            "waves = [",
        ],
    )

    require_text(
        "game/tales-of-dusk/data/defs/units/unit_guard.tres",
        [
            'unit_id = &"guard"',
            "supply_cost",
        ],
    )

    print("CI repo smoke check OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
