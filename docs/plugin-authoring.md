# Plugin Authoring

A plugin should have one focused purpose and contain a small, composable set of related skills.

```text
plugins/<plugin-name>/
├── README.md
├── skills/
├── agents/       # optional
├── commands/     # optional
├── hooks/        # optional
└── .mcp.json     # optional
```

The plugin README should document its purpose, included skills, requirements, permissions, integrations, and local verification steps.

Do not add hooks or MCP simply because the format permits them. Add them when a repeatable workflow cannot be expressed reliably through instructions and deterministic scripts alone.

All plugin-local executable surfaces need a security review and a smoke test. External sources should be pinned to a tag or commit where practical.
