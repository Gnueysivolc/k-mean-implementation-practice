import plotly.graph_objects as go
import numpy as np


k=6 # number of clusters
"""
guess_centers = np.random.randint(0, 100, (k, 2))  # guess k random centers

"""
guess_centers = np.array([[150, 200], [300, 230], [425, 193], [250, 250], [375, 280], [225, 250]])


num_of_points = 100     # number of points for each circle data
center_x = [150, 300, 425, 250, 375, 225]   # center for generating data
center_y = [200, 230, 193, 250, 280, 250]
radius = 50

all_x_values = []  # create empty array to store all x and y values
all_y_values = []


#######    generate two dimentional data for k-mean algorithm!!!!!
fig = go.Figure()
color = ['red', 'blue', 'yellow', 'purple', 'black', 'green']

#input an array of centers, an array of radius, number of point, 
def generate_data(num_of_points, center_x, center_y, radius, color):
    x_values = [0] * num_of_points  # create x and y arrays of all 0 of size of num of points
    y_values = [0] * num_of_points
    theta = np.random.uniform(0, 2 * np.pi, num_of_points)
    length = np.random.randint(0, radius, num_of_points)
    for i in range(num_of_points):
        x_values[i] = center_x + length[i] * np.cos(theta[i])  # x = center * random length and random angle
        y_values[i] = center_y + length[i] * np.sin(theta[i])  # y = center * random length and random angle
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers', marker=dict(color=color, size=5)))
    
    # Update the figure
    fig.update_layout(
    title='circle data', 
    xaxis=dict(
            range=[0, 500],
            anchor='x',
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            range=[0, 500],
            anchor='y',
            showgrid=False,
            zeroline=False
        ),
    barmode='overlay', 
    plot_bgcolor='rgb(245,245,245)',
    legend=dict(
        x=0.02,
        y=0.95),
    margin = dict(t=0, b=0, l=0, r=0)
    )

    all_x_values.extend(x_values)   # return all data points in one x and y array
    all_y_values.extend(y_values)   




for i in range(6):
    generate_data(num_of_points, center_x[i], center_y[i], radius, color[i])

'''
for x, y in zip(all_x_values, all_y_values):
    print(f"x: {x:.2f}, y: {y:.2f}")
'''

def cal_assign(center, x, y):
    distance = np.sqrt((x - center[0])**2 + (y - center[1])**2)
    return distance

fig.show(config={'displayModeBar': False})

