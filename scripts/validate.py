#!/usr/bin/env python3
"""Validate the skill package, docs, and the dist zip."""

from __future__ import annotations

import html.parser
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "skills" / "website-ui-design" / "scripts"))

from contrast import contrast_ratio
from pack import DIST, PREFIX, SKILL_DIR, member_bytes
from skills_ref import validate as validate_skill

CANONICAL_PAIRS = (
    ("#FFDF70", "#153472"),
    ("#EFC2A3", "#DA0011"),
    ("#FE5C1B", "#1A3B32"),
    ("#9ED4F0", "#144975"),
    ("#EBD2D6", "#E45600"),
)

PAIR_FILES = (
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "references" / "chinese-colors.md",
    SKILL_DIR / "references" / "style-library.md",
    SKILL_DIR / "assets" / "starter.html",
    ROOT / "README.md",
    ROOT / "docs" / "wechat_article.md",
)

# Text on background. Body text must clear 4.5:1. These are the published roles.
CONTRAST_PAIRS = (
    ("#161823", "#FFDF70"),
    ("#153472", "#FFDF70"),
    ("#3D3B4F", "#FFDF70"),
    ("#FFFFFF", "#153472"),
    ("#3A1414", "#EFC2A3"),
    ("#FFFFFF", "#DA0011"),
    ("#161823", "#FE5C1B"),
    ("#FFF7EE", "#1A3B32"),
    ("#161823", "#FFF7EE"),
    ("#5C4036", "#FFF7EE"),
    ("#0A2A45", "#9ED4F0"),
    ("#3A5470", "#9ED4F0"),
    ("#FFFFFF", "#144975"),
    ("#4A1E10", "#EBD2D6"),
    ("#7A4530", "#EBD2D6"),
    ("#161823", "#E45600"),
    ("#161823", "#F2ECDE"),
    ("#FFFFFF", "#9D2933"),
    ("#161823", "#FF461F"),
    ("#111111", "#FF4D00"),
    ("#FFFFFF", "#4314FF"),
    ("#111111", "#FCEE21"),
    ("#1A1A1A", "#FAFAFA"),
    ("#FAFAFA", "#1A1A1A"),
    ("#6B6B6B", "#FAFAFA"),
    ("#FFFFFF", "#2563EB"),
    ("#F4F7FB", "#0B1220"),
    ("#F4F7FB", "#134E4A"),
    ("#C5D0DC", "#0B1220"),
    ("#0B1220", "#F4F7FB"),
    ("#E5E7EB", "#0A0F1A"),
    ("#94A3B8", "#0A0F1A"),
    ("#94A3B8", "#111827"),
    ("#0A0F1A", "#06B6D4"),
    ("#F5C16C", "#0A0F1A"),
    ("#111111", "#E63946"),
    ("#1A1A1A", "#FDF6E3"),
    ("#FFFFFF", "#E2231A"),
    ("#1A1A1A", "#F7D417"),
    ("#FFFFFF", "#2451A6"),
    ("#2D2A26", "#FBF7F2"),
    ("#6E685F", "#FBF7F2"),
    ("#FFFFFF", "#3F6248"),
    ("#2D2A26", "#C98A6B"),
    ("#161823", "#EFC2A3"),
    ("#144975", "#9ED4F0"),
    ("#FFFFFF", "#1A3B32"),
)

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEX_RE = re.compile(r"#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})\b")


class TagStack(html.parser.HTMLParser):
    VOID = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in self.VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected </{tag}> (open: {self.stack[-3:]})")
            return
        self.stack.pop()


def check_markdown_links(errors: list[str]) -> None:
    files = [ROOT / "README.md", *SKILL_DIR.rglob("*.md")]
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            cleaned = target.split("#", 1)[0].strip()
            if not cleaned:
                continue
            resolved = (path.parent / cleaned).resolve()
            if not resolved.is_file():
                errors.append(f"broken link in {path.relative_to(ROOT)}: {target}")


