from app.schemas import GenerateRequest, GenerateResponse, PostType, Suggestion, Tone
from app.safety import clamp_text, redact_pii


def generate_fallback_response(request: GenerateRequest) -> GenerateResponse:
    safe_text = clamp_text(redact_pii(request.selectedText))
    post_type = classify_post_type(safe_text)

    return GenerateResponse(
        summary=safe_text[:180],
        postType=post_type,
        replyScore=score_reply_opportunity(post_type),
        strategy=build_strategy(post_type),
        suggestions=build_suggestions(request.tone),
        warnings=[
            "Review before posting.",
            "Avoid sharing confidential or private information.",
        ],
    )


def classify_post_type(text: str) -> PostType:
    lowered = text.lower()

    if any(word in lowered for word in ["hiring", "job", "recruiter", "role"]):
        return PostType.HIRING_POST

    if any(word in lowered for word in ["ai", "system", "engineering", "latency"]):
        return PostType.TECHNICAL_POST

    if any(word in lowered for word in ["launch", "congrats", "milestone"]):
        return PostType.MILESTONE

    if "?" in text:
        return PostType.DISCUSSION

    return PostType.GENERIC


def score_reply_opportunity(post_type: PostType) -> float:
    scores = {
        PostType.HIRING_POST: 8.5,
        PostType.TECHNICAL_POST: 8.0,
        PostType.MILESTONE: 7.5,
        PostType.DISCUSSION: 7.0,
        PostType.GENERIC: 6.5,
    }

    return scores[post_type]


def build_strategy(post_type: PostType) -> str:
    strategies = {
        PostType.HIRING_POST: "Show relevant alignment without asking for a referral publicly.",
        PostType.TECHNICAL_POST: "Add a thoughtful technical observation or question.",
        PostType.MILESTONE: "Be warm, specific, and congratulatory.",
        PostType.DISCUSSION: "Share a balanced perspective and invite conversation.",
        PostType.GENERIC: "Respond with a concise, thoughtful comment.",
    }

    return strategies[post_type]


def build_suggestions(tone: Tone) -> list[Suggestion]:
    if tone == Tone.TECHNICAL:
        return [
            Suggestion(
                label="Technical",
                text="The interesting part is how this moves from idea to reliable execution at scale.",
            )
        ]

    if tone == Tone.RECRUITER_SAFE:
        return [
            Suggestion(
                label="Recruiter-safe",
                text="Really interesting direction. This is the kind of practical, high-impact work I enjoy following.",
            )
        ]

    return [
        Suggestion(
            label="Professional",
            text="This is a thoughtful perspective. Thanks for sharing it.",
        )
    ]