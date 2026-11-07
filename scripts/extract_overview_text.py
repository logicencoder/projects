"""Fill summary, stack and highlights of catalogue entries from the overview READMEs.

Usage: python3 scripts/extract_overview_text.py CLONES_DIR
The text is taken verbatim (links stripped, first sentences only) so the catalogue stays
consistent with the overview repositories; review the result before publishing.
"""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKIP={'Tech stack','Scope and limits','Quality checks','Diagnostics and help','Playback it covers','Audio engines'}
def clean(s):
    s=re.sub(r'!\[[^\]]*\]\([^)]*\)','',s)
    s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s)
    return re.sub(r'\s+',' ',s.replace('**','').replace('`','')).strip()
def first_sentence(p,limit=300):
    p=clean(p)
    sents=re.findall(r'.+?[.!?](?:\s|$)',p) or [p]
    out=sents[0].strip()
    if len(out)<90 and len(sents)>1 and len(out+' '+sents[1].strip())<=limit: out+=' '+sents[1].strip()
    return out if len(out)<=limit else out[:limit].rsplit(' ',1)[0]+'…'
def parse(text):
    text=re.sub(r'<!--.*?-->','',text,flags=re.S)
    parts=re.split(r'^## ',text,flags=re.M)
    head=parts[0]
    paras=[p.strip() for p in re.split(r'\n\s*\n',head) if p.strip() and not p.strip().startswith('#') and not p.strip().startswith('![') and not p.strip().startswith('*')]
    summary=clean(paras[0]) if paras else ''
    stack=[];highlights=[]
    for sec in parts[1:]:
        title,_,body=sec.partition('\n'); title=title.strip()
        if title=='Tech stack':
            for row in body.splitlines():
                c=[x.strip() for x in row.strip().strip('|').split('|')]
                if len(c)==2 and not set(c[0])<=set('-: ') and c[0].lower() not in ('layer',''):
                    stack.append(f'{c[0]}: {clean(c[1])}')
            continue
        if title in SKIP or body.startswith('---'): continue
        bp=[p.strip() for p in re.split(r'\n\s*\n',body) if p.strip() and not p.strip().startswith(('![','|','---','Private code','See [','**[','<'))]
        if bp: highlights.append({'title':title,'text':first_sentence(bp[0])})
    return summary,stack,highlights
def main(clones):
    cat=json.loads((ROOT/'catalogue.json').read_text())
    for s in cat['sections']:
        for i in s['items']:
            r=i.get('repo')
            if not r or i.get('manual'): continue
            f=Path(clones)/r/'README.md'
            if not f.exists(): continue
            summary,stack,hl=parse(f.read_text())
            i['summary']=summary; i['stack']=stack; i['highlights']=hl[:5]
    (ROOT/'catalogue.json').write_text(json.dumps(cat,indent=1,ensure_ascii=False)+'\n')
if __name__=='__main__': main(sys.argv[1])
