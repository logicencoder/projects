"""Check catalogue completeness, preview provenance and generated membership."""
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
        self.items=[i for g in self.data['groups'] for i in g['items']]
        self.previews=json.loads((ROOT/'previews.json').read_text())
        self.text=(ROOT/'README.md').read_text()
    def test_unique_project_membership(self):
        repos=[i['repo'] for i in self.items]
        self.assertEqual(len(repos),len(set(repos)))
        self.assertEqual(set(repos),{p['repo'] for p in self.previews})
        self.assertEqual(len(repos),47)
        self.assertEqual(len(self.data['additional']),9)
    def test_all_presentations_have_links(self):
        for item in self.items:
            self.assertIn('### '+item['name']+'\n',self.text)
            self.assertIn('https://github.com/logicencoder/'+item['repo']+')',self.text)
            for related in item.get('related',[]):
                self.assertIn('https://github.com/logicencoder/'+related+')',self.text)
    def test_all_48_public_overviews_covered(self):
        names={i['repo'] for i in self.items if i['repo'].endswith('-overview')}
        names.update(r for i in self.items for r in i.get('related',[]))
        self.assertEqual(len(names),48)
    def test_verified_previews_are_pinned(self):
        for preview in self.previews:
            self.assertFalse(preview.get('error'))
            if preview.get('image'):
                image=preview['image']
                self.assertIn(image['url'],self.text)
                self.assertRegex(image['url'],r'raw\.githubusercontent\.com/logicencoder/[^/]+/[0-9a-f]{40}/')
                self.assertGreaterEqual(image['width'],400)
                self.assertGreater(image['bytes'],0)
        self.assertEqual(len(re.findall(r'!\[',self.text)),38)
    def test_generated_output_is_current(self):
        readme,details=build.render()
        self.assertEqual(self.text,readme)
        self.assertEqual((ROOT/'docs/operator-tools.md').read_text(),details)
    def test_no_infrastructure_details_or_retired_apps(self):
        self.assertNotRegex(self.text,r'192\.168\.|127\.0\.0\.1|/home/|PRIVATE_KEY|API_KEY=')
        for retired in ['satellite-map-bridge','sun-live-bridge','people-in-space-bridge','exoplanet-explorer-bridge','launch-tracker-bridge']:
            self.assertNotIn('github.com/logicencoder/'+retired+')',self.text)
    def test_local_image_is_real_png(self):
        data=(ROOT/'assets/russian-dc-overview.png').read_bytes()
        self.assertEqual(data[:8],b'\x89PNG\r\n\x1a\n')
        self.assertEqual(int.from_bytes(data[16:20],'big'),1600)
        self.assertEqual(int.from_bytes(data[20:24],'big'),1100)

if __name__=='__main__':
    unittest.main()
