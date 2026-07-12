# Claude Code Instructions

This repository contains the `life-designer-pro` skill.

When the user asks to start, continue, review, or visualize a life-design session, invoke the skill at `.claude/skills/life-designer-pro/SKILL.md`.

Repository rules:

- Preserve the distinction between independent adaptation and official Stanford material.
- Keep `SKILL.md`, `.claude/skills/life-designer-pro/SKILL.md`, and `.agents/skills/life-designer-pro/SKILL.md` identical.
- Keep the interview adaptive and ask one question at a time.
- Do not generate a complete blueprint before the final-output gate is satisfied.
- Run `python scripts/validate_package.py` after edits.
