"""
Plot a simple line graph
Customize it to create more informative data visualization
"""

import matplotlib.pyplot as plt

# Data to plot. 
squares = [1, 4, 9, 16, 25]

# subplot can generate one or more plots in the same figure (fig).
fig, ax = plt.subplots()

# plot the data.
ax.plot(squares)

# Display the plot. 
plt.show()