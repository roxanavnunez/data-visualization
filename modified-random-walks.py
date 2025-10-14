"""Chapter 15 Exercise 4"""
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

            # Rempove -1
            x_direction = choice([0,1])

            # Longer list of choices
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            x_step = x_direction * x_distance

            # Remove -1
            y_direction = choice([0,1])
            
            # Longer list of choices
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            y_step = y_direction * y_distance

            # Reject moves that go nowwhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# Make a random walk.
rw = RandomWalk(5_000)
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')

# Altering the size to fill the screen
fig, ax = plt.subplots(figsize=(10,6))

# Color the points
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none',s=1)

ax.set_aspect('equal')

# Emphasize the first and last points.
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none', 
            s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()