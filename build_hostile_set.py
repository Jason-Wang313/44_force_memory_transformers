from pathlib import Path

top = Path("docs/top_300_titles.txt").read_text(encoding="utf-8").splitlines()
selected = top[:100]
out = ["# Hostile Prior Set", ""]
for line in selected:
    out.append(f"- {line}")
Path("docs/hostile_prior_set.md").write_text("\n".join(out), encoding="utf-8")
print(len(selected))
