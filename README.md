# Exam notes

A plain HTML/CSS/JavaScript concept tutorial library. Open index.html, search a scenario or method, and enter a detailed worked chapter. Sample-paper questions link directly to the required concepts. The former six-block card catalogue is retired.

## Read this before writing any chapter notes

These instructions capture the user's corrections in the Exam project conversation on 25 October 2026. They apply across chapter chats. The user wants an exam cheat sheet built from their learning conversation, not an independently written textbook summary or formula table.

### Use the actual chapter conversation

- Read the relevant chapter discussion before summarizing. Preserve the user's own wording, explanations, examples, questions, and reasoning that they understand. Correct the specific mistakes clearly; do not replace everything with the tutor's preferred academic explanation.
- Check technical accuracy and syllabus scope against the uploaded lecture notes and sample papers. Keep the lecturer's terms and diagram conventions. Conversation determines how to explain; lectures check what is correct and in scope.
- Record which conversation and source pages were actually read. A chat title, a few recent messages, or opaque content references are not the full discussion. Never claim that generic notes reproduce a conversation that was unavailable.
- If access is partial, state that limit briefly and preserve it in the chapter handoff. The earlier permission to generate initial standard-concept drafts was a one-off exception, not the default method for later chapter summaries.

### Separate chapters by the problem they solve

- CF/MF belongs in its own recommendation chapter: what CF and MF are, their relationship, and the problem they solve.
- SVD/PCA belongs in a separate chapter addressing decomposition and dimensionality reduction. Do not combine it with CF/MF in a shared cheat sheet or print page merely because both involve matrices. Cross-reference only a distinction the user has discussed and needs.
- A common website and presentation style do not mean combining different topics into one chapter.

### Write for scenario-based exam answers

For each chapter, cover the relevant questions in short, understandable points:

1. What is it, how are the related methods connected, and what problem does it solve?
2. What are the steps? Explain the purpose of each step and carry through an example discussed with the user. The user explicitly requests examples in the CF/MF cheat sheet; this does not authorize unsolicited examples in every tutoring reply.
3. What data preparation is needed? For CF/MF, address sparse data, missing feedback, and new users/items: problem → consequence → remedy → why it helps.
4. How is the model trained? Explain the objective or loss in words the user understands; use mathematics only when it helps answer the exam question.
5. How should it be evaluated? Explain the split, metric, interpretation, and relationship to the task.
6. How does overfitting appear, how can it be prevented, and why do the relevant techniques help? Use techniques actually taught or discussed, not an unexplained list.
7. Given a proposed model or flawed setup, what should change and why? Use problem → proposed change → reason. Include architecture or simple analytical calculations only where relevant to the chapter.

### No unexplained notation or terminology

- Do not introduce symbols such as Ω merely to make a formula look formal. Prefer plain wording such as "known training ratings" when that is what the user understands.
- Include a formula only when needed for the discussed concept or likely exam calculation. Explain every symbol, what the formula does, and how to interpret the result. If the user does not understand a formula, explain it before treating it as established revision material.
- Prioritize useful reasoning over memorization. A sheet of equations is not an adequate substitute for the explanations, decision steps, and examples above.
- Be direct when checking understanding: Correct / Incorrect / Partly correct, with the exact issue. Keep tutoring replies short and let the user explain in their own words.

### Design and printing

- Use the user's screenshot references: visible chapter navigation, a second row of views, compact grouped sections, Essential/Deeper controls, and informative diagrams with nearby takeaways.
- Screen study notes and condensed print sheets have different density needs. Keep each topic's print sheet separate, minimize wasted spacing, use compact diagrams, and verify actual A4 pagination. Do not promise a page count without rendering it.
- The combined CF/MF + SVD/PCA print mockup was rejected. Its combined-topic layout is not the template for future chapters.
- Record later corrections in these shared rules and the relevant chapter handoff so the user does not need to repeat them.

## Shared tutoring workflow

Every chapter discussion feeds this same website. Read [STUDY_RULES.md](STUDY_RULES.md) for the tutoring agreement and [CHAPTERS.md](CHAPTERS.md) for chapter status and handoffs. [AGENTS.md](AGENTS.md) provides repository instructions for Codex.

For separate chats in the ChatGPT Exam project, add the prepared `EXAM_PROJECT_INSTRUCTIONS.md` (in the parent output folder) to that project's instructions once. A local README does not update ChatGPT project settings. Current source-access limits and verified publishing status are recorded in the study agreement. GitHub publishing has succeeded; do not repeat a historical authentication blocker without checking current access.

## CF/MF exam cheat sheet

[Read the CF/MF chapter](chapters/cf-mf.html) or [download its 2-page A4 cheat sheet](downloads/cf-mf-cheat-sheet.pdf). It covers steps, worked examples, data problems, evaluation, overfitting remedies, and scenario answer patterns. SVD/PCA is separate. Full chapter-conversation and lecture-source verification are still pending.

## Open the site

Open `index.html` directly in a modern browser. All paths are relative, so the same files work under GitHub Pages at `/exam-notes/`.

To publish with GitHub Pages, choose **Settings → Pages → Deploy from a branch**, select the branch containing these files and **/(root)**, then save. Publishing is not enabled by this code alone.

