# Delivery quality rubric

Use this rubric before handing off a paper note.

## 1. Source fidelity

- The full paper was read, including discussion, limitations, and relevant appendices.
- Title, authors, institution, venue, year, DOI, page count, model names, and hardware are verified.
- Sample sizes, conditions, tasks, measures, and statistics match the paper.
- Nonsignificant findings are retained when they qualify the narrative.
- No claim relies on memory when the paper can be checked.

## 2. Evidence discipline

- Objective performance, subjective ratings, qualitative themes, and author interpretation are distinguishable.
- “No significant difference” is not phrased as proof of no effect.
- Small samples, exploratory analyses, missing baselines, and confounds are visible.
- Author-stated limitations are separated from the note author's inferred opportunities.
- Future directions are tied to a concrete limitation, mechanism, or tension.

## 3. Figure quality

- A reviewed figure pack exists.
- Each used figure has been visually inspected at readable scale.
- No legend, axis, subfigure label, or necessary annotation is clipped.
- Images appear where they explain the narrative.
- Captions explain what to notice and preserve original figure numbers.
- Obsidian embeds resolve from the note location.

## 4. Note quality

- Frontmatter is valid and contains no template instructions.
- Heading hierarchy is coherent and empty sections are removed.
- The opening paragraph is speakable in roughly one minute.
- System or method logic is understandable without repeatedly opening the PDF.
- Experiments are summarized with enough detail to judge the evidence.
- The final evaluation states both the contribution and its boundary.
- Discussion questions are specific enough to support a seminar conversation.
- A presentation outline matches the requested duration.

## 5. Artifact hygiene

- No temporary paths, tool tokens, raw extraction logs, or private machine details remain.
- Local file links use the destination's established convention.
- The note and assets use stable, descriptive filenames.
- `scripts/validate_note_links.py` reports no missing image embeds.
- Optional PDF exports have been rendered and visually reviewed page by page.

## Stop conditions

Do not claim completion when:

- the paper cannot be read completely;
- key figures are missing or unreadable;
- exact experimental numbers cannot be verified;
- required destination access is unavailable;
- the note still contains unresolved placeholders.

In those cases, deliver the verified partial work and state the specific missing input or permission.
