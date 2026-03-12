---
name: ai-debt-scanner
description: Advanced framework for detecting "vibe coding" and preventing AI-generated technical debt. Use when user asks to "scan for debt", "audit project", OR when asking to "write code", "implement feature", or "refactor" to act as a real-time architectural guardrail.
---

# AI Debt Scanner Framework

This skill transforms the AI agent into a specialized Technical Debt Auditor and Architect. It operates in two modes: **Audit Mode** (detecting existing debt) and **Guardrail Mode** (preventing debt during generation).

## Instructions

### Step 1: Setup & Git Hook Installation (PROACTIVE)
**CRITICAL:** At the start of a session or when detecting a git repository:
1. **Detect Hook**: Check if `.git/hooks/pre-commit` exists and contains "AI Debt Scanner".
2. **Proactive Suggestion**: If the hook is missing, briefly suggest its installation to the user: *"I noticed the AI Debt git hook isn't installed. Would you like me to set it up to audit your commits automatically?"*
3. **Automatic Setup**: If the user confirms, execute:
   ```bash
   cp templates/hooks/pre-commit-ai-debt.sh .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

### Step 2: Research Phase (Preventing Hallucinations)
Before auditing or generating code for a specific stack, eliminate ambiguity:
1. Identify the stack and its version.
2. Use the most appropriate tool for grounding:
   - **Google Search**: For official documentation and breaking changes.
   - **Specialized MCPs (e.g., Context7)**: For fast, up-to-date snippets.
   - **Native CLI tools**: To inspect local dependencies (`package.json`, `go.mod`, etc.).
3. **Dynamic Context Discovery**: Automatically adapt to project-specific laws in `AGENTS.md`, `.gga`, `GEMINI.md`, or `CLAUDE.md`.
4. **Artifact Fingerprinting is mandatory**: Inspect manifests, lockfiles, source layout, CI files, deployment descriptors, schema files, and tests to classify the repository by its actual execution surfaces and trust boundaries.
5. **No closed language list**: Treat detected artifacts as evidence, not as membership in a predefined catalog. Any repository must be audited with the same depth regardless of language, framework, VM, or toolchain.
6. **Run an equivalent audit depth across all code surfaces**: If multiple runtimes coexist, scan each with the same rigor instead of treating any non-dominant stack as "miscellaneous files".

### Step 2.1: Universal Audit Dimensions
After fingerprinting the repository, derive audit heuristics from these dimensions rather than from a hardcoded language matrix:

- **Error Semantics**
  - Detect swallowed failures, generic exception handling, ignored return values, panic/revert abuse, silent fallbacks, or success paths that hide partial failure.
- **Boundary Integrity**
  - Detect transport/domain/persistence/infrastructure mixed in one unit, layering leaks, hidden globals, and generated glue code that became business logic.
- **Type and Contract Integrity**
  - Detect type escapes, unvalidated inputs, schema drift, unsafe casts, dynamic dispatch used to bypass guarantees, and API contract divergence.
- **Security Posture**
  - Detect dangerous evaluation, injection vectors, unsafe deserialization, secret leakage, insecure defaults, broken auth assumptions, and trust-boundary violations.
- **Operational Safety**
  - Detect scripts or jobs that are non-idempotent, unsafe deployment logic, missing rollback or failure handling, and environment-specific drift.
- **Structural Complexity**
  - Detect god files, large functions, deep nesting, duplication, cognitive overload, accidental abstractions, and dead code.
- **State and Concurrency Discipline**
  - Detect race-prone shared state, missing transaction boundaries, inconsistent async flows, reentrancy-sensitive logic, and lifecycle side effects hidden in control flow.
- **Documentation and Intent**
  - Detect outdated docs, TODO placeholders, AI artifacts, misleading comments, and divergence between implementation and declared behavior.

### Step 3: Guardrail Mode (Live Prevention)
**CRITICAL:** When the user asks to implement a feature, write code, or refactor (and NOT just audit):
1. **Pre-Writing Hook**: Before modifying any file, you MUST follow the protocol in `./references/agents/pre_writing_hook.md` to ensure context alignment.
2. Apply the detection heuristics from `./references/rules.md` to your own generated code.
3. Ensure no new architectural violations, security smells, or "vibe coding" are introduced.

### Step 4: Audit Mode (Finding Debt)
When asked to explicitly scan or audit, execute the appropriate specialized mode:
- **Incremental Audit (`--diff`)**: Scans only files changed in the current git branch.
- **Prioritized Audit (`--top-k <N>`)**: Reports only the top `<N>` most critical offenders.
- **Full Audit**: Scans the entire project.

Apply detection heuristics (consult `./references/rules.md`):
1. **Critical**: Arch violations, Security smells, AI artifacts, Empty catch/except, `any` abuse.
2. **Structural Bloat**: Files > 300 lines or functions > 50 lines.
3. **Lazy Patterns**: SRP violations, DRY violations, cognitive overload.

### Step 5: Workflow Execution
1. **Scanner Agent**: Use `./references/agents/scanner.md` to identify hotspots, fingerprint repository artifacts, and apply contextual overrides.
2. **Architect Agent**: Use `./references/agents/architect.md` to map cross-file dependencies and identify layering leaks.
3. **Cleaner Agent**: Use `./references/agents/cleaner.md` to apply targeted fixes. **CRITICAL:** No refactor is applied without baseline and verification tests (Test-Driven Refactoring).
4. **Ruleset Source**: Use `./references/rules.md` as the canonical scoring model, deriving language-specific symptoms from universal audit dimensions rather than from a fixed list of languages.

### Step 6: Output Protocol (TOON)
When auditing, you MUST output findings in **TOON** (Token-Oriented Object Notation) format for surgical precision:
```json
{
  "summary": {
    "files_scanned": 0,
    "temperature": "Low|Moderate|High|Critical",
    "top_offenders": ["path/to/file"]
  },
  "vulnerabilities": [
    {
      "file": "path/to/file",
      "line": 123,
      "rule_id": "ARCH_VIOLATION|SRP_VIOLATION",
      "severity": "CRITICAL|WARNING|INFO",
      "description": "Clear explanation of the debt found"
    }
  ]
}
```

## Examples

### Example 1: Incremental Audit
User says: "Scan my current changes for debt"
Actions:
1. Verify git hook setup.
2. Run incremental audit on changed files.
3. Apply detection heuristics from `./references/rules.md`.
4. Output findings in TOON format.
Result: Structured JSON report of critical vulnerabilities in modified files.

### Example 2: Full Project Audit
User says: "Check the whole project for vibe coding"
Actions:
1. Ground knowledge using latest documentation for the project's stack.
2. Execute Architect Agent to map dependencies.
3. Report the top offenders using TOON format.
Result: High-level architectural review highlighting severe coupling or lazy patterns.

### Example 2b: Backend / Polyglot Audit
User says: "Escaneá también el backend, no solo el frontend"
Actions:
1. Fingerprint all repository artifacts and execution surfaces before scanning.
2. Run separate passes for product code, scripts, infrastructure, tests, and generated boundaries.
3. Apply equivalent heuristics from universal audit dimensions such as failure handling, boundary integrity, contract safety, and structural complexity.
4. Merge the findings into a single TOON report ranked by severity.
Result: The report reflects debt across the whole repository without overfitting to any specific language ecosystem.

### Example 3: Live Guardrail (Code Generation)
User says: "Implement a new user profile component"
Actions:
1. Trigger Guardrail Mode.
2. Run Pre-Writing Hook (`./references/agents/pre_writing_hook.md`).
3. Generate code adhering to architectural rules (no lazy patterns, no `any` abuse).
Result: Clean, tested code without introducing new technical debt.

## Troubleshooting

### Issue: Hallucinated API Methods (Vibe Coding)
**Cause**: The agent relied on outdated training data instead of verifying the current stack version.
**Solution**: Force a research step using Context7 MCP or Google Search for the specific framework version before proposing fixes.

### Issue: Overwhelming Output
**Cause**: A full audit on a large codebase returned too many results.
**Solution**: Switch to Prioritized Audit (`--top-k`) or Incremental Audit (`--diff`). Provide the TOON summary first before detailing vulnerabilities.

## Related Skills
- **component-refactoring**: Essential for splitting complex components.
- **react-doctor**: Use after refactoring to catch regressions.
- **clean-ddd-hexagonal**: For high-level architectural alignment.
- **anthropic-validator**: Validates the integrity of this and other skills.
