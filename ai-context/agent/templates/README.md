# AI Context

## Purpose

This directory is the canonical AI-readable knowledge base for this project.

It exists to help AI agents understand the project before planning or changing
code.

## Reading order

For a specific question, check `manifest.json`'s `topics` map first and read
only the one or two files it points to. Fall back to the full sequential
order below only when the topic isn't listed, or when the task requires
broad context (for example, initializing or updating this directory itself):

1. `manifest.json`
2. `project-overview.md`
3. `business-context.md`
4. `domain-model.md`
5. `architecture.md`
6. `design-patterns.md`
7. `coding-standards.md`
8. `testing-strategy.md`
9. `feature-catalog.md`
10. `decisions.md`
11. `glossary.md`
12. `open-questions.md`
13. `change-log.md`

## Agent usage rules

- Check `manifest.json`'s `topics` map before reading anything else; read only
  the matched file(s) unless the question spans multiple topics or none
  match.
- Read the relevant context before making changes.
- Verify context against the current code when accuracy is critical.
- Treat `open-questions.md` as unresolved information.
- Update the context after meaningful feature, architecture, domain, or testing
  changes.
- Never treat this directory as a substitute for inspecting implementation.
