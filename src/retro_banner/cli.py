"""Command-line interface for retro-banner."""

from __future__ import annotations

import argparse
import sys

from .core import render


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="retro-banner",
        description="Make a retro framed banner for your terminal.",
    )
    parser.add_argument("text", nargs="*", help="text to put in the banner")
    parser.add_argument("-b", "--border", choices=("double", "single", "star", "none"), default="double")
    parser.add_argument("-p", "--padding", type=int, default=1)
    parser.add_argument("--width", type=int, help="interior width for centered text")
    args = parser.parse_args(argv)
    text = " ".join(args.text) if args.text else sys.stdin.read().rstrip("\n")
    try:
        print(render(text, border=args.border, padding=args.padding, width=args.width))
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