def check_html(errors: list[str]) -> None:
    starter = (SKILL_DIR / "assets" / "starter.html").read_text(encoding="utf-8")
    parser = TagStack()
    parser.feed(starter)
    parser.close()
    errors.extend(f"starter.html: {item}" for item in parser.errors)
    if parser.stack:
        errors.append(f"starter.html unclosed tags: {parser.stack}")
    required = (
        "--on-primary",
        ":focus-visible",
        "prefers-reduced-motion",
        'id="main"',
        "pair-douhuang",
        "scripts/contrast.py",
    )
    for snippet in required:
        if snippet not in starter:
            errors.append(f"starter.html missing {snippet}")
    if "—" in starter or "–" in starter:
        errors.append("starter.html contains an em dash or en dash")
    if "addEventListener" in starter or "GSAP" in starter:
        errors.append("starter.html contains a scroll listener or GSAP")
    label_rules = {
        ".pair-fuguang .top": "#161823",
        ".pair-danhong .top": "#161823",
        ".pair-danfen .top": "#4A1E10",
        ".pair-danfen .bottom": "#161823",
    }
    for selector, color in label_rules.items():
        match = re.search(re.escape(selector) + r"\s*\{[^}]+\}", starter)
        if match is None or color not in match.group(0):
            errors.append(f"starter.html {selector} should use {color}")


def check_docs(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "unzip dist/website-ui-design.zip -d ~/.workbuddy/skills\n" not in readme:
        errors.append("README unzip command is missing or still double-nests the skill")
    if "1600×1056" not in readme:
        errors.append("README should record the banner as 1600×1056")
    style = (SKILL_DIR / "references" / "style-library.md").read_text(encoding="utf-8")
    anti = (SKILL_DIR / "references" / "anti-slop.md").read_text(encoding="utf-8")
    for banned in ("#6D5BFF", "#7C3AED", "GSAP"):
        if banned in style or banned in anti:
            errors.append(f"{banned} is still recommended in the style or anti-slop docs")
    if "animation-timeline" not in anti:
        errors.append("anti-slop.md should prefer CSS animation-timeline")
    colors = (SKILL_DIR / "references" / "chinese-colors.md").read_text(encoding="utf-8")
    if "#0A1A2A" in colors and "不要把它们改写成" not in colors:
        errors.append("chinese-colors.md still tells agents to darken sampled hexes")
    for path in PAIR_FILES:
        text = path.read_text(encoding="utf-8")
        for warm, cool in CANONICAL_PAIRS:
            if warm not in text or cool not in text:
                errors.append(
                    f"{path.relative_to(ROOT)} is missing sampled pair {warm} / {cool}"
                )
        for match in HEX_RE.findall(text):
            if len(match) == 4:
                errors.append(f"3-digit hex in {path.relative_to(ROOT)}: {match}")


def check_contrast(errors: list[str]) -> None:
    for foreground, background in CONTRAST_PAIRS:
        ratio = contrast_ratio(foreground, background)
        if ratio < 4.5:
            errors.append(
                f"contrast {ratio:.2f} < 4.5 for {foreground} on {background}"
            )
    bad = contrast_ratio("#FFFFFF", "#FE5C1B")
    if bad >= 4.5:
        errors.append("contrast.py failed to flag white on 丹红")


def check_zip(errors: list[str]) -> None:
    if not DIST.is_file():
        errors.append("dist/website-ui-design.zip is missing; run python3 scripts/pack.py")
        return
    expected = member_bytes()
    with zipfile.ZipFile(DIST) as archive:
        names = archive.namelist()
        if names != sorted(expected):
            errors.append(
                "dist zip members drifted from skills/website-ui-design; "
                "run python3 scripts/pack.py"
            )
            return
        for name, data in expected.items():
            if archive.read(name) != data:
                errors.append(f"dist zip is stale for {name}; run python3 scripts/pack.py")
                return
    if f"{PREFIX}/SKILL.md" not in expected:
        errors.append("zip prefix missing")


def main() -> int:
    errors: list[str] = []
    skill_errors = validate_skill(SKILL_DIR)
    errors.extend(f"skills-ref: {item}" for item in skill_errors)
    check_markdown_links(errors)
    check_html(errors)
    check_docs(errors)
    check_contrast(errors)
    check_zip(errors)
    if errors:
        print(f"{len(errors)} validation error(s):")
        for item in errors:
            print(f" - {item}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
