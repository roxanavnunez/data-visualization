from pathlib import Path
import csv

script_dir = Path(__file__).parent
path = script_dir / 'weather_data/sitka_weather_07-2021_simple.csv'
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)