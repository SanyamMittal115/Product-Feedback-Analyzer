---
name: product-feedback-analyzer
description: Turns raw user feedback into a ranked "what to build next" list for product managers. Use whenever the user uploads or pastes app store reviews, survey comments, NPS comments, support emails, feature requests, or interview notes, or says "analyze this feedback", "what are users asking for", "what should we build next", "prioritize these requests", "find themes in these reviews", or "check this against the roadmap", even if they don't say "skill". Also use to turn one theme into a one-page product spec.
---

# Product Feedback Analyzer

Turns a pile of messy user feedback into: themes ranked by how often they come up, a check of each theme against the roadmap, urgent items for a human, and (on request) a one-page spec.

## Before you start

The product's knowledge lives in `references/`:
- `references/roadmap.md` lists what is shipped (and where to find it), partial, planned, not planned, and known bugs. **Read this before labeling anything.**
- `references/urgent-rules.md` is what must go to a human.
- `assets/one-pager-template.md` is the format for a product spec.

The bundled files describe a fictional app (StudySync, a study planner and flashcard app). For a real product, the user replaces the files in `references/` and nothing else changes.

## Pick the mode

| The user wants... | Mode |
|---|---|
| Analysis of many pieces of feedback (CSV, spreadsheet, pasted list) | 1. Analyze a batch |
| A spec or one-pager for one theme | 2. Draft a one-pager |

If a batch analysis finds a strong theme, finish Mode 1, then offer Mode 2 for the top one or two.

## Mode 1: Analyze a batch

1. **Load the file.** Required: `feedback_id`, `message`. Optional: `rating` (1-5), `source`. If `rating` is missing, skip the rating column and say so.
2. **Read every message.** Do not sample or use keyword matching. Group by meaning: "add dark mode", "the white screen hurts my eyes at night", and "is there a night theme?" are one theme.
3. **Flag urgent items first.** Any message matching `urgent-rules.md` goes in a separate "Needs human" group and is not counted in theme rows.
4. **Label the rest.** One short, consistent theme name per message. If a message fits two themes (praise plus a request), pick the actionable one and don't double count. Pure praise gets the theme "Praise". Messages with no usable detail get "Unclear feedback".
5. **Check the roadmap for every theme** (not just the top ones). Mark each with one `roadmap_status`:
   - **Shipped**: it already exists. Users are asking because they can't find it.
   - **Partial**: it exists but is missing what users keep asking for.
   - **Planned**: on the roadmap, not yet built.
   - **Not planned**: not on the roadmap, or deliberately out of scope.
   - **Tracked bug**: a bug listed under known bugs.
   - **Untracked bug**: a bug not on the known list.
   - **n/a**: praise, unclear feedback, and every "Needs human" row.
6. **Save the file.** Save a copy of the CSV to the outputs folder with three added columns: `theme`, `needs_human` (yes/no), and `roadmap_status`. All three columns are always present, even if every status is the same.
7. **Do the math with the script, not in your head:**
   `python scripts/theme_stats.py <labeled.csv>`
   It prints mentions, share of total, average rating, and roadmap status per theme.
8. **Report** in this order:
   - One-sentence headline (example: "Three themes make up 40% of feedback, and one of them is a feature you already shipped.")
   - The ranked table from the script
   - Top 3 themes, each with 2 short real quotes
   - Roadmap findings: **Shipped but still requested** means a discoverability problem, not a build problem. **Planned with high volume** may deserve a higher priority. **Not planned with high volume** should be revisited or confirmed on purpose. Bugs with low ratings come first.
   - Urgent items for a human, with the rule matched and urgency
   - Recommended next step (usually: fix discoverability, then reprioritize, then write the one-pager for the top build)

Be honest about uncertainty. If the file is small, say the percentages are rough. Mentions are not users: one person can send several messages.

## Mode 2: Draft a one-pager

1. Pick the theme (highest volume that is Planned, Partial, or Not planned, unless the user names one).
2. Fill `assets/one-pager-template.md` using only the feedback and the roadmap. Quote real feedback as evidence and give the count.
3. For anything you don't know (effort, dates, technical limits, pricing), leave a clearly marked `[CONFIRM: ...]` placeholder. Never invent them.

## Don't

- Don't invent roadmap dates, effort estimates, or user numbers.
- Don't treat praise as a request.
- Don't send an urgent item through normal analysis; flag it for a human.
- Don't treat figures of speech ("I'd kill for offline mode") as threats.
- Don't paste long messages back; quote briefly.
