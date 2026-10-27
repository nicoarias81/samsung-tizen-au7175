#!/usr/bin/env python3
"""Validate committed profile, plan and verification evidence."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODEL = "UE55AU7175UXXC"
BUILD = "T-KSU2EDEUC-REL-202607211851"


def main():
    profile = json.loads((ROOT / "profiles/ue55au7175uxxc-202607211851.json").read_text(encoding="utf-8"))
    before = json.loads((ROOT / "plans/phase1-advertising-tvplus/before.json").read_text(encoding="utf-8"))
    after = json.loads((ROOT / "plans/phase1-advertising-tvplus/verified-after.json").read_text(encoding="utf-8"))
    assert profile["model"] == before["model"] == after["model"] == MODEL
    assert profile["firmware"] == before["firmware"] == after["build"] == BUILD
    expected = set(profile["groups"]["advertising"]["app_ids"] + profile["groups"]["tv-plus"]["app_ids"])
    assert {x["app_id"] for x in before["apps"]} == expected
    assert {x[0] for x in after["rows"]} == expected
    assert all(x[1:] == ["true", "false", "false"] for x in after["rows"])
    for name in ("apply.sh", "restore.sh", "restore-tvplus-autorun.sh"):
        data = (ROOT / "plans/phase1-advertising-tvplus" / name).read_bytes()
        assert b"\r\n" not in data, f"{name} must use LF"
    print(f"OK: {len(expected)} apps, identity guards and LF scripts verified")


if __name__ == "__main__":
    main()
