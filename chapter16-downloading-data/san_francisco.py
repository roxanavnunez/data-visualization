"""
Chapter 16 Exercise 3
"""

from pathlib import Path
import csv
from datetime import datetime

from matplotlib import pyplot as plt

script_dir = Path(__file__).parent
path = script_dir / 'weather_data/san_francisco_2021_full.csv'
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        high = int(row[8])
        low = int(row[10])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021\nSan Francisco", fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.set_ylim(0,150)
ax.tick_params(labelsize=16)

plt.show()