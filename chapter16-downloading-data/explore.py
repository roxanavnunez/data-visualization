"""
Chapter 16 Exercise 5
"""
from pathlib import Path
import csv
from datetime import datetime
from matplotlib import pyplot as plt

def _get_index(header_row, column_name):
    """Find the index of a column in CSV header row."""
    for index, value in enumerate(header_row):
        if value == column_name:
            return index

script_dir = Path(__file__).parent
path = script_dir / 'weather_data/san_francisco_2021_full.csv'
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract city name, dates and PRCP
city_name = None
dates, prcps = [], []
index_date = _get_index(header_row, 'DATE')
index_prcp = _get_index(header_row, 'PRCP')
index_city = _get_index(header_row, 'NAME')

for row in reader:
    if city_name == None:
        city_name = row[index_city]
    current_date = datetime.strptime(row[index_date],'%Y-%m-%d')
    prcp = float(row[index_prcp])
    dates.append(current_date)
    prcps.append(prcp)

# Plot PRCP
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue')

# Format plot.
ax.set_title(f"Daily Rainfall Amounts, 2021\n{city_name}", fontsize=20)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("PRCP", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()