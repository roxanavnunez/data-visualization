"""Excersice 15-5"""

import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self,num_points=5_000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go, and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowwhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def get_step(self):
        """Determine direction and distance for each step"""
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')

# Altering the size to fill the screen
fig, ax = plt.subplots(figsize=(10,6))

# Color the points
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none',s=10)

ax.set_aspect('equal')

# Emphasize the first and last points.
ax.scatter(0,0, c='green', edgecolors='none', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none', 
            s=50)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
           