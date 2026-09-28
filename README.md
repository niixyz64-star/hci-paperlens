# HCI PaperLens

HCI PaperLens is a Codex skill for producing visually rich, evidence-grounded Obsidian reading notes for CHI, UIST, CSCW, IUI, DIS, and related HCI papers.

It turns three inputs into a research-seminar-ready note:

1. a rule template that defines the note structure;
2. a reviewed figure pack extracted from the paper;
3. the full paper as the authority for claims and evidence.

> Template sets structure, figures carry explanation, the paper supports claims, and the seminar determines narrative order.

## What it produces

- a plain PDF close-reading note by default, or Markdown / Word on request;
- a figure pack containing complete original Figures and a provenance index; extraction intermediates stay temporary;
- a one-minute spoken opening and an 8–10 minute seminar outline;
- explicit separation between findings, author interpretation, and reviewer inference;
- embedded images in PDF/Word for independent sharing; relative-linked assets for Markdown.

## Install

Copy the `hci-paperlens` folder into your Codex skills directory, typically:

```text
~/.codex/skills/hci-paperlens/
```

Then invoke it explicitly or ask Codex to closely read an HCI paper for a research seminar.

```text
Use $hci-paperlens to extract this paper's figures and create an evidence-grounded Obsidian reading note for my research seminar.
```

The skill also supports automatic discovery for relevant requests.

## Workflow

```text
template contract
      ↓
full-paper structural pass
      ↓
figure extraction and visual review
      ↓
claim–evidence reading pass
      ↓
seminar-oriented note composition
      ↓
fact, figure, and link validation
```

The bundled template is a reusable default. A user-supplied template always takes precedence.

## Helper scripts

```text
python scripts/extract_pdf_assets.py PAPER.pdf OUTPUT_DIR
python scripts/build_figure_index.py OUTPUT_DIR --pdf PAPER.pdf
python scripts/validate_note_links.py NOTE.md
```

The extraction script requires Poppler's `pdftoppm` and `pdfinfo`. It uses `pdfimages` when available and otherwise falls back to `pypdf`. Raw candidates are temporary. Prefer complete original embedded images without recropping; render vector/composite Figures once from the source PDF region when necessary. Visual source comparison remains mandatory.

## Version

Current release: **2.0.0**

## License

MIT

## Formats and portability

Write a Markdown master first, then export the requested format (PDF by default). Plain PDF preserves the note structure without decorative covers. Word embeds images and keeps text editable. Markdown must travel with its image folder; copying its text to Feishu does not upload local images. See `references/output-formats.md`.
