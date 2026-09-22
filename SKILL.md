---
name: hci-paperlens
description: Create evidence-grounded, visually rich Obsidian reading notes for HCI papers and research-seminar presentations. Use when a user asks to closely read a CHI, UIST, CSCW, IUI, DIS, or related HCI paper; extract and organize its figures; synthesize its system, study, findings, limitations, and research opportunities; or prepare a paper discussion note. Do not use for a brief abstract-only summary or a generic literature list.
metadata:
  version: "1.1.1"
  short-description: "Visual HCI paper notes for research seminars"
---

# HCI PaperLens

Create a seminar-ready paper note by combining three sources:

1. a note template that defines the skeleton;
2. a reviewed figure pack that provides visual explanations;
3. the full paper, which remains the authority for facts and evidence.

The invariant is: **template sets structure, figures carry explanation, the paper supports claims, and the seminar determines narrative order.**

## Required workflow

### 1. Establish the note contract

- Use the user's template when one is supplied. Read it completely before drafting.
- Otherwise use [assets/hci-paper-note-template.md](assets/hci-paper-note-template.md).
- Preserve the user's frontmatter, Obsidian syntax, naming conventions, and output location.
- Adapt sections to the paper type; never invent a formative study, technical evaluation, or other section merely to fill the template.

### 2. Read the paper once for structure

Read the complete paper, not only the abstract. Locate metadata, research gap, research questions, contributions, method or system, studies, figures, tables, discussion, limitations, appendices, and prompts or instruments.

For PDF handling and figure selection, follow [references/figure-pack-spec.md](references/figure-pack-spec.md). When helpful, run `scripts/extract_pdf_assets.py` to create the initial asset pack.

### 3. Finish the figure pack before drafting

Do not begin the final note until a reviewed figure pack exists.

- If the user provides a figure pack, audit it and reuse it.
- Otherwise extract embedded images, render relevant pages, crop complete figures, and create `图片索引.md`.
- Prefer figures that explain the research problem, system pipeline, interface, study design, main quantitative result, or representative cases.
- Place images at the point where they explain the text; do not collect them at the end.

The script can perform mechanical extraction, but complete-figure cropping and final selection require visual inspection.

### 4. Read again for evidence

Build an internal claim-evidence map. Distinguish:

- findings directly supported by objective or statistical evidence;
- authors' interpretations or proposals with limited evidence;
- your own critique or research inference.

Record exact sample sizes, conditions, tasks, measures, effect directions, statistics, nonsignificant results, and stated limitations. Do not turn “no significant difference” into proof of no effect.

### 5. Write for a research seminar

Use the template as the base, then organize the explanation in this order when appropriate:

1. why the problem matters;
2. what earlier approaches miss;
3. the paper's central idea;
4. how the system or method works;
5. how it was evaluated;
6. what the evidence supports;
7. what remains uncertain;
8. what the group should discuss or build next.

Include a concise one-minute opening and an 8–10 minute presentation outline unless the user requests another duration. Translate figure captions into concise explanatory Chinese when writing Chinese notes, and retain the original figure number.

For the complete writing process, read [references/workflow.md](references/workflow.md).

### 6. Validate before delivery

Apply [references/quality-rubric.md](references/quality-rubric.md). At minimum:

- verify title, authors, venue, year, DOI, tasks, sample sizes, conditions, statistics, and model or device names against the paper;
- visually inspect every embedded figure;
- use relative Obsidian image embeds whenever the note and assets share a vault;
- run `scripts/validate_note_links.py` when producing a local Markdown artifact;
- remove template instructions, blank placeholder sections, temporary paths, and unsupported claims;
- report where the note and figure pack were saved.

Generate a PDF only when the user asks for one, and render it page-by-page for visual QA.

## Supporting resources

- Read [references/workflow.md](references/workflow.md) for close reading, evidence synthesis, note composition, and seminar preparation.
- Read [references/figure-pack-spec.md](references/figure-pack-spec.md) when extracting, auditing, cropping, naming, or indexing figures.
- Read [references/quality-rubric.md](references/quality-rubric.md) before final delivery.
- Copy or adapt [assets/hci-paper-note-template.md](assets/hci-paper-note-template.md) only when the user has not supplied a preferred template.

## Scripts

All scripts are optional helpers, not substitutes for reading and visual review.

```text
python scripts/extract_pdf_assets.py PAPER.pdf OUTPUT_DIR
python scripts/build_figure_index.py OUTPUT_DIR --pdf PAPER.pdf
python scripts/validate_note_links.py NOTE.md
```

Use `--help` for available options and Poppler path overrides.
