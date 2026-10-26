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


## Printable glossary — 25 October 2026

`glossary.html` is the user's searchable, printable English–Chinese exam glossary, linked from the shared navigation. It displays one row per enabled term family, with full English expansions beside abbreviations and compact Chinese hints. It has an A4 portrait two-column print stylesheet; screen controls/navigation do not print. A search filters the printable entries; Show all restores the complete glossary. `tools/generate_glossary.py` generates it from downloads/TERM_TRANSLATIONS.csv and is called by the translation rebuilder. Keep this page synchronized whenever editing terminology. Do not claim an exact printed page count without actual print pagination. Preserve existing concept explanations and reviewed/quiz/print-selection browser state.


## Resume lecture outline — 26 October 2026

On ordinary Lecture order visits, use saved Reviewed ticks to expand only the first unfinished lecture and its parent section; collapse completed/other lectures. Do not hard-code MR Day 1 open. Explicit concept, quiz or anchor links take precedence. This changes only the initial outline view, never Reviewed ticks, quiz results or exam-pack selections. Do not automatically collapse the current lecture while the user is ticking concepts.


## Exam-ready mathematical layout — 26 October 2026

Use proper typeset fractions, summations, subscripts and superscripts for examinable mathematical formulas; a slash-separated string or only a numeric example is insufficient when the user must substitute new exam values. Immediately below each general formula define EVERY symbol in short, clear language, including indices, counts, denominators, units and conventions. Then retain/show the worked numerical substitution and interpretation. Bayes uses P(H|D)=P(H)P(D|H)/P(D), with posterior/prior/likelihood/evidence roles and a summed evidence denominator when not supplied. Prefer lecture notation and preserve its stated convention; explicitly distinguish any standard restatement or correction. Do not add formulas to qualitative topics for uniformity or turn notes into a formula table. Native MathML is used here, with no external framework/CDN. Keep inline Chinese glossary inserts out of mathematical notation; explain jargon in nearby prose/definitions. Formula blocks must remain legible on mobile and A4, including exam-pack printing. FORMULA_REVIEW.json records the 167-page review and 61 typeset pages; it does not assert every image-only lecture equation was exhaustively compared. Original worked steps remain intact.


## Preserve lecture section scope — 26 October 2026

The user flagged Forms of Knowledge Representation as important exam material. Do not replace a lecture overview/list with one narrow subtopic. MR Day 2 section 2.2.1 has an opening list and ten developed forms: logical, rule-based, semantic networks, frames, ontologies, constraint-based, probabilistic, case-based, vector/embedding, knowledge graphs. The full overview now lives at concepts/extra-knowledge-representation.html, with lecture examples, comparisons and sample-question application. Day 2 links this overview, not the detailed first-order logic page. Keep c017 under MR Day 4, where its rainy-day predicate example is actually taught. Broad section headings must retain their full scope and lecture list before linking existing detail pages; never imply an arbitrary extracted checkpoint is the whole lecture topic. Explain representation versus inference and give scenario-based selection reasons. PDF viewer page numbers differ from printed slide numbers; preserve section title and exact references without dismissing the user's pointer.


## Exact lecture title and worked-example provenance — 26 October 2026

Use the lecturer’s title Probabilistic Reasoning: Bayesian Inference for c016 (MR Day 2 PDF pp.40–41, printed slides 41–42). The men/women, long/short hair example is the lecture’s worked example, not a newly invented toy example. Keep the 0.5, 0.04, 0.50 inputs and 0.02/0.27 result; the lecture rounds it to 7%. If displaying short-hair complements, label them calculated complements. Preserve source provenance clearly; do not rename lecture topics into generic AI labels or describe source examples as newly illustrative.


## Original lecture visuals and revision wording — 26 October 2026

