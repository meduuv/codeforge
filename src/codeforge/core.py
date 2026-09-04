"""Simple source inspection helpers."""


def count_lines(text: str) -> dict[str, int]:
    """Count total, blank, and non-blank lines."""
    lines = text.splitlines()
    blank = sum(not line.strip() for line in lines)
    return {"total": len(lines), "blank": blank, "non_blank": len(lines) - blank}


def todo_items(text: str) -> list[str]:
    """Return source lines containing a TODO marker."""
    return [line.strip() for line in text.splitlines() if "TODO" in line]
