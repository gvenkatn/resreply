from app.providers.base import ModelProvider
from app.reply_service import generate_fallback_response
from app.schemas import GenerateRequest, GenerateResponse


class FallbackProvider(ModelProvider):
    @property
    def name(self) -> str:
        return "fallback"

    def generate(
        self,
        request: GenerateRequest,
        safe_text: str,
    ) -> GenerateResponse:
        fallback_request = request.model_copy(
            update={"selectedText": safe_text}
        )
        return generate_fallback_response(fallback_request)