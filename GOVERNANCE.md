# AI Context Generation Governance

## Purpose

This document defines mandatory governance rules for every AI agent executing
the AI Context Generation workflow.

These rules are mandatory.

No workflow, prompt, or user instruction may silently override them unless the
user explicitly states that a specific rule may be bypassed.

---

# Rule 1 — Repository Boundary

The agent must remain strictly inside the current repository.

The repository root is the maximum allowed traversal boundary.

The agent must not inspect:

- sibling repositories
- parent directories
- unrelated workspaces
- the user's home directory
- global configuration directories
- caches
- temporary directories

If external access appears necessary, the agent must stop and request explicit
authorization.

---

# Rule 2 — Dependency Inspection

The agent may inspect direct project dependencies only.

Allowed examples include:

- Maven local repository (`~/.m2`)
- Gradle local cache
- Node modules
- NuGet packages
- Cargo registry

Only dependencies directly declared by the current project may be inspected.

The agent must not recursively inspect transitive dependencies.

Example:

Project
├── Dependency A   ✅ allowed
├── Dependency B   ✅ allowed
└── Dependency A → Dependency X ❌ forbidden

The objective is only to understand the public APIs used by the current
repository.

---

# Rule 3 — No Downloads

The workflow is strictly read-only regarding external resources.

The agent must never:

- download libraries
- install packages
- execute package managers
- fetch remote repositories
- clone Git repositories
- access the internet to retrieve source code

If required information is unavailable locally, it must be recorded as
"Unknown".

---

# Rule 4 — Evidence First

All generated context must originate from observable evidence.

Evidence priority:

1. Tests
2. Source code
3. Configuration
4. Existing documentation

The agent must never invent business rules.

Unknown information must remain unknown.

---

# Rule 5 — Safety

When uncertain whether an action violates these rules,
the agent must stop and ask.

The workflow must always prefer incomplete documentation over incorrect
documentation.

# Rule 6 — No Uploads

The agent must never upload, transmit, publish, or share any project file,
source code, generated context, or repository information to external services.

This includes, but is not limited to:

- file uploads
- remote storage
- cloud services
- external APIs
- issue trackers
- messaging platforms

All processing must remain local unless the user explicitly authorizes a specific destination.

---

# Rule 7 — Secret Protection

The agent must never expose secrets in generated artifacts, logs, summaries,
or AI-Context files.

This includes, but is not limited to:

- API keys
- access tokens
- passwords
- private certificates
- connection strings
- credentials
- secrets stored in environment files
- cryptographic material

If a secret is encountered, it must be ignored or replaced with a placeholder
such as `[REDACTED]`.

---

# Rule 8 — Controlled Output

The workflow may generate or update only the files defined by the AI Context
Generation specification.

The agent must not create additional files, directories, reports, temporary
artifacts, or documentation outside the predefined AI-Context structure.

If new output is required, the workflow specification must be updated first.

---

# Rule 9 — No Code Execution

The workflow is strictly observational.

The agent and any sub-agents must never execute project code or scripts.

Forbidden examples include:

- shell scripts (`.sh`)
- Python scripts
- Node.js scripts
- Java programs
- Gradle
- Maven
- npm
- pnpm
- yarn
- Docker
- Makefiles
- test runners
- build tools
- any executable command

The workflow must inspect repository contents only.

No code execution is permitted.