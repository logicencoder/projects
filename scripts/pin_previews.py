"""Pin catalogue images to the current commit of each overview repository.

Usage: python3 scripts/pin_previews.py CLONES_DIR
CLONES_DIR holds local clones named after the overview repositories; the commit comes
from GitHub, dimensions and size from the local file (which must exist at that path).
"""
import json,struct,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def dims(p):
    h=p.read_bytes()[:24]
    return list(struct.unpack('>II',h[16:24])) if h[:8]==b'\x89PNG\r\n\x1a\n' else [None,None]
def main(clones):
    cat=json.loads((ROOT/'catalogue.json').read_text()); out=[]
    for s in cat['sections']:
        for i in s['items']:
            repo=i.get('repo')
            if not repo: continue
            e={'repo':repo,'overview':f'https://github.com/logicencoder/{repo}'}
            img=i.get('image')
            if img and not img['path'].startswith('LOCAL:'):
                sha=subprocess.run(['gh','api',f'repos/logicencoder/{repo}/commits/main','-q','.sha'],capture_output=True,text=True,check=True).stdout.strip()
                f=Path(clones)/repo/img['path']
                assert f.exists(),f
                w,h=dims(f)
                e['commit']=sha
                e['image']={'url':f'https://raw.githubusercontent.com/logicencoder/{repo}/{sha}/{img["path"]}','alt':img['alt'],'width':w,'height':h,'bytes':f.stat().st_size}
            out.append(e)
    (ROOT/'previews.json').write_text(json.dumps(out,indent=1)+'\n')
    print('pinned',len(out))
if __name__=='__main__': main(sys.argv[1])
