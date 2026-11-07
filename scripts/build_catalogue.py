"""Build the public project index from reviewed descriptions and pinned preview metadata.

Order in catalogue.json is the only ranking: the first section holds the most interesting
applications, later sections progressively less finished work. Sections marked linkonly
render a name, a sentence and a link, never an image.
"""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
def anchor(text):
    return re.sub(r'[^a-z0-9 -]','',text.lower()).replace(' ','-')
def render():
    cat=json.loads((ROOT/'catalogue.json').read_text())
    previews={p['repo']:p for p in json.loads((ROOT/'previews.json').read_text())}
    lines=['# Logic Encoder — Projects','',
        'A catalogue of the applications, dashboards, tools and engineering projects built by Logic Encoder. Each entry shows what the product does, what it offers, how it is built and where to read more. The list starts with the most substantial and most interesting work and ends with smaller tools, prototypes and unfinished work.','',
        'Across these projects: Python (FastAPI, asyncio) and Node.js backends, real-time WebSocket dashboards, blockchain and exchange tooling, WordPress themes and plugins, native desktop software in Rust and C#, Linux service operations, security checks, and AI-assisted development.','','[Website](https://logicencoder.com) · [Web applications](https://logicencoder.com/applications/) · [Contact](https://logicencoder.com/contact/)','']
    for s in cat['sections']:
        lines+=['## '+s['title'],'']
        for item in s['items']:
            lines+=['### '+item['name'],'']
            img=item.get('image')
            meta=previews.get(item.get('repo')) if item.get('repo') else None
            if img:
                alt=img['alt'].replace(']','').replace('[','')
                lines+=[f"![{alt}]({img['path'][6:]})" if img['path'].startswith('LOCAL:') else f"![{alt}]({meta['image']['url']})",'']
            lines+=[item.get('summary') or item['description'],'']
            if item.get('note'): lines+=[item['note'],'']
            if item.get('highlights'):
                lines+=['**What it offers**','']
                lines+=[f"- **{h['title']}** — {h['text']}" for h in item['highlights']]+['']
            if item.get('stack'):
                lines+=['**Built with**','']
                lines+=['- '+re.sub(r'^([^:]+):',r'**\1:**',x[:200]) for x in item['stack'][:6]]+['']
            links=[]
            if item.get('repo'):
                assert meta,item['repo']
                links.append(f"[Overview]({meta['overview']})")
            if item.get('live'): links.append(f"[Open application]({item['live']})")
            links+=[f"[{m['label']}]({m['url']})" for m in item.get('more',[])]
            if links: lines+=[' · '.join(links),'']
    lines+=['---','',
        'Retired components, deployment backups, shared libraries, supporting services, policy archives and utilities are kept in their own repositories and are not listed here.','',
        '**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)','']
    return '\n'.join(lines)

if __name__=='__main__':
    (ROOT/'README.md').write_text(render())
    print('Built README.md from reviewed catalogue data')
