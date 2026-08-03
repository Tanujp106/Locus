# Locus Architecture

## Core model

- A skill is a self-contained, portable workflow centered on `SKILL.md`.
- A plugin is a focused domain bundle containing related skills.
- A marketplace is a distribution index, not the authoring source.

## Canonical layout

```text
plugins/design/
├── README.md
└── skills/
    └── design-system-audit/
        ├── SKILL.md
        ├── evals/
        ├── references/
        ├── examples/
        ├── scripts/
        └── assets/
```

Do not create a second top-level skill source. Keep each skill inside the plugin that owns its domain.

## Distribution adapters

When a plugin is ready for native distribution, add the platform-specific manifests without moving its `skills/` directory:

```text
.claude-plugin/marketplace.json
.agents/plugins/marketplace.json
plugins/<name>/.claude-plugin/plugin.json
plugins/<name>/.codex-plugin/plugin.json
```

Keep native metadata out of `SKILL.md` unless the field is supported by the portable Agent Skills format.

## Optional plugin surfaces

Add `agents/`, `commands/`, `hooks/`, `.mcp.json`, `.lsp.json`, `bin/`, or `settings.json` only when a real plugin capability requires them. Each integration needs documentation, security review, and a smoke test.
