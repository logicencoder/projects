"""Check catalogue structure, ordering rules, preview provenance and generated membership."""
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build_catalogue',ROOT/'scripts/build_catalogue.py')
build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)

class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'catalogue.json').read_text())
        self.items=[i for s in self.data['sections'] for i in s['items']]
        self.previews={p['repo']:p for p in json.loads((ROOT/'previews.json').read_text())}
        self.text=(ROOT/'README.md').read_text()
    def test_unique_names(self):
        names=[i['name'] for i in self.items]
        self.assertEqual(len(names),len(set(names)))
        repos=[i['repo'] for i in self.items if i.get('repo')]
        self.assertEqual(len(repos),len(set(repos)))
    def test_readme_is_generated_from_data(self):
        self.assertEqual(build.render(),self.text)
    def test_top_order(self):
        top=[i['name'] for i in self.data['sections'][0]['items']]
        self.assertEqual(top[:2],['Universal Service Manager','MEXC Trading App'])
    def test_removed_entries_stay_removed(self):
        for word in ['Multi-Coin','Bot Suite','Arbitrage Dashboard','DEX Swapper','Sol Pump','LE Shop','Sitemap Manager','LE Digest','Useful Scripts','Cursor Health','Chain Checker','Chain Watchers','Proxy Pool','Tokyo VPN','Rocinante Explorer','Additional operator tools','Companion']:
            self.assertNotIn(word,self.text,word)
    def test_forbidden_word(self):
        self.assertNotIn('flagship',self.text.lower())
        self.assertNotIn('flagship',(ROOT/'catalogue.json').read_text().lower())
    def test_linkonly_sections_have_no_images(self):
        for s in self.data['sections']:
            if s.get('linkonly'):
                for i in s['items']: self.assertNotIn('image',i)
    def test_images_are_pinned_with_seo_names(self):
        for i in self.items:
            img=i.get('image')
            if not img or img['path'].startswith('LOCAL:'): continue
            meta=self.previews[i['repo']]
            self.assertIn(meta['image']['url'],self.text)
            self.assertRegex(meta['image']['url'],r'raw\.githubusercontent\.com/logicencoder/[^/]+/[0-9a-f]{40}/')
            name=Path(img['path']).stem
            self.assertRegex(name,r'^[a-z0-9]+(-[a-z0-9]+)+$',name)
            self.assertNotRegex(name,r'20\d\d-\d\d-\d\d')
    def test_local_images_exist(self):
        for i in self.items:
            img=i.get('image')
            if img and img['path'].startswith('LOCAL:'): self.assertTrue((ROOT/img['path'][6:]).exists())
    def test_overview_links(self):
        for i in self.items:
            if i.get('repo'): self.assertIn('https://github.com/logicencoder/'+i['repo']+')',self.text)
if __name__=='__main__': unittest.main()