## Add a chapter

1. Copy `chapters/template.html` to `chapters/your-chapter.html`.
2. Replace its title, description, chapter heading, overview, and section placeholders. Keep section IDs and contents links in sync.
3. Add an `<li><a href="chapters/your-chapter.html">Your chapter title</a></li>` to the `chapter-list` in `index.html`.
4. Update the chapter count and remove the `empty-state` element once the first chapter exists.

The template is linked separately from the chapter list and is not counted as course content.

## Template features

- **Study View:** readable layout, section navigation, expandable recall answers.
- **A4 Print View:** paper-style preview with all answers and SVG labels visible. The preview indicates page width; the browser print preview determines pagination.
- **Print / Save PDF:** opens the browser print dialog. CSS requests A4 with 16 mm margins, hides navigation and controls, and keeps small diagrams and callouts together. Choose A4 and disable browser headers/footers in the dialog for best results. Long content can span pages.
- **Interactive SVG:** replace the inline SVG while preserving its accessible title and description. The example label toggle works with mouse, touch, and keyboard. Print always includes labels. For multiple diagrams, give them unique IDs and extend the script accordingly.
- **Math:** native MathML renders formulas without a CDN or network request in current browsers. Replace the formula placeholder with MathML, for example `<math display="block"><mrow><mi>a</mi><mo>=</mo><mfrac><mi>b</mi><mi>c</mi></mfrac></mrow></math>`. This is an authoring syntax example, not chapter content. Raw LaTeX is not automatically rendered.

Core text, links, formulas, and SVGs work without JavaScript. JavaScript enables the view switches, label toggle, and printing behavior. The print stylesheet exposes closed recall answers; the script additionally opens and restores them for printing.

## Files

```text
index.html              Shared chapter index
chapters/template.html  Reusable chapter structure
assets/styles.css       Responsive study and A4 print styles
assets/chapter.js        View, diagram, and print interactions
.nojekyll               Serve plain static files on GitHub Pages
```

## Source-linked revision inventory

[Browse the concept checklist](concepts.html): 163 first-pass revision checkpoints across six blocks, linked to 36 core lecture PDFs (2206 pages). These are tutor-defined study units, not an official count of unique examinable concepts. See [CONCEPTS.md](CONCEPTS.md) and [SOURCE_INVENTORY.json](SOURCE_INVENTORY.json). Shared `assets/site.css` controls the index and every chapter shell. Keep navigation and styling consistent when adding chapters.


## Full revision draft request — 25 October 2026

The user explicitly authorized generating all 163 checkpoint notes before individual chapter discussions, plus mapping both sample papers. This supersedes any earlier restriction against drafting undiscussed chapters. These are lecture-based review drafts, not summaries of conversations that have not happened or proof of mastery. Keep subsequent tutoring one concept at a time and update the same pages with the user’s understood wording.

Open notes.html for six teaching blocks and sample-papers.html for 28 question-part maps. HMM and SVM are explicit sample-paper additions beyond the 163 checkpoints. Source gaps and lecture inconsistencies are marked in affected notes. See REVISION_GUIDE.md and REVISION_BUILD.json. The sample discussions are study answers, not official keys; question focus was checked against original papers, including missing 5002 Q2(c). Keep the current compact shared design and routine publish workflow.


## Tutorial rebuild — user correction, 25 October 2026

The user rejected shallow checkpoint cards and browsing by lecture block. This supersedes the earlier all-notes structure. index.html (also concepts.html) is the searchable concept index. Every checkpoint opens a worked tutorial section inside a coherent problem-led chapter. Existing search, CF/MF and SVD/PCA pages are part of this same index, not separate privileged notes. notes.html is a compatibility copy of the index; former block pages point to the index.

Required depth: explain what the method does and why; trace a concrete worked example/calculation; show a meaningful mechanism diagram where useful; compare scenario choices; explain data/components/loss/evaluation as relevant; diagnose failure → cause → change → reason; give specific exam answer guidance. Do not recreate short generic cards or pad pages with repeated boilerplate.

Use sample questions as navigation tests: 5001 Q1(a) → intent/slots (dialogue state if relevant); Q1(b) → FAQ retrieval with representation, ranking, threshold/fallback and approved answer. These are related components but different questions. Map every part to the exact chapter section, not a broad lecture module. Preserve source gaps and distinguish proposed answers from official keys. The user authorized reorganizing/replacing previous generated pages. Keep future tutoring short and update these detailed pages with the user’s understood wording.



## Lecture visuals and topic-specific teaching — 25 October 2026

The user rejected the same seven-part text template for every concept. Choose the teaching form from the topic: graph/trace for search, matrix and arithmetic for factorization, plots and formulas for signals/statistics, network shapes and updates for neural models, and component/dataflow diagrams for architectures. Reuse or redraw actual lecture examples with exact PDF page references where available. Distinguish lecture values from newly illustrative values; never invent lecture provenance. Define every mathematical symbol and show substitutions, result and interpretation. Use tables for comparisons and intermediate steps. Do not add formulas to qualitative concepts merely for uniformity. Existing interactive examples remain. Old notes/ module bookmarks now resolve directly to the actual concept tutorial.
