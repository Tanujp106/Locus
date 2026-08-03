#!/usr/bin/env python3
"""Validate portable Agent Skills stored in Locus plugins."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing YAML frontmatter"]

    fields: dict[str, str] = {}
    closing = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing = index
            break
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line or line.startswith((" ", "\t")):
            errors.append(f"{path}:{index + 1}: invalid frontmatter line")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")

    if closing is None:
        errors.append(f"{path}: frontmatter is not closed")
    elif not any(line.strip() for line in lines[closing + 1 :]):
        errors.append(f"{path}: skill body is empty")
    return fields, errors


def validate_eval_manifest(skill_dir: Path, skill_name: str) -> list[str]:
    manifest = skill_dir / "evals" / "evals.json"
    if not manifest.exists():
        return []

    errors: list[str] = []
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return [f"{manifest}: invalid JSON ({error})"]

    if data.get("skill_name") != skill_name:
        errors.append(f"{manifest}: skill_name must be {skill_name!r}")
    cases = data.get("evals")
    if not isinstance(cases, list) or not cases:
        errors.append(f"{manifest}: evals must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            errors.append(f"{manifest}: every eval must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{manifest}: every eval needs a non-empty id")
        elif case_id in seen_ids:
            errors.append(f"{manifest}: duplicate eval id {case_id!r}")
        else:
            seen_ids.add(case_id)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{manifest}: eval {case_id!r} needs a prompt")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            errors.append(f"{manifest}: eval {case_id!r} needs assertions")
        for relative_file in case.get("files", []):
            if not isinstance(relative_file, str):
                errors.append(f"{manifest}: eval {case_id!r} has a non-string file")
                continue
            candidate = (skill_dir / relative_file).resolve()
            if skill_dir.resolve() not in candidate.parents:
                errors.append(f"{manifest}: eval {case_id!r} escapes the skill directory")
            elif not candidate.exists():
                errors.append(f"{manifest}: eval file does not exist: {relative_file}")
    return errors


def validate_skill(skill_file: Path) -> list[str]:
    skill_dir = skill_file.parent
    folder_name = skill_dir.name
    fields, errors = parse_frontmatter(skill_file)
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append(f"{skill_file}: missing required name")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_file}: name must be lowercase kebab-case")
    elif len(name) > 64:
        errors.append(f"{skill_file}: name exceeds 64 characters")
    elif name != folder_name:
        errors.append(f"{skill_file}: name must match its directory ({folder_name!r})")

    if not description:
        errors.append(f"{skill_file}: missing required description")
    elif len(description) > 1024:
        errors.append(f"{skill_file}: description exceeds 1024 characters")

    if "../" in skill_file.read_text(encoding="utf-8"):
        errors.append(f"{skill_file}: references must not escape the skill directory")

    if name:
        errors.extend(validate_eval_manifest(skill_dir, name))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    skill_files = sorted(root.glob("plugins/*/skills/*/SKILL.md"))
    errors = [error for skill_file in skill_files for error in validate_skill(skill_file)]

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    count = len(skill_files)
    print(f"Validated {count} skill{'s' if count != 1 else ''}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
