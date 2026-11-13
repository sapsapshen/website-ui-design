#!/usr/bin/env python3
"""Build dist/website-ui-design.zip from skills/website-ui-design."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "website-ui-design"
DIST = ROOT / "dist" / "website-ui-design.zip"
PREFIX = "website-ui-design"

MEMBERS = (
    "SKILL.md",
    "assets/starter.html",
    "references/anti-slop.md",
    "references/chinese-colors.md",
    "references/example.md",
    "references/style-library.md",
    "scripts/contrast.py",
)


def member_bytes() -> dict[str, bytes]:
    missing = [name for name in MEMBERS if not (SKILL_DIR / name).is_file()]
    if missing:
        raise SystemExit("missing skill files: " + ", ".join(missing))
    return {
        f"{PREFIX}/{name}": (SKILL_DIR / name).read_bytes() for name in MEMBERS
    }


def write_zip(destination: Path | None = None) -> Path:
    target = destination or DIST
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = member_bytes()
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(payload):
            info = zipfile.ZipInfo(name)
            info.date_time = (2026, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, payload[name])
    return target


def main() -> int:
    path = write_zip()
    print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