The user explicitly prefers reusing the lecturer's ORIGINAL graphics because they recognize them from class. Use a clear original diagram/crop with exact PDF page/slide attribution by default. Redraw only when the original is messy, too large/complex, unclear, or needs an explicitly labelled extra explanation. Keep the original available in those cases. This supersedes the earlier default instruction to redraw diagrams; do not copy full PDFs or raw private conversations. Preserve source materials read-only. Semantic Networks c018 now uses the original MR Day 2 PDF p.50 / printed slide 51 graphic, with a full-slide link and an optional old alternative illustration excluded from printing. Explain MemberOf versus SubsetOf, relation direction, property values and John's explicit Legs=1 exception. Add drawing steps where exam wording requires them.

Checked original 5001 sample: Q1(c) requests frame schema, Q2(c–d) request architectures and knowledge structures; it does not explicitly request a semantic-network drawing. Generated 5001 Practice B Q1(b) does request a semantic network/knowledge graph; label it practice, not official. The user's Exam_Revision guides contain useful scenario-wording routes and answer flows. 88 clues from 5001_CHEATSHEET.md, 5002_CHEATSHEET.md and 5002_CONCEPT_REFERENCE.md have been integrated into the SAME searchable Problem → method finder, with exact concept destinations and short source names. PERSONAL_QUICK_REVISION.md supplies command/target/output and distinction reminders, not raw personal attempts/scores. REVISION_CUE_IMPORT.json records mappings. Existing practice/review files are evidence to check, not instructions to execute. Preserve source gaps; related context is not a dedicated explanation of a missing model. Resolve relative image URLs when importing concept content into the printable exam pack.


## Example placement — 26 October 2026

Keep Canary/Bird/Animal with Ontologies c020 for the user’s revision. Semantic Networks c018 uses the lecturer’s original Mary/John/Persons/Mammals diagram and matching worked discussion. Do not mix the Canary example back into that page. The source comparison slide shows several representations; do not imply subclass hierarchies are theoretically exclusive to ontologies.


## Knowledge representation: examinable output formats — 26 October 2026

For every knowledge-representation form, include the format the student must DRAW or WRITE, not merely its definition or suitability. The overview now links ten format sections: logic/predicates and symbols; IF–THEN rules; semantic-network nodes/labelled edges; frame records/slots/fillers/inheritance; ontology classes/properties/axioms; CSP variables/domains/constraints; probabilistic nodes/dependencies/conditional probabilities; case records; vector representations; and knowledge-graph triples. Each has a concrete lecture-linked structure, symbol definitions and short exam-production instructions. Original lecture slides are included at the existing detail pages, with exact PDF/printed-slide references. Preserve what the slide actually supplies; mark any instantiation, extra field or missing numerical table rather than inventing lecture facts. Vector representation is explained in the overview rather than incorrectly linked as if neural graph embeddings were its complete explanation.


## Superseded: relationship-label emphasis — 26 October 2026 (see latest core-concepts rule below)

The user primarily needs to identify and apply MemberOf (individual→group), SubsetOf (group→broader group), HasMother, SisterOf and attribute/value links such as Legs. Keep c018 tightly focused on the original Mary/John diagram, relationship meanings, direction, valid readings and mistakes. Remove ontology-selection discussion and unrelated official frame question Q1(c) material from this concept page. Its two quizzes now test these exact link distinctions and the individual property shown for John. Do not attach a sample question to a concept merely because both mention relationships or inheritance.


## Three-page source audit — 26 October 2026

Compared Semantic Networks, Frames and Ontologies to original MR Day 2 PDF pp.50–53, including visual review of the comparison slide. Keep semantic-network teaching on Mary/John and relationship identification; Frames on the Person record, slot/filler terminology, Bird defaults/unknowns and the explicitly labelled proposed Q1(c) schema; Ontologies on formal classes/properties/constraints, the exact university inference and Canary axiom notation. Do not invent Academic subclass Person: infer Alice Academic from Professor subclass Academic and Alice Person from the separately drawn Professor subclass Person. Do not imply an unusual property endpoint automatically proves logical inconsistency without declared constraints. The original comparison slide DOES use Canary in multiple representations; do not falsely claim Canary can only be represented in an ontology. It remains under Ontologies in this user's site organization. Retired the stale grouped chapter copy so rejected examples do not reappear through old pages. c018 quizzes use the Mary/John relations; c019-q2 now tests Fly(default) and Diet=? instead of an unrelated patient-diagnosis task. Source examples, proposed exam applications and optional context must be clearly distinguished.


