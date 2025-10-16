"""
Chapter 15 Exercise 10
Practicing with Plotly and Pandas
Make the visualization of a random walk
"""
import plotly.express as px
import pandas as pd

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(5_000)
rw.fill_walk()

# Create DataFrame
df = pd.DataFrame({
    'x': rw.x_values,
    'y': rw.y_values,
    'step': range(len(rw.x_values)),
    'progress': [i/len(rw.x_values) for i in range(len(rw.x_values))],
    })

# Visualization
fig = px.scatter(
    df,
    x='x',
    y='y',
    color='progress',
    color_continuous_scale='blues',
    title='Random Walk',
)

# Initial point
fig.add_scatter(
    x=[df['x'].iloc[0]], 
    y=[df['y'].iloc[0]],
    mode='markers',
    marker=dict(size=10, color='green'),
    name='Start',
    showlegend=True
)

#Final point
fig.add_scatter(
    x=[df['x'].iloc[-1]], 
    y=[df['y'].iloc[-1]],
    mode='markers',
    marker=dict(size=10, color='red'),
    name='End',
    showlegend=True
)

fig.show()
