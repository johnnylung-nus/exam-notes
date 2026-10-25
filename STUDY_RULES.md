# Exam study agreement

Last updated: 25 October 2026 (Asia/Singapore).

## Purpose

Act as the user's tutor. The goal is understanding and application in scenario-based exams, not long academic passages. Discuss one chapter per Exam project chat, while maintaining the same exam-notes website across 30+ chapters. The user should not repeat style or workflow preferences.

## Source discipline

- First consult the relevant uploaded lecture notes and sample exam papers. Record exact filenames and slide/page references for chapter claims, diagrams, and formulas.
- Prefer the lecturer's terms, symbols, methods, and visual conventions. Reproduce the relationships in a similar or clearer original SVG; do not silently change the meaning.
- Do not add unfamiliar concepts or new terms beyond the lectures unless requested. Explain the lecturer's existing terms plainly.
- Use the chapter discussion to identify what needs clarification, but verify technical takeaways against the lectures. Correct earlier chat mistakes rather than copying them.
- If files or earlier messages cannot be accessed, say exactly what is missing. Do not fill the gap with a generic internet chapter or invented source references.
- Distinguish provided sample questions from newly written practice questions. Do not claim a generated question is an actual exam question.

## Conversation style

- Short, direct bullet points. Answer the question asked, usually in 2–5 points; extend only when needed or requested.
- One concept at a time. Allow the user to explain it in their own words before moving on.
- Give a clear verdict: **Correct**, **Incorrect**, or **Partly correct**, followed by the exact correct and incorrect parts. Do not use reassuring "almost, but..." language that obscures an error.
- If an answer depends on an assumption, name the assumption. Never mark an incorrect statement correct for encouragement.
- Use plain explanations. Introduce only the minimum necessary lecture terminology and explain it when unclear.
- Give examples only when asked. Do not automatically add analogies, worked examples, practice scenarios, or quizzes.
- When the user requests a question, ask one and wait for their attempt. Do not reveal the answer prematurely.
- Track repeated misconceptions and unresolved questions; revisit them when relevant without claiming mastery from one correct response.

## Exam focus

Use these as a relevance checklist, not a compulsory lengthy response structure. Match the sample papers when accessible:

1. Understand the complete scenario: objective, available data, constraints, and assumptions.
2. Select or assess a proposed model and explain why it fits the task.
3. Identify limitations, invalid assumptions, and failure modes.
4. Identify data problems and explain suitable remedies.
5. Suggest modifications and justify how they address the problem.
6. Understand or design architecture using the lecture's components and notation.
7. State the loss/objective, explain its terms, and distinguish training loss from evaluation metrics.
8. Choose evaluation methods and explain what the results mean.
9. Apply simple analytical mathematics, show essential working, and interpret the result in the scenario.

Cover only the items relevant to the chapter. Do not invent evaluation, architecture, or loss sections for topics where they do not apply.

## Shared HTML notes

- Repository: `johnnylung-nus/exam-notes`.
- Canonical local checkout currently: `C:/Users/cklun/Documents/Codex/2026-10-24/create-a-minimal-html-exam-notes/outputs/exam-notes`.
- Keep one chapter index at `index.html`, with chapter pages under `chapters/`. "Same HTML" means the same shared website and template, not a separate project per conversation.
- Stable chapter slugs avoid duplicates. Register new chapters in `CHAPTERS.md` and link published pages from the index.
- Use white background, clean system sans-serif text, compact headings, neutral colors, short bullets, readable formulas, and useful original SVG diagrams. Preserve mobile support, Study View, and A4 Print View. No React or complicated framework.
- Reuse `chapters/template.html`, `assets/styles.css`, and `assets/chapter.js`; do not redesign every chapter.
- During discussion, save meaningful corrected takeaways to the relevant chapter when sources and file access permit. Do not dump every conversational turn into notes or expand undiscussed chapters automatically.
- Notes should prioritize: concise concept summary, essential notation/formulas with meanings, requested diagrams, relevant exam reasoning, and corrected misconceptions. Include examples/practice only if requested.
- Keep reference filenames/pages with each chapter. In-progress content must be clearly marked; never label it lecture-verified or complete without evidence.
- Update the shared index and register after chapter changes. Preserve other chapters. Record unresolved points and the next concept for handoff between chats.
- Keep lecture files read-only. Do not upload whole source documents or raw private conversations to a public repository.

