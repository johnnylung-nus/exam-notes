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


## Problem-first exam lookup — 25 October 2026

The user requires a question-clue → problem → candidate model/method/technique → conditions → answer flow/modification → exact tutorial map. Maintain `problems.html` and `assets/problem-map.json` alongside the concept index whenever adding or changing concepts. Do not force the user to know the method name first or browse hundreds of concepts. Distinguish related components: intent/slots/state for task dialogue; FAQ retrieval for approved Q&A; frames/schema/inheritance for structured knowledge. Keywords narrow candidates; selection must be justified by required output, available data, assumptions and constraints. Preserve direct links and related sample-paper parts; keep the wording short and usable during the exam.


## Individual concept pages — 25 October 2026

Every existing checkpoint now has its own `concepts/<id>.html` page; use `CONCEPT_ROUTES.json` for the destination. The concept index, problem finder and sample-paper routes must open these pages directly. Explain the specific topic using lecture terminology and exact references, preserve its worked example/diagram/calculation and source caveats, and choose its own teaching order and headings. Do not replace it with a short summary card or expand it into a multi-concept chapter. Related concepts are links, not extra pages concatenated into the same lesson. Keep Study/A4 views and one-concept printing. Old grouped chapter URLs remain compatible; update the individual page first when tutoring that concept.


## Overall purpose — user's clarification, 25 October 2026

Summarise the lecture notes into clear, compact, exam-ready explanations in the user's understood wording. The deliverable is not merely an index, a formula list or a collection of cards. Each concept has its own tailored page. Use the lecture's terminology, notation, examples and diagram conventions; cite exact available source pages and preserve source gaps.

Choose the teaching tools that actually clarify that concept: graphics, formulas with defined symbols and worked substitutions, examples, process flows, charts, comparison tables and short bullets. Not every concept needs every format, nor the same section order. A visual or formula must explain a mechanism or help solve a question, rather than decorate the page.

Extend the lecture explanation into exam application where relevant: data preparation and data problems; architecture/components and flow; objective/loss and what it measures; evaluation and metric choice; parameter/hyperparameter tuning; model/method comparisons; overfitting diagnosis and handling with reasons; advantages, limitations and assumptions. Keep these tied to the taught concept and scenario constraints, not unexplained new syllabus material. Distinguish an inferred application or original illustrative example from a lecture claim. Use the sample-paper questions and required answer flows to check practical usefulness.

Maintain both routes: question/problem clues -> method candidates -> exact concept page, and concept-name lookup -> the same page. Keep mobile study and compact A4 printing. This clarification describes the content standard; creating separate pages or navigation alone does not establish that every explanation has met it. Continue correcting individual pages as the user reviews and discusses them.


## Drawings as a teaching priority — 25 October 2026

The user explicitly wants drawings as much as possible: use meaningful diagrams, flows, plotted relationships and worked visual traces wherever they make the lecture concept understandable. Do not treat a token diagram somewhere on a page as satisfying this requirement. Architecture/system concepts need visible labelled components, arrows identifying what flows, and feedback/learning boundaries where applicable. Read the actual lecture and relevant sample-paper drawings; preserve their labels and distinguish different frameworks. Cognitive-system c059 now has the Q2(h) eleven-role framework and complete case mapping, the lecture's internal architecture, and its world input/output loop. Show diagrams in the lesson itself, with readable labels and compact print sizing; do not hide essential drawings in collapsed text. Do not add decorative or redundant figures just to reach a count.


## Approved lecture review and quiz workflow — 25 October 2026

The Lecture outline is approved. Top-level order is fixed by the user: Machine Reasoning, Reasoning Systems, Cognitive Systems, PSUPR, PRMLS, ISSM. `lecture.html` follows actual lecture file/day and substantive page order, linking to the same existing individual concept pages as Concept index and Problem Finder. Never regenerate an alternative explanation for a lecture view. Review/quiz controls are separate from each concept's explanation article.

Provide 2–3 analytical, unambiguous, lecture-scoped MCQs per supported concept, with a clear correct/incorrect judgement and an explanation for every option after answering. Cite exact supporting lecture PDF pages. Sample-paper-only practice is labelled separately; unsupported sources are flagged rather than invented. Review ticks and quiz correctness are independent. Browser-local state holds review ticks, latest checked quiz answers and exam-pack selection.

Exam-pack exclusions remove topics only from combined printing; retain their notes and lecture navigation unless the user explicitly asks for removal. Do not auto-delete background topics on an assumed exam prediction. Wide desktop, responsive mobile and compact A4 portrait print use the same explanation. `exam-pack.html` loads selected existing pages at viewing time, not a second edited copy of the notes; printing omits quizzes and navigation. Future concept edits automatically flow into the next loaded pack. Maintain the lecture mapping and quiz bank when relevant content changes.


## CSP added to MR Day 1 — 25 October 2026

`concepts/extra-csp.html` fills the missing Day 1 CSP workshop (PDF pp.76–89): identify variables/domains/constraints, distinguish mandatory hard rules from soft preferences, and trace backtracking including undo/domain restoration. Uses the actual Singapore map-colouring prefix and labelled computed continuation, plus an original timetable example and N-Queens formulation. Hard/soft cross-reference is RS day3.pdf p.53, not a claim those labels were fully explained in MR’s CSP slides. Linked from all indexes and lecture order, with three MCQs. Keep CSP as one shared page.


## Plain-English terminology — 25 October 2026

The user says English terminology can be difficult. Explain unfamiliar terms with everyday words before notation, contrast easily confused terms directly, and show small examples. CSP now distinguishes “constrained” (has fewer choices) from “constraining” (removes others’ choices): MRV chooses the unassigned variable; LCV orders that variable’s values. Reference Day 1 PDF pp.83–85 and preserve the plain-language explanation when revising.


## First-use Chinese meaning aids — 25 October 2026

At the first visible occurrence of each technical term on each concept page, retain the English lecture term and add a very short Traditional Chinese meaning in parentheses. Choose the closest contextual meaning, not a literal word-for-word translation. Skip personal names, proper model names with no useful translation, and ordinary English where a translation would distract. Do not translate SVG labels if it would crowd or break a diagram; explain the term in nearby prose. Keep formulas, source citations, links and quiz answers unchanged. Apply this to new notes and future edits without asking again. The shared glossary is assets/term-translations.json; correct contextual exceptions rather than blindly substituting.

- Treat singular/plural forms, spelling/hyphen variants, related adjective/noun forms (heuristic/heuristics; admissible/admissibility), and an acronym plus its full name as one term family. Translate only the first occurrence of that family per concept page. Do not repeat the Chinese aid for later variants. See assets/term-variants.json.
