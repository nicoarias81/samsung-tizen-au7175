#!/usr/bin/env python3
"""Capture read-only post-reboot resource metrics over SDB."""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TARGETS = (
    "samsung-analytics|acr|canalysis|contents-recognition|adagent|pisa|"
    "targeted-ad|PromotionApp|tvplus"
)
MODEL = "UE55AU7175UXXC"


def load_vendor(path: Path):
    candidates = (path / "src", path / "vendor", path)
    for candidate in candidates:
        if (candidate / "samsung_tv_root").is_dir():
            sys.path.insert(0, str(candidate))
            break
    from samsung_tv_root.archive_root import _capture
    from samsung_tv_root.sdb import SdbClient, find_sdb
    return _capture, SdbClient, find_sdb


def parse(text: str):
    sections = {}
    current = None
    for line in text.splitlines():
        if line in {"memory", "load", "uptime", "targets"}:
            current = line
            sections[current] = []
        elif current:
            sections[current].append(line)
    mem_line = next((x for x in sections.get("memory", []) if x.strip().startswith("Mem:")), None)
    swap_line = next((x for x in sections.get("memory", []) if x.strip().startswith("Swap:")), None)
    if not mem_line or not swap_line:
        raise RuntimeError("No se pudo interpretar free -m")
    mem = list(map(int, mem_line.split()[1:]))
    swap = list(map(int, swap_line.split()[1:]))
    load = sections["load"][0].split()[:3]
    uptime = float(sections["uptime"][0].split()[0])
    processes = []
    for line in sections.get("targets", []):
        match = re.match(r"\s*(\d+)\s+(\d+)\s+(\S+)\s+(.*)", line)
        if match:
            processes.append({"pid": int(match[1]), "rss_kib": int(match[2]), "comm": match[3], "args": match[4]})
    return {
        "memory_mib": {"total": mem[0], "used": mem[1], "free": mem[2], "shared": mem[3], "buff_cache": mem[4], "available": mem[5]},
        "swap_mib": {"total": swap[0], "used": swap[1], "free": swap[2]},
        "load_average": [float(x) for x in load],
        "uptime_seconds": uptime,
        "target_processes": processes,
        "target_rss_mib": round(sum(x["rss_kib"] for x in processes) / 1024, 1),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True, help="IP del TV; no se guarda por defecto")
    parser.add_argument("--sdb", required=True, type=Path)
    parser.add_argument("--vendor-root", required=True, type=Path, help="Checkout auditado de samsung-tv-root o quiet-tizen")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--include-host", action="store_true")
    args = parser.parse_args()
    capture, SdbClient, _ = load_vendor(args.vendor_root)
    client = SdbClient(str(args.sdb), args.host, timeout=20)
    client.connect(); client.require_device()
    rows = [x.split() for x in client.run(("devices",), check=True).stdout.splitlines() if x.split() and x.split()[0] == client.serial]
    if len(rows) != 1 or rows[0][1:] != ["device", MODEL]:
        raise RuntimeError(f"Identidad SDB inesperada: {rows}")
    command = (
        "echo memory; free -m; echo load; cat /proc/loadavg; "
        "echo uptime; cat /proc/uptime; echo targets; "
        f"ps -eo pid,rss,comm,args | grep -E '{TARGETS}' | grep -v grep || true"
    )
    result = parse(capture(client, command))
    result.update({"model": MODEL, "captured_at_utc": datetime.now(timezone.utc).isoformat()})
    if args.include_host:
        result["host"] = args.host
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "target_processes": len(result["target_processes"]), "target_rss_mib": result["target_rss_mib"]}))


if __name__ == "__main__":
    main()
