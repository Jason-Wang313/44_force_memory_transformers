import csv, re, json, os

rows = list(csv.DictReader(open("docs/related_work_matrix.csv", encoding="utf-8")))
keywords = [
    "tactile", "force", "haptic", "contact", "manipulation", "transformer",
    "world model", "imitation", "policy", "robot", "memory", "sequence",
]

def score(title):
    t = title.lower()
    s = 0
    for kw in keywords:
        if kw in t:
            s += 3
    if "transformer" in t and ("tactile" in t or "force" in t or "contact" in t):
        s += 5
    if "world model" in t or "memory" in t:
        s += 4
    return s

rows.sort(key=lambda r: (score(r["title"]), r["year"]), reverse=True)
with open("docs/top_300_titles.txt", "w", encoding="utf-8") as f:
    for r in rows[:300]:
        f.write(f'{score(r["title"]):02d} | {r["year"]} | {r["title"]}\n')
print(rows[:20])
