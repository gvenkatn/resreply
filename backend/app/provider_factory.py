from app.providers.base import ModelProvider
from app.providers.fallback import FallbackProvider
from app.settings import ModelProviderName, Settings


def get_model_provider(settings: Settings) -> ModelProvider:
    if settings.model_provider == ModelProviderName.FALLBACK:
        return FallbackProvider()

    raise ValueError(f"Unsupported model provider: {settings.model_provider}")