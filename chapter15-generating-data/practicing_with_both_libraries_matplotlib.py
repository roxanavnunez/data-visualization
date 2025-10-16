"""
Chapter 15 Exercise 10
Practicing with matplotlib
Make a Die-rolling visualization
"""
import matplotlib.pyplot as plt
from collections import Counter
from die import Die

# Create a D6 dice.
# Number of rolls
die = Die()
roll_number = 1000

# Make some rolls, and store results in a list.
results = [die.roll() for _ in range(roll_number)]

# Analyze the results.
frequencies = Counter(results)

# Visualize the results.
title = f"Results of Rolling a D6 {roll_number:,} Times"

fig, ax = plt.subplots()
ax.bar(list(frequencies.keys()),
       list(frequencies.values()))
ax.set_title(title)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

plt.show()