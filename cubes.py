"""
Chapter 15 Excersise 2
"""

import matplotlib.pyplot as plt

""" Plot the first five cubic numbers"""

# First five cubic numbers
x_values = range(1,6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

ax.scatter(x_values,y_values,color='red',s=100)

# Set chart title and label axes.
ax.set_title("First 5 cubic numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of a value", fontsize=14)
ax.tick_params(labelsize=14)

"""Plot the first 5_000 cubic numbers"""

# First 5_000 cubic numbers
x_values2 = range(1,5_001)
y_values2 = [x**3 for x in x_values2]

plt.style.use('ggplot')
fig, ax2 = plt.subplots()

ax2.scatter(x_values2,y_values2,color='green',s=10)

# Set chart title and label axes.
ax2.set_title("First 5_000 cubic numbers", fontsize=24)
ax2.set_xlabel("Value", fontsize=14)
ax2.set_ylabel("Cube of a value", fontsize=14)
ax2.tick_params(labelsize=14)

plt.show()


