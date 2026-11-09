# product-feedback-analyzer

A Claude skill that turns raw user feedback (app store reviews, survey comments, NPS, support emails, feature requests, interview notes) into a ranked "what to build next" list, and can turn one theme into a one-page product spec.

## Structure

- `SKILL.md` — skill instructions and trigger description
- `references/` — urgent-issue rules and roadmap context
- `assets/one-pager-template.md` — template for the one-page spec
- `scripts/theme_stats.py` — helper script for theme statistics
- `tests/Test_skill.csv` — 54 sample feedback entries for testing against the fictional StudySync roadmap

## Usage

Add this folder as a skill in Claude (zip the folder with `SKILL.md` at its top level, or place it in your skills directory), then upload or paste feedback and ask Claude to analyze it.

To try it, use `tests/Test_skill.csv` as the feedback input. It contains fictional reviews, feature requests, bug reports, and urgent cases. The skill should label the feedback and then run `python scripts/theme_stats.py <labeled.csv>` on the labeled output.
