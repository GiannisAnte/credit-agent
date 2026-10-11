from app.graph.builder import build_graph


def test_graph_restores_state_for_same_thread() -> None:
    graph = build_graph()
    config = {"configurable": {"thread_id": "checkpoint-test-001"}}

    graph.invoke(
        {
            "session_id": "checkpoint-test-001",
            "client_id": "client-001",
            "current_message": "Нужен кредит на машину",
            "pending_question": "Машина для личного пользования или перепродажи?",
        },
        config=config,
    )

    result = graph.invoke(
        {
            "session_id": "checkpoint-test-001",
            "client_id": "client-001",
            "current_message": "Для личного пользования",
        },
        config=config,
    )

    assert result["pending_question"] == (
        "Машина для личного пользования или перепродажи?"
    )
    assert result["current_message"] == "Для личного пользования"
