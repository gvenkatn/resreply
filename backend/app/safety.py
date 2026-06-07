import re


EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"\+?\d[\d\-\s().]{7,}\d")
SECRET_RE = re.compile(
    r"(?i)\b(api[_-]?key|secret|token|password)\s*[:=]\s*[^\s]+"
)


def redact_pii(text: str) -> str:
    redacted = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    redacted = PHONE_RE.sub("[REDACTED_PHONE]", redacted)
    redacted = SECRET_RE.sub("[REDACTED_SECRET]", redacted)
    return redacted.strip()


def clamp_text(text: str, max_chars: int = 8000) -> str:
    stripped = text.strip()

    if len(stripped) <= max_chars:
        return stripped

    return stripped[:max_chars] + "..."