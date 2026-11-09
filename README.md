# Product Feedback Analyzer

I built this Claude skill to make sense of product feedback without having to manually sort through every review or feature request.

Give it a CSV of user feedback and it will group similar comments, check them against your product roadmap, and show which issues are coming up most often. It also flags feedback that needs a person to step in, like billing problems or data loss.

The goal is to make it easier to decide what to fix, what to build, and what users might simply be having trouble finding.

## What it does

- Groups feedback by theme, even when users describe the same problem differently
- Counts mentions and calculates average ratings for each theme
- Compares requests with the roadmap to see what's shipped, planned, or missing
- Separates urgent reports from regular feature feedback
- Creates a one-page feature proposal when you want to explore a theme further

## Files

- `SKILL.md` - Instructions Claude follows when analyzing feedback
- `references/roadmap.md` - Example roadmap for a fictional study app called StudySync
- `references/urgent-rules.md` - Rules for flagging issues that need human review
- `scripts/theme_stats.py` - Python script that calculates theme statistics
- `assets/one-pager-template.md` - Template for turning a theme into a feature proposal
- `tests/Test_skill.csv` - Sample dataset with 54 feedback messages
- `tests/answer_key.csv` - Expected classifications for the sample dataset

## Trying it out

1. Add this folder as a Claude skill, with `SKILL.md` at the root.
2. Upload `tests/Test_skill.csv` and ask Claude to analyze the feedback.
3. Compare the labeled results with `tests/answer_key.csv`.

The test data covers feature requests, complaints, bugs, praise, and cases that should be escalated. It uses StudySync, a fictional flashcard and study planner app.

For your own product, replace the files in `references/` with your roadmap and escalation rules.

## How the analysis works

Claude reads each message, assigns a theme, and checks its status against the roadmap. It saves a labeled CSV and uses the Python script to calculate the summary table:

```bash
python scripts/theme_stats.py labeled.csv
```

The output includes the number of mentions, share of feedback, average rating, and roadmap status for each theme.

One important limitation: feedback volume isn't the same as the number of unique users. The skill is meant to help with prioritization, not make the final product decision for you.
