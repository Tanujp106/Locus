# Contributing to Locus

Locus is currently a personal collection, but its structure is designed to remain understandable if it becomes public.

## Adding a plugin

Create a focused directory under `plugins/` and add a README describing its purpose, included skills, requirements, and integrations.

## Adding a skill

Create:

```text
plugins/<plugin-name>/skills/<skill-name>/SKILL.md
```

Add `references/`, `examples/`, `scripts/`, `assets/`, and `evals/` only when they support the skill. Keep the skill name lowercase kebab-case and make the description explain when it should activate.

## Required checks

```bash
python3 -m unittest discover -s tests
python3 scripts/validate_skills.py .
git diff --check
```

Do not commit secrets, private transcripts, generated eval workspaces, or unreviewed executable integrations.
