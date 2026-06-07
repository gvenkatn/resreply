from fastapi import FastAPI

from app.reply_service import generate_fallback_response
from app.schemas import GenerateRequest, GenerateResponse

app = FastAPI(title="ResReply API", version="0.1.0")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "resreply-api",
    }


@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    return generate_fallback_response(request)