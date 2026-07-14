# Review Cadence

## Choosing a cadence

The cadence is the user's choice; offer the options and let them pick. Guidance to offer, not impose:

- An active experiment benefits from weekly or monthly check-ins, matched to how fast its evidence arrives.
- A steady stretch of life may only need the quarterly reset.
- Cadences stack well: a weekly self-review, a monthly session with the coach, a quarterly re-score of the futures.
- The cadence can change at any review. Changing it is itself a design decision; ask for one sentence of reasoning so the change is deliberate rather than drift.
- The day and time are the user's choice too. A review scheduled for a moment the user cannot honor is a review that will not happen; ask when in their week or month the ten to ninety minutes genuinely exist.

## The review loop

Every review, at any cadence, follows the same five moves:

1. Ask what progress or milestones happened since the last review, one short question at a time.
2. Tie each milestone back to the deliverables it touches: the Life Map (the experiment box, the path being tested), the Blueprint (dashboard scores, prototype status, boundaries), and the weekly conditions. Practices the user picked earlier from the Practice Menu count as experiments here: keep, adjust, or drop each one based on what actually happened.
3. At monthly and larger reviews, ask what the user would like to add to their life or career roadmap for the future: a goal, a skill, a relationship investment, an experience, a contribution. Place each addition into the deliverables where it belongs: the One-Year Roadmap first, then the prototype plan when it deserves an experiment, the three paths when it reshapes one, and the weekly conditions when it needs protected time. An addition that lands nowhere yet goes into the AI Coach Memory's open questions so it is not lost. Then guide, do not just collect: from `references/PRACTICE_MENU.md` (organized by the same life areas), proactively bring the two to four practices most relevant to this user's evidence, with one clause each on why it fits them, and ask which they want to prioritize now, add to the roadmap, or give weekly time to, or whether something else deserves the focus instead. Shrink whatever they pick until starting feels easy.
4. Show the user the updated deliverables in the conversation and ask them to confirm or correct the updates before anything is saved.
5. Close with a concise adjustment plan, then ask whether the current cadence still fits or should move (weekly, monthly, or quarterly), and confirm the next review's date and time; the user chooses both, down to the day and hour that fit their life. When the user changes cadence, update their reminder to match: reschedule the scheduled task where the environment supports it, or hand them the new review prompt and suggest updating their calendar. Refresh the AI Coach Memory with the new date.

Progress the user cannot see back in their own deliverables is progress the method gets no credit for; the tie-back is what makes the review feel like their life advancing, not another status meeting.

Presentation rule: the deliverables are the ending, not the file paths. The review's final message shows the content itself, in the conversation: the updated Life Map (drawn visually when a rendering tool is available, in its text form otherwise), the top three priorities, the period's action items, and the single most useful next step. Saving to files is storage, not communication. Update files quietly after the user confirms, mention their location in one short line at most, and never end a review with only "saved to a file".

## Reminders

Reviews only work when they happen, so always offer a reminder at session close.

When the environment provides scheduling tools (for example Claude Code scheduled tasks), offer to create a recurring task on the user's chosen cadence, at the day and time they pick (a Sunday evening, the 15th at 9am, a first-Friday morning); the reminder should arrive when they can actually act on it. The scheduled prompt must be self-contained and instruct the future session to:

1. Load the user's saved AI Coach Memory block (or file, if the user chose a location).
2. Greet the user and, before conducting the review, confirm the frequency still fits: keep the current cadence, or change it (and the day or time) right now. If the user changes it, reschedule the reminder first, then ask whether they want to run the review now or wait for the new date. Then ask what progress or milestones happened since the last review, one short question at a time: what they achieved, what the active experiment produced, score movements, and anything important that happened.
3. Tie each milestone back to the deliverables it touches and update only the sections supported by the new evidence, following the matching review prompt in `prompts/`. Review previously picked practices like any other experiment.
4. Ask what the user would like to add to their life or career roadmap for the future, and place each addition into the deliverables where it belongs. Then proactively bring the most relevant practices from `references/PRACTICE_MENU.md` for their situation and ask which to prioritize, add to the roadmap, or give weekly time to, or whether something else deserves the focus.
5. Show the updated deliverables in the conversation and ask the user to confirm or correct them before saving.
6. End with a concise adjustment plan, ask whether to keep the current cadence or change it, set the next review date accordingly (rescheduling this task when the user changes cadence), and refresh the AI Coach Memory block.

When no scheduling tool exists, give the user the matching review prompt text to save and suggest they set a calendar reminder for the chosen date.

Never ask for an email address, phone number, or other contact details. The skill runs inside the user's own AI environment and has no way to send messages; collecting contact information would gather sensitive data it cannot use.

## Weekly review: 10 minutes

1. What gave me energy?
2. What consumed energy without enough value?
3. Who did I invest in?
4. Did my calendar reflect my top three weekly conditions?
5. What evidence did I collect from an active experiment?
6. What will I adjust next week?

## Monthly review: 30 minutes

Review dashboard scores, energy map, relationship investments, current experiments, decision filters, and boundaries. Update only what changed.

## Quarterly reset: 60–90 minutes

If a vision letter exists, open and read it before anything else.

Ask:

- What surprised me?
- Which assumption proved inaccurate?
- Which experiment should stop, continue, or expand?
- Is my ordinary day improving?
- Which portfolio area has been neglected?
- What deserves the next quarter's primary experiment?

## Annual redesign: 2–3 hours

Revisit the three two-year paths, personal compass, weekly conditions, relationship architecture, financial foundation, manifesto, and ordinary day. Create new paths when the old set no longer represents credible choices.
