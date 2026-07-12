#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'SKILL.md',
    'README.md',
    'QUICKSTART.md',
    'CLAUDE.md',
    'AGENTS.md',
    '.claude/skills/life-designer-pro/SKILL.md',
    '.agents/skills/life-designer-pro/SKILL.md',
    '.agents/skills/life-designer-pro/agents/openai.yaml',
    'references/METHODOLOGY.md',
    'references/CONVERSATION_PROTOCOL.md',
    'references/DELIVERABLES.md',
    'references/IMAGE_GENERATION.md',
    'references/SAFETY_AND_LIMITS.md',
]

errors = []
for item in REQUIRED:
    if not (ROOT / item).exists():
        errors.append(f'Missing required file: {item}')

skill_paths = [
    ROOT / 'SKILL.md',
    ROOT / '.claude/skills/life-designer-pro/SKILL.md',
    ROOT / '.agents/skills/life-designer-pro/SKILL.md',
]
if all(p.exists() for p in skill_paths):
    contents = [p.read_text(encoding='utf-8') for p in skill_paths]
    if len(set(contents)) != 1:
        errors.append('The three SKILL.md copies are not identical.')

# All duplicated references and templates must stay in sync across the
# root, .claude, and .agents trees.
DUP_ROOTS = ['', '.claude/skills/life-designer-pro/', '.agents/skills/life-designer-pro/']
for subdir in ['references', 'templates']:
    canonical = ROOT / subdir
    if not canonical.exists():
        continue
    for src in sorted(canonical.glob('*.md')):
        rel = f'{subdir}/{src.name}'
        copies = [ROOT / f'{d}{rel}' for d in DUP_ROOTS]
        missing = [c for c in copies if not c.exists()]
        for c in missing:
            errors.append(f'Missing duplicated file: {c.relative_to(ROOT)}')
        present = [c for c in copies if c.exists()]
        if len(present) > 1:
            texts = {c.read_text(encoding='utf-8') for c in present}
            if len(texts) != 1:
                errors.append(f'Duplicated copies of {rel} are not identical.')

for path in skill_paths:
    if path.exists():
        text = path.read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
        if not match:
            errors.append(f'Invalid YAML frontmatter in {path.relative_to(ROOT)}')
            continue
        front = match.group(1)
        if not re.search(r'^name:\s*life-designer-pro\s*$', front, re.M):
            errors.append(f'Missing or invalid name in {path.relative_to(ROOT)}')
        if not re.search(r'^description:\s*.+$', front, re.M):
            errors.append(f'Missing description in {path.relative_to(ROOT)}')

link_pattern = re.compile(r'\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)')
for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    for target in link_pattern.findall(text):
        clean = target.split('#', 1)[0]
        if not clean:
            continue
        resolved = (md.parent / clean).resolve()
        if not resolved.exists():
            errors.append(f'Broken link in {md.relative_to(ROOT)}: {target}')

if errors:
    print('Validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print('Validation passed.')
