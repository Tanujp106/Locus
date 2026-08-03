# Evaluating Skills

Evaluations measure whether a skill improves agent behavior, not whether its Markdown merely parses.

## Skill-local cases

Store stable cases beside the skill:

```text
skills/example-skill/evals/
├── evals.json
├── files/
└── rubric.md
```

Example manifest:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": "basic-workflow",
      "prompt": "Run the example workflow.",
      "assertions": [
        "The required output is produced.",
        "The workflow does not skip validation."
      ]
    }
  ]
}
```

## Comparison model

Compare the same case with the skill loaded and without it, or against the previous skill version. Use assertions for deterministic requirements and a human rubric for subjective work such as design, writing, and SEO.

Keep generated outputs, timing data, model transcripts, and HTML reports in ignored `evals-workspace/iteration-N/` directories.

## Coverage

Prefer a small representative suite:

- common workflow
- edge case
- invalid or incomplete input
- ambiguity or conflicting requirements
- regression case from a previous failure
