import csv, hashlib, os, time, math
from urllib.parse import quote
import requests

OUT = "docs"
os.makedirs(OUT, exist_ok=True)

queries = [
    "robot manipulation tactile transformer",
    "force torque transformer robotics",
    "contact-rich manipulation tactile memory",
    "visuo tactile transformer manipulation",
    "robot world model tactile contact",
    "action chunking transformer robotics",
    "haptic force sequence modeling robot",
    "tactile representation learning robotics",
    "force sensing manipulation transformer",
    "contact dynamics robot transformer",
]

seen = {}
rows = []

def add_row(source, title, year, url, doi, query, score):
    key = (title or "").strip().lower()
    if not key or key in seen:
        return
    seen[key] = True
    rows.append({
        "source": source,
        "query": query,
        "title": title,
        "year": year,
        "url": url,
        "doi": doi,
        "score": score,
    })

def crossref_query(q, rows_target=120):
    base = "https://api.crossref.org/works"
    cursor = "*"
    got = 0
    for page in range(3):
        params = {
            "query.title": q,
            "rows": 100,
            "cursor": cursor,
            "cursor_max": 10000,
        }
        r = requests.get(base, params=params, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        msg = r.json()["message"]
        cursor = msg.get("next-cursor", cursor)
        items = msg.get("items", [])
        for it in items:
            title = (it.get("title") or [""])[0]
            year = None
            for fld in ("published-print", "published-online", "created"):
                parts = it.get(fld, {}).get("date-parts", [[None]])
                if parts and parts[0] and parts[0][0]:
                    year = parts[0][0]
                    break
            add_row("crossref", title, year, it.get("URL"), it.get("DOI"), q, it.get("score"))
        got = len(rows)
        if got >= rows_target:
            break
        time.sleep(0.2)

for q in queries:
    try:
        crossref_query(q)
    except Exception as e:
        add_row("error", f"QUERY_ERROR: {q}", "", "", "", q, str(e))

# fallback expansion with robotics-adjacent queries if needed
extra_queries = [
    "robotics transformer manipulation",
    "tactile sensing manipulation",
    "contact-rich manipulation robot learning",
    "haptic robotics force sensing",
]
for q in extra_queries:
    try:
        crossref_query(q, rows_target=300)
    except Exception as e:
        add_row("error", f"QUERY_ERROR: {q}", "", "", "", q, str(e))

with open(os.path.join(OUT, "related_work_matrix.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["source", "query", "title", "year", "url", "doi", "score"])
    w.writeheader()
    for row in rows:
        w.writerow(row)

print(len(rows))
