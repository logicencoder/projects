"""Build the public project index from reviewed descriptions and preview metadata."""
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
def anchor(text):
    return re.sub(r'[^a-z0-9 -]','',text.lower()).replace(' ','-')
def render():
    catalogue=json.loads((ROOT/'catalogue.json').read_text())
    previews={p['repo']:p for p in json.loads((ROOT/'previews.json').read_text())}
    items=[i for g in catalogue['groups'] for i in g['items']]
    lines=['# Logic Encoder — Projects','',
        'A visual catalogue of applications, dashboards, operator tools and engineering projects built by Logic Encoder. Browse a short summary here, then open the product presentation for its capabilities, source context and additional views.','',
        '[Website](https://logicencoder.com) · [Web applications](https://logicencoder.com/applications/) · [Contact](https://logicencoder.com/contact/)','',
        '## Browse by area','']
    for group in catalogue['groups']:
        lines.append(f"- [{group['title']}](#{anchor(group['title'])}) — {len(group['items'])} projects")
    lines+=['- [Additional operator tools](#additional-operator-tools) — dedicated tool summaries','',
        'Screenshots are historical views of the actual products, not promises of current readings. Product presentations describe limitations and availability. Fictional spacecraft experiences are explicitly identified as simulations.','']
    for group in catalogue['groups']:
        lines+=['## '+group['title'],'']
        for item in group['items']:
            repo=item['repo'];meta=previews[repo]
            assert not meta.get('error'),meta
            lines+=['### '+item['name'],'',item['description'],'']
            links=[f"[Overview]({meta['overview']})"]
            if item.get('live'):
                links.append(f"[Open application]({item['live']})")
            for related in item.get('related',[]):
                links.append(f'[Companion service overview](https://github.com/logicencoder/{related})')
            lines+=[' · '.join(links),'']
            if repo=='russian-dc-observatory-monitor-overview':
                lines+=['![Russian DC Observatory populated public overview](assets/russian-dc-overview.png)','']
            elif meta.get('image'):
                image=meta['image']
                alt=image['alt'].replace(']','').replace('[','')
                lines+=[f"![{alt}]({image['url']})",'']
    lines+=['## Additional operator tools','',
        'These focused tools have their own concise summaries below. They are not separate public WordPress dashboards.','']
    details=['# Additional operator tools','',
        '[Back to the project catalogue](../README.md)','',
        'Focused operator and development tools maintained alongside the larger applications. These summaries describe purpose, not access instructions or private deployment details.','']
    for item in catalogue['additional']:
        target=anchor(item['name'])
        lines += ['### '+item['name'],'',item['description'],'',f'[Overview](docs/operator-tools.md#{target})','']
        details += ['## '+item['name'],'',item['description'],'']
    lines+=['---','',
        'Companion backends are linked with the corresponding product instead of being presented as duplicate applications. Retired components, deployment backups, shared libraries, policy archives and boilerplate templates are not promoted as standalone current apps.','',
        '**[Logic Encoder](https://logicencoder.com)** · [GitHub](https://github.com/logicencoder) · [Contact](https://logicencoder.com/contact/)','']
    return '\n'.join(lines),'\n'.join(details)

if __name__=='__main__':
    readme,details=render()
    (ROOT/'README.md').write_text(readme)
    (ROOT/'docs').mkdir(exist_ok=True)
    (ROOT/'docs/operator-tools.md').write_text(details)
    print('Built README.md and operator tool summaries from reviewed catalogue data')
