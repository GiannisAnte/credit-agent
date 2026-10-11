from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage

from app.graph.state import AgentState
from app.schemas.safety import SafetyCheckResult
from app.services.llm import get_chat_model
import logging
from time import perf_counter

logger = logging.getLogger(__name__)

PROMPT_PATH = (
    Path(__file__).resolve().parents[2]
    / "prompts"
    / "safety_check.md"
)


def load_safety_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8").strip()



def safety_check_node(state: AgentState) -> dict:
    model = get_chat_model().with_structured_output(
        SafetyCheckResult,
        include_raw=True,
    )

    history = state.get("messages", [])
    current_message = state.get("current_message", "")

    started_at = perf_counter()

    logger.info("Starting safety check")

    try:
        result = model.invoke(
            [
                SystemMessage(content=load_safety_prompt()),
                HumanMessage(
                    content=(
                        "История диалога:\n"
                        f"{history}\n\n"
                        "Последнее сообщение пользователя для проверки:\n"
                        f"{current_message}"
                    )
                ),
            ]
        )
    except Exception:
        logger.exception(
            "Safety LLM invocation failed; elapsed_seconds=%.3f",
            perf_counter() - started_at,
        )
        raise

    elapsed = perf_counter() - started_at

    raw_message = result.get("raw")
    parsed_response = result.get("parsed")
    parsing_error = result.get("parsing_error")

    logger.debug("Safety LLM raw response: %r", raw_message)
    logger.info(
        "Safety LLM call finished; elapsed_seconds=%.3f",
        elapsed,
    )

    if parsing_error is not None:
        logger.error(
            "Failed to parse safety LLM response: %s",
            parsing_error,
        )
        raise parsing_error

    if parsed_response is None:
        logger.error("Safety LLM returned no parsed response")
        raise ValueError("LLM returned no parsed safety result")

    logger.info(
        "Safety classification completed: trolling=%s, compliance=%s, "
        "prompt_injection=%s",
        parsed_response.is_trolling,
        parsed_response.is_compliance,
        parsed_response.prompt_injection,
    )

    return {
        "is_trolling": parsed_response.is_trolling,
        "is_compliance": parsed_response.is_compliance,
        "prompt_injection": parsed_response.prompt_injection,
    }

