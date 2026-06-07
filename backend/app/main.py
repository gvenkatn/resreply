from fastapi import FastAPI

from app.provider_factory import get_model_provider
from app.safety import clamp_text, redact_pii
from app.schemas import GenerateRequest, GenerateResponse
from app.settings import get_settings

app = FastAPI(title="ResReply API", version="0.1.0")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "resreply-api",
    }


@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    settings = get_settings()
    safe_text = clamp_text(
        redact_pii(request.selectedText),
        max_chars=settings.max_selected_text_chars,
    )
    provider = get_model_provider(settings)

    return provider.generate(request, safe_text)