#!/usr/bin/env python3
"""Build a Markdown first draft of a PaperLens figure index."""

from __future__ import annotations

import argparse
import re
import struct
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif"}


def image_size(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return struct.unpack(">II", data[16:24])
    if data.startswith((b"GIF87a", b"GIF89a")) and len(data) >= 10:
        return struct.unpack("<HH", data[6:10])
    if data.startswith(b"\xff\xd8"):
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            i += 2
            if marker in (0xD8, 0xD9):
                continue
            if i + 2 > len(data):
                break
            length = int.from_bytes(data[i : i + 2], "big")
            if marker in range(0xC0, 0xC4) and i + 7 < len(data):
                return (
                    int.from_bytes(data[i + 5 : i + 7], "big"),
                    int.from_bytes(data[i + 3 : i + 5], "big"),
                )
            i += max(length, 2)
    return None


def files_in(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS)


def dims(path: Path) -> str:
    size = image_size(path)
    return f"{size[0]}×{size[1]} px" if size else "尺寸未识别"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create 图片索引.md for a PaperLens figure pack.")
    parser.add_argument("figure_pack", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    root = args.figure_pack.resolve()
    figures = [p for p in files_in(root) if p.stem.startswith('Fig_')]
    output = args.output.resolve() if args.output else root / '图片索引.md'
    source = args.pdf.name if args.pdf else '未指定'
    lines = [f'# {root.name} 图片索引', '', f'- 来源 PDF：{source}', f'- 完整原文 Figures：{len(figures)}', '', '## 完整 Figures', '']
    for figure in figures:
        lines.append(f'- {figure.name}: {dims(figure)}')
    lines.extend(['', '此文件是清单初稿。交付前逐图补充原图号、PDF页码、图注、来源对象或区域坐标、提取方式和使用状态，并对照原文确认完整。', ''])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
