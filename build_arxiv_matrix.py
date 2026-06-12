import csv, os, time, re
from urllib.parse import quote
import requests
import xml.etree.ElementTree as ET

OUT = "docs"
os.makedirs(OUT, exist_ok=True)

queries = [
    "all:robotics",
    "all:manipulation",
    "all:transformer AND robotics",
    "all:tactile",
    "all:force sensing",
    "all:world model AND robot",
    "all:imitation learning AND robot",
    "all:contact-rich AND robot",
    "all:policy AND robot AND tactile",
    "all:haptic AND robot",
]

ns = {"a": "http://www.w3.org/2005/Atom", "opensearch": "http://a9.com/-/spec/opensearch/1.1/"}
seen = set()
rows = []

def get_text(el, path):
    node = el.find(path, ns)
    return node.text.strip() if node is not None and node.text else ""

def harvest(query, start=0, max_results=100):
    url = f"https://export.arxiv.org/api/query?search_query={quote(query)}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return ET.fromstring(r.text)

for q in queries:
    for start in [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]:
        try:
            root = harvest(q, start=start, max_results=100)
            entries = root.findall("a:entry", ns)
            if not entries:
                break
            for e in entries:
                title = " ".join(get_text(e, "a:title").split())
                aid = get_text(e, "a:id")
                year = get_text(e, "a:published")[:4]
                key = title.lower()
                if key in seen:
                    continue
                seen.add(key)
                rows.append({
                    "source": "arxiv",
                    "query": q,
                    "title": title,
                    "year": year,
                    "url": aid,
                    "doi": "",
                    "score": "",
                })
            time.sleep(0.2)
        except Exception as ex:
            rows.append({
                "source": "error",
                "query": q,
                "title": f"QUERY_ERROR: {q}",
                "year": "",
                "url": "",
                "doi": "",
                "score": str(ex),
            })
            break

with open(os.path.join(OUT, "related_work_matrix.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["source", "query", "title", "year", "url", "doi", "score"])
    w.writeheader()
    for row in rows:
        w.writerow(row)

print(len(rows))
