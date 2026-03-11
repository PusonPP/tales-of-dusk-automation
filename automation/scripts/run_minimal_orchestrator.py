import json

from automation.langgraph.graphs.minimal_orchestrator import (
    build_inmemory_minimal_orchestrator,
)
from automation.langgraph.schemas.workflow_state import WorkflowState


def main() -> None:
    graph = build_inmemory_minimal_orchestrator()

    thread_id = "phase4-smoke"
    initial_state = WorkflowState(thread_id=thread_id)

    config = {
        "configurable": {
            "thread_id": thread_id,
        }
    }

    result = graph.invoke(initial_state.model_dump(), config=config)
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()