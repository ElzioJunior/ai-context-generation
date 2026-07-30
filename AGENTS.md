# AI Context Agent Instructions

## Purpose

This repository uses an `AI-Context` directory as the canonical AI-readable knowledge base for the project's business rules, architecture, development standards, testing approach, features, decisions, and terminology.

You are responsible for creating and maintaining that knowledge base whenever the user requests `initialize`, `generate`, or `update`.

---

# Governance Rules

These governance rules are mandatory for every workflow.

They take precedence over all workflow instructions and must not be bypassed unless the user explicitly authorizes a specific exception.

## Rule 1 — Repository Boundary

The agent and any sub-agents must remain strictly inside the current repository.

The repository root is the maximum allowed traversal boundary.

The agent must not inspect:

* sibling repositories
* parent directories
* unrelated workspaces
* the user's home directory
* global configuration directories
* caches
* temporary directories

If external access appears necessary, the workflow must stop and request explicit authorization.

---

## Rule 2 — Dependency Inspection

The agent may inspect only direct dependencies declared by the current project.

Examples include:

* Maven local repository (`~/.m2`)
* Gradle cache
* Node modules
* NuGet packages
* Cargo registry

The agent must not recursively inspect transitive dependencies.

The objective is only to understand the public APIs directly consumed by the repository.

---

## Rule 3 — No Downloads

The workflow is strictly read-only regarding external resources.

The agent and any sub-agents must never:

* download libraries
* install packages
* fetch remote repositories
* clone repositories
* access the internet to retrieve source code
* execute package managers

If required information is unavailable locally, it must be recorded as `Unknown`.

---

## Rule 4 — No Uploads

The workflow must never upload, transmit, publish, or share repository contents with external services.

This includes, but is not limited to:

* file uploads
* cloud storage
* external APIs
* issue trackers
* messaging platforms
* remote services

No repository information may leave the local environment unless the user explicitly authorizes it.

---

## Rule 5 — No Git Operations

The workflow must never execute Git operations that modify or publish repository history.

Forbidden operations include, but are not limited to:

* `git push`
* `git pull`
* `git fetch`
* `git merge`
* `git rebase`
* `git commit`
* `git tag`
* `git cherry-pick`

Version control operations remain the responsibility of the developer unless explicitly requested.

---

## Rule 6 — Secret Protection

The agent must never expose secrets in generated artifacts, logs, summaries, or AI-Context files.

This includes, but is not limited to:

* API keys
* access tokens
* passwords
* certificates
* connection strings
* credentials
* environment secrets
* cryptographic material

If a secret is encountered, it must be ignored or replaced with `[REDACTED]`.

---

## Rule 7 — Controlled Output

The workflow may generate or update only files defined by the AI Context Generation specification.

No additional files, folders, temporary artifacts, or reports may be created outside the predefined `AI-Context` structure.

---

## Rule 8 — Read-Only Repository

The workflow is read-only with respect to the project.

The only files that may be created, modified, or removed are those inside the `AI-Context` directory.

The workflow must never modify:

* source code
* tests
* build files
* configuration
* documentation
* project metadata
* any other repository artifact

unless the user explicitly requests it.

---

## Rule 9 — No Code Execution

The workflow is strictly observational.

The agent and any sub-agents must never execute project code or scripts.

Examples include:

* shell scripts
* Python scripts
* Java applications
* Node.js programs
* Gradle
* Maven
* npm
* pnpm
* yarn
* Docker
* Make
* test runners
* build tools
* any executable command

Repository inspection must be performed without executing project code.

---

## Rule 10 — Safety

Whenever there is uncertainty about whether an action violates these rules, the workflow must stop and ask the user.

The workflow must always prefer incomplete documentation over incorrect documentation.

---

# Supported Commands

## `initialize`

Create the `AI-Context` directory from the current state of the repository.

## `generate`

Alias for `initialize`.

## `update`

Update the existing `AI-Context` directory using the current repository state and the requested or detected changes.

---

# General Rules

1. Inspect the repository before generating or updating context.
2. Treat source code, tests, configuration, migrations, API contracts, and existing documentation as evidence.
3. Clearly mark uncertainty with `Unknown`, `Not confirmed`, or `Needs clarification`.
4. Prefer precise references to modules, packages, classes, functions, routes, events, tables, and tests.
5. Keep the generated context useful for future AI agents that have never seen the repository.
6. Do not copy large portions of source code into the context.
7. Summarize behavior, constraints, intent, and relationships instead of implementation details.
8. Preserve valid existing context during updates.
9. Record meaningful changes in `AI-Context/change-log.md`.
10. Record unresolved findings in `AI-Context/open-questions.md`.
11. Use the templates under `templates/AI-Context` as the required output structure.

---

# Evidence Priority

When sources conflict, use the following priority:

1. Executable tests
2. Running behavior and public contracts
3. Current source code
4. Database migrations and schemas
5. Configuration
6. Architecture decision records
7. Current project documentation
8. Comments
9. Naming-based inference

Never invent business rules or architectural decisions.

When uncertainty remains, document it instead of guessing.

---

# Completion Requirements

A workflow is complete only when:

* Every required `AI-Context` file exists.
* Each file contains repository-specific information or explicitly states that the information is unavailable.
* `manifest.json` is valid JSON.
* Cross-file terminology is consistent.
* Open uncertainties are documented.
* The final response summarizes the created or updated files and the most important findings.
