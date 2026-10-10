from app.graph.state import AgentState


def safety_check_node(state: AgentState) -> dict:
    message = state.get("current_message", "").lower()

    injection_markers = (
        "ignore all previous instructions",
        "ignore previous instructions",
        "reveal your system prompt",
    )

    injection_detected = any(
        marker in message for marker in injection_markers
    )

    return {
        "is_trolling": False,
        "compliance_blocked": False,
        "prompt_injection_detected": injection_detected,
    }
