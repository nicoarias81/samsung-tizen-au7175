import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ArtifactTests(unittest.TestCase):
    def test_phase_one_exact_rows(self):
        profile = json.loads((ROOT / "profiles/ue55au7175uxxc-202607211851.json").read_text())
        evidence = json.loads((ROOT / "plans/phase1-advertising-tvplus/verified-after.json").read_text())
        expected = set(profile["groups"]["advertising"]["app_ids"] + profile["groups"]["tv-plus"]["app_ids"])
        self.assertEqual(expected, {row[0] for row in evidence["rows"]})
        self.assertEqual(11, len(evidence["rows"]))
        self.assertTrue(all(row[1:] == ["true", "false", "false"] for row in evidence["rows"]))

    def test_shell_files_are_lf(self):
        for script in (ROOT / "plans/phase1-advertising-tvplus").glob("*.sh"):
            self.assertNotIn(b"\r\n", script.read_bytes())

    def test_no_sensitive_capture_committed(self):
        forbidden = {".db", ".sqlite", ".log", ".dll"}
        found = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in forbidden and ".git" not in p.parts]
        self.assertEqual([], found)


if __name__ == "__main__":
    unittest.main()
