# HCI PaperLens workflow

## Contents

1. Inputs and defaults
2. Template contract
3. Two-pass reading
4. Evidence synthesis
5. Seminar-oriented composition
6. Delivery

## 1. Inputs and defaults

Required inputs are the paper and a note template. The template may be user-supplied or the bundled default. A figure pack is also required before final drafting, but it can be supplied or generated during the task.

Useful optional inputs include an output directory, Zotero key, related-note folder, focus question, preferred language, presentation duration, and preferred output format.

When the user does not specify them, use sensible defaults:

- output language: the language used in the request;
- note name: `{ShortTitle} 阅读笔记.md` for Chinese output or `{ShortTitle} Reading Note.md` otherwise;
- presentation duration: 8–10 minutes;
- Markdown dialect: Obsidian when the destination is an Obsidian vault;
- final format: PDF unless Markdown, Word, or multiple formats are requested;
- Markdown master: temporary unless explicitly requested as a deliverable.

Do not hardcode personal drive letters, Zotero folders, temporary attachment locations, or a particular vault structure into reusable output.

## 2. Template contract

Read the selected template completely. Extract an internal contract covering:

- frontmatter fields and required tags;
- heading hierarchy;
- tables and callouts;
- local PDF-link convention;
- image-link syntax;
- optional versus required sections;
- naming conventions and tone.

Remove template usage instructions from the completed note. Preserve the template's style, but adapt its content structure to the paper. A system paper, empirical paper, design study, dataset paper, and benchmark paper should not be forced into identical subsections.

The bundled template uses the RegulAR reading-note narrative. Preserve its applicable top-level order, but replace generic subsection placeholders with paper-specific mechanisms, findings and limitations. Explain formative observations before derived requirements; separate evaluation studies by purpose; organize results by findings rather than figure order. Keep author discussion, author-stated limitations, and reader critique distinct. Research implications should develop a concrete question and a bounded follow-up study or system, using the user's research interests only when known. Follow the bundled template for detailed section guidance; do not import the reference note's paper-specific facts, image paths or cropping conventions.

## 3. Two-pass reading

### Pass 1: structural map

Read the entire paper and map:

- metadata and canonical links;
- problem, gap, and research questions;
- contributions;
- related-work positioning;
- formative or needs-finding studies;
- design requirements;
- system or method components;
- user studies and technical evaluations;
- all figures and tables;
- discussion, limitations, conclusion, and appendices.

Use this map to select figures and identify evidence locations. Complete the figure pack before drafting prose.

### Pass 2: evidence map

Create an internal matrix with these columns:

| Claim | Mechanism | Evidence | Evidence type | Strength / caveat | Location |
| --- | --- | --- | --- | --- | --- |

Capture exact details rather than vague summaries:

- participants and recruitment;
- task and condition assignment;
- baselines and controlled factors;
- independent and dependent variables;
- quantitative values, effect direction, significance, and correction procedures;
- qualitative themes and representative behavior;
- technical accuracy, latency, failure, and false-positive measures;
- author-stated limitations and future work.

Classify each substantive statement as one of:

1. supported finding;
2. author interpretation or proposal;
3. note author's critique or inference.

Keep categories 2 and 3 linguistically explicit.

## 4. Evidence synthesis

Do not use “better” without saying on which measure. Do not report a trend as significant. Do not treat an absence of statistical significance as proof of equivalence. When a user study is small or primarily qualitative, make that boundary visible.

For comparative systems, state what the baseline controls. For generated or adaptive interfaces, distinguish model quality, interaction quality, task performance, and user preference.

When the paper reports both subjective and behavioral evidence, keep them separate. A participant saying recovery felt easier does not by itself demonstrate faster or more accurate recovery.

## 5. Seminar-oriented composition

The note should answer the questions a seminar audience will ask:

1. What is the problem?
2. Why do existing approaches fail?
3. What is the paper's key move?
4. How does the method work?
5. What was actually evaluated?
6. Which results are convincing?
7. What is not yet established?
8. What should be discussed or built next?

### One-minute opening

Write one speakable paragraph containing the problem, key idea, evaluation scale, strongest result, and most important limitation. Avoid dense numeric detail unless a number is central to the claim.

### Figures

Place each selected figure at its first explanatory use. Follow it with a short caption in the note language that explains what the audience should notice and retains the paper's original figure number.

### Results

Prefer compact tables for repeated comparisons. Highlight key values but preserve nonsignificant findings and contradictory evidence. Explain metrics whose interpretation is non-obvious.

### Critique

Separate:

- strengths of the research contribution;
- methodological or evidential concerns;
- transferable design or writing patterns;
- research opportunities inferred from the work.

Do not make “future work” a generic wish list. Tie each direction to a demonstrated limitation, mechanism, or open design tension.

### Seminar outline

For an 8–10 minute presentation, a useful default is:

1. problem and gap — 1 minute;
2. key idea — 1 minute;
3. method or system — 2 minutes;
4. evaluation — 1 minute;
5. results — 2 minutes;
6. critique and limitations — 1 minute;
7. implications and discussion — 1–2 minutes.

Adjust rather than mechanically preserving these times when the user specifies another duration.

## 6. Delivery

Follow [output-formats.md](output-formats.md). Deliver the chosen file(s), a complete-Figure folder and its index. The Markdown master and extraction/rendering intermediates remain temporary unless requested. Default to a plain PDF, not a decorated report. Inspect every exported page and verify embedded images before reporting success.
