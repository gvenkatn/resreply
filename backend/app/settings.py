from enum import Enum
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelProviderName(str, Enum):
    FALLBACK = "fallback"
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GROQ = "groq"
    GEMINI = "gemini"
    OPENROUTER = "openrouter"
    OLLAMA = "ollama"


class Settings(BaseSettings):
    app_name: str = "ResReply API"
    app_env: str = "local"
    model_provider: ModelProviderName = ModelProviderName.FALLBACK
    enable_byok: bool = False
    enable_request_logging: bool = True
    enable_raw_debug_logs: bool = False
    max_selected_text_chars: int = Field(default=8000, ge=1, le=20000)

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings() -> Settings:
    return Settings()