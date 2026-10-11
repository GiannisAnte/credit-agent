
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from app.graph.nodes.response import response_node
from app.graph.nodes.safety import safety_check_node
from app.graph.state import AgentState


def route_after_safety(state: AgentState) -> str:
    if (
        state.get("is_trolling")
        or state.get("is_compliance")
        or state.get("prompt_injection")
    ):
        return "response"

    # Пока бизнес-ноды не подключены, обычные запросы тоже
    # переходят к response. Позже заменим этот маршрут.
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

    checkpointer = InMemorySaver()
    return builder.compile(checkpointer=checkpointer)
