import httpx
from langchain_openai import ChatOpenAI

from app.core.config import get_settings


def get_chat_model() -> ChatOpenAI:
    """Create a chat model using the application settings."""
    settings = get_settings()

    if not settings.llm_api_key:
        raise RuntimeError("LLM_API_KEY is required.")

    return ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url,
        timeout=settings.llm_timeout_seconds,
        max_retries=2,
        http_client=httpx.Client(trust_env=False),
        http_async_client=httpx.AsyncClient(trust_env=False),
    )