import pytest
from pydantic import ValidationError

from app.settings import ModelProviderName, Settings


def test_settings_uses_safe_defaults():
    settings = Settings()

    assert settings.app_name == "ResReply API"
    assert settings.model_provider == ModelProviderName.FALLBACK
    assert settings.enable_raw_debug_logs is False


def test_settings_accepts_supported_provider():
    settings = Settings(model_provider="anthropic")

    assert settings.model_provider == ModelProviderName.ANTHROPIC


def test_settings_rejects_invalid_provider():
    with pytest.raises(ValidationError):
        Settings(model_provider="unknown")


def test_settings_rejects_invalid_text_limit():
    with pytest.raises(ValidationError):
        Settings(max_selected_text_chars=0)