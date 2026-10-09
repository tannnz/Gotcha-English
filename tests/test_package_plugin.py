"""Packaging regression tests use only disposable, fictional repositories."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('package_plugin', Path(__file__).resolve().parents[1] / 'scripts/package-plugin.py')
packaging = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packaging)


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        self.write('.gitignore', '*\n!/.gitignore\n!/plugin.json\n!/.codex-plugin/\n!/.codex-plugin/plugin.json\n!/.claude-plugin/\n!/.claude-plugin/plugin.json\n!/skills/\n!/skills/**/\n!/skills/**/SKILL.md\n!/skills/**/template.md\n!/assets/\n!/assets/logo.svg\n')
        self.manifest = {'name': 'gotcha-english', 'version': '0.1.1', 'description': 'Fictional test plugin', 'author': {'name': 'Test'}, 'extensions': {'com.openai': {'interface': {'displayName': 'Test'}}}}
        self.save_manifest()
        self.write('.agents/plugins/marketplace.json', json.dumps({'name': 'gotcha-english-local', 'plugins': [{'name': 'gotcha-english', 'source': {'source': 'local', 'path': './'}}]}))
        self.write('.claude-plugin/marketplace.json', json.dumps({'name': 'gotcha-english-local', 'plugins': [{'name': 'gotcha-english', 'source': './'}]}))
        self.skill('fictional-coach')
        packaging.sync_metadata(self.root)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def skill(self, name):
        self.write(f'skills/{name}/SKILL.md', f'---\nname: {name}\ndescription: Fictional skill for testing.\n---\n\nRead [template](references/template.md).\n')
        self.write(f'skills/{name}/references/template.md', 'Fictional output template.\n')

    def save_manifest(self):
        self.write('plugin.json', json.dumps(self.manifest))

    def test_multiple_skills_and_filtered_metadata(self):
        self.skill('second-coach')
        _, files = packaging.check(self.root)
        self.assertIn('skills/second-coach/SKILL.md', files)
        claude = packaging.read_json(self.root / '.claude-plugin/plugin.json')
        self.assertNotIn('extensions', claude)
        self.assertNotIn('interface', claude)
        self.assertEqual(packaging.read_json(self.root / '.codex-plugin/plugin.json')['skills'], './skills/')

    def test_reproducible_build_does_not_mutate_sources(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file() and '.git' not in p.parts}
        first = packaging.build(self.root)
        first_bytes = first.read_bytes()
        self.assertEqual(packaging.build(self.root).read_bytes(), first_bytes)
        for relative, content in before.items():
            self.assertEqual((self.root / relative).read_bytes(), content)
        with zipfile.ZipFile(first) as package:
            self.assertIsNone(package.testzip())
            self.assertTrue(all(name.startswith('gotcha-english/') for name in package.namelist()))
            self.assertFalse(any('marketplace' in name for name in package.namelist()))

    def test_check_is_read_only(self):
        before = sorted(str(p.relative_to(self.root)) for p in self.root.rglob('*'))
        packaging.check(self.root)
        self.assertEqual(before, sorted(str(p.relative_to(self.root)) for p in self.root.rglob('*')))

    def test_missing_reference(self):
        (self.root / 'skills/fictional-coach/references/template.md').unlink()
        with self.assertRaisesRegex(packaging.ValidationError, 'referenced resource'):
            packaging.check(self.root)

    def test_ignored_reference_fails(self):
        self.write('skills/fictional-coach/private.md', 'Ignored private test data')
        with (self.root / 'skills/fictional-coach/SKILL.md').open('a') as target:
            target.write('\n[private](private.md)\n')
        with self.assertRaisesRegex(packaging.ValidationError, 'excluded referenced resource'):
            packaging.check(self.root)

    def test_ignored_temporary_file_not_packaged(self):
        self.write('skills/fictional-coach/temporary.txt', 'Should not ship')
        with zipfile.ZipFile(packaging.build(self.root)) as package:
            self.assertFalse(any(name.endswith('temporary.txt') for name in package.namelist()))

    def test_symlink_rejected_even_when_ignored(self):
        (self.root / 'skills/fictional-coach/link').symlink_to(self.root / 'plugin.json')
        with self.assertRaisesRegex(packaging.ValidationError, 'symlink'):
            packaging.check(self.root)

    def test_metadata_invalid_and_stale(self):
        self.manifest['version'] = 'invalid'
        self.save_manifest()
        with self.assertRaisesRegex(packaging.ValidationError, 'version'):
            packaging.check(self.root)
        self.manifest['version'] = '0.1.2'
        self.save_manifest()
        with self.assertRaisesRegex(packaging.ValidationError, 'stale'):
            packaging.check(self.root)
        packaging.sync_metadata(self.root)
        packaging.check(self.root)

    def test_invalid_frontmatter(self):
        self.write('skills/fictional-coach/SKILL.md', '---\nname: wrong\ndescription: Fictional\n---\n')
        with self.assertRaisesRegex(packaging.ValidationError, 'matching name'):
            packaging.check(self.root)

    def test_market_source_must_be_root(self):
        self.write('.agents/plugins/marketplace.json', json.dumps({'name': 'gotcha-english-local', 'plugins': [{'name': 'gotcha-english', 'source': {'source': 'local', 'path': './old'}}]}))
        with self.assertRaisesRegex(packaging.ValidationError, 'repository root'):
            packaging.check(self.root)

    def test_assets_and_remote_references(self):
        self.manifest['extensions']['com.openai']['interface']['iconSmall'] = './assets/logo.svg'
        self.save_manifest()
        packaging.sync_metadata(self.root)
        with self.assertRaisesRegex(packaging.ValidationError, 'missing or excluded asset'):
            packaging.check(self.root)
        self.write('assets/logo.svg', '<svg/>')
        with (self.root / 'skills/fictional-coach/SKILL.md').open('a') as target:
            target.write('\n[remote](https://example.com/resource)\n')
        _, files = packaging.check(self.root)
        self.assertIn('assets/logo.svg', files)

    def test_sync_preserves_skill_content(self):
        path = self.root / 'skills/fictional-coach/SKILL.md'
        content = path.read_bytes()
        self.manifest['version'] = '0.1.2'
        self.save_manifest()
        packaging.sync_metadata(self.root)
        self.assertEqual(path.read_bytes(), content)

    def test_markdown_examples_are_not_resource_links(self):
        with (self.root / 'skills/fictional-coach/SKILL.md').open('a') as target:
            target.write('\n```markdown\n[example](fictional-path.md)\n```\n\n`[inline](also-fictional.md)`\n')
        packaging.check(self.root)

    def test_executable_modes_are_normalized_and_reproducible(self):
        script = self.write('skills/fictional-coach/run.sh', '#!/bin/sh\nexit 0\n')
        with (self.root / '.gitignore').open('a') as target:
            target.write('!/skills/fictional-coach/run.sh\n')
        script.chmod(0o710)
        archive = packaging.build(self.root)
        content = archive.read_bytes()
        with zipfile.ZipFile(archive) as package:
            self.assertEqual(package.getinfo('gotcha-english/skills/fictional-coach/run.sh').external_attr >> 16, 0o100755)
            self.assertEqual(package.getinfo('gotcha-english/skills/fictional-coach/SKILL.md').external_attr >> 16, 0o100644)
        script.chmod(0o755)
        self.assertEqual(packaging.build(self.root).read_bytes(), content)

    def test_sync_rejects_parent_symlink_before_any_write(self):
        external = tempfile.TemporaryDirectory()
        self.addCleanup(external.cleanup)
        outside = Path(external.name)
        sentinel = outside / 'plugin.json'
        sentinel.write_text('Do not overwrite', encoding='utf-8')
        directory = self.root / '.claude-plugin'
        for child in directory.iterdir():
            child.unlink()
        directory.rmdir()
        directory.symlink_to(outside, target_is_directory=True)
        before = (self.root / '.codex-plugin/plugin.json').read_bytes()
        self.manifest['version'] = '0.1.2'
        self.save_manifest()
        with self.assertRaisesRegex(packaging.ValidationError, 'symlink'):
            packaging.sync_metadata(self.root)
        self.assertEqual(sentinel.read_text(encoding='utf-8'), 'Do not overwrite')
        self.assertEqual((self.root / '.codex-plugin/plugin.json').read_bytes(), before)

    def test_sync_rejects_file_symlink(self):
        target = self.root / '.codex-plugin/plugin.json'
        target.unlink()
        target.symlink_to(self.root / 'plugin.json')
        before = (self.root / 'plugin.json').read_bytes()
        with self.assertRaisesRegex(packaging.ValidationError, 'symlink'):
            packaging.sync_metadata(self.root)
        self.assertEqual((self.root / 'plugin.json').read_bytes(), before)

    def test_skill_reference_must_be_self_contained(self):
        self.skill('second-coach')
        with (self.root / 'skills/fictional-coach/SKILL.md').open('a') as target:
            target.write('\n[cross-skill](../second-coach/references/template.md)\n')
        with self.assertRaisesRegex(packaging.ValidationError, 'inside its Skill'):
            packaging.check(self.root)

    def test_reference_escape_rejected(self):
        with (self.root / 'skills/fictional-coach/SKILL.md').open('a') as target:
            target.write('\n[outside](../../../outside.md)\n')
        with self.assertRaisesRegex(packaging.ValidationError, 'escapes repository'):
            packaging.check(self.root)


if __name__ == '__main__':
    unittest.main()
