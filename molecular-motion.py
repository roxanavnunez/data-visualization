import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:

    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')

    # Altering the size to fill the screen
    fig, ax = plt.subplots(figsize=(10,6))

    ax.plot(rw.x_values,rw.y_values,linewidth=3)
    
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0,0, c='green', edgecolors='none', s=300)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none', 
               s=300)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower().strip() == 'n':
        break