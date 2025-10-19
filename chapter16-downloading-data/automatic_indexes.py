"""
Chapter 16 Exercise 4
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

def _get_data(reader, index_city_name, index_date, index_tmin, index_tmax):
    """
    Extract the city name, dates and high and low temperatures from CSV file.
    """
    city_name = None
    dates, highs, lows = [], [], []
    for row in reader:
        if city_name == None:
            city_name = row[index_city_name]
        current_date = datetime.strptime(row[index_date], '%Y-%m-%d')
        try:
            high = int(row[index_tmax])
            low = int(row[index_tmin])
        except ValueError:
            print(f'Missing data for {city_name} {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    return city_name, dates, lows, highs

def _read_file(file_name):
    """Read weather data from CSV file."""
    script_dir = Path(__file__).parent
    path = script_dir / 'weather_data' / file_name
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    index_tmin = _get_index(header_row,'TMIN')
    index_tmax = _get_index(header_row, 'TMAX')
    index_city_name = _get_index(header_row, 'NAME')
    index_date = _get_index(header_row, 'DATE')
    city_name, dates, lows, highs = _get_data(reader, index_city_name, index_date, index_tmin, index_tmax)

    return city_name, dates, lows, highs

def plot_file(file_name):
    """Plot daily temperature ranges from weather data CSV."""
    city_name, dates, lows, highs = _read_file(file_name)

    # Plot the high and low temperatures.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    ax.set_title(f"Daily High and Low Temperatures, 2021\n{city_name}", fontsize=20)
    ax.set_xlabel("", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.set_ylim(0,150)
    ax.tick_params(labelsize=16)

    plt.show()

file1 = 'death_valley_2021_simple.csv'
file2 = 'sitka_weather_2021_simple.csv'

plot_file(file1)
plot_file(file2)
