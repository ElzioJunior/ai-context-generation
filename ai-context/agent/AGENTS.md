# AI Context Agent Instructions

## Purpose

This repository uses an `ai-context` directory as the canonical AI-readable knowledge base for the project's business rules, architecture, development standards, testing approach, features, decisions, and terminology.

These instructions, the `workflows/`, `templates/`, and `scripts/` directories live in `ai-context/agent/` — that subfolder is the tool itself, copied in as-is. The knowledge base you create or update belongs in `ai-context/`, as siblings of `agent/` (for example `ai-context/architecture.md`, not `ai-context/agent/architecture.md`).

You are responsible for creating and maintaining that knowledge base whenever the user requests `initialize`, `generate`, or `update`.

---

# Governance Rules

These governance rules are mandatory for every workflow.

They take precedence over all workflow instructions and must not be bypassed unless the user explicitly authorizes a specific exception.

## Architecture Decision Records (ADRs)

Before executing any workflow, read every Architecture Decision Record (ADR)
under the `ADR/` directory.

ADRs define the architectural principles, long-term design decisions, and
constraints of AI Context Generation.

When an ADR conflicts with an implementation detail, the ADR takes precedence
unless a newer ADR explicitly supersedes it.

When introducing a new architectural decision that is not covered by an
existing ADR, propose creating a new ADR instead of silently changing the
architecture.

## Context Resolution Strategy

For every request:

1. Read the AI-Context before inspecting the repository.
2. Classify the request as either:
  - Knowledge Task
  - Implementation Task
3. Knowledge Tasks must rely on AI-Context whenever possible.
4. Implementation Tasks may inspect source code only after consulting AI-Context.
5. Repository traversal must always be minimized.
6. When implementation and AI-Context differ, treat the implementation as the current source of truth and recommend updating the AI-Context.

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

The agent must never expose secrets in generated artifacts, logs, summaries, or ai-context files.

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

No additional files, folders, temporary artifacts, or reports may be created outside the predefined `ai-context` structure. `ai-context/agent/` is the tool's own instruction bundle, not output — never create or modify files there.

---

## Rule 8 — Read-Only Repository

The workflow is read-only with respect to the project.

The only files that may be created, modified, or removed are those inside the `ai-context` directory, excluding `ai-context/agent/` (Rule 7).

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

This rule governs the *target* repository's own code and build tooling
(what the workflow is documenting). It does not prohibit running
`ai-context/agent/scripts/validate_context.py` — that script is part of the
AI Context Generation tool itself, performs read-only deterministic checks
over the generated `ai-context` directory, and is not project code under
inspection.

---

## Rule 10 — Safety

Whenever there is uncertainty about whether an action violates these rules, the workflow must stop and ask the user.

The workflow must always prefer incomplete documentation over incorrect documentation.

---

## Rule 11 — Provenance Tagging

Every non-trivial factual claim written into a canonical `ai-context` file must carry one of these tags:

* `[VERIFIED: <path>:<line-or-range>@<commit-sha>]` — read directly from current source, tests, config, or schema, anchored to the commit it was verified against. The commit SHA lets a later run detect staleness mechanically (has `<path>` changed since `<commit-sha>`?) instead of trusting the tag forever.
* `[POLICY: <path>]` — asserted by a prescriptive document (for example a root-level `CLAUDE.md` or `AGENTS.md` in the target repository) but not independently confirmed against the current source tree.
* `[Not confirmed]` — no evidence found anywhere; must also have a matching entry in `open-questions.md`.

A `POLICY` claim must never be written as if it were `VERIFIED`. If a `POLICY` claim and the actual source disagree, document both and record the contradiction in `open-questions.md` instead of silently preferring one.

This rule exists because an agent once wrote a repository's mandated-but-unimplemented layering rule into four context files as observed fact. Tagging it `[POLICY: ...]` from the start would have made the gap visible immediately instead of requiring a manual audit to find it later.

---

## Rule 12 — Single Source of Truth

Each fact — a business rule, an entity's fields, a pattern's participants, an architectural decision — has exactly one canonical file. Any other file that needs the fact links to it (for example "see `business-context.md` RULE-002") instead of restating its content. A one-line pointer is acceptable; a full redefinition is not.

Duplicated facts drift independently: a correction applied to one copy can silently leave others wrong. This has happened in practice — a correction landed in one canonical file but was missed in three others that had independently restated the same fact, and the mismatch was only caught by accident during unrelated work.

