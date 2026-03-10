from automation.langgraph.schemas.workflow_state import WorkflowState


def main():
    state = WorkflowState(thread_id="bootstrap-phase3")
    print("WorkflowState validation OK")
    print(state.model_dump())


if __name__ == "__main__":
    main()