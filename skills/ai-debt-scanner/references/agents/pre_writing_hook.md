# Pre-Writing Hook (The Auditor's Guardrail)

## Mission
Act as a lightweight guardrail before code is written or modified. Your goal is to prevent obvious debt without turning small changes into research-heavy loops.

## Checklist
Use the shortest checklist that safely fits the task.

### Quick Check
Run this for small, local edits:
1. What file or boundary is being changed?
2. Does the change fit this file/module, or is it crossing a boundary that should stay separate?
3. Am I introducing obvious debt: swallowed errors, unchecked inputs, hidden globals, duplication, or dead code?
4. Am I matching the local style and naming conventions?

### Standard Check
Add these only when the change spans multiple files or contracts:
1. What runtime, framework, or toolchain details actually matter for this change?
2. Which contracts, schemas, APIs, or generated boundaries are affected?
3. Do I need one adjacent file of context before editing?

### Deep Check
Use only for architecture-sensitive work:
1. Which trust boundaries or execution surfaces are involved?
2. Is there a repo-wide convention or rule that must be reconciled first?
3. Would editing now be reckless without a broader plan?

## Protocol
If the Quick Check passes, edit the code.
If the Standard or Deep Check reveals cross-cutting risk, expand context deliberately, not recursively.
Do not block a small fix on repo-wide analysis unless the evidence points to repo-wide risk.
