"""
Plot a simple line graph
Customize it to create more informative data visualization
"""

import matplotlib.pyplot as plt

# Data to plot. 
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Using built-in styles
plt.style.use('seaborn-v0_8')


# subplot can generate one or more plots in the same figure (fig).
# Plot the data.
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Display the plot. 
plt.show()