from pathlib import Path
import csv

script_dir = Path(__file__).parent
path = script_dir / 'weather_data/sitka_weather_07-2021_simple.csv'
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)