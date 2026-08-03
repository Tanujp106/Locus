import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_skills.py"


def write_skill(root: Path, name: str = "sample-skill", *, mismatch: bool = False) -> None:
    skill_dir = root / "plugins" / "design" / "skills" / name
    (skill_dir / "evals" / "files").mkdir(parents=True)
    skill_name = "different-name" if mismatch else name
    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {skill_name}\ndescription: Use when evaluating a sample workflow.\n---\n\n# Sample\n\nFollow the workflow.\n",
        encoding="utf-8",
    )
    (skill_dir / "evals" / "evals.json").write_text(
        json.dumps(
            {
                "skill_name": name,
                "evals": [
                    {
                        "id": "basic",
                        "prompt": "Run the sample workflow.",
                        "assertions": ["The workflow is followed."],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )


class ValidateSkillsTests(unittest.TestCase):
    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(root)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_accepts_valid_skill_and_eval_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_skill(root)

            result = self.run_validator(root)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("1 skill", result.stdout)

    def test_rejects_skill_name_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_skill(root, mismatch=True)

            result = self.run_validator(root)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("must match its directory", result.stderr)


if __name__ == "__main__":
    unittest.main()
