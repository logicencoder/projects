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
        'A visual catalogue of applications, dashboards, operator tools and engineering projects built by Logic Encoder. Browse a short summary here, then open the product presentation for its capabilities, source context and additional views.','',
        '[Website](https://logicencoder.com) · [Web applications](https://logicencoder.com/applications/) · [Contact](https://logicencoder.com/contact/)','',
        '## Browse','']
    for s in cat['sections']:
        lines.append(f"- [{s['title']}](#{anchor(s['title'])}) — {len(s['items'])} projects")
    lines+=['','Screenshots are historical views of the actual products, not promises of current readings. Product presentations describe limitations and availability. Fictional spacecraft experiences are explicitly identified as simulations.','']
    for s in cat['sections']:
        lines+=['## '+s['title'],'']
        for item in s['items']:
            lines+=['### '+item['name'],'',item['description'],'']
            if item.get('note'): lines+=[item['note'],'']
            links=[]
            meta=previews.get(item.get('repo')) if item.get('repo') else None
            if item.get('repo'):
                assert meta,item['repo']
                links.append(f"[Overview]({meta['overview']})")
            if item.get('live'): links.append(f"[Open application]({item['live']})")
            links+=[f"[{m['label']}]({m['url']})" for m in item.get('more',[])]
            if links: lines+=[' · '.join(links),'']
            img=item.get('image')
            if s.get('linkonly'): assert not img,item['name']
            elif img:
                alt=img['alt'].replace(']','').replace('[','')
                if img['path'].startswith('LOCAL:'): lines+=[f"![{alt}]({img['path'][6:]})",'']
                else: lines+=[f"![{alt}]({meta['image']['url']})",'']
    lines+=['---','',
        'Retired components, deployment backups, shared libraries, supporting services, policy archives and utilities are kept in their own repositories and are not listed here.','',
        '**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)','']
    return '\n'.join(lines)

if __name__=='__main__':
    (ROOT/'README.md').write_text(render())
    print('Built README.md from reviewed catalogue data')
