# Shared chapter register

Maintain this across chapter chats. Use the lecturer's chapter names and ordering when available; do not invent a 30-chapter syllabus.

| Chapter ID | Topic | Target page | Source references | Discussion / status |
| --- | --- | --- | --- | --- |
| cf-mf | Collaborative filtering / matrix factorization | `chapters/cf-mf.html` | Pending accessible lecture notes and sample paper | Draft generated 25 October 2026 at user request. Standard definitions checked against Google developer references; lecture wording and sample-paper alignment pending. |
| svd | SVD | `chapters/svd.html` | Pending accessible lecture notes | Draft generated 25 October 2026. Standard SVD/PCA definitions checked against NumPy and scikit-learn documentation; lecture check pending. "SVD explanation" chat ID: `6adbff4f-6618-83ec-9faa-e8d713d05e9f`. Only a partial discussion is readable. |

| astar | A* search | `chapters/astar.html` | MR-Day 1_JR_v1.pdf, PDF pp.61–68 / slides 66–73 | Interactive lecture tree and six selections. Discussion in progress; no mastery claim. |

## Per-chapter handoff

When a chapter is discussed or updated, record:

- Source filenames and pages/slides actually read.
- Concepts discussed and corrected takeaways.
- Specific misconceptions to revisit.
- Unresolved questions and the next concept.
- Notes file and local/committed/pushed/deployed status, as verified.

Do not mark an untested concept mastered. Do not record personal details or raw chat transcripts here.

## Latest publication

- 25 October 2026: both draft chapters and the index pushed in `f38be80`; GitHub Pages deployment run `40109778105` completed successfully. Live index verified in the browser with both chapter links.
- Live SVD connection toggle and A4 view checked; local links, anchors, unique IDs, and JavaScript syntax passed checks.
- Public index: https://johnnylung-nus.github.io/exam-notes/ . Lecture and sample-paper source verification remains pending; do not label these drafts lecture-verified.

## Content correction and conversation handoff — 25 October 2026

- The user rejected generic/formula-led content and the combined CF/MF + SVD/PCA print sheet. These drafts are not approved exam cheat sheets.
- CF/MF: locate and read the relevant full chapter conversation; its exact chat title and full content have not yet been verified in this session. Rewrite in the user's understood wording: CF/MF relationship, recommendation problem, steps with examples, evaluation, overfitting prevention, sparse/missing-data issues and remedies, and scenario-based justification.
- SVD/PCA: keep separate. The known source chat is "SVD explanation" (`6adbff4f-6618-83ec-9faa-e8d713d05e9f`); the reader previously exposed only five recent exchanges and opaque assistant-message references. Do not claim full-discussion access.
- For each future update, record the conversation actually read, concepts/examples carried over, corrected misconceptions, lecture pages checked, unresolved questions, and next concept. Do not publish raw transcripts.
- This handoff records the corrections; it does not claim that chapter content has already been rewritten or redesigned.

## CF/MF rewrite — 25 October 2026

- Replaced the initial formula-led CF/MF draft with a scenario-based cheat sheet and a separate CF/MF-only 2-page A4 PDF. SVD/PCA remains a separate chapter and was not rewritten in this update.
- Read this chat's requested coverage and corrections. No full earlier CF/MF discussion or uploaded lecture was accessible; the illustrative movie/factor/metric examples are newly written and explicitly labelled as such.
- Covers CF/MF relationship, problem, steps with reasons, worked predictions and errors, sparsity/cold start, evaluation, overfitting remedies, and problem/change/reason answer patterns. Removes unexplained Greek notation.
- PDF generated at 9.3 pt in two columns; both pages rendered and reviewed. Sources checked: Google recommendation documentation, Surprise MF documentation, scikit-learn metrics and leakage guidance. Lecture-specific validation remains pending.
- Next discussion: check the step explanations and examples against the actual chapter conversation and lecture wording; revise specific misunderstandings from the user's feedback.

## A* handoff - 25 October 2026
Based on the A* exchanges in Machine Reasoning chat 01a0e888-799b-76b2-a31f-9bce1f7533bc. Discussed actual g versus estimated h/f; frontier means all waiting nodes; switching branches is not physical backtracking. User requested lecture-style step graphics. Source extraction pp.61–68 checked; sample papers not checked. Next: let user inspect the branch switch and stopping rule. New page uses existing shared styles without redesigning other chapters.

## Search comparison extension - 25 October 2026
User requested Hill Climbing and Dijkstra graphics plus slide 74 summary. Added chapters/search-comparison.html, linked from A* and the index. Same Machine Reasoning discussion; read PDF p.41, pp.51–58, pp.61–69 and visually checked map p.52 and comparison p.69. Hill Climbing follows the deck's best-child version; its broader greedy-best-first label is explicitly distinguished. Dijkstra trace independently calculated from lecture map: 13 selections through Bucharest, final cost 418; Hill Climbing 4 selections, cost 450. Source slide trace vs derived trace labelled. Next: user review of g-only versus h-only choices and selection order versus final route.
Validation: calculated expected selections/costs; next/previous/method reset passed. Final trees rendered and visually checked at 736px and 280px. Actual browser A4 pagination has not been verified; no page-count claim.
User-requested reminder: Dijkstra is uninformed; Hill Climbing and A* are informed because they use h. Added to the screen/print comparison table (Day 1 PDF p.71 / slide 76).
User-highlighted exam cue: Search = Reasoning Engine. Added exact wording plus State space + Actions + Goal + Evaluation, sourced to Day 1 PDF p.71 / slide 76; applies to this search framing, not a claim that all reasoning is search.
Added requested summary of State/state space, Actions, Goal and Evaluation; distinguished goal achievement from solution quality and connected evaluation to g/h/g+h. Source Day 1 PDF pp.27,30,71. Saved locally; publication remains pending after automatic approval review failed due to a usage limit.


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
