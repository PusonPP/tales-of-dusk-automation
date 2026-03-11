from automation.langgraph.graphs.minimal_orchestrator import build_minimal_orchestrator
from automation.langgraph.schemas.workflow_state import WorkflowState


def test_minimal_orchestrator_happy_path():
    graph = build_minimal_orchestrator()

    initial_state = WorkflowState(thread_id="phase4-test").model_dump()
    result = graph.invoke(initial_state)

    assert str(result["current_stage"]) == "codex_tasking"
    assert result["active_artifact_ids"]["design_brief"] == "BRF-0001"
    assert result["active_artifact_ids"]["proposal"] == "PRP-0001"
    assert result["active_artifact_ids"]["review"] == "RVW-0001"
    assert result["active_artifact_ids"]["approved_spec"] == "SPEC-0001"
    assert result["blockers"] == []
    assert len(result["artifact_history"]) == 4