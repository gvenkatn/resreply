import pytest

from app.provider_factory import get_model_provider
from app.providers.fallback import FallbackProvider
from app.settings import Settings


def test_get_model_provider_returns_fallback_provider():
    settings = Settings(model_provider="fallback")

    provider = get_model_provider(settings)

    assert isinstance(provider, FallbackProvider)
    assert provider.name == "fallback"


def test_get_model_provider_rejects_unsupported_provider():
    settings = Settings(model_provider="anthropic")

    with pytest.raises(ValueError):
        get_model_provider(settings)