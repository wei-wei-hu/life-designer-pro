# Quickstart

## Use it inside this repository

1. Get the code:

```bash
git clone https://github.com/wei-wei-hu/life-designer-pro.git
cd life-designer-pro
```

(Or download the ZIP from the repository page and unzip it.)
2. Open the repository in Claude Code or Codex.
3. Start with one of these prompts:

Claude Code:

```text
/life-designer-pro
```

Codex:

```text
$life-designer-pro Start a new guided session.
```

4. Answer the first question only.
5. Continue until the coach confirms it has enough evidence to produce the blueprint.

## Install it for use across repositories

Run from the repository root.

macOS or Linux:

```bash
bash scripts/install.sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

The script copies the skill (SKILL.md plus references, templates, and prompts) to:

- Claude Code: `~/.claude/skills/life-designer-pro/`
- Codex: `~/.agents/skills/life-designer-pro/`

**Verify it worked:** start a new Claude Code session (skills load at session start) and type `/life-designer-pro`. If the skill appears, you are ready. For Codex, open a new session and use `$life-designer-pro`.

## Best first-session setup

A quick session takes 5 to 10 minutes: four or five short questions that surface your real question, a life map, and a first experiment. Ask for a deep session (30 to 60 minutes, six to nine questions) when you want the full Core Blueprint or Full Kit. Use a private conversation, answer with real examples instead of abstract labels, and know that “I don’t know” is a valid answer; the coach should respond with a more concrete question. You can pause at any checkpoint and resume later with the memory snapshot the coach offers.

## Resume later

Save the final `AI Coach Memory` block. In a new session, attach or paste it and say:

```text
Use the life-designer-pro skill. Continue from this AI Coach Memory. Review what has changed before updating any recommendation.
```

## Generate only selected outputs

You may ask for a subset:

```text
Use the life-designer-pro skill. Based on the completed blueprint, generate only the LinkedIn banner prompt and one-page blueprint.
```

## Keep the source description accurate

Use this wording when sharing this work:

> Inspired by *Designing Your Life* by Bill Burnett and Dave Evans and expanded into an independent AI-guided life architecture method.

Do not describe the repository as an official Stanford prompt or Stanford-created AI product.
