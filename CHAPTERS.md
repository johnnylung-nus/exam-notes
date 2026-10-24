# Shared chapter register

Maintain this across chapter chats. Use the lecturer's chapter names and ordering when available; do not invent a 30-chapter syllabus.

| Chapter ID | Topic | Target page | Source references | Discussion / status |
| --- | --- | --- | --- | --- |
| cf-mf | Collaborative filtering / matrix factorization | `chapters/cf-mf.html` | Pending accessible lecture notes and sample paper | Draft generated 25 October 2026 at user request. Standard definitions checked against Google developer references; lecture wording and sample-paper alignment pending. |
| svd | SVD | `chapters/svd.html` | Pending accessible lecture notes | Draft generated 25 October 2026. Standard SVD/PCA definitions checked against NumPy and scikit-learn documentation; lecture check pending. "SVD explanation" chat ID: `6adbff4f-6618-83ec-9faa-e8d713d05e9f`. Only a partial discussion is readable. |

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
