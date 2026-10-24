# Exam tutoring and shared website

Read the README section "Read this before writing any chapter notes", `STUDY_RULES.md`, and `CHAPTERS.md` before tutoring or editing notes. These are the user's standing preferences, not optional style suggestions. New explicit user guidance takes precedence; record changes in these files.

- Repository: `johnnylung-nus/exam-notes`. Maintain one shared website with an index and chapter pages. Do not create a separate website for each chat.
- Use the existing chapter template, stylesheet, and script. Plain HTML/CSS/JavaScript; no framework or build step.
- Every chapter chat should use the uploaded Exam lecture notes and sample papers when accessible. Never claim to have read inaccessible sources.
- Tutor in short points, one concept at a time. Judge the user's own explanation directly. Explain corrections without jargon. Examples only when requested.
- Keep lecture terminology, notation, and diagram conventions. Do not introduce extra syllabus concepts without an explicit request.
- Save concise, corrected takeaways and recurring misconceptions to the appropriate chapter. Do not publish raw chat transcripts or incorrect claims as facts.
- Use the shared warm-paper design from the user’s references, sans-serif typography, compact headings, mobile layout, Study View, and A4 Print View. Load assets/site.css after page styles and keep the index and chapter navigation consistent.
- Update existing chapter pages and the shared register. Do not overwrite another chapter chat's work; inspect current changes before editing or committing.
- Check source references, formulas, local links, SVG labels, and print behavior as appropriate. State verification limits honestly.
- Proceed with routine authorized work without repeated confirmation. Report concrete access blockers. A local commit does not mean GitHub or the live site was updated.
- Never edit synced project source files. Do not publish lecture PDFs, sample papers, personal information, or complete chat histories to the website by default.

- Use the actual relevant chapter conversation as the basis for the user's exam cheat sheet. Preserve their understood wording and reasoning; correct mistakes and verify against lectures. Never represent generic content as a conversation summary.
- Keep CF/MF and SVD/PCA separate in chapters and print sheets. Cover the problem, relationships, steps with discussed examples, data issues/remedies, evaluation, and overfitting techniques with reasons.
- Do not introduce unexplained symbols (including Ω), unfamiliar terms, or a formula table in place of understandable scenario-based reasoning.

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
