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


## KG traversal must be explained, not listed — 26 October 2026

The Day3 traversal section includes definition (PDF24), seven-type table (25), incomplete graphs (26), roster/FIBA/Olympics application (27–33) and limitations (36). c022 now explains these mechanisms with a small labelled teaching graph and keeps original reference slides. Distinguish query shape/conditions (one-hop, multi-hop, conjunction) from exploration strategy (DFS, BFS, weights, random walk); they can be combined. BFS minimizes hops only under the relevant equal-cost convention, not arbitrary weighted cost. Random walks sample paths; they do not guarantee exhaustive retrieval or shortest paths. Missing graph facts are not real-world negatives. Link to existing algorithm explanations instead of duplicating whole chapters.


## TransR limitation coverage — 26 October 2026

Keep all four lecture p.55 points explicit: Increased Model Complexity; Computational Overhead; Limited Interpretability & Scalability; Risk of Overfitting. Explain each through relation-specific projection matrices, not a generic disadvantage list. Complexity means additional parameters/choices; overhead means projection operations; interpretability means learned coordinates/matrices are not naturally human-readable; scalability concerns storage/candidate-processing costs; overfitting is particularly relevant for sparsely observed relations. c024#transr-limitations provides the consolidated table and exam implication, replacing duplicate generic implementation prose.


## Tensor foundation — 27 October 2026

The user needs elementary concepts that lecture terminology assumes. Tensors and Shapes now has a dedicated page extra-tensors, placed before RESCAL/DistMult in MR Day3 with a clear foundation label. Explain scalar0D/vector1D/matrix2D as special tensors; tensor is NOT restricted to3D+. Distinguish axis count, shape, element count, matrix rank and embedding dimension. Connect H×W×C image shapes and E×E×R knowledge-graph tensor slices to their actual meanings. Mark tutoring examples as such rather than invented lecture claims. Existing neural/KG pages link to the same foundation page.


## Exam keyword emphasis — 27 October 2026

All concept explanations need short highlighted exam phrases: core mechanism, contrast, assumption, limitation, data issue, metric and selection clue. Use strong.exam-keyword: bold/pale emphasis on screen, bold black without colour fill in print. Prefer decisive phrases over repeatedly highlighting model names. At most three new highlights per paragraph/bullet/table cell; no full-sentence highlighting. Do not alter formulas, SVGs, references or existing bold text. EXAM_KEYWORD_REVIEW.json records coverage across174 concept pages. Text preservation was verified by removing added markup and comparing with original content. This is a presentation pass, not a new source-completeness claim. Maintain this emphasis during future edits.


## Lecture-style exam presentation — 27 October 2026

Bold keywords alone do not make a long paragraph usable in an exam. Prefer short points with one idea each; explicit Pros / Cons; compact comparisons; and cause → consequence. Keep the lecturer’s key terms and make the decisive contrast visible before examples. c025 was rewritten accordingly: full matrix vs diagonal, cross-dimension vs matching-dimension interactions, symmetry limitation, memory/computation/scalability. Put secondary mathematical caveats in deeper detail; do not reproduce a source error without clarification. This supersedes retaining long prose merely because highlights have been added.


## Exam-reading restructure applied — 27 October 2026

A request to improve the notes must cause concrete webpage edits, not another acknowledgement or only added bold text. Applied a presentation pass to all174 concept pages:305 long prose blocks split into short points;292 supporting implementation/model-answer sections moved into optional details. Keep core mechanisms, formulas, worked calculations and diagrams visible. Supporting detail is omitted from default printing; “Print supporting explanations” can include it on a concept or exam pack. Existing section anchors remain; incoming hash links open the needed details. This structural pass retains the technical wording; do not call it a new complete lecture-source audit. EXAM_READABILITY_REVIEW.json records per-page changes.

Begin concise explanations with what a concept DOES, its input/output and decisive mechanism, then the minimum useful example/formula with symbol meanings. c025 opens with triple → matching-coordinate products → sum → compatibility score. DistMult is hᵀRᵣt only when Rᵣ is diagonal; a general full relation matrix is RESCAL. Raw scores are not probabilities/truth and have no universal cutoff. Avoid appending duplicate summaries; replace/reorganize instead. The user’s example illustrates desired simplicity, not permission to repeat technical mistakes.


