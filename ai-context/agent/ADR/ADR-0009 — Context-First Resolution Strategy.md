# ADR-0009 — Context-First Resolution Strategy

## Decision

Every AI task must begin by consulting the AI-Context directory.
The AI-Context is the primary source of project knowledge.
The repository must only be inspected when the requested task requires implementation details that are unavailable, incomplete, or outdated in the existing AI-Context.
When repository inspection is necessary, the agent must inspect only the minimum set of files required to complete the task.
If the implementation differs from the AI-Context, the implementation must be treated as the current source of truth, and the agent should recommend executing the update workflow to synchronize the knowledge base.

## Why

The purpose of AI Context Generation is not to prevent repository inspection, but to minimize it.
By starting with the AI-Context, AI agents avoid repeatedly rediscovering business rules, architecture, coding standards, and project knowledge that rarely change.
This reduces token consumption, execution time, and operational costs while allowing agents to inspect implementation details only when necessary to complete a task correctly.
