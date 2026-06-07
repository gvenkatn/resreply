# ResReply Product Requirements Document

## Product Summary

ResReply is a privacy-first browser AI copilot that helps users generate thoughtful, high-signal replies across social platforms and generic webpages.

The MVP analyzes user-selected webpage text and returns reply suggestions with a strategy, reply score, and safety warnings.

## Problem

Professionals often see posts from recruiters, engineers, founders, and technical communities but struggle to respond quickly without sounding generic, desperate, or AI-generated.

Generic AI assistants can generate text, but they do not provide a focused workflow for professional reply strategy, platform context, public reputation, or safety.

## Target Users

- Software engineers
- Job seekers
- Founders
- Technical creators
- Students
- Professionals networking online

## MVP User Flow

1. User highlights text on any webpage.
2. User opens the ResReply Chrome extension.
3. Extension reads selected text.
4. User chooses a reply tone.
5. Backend generates a strategy, score, warnings, and reply suggestions.
6. User manually copies a reply.

## MVP Features

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

## Success Criteria

- User can generate replies from selected text.
- MVP works across generic webpages.
- Output includes at least three reply suggestions.
- User can copy a reply manually.
- No raw selected text is logged by default.
