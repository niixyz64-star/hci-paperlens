# Complete original Figure specification

## Final pack

```text
图片素材/{ShortTitle}/
  Fig_01.jpg
  Fig_02.png
  图片索引.md
```

Preserve original numbering and supplementary labels. A multi-panel Figure is one complete figure, not a selection of panels. Tables are transcribed as document tables by default; do not dump table/page screenshots or publisher logos into this folder.

## Extraction and source matching

1. Extract raw image objects and render reference pages into a temporary working directory with `extract_pdf_assets.py`. Objects may be logos, fragments, duplicates, or figures with labels drawn separately.
2. Visually match each candidate against its original Figure and caption. Page order and image dimensions are not proof of a match.
3. If one embedded image contains the complete Figure, copy the original image bytes, preserving its extension, aspect ratio and resolution. No recropping, upscaling or recompression merely for appearance.
4. If a Figure is vector artwork or a composite of objects, render its complete region directly from the PDF once at adequate resolution (typically 250–300 dpi). Define bounds in source-page coordinates, preserving every panel, axis, legend and annotation. Do not guess bounds from resized previews; account for display-to-source scale. Do not crop the rendered result again. If bounds are wrong, correct the source region and rerender from the PDF.
5. Compare the complete exported Figure side by side with the source page at readable scale. Verify all edges, panel labels, legends and axes. Exclude neighboring columns, headers and footers. Correct incomplete extraction using step 4, not a clipped fragment.
6. Keep only reviewed, complete Figures in the final pack. Keep raw objects, page renders and debug contact sheets in temporary storage.

## Captions and provenance

Write captions in the note separately: original Figure number, source PDF page, and what the reader should notice. Preserve captions already inside source image bytes; do not crop to remove them. In the index record filename, original Figure number, PDF page (and printed page when different), dimensions, caption/description, source object or source-region coordinates, extraction method, and used/unused status.

`build_figure_index.py` creates an inventory draft only. Enrich provenance and captions after visual review before delivery.

## Linking

Portable Markdown uses note-relative links, for example `![Figure 1](图片素材/Paper/Fig_01.jpg)`. Obsidian embeds are appropriate when the destination is a vault. Package the Markdown and its assets together. PDF and Word must embed the images; never rely on local image paths in those deliverables.
