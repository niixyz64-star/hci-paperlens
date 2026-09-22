#!/usr/bin/env python3
"""Extract embedded PDF images and render pages for HCI PaperLens.

Requires Poppler's `pdftoppm` and `pdfinfo` executables. It uses `pdfimages`
when available and falls back to `pypdf` for embedded-image extraction.
Use --poppler-bin when Poppler is not available on PATH.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path


def executable(name: str, poppler_bin: Path | None, required: bool = True) -> str | None:
    suffix = ".exe" if sys.platform.startswith("win") else ""
    if poppler_bin:
        candidate = poppler_bin / f"{name}{suffix}"
        if candidate.exists():
            return str(candidate)
    found = shutil.which(name) or shutil.which(f"{name}{suffix}")
    if not found and required:
        raise SystemExit(
            f"Missing Poppler executable: {name}. Install Poppler or pass --poppler-bin."
        )
    return found


def extract_with_pypdf(pdf: Path, temp: Path) -> dict[int, list[Path]]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit(
            "pdfimages is unavailable and the pypdf fallback is not installed. "
            "Install pypdf or provide a Poppler build containing pdfimages."
        ) from exc

    extracted: dict[int, list[Path]] = {}
    reader = PdfReader(str(pdf))
    for page_number, page in enumerate(reader.pages, start=1):
        page_files: list[Path] = []
        for image_number, image in enumerate(page.images, start=1):
            suffix = Path(image.name).suffix.lower() or ".bin"
            target = temp / f"p{page_number:03d}-{image_number:03d}{suffix}"
            target.write_bytes(image.data)
            page_files.append(target)
        extracted[page_number] = page_files
    return extracted


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


def page_count(pdfinfo: str, pdf: Path) -> int:
    proc = subprocess.run(
        [pdfinfo, str(pdf)], check=True, capture_output=True, text=True, errors="replace"
    )
    match = re.search(r"^Pages:\s+(\d+)", proc.stdout, re.MULTILINE)
    if not match:
        raise SystemExit("Could not determine PDF page count.")
    return int(match.group(1))


def run(args: list[str]) -> None:
    subprocess.run(args, check=True)


def parse_pages(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(1, total + 1))
    pages: list[int] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = (int(x) for x in part.split("-", 1))
            pages.extend(range(start, end + 1))
        else:
            pages.append(int(part))
    return sorted(set(page for page in pages if 1 <= page <= total))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract embedded images and render PDF pages into a PaperLens figure pack."
    )
    parser.add_argument("pdf", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--poppler-bin", type=Path)
    parser.add_argument("--dpi", type=int, default=160)
    parser.add_argument("--min-width", type=int, default=180)
    parser.add_argument("--min-height", type=int, default=100)
    parser.add_argument("--min-area", type=int, default=40000)
    parser.add_argument("--pages", help="Pages to render, e.g. 1,3,5-8. Default: all pages.")
    args = parser.parse_args()

    pdf = args.pdf.resolve()
    if not pdf.is_file():
        raise SystemExit(f"PDF not found: {pdf}")

    root = args.output_dir.resolve()
    raw_dir = root / "原始嵌入图"
    page_dir = root / "页面渲染"
    crop_dir = root / "整图裁剪"
    raw_dir.mkdir(parents=True, exist_ok=True)
    page_dir.mkdir(parents=True, exist_ok=True)
    crop_dir.mkdir(parents=True, exist_ok=True)

    pdfimages = executable("pdfimages", args.poppler_bin, required=False)
    pdftoppm = executable("pdftoppm", args.poppler_bin)
    pdfinfo = executable("pdfinfo", args.poppler_bin)
    assert pdftoppm and pdfinfo
    total_pages = page_count(pdfinfo, pdf)

    seen: set[str] = set()
    global_index = 0
    kept = 0
    with tempfile.TemporaryDirectory(prefix="paperlens-") as temp_name:
        temp = Path(temp_name)
        fallback_files = extract_with_pypdf(pdf, temp) if not pdfimages else {}
        for page in range(1, total_pages + 1):
            if pdfimages:
                prefix = temp / f"p{page:03d}"
                run(
                    [
                        pdfimages,
                        "-f",
                        str(page),
                        "-l",
                        str(page),
                        "-png",
                        str(pdf),
                        str(prefix),
                    ]
                )
                page_files = sorted(
                    p for p in temp.iterdir() if p.name.startswith(prefix.name + "-")
                )
            else:
                page_files = fallback_files.get(page, [])
            page_index = 0
            for source in page_files:
                size = image_size(source)
                if size:
                    width, height = size
                    if (
                        width < args.min_width
                        or height < args.min_height
                        or width * height < args.min_area
                    ):
                        source.unlink(missing_ok=True)
                        continue
                digest = hashlib.sha256(source.read_bytes()).hexdigest()
                if digest in seen:
                    source.unlink(missing_ok=True)
                    continue
                seen.add(digest)
                global_index += 1
                page_index += 1
                target = raw_dir / (
                    f"p{page:02d}_img{page_index:02d}_{global_index:03d}{source.suffix.lower()}"
                )
                shutil.move(str(source), target)
                kept += 1

    render_pages = parse_pages(args.pages, total_pages)
    for page in render_pages:
        prefix = page_dir / f"page-{page:03d}"
        run(
            [
                pdftoppm,
                "-f",
                str(page),
                "-l",
                str(page),
                "-singlefile",
                "-png",
                "-r",
                str(args.dpi),
                str(pdf),
                str(prefix),
            ]
        )

    print(f"PaperLens figure pack: {root}")
    print(
        f"Pages: {total_pages}; embedded images kept: {kept}; pages rendered: {len(render_pages)}"
    )
    print("Next: visually crop complete figures into 整图裁剪, then build the index.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
