# Locus Agent Instructions

Locus is a portable collection of reusable Agent Skills and domain plugins.

## Repository rules

- Keep `AGENTS.md` and `CLAUDE.md` focused on repository governance; put domain behavior in skills.
- Treat `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` as the canonical skill layout.
- Keep skills self-contained. Do not reference files outside a skill or plugin with `../` paths.
- Use progressive disclosure: keep `SKILL.md` focused and move detail to `references/`.
- Add `evals/evals.json` for behavioral cases and keep generated runs in ignored `evals-workspace/`.
- Add hooks, MCP, agents, or commands only when a real workflow needs them.
- Never commit secrets, private memory, generated model transcripts, or credentials.

## Validation

Run:

```bash
python3 -m unittest discover -s tests
python3 scripts/validate_skills.py .
git diff --check
```

Before publishing, inspect the complete diff and verify the configured GitHub remote and branch.