---

## Rule 13 — Exhaustive Enumeration for Countable Artifacts

Anything enumerable — entities, endpoints, test files, external clients, enum values — must be produced by an exhaustive listing (`grep`/`find` across the relevant directory), never by sampling representative examples. Prose summaries remain appropriate for behavior and intent; they are not a substitute for a complete list when the question is "how many" or "which ones."

This rule exists because a domain-model file once documented only a fraction of the actual entity classes in a repository because the generator sampled instead of enumerating.

---

## Rule 14 — Cross-File Consistency Sweep

Before an `update` run reports completion, search every `ai-context` file for the term(s)/entity/pattern name touched by the update — not only the file(s) already edited. If the term appears elsewhere with contradicting or stale content, fix it in the same pass. Do not defer this to "a future update will touch that file" — that is how the drift described in Rule 12 persisted undetected across multiple files.

---

## Rule 15 — Git-History Read Scope

Rule 5 already forbids any git operation that writes or publishes history. Within that boundary, read-only history inspection (`git log`, `git blame`, `git show`) should be used specifically when:

* A decision's rationale is missing from `decisions.md` — check the commit or PR that introduced the change.
* A TODO or comment's currency is in question — check when it was added and whether the condition it references has since changed.
* A pattern's "legacy" or "mandatory" status needs confirmation — check whether recent commits extend it or move away from it.

Do not reach for git history when current source already answers the question directly (for example, an entity's current fields) — that is a redundant read that inflates generation cost without improving precision.

---

## Rule 16 — Topic Routing in `manifest.json`

`manifest.json` must include a `topics` map from question/topic keywords to the one or two canonical files that answer them (for example `"testing": ["testing-strategy.md"]`, `"entities": ["domain-model.md"]`). This lets a consuming agent read only the files relevant to its question instead of the entire knowledge base.

---

# Supported Commands

## `initialize`

Populate the `ai-context` directory (as siblings of the existing `ai-context/agent/` folder) from the current state of the repository.

## `generate`

Alias for `initialize`.

## `update`

Update the existing `ai-context` directory using the current repository state and the requested or detected changes.

---

# General Rules

1. Inspect the repository before generating or updating context.
2. Treat source code, tests, configuration, migrations, API contracts, and existing documentation as evidence.
3. Clearly mark uncertainty with `Unknown`, `Not confirmed`, or `Needs clarification`.
4. Prefer precise references to modules, packages, classes, functions, routes, events, tables, and tests.
5. Keep the generated context useful for future AI agents that have never seen the repository.
6. Do not copy large portions of source code into the context.
7. Summarize behavior, constraints, intent, and relationships instead of implementation details — except for countable artifacts (Rule 13), which must be enumerated exhaustively, not sampled.
8. Preserve valid existing context during updates.
9. Record meaningful changes in `ai-context/change-log.md`.
10. Record unresolved findings in `ai-context/open-questions.md`.
11. Use the templates under `ai-context/agent/templates` as the required output structure.
12. Tag every non-trivial claim with its provenance (Rule 11) and write each fact in exactly one canonical file (Rule 12).
13. Write terse, declarative sentences. Omit narrative or connective filler ("It should be noted that...", "This is important because...") and do not restate the question or section heading in prose — a consuming agent pays token cost for every word regenerated here, on every future read.
14. Architectural decisions must always comply with the existing ADRs. Never introduce a new architectural direction that contradicts an ADR unless explicitly requested by the user.

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

* Every required `ai-context` file exists.
* Each file contains repository-specific information or explicitly states that the information is unavailable.
* `manifest.json` is valid JSON and its `topics` map (Rule 16) reflects any new or renamed file.
* Cross-file terminology is consistent.
* Every claim added or changed carries a provenance tag (Rule 11).
* No fact touched by this run is left duplicated across files without being reconciled to a single canonical source (Rule 12).
* Open uncertainties are documented.
* `ai-context/agent/scripts/validate_context.py` has been run against the generated `ai-context` directory and every reported `ERROR` is resolved. If
  the script is not present, note that explicitly in the completion report instead of skipping the check silently.
* The final response summarizes the created or updated files and the most important findings.
* Existing ADRs remain respected throughout the workflow.
* If the workflow reveals a new architectural decision that should be preserved for future development, recommend creating a new ADR.
