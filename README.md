# AI Context Workflow

A vendor-agnostic, workflow-only specification for creating and maintaining an
AI-readable knowledge base inside software projects.

The workflow does not provide a parser, CLI, plugin, or runtime. Instead, it
defines instructions that an AI coding agent can follow directly.

## Why AI Context Generation?

AI Context Generation provides AI agents with a persistent, structured understanding of a project.

Instead of repeatedly rediscovering business rules, architecture, coding standards, and testing conventions from source code, agents read the existing AI-Context knowledge base and inspect only what has changed.

This reduces repeated repository analysis, lowers token consumption, decreases AI operational costs, and produces more consistent development across AI sessions.

## Governance

AI Context Generation is governed by a strict set of mandatory rules that define the boundaries of every workflow.

These rules ensure that agents remain inside the target repository, inspect only permitted dependencies, never download external resources, and rely only on observable evidence. This guarantees predictable, secure, and reproducible context generation across every project.

## Commands

### `initialize`

Creates the initial `AI-Context` knowledge base by inspecting the current
project, its source code, tests, configuration, documentation, and repository
history when available.

`generate` is accepted as an alias for `initialize`.

### `update`

Updates the existing `AI-Context` knowledge base after features, architectural
changes, business-rule changes, refactorings, or test-strategy changes.

## Generated directory

The workflow creates the following directory inside the target project:

```text
AI-Context/
├── README.md
├── manifest.json
├── project-overview.md
├── business-context.md
├── domain-model.md
├── architecture.md
├── design-patterns.md
├── coding-standards.md
├── testing-strategy.md
├── feature-catalog.md
├── decisions.md
├── glossary.md
├── open-questions.md
└── change-log.md
```

## How to use

Clone this repository

Copy `AGENTS.md`, the `workflows` directory, and the `templates` directory into
the project or into a shared agent-instructions repository:
```
cp -R \
  AI-Context-Generation/workflows \
  AI-Context-Generation/templates \
  AI-Context-Generation/AGENTS.md \
[YOUR_REPOSITORY_FOLDER]
```

Then instruct the coding agent with one of these commands:

```text
Follow AGENTS.md and execute the initialize workflow.
```

```text
Follow AGENTS.md and execute the update workflow for the current changes.
```

The agent must inspect the repository, create or update `AI-Context`, report
uncertainties, and avoid inventing facts.

## Design principles

- Vendor agnostic
- Human readable
- AI readable
- Repository grounded
- Incrementally maintainable
- Explicit about uncertainty
- No hidden runtime dependency
- No requirement for a parser
