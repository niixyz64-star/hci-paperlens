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
    crops = files_in(root / "整图裁剪")
    raw = files_in(root / "原始嵌入图")
    output = args.output.resolve() if args.output else root / "图片索引.md"
    source = args.pdf.name if args.pdf else "未指定"

    lines = [
        f"# {root.name} 图片索引",
        "",
        f"- 来源 PDF：`{source}`",
        f"- 完整 Figure / Table 裁剪：{len(crops)} 张",
        f"- PDF 原始嵌入图（去重并过滤小元素）：{len(raw)} 张",
        "",
        "## 整图裁剪",
        "",
    ]
    if crops:
        for image in crops:
            figure = re.search(r"(Figure|Table)_([^_]+)_p(\d+)", image.stem, re.IGNORECASE)
            label = f"{figure.group(1).title()} {figure.group(2)}，第 {int(figure.group(3))} 页" if figure else "图号和页码请核对"
            lines.append(
                f"- `{image.name}`：{label}，{dims(image)}；用途与图注请在视觉检查后补充。"
            )
    else:
        lines.append("- 尚无完整裁剪；请从页面渲染图中裁剪并视觉检查关键 Figure / Table。")

    lines.extend(["", "## 原始嵌入图", ""])
    if raw:
        for image in raw:
            page_match = re.match(r"p(\d+)_", image.name)
            page = f"第 {int(page_match.group(1))} 页，" if page_match else ""
            lines.append(f"- `{image.name}`：{page}{dims(image)}")
    else:
        lines.append("- 未提取到符合筛选条件的原始嵌入图。")

    lines.extend(
        [
            "",
            "## 使用检查",
            "",
            "- 完整图是否保留图例、坐标轴、分图标签和必要标注。",
            "- 图中文字在笔记预期宽度下是否可读。",
            "- 已使用图片是否放在首次承担解释作用的位置。",
            "- Obsidian 嵌入是否使用稳定的库内相对路径。",
            "",
        ]
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