## Semantic Networks core concepts — latest user correction, 26 October 2026

This supersedes the earlier 'Semantic-network learning target' emphasis on individual relationship labels. The important lecture concepts are INHERITANCE and GRAPH TRAVERSAL. Explain both in plain English with short Chinese meanings, using the original Mary/John graph. MemberOf, SubsetOf, HasMother, SisterOf and Legs are example relationships; the user understands them from the graphic and does not want repeated long explanations of each label. Traversal is following appropriate links to find information; inheritance is obtaining applicable category knowledge/properties while respecting explicit exceptions. Do not copy properties through arbitrary relations. Keep the page compact and the quizzes focused on these core mechanisms. When the user asks for clarification during tutoring, save the useful clarification to the relevant webpage, not just the chat.


## Use cases are examinable teaching content — 26 October 2026

Keep the use cases NAMED BY THE LECTURER. A bare technical name is insufficient: explain its meaning in plain English with a short Chinese aid, give a brief concrete example, and connect the scenario requirement to why the representation/method fits. The user explicitly requests examples here; this overrides the generic 'examples only if asked' restriction for these use-case explanations. Stereotypical scenarios means familiar/typical situations with usual roles/properties/defaults, not social prejudice. A hotel-room frame is a labelled teaching example; actual slot values and exceptions override defaults. Do not treat a use-case keyword as proof of suitability or claim generated scenarios are actual exam questions. This pass expands the lecture use cases across all ten knowledge-representation forms using MR Day 2 PDF pp.48–58. Knowledge Graph p.58 provides university entities/facts as its example rather than a separate use-case bullet list; label it accordingly. Save useful tutoring clarifications to the webpages, not just chat.


## Use-case heading wording — 26 October 2026

Use the exact heading **Used Cases:** on knowledge-representation pages. Do not use headings such as “The lecture’s uses, in plain words” or “The lecture’s use cases: meaning and scenario clues”. Keep the explanations and examples beneath this concise heading.


## Complete representation sequence — 26 October 2026

MR Day 2 must explicitly include Constraint-Based Representation (PDF p.54), Probabilistic Representation (p.55), Case-Based Representation (p.56), and Vector / Embedding Representation (p.57) AFTER Ontologies and BEFORE Knowledge Graphs (p.58). Each now has its own representation page with original lecture image, format, meanings and Used Cases. These describe knowledge representation; the linked CSP/backtracking, Bayesian inference and case-based reasoning pages explain the associated procedures. Their representation-format and Used Cases content was moved to the canonical representation pages rather than rewritten in multiple places; old anchors link onward. Maintain the complete lecture order and Previous/Next links across this sequence.


## Bayesian Networks restored — 26 October 2026

Bayesian Networks is a substantive MR Day 2 lecture topic, PDF pp.71–84; it must not be omitted or treated as only a mention under Bayesian inference/probabilistic representation. Canonical page: concepts/extra-bayesian-network.html. Includes original p.72 network/CPT slide, DAG/CPT concepts, root priors, false complements, joint factorization, the burglary-given-JohnCalls calculation, distinction from Naive Bayes, design/learning and scenario use. Full calculation from given CPTs gives about1.63%; the lecture displayed intermediate approximations give about1.62%. Preserve and explain this rounding distinction. Day2 order places it after the p.67 decision-tree topic, following the source order. Do not describe the comparison to medical designs as a compulsory exam solution; use the actual question requirements.


