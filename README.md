# Locus

Locus is a personal, portable library of reusable Agent Skills organized into installable domain plugins.

The repository is designed around three layers:

1. `SKILL.md` is the portable workflow contract.
2. `plugins/<name>/` groups related skills into a focused domain bundle.
3. Claude Code and Codex marketplace manifests are distribution adapters added when a plugin is ready to publish.

## Repository map

```text
plugins/<plugin-name>/
├── README.md
└── skills/<skill-name>/
    ├── SKILL.md
    ├── evals/
    ├── references/
    ├── examples/
    ├── scripts/
    └── assets/
```

Start with [the architecture guide](docs/architecture.md), then read [skill authoring](docs/authoring-skills.md) and [evaluation guidance](docs/evaluating-skills.md).

## Validate locally

```bash
python3 -m unittest discover -s tests
python3 scripts/validate_skills.py .
git diff --check
```

## Current status

The repository foundation is intentionally portable-first. Native marketplace manifests, hooks, MCP servers, agents, and commands will be added only when a real plugin needs them.
