# ResReply Low-Level Design

## API Contract

### POST /generate

The extension sends selected webpage text to the backend.

Request:

{
  "selectedText": "string",
  "tone": "professional",
  "persona": {
    "role": "Software Engineer",
    "interests": ["AI infrastructure", "distributed systems"],
    "style": "concise, warm, technical"
  }
}

Response:

{
  "summary": "string",
  "postType": "hiring_post | technical_post | milestone | discussion | generic",
  "replyScore": 8.4,
  "strategy": "string",
  "suggestions": [
    {
      "label": "Short",
      "text": "string"
    },
    {
      "label": "Thoughtful",
      "text": "string"
    },
    {
      "label": "Question",
      "text": "string"
    }
  ],
  "warnings": ["string"]
}

## Backend Modules

### main.py

Owns the FastAPI app and route definitions.

Routes:

- GET /health
- POST /generate

### schemas.py

Defines typed request and response models.

Models:

- Persona
- GenerateRequest
- Suggestion
- GenerateResponse

### safety.py

Owns input safety utilities.

Responsibilities:

- Redact emails
- Redact phone numbers
- Redact obvious secrets
- Clamp selected text length

### prompt.py

Builds the structured model prompt.

The prompt must treat selected webpage text as untrusted content, not instructions.

### reply_service.py

Owns reply-generation orchestration.

Responsibilities:

- Apply redaction
- Choose provider
- Call fallback or LLM provider
- Return structured response

## Extension Modules

### manifest.json

Defines Chrome extension permissions and entry points.

Required MVP permissions:

- activeTab
- scripting
- clipboardWrite

### contentScript.ts

Reads user-selected text from the active webpage.

### App.tsx

Owns popup UI state.

State:

- selectedText
- tone
- loading
- result
- error

### api.ts

Calls the backend generation endpoint.

### types.ts

Defines shared TypeScript types for API request and response objects.

## Error Handling

If selected text is empty, show a user-friendly error.

If backend is unavailable, tell the user to start the FastAPI server.

If LLM provider fails, backend should use fallback generation.

If generated response is malformed, backend should return a safe fallback response.

## Security Constraints

- Do not expose API keys in extension code.
- Do not auto-post generated replies.
- Do not log raw selected text.
- Do not log generated replies.
- Redact sensitive data before provider calls.
- Keep user manually in control of posting.