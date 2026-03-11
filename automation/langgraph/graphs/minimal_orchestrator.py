from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from automation.langgraph.nodes.minimal_orchestrator_nodes import (
    halt_on_blocker,
    load_design_brief,
    promote_to_codex_tasking,
    register_approved_spec,
    register_proposal,
    register_review,
    rollback_stop,
    route_after_baseline,
    route_after_review,
    validate_repo_baseline,
)
from automation.langgraph.schemas.workflow_state import WorkflowState


def build_minimal_orchestrator(checkpointer=None):
    builder = StateGraph(WorkflowState)

    builder.add_node("validate_repo_baseline", validate_repo_baseline)
    builder.add_node("load_design_brief", load_design_brief)
    builder.add_node("register_proposal", register_proposal)
    builder.add_node("register_review", register_review)
    builder.add_node("register_approved_spec", register_approved_spec)
    builder.add_node("promote_to_codex_tasking", promote_to_codex_tasking)
    builder.add_node("halt_on_blocker", halt_on_blocker)
    builder.add_node("rollback_stop", rollback_stop)

    builder.add_edge(START, "validate_repo_baseline")

    builder.add_conditional_edges(
        "validate_repo_baseline",
        route_after_baseline,
        {
            "load_design_brief": "load_design_brief",
            "halt_on_blocker": "halt_on_blocker",
        },
    )

    builder.add_edge("halt_on_blocker", END)

    builder.add_edge("load_design_brief", "register_proposal")
    builder.add_edge("register_proposal", "register_review")

    builder.add_conditional_edges(
        "register_review",
        route_after_review,
        {
            "register_approved_spec": "register_approved_spec",
            "rollback_stop": "rollback_stop",
        },
    )

    builder.add_edge("rollback_stop", END)
    builder.add_edge("register_approved_spec", "promote_to_codex_tasking")
    builder.add_edge("promote_to_codex_tasking", END)

    return builder.compile(checkpointer=checkpointer)


def build_inmemory_minimal_orchestrator():
    return build_minimal_orchestrator(checkpointer=InMemorySaver())