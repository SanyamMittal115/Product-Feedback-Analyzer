#!/usr/bin/env python3
"""Summarize labeled feedback: mentions, share, average rating, and roadmap status per theme.

Usage: python theme_stats.py labeled.csv

Needs `theme` and `needs_human` columns. Uses `rating` and `roadmap_status` if present.
Rows with needs_human == yes are reported as one "Needs human" row.
"""
import argparse, csv
from collections import defaultdict

p = argparse.ArgumentParser()
p.add_argument("path")
a = p.parse_args()

with open(a.path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
if not rows or "theme" not in rows[0]:
    raise SystemExit("CSV needs a 'theme' column.")

has_rating = "rating" in rows[0]
has_status = "roadmap_status" in rows[0]
counts, ratings, status = defaultdict(int), defaultdict(list), {}
for r in rows:
    human = str(r.get("needs_human", "")).strip().lower() in ("yes", "y", "true", "1")
    t = "Needs human" if human else (r["theme"].strip() or "Unlabeled")
    counts[t] += 1
    if has_rating:
        try:
            ratings[t].append(float(r["rating"]))
        except (ValueError, TypeError):
            pass
    if has_status:
        status.setdefault(t, "n/a" if human else r["roadmap_status"].strip())

total = sum(counts.values())
allr = [x for v in ratings.values() for x in v]
head = f"Total feedback: {total}"
if allr:
    head += f" | Average rating: {sum(allr)/len(allr):.1f}"
print(head + "\n")
cols = ["Theme", "Mentions", "% of total"]
if has_rating: cols.append("Avg rating")
if has_status: cols.append("Roadmap status")
print("| " + " | ".join(cols) + " |")
print("|" + "|".join(["---"] + ["---:"] * (2 + has_rating) + (["---"] if has_status else [])) + "|")
for t in sorted(counts, key=lambda k: -counts[k]):
    cells = [t, str(counts[t]), f"{counts[t]/total*100:.0f}%"]
    if has_rating:
        cells.append(f"{sum(ratings[t])/len(ratings[t]):.1f}" if ratings[t] else "-")
    if has_status:
        cells.append(status.get(t, ""))
    print("| " + " | ".join(cells) + " |")
