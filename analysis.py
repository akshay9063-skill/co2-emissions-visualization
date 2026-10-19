from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "visualizations"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA / "selected_country_emissions_2024.csv")
trend = pd.read_csv(DATA / "rounded_historical_trend.csv")

ranked = df.sort_values("co2_emissions_2024_billion_tonnes")
fig, ax = plt.subplots(figsize=(9, 5.4))
ax.barh(ranked["country"], ranked["co2_emissions_2024_billion_tonnes"])
ax.set_title("Annual CO₂ emissions by selected countries (2024)")
ax.set_xlabel("Billion tonnes of CO₂")
ax.set_ylabel("")
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "01_country_ranking.png", dpi=180)
plt.close(fig)

values = df["co2_emissions_2024_billion_tonnes"].tolist()
labels = df["country"].tolist()
rest = 38.6 - sum(values)
values.append(rest)
labels.append("Other countries/regions")
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, pctdistance=0.72)
ax.set_title("Approximate share of global annual CO₂ emissions (2024)")
fig.tight_layout()
fig.savefig(OUT / "02_global_share.png", dpi=180)
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 5.4))
for col in ["China", "United States", "India"]:
    ax.plot(trend["year"], trend[col], marker="o", linewidth=2, label=col)
ax.set_title("CO₂ emissions trend: China, United States and India")
ax.set_xlabel("Year")
ax.set_ylabel("Billion tonnes of CO₂ (rounded, exploratory)")
ax.set_xticks(trend["year"])
ax.grid(alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "03_trend.png", dpi=180)
plt.close(fig)
print("Charts regenerated in visualizations/.")
