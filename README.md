# Exam notes

A minimal, mobile-friendly chapter library built with HTML, CSS, and a small amount of vanilla JavaScript. No build tools, framework, or external runtime dependencies. No course notes are included yet.

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
index.html              Chapter index (initially empty)
chapters/template.html  Reusable chapter structure
assets/styles.css       Responsive study and A4 print styles
assets/chapter.js        View, diagram, and print interactions
.nojekyll               Serve plain static files on GitHub Pages
```
