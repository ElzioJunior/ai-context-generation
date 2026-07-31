# Update Workflow

## Command

`update`

## Goal

Synchronize the existing `ai-context` knowledge base with new repository
changes while preserving valid prior knowledge.

## Inputs

Use all available evidence:

- User description of the new feature or change
- Current working tree
- Git diff
- Relevant commits (read-only — see AGENTS.md Rule 15 for when git history
  specifically resolves a precision gap: missing decision rationale,
  TODO/comment currency, legacy-pattern status)
- Updated tests
- Updated contracts
- Updated migrations
- Existing `ai-context`

## Procedure

### 1. Determine the change scope

Identify whether the change affects:

- Business behavior
- Domain terminology
- Domain model
- Architecture
- Public APIs
- Persistence
- Integrations
- Design patterns
- Coding standards
- Testing strategy
- Feature catalog
- Decisions
- Open questions

### 2. Inspect the implementation

Read the changed and related files. Do not rely only on the user-provided
description.

Inspect tests as first-class evidence.

### 3. Compare against existing context

For each affected context file, classify information as:

- Still valid
- Modified
- Added
- Removed
- Uncertain
- Contradictory

### 4. Update only what changed

Preserve valid content. Avoid rewriting unrelated sections.

When a behavior is removed, update all affected references and record the
removal in the change log.

Tag every added or changed claim with its provenance (Rule 11). If the
change corrects a fact that also appears elsewhere (Rule 12), fix the
canonical copy and convert the others to a link — do not leave a second,
now-divergent restatement in place.

### 4a. Cross-file consistency sweep

Before continuing to step 5, search every `ai-context` file for the
term(s), entity, or pattern name touched by this update — not only the
file(s) already edited. If the term appears elsewhere with contradicting or
stale content, fix it in this same pass (Rule 14). A fix that lands in only
one file, while the same fact sits stale in others, is not complete.

### 5. Update the feature catalog

For a new or changed feature, document:

- Feature name
- Purpose
- Actors
- Trigger
- Main flow
- Business rules
- Inputs and outputs
- Failure behavior
- Related modules
- Related tests
- Known limitations

If the feature adds or changes a countable artifact (endpoints, entities,
enum values), enumerate it exhaustively via `grep`/`find` rather than listing
only the examples the user mentioned (Rule 13).

### 6. Update decisions and questions

Add or revise decisions when the implementation introduces a meaningful
architectural or business choice.

Move resolved questions out of `open-questions.md` and reflect their answers in
the relevant canonical file.

### 7. Update the change log

Add a dated entry containing:

- Change summary
- Context files affected
- Evidence inspected
- Decisions added or changed
- Questions opened or resolved

### 8. Validate consistency

Ensure that terminology, features, architecture, and tests remain aligned
across every context file. Confirm the cross-file sweep (step 4a) found no
remaining duplicate or contradicting copies of the changed fact, and that
`manifest.json`'s `topics` map still points to the correct canonical file if
a fact moved.

### 9. Report completion

Return:

- Files updated
- New knowledge captured
- Existing knowledge changed
- Contradictions found
- Questions requiring human confirmation

## Prohibited behavior

- Do not regenerate every file unnecessarily.
- Do not erase valid historical decisions.
- Do not describe planned behavior as implemented behavior.
- Do not claim tests exist unless they are present.
