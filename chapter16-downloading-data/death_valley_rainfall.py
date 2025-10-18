"""
Chapter 16 Exercise 1 
Optional
"""
from pathlib import Path
import csv
from datetime import datetime
from matplotlib import pyplot as plt

script_dir = Path(__file__).parent
path = script_dir / 'weather_data/death_valley_2021_full.csv'
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and PRCP
dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[2],'%Y-%m-%d')
    prcp = float(row[3])
    dates.append(current_date)
    prcps.append(prcp)

# Plot PRCP
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue')

# Format plot.
ax.set_title("Daily Rainfall Amounts, 2021\nDeath Valley, CA", fontsize=24)
ax.set_xlabel("", fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("PRCP", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()