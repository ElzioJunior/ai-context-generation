# ADR-0001 — AI-Context as the Single Source of Truth

## Decision

AI agents must treat the AI-Context directory as the primary source of project knowledge.

## Resolution Strategy

Read AI-Context before inspecting source code.
Inspect source code only when the required information is missing, incomplete, or needs validation.
Minimize repository traversal whenever the AI-Context already provides sufficient information.
If the implementation differs from the documented context, treat the implementation as the current source of truth and recommend updating the AI-Context through the update workflow.

## Why
Every AI agent should begin by reading `AI-Context` instead of rediscovering the repository from scratch.
