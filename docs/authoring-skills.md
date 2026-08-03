# Authoring Skills

## Minimum contract

Every skill has a `SKILL.md` with YAML frontmatter containing `name` and `description`.

```yaml
---
name: example-skill
description: Use when a task requires the example workflow or its specific output format.
license: MIT
compatibility: Requires access to the project files.
---
```

Use lowercase kebab-case names. Make the description describe activation conditions, not the entire workflow.

## Progressive disclosure

- Keep the main workflow in `SKILL.md`.
- Move detailed patterns, API notes, and edge cases to `references/`.
- Put complete working examples in `examples/`.
- Put deterministic helpers in `scripts/`.
- Put output templates and supporting files in `assets/`.

Create only the directories the skill needs. Keep referenced paths relative to the skill root and never use `../` to reach another plugin.

## Skill quality

Before publishing a skill, test it on representative tasks, edge cases, and failure cases. Add `evals/evals.json` once the skill has a stable behavior worth protecting.
