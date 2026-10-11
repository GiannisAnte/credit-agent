from app.core.config import Settings


def test_settings_have_local_defaults() -> None:
    settings = Settings()

    assert settings.app_name == "Credit Product Agent"
    assert settings.app_env == "local"
    assert settings.llm_model != ""
    assert settings.llm_api_key is not None
