from langgraph.graph import END, START, StateGraph

from app.graph.nodes.response import response_node
from app.graph.nodes.safety import safety_check_node
from app.graph.state import AgentState


def route_after_safety(state: AgentState) -> str:
    if state.get("prompt_injection_detected"):
        return "response"

    return "response"


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("safety_check", safety_check_node)
    builder.add_node("response", response_node)

    builder.add_edge(START, "safety_check")
    builder.add_conditional_edges(
        "safety_check",
        route_after_safety,
        {
            "response": "response",
        },
    )
    builder.add_edge("response", END)

    return builder.compile()
