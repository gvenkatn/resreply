# ResReply

ResReply is a privacy-first browser AI copilot that helps users generate thoughtful, high-signal replies across social platforms and generic webpages.

The MVP works by analyzing user-selected webpage text and returning professional reply suggestions with a strategy, reply score, and safety warnings.

## Problem

Professionals often see posts from recruiters, engineers, founders, and technical communities but struggle to respond quickly without sounding generic, desperate, or AI-generated.

ResReply helps users:
- Understand the context of a post
- Decide how to respond
- Generate professional replies
- Avoid overclaiming or unsafe public comments

## MVP Scope

The MVP supports:
- User-selected text extraction
- Tone selection
- Reply generation
- Reply score
- Strategy explanation
- Safety warnings
- Manual copy flow

## Non-Goals

ResReply does not:
- Auto-post comments
- Bulk-comment
- Scrape profiles
- Monitor pages in the background
- Store raw page content by default
- Expose LLM API keys in the browser extension

## Architecture Preview

```text
Webpage selected text
  -> Chrome extension
  -> FastAPI backend
  -> Model provider or fallback engine
  -> Structured reply suggestions
  -> Manual copy by user