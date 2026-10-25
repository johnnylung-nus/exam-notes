"""Generate the printable glossary from the editable CSV; no dependencies."""
from pathlib import Path
from html import escape
import csv,re

def generate(root):
    root=Path(root)
    rows=[r for r in csv.DictReader((root/'downloads/TERM_TRANSLATIONS.csv').open(encoding='utf-8-sig',newline='')) if r.get('Enabled','yes').strip().lower() not in {'no','false','0'}]
    rows.sort(key=lambda r:r['Term'].casefold())
    entries=[];letter=None
    for r in rows:
        initial=r['Term'][0].upper()
        if initial!=letter:
            entries.append('<h2 class="glossary-letter" id="letter-'+initial+'">'+initial+'</h2>');letter=initial
        term=escape(r['Term']);full=r.get('Full form','').strip();abbr=r.get('Abbreviations','').strip()
        extra=[]
        if abbr and abbr.lower()!=r['Term'].lower():extra.append(abbr)
        if full and full.lower()!=r['Term'].lower():extra.append(full)
        detail='<small>'+escape(' · '.join(extra))+'</small>' if extra else ''
        search=' '.join(r.values())
        entries.append('<div class="glossary-entry" data-search="'+escape(search,quote=True)+'"><dt>'+term+detail+'</dt><dd lang="zh-Hant">'+escape(r['Chinese hint'])+'</dd></div>')
    letters=sorted({r['Term'][0].upper() for r in rows})
    jumps=' '.join('<a href="#letter-'+x+'">'+x+'</a>' for x in letters)
    page='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>English–Chinese exam glossary · Exam notes</title><link rel="stylesheet" href="assets/site.css"><link rel="stylesheet" href="assets/glossary.css"><script src="assets/glossary.js" defer></script></head><body class="glossary-page"><a class="skip" href="#content">Skip to glossary</a><header class="masthead"><a href="index.html">Exam / glossary</a><span>English terms · Full forms · Short Chinese meanings</span></header><nav class="sheet-nav" aria-label="Main navigation"><a href="lecture.html">Lecture order</a><a href="problems.html">Problem → method</a><a href="index.html">Concept index</a><a href="sample-papers.html">Exam questions → concepts</a><a href="glossary.html" aria-current="page">Glossary</a></nav><main id="content"><header class="glossary-title"><h1>English–Chinese exam glossary</h1><p>'''+str(len(rows))+''' term families · English full forms beside abbreviations · 簡短中文意思</p></header><div class="glossary-tools"><label for="glossary-search">Find an English term, abbreviation or Chinese meaning</label><input id="glossary-search" type="search" placeholder="CSP, inference, 啟發式…"><div><button id="print-glossary">Print glossary · A4</button> <button id="clear-glossary">Show all</button> <a href="downloads/TERM_TRANSLATIONS.csv" download>Download editable list</a></div><p id="glossary-count" role="status">All '''+str(len(rows))+''' terms shown.</p><p>Printing uses two compact columns on A4. Clear the search to print the complete list; a search prints only matching entries.</p><nav aria-label="Glossary letters">'''+jumps+'''</nav></div><dl class="glossary-list">'''+''.join(entries)+'''</dl><p class="glossary-empty" hidden>No matching term.</p><footer>Short meaning aids for the lecture notes and sample papers. Interpret context-sensitive terms using the linked concept notes.</footer></main></body></html>'''
    (root/'glossary.html').write_text(page,encoding='utf-8')
    return len(rows)

if __name__=='__main__':generate(Path(__file__).resolve().parents[1])
