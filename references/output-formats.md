# Output formats and conversion

## Shared master

Draft one complete Markdown source in temporary storage, using final Figure paths or a temporary mirror of the final layout. Resolve and validate every image before export. Keep metadata, captions and provenance in the master; show useful bibliographic metadata in the document instead of dumping raw YAML. Use the same substantive content for all requested formats.

## Continuous layout for PDF and Word

- Flow sections and headings continuously; do not start each section or heading level on a new page. Let page capacity determine natural pagination unless the user explicitly requests section-based pagination.
- Separate sections with paragraph spacing rather than repeated empty paragraphs. Suggested spacing: 12–18 pt before a section heading, 6–8 pt after a heading, and 4–6 pt after body paragraphs.
- Ignore section-separating forced-page-break markers in Markdown by default, including `<!-- pagebreak -->`. Horizontal rules are not page breaks. Disable template/style settings such as `pageBreakBefore` that restart headings on new pages.
- Keep a heading with at least two following body lines where possible. Do not bind entire sections together or chain all paragraphs with keep-with-next.
- Preserve complete images and aspect ratio; keep captions with figures where possible. Modestly reduce display size to fit only when legibility is preserved. Otherwise move the complete figure and caption to the next page; never crop to fill a page.
- Allow long tables to span pages and repeat the header. Do not lock a whole table to one page; avoid splitting ordinary rows across pages where practical.
- Do not reduce body font size, compress line spacing, or remove content just to reduce page count. Remove artificial breaks and excess spacing first.
- Inspect every page. No empty pages are acceptable. Except on the final page, bottom whitespace exceeding roughly one third of a page triggers inspection for forced breaks, excessive keep-together settings, and image/table layout. Fix avoidable gaps; necessary gaps for a complete, readable large figure or table are acceptable. This is a review threshold, not a quota to fill by distorting content.

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
