# Output formats and conversion

## Shared master

Draft one complete Markdown source in temporary storage, using final Figure paths or a temporary mirror of the final layout. Resolve and validate every image before export. Keep metadata, captions and provenance in the master; show useful bibliographic metadata in the document instead of dumping raw YAML. Use the same substantive content for all requested formats.

## Default: PDF

Convert the master to a simple reading document with consistent body type, heading hierarchy, restrained margins, readable tables and optional page numbers. No extra cover, colored cards, decorative emojis or redesigned prose unless requested. Embed original images at native quality with preserved aspect ratio; fit large figures to a full page when needed. Keep captions with figures, headings with following content, and repeat table headers across pages.

Use an available document converter (for example Pandoc with a working PDF engine, or a Markdown-aware HTML/PDF pipeline). A purpose-built renderer is acceptable only if it faithfully supports all syntax present. Check dependencies before conversion; do not treat a missing converter as permission to silently drop content. Use embedded CJK-capable fonts for Chinese text and verify symbols, math, bold and punctuation.

Convert Obsidian image embeds and callouts to supported image/callout structures. Render Mermaid to a real diagram, not a code block or prose replacement. Preserve equations, links, footnotes and tables. Fail or report a specific unsupported element rather than silently discarding it.

Render every page and inspect at readable scale for clipping, overflow, missing glyphs, poor image scale and awkward pagination. A contact sheet is for navigation, not a substitute for checking detailed pages. Confirm searchable text and the expected image/figure count.

## Word (.docx)

Export from the same master with native heading/list/table styles and embedded images (not external image relationships). Keep text editable, captions adjacent and layout restrained. Inspect the DOCX media package, then render the document with an available Word/LibreOffice or document rendering tool and review every page. If rendering is unavailable, state that limitation rather than claiming visual verification. A cloud platform's DOCX import fidelity depends on that platform; do not promise identical layout.

## Markdown (.md)

Deliver the note plus its relative-linked image folder and index as a movable package (ZIP optional). Standard Markdown is preferable for portability; preserve Obsidian syntax when requested or when writing to a vault. Validate links after the final copy. Explain, when cloud reuse is relevant, that copying Markdown text alone does not upload local images. Do not use giant base64 image URLs as a portability workaround.

## Final folder

```text
{ShortTitle} 阅读笔记.pdf       # default; .md/.docx only as requested
图片素材/{ShortTitle}/
  Fig_01.jpg
  Fig_02.png
  图片索引.md
```

An original-paper copy is optional according to user intent. Keep drafts, extracted fragments, page PNGs and logs outside the final folder. Do not overwrite unrelated user files. Report the actual delivered formats and validation limits.
