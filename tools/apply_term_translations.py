"""Rebuild first-use Chinese hints from downloads/TERM_TRANSLATIONS.csv.
Delete/disable a row to remove its hints. UTF-8 CSV, no dependencies.
Run with Python from any folder. No commit or push is performed here.
"""
from pathlib import Path
from html.parser import HTMLParser
import csv,re,json

def rebuild(root):
    root=Path(root)
    rows=list(csv.DictReader((root/'downloads/TERM_TRANSLATIONS.csv').open(encoding='utf-8-sig',newline='')))
    expansions={a.strip():r.get('Full form','').strip() for r in rows if r.get('Enabled','yes').strip().lower() not in {'no','false','0'} and r.get('Full form','').strip() for a in r.get('Abbreviations','').split(';') if a.strip()}
    expansion_lookup={a.lower():v for a,v in expansions.items()}
    aliases={};hints={}
    for row in rows:
        if row['Enabled'].strip().lower() in {'no','false','0'}:continue
        name=row['Term'].strip();hint=row['Chinese hint'].strip()
        if not name or not hint:continue
        hints[name]=hint
        for term in [name]+row['Variants'].split(';'):
            term=term.strip().lower()
            if not term:continue
            if term in aliases and aliases[term]!=name:raise ValueError('Overlapping variant: '+term)
            aliases[term]=name
    pattern=re.compile(r'(?<![\w-])('+'|'.join(re.escape(x) for x in sorted(set(aliases)|set(expansion_lookup),key=len,reverse=True))+r')(?![\w-])',re.I)
    strip=re.compile(r'<span class="term-zh" lang="zh-Hant">.*?</span>',re.S)
    class Annotator(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=False);self.out=[];self.stack=[];self.seen=set();self.expanded=set();self.count=0
        def handle_starttag(self,t,a):
            self.out.append(self.get_starttag_text())
            if t not in {'br','hr','img','input','meta','link','source','wbr','area','base','embed','param','col'}:self.stack.append((t,dict(a)))
        def handle_startendtag(self,t,a):self.out.append(self.get_starttag_text())
        def handle_endtag(self,t):
            self.out.append('</'+t+'>')
            for i in range(len(self.stack)-1,-1,-1):
                if self.stack[i][0]==t:self.stack=self.stack[:i];break
        def handle_data(self,s):
            eligible=any(t=='article' for t,a in self.stack) and not any(t in {'script','style','svg','nav','button','code','pre'} or 'lecture-reference' in a.get('class','') or 'topic-related' in a.get('class','') for t,a in self.stack)
            if eligible:
                def sub(m):
                    key=m[0].lower();family=aliases.get(key);parts=[]
                    if key in expansion_lookup and key not in self.expanded:
                        full=expansion_lookup[key]
                        if not re.match(r'^\s*[(（]\s*'+re.escape(full),s[m.end():],re.I):parts.append(full)
                        self.expanded.add(key)
                    if family and family not in self.seen:
                        parts.append(hints[family]);self.seen.add(family)
                    if not parts:return m[0]
                    self.count+=1
                    from html import escape
                    return m[0]+'<span class="term-zh" lang="zh-Hant">（'+escape('；'.join(parts))+'）</span>'
                s=pattern.sub(sub,s)
            self.out.append(s)
        def handle_entityref(self,n):self.out.append('&'+n+';')
        def handle_charref(self,n):self.out.append('&#'+n+';')
        def handle_comment(self,s):self.out.append('<!--'+s+'-->')
        def handle_decl(self,s):self.out.append('<!'+s+'>')
    total=0;changed=0
    for p in (root/'concepts').glob('*.html'):
        original=p.read_text(encoding='utf-8');base=strip.sub('',original);parser=Annotator();parser.feed(base);out=''.join(parser.out)
        assert strip.sub('',out)==base,p.name
        total+=parser.count
        if out!=original:p.write_text(out,encoding='utf-8');changed+=1
    (root/'assets/term-translations.json').write_text(json.dumps(hints,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (root/'assets/term-variants.json').write_text(json.dumps([[r['Term']]+[x.strip() for x in r['Variants'].split(';') if x.strip()] for r in rows if r['Variants'].strip()],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'term_families':len(hints),'changed_pages':changed,'hints':total}))

if __name__=='__main__':rebuild(Path(__file__).resolve().parents[1])
