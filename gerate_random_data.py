import plotly.graph_objects as go
import numpy as np

#######    generate two dimentional data for k-mean algorithm!!!!!
fig = go.Figure()


#input an array of centers, an array of radius, number of point, 
def generate_data(num_of_points, center_x, center_y, radius):
    x_values = [0] * num_of_points
    y_values = [0] * num_of_points
    theta = np.random.uniform(0, 2 * np.pi, num_of_points)
    length = np.random.randint(0, radius, num_of_points)
    for i in range(num_of_points):
        x_values[i] = center_x + length[i] * np.cos(theta[i])
        y_values[i] = center_y + length[i] * np.sin(theta[i])
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers', marker=dict(color='green', size=2)))
    
    # Update the figure
    fig.update_layout(width=500, height=500, title='Circle in a Square')

num_of_points = 100
center_x = [150, 300, 425]
center_y = [200, 230, 193]
radius = 50
for i in range(3):
    generate_data(num_of_points, center_x[i], center_y[i], radius)

fig.show(config={'displayModeBar': False})
