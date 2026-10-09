"""Validate the canonical Skills and export reproducible plugin packages."""
import argparse
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit
import zipfile


class ValidationError(ValueError):
    pass


def read_json(path):
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise ValidationError(f'{path}: {exc}') from exc
    if not isinstance(value, dict):
        raise ValidationError(f'{path}: expected a JSON object')
    return value


def metadata(root):
    value = read_json(root / 'plugin.json')
    for key in ('name', 'version', 'description'):
        if not isinstance(value.get(key), str) or not value[key].strip():
            raise ValidationError(f'plugin.json: missing or invalid {key}')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value['name']):
        raise ValidationError('plugin.json: name must use lowercase words separated by hyphens')
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?', value['version']):
        raise ValidationError('plugin.json: version must be semantic major.minor.patch')
    author = value.get('author')
    if not isinstance(author, dict) or not isinstance(author.get('name'), str) or not author['name'].strip():
        raise ValidationError('plugin.json: author.name is required')
    extensions = value.get('extensions', {})
    if not isinstance(extensions, dict) or not isinstance(extensions.get('com.openai', {}), dict):
        raise ValidationError('plugin.json: invalid extensions')
    interface = extensions.get('com.openai', {}).get('interface', {})
    if not isinstance(interface, dict):
        raise ValidationError('plugin.json: interface must be an object')
    if 'shortDescription' in interface and (not isinstance(interface['shortDescription'], str) or len(interface['shortDescription']) > 30):
        raise ValidationError('plugin.json: shortDescription must be a string of at most 30 characters')
    return value


def overlays(value):
    fields = ('name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords')
    common = {key: value[key] for key in fields if key in value}
    codex = dict(common, skills='./skills/')
    interface = value.get('extensions', {}).get('com.openai', {}).get('interface')
    if interface is not None:
        codex['interface'] = interface
    return {'.codex-plugin/plugin.json': codex, '.claude-plugin/plugin.json': common}


def sync_metadata(root):
    root = root.resolve()
    generated = overlays(metadata(root))
    # Validate both destinations before writing either generated manifest.
    for relative in generated:
        path = root / relative
        if path.is_symlink() or path.parent.is_symlink():
            raise ValidationError(f'{relative}: symlinks are not permitted')
    for relative, value in generated.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def allowed(root, path):
    result = subprocess.run(['git', '-C', str(root), 'check-ignore', '--no-index', '-q', '--', path.relative_to(root).as_posix()], capture_output=True)
    if result.returncode not in (0, 1):
        raise ValidationError('Cannot check the Git allowlist: ' + result.stderr.decode().strip())
    return result.returncode == 1


def local_target(root, origin, reference):
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    target = origin.parent / unquote(parsed.path)
    try:
        target.resolve().relative_to(root.resolve())
    except ValueError:
        raise ValidationError(f'{origin.relative_to(root)}: reference escapes repository: {reference}')
    return target.resolve()


def check_catalog(root, relative, name, codex):
    catalog = read_json(root / relative)
    if catalog.get('name') != 'gotcha-english-local':
        raise ValidationError(f'{relative}: unexpected marketplace name')
    entries = catalog.get('plugins')
    if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
        raise ValidationError(f'{relative}: expected one plugin entry')
    entry = entries[0]
    expected = {'source': 'local', 'path': './'} if codex else './'
    if entry.get('name') != name or entry.get('source') != expected:
        raise ValidationError(f'{relative}: plugin must point to repository root with matching name')


