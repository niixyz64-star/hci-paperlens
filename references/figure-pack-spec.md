# Figure pack specification

## Purpose

The figure pack is a reviewed visual evidence set, not a dump of every PDF object. It must exist before final note drafting.

## Directory structure

Use the user's established structure when present. Otherwise use:

```text
图片素材/{ShortTitle}/
|-- 图片索引.md
|-- 整图裁剪/
|   |-- Figure_01_p01.png
|   `-- Figure_03_p05.png
|-- 原始嵌入图/
|   |-- p01_img01_001.png
|   `-- p05_img01_003.png
`-- 页面渲染/
    |-- page-001.png
    `-- page-005.png
```

`页面渲染/` is a working and audit folder. It may be omitted from the final pack when the user prefers a compact archive and all crops have been verified.

## Extraction sequence

1. Extract embedded raster images page by page.
2. Deduplicate exact files and filter tiny decorative assets.
3. Render PDF pages to PNG for layout-aware review.
4. Identify complete figures and tables by reading the paper and captions.
5. Crop complete figures from rendered pages when a figure consists of multiple PDF objects or extracted parts.
6. Visually inspect every crop.
7. Build the index and mark which figures are used in the note.

`scripts/extract_pdf_assets.py` handles steps 1–3. Cropping and final selection require visual judgment.

## Naming

Raw embedded image:

```text
p{page:02d}_img{page_index:02d}_{global_index:03d}.{ext}
```

Complete crop:

```text
Figure_{figure_number:02d}_p{page:02d}.png
Table_{table_number:02d}_p{page:02d}.png
```

Preserve supplementary labels when needed, for example `Figure_03a_p05.png`.

## Selection criteria

Prioritize:

- teaser or concept figure;
- system architecture or pipeline;
- interaction or UI states;
- study setup when it materially affects interpretation;
- central quantitative result;
- representative qualitative cases;
- design space or taxonomy central to the contribution.

Exclude or leave unused:

- publisher marks, logos, decorative lines, and icons;
- duplicates and lower-resolution copies;
- figures unrelated to the note's narrative;
- unreadable crops;
- small fragments that lack context.

## Visual QA

For every complete crop, verify:

- no caption, legend, axis label, or subfigure label needed for understanding is clipped;
- text is readable at the note's expected display width;
- aspect ratio is unchanged;
- no large accidental page margins remain;
- figure number, source page, and index entry agree;
- personal information is not exposed unintentionally.

## Image index

The index should state the source PDF and counts, then list complete crops and raw images. For each complete crop include, when available:

- filename;
- page and figure or table number;
- pixel dimensions;
- original caption or a faithful short description;
- explanatory role in the note;
- used / unused status.

Run `scripts/build_figure_index.py` to create a mechanical first draft, then enrich and correct it after visual inspection.

## Embedding in Obsidian

Prefer a vault-relative embed:

```markdown
![[图片素材/03_RegulAR/整图裁剪/Figure_03_p05.png|1000]]
```

Follow it with a note-language caption:

```markdown
> Figure 3. 系统由任务图构建、运行时监测和影响感知干预组成。（原论文 Figure 3）
```

Avoid temporary attachment paths and absolute links when a relative vault path is possible.
