from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Credit Product Agent"
    app_env: str = "local"
    log_level: str = "INFO"


    llm_base_url: str | None = None
    llm_api_key: str | None = None
    llm_model: str = ""
    llm_timeout_seconds: float = 30.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
