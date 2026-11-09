---
name: product-feedback-analyzer
description: Analyze product feedback from reviews, surveys, support messages, feature requests, or interview notes. Use when someone asks what users are requesting, which problems come up most often, what to build next, or how feedback compares with the roadmap. Can also draft a one-page feature proposal from a theme.
---

# Product Feedback Analyzer

Use this skill to organize user feedback into themes, compare those themes with the roadmap, and identify what deserves attention. It can also write a short feature proposal based on the findings.

## Start here

Read these files before analyzing feedback:

- `references/roadmap.md` - What's shipped, partially available, planned, out of scope, and already tracked as a bug
- `references/urgent-rules.md` - Feedback that needs human review
- `assets/one-pager-template.md` - Format to use for feature proposals

The included references describe StudySync, a fictional study planner and flashcard app. For a different product, use that product's roadmap and escalation rules instead.

## Choose the task

- For a CSV, spreadsheet, or list of reviews, follow **Analyze feedback**.
- For a request to write a feature spec, follow **Write a one-pager**.

After analyzing a batch, you can offer to write a one-pager for one of the leading themes.

## Analyze feedback

1. **Open the data.** The file must have `feedback_id` and `message` columns. `rating` (1-5) and `source` are optional. If ratings aren't provided, leave them out of the summary and mention that.
2. **Read every message.** Don't sample the file or rely only on keywords. Group messages by what users mean. For example, requests for a night theme and complaints about a bright screen belong under the same dark mode theme.
3. **Check for urgent issues first.** Apply `references/urgent-rules.md`. Put matching messages in a separate "Needs human" group, not in the regular theme counts.
4. **Give each remaining message one theme.** Use short, consistent names. When a message contains praise and a feature request, classify the request. Use "Praise" for praise alone and "Unclear feedback" when there's not enough detail. Don't count a message twice.
5. **Check every theme against the roadmap.** Use one of these values for `roadmap_status`:
   - **Shipped** - The feature already exists.
   - **Partial** - Some of the functionality exists, but users are asking for more.
   - **Planned** - It's on the roadmap but hasn't shipped.
   - **Not planned** - It's not on the roadmap or is intentionally out of scope.
   - **Tracked bug** - The issue appears in the known bugs list.
   - **Untracked bug** - The issue is a bug but isn't listed.
   - **n/a** - Praise, unclear feedback, or anything marked "Needs human".
6. **Save a labeled CSV.** Keep the original columns and add `theme`, `needs_human` (yes/no), and `roadmap_status`. Always include all three columns.
7. **Calculate the numbers with the script.** Run `python scripts/theme_stats.py <labeled.csv>`. Use its results for mention counts, percentages, average ratings, and roadmap status.
8. **Write the summary.** Include:
   - A short opening with the main finding
   - The ranked table from the script
   - The top three themes, with two short quotes from real feedback for each
   - What the roadmap comparison tells us
   - Urgent items, the rule each matched, and their urgency
   - A practical next step

When interpreting the roadmap, don't assume every popular request needs a new feature. If something has already shipped, users may just have trouble finding it. Planned features with a lot of feedback may deserve another look at priority. Bugs with low ratings should get attention.

If the sample is small, say so. A mention isn't necessarily a unique user.

## Write a one-pager

1. Use the theme the user asks for. Otherwise, choose a high-volume theme marked Planned, Partial, or Not planned.
2. Fill in `assets/one-pager-template.md` using the feedback and roadmap. Include the mention count and short, real quotes.
3. If something isn't known, such as timing, engineering effort, technical constraints, or pricing, write `[CONFIRM: ...]` rather than guessing.

## Things to watch for

- Don't make up dates, effort estimates, or user counts.
- Don't turn praise into a feature request.
- Don't bury urgent reports in the regular analysis.
- Don't mistake figures of speech, like "I'd kill for offline mode", for actual threats.
- Keep quotes short and use the original wording.
