"""Build the local plugin from the canonical Diary Coach source."""
import json
from pathlib import Path
import shutil
import zipfile

root = Path(__file__).resolve().parents[1]
plugin = root / 'plugins/gotcha-english'
source = root / '.agents/skills/diary-coach'
files = ('SKILL.md', 'agents/openai.yaml', 'references/output-template.md')
interface = {
    'displayName': 'GotchaEnglish',
    'shortDescription': '逐段批改英语日记，讲解语法与自然表达',
    'longDescription': '使用 Diary Coach 逐段批改英语日记，解释语法、词义和搭配问题，提供完整修改版，并保留原意、口语风格和个人表达。',
    'developerName': 'GotchaEnglish',
    'category': 'Education',
    'defaultPrompt': 'Use $diary-coach to review my English diary paragraph by paragraph.',
}
manifest = {
    '$schema': 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
    'name': 'gotcha-english', 'version': '0.1.0',
    'description': 'Review English diaries paragraph by paragraph, explain grammar and word usage, and preserve the writer’s meaning and voice.',
    'author': {'name': 'GotchaEnglish'},
    'extensions': {'com.openai': {'interface': interface}},
}
plugin.mkdir(parents=True, exist_ok=True)
(plugin / 'plugin.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
# Compatibility manifest for local Codex clients.
overlay = plugin / '.codex-plugin/plugin.json'
overlay.parent.mkdir(parents=True, exist_ok=True)
overlay.write_text(json.dumps({
    'name': manifest['name'], 'version': manifest['version'],
    'description': manifest['description'], 'author': manifest['author'],
    'skills': './skills/', 'interface': interface,
}, ensure_ascii=False, indent=2) + '\n')
for relative in files:
    target = plugin / 'skills/diary-coach' / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source / relative, target)
    assert target.read_bytes() == (source / relative).read_bytes()
assert len(interface['shortDescription']) <= 30
archive = root / 'dist/gotcha-english-0.1.0.zip'
archive.parent.mkdir(exist_ok=True)
expected = ['plugin.json', '.codex-plugin/plugin.json'] + ['skills/diary-coach/' + p for p in files]
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as package:
    for relative in expected:
        package.write(plugin / relative, 'gotcha-english/' + relative)
with zipfile.ZipFile(archive) as package:
    assert package.testzip() is None
    assert len(package.namelist()) == len(expected)
print('Built and verified:', archive)