## Extract and explain, do not merely copy — 26 October 2026

The website's value is extracting the IMPORTANT CONCEPTS from lecture material, explaining them clearly, organizing them for recall and exam use, and showing the differences that determine method choice. Original slides/graphics are references and memory aids, not substitutes for teaching. Keep the lecturer's terminology and scope; identify the key mechanism, explain unfamiliar words in plain English, give the requested short example, and connect it to exam scenarios. Naive Bayes must prominently explain its relationship to general Bayesian networks: it IS a special BN and assumes feature independence GIVEN the class. A general BN represents other dependency structures with local CPTs; it does not imply every variable depends on every other variable. Compare assumptions, factorization, probability requirements, parameter/data needs and inference, rather than listing two model names. Canonical comparison: concepts/c144.html#nb-vs-bn; link it from the BN page instead of maintaining separate conflicting explanations.


## Explain ROC AUC explicitly — 26 October 2026

Mentioning AUC or warning it is not profit is not enough. c140 must define ROC axes and threshold sweep, area under the curve, positive-versus-negative pairwise ranking (ties half), interpretation of1/0.5 and a numerical example; distinguish ranking from accuracy and probability calibration. Original reference is MR Day2 PDF p.90 / printed91, now included in lecture order. The tiny pairwise example is explicitly original teaching data.


## Editorial cleanup applied — 26 October 2026

Do not merely acknowledge requests to improve exam notes: make concrete edits. Repeated additions had bloated ROC/AUC and Naive Bayes. Removed repeated generic choice/design/model-answer sections and duplicate arithmetic while retaining the core explanation, symbolic formula/definitions, one full worked example, important limitations and exact source references. Contents navigation is regenerated from retained sections, with legacy anchor targets preserved. Semantic Networks, Frames, Ontologies and Bayesian Networks were checked for their distinct core teaching order; do not add a common boilerplate template back to make pages look uniform. Further edits should replace or consolidate an existing explanation where possible instead of appending another summary of the same idea.


## Avoid repeated Day 2/3 review entries — 26 October 2026

MR Day3 starts with a recap of Knowledge Graph structure (c021, PDF pp.8,10) and Ontologies (c020,p.10), already studied in Day2. Remove those two duplicate checklist rows from Day3; retain their source locations as recapReferences metadata. Day3 review starts at KG traversal and multi-hop queries, then TransE, TransR, DistMult and neural graph embeddings. Preserve the existing single concept pages and saved Reviewed state. Do not present a recap as another new topic to study/print.


## KG query patterns — 26 October 2026

Do not reduce Day3 query teaching to a generic multi-hop paragraph or only a drug example. Explain the three lecture p.19 patterns: one-hop (one relation), path/multi-hop (connected chain through shared intermediate entities), conjunctive (AND/intersection of conditions on the same candidate). Use the original slide and its basketball questions; do not invent real coach/owner/friend names. Define hop, conjunction, candidate set, intermediate variable and relation direction in plain words. Anonymous candidates are explicitly illustrative. A missing graph fact does not prove a real-world negative. c021 links prominently to the detailed c022 explanation; c022 preserves the drug/trial application only as optional further practice.


## Explain the disease/protein/drug/trial query — 26 October 2026

Canonical worked explanation: c022.html#drug-query, now in the main print/read flow. Start at the disease, traverse Associated With to proteins and Targeted By to candidate drugs, then retain the SAME drug with the Involved In Phase II trial condition. Define inverse verbal relation: Protein Targeted By Drug equals Drug targets Protein; do not reverse its meaning. Distinguish the two-hop path from the AND condition; output is Drug, not Protein/Trial. Anonymous records are labelled teaching examples, not medical assertions. A missing graph path is not a proof of real-world falsehood; a retrieved trial link does not establish cure, safety or approval. Use current status if required and supplied. Original source slide p.22 is included.
