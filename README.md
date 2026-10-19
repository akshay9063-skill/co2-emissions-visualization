# CO₂ Emissions Data Visualization and Communication

## Project objective
Communicate patterns in annual territorial CO₂ emissions using clear, annotated visualizations and a short evidence-based narrative.

## Data source
Our World in Data (OWID), *Annual CO₂ emissions*, sourced from the Global Carbon Budget (2025):
https://ourworldindata.org/grapher/annual-co2-emissions-per-country

OWID reports 2024 annual emissions of approximately 12.3 billion tonnes for China, 4.9 billion for the United States, 3.19 billion for India, and 38.6 billion tonnes globally. Emissions exclude land-use change; territorial accounting attributes emissions to where they are produced, not where goods are consumed.

## Files
- `data/selected_country_emissions_2024.csv`: selected 2024 country values used in the ranking chart.
- `data/rounded_historical_trend.csv`: rounded trend points used for a high-level illustrative trend. Treat these as exploratory rounded values, not precision estimates.
- `visualizations/`: exported PNG charts.
- `src/analysis.py`: Python script to regenerate the charts from the included data.
- `report.docx`: report submitted for the task.

## Run locally
1. Install Python 3.10+.
2. In a terminal, run `python -m pip install pandas matplotlib`.
3. From this folder, run `python src/analysis.py`.

## Main findings
1. China is the largest emitter among the selected countries in the 2024 comparison.
2. The United States and India follow, with a substantial gap between the first and second positions.
3. The trend chart suggests different trajectories: China and India rise across the selected years, while US emissions are lower in 2020 than in 2000 and recover slightly by 2024.
4. The seven selected countries together account for a little over half of the reported global total; the remaining share is distributed across other countries and regions.

## Limitations
The country ranking uses values reported by OWID for 2024 and rounded for readability. The historical trend file is deliberately rounded and exploratory; use the linked OWID dataset for precise year-by-year analysis. Territorial emissions do not represent consumption-based emissions, and totals may vary by dataset revision.

## Citation
Our World in Data. “Annual CO₂ emissions.” Data source: Global Carbon Budget (2025). Retrieved October 2026. https://ourworldindata.org/grapher/annual-co2-emissions-per-country
