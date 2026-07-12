# Life Designer Pro

An AI-assisted life-design coach and reusable skill for Claude Code and OpenAI Codex.

Life Designer Pro helps you look at your work, relationships (from partner and family to professional network), health, fun, learning and creativity, community, finances, and contribution as one connected life. It uses an adaptive coaching conversation, three alternative future designs, evidence-based prototypes, and a reusable review loop.

> **Attribution:** Inspired by ideas from [*Designing Your Life*](https://designingyour.life/) by [Bill Burnett](https://designingyour.life/about-us/) and [Dave Evans](https://designingyour.life/about-us/) and the [Stanford Life Design Lab](https://lifedesignlab.stanford.edu/). This repository is an independent adaptation. It is not an official Stanford product and is not affiliated with Stanford University.

## What makes this different

Most life-planning prompts jump from a few answers to a confident recommendation. This method slows down the diagnosis, distinguishes facts from assumptions, tracks repeated themes, tests contradictions, and produces practical experiments rather than a permanent verdict.

Its central test is simple:

> If this future works, what will an ordinary day feel like?

## See it in action

A session opens with eight life-area ratings, then follows the evidence one plain question at a time. A fictional example:

> **Coach:** Which one area most needs your attention right now? The lowest score is not automatically the most urgent.
>
> **User:** Work is 4, and yes, work is the urgent one. I am successful, but every week is meetings and escalations.
>
> **Coach:** Your concern seems to be the kind of work occupying your time, not your performance. Tell me about one recent work period that left you energized rather than depleted.

A few questions later (a quick session takes five to ten minutes), the session has found the real question underneath the stated one, and can draw the whole thing on one page, the Life Map:

```text
[ TODAY: the operating scope ]        [ TODAY: the craft ]
  meetings · escalations · work 4       systems design · mentoring
              \                          /
               [ THE REAL QUESTION ]
      what mix of operating, creating, teaching,
      and autonomy makes a week worth repeating?
                        |
               [ WHAT TRAVELS WITH YOU ]
    two creation blocks · family time · developing one person
                        |
          [ ACTIVE EXPERIMENT · review in 30 days ]
       one three-session workshop + advising one team
           /              |               \
[ Enterprise builder ] [ Operator-educator ] [ Portfolio advisor ]
  redesigned scope       being tested first    advisory + writing
                        |
               [ EVIDENCE LOOP ]
        weekly 10 min · monthly · quarterly re-score
```

Three paths, all legitimate, none a backup plan. One experiment small enough to start this week. A review loop that re-scores the futures as real evidence arrives, on a cadence the user picks: weekly, monthly, or quarterly. See [examples/](examples/) for the fictional session excerpt, condensed blueprint, and life map.

Two rules run through every deliverable: nothing is invented (thin evidence gets marked "insufficient evidence" instead of being papered over), and every recommendation is a testable prototype, not a verdict. The current version's improvements all came from live user-session feedback: a clearer opening question, one-ask-per-question style, honest partial-coverage notes, and the visual Life Map itself.

## What you get

- **Your Life Map:** one page showing your current priorities, energy sources, tensions, and the areas of life that need more attention.
- **Your Life Design Blueprint:** future life paths grounded in your own evidence, the ordinary day and trade-offs behind each one, and the questions you still need to test.
- **Your Prototype Plan:** one-day, 30-day, and 90-day tests that help you learn more before making a bigger commitment, with criteria for when to stop, continue, or expand.

Everything is modular: ask for only what you want, from a one-page summary to the full kit with a personal manifesto, images, and review prompts. Exact specifications live in [references/DELIVERABLES.md](references/DELIVERABLES.md). Prefer a zero-install version? [LITE_PROMPT.md](LITE_PROMPT.md) is a single copy-paste prompt that preserves the core method for claude.ai or any chat assistant.

## Repository structure

```text
life-designer-pro/
├── SKILL.md                         # Canonical Agent Skill
├── CLAUDE.md                        # Claude Code repository instructions
├── AGENTS.md                        # Codex repository instructions
├── README.md
├── QUICKSTART.md
├── LITE_PROMPT.md
├── LICENSE.md
├── CHANGELOG.md
├── .claude/skills/life-designer-pro/SKILL.md
├── .agents/skills/life-designer-pro/
│   ├── SKILL.md
│   └── agents/openai.yaml
├── references/
│   ├── METHODOLOGY.md
│   ├── CONVERSATION_PROTOCOL.md
│   ├── DELIVERABLES.md
│   ├── IMAGE_GENERATION.md
│   ├── SAFETY_AND_LIMITS.md
│   └── REVIEW_CADENCE.md
├── templates/
│   ├── BLUEPRINT_TEMPLATE.md
│   ├── LIFE_DASHBOARD_TEMPLATE.md
│   ├── LIFE_MAP_TEMPLATE.md
│   ├── EXPERIMENT_BOARD_TEMPLATE.md
│   ├── AI_COACH_MEMORY_TEMPLATE.md
│   └── ONE_PAGE_BLUEPRINT_TEMPLATE.md
├── prompts/
│   ├── START_SESSION.md
│   ├── WEEKLY_REVIEW.md
│   ├── MONTHLY_REVIEW.md
│   ├── QUARTERLY_RESET.md
│   ├── ANNUAL_REDESIGN.md
│   └── CONTINUE_COACHING.md
├── examples/
│   ├── EXAMPLE_CONVERSATION.md
│   ├── EXAMPLE_BLUEPRINT.md
│   └── EXAMPLE_LIFE_MAP.md
└── scripts/
    ├── install.sh
    ├── install.ps1
    └── validate_package.py
```

## Two ways to use it

### 1. Use the repository directly

```bash
git clone https://github.com/wei-wei-hu/life-designer-pro.git
cd life-designer-pro
```

Open the repository in Claude Code or Codex and ask:

```text
Use the life-designer-pro skill and start a new session.
```

Claude Code discovers the skill from `.claude/skills/life-designer-pro/`. Codex discovers it from `.agents/skills/life-designer-pro/`.

### 2. Install it as a personal skill

Run the install script from the repository root.

macOS or Linux:

```bash
bash scripts/install.sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

The scripts install the skill (SKILL.md plus references, templates, and prompts) into both user-level locations:

- Claude Code: `~/.claude/skills/life-designer-pro/`
- Codex: `~/.agents/skills/life-designer-pro/`

To verify, start a new Claude Code session (skills load at session start) and type `/life-designer-pro`.

## Starting commands

Claude Code:

```text
/life-designer-pro
```

Codex:

```text
$life-designer-pro Start a new guided session.
```

Natural-language activation also works when the user asks for life design, career-and-life planning, an integrated future plan, an ordinary-day analysis, or a personal life blueprint.

## Recommended workflow

1. Read [QUICKSTART.md](QUICKSTART.md).
2. Start a private session in a quiet setting.
3. Answer one question at a time using concrete examples.
4. Complete the blueprint only after enough evidence has been collected.
5. Save the final `AI Coach Memory` section.
6. Use the weekly, monthly, and quarterly prompts to keep the blueprint current.
7. Treat every recommendation as a prototype open to revision.

## Important limits

Life Designer Pro supports reflection and planning. It does not provide therapy, diagnosis, medical advice, legal advice, or financial advice. See [references/SAFETY_AND_LIMITS.md](references/SAFETY_AND_LIMITS.md).

## About the author

Life Designer Pro is created by [Weiwei Hu](https://www.linkedin.com/in/weiweihu/), who works at the intersection of big data, AI, and business decision-making. She is currently Director of Big Data, Insights & Strategy at HP, leading Print AI transformation programs including agentic AI workflow enablement, and writing about practical AI adoption for senior executives. She is the author of *Generative Engine Optimization (GEO): The Complete Playbook for Leaders to Win in AI Search*.

Connect with her:

- LinkedIn: [linkedin.com/in/weiweihu](https://www.linkedin.com/in/weiweihu/)
- Personal site: [weiweihu.carrd.co](https://weiweihu.carrd.co/)
- Articles on Towards Data Science: [towardsdatascience.com/author/weiwei-hu](https://towardsdatascience.com/author/weiwei-hu/)

If this skill helped you find your real question, she would love to hear what it turned out to be.

## License and attribution

Licensed under [CC BY 4.0](LICENSE.md): use it, share it, adapt it, including commercially, as long as you credit the author. When you share or adapt this work, include:

> Life Designer Pro by Weiwei Hu (https://www.linkedin.com/in/weiweihu/), source: https://github.com/wei-wei-hu/life-designer-pro, licensed under CC BY 4.0.

## Validation

Run:

```bash
python scripts/validate_package.py
```

The validator checks required files, YAML frontmatter, duplicate skill consistency, and internal Markdown links.
