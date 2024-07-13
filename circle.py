import plotly.graph_objects as go
import numpy as np

# Set the circle properties
circle_x = 250
circle_y = 250
circle_radius = 150

# Create the figure
fig = go.Figure()

# Draw the circle
theta = np.linspace(0, 2 * np.pi, 100)
x = circle_x + circle_radius * np.cos(theta)
y = circle_y + circle_radius * np.sin(theta)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='black', width=2)))

# Function to generate and draw random points
def generate_points():
    # Generate random points
    x = np.random.randint(0, 500, 1)
    y = np.random.randint(0, 500, 1)

    # Check if the point is inside the circle
    distance = np.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= circle_radius:
        # Point is inside the circle, display it in green
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='green', size=10)))
    else:
        # Point is outside the circle, display it in red
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='red', size=10)))

    # Update the figure
    fig.update_layout(width=500, height=500, title='Circle in a Square')
    fig.show(config={'displayModeBar': False})

# Generate and display points continuously
#while True:
    #generate_points()


generate_points()