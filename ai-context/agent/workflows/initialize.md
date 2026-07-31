# Initialize Workflow

## Command

`initialize`

Alias: `generate`

## Goal

Create a complete initial `ai-context` knowledge base from the current project.

## Procedure

### 1. Discover the repository

Inspect:

- Top-level directories and files
- Build and dependency files
- Application entry points
- Main modules and packages
- Tests
- API definitions
- Database schemas and migrations
- Configuration
- Existing documentation
- CI/CD definitions
- Git history when available and useful

### 2. Identify the project boundary

Determine:

- What the system does
- Who or what uses it
- Main business capabilities
- Main runtime components
- External systems
- Persistence mechanisms
- Deployment model
- Supported environments

### 3. Extract business context

Identify:

- Business goals
- Domain concepts
- Actors
- Business rules
- Validations
- State transitions
- Important workflows
- Error and exception behavior

Do not infer business intent solely from names when there is insufficient
evidence.

### 4. Extract technical context

Identify:

- Architecture style
- Module boundaries
- Dependency direction
- Integration patterns
- Design patterns
- Coding conventions
- Error-handling conventions
- Observability approach
- Security boundaries
- Data ownership

### 5. Extract testing context

Identify:

- Test frameworks
- Unit-test conventions
- Integration-test conventions
- Functional or end-to-end tests
- Fixtures and test data
- Mocking strategy
- Naming conventions
- Coverage expectations when explicitly defined
- Commands used to run tests

### 6. Generate `ai-context`

Create every file defined in `ai-context/agent/templates/`, written as
siblings of `ai-context/agent/` (for example `ai-context/architecture.md`,
not `ai-context/agent/architecture.md`).

Replace template guidance with repository-specific content. Keep section
headings unless they are demonstrably irrelevant.

For every countable artifact (entities, endpoints, test files, external
clients, enum values), produce the list by `grep`/`find` across the relevant
directory — never by sampling a few representative examples (AGENTS.md
Rule 13).

Tag every non-trivial claim with its provenance — `[VERIFIED: ...]`,
`[POLICY: ...]`, or `[Not confirmed]` (Rule 11). Where a fact would
otherwise need to be restated in more than one file, write it once in its
canonical file and link to it from the others (Rule 12).

Populate `manifest.json`'s `topics` map so each topic points at its one or
two canonical files (Rule 16).

### 7. Validate consistency

Check that:

- Feature names match domain terminology.
- Architecture descriptions match actual dependency direction.
- Testing descriptions match existing tests.
- Decisions do not contradict source code.
- Unknowns are recorded in `open-questions.md`.
- `manifest.json` lists every generated context file and its `topics` map is
  complete.
- No fact is restated in more than one file (Rule 12) — grep the draft files
  for repeated claims before finishing.
- Every claim carries a provenance tag (Rule 11).

### 8. Report completion

Return:

- Files created
- Main business capabilities discovered
- Main architectural findings
- Main testing findings
- Important uncertainties
- Recommended next clarification points

## Prohibited behavior

- Do not change production code unless explicitly requested.
- Do not refactor while generating context.
- Do not fabricate missing requirements.
- Do not remove existing documentation outside `ai-context`.
