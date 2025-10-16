"""
Chapter 15 Exercise 9
Using Counter class
"""
import plotly.express as px

from collections import Counter

from die import Die

# Create three D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(1_000)]

# Analyze the results.
frequencies = Counter(results)

# Visualize the results.
title = "Results of Rolling Three D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(
    x=list(frequencies.keys()), 
    y=list(frequencies.values()), 
    title=title, 
    labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# Show the Figure in the explorer
fig.show()