def check(root):
    root = root.resolve()
    value = metadata(root)
    for relative, expected in overlays(value).items():
        if read_json(root / relative) != expected:
            raise ValidationError(f'{relative}: generated metadata is stale; run --sync-metadata')
    check_catalog(root, '.agents/plugins/marketplace.json', value['name'], True)
    check_catalog(root, '.claude-plugin/marketplace.json', value['name'], False)
    if not (root / 'LICENSE').is_file():
        raise ValidationError('LICENSE: missing license file')
    resources = ['LICENSE', 'plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json']
    skills = root / 'skills'
    discovered = []
    for directory in sorted(skills.iterdir() if skills.is_dir() else []):
        if not directory.is_dir():
            raise ValidationError(f'skills/{directory.name}: expected a Skill directory')
        entrypoint = directory / 'SKILL.md'
        if not entrypoint.is_file():
            raise ValidationError(f'skills/{directory.name}: missing SKILL.md')
        content = entrypoint.read_text(encoding='utf-8')
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', content, re.S)
        if not match:
            raise ValidationError(f'{entrypoint}: missing frontmatter')
        fields = dict(re.findall(r'^([a-z]+):\s*(.+)$', match[1], re.M))
        name = fields.get('name', '').strip().strip('\"\'').strip()
        description = fields.get('description', '').strip().strip('\"\'').strip()
        if name != directory.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or not description or description in ('|', '>'):
            raise ValidationError(f'{entrypoint}: require matching name and single-line description')
        discovered.append(entrypoint)
    if not discovered:
        raise ValidationError('No skills/*/SKILL.md found')
    for base in (skills, root / 'assets'):
        if base.is_symlink():
            raise ValidationError(f'{base.name}: symlinks are not permitted')
        if not base.exists():
            continue
        for path in sorted(base.rglob('*')):
            if path.is_symlink():
                raise ValidationError(f'{path.relative_to(root)}: symlinks are not permitted')
            if path.is_file() and allowed(root, path):
                resources.append(path.relative_to(root).as_posix())
    for relative in resources:
        path = root / relative
        if path.is_symlink() or not allowed(root, path):
            raise ValidationError(f'{relative}: required resource is not allowlisted')
    included = {(root / relative).resolve() for relative in resources}
    for entrypoint in discovered:
        if entrypoint.resolve() not in included:
            raise ValidationError(f'{entrypoint}: SKILL.md is not allowlisted')
    for relative in resources:
        origin = root / relative
        if origin.suffix.lower() != '.md':
            continue
        content = origin.read_text(encoding='utf-8')
        # Examples inside fenced code blocks are not runtime resource links.
        content = re.sub(r'^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[^\n]*(?:\n|$)', '', content, flags=re.M | re.S)
        content = re.sub(r'(`+)[^`\n]*?\1', '', content)
        refs = re.findall(r'!?\[[^\]]*\]\(\s*<?([^\s)>]+)>?(?:\s+[\"\'][^\n]*?)?\)', content)
        refs += re.findall(r'^\s*\[[^\]]+\]:\s*<?([^\s>]+)>?', content, re.M)
        for reference in refs:
            target = local_target(root, origin, reference)
            if target is not None and relative.startswith('skills/'):
                skill_root = root / Path(relative).parts[0] / Path(relative).parts[1]
                try:
                    target.relative_to(skill_root)
                except ValueError:
                    raise ValidationError(f'{relative}: resource reference must stay inside its Skill: {reference}')
            if target is not None and target not in included:
                raise ValidationError(f'{relative}: missing or excluded referenced resource: {reference}')
    def manifest_refs(node):
        if isinstance(node, dict):
            for key, child in node.items():
                if isinstance(child, str) and (child.startswith(('./', 'assets/', 'skills/')) or key in ('logo', 'icon', 'iconSmall', 'iconLarge', 'screenshots')):
                    yield child
                elif key == 'screenshots' and isinstance(child, list):
                    yield from (item for item in child if isinstance(item, str))
                else:
                    yield from manifest_refs(child)
        elif isinstance(node, list):
            for child in node:
                yield from manifest_refs(child)
    for reference in manifest_refs(value):
        target = local_target(root, root / 'plugin.json', reference)
        if target is not None and target not in included:
            raise ValidationError(f'plugin.json: missing or excluded asset: {reference}')
    return value, sorted(set(resources))


def build(root):
    root = root.resolve()
    value, resources = check(root)
    archive = root / 'dist' / f"{value['name']}-{value['version']}.zip"
    archive.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as package:
        for relative in resources:
            info = zipfile.ZipInfo(value['name'] + '/' + relative, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            source_mode = (root / relative).stat().st_mode
            info.external_attr = (0o100755 if source_mode & 0o111 else 0o100644) << 16
            package.writestr(info, (root / relative).read_bytes())
    return archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument('--check', action='store_true')
    actions.add_argument('--sync-metadata', action='store_true')
    args = parser.parse_args()
    try:
        if args.sync_metadata:
            sync_metadata(args.root)
            print('Platform metadata synchronized.')
        elif args.check:
            value, resources = check(args.root)
            print(f"Validated {value['name']} {value['version']}: {len(resources)} package files.")
        else:
            print('Built and verified:', build(args.root))
    except (ValidationError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