## Required presentation standard — 27 October 2026

Follow the user's reference for highlighting, point form, explanation logic and layout:
- Start with what the concept DOES, in one plain sentence; connect input → operation → output.
- Explain the meaning before notation. Give the formula only where useful, define every symbol, then show one concise example/calculation and interpret the result.
- Use short points, one idea per point. Bold the decisive exam keywords or contrast, not whole paragraphs or every technical word.
- Use a clear teaching sequence appropriate to the concept: purpose → mechanism → result → key limitation/choice. Do not impose identical headings or a compulsory template on unrelated topics.
- Make comparison, Pros/Cons, conditions and cause → consequence easy to scan. Use a compact table when it reduces reading.
- Keep the main exam answer visible and compact; put secondary explanation behind optional detail. Do not repeat the same definition, calculation or warning in several sections.
- Retain useful original lecture graphics and source notation; explain what the reader must notice. A copied slide is not a substitute for an organized explanation.
- Keep typography/spacing compact, mobile readable and A4 friendly, with clear hierarchy and no oversized decorative blocks.
- Preserve technical accuracy when simplifying: a compatibility score is not automatically a truth probability; DistMult uses a diagonal relation matrix. A reference shows presentation preferences, not an authoritative technical answer key.
This is a standing requirement across all concept pages and future conversations; apply it during editing, not only acknowledge it in chat.


## Default teaching flow — user's clarification, 27 October 2026

Use the lecture's teaching flow for concept pages:
1. **What is it?** Explain the concept plainly: what it does, the problem it addresses, and its key mechanism. Explain unfamiliar terms rather than only naming them.
2. **Calculation / worked example / graphics.** Where relevant, give the general formula, define every symbol, substitute values, and interpret the result. Prefer a clear original lecture example or diagram with its source; explain what to notice. Label added teaching examples. For qualitative topics use a meaningful worked scenario/flow instead of forcing an equation.
3. **Pros and Cons.** Extract the important advantages and limitations; state the reason and practical consequence in short points. Avoid generic lists unrelated to the mechanism.
4. **Used Cases:** Explain which problem/scenario it suits and why, using the lecturer's use cases where present. Include a short example and exam-selection clues; do not invent uses merely to fill a heading.

This is the default explanation sequence, not a requirement to create empty or irrelevant sections. Preserve topic-specific structure, short points, selective bold keywords, compact tables/layout and A4 readability. Do not duplicate material across stages or replace explanation with copied slides. Apply this flow during future edits and substantive revisions of existing pages.


## Full lecture outline and concept mapping audit — 27 October 2026
All 36 selected core lecture files were checked at source-section/page-reference level against the canonical Concept Index. Use lecture-review.json agenda sections and LECTURE_MAPPING_REVIEW.json. Preserve source headings/order; distinguish recap, workshop application, existing shared explanation and missing/partial coverage. Never infer completeness from a linked page or promote a passing mention to a main agenda topic. Existing concepts may recur across lectures but retain one canonical page and one saved review/print state. Reciprocal lecture references now appear in the indexes and concept-page context. This audit does not certify exhaustive correctness/completeness of all text, images, calculations or quizzes; recorded gaps must stay visible until resolved.


## Paper-only open-book exam lookup — 27 October 2026
The exam permits paper notes, pen and calculator; web search/click navigation is not available in the exam. Every topic must show a stable paper code, with scenario/keyword and alphabetical topic indexes printed at the front of the selected exam pack. assets/paper-index.json is the permanent code register: never renumber/reuse published codes when inserting/excluding topics. Six divider groups: MR Machine Reasoning, RS Reasoning Systems, CG Cognitive Systems, PS PSUPR, PR PRMLS, IS ISSM. Repeat the code beside subsection headings and show target codes on printed cross-references. Codes are topic locators, NOT physical page numbers; do not invent pagination. Preserve saved review/selection state. Index and dividers are navigation only, not duplicated explanations.


## Word exam notes are the preferred deliverable — 27 October 2026
The user requested editable topical Word files for a paper-only exam. See WORD_NOTES.md for the six subject files, master index and preservation rules. Preserve user edits; do not overwrite edited Word documents by rebuilding from HTML. All future exam navigation must work on printed paper using topic codes and real page references.
