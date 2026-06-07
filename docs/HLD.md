# ResReply High-Level Design

## Overview

ResReply is a browser-based AI reply copilot. The MVP allows users to select text on any webpage, send it to a backend API, and receive structured reply suggestions.

The system is human-in-the-loop. ResReply does not auto-post, bulk-comment, scrape profiles, or monitor pages in the background.

## Architecture

Webpage
  -> Chrome Extension Content Script
  -> Extension Popup UI
  -> FastAPI Backend
  -> Model Provider or Fallback Engine
  -> Structured Reply Response
  -> Manual Copy by User

## Components

### Chrome Extension

The extension is responsible for:

- Reading user-selected text
- Displaying a popup UI
- Letting the user choose a tone
- Calling the backend API
- Rendering reply suggestions
- Letting the user manually copy a reply

### FastAPI Backend

The backend is responsible for:

- Validating requests
- Redacting sensitive data
- Building model prompts
- Calling a model provider or fallback engine
- Returning structured JSON responses

### Model Provider

The model provider generates:

- Post summary
- Post type
- Reply score
- Response strategy
- Suggested replies
- Safety warnings

### Fallback Engine

The fallback engine returns deterministic suggestions when no LLM provider is configured or when the provider fails.

## Key Design Decisions

### Selected Text First

The MVP analyzes user-selected text instead of scraping the full page.

This improves privacy, keeps the system platform-agnostic, and avoids brittle DOM parsing.

### Backend-Mediated Model Calls

The extension does not call LLM providers directly.

This protects API keys and allows the backend to enforce redaction, rate limiting, logging policy, and provider routing.

### Manual Copy Only

The product does not auto-post.

This keeps the user in control and reduces platform-policy, spam, and reputation risks.

## Future Architecture

Phase 2 may add:

- Platform-aware extractors
- Side panel UI
- User persona storage
- Provider abstraction
- Structured logging
- Request IDs
- Prompt evaluation tests