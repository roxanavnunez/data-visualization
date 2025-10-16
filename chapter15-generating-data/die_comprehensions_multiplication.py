"""
Chapter 15 Exercise 9
Using Counter
"""
import math
import plotly.express as px
from collections import Counter
from die import Die

# Create two D6
num_dice = 2
dice = [Die() for _ in range(num_dice)]

# Make some rolls, and store results in a list.
num_rolls = 1000
results = [math.prod(die.roll() for die in dice) for _ in range(num_rolls)]

# Analyze the results.
frequencies = Counter(results)

# Visualize the results.
title = f"Results of Multiplying {num_dice} D6 {num_rolls:,} Times"
labels = {"x": "Result", "y": "Frequency of Result"}

fig = px.bar(
    x=list(frequencies.keys()), 
    y=list(frequencies.values()), title=title, 
    labels=labels)

# Further customize chart. 
# Include impossible results
fig.update_layout(xaxis_dtick=1)

# Show the Figure in the explorer
fig.show()