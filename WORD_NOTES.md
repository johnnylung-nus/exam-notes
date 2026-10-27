# Editable Word exam notes

The user now prefers editable Word files for a paper-only exam. The website is not the primary exam deliverable.

Outputs are in the adjacent outputs folder `Exam Word Notes 2026-10-27`: six subject documents and `00 Master Exam Index.docx`. Each subject has a front index with native Word PAGEREF fields, numbered topics, a running topic header, page numbers, editable text/tables/OMML equations and embedded diagrams. The master maps scenario keywords and 28 sample-paper parts to topic codes and page numbers.

Preserve user edits in these Word files. Read the current file before editing. Never regenerate the documents from the website and overwrite the user's work. Keep existing stable topic codes. Follow the substantive lecture teaching order, not the first passing mention on an overview slide. The source-order appendix connects shared concepts across subjects.

Current scope: 178 topics. The unsupported transfer-learning extension is excluded; the HMM sample-paper addition is retained and labelled. Added lecture-based explanations cover explainability, LDA, DBSCAN and DTW. The Naive Bayes chapter includes joint versus conditional probability.

After edits, let Word paginate, then update the subject document's index fields. The separate master index has fixed page references for this edition; update its references when changing pagination. Do not invent page numbers or silently call a partial source audit complete.

Creation and QA working files are in the Exam project mirror under work/word-exam and work/build_word_notes.py. Synced lecture sources remain read-only. Rendering uses the packaged document renderer with the installed LibreOffice components and local Windows fonts. Deliver DOCX files, not intermediate page images or QA PDFs.