## Autonomy and updates

- Make routine implementation decisions and edits without repeatedly asking permission. Ask only for missing essential information or required authorization.
- When more guidelines arrive, update this agreement and the reusable project instructions; do not require the user to restate old rules.
- Check the actual source and repository state. Distinguish local changes, committed changes, pushed changes, and deployed changes.
- If separate chats edit simultaneously, avoid broad rewrites and coordinate around current files; never discard another chat's changes.

## Cross-chat setup

Repository AGENTS.md applies to Codex sessions working in that repository. It does not itself change ChatGPT project settings. Add `../EXAM_PROJECT_INSTRUCTIONS.md` to the Exam project's instructions once, so separate Chat and Work chats receive the same agreement and destination. Files created in a local project mirror are not automatically uploaded or synced into ChatGPT project instructions.

## Current access limits

- The local Exam mirror's `sources/` directory was empty when checked on 24 October 2026. This does not prove the uploaded files are absent from the ChatGPT project; they are not accessible through this mirror in this session.
- The chat reader returned five recent exchanges from "SVD explanation" and opaque references in place of assistant response bodies. Full SVD/CF/MF coverage is not verified.
- CF/MF and SVD drafts were generated at the user’s explicit request to proceed despite unavailable lecture sources. They are standard-concept drafts, not lecture-verified notes. The pages visibly state this; verify against uploaded lectures when access is available.
- GitHub push and Pages deployment succeeded on 25 October 2026. Live index: https://johnnylung-nus.github.io/exam-notes/ . Continue using this repository and live URL; do not repeat the earlier authentication blocker without new evidence.

## 25 October 2026 update: publishing preference

- The user explicitly authorizes routine generation, website edits, commits, and pushes to `johnnylung-nus/exam-notes` without a separate approval conversation each time. After chapter discussion, update the corresponding chapter and index and push when access permits.
- Prefer showing the updated webpage and a concise outcome over explaining Git procedures. Do not claim that access is missing merely from an older failure: retry when the user says access has been granted.
- For this initial CF/MF and SVD generation, proceed with standard-concept draft notes even though lecture access is unavailable. Keep the draft/source status visible; replace external terminology with lecture terminology once verified. This exception does not authorize inventing lecture citations.

## 25 October 2026 correction: conversation-based exam cheat sheets

The README section "Read this before writing any chapter notes" is the shared checklist for this correction. Read it before creating or revising any chapter.

- Base notes on the actual relevant chapter conversation, in the user's own understandable wording, with specific errors corrected and claims checked against lecture material.
- Keep CF/MF and SVD/PCA in separate chapters AND separate print sheets. They solve different problems. The user rejected the combined print mockup.
- Organize the CF/MF cheat sheet around definitions and relationship, recommendation problem, steps with discussed examples, data processing/sparsity remedies, training objective in plain words, evaluation, overfitting prevention, and scenario-based modifications with reasons.
- No unexplained symbols such as Ω, new jargon, or formula-table substitution for understanding. Formulas require a purpose, symbol definitions, interpretation, and user understanding.
- The user has explicitly requested examples in the CF/MF sheet. Continue to avoid unsolicited examples in ordinary tutoring unless requested.
- The initial generic CF/MF and SVD drafts were not accepted as satisfying the user's exam-note needs. Their existence is not evidence of approved content or an approved template. Rewrite from conversation and lectures as access permits; do not silently treat the old one-off generation exception as permanent.
- Preserve the user's compact navigation/card references and separate screen/print layouts. Further website redesign remains in the mockup-review phase.

## Source access and common design — 25 October 2026

- The synced Exam mirror is empty, but lecture PDFs were located in the local NUS Semester_1 ISY5001 and ISY5002 course folders through file references in the other Exam chat. Do not keep reporting all lecture materials inaccessible; check the actual source paths. Treat originals as read-only.
- `CONCEPTS.md` links the first-pass study checkpoints to lecture filenames and PDF pages. The page total covers selected core lecture files only, not the entire uploaded project or all exam material. No claim is made that every checkpoint is a distinct examinable concept.
- Index and chapter pages must load the same shared site stylesheet and use the same chapter menu. New chapter work must preserve other chats’ additions and update this menu consistently.


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


## Editable terminology source — 25 October 2026

