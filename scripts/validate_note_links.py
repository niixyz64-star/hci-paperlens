#!/usr/bin/env python3
"""Validate local image embeds and common artifact hygiene in an Obsidian note."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote


OBSIDIAN_IMAGE = re.compile(r"!\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def clean_markdown_target(value: str) -> str:
    value = value.strip().strip("<>")
    if " " in value and not value.startswith(("http://", "https://", "data:")):
        value = value.split(' "', 1)[0]
    return unquote(value)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check image links and hygiene in an HCI PaperLens note."
    )
    parser.add_argument("note", type=Path)
    parser.add_argument(
        "--vault-root",
        type=Path,
        help="Obsidian vault root. Defaults to the note directory for relative embeds.",
    )
    args = parser.parse_args()

    note = args.note.resolve()
    if not note.is_file():
        raise SystemExit(f"Note not found: {note}")
    text = note.read_text(encoding="utf-8-sig")
    vault = args.vault_root.resolve() if args.vault_root else note.parent

    errors: list[str] = []
    warnings: list[str] = []
    checked = 0

    for target in OBSIDIAN_IMAGE.findall(text):
        checked += 1
        candidate = Path(clean_markdown_target(target))
        resolved = candidate if candidate.is_absolute() else vault / candidate
        if not resolved.exists():
            errors.append(f"Missing Obsidian image: {target} -> {resolved}")

    for target in MARKDOWN_IMAGE.findall(text):
        cleaned = clean_markdown_target(target)
        if cleaned.startswith(("http://", "https://", "data:")):
            continue
        checked += 1
        if cleaned.startswith("file:///"):
            candidate = Path(cleaned[8:])
        else:
            candidate = Path(cleaned)
        resolved = candidate if candidate.is_absolute() else note.parent / candidate
        if not resolved.exists():
            errors.append(f"Missing Markdown image: {target} -> {resolved}")

    if re.search(r"(?i)(appdata[/\\]local[/\\]temp|/tmp/|\\temp\\)", text):
        warnings.append("The note contains a temporary filesystem path.")
    if re.search(r"(?i)\b(TODO|TBD|PLACEHOLDER)\b", text):
        warnings.append("The note contains an unresolved placeholder token.")
    if not text.startswith("---"):
        warnings.append("The note does not begin with YAML frontmatter.")
    if checked == 0:
        warnings.append("No local image embeds were found.")

    print(f"Note: {note}")
    print(f"Local image embeds checked: {checked}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("OK: no missing local image embeds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
