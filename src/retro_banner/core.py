"""Core banner rendering functions."""

from __future__ import annotations

from typing import Literal

Border = Literal["double", "single", "star", "none"]

_BORDERS: dict[str, tuple[str, str, str, str, str, str]] = {
    "double": ("╔", "╗", "╚", "╝", "═", "║"),
    "single": ("┌", "┐", "└", "┘", "─", "│"),
    "star": ("*", "*", "*", "*", "*", "*"),
}


def render(
    text: str,
    *,
    border: Border = "double",
    padding: int = 1,
    width: int | None = None,
) -> str:
    """Render *text* inside a Unicode frame.

    Multiline text is supported. ``width`` sets the interior width; lines are
    centered in that space. If omitted, the longest input line determines it.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if border not in (*_BORDERS, "none"):
        raise ValueError("border must be 'double', 'single', 'star', or 'none'")
    if not isinstance(padding, int) or isinstance(padding, bool) or padding < 0:
        raise ValueError("padding must be a non-negative integer")
    lines = text.splitlines() or [""]
    longest = max(map(len, lines))
    if width is None:
        content_width = longest + padding * 2
    else:
        if not isinstance(width, int) or isinstance(width, bool) or width < 1:
            raise ValueError("width must be a positive integer")
        content_width = width
        if longest > content_width:
            raise ValueError("width is too small for the text")
    if border == "none":
        return "\n".join(line.center(content_width) for line in lines)
    tl, tr, bl, br, h, v = _BORDERS[border]
    top = tl + h * content_width + tr
    body = [v + line.center(content_width) + v for line in lines]
    bottom = bl + h * content_width + br
    return "\n".join([top, *body, bottom])


def banner(text: str, *, style: Border = "double", padding: int = 1) -> str:
    """Convenience wrapper around :func:`render` using ``style`` as border."""
    return render(text, border=style, padding=padding)