`downloads/TERM_TRANSLATIONS.csv` is now the authoritative editable list, replacing the earlier JSON files as the input. One row is one term family. `Term` is its representative English term; `Variants` lists aliases separated by semicolons; `Chinese hint` is the short inline aid. `Plain meaning` and `Example (reference only)` help the user review the vocabulary and are not inserted into notes. Delete a row or set `Enabled` to `no` to remove its inline translations; add a row to introduce a family; edit the hint to change its wording. Rebuild using `python tools/apply_term_translations.py`, verify, then publish. It removes old hints first, so deleted rows do not leave stale translations. The JSON lists are generated outputs; do not edit them as the source.

Generalize from the user's examples: prioritize unfamiliar English meaning, reasoning relationships, model components, data operations and easily confused terminology, not merely formal algorithm names. Use a concise Traditional Chinese meaning, optionally a very short functional clue when the formal translation alone is unhelpful. Use one aid per family per concept page. Preserve the English for exam recognition. Avoid personal-name translations and unnecessary ordinary-word annotations. Resolve context-sensitive meanings explicitly (e.g. neural bias versus statistical bias). User examples illustrate the desired teaching style and are not an authoritative answer key: correct inaccuracies rather than copying them. A* heuristic does not inherently sacrifice optimality; admissibility matters. Backpropagation computes gradients; the optimizer updates weights. AI hallucination means unsupported generated output. Skip unclear labels such as 'Brain class' until their source meaning is known. No new concept page or syllabus extension is authorized merely because a term is listed.


## Chinese vocabulary scope clarified — 25 October 2026

The user wants the existing English technical vocabulary plus missing vocabulary found in the webpages and lecture notes to receive a Chinese term/translation or very short Chinese meaning. Their pasted list is a selection guide, NOT a complete whitelist and NOT a request to replace the Chinese list with English explanations. Search the actual notes/lectures for missing vocabulary, choose the closest contextual Chinese aid, keep English visible, and avoid unnecessary variants. The editable CSV now has four columns: Term, Variants, Chinese hint, Enabled; this supersedes the earlier extra English-meaning/example columns. Keep variant grouping behind one representative term. Rebuild and publish after user edits; deleting rows or setting Enabled=no removes their hints. Do not label mathematical variable names or ambiguous abbreviations as technical terms merely because their spelling matches. Existing formulas, figures, examples and sources must remain intact.

This pass searched the extracted text of all 36 core lecture PDFs and all 167 concept pages. It added 198 term families and revised 26 existing families, for 598 editable families. This is a vocabulary coverage pass, not a claim that image-only lecture labels have all been exhaustively reviewed. Work/source audit: work/chinese-hint-source-audit.json in the current task workspace; do not publish source lecture text.


## Exam-paper vocabulary — 25 October 2026

Include unfamiliar technical and scenario terms from BOTH sample papers, not only lecture/model terminology. The 5001 and 5002 page-labelled paper extracts and their SAMPLE_QA study discussions were checked for this pass; the discussions are not official keys. Added 80 missing term families (678 total), including qualitative, derived variable, clickstream, loadings, movement envelope, differential diagnoses and wavelet transformation. Translate exam-case meanings precisely: Revenue is a binary completed-purchase label here; spatial-domain follows the paper's terminology; bins may refer to histogram intervals or physical collection containers. Avoid applying clinical 'sign' translations to mathematical signs. Keep technical English, compact Traditional Chinese meaning aids and first-use family deduplication. The editable source remains downloads/TERM_TRANSLATIONS.csv. Do not publish the original paper text or private tutoring record. Image-only labels have not all been exhaustively checked in this vocabulary pass.


## First-use abbreviation full forms — 25 October 2026

At the first prose/heading use of a technical abbreviation on EACH concept page, show its English full form in brackets beside it, alongside the short Chinese hint when that family first appears. Example: CSP (Constraint Satisfaction Problem；約束滿足問題). Do not assume an acronym is self-explanatory merely because its Chinese translation was given. Expand the abbreviation once even if its term family appeared earlier in full English; do not repeat existing adjacent full forms. Keep later occurrences compact. Use verified contextual expansions, never invent expansions of proper model names, mathematical variables, file codes or course identifiers. Do not crowd SVGs or alter formulas. The editable CSV now adds Abbreviations and Full form columns; this supersedes the four-column schema. Rebuild with tools/apply_term_translations.py; preserve source content and publish routine updates. Initial pass supplies 94 abbreviation/full-form definitions.
