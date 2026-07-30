# AI Context Agent Instructions

## Purpose

This repository uses an `AI-Context` directory as the canonical, AI-readable
knowledge base for the project's business rules, architecture, development
standards, testing approach, features, decisions, and terminology.

You are responsible for creating and maintaining that knowledge base when the
user requests `initialize`, `generate`, or `update`.

## Supported commands

### `initialize`

Create the `AI-Context` directory from the current state of the repository.

### `generate`

Alias for `initialize`.

### `update`

Update the existing `AI-Context` directory using the current repository state
and the requested or detected changes.

## General rules

1. Inspect the repository before writing context files.
2. Treat source code, tests, configuration, migrations, API contracts, and
   existing documentation as evidence.
3. Do not invent business rules, architectural decisions, or conventions.
4. Clearly mark uncertainty with `Unknown`, `Not confirmed`, or
   `Needs clarification`.
5. Prefer precise references to modules, packages, classes, functions, routes,
   events, tables, and tests.
6. Keep the context useful to future AI agents that have not seen the
   repository before.
7. Do not copy large source files into the context.
8. Summarize behavior, constraints, intent, and relationships.
9. Preserve valid existing context during updates.
10. Record meaningful context changes in `AI-Context/change-log.md`.
11. Record inferred but unconfirmed matters in
    `AI-Context/open-questions.md`.
12. Use the templates under `templates/AI-Context` as the required structure.

## Evidence priority

Use this priority order when sources conflict:

1. Executable tests
2. Running behavior and public contracts
3. Current source code
4. Database migrations and schemas
5. Configuration
6. Architecture decision records
7. Current project documentation
8. Comments
9. Naming-based inference

When conflicts remain, document them instead of silently choosing one version.

## Completion requirements

A workflow is complete only when:

- Every required `AI-Context` file exists.
- Each file contains repository-specific information or an explicit statement
  that the information is unavailable.
- `manifest.json` is valid JSON.
- Cross-file terminology is consistent.
- Open uncertainties are listed.
- The final response summarizes created or updated files and important
  findings.
