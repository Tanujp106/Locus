---
name: organizing-agent-skills
description: Use when creating or extending a Locus skill or plugin and deciding where SKILL.md, evals, references, examples, scripts, assets, host metadata, hooks, or MCP configuration should live.
---

# Organizing Agent Skills

## Overview

Keep one canonical, portable workflow inside the plugin that owns its domain. Use this guide before creating files so the skill stays self-contained and ready for evaluation or distribution.

## Placement workflow

1. Choose the owning domain plugin, such as `design`, `development`, or `seo`.
2. Create `plugins/<plugin>/skills/<skill>/SKILL.md`, the portable workflow contract. Keep it focused on activation, procedure, constraints, and verification.
3. Add only needed supporting directories. Do not create empty folders, a skill-level `README.md`, or a second root-level `skills/` source.
4. Keep references and helpers self-contained. Do not depend on sibling plugins or paths outside the skill.

## Placement matrix

| Need | Location | Put there |
| --- | --- | --- |
| Core workflow | `SKILL.md` | Instructions another agent must read |
| Long or conditional guidance | `references/` | API notes, domain rules, patterns, and edge cases |
| Deterministic automation | `scripts/` | Self-contained executable helpers |
| Illustrative output | `examples/` | Representative completed outputs or usage examples |
| Copyable output resource | `assets/` | Templates, boilerplate, icons, images, fonts, or final-artifact files |
| Behavioral test cases | `evals/evals.json` | Prompts and assertions |
| Eval fixtures | `evals/files/` | Input files referenced by the eval manifest |
| Generated eval runs | `evals-workspace/iteration-N/` | Reports, transcripts, scores, and temporary outputs; ignored and outside the skill |
| Codex UI metadata | `agents/openai.yaml` | Host-specific display name, blurb, and default prompt |

Use `SKILL.md` or `references/` for instructions. Use `assets/` for files copied or modified into a deliverable, and `examples/` for files that only demonstrate an outcome.

## Plugin-level integrations

Keep integrations outside portable skill instructions:

- `plugins/<plugin>/.mcp.json`: plugin MCP server configuration.
- `plugins/<plugin>/hooks/`: plugin hooks and their supporting scripts.
- `plugins/<plugin>/agents/` or `commands/`: plugin-level host surfaces when required.
- Native marketplace manifests: add only when distribution is required; they adapt the canonical plugin.

Do not invent a universal `ui/metadata.json`. Use the host adapter supported by the target runtime, such as a skill-local `agents/openai.yaml` for Codex.

## Before publishing

- Confirm the skill name is lowercase kebab-case and matches its directory.
- Check that every referenced file is inside the skill or documented plugin surface.
- Add representative, edge, invalid-input, and regression cases to `evals/evals.json` when behavior is stable enough to protect.
- Run the repository tests, skill validator, and `git diff --check`.

## Example layout

```text
plugins/design/
├── README.md
└── skills/new-skill/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── evals/evals.json
    ├── references/
    ├── examples/
    ├── scripts/
    └── assets/
```

Omit unused directories. Keep generated evaluation workspaces at the repository root, not inside this tree.
