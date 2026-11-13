#!/usr/bin/env python3
"""Check WCAG 2.2 contrast for hex pairs. Python stdlib only.

Body text needs 4.5:1. Large text (24px, or bold and at least 18.67px) needs 3:1.
A 16px button label is body text. Pass --min 3 only for real large text.

Usage:
  python3 scripts/contrast.py #161823 #FE5C1B
  python3 scripts/contrast.py --min 3 #FFFFFF #DA0011 #161823 #FFDF70
"""

from __future__ import annotations

import sys


def usage() -> None:
    print(
        "usage: python3 scripts/contrast.py [--min 4.5] #RRGGBB #RRGGBB [...]",
        file=sys.stderr,
    )


def parse_hex(raw: str) -> tuple[int, int, int]:
    text = raw.strip()
    if text.startswith("#"):
        text = text[1:]
    if len(text) != 6 or any(c not in "0123456789abcdefABCDEF" for c in text):
        raise ValueError(f"not a 6-digit hex color: {raw}")
    value = int(text, 16)
    return (value >> 16) & 255, (value >> 8) & 255, value & 255


def channel(value: int) -> float:
    amount = value / 255
    if amount <= 0.04045:
        return amount / 12.92
    return ((amount + 0.055) / 1.055) ** 2.4


def luminance(rgb: tuple[int, int, int]) -> float:
    red, green, blue = (channel(part) for part in rgb)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(foreground: str, background: str) -> float:
    lighter = luminance(parse_hex(foreground))
    darker = luminance(parse_hex(background))
    if darker > lighter:
        lighter, darker = darker, lighter
    return (lighter + 0.05) / (darker + 0.05)


def main(argv: list[str]) -> int:
    minimum = 4.5
    args = argv[1:]
    if args[:1] == ["--min"]:
        if len(args) < 2:
            usage()
            return 2
        try:
            minimum = float(args[1])
        except ValueError:
            print(f"bad --min value: {args[1]}", file=sys.stderr)
            return 2
        args = args[2:]
    if len(args) < 2 or len(args) % 2 != 0:
        usage()
        return 2

    failed = False
    for index in range(0, len(args), 2):
        foreground, background = args[index], args[index + 1]
        try:
            ratio = contrast_ratio(foreground, background)
        except ValueError as exc:
            print(exc, file=sys.stderr)
            return 2
        status = "OK" if ratio + 1e-9 >= minimum else "FAIL"
        if status == "FAIL":
            failed = True
        print(f"{ratio:5.2f}  {status}  {foreground} on {background}  (min {minimum:g})")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
