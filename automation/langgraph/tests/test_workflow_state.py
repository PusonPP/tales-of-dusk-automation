from automation.langgraph.schemas.workflow_state import WorkflowState


def test_workflow_state_bootstrap():
    state = WorkflowState(thread_id="bootstrap-phase3")
    assert state.current_stage == "brief_intake"
    assert state.repo.default_branch == "main"
    assert state.runtime_invariants.main_scene_path == "res://scenes/boot/boot.tscn"