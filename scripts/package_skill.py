#!/usr/bin/env python3
"""Build only the four reviewed standalone Skill files; no network or installs."""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = Path('plugins/superseedance-video')
SKILL = PLUGIN / 'skills/superseedance-video'
MEMBERS = (
    (SKILL / 'SKILL.md', 'superseedance-video/SKILL.md'),
    (SKILL / 'references/shot-plan.md', 'superseedance-video/references/shot-plan.md'),
    (SKILL / 'references/mcp-handoff.md', 'superseedance-video/references/mcp-handoff.md'),
    (PLUGIN / 'LICENSE', 'superseedance-video/LICENSE'),
)
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
SECRET_PATTERNS = (
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'\b(?:sk-ant-api\w*|sk_live|av_live)_[A-Za-z0-9_-]{20,}\b'),
    re.compile(r'\bBearer\s+[A-Za-z0-9_-]{32,}\b'),
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_member(relative):
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Invalid allowlisted source path')
    path = ROOT / relative
    for component in [path, *path.parents]:
        if component == ROOT:
            break
        if component.is_symlink():
            raise ValueError(f'Symlink source refused: {relative}')
    path.resolve(strict=True).relative_to(ROOT)
    if not path.is_file() or path.stat().st_size > 256_000:
        raise ValueError(f'Expected a small regular source file: {relative}')
    data = path.read_bytes()
    value = data.decode('utf-8')
    if any(pattern.search(value) for pattern in SECRET_PATTERNS):
        raise ValueError(f'Possible credential in source; review locally: {relative}')
    return data


def collect():
    result = [(name, read_member(source)) for source, name in MEMBERS]
    first = result[0][1].decode('utf-8')
    if not first.startswith('---\n') or '\nname: superseedance-video\n' not in first:
        raise ValueError('Skill identity/frontmatter is missing')
    return result


def archive(items):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in items:
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


def verify_zip(blob, items):
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        if z.namelist() != [name for name, _ in items] or z.testzip() is not None:
            raise ValueError('ZIP contents or checksum validation failed')
        for name, data in items:
            if z.read(name) != data:
                raise ValueError(f'ZIP member differs: {name}')
            p = Path(name)
            if p.is_absolute() or '..' in p.parts:
                raise ValueError('Unsafe archive member path')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true', help='Validate files and print hashes; write nothing')
    mode.add_argument('--self-test', action='store_true', help='Validate deterministic ZIP in memory; write nothing')
    mode.add_argument('--output', type=Path, help='Explicit new .zip path; parent must exist; never overwrite')
    args = parser.parse_args()
    items = collect()
    summary = {'members': [{'path': name, 'bytes': len(data), 'sha256': sha(data)} for name, data in items]}
    if args.check:
        summary['status'] = 'source-check-passed; no ZIP written'
    else:
        blob = archive(items)
        verify_zip(blob, items)
        if blob != archive(items):
            raise ValueError('Archive is not deterministic')
        summary.update({'zip_bytes': len(blob), 'zip_sha256': sha(blob)})
        if args.self_test:
            summary['status'] = 'in-memory-self-test-passed; no ZIP written'
        else:
            target = args.output.expanduser().absolute()
            if target.suffix.lower() != '.zip' or not target.parent.is_dir():
                raise ValueError('Output must be a .zip with an existing parent directory')
            if target.is_symlink():
                raise ValueError('Symlink destination refused')
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, 'O_NOFOLLOW', 0)
            fd = os.open(target, flags, 0o644)
            try:
                with os.fdopen(fd, 'wb') as output:
                    output.write(blob)
            except BaseException:
                target.unlink(missing_ok=True)
                raise
            summary.update({'status': 'ZIP written; not published', 'output': str(target)})
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, UnicodeError, zipfile.BadZipFile) as exc:
        print(f'Packaging stopped: {exc}', file=sys.stderr)
        raise SystemExit(1)
