import plotly.graph_objects as go
import numpy as np

#######    generate two dimentional data for k-mean algorithm!!!!!
fig = go.Figure()


#input an array of centers, an array of radius, number of point, 
def generate_data(num_of_points, center_x, center_y, radius):
    
    theta = np.random.randint(0, 2 * np.pi, num_of_points)
    length = np.random.randint(0, radius, num_of_points)
    for i in range(num_of_points):
        x = center_x + length[i] * np.cos(theta[i])
        y = center_y + length[i] * np.sin(theta[i])
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='green', size=2)))



# Function to generate and draw random points
def generate_points():
    # Generate random points
    x = np.random.randint(0, 500, 1)
    y = np.random.randint(0, 500, 1)

    # Check if the point is inside the circle
    distance = np.sqrt((x - circle_x)**2 + (y - circle_y)**2)
    if distance <= circle_radius:
        # Point is inside the circle, display it in green
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='green', size=2)))
    else:
        # Point is outside the circle, display it in red
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers', marker=dict(color='red', size=2)))

    # Update the figure
    fig.update_layout(width=500, height=500, title='Circle in a Square')

    


# Generate and display points continuously
for i in range(100):
    generate_points()


fig.show(config={'displayModeBar': False})
