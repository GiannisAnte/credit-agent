from app.graph.state import AgentState


def response_node(state: AgentState) -> dict:
    if state.get("prompt_injection_detected"):
        return {
            "response_status": "blocked",
            "response_message": (
                "Не удалось обработать запрос. "
                "Пожалуйста, задайте вопрос о банковских продуктах."
            ),
        }

    return {
        "response_status": "completed",
        "response_message": "Запрос прошёл предварительную проверку.",
    }
