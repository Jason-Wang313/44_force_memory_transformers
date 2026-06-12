import json, os
import matplotlib.pyplot as plt

data = json.load(open("docs/synthetic_results.json", encoding="utf-8"))
names = list(data.keys())
overall = [data[k]["overall_acc"] for k in names]
switch = [data[k]["switch_acc"] for k in names]

fig, ax = plt.subplots(figsize=(5.2, 2.8))
x = range(len(names))
ax.bar([i-0.18 for i in x], overall, width=0.36, label="overall")
ax.bar([i+0.18 for i in x], switch, width=0.36, label="switch points")
ax.set_ylim(0, 1.0)
ax.set_xticks(list(x))
ax.set_xticklabels(["Flat\nTransformer", "Forget\nMemory"], fontsize=9)
ax.set_ylabel("Accuracy")
ax.legend(frameon=False)
ax.set_title("Explicit forgetting helps most at phase switches")
fig.tight_layout()
os.makedirs("figures", exist_ok=True)
fig.savefig("figures/force_memory_synth.png", dpi=200)
