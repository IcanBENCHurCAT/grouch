import os
import re
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class TestGrouchSkill(unittest.TestCase):
    def setUp(self):
        self.skill_file = ROOT_DIR / "skills" / "grouch" / "SKILL.md"
        self.levels_file = ROOT_DIR / "skills" / "grouch" / "examples" / "levels.md"
        self.paste_file = ROOT_DIR / "PASTE.md"
        self.readme_file = ROOT_DIR / "README.md"
        self.license_file = ROOT_DIR / "LICENSE"

    def test_required_files_exist(self):
        self.assertTrue(self.skill_file.is_file(), "SKILL.md missing")
        self.assertTrue(self.levels_file.is_file(), "examples/levels.md missing")
        self.assertTrue(self.paste_file.is_file(), "PASTE.md missing")
        self.assertTrue(self.readme_file.is_file(), "README.md missing")
        self.assertTrue(self.license_file.is_file(), "LICENSE missing")

    def test_skill_frontmatter(self):
        content = self.skill_file.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---"), "SKILL.md must begin with frontmatter")
        
        # Simple frontmatter extractor
        parts = content.split("---", 2)
        self.assertGreaterEqual(len(parts), 3, "Frontmatter must be enclosed by ---")
        frontmatter = parts[1]
        
        name_match = re.search(r'name:\s*["\']?([^"\'\n]+)', frontmatter)
        self.assertIsNotNone(name_match, "Frontmatter must contain 'name'")
        self.assertEqual(name_match.group(1).strip(), "grouch")
        
        desc_match = re.search(r'description:\s*["\']?([^"\'\n]+)', frontmatter)
        self.assertIsNotNone(desc_match, "Frontmatter must contain 'description'")
        self.assertGreater(len(desc_match.group(1).strip()), 10)

    def test_levels_consistency(self):
        skill_text = self.skill_file.read_text(encoding="utf-8")
        levels_text = self.levels_file.read_text(encoding="utf-8")
        readme_text = self.readme_file.read_text(encoding="utf-8")
        paste_text = self.paste_file.read_text(encoding="utf-8")

        for level in ["low", "high", "oscar"]:
            self.assertIn(level, skill_text.lower(), f"Level '{level}' missing in SKILL.md")
            self.assertIn(level, levels_text.lower(), f"Level '{level}' missing in levels.md")
            self.assertIn(level, readme_text.lower(), f"Level '{level}' missing in README.md")
            self.assertIn(level, paste_text.lower(), f"Level '{level}' missing in PASTE.md")

    def test_no_em_dashes_in_skill(self):
        skill_text = self.skill_file.read_text(encoding="utf-8")
        # Contract states: no em dashes (—)
        self.assertNotIn("—", skill_text, "SKILL.md must not contain em dashes (—)")

    def test_paste_character_limits(self):
        paste_text = self.paste_file.read_text(encoding="utf-8")
        
        # Section 2: ChatGPT Custom Instructions (< 1500 chars limit)
        custom_instructions_match = re.search(
            r"## 2\. ChatGPT Custom Instructions.*?\n```text\n(.*?)\n```",
            paste_text,
            re.DOTALL
        )
        self.assertIsNotNone(custom_instructions_match, "ChatGPT instructions code block not found in PASTE.md")
        custom_instructions = custom_instructions_match.group(1)
        self.assertLessEqual(
            len(custom_instructions),
            1500,
            f"ChatGPT Custom Instructions snippet ({len(custom_instructions)} chars) exceeds 1500 chars limit"
        )

        # Section 1: 1-Turn Opener (< 500 chars)
        opener_match = re.search(
            r"## 1\. Instant 1-Turn Opener.*?\n```text\n(.*?)\n```",
            paste_text,
            re.DOTALL
        )
        self.assertIsNotNone(opener_match, "1-Turn Opener code block not found in PASTE.md")
        opener = opener_match.group(1)
        self.assertLessEqual(
            len(opener),
            500,
            f"1-Turn Opener snippet ({len(opener)} chars) exceeds 500 chars limit"
        )

if __name__ == "__main__":
    unittest.main()
