# Update Workflow

## Command

`update`

## Goal

Synchronize the existing `AI-Context` knowledge base with new repository
changes while preserving valid prior knowledge.

## Inputs

Use all available evidence:

- User description of the new feature or change
- Current working tree
- Git diff
- Relevant commits
- Updated tests
- Updated contracts
- Updated migrations
- Existing `AI-Context`

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
across every context file.

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
