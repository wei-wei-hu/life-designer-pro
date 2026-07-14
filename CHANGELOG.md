# Changelog

## 1.7.4 - 2026-07-14

- Deliverables now arrive one at a time: when a set is chosen, the coach shows a short numbered menu, the user picks, one deliverable is shown per message, and the remaining menu is re-offered until done; the review's compact closing display stays as the single sanctioned exception

## 1.7.3 - 2026-07-14

Fixes from a live user session:

- The opening ratings question now defines the scale as satisfaction today (0 in serious trouble, 10 could not realistically be better) and ships as a labeled list format, with a rule that the scale line must stay attached however the coach reformats it; a bare unexplained list is forbidden
- Honest time estimates everywhere: the quick session is about five minutes and the deep session usually 10 to 15 (the user's answer length sets the pace), replacing the inflated 30-to-60-minute claim that postponed sessions instead of starting them

## 1.7.2 - 2026-07-14

- Every interview and review now closes with the coach's best counsel: two or three actionable suggestions (one for the weekly) synthesized from everything known about the user, each grounded in their own evidence with a one-clause why and a first step small enough to start this week, chosen by the coach's judgment of what would help most, including what the user did not ask about, and labeled plainly as judgment to take or leave

## 1.7.1 - 2026-07-14

Fixes from two end-to-end validation sessions of the guided experience (initial interview and bi-weekly review, synthetic personas, 26/26 checks passed):

- Bi-weekly joined the cadence menu everywhere, served by the monthly prompt at lighter depth; any rhythm the user names is valid
- Cadence is asked once per review: settled at the open for scheduled runs, so the close only restates the next date and time
- One practice conversation per review: the proactive shortlist builds on the check-in results instead of opening a second menu
- Question budget now counts the check-in and metaphor tool explicitly (six primaries normal with one, seven with more)
- Life Map gained a missing-paths escape hatch matching the missing-experiment one: lens-labeled proposal sketches, scores marked insufficient
- Heroes probe split across two turns to honor the one-ask rule; memory template gained a life-metaphors line; one-page review date now sourced from the AI Coach Memory; manual monthly and quarterly prompts open with the cadence check; imminent-slot guidance added for mid-cycle cadence changes

## 1.7.0 - 2026-07-14

- The Practice Menu became a guided experience: once the user's priority area is known (first interview or review start), its practices are asked as a two-question pick-list check-in (which already happen, which to add or grow), with answers flowing into evidence and roadmap candidates
- Every review close now also asks which other deliverables the user wants to see or check, shown in the conversation on request

## 1.6.11 - 2026-07-14

- Review close is now automatic and complete: the review's evidence propagates across every deliverable it touches so all outputs agree, the key deliverables (Life Map, moved dashboard rows, top priorities, proposed action items) are shown in the conversation by default, and the user confirms before anything is saved

## 1.6.10 - 2026-07-14

- Action items at every review close are now guided proposals: curated from the review's evidence with a one-clause why each, three to five at most, confirmed, reordered, or swapped by the user before they become the plan

## 1.6.9 - 2026-07-14

- The coach now guides instead of only collecting: at reviews and when building the roadmap or prototype plan, it proactively brings the practices most relevant to the user's own evidence, explains in one clause why each fits, and asks which to prioritize, add to the roadmap, or give weekly time to, always with a "something else" exit so guidance never becomes prescription

## 1.6.8 - 2026-07-13

- Scheduled review reminders now open by confirming the frequency still fits (keep, or change cadence, day, or time) before conducting the review, rescheduling themselves when the user changes it

## 1.6.7 - 2026-07-13

- Reviews now end with the deliverables themselves shown in the conversation (the Life Map rendered visually where tools allow, top priorities, action items, and the single best next step); files are updated quietly after confirmation and never presented as the result

## 1.6.6 - 2026-07-13

- Users now set the exact day and time of their recurring review, not just the cadence: the session close asks when in their week or month the time genuinely exists, reminders are created at that moment, and every review close reconfirms date and time along with cadence

## 1.6.5 - 2026-07-13

- Every review now closes by asking whether the current cadence still fits or should change (weekly, monthly, quarterly), sets the next review date to match, and updates the user's reminder accordingly (rescheduling the scheduled task where the environment supports it, or handing over the new review prompt for a calendar update)

## 1.6.4 - 2026-07-13

- Reviews now connect priorities and progress to the Practice Menu: previously picked practices are reviewed like any other experiment (keep, adjust, drop), and when a priority area shows little progress or a new addition needs a concrete first step, the coach offers one to three matching practices from the menu's same life areas

## 1.6.3 - 2026-07-13

- Life metaphors now have a guaranteed home in the deliverables: the Personal Compass records the today metaphor, the tomorrow metaphor, and the bridge between them; heroes-probe qualities are named as a values source

## 1.6.2 - 2026-07-13

- The review loop gained a forward-looking move: monthly and larger reviews now ask what the user wants to add to their life or career roadmap, and every addition is placed into a deliverable (One-Year Roadmap first, then prototype plan, paths, or weekly conditions) or held in the AI Coach Memory so it is not lost

## 1.6.1 - 2026-07-13

- Every review now follows an explicit four-move loop: ask for progress and milestones, tie each back to the deliverables it touches (Life Map, Blueprint, prototype plan), show the updated deliverables and ask the user to confirm before saving, then close with the adjustment plan and next review date; all four review prompts updated to match

## 1.6.0 - 2026-07-13

- Added three tools adapted from Ayse Birsel's Design the Life You Love (credited in the attribution notes): the life metaphor bridge (a metaphor for today, one for tomorrow, and how one becomes the other), the heroes-to-values probe for users who stall on values questions, and the Vision Letter (deliverable 28), saved privately and opened at a future review

## 1.5.0 - 2026-07-13

- Added the Practice Menu: 48 small, high-return practices across the five life areas, offered as user-chosen options for prototype plans and weekly systems (pick one to three, shrink until starting feels easy)

## 1.4.1 - 2026-07-12

Fixes from two end-to-end validation sessions (quick and deep, synthetic personas):

- Protocol ratings list now includes contribution and meaning (was seven areas vs. the opener's eight)
- AI Coach Memory clarified as always-created session infrastructure, independent of deliverable selection
- Scripted opener documented as the one sanctioned exception to the one-ask rule; question-budget counting clarified
- Weekly-conditions triage now requires the full user-owned ranking, not only a keep-one answer
- Life Map may propose the experiment when none exists yet, confirmed with the review date at session close
- Dashboard first-session convention: trend column reads "no prior evidence"
- Adjacent Life first-90-days framed as start-today reconnaissance; portfolio sweep capped for brief answerers; redundant final checkpoint skipped; baseline projection horizon shortened to two-then-five years; template title aligned

## 1.4.0 - 2026-07-12

- Three futures are now three two-year paths (ordinary day, first 90 days, months 4-12, year 2) instead of five-year designs; shorter horizon keeps paths realistic and testable, refreshed by the annual redesign
- Lite prompt aligned with the two-year horizon and its ordinary-day wording
- Weekly-conditions question now enforces the triage: if the user lists more than three, the coach asks a forced-choice follow-up instead of accepting the longer list

## 1.3.0 - 2026-07-11

Improvements from the first live user session:

- Opening question now defines the 0-10 scale and states that the lowest score is not automatically the most urgent
- Added question-style rules: one ask per question, plain words, short setup, offer a "pick one" way in, match the user's energy
- Added a session-depth rule resolving the conflict between the 6-9 question budget and full-coverage requirements: secure the real question, weekly conditions, and one energizer; mark the rest insufficient
- Energy drains can now be collected through a pick-list for brief answerers
- The pause/snapshot offer is now a required part of the checkpoint format instead of a one-line rule elsewhere
- Executive Summary spec now requires a session-coverage note when coverage was partial
- Deliverable selection now always asks first (a general request is not a scope), presents results in conversation, and only writes files on request
- Added a required six-step session close (confirm proposals, offer gap follow-up, set review date, offer images, hand over memory) so sessions no longer end at file delivery
- Deliverable 16 redefined from a text pyramid to the visual Life Map (today, real question, portable conditions, active experiment, three futures, evidence loop) with a new template and text fallback
- Review cadence is now the user's explicit choice (weekly, monthly, quarterly, stackable, changeable at any review); added the missing prompts/WEEKLY_REVIEW.md
- README gained a See-it-in-action showcase (fictional persona only); example conversation updated to the new opening question; added examples/EXAMPLE_LIFE_MAP.md
- Install scripts now copy prompts/ (previously the installed skill had dangling references to review prompts); QUICKSTART gained a verify step and a realistic 30-60 minute estimate
- README and QUICKSTART now carry the repository URL and clone instructions
- License replaced: all-rights-reserved placeholder is now CC BY 4.0 with a preferred attribution line (use freely, credit Weiwei Hu when sharing or adapting)
- Quick session is now the default: four or five questions in 5-10 minutes producing the real question, life map, and first experiment; the 30-60 minute deep interview became opt-in
- README voice pass: AI-assisted life-design coach, "you" instead of "a person", official Designing Your Life and Stanford Life Design Lab links, review loop instead of review system
- Lite prompt aligned with 1.3.0: quick 4-5 question core, defined rating scale, easy-question rules, text life map, insufficient-evidence rule, cadence choice, paste-back memory block

## 1.2.0 - 2026-07-11

- Unified the Current-Life Dashboard schema across DELIVERABLES.md, BLUEPRINT_TEMPLATE.md, and LIFE_DASHBOARD_TEMPLATE.md (Score 0–10 / Trend / Evidence / Next review question)
- Expanded the opening ratings question from seven to eight areas to include contribution and meaning, matching the dashboard
- Aligned Energy and Flow Map template headings with the deliverable spec (recovery activities, supportive people, praised-but-draining, increase/reduce)
- Added full substructure to the blueprint template for the three futures (10 elements plus scorecard table) and renamed Recommended Prototype to Prototype Plan with all 14 sub-fields
- Weekly Life Conditions template now shows five to seven lines instead of a hard-coded five
- Clarified that lens names (Current Direction, Adjacent Life, Unconstrained Life) are design constraints and each future gets a user-specific title
- Added a thin-evidence rule for the ordinary-day section
- Added a global evidence rule distinguishing invented user facts from labeled coach-derived proposals
- Gave the Continuing AI-Companion Prompt (deliverable 25) a required six-point structure
- Mapped every One-Page Blueprint field to its upstream Core Blueprint section and removed unsourced fields (north-star direction, top five values)
- Added aspect ratios for all four image formats and prompt templates for desktop and phone wallpapers; added the one-visual-system rule
- Converted the AI Coach Memory privacy note to a coach-facing comment and added granularity guidance
- Marked the bundled examples as style exemplars, not a full evidence base

## 1.1.0 - 2026-07-11

- Added gravity-problem triage (actionable vs. unchangeable problems) to methodology and conversation protocol
- Added behavior-versus-words hypothesis check
- Added optional consent-based baseline projection with emotional-safety skip rule
- Added question budget (6–9 primary questions) and stated time commitment
- Added mid-session pause/resume via partial AI Coach Memory snapshots
- Enriched prototype plan: anti-vision and vision lines, quarterly core question, one-month buildable, pocket-practice reminders
- Added LITE_PROMPT.md: copy-paste version for claude.ai
- Extended validator to verify all duplicated references and templates stay identical
- Aligned README deliverable count with DELIVERABLES.md (27)

## 1.0.0 - 2026-07-11

- Initial GitHub-ready release
- Added Claude Code and Codex-compatible skill locations
- Added canonical root `SKILL.md`
- Added adaptive conversation protocol
- Added 27 core and extended deliverables
- Added image-generation evidence rules
- Added monthly, quarterly, and annual review prompts
- Added install and validation scripts
