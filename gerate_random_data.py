import plotly.graph_objects as go
import numpy as np

times = 5   #number of time running k-mean
k=6 # number of guess clusters
"""
guess_centers = np.random.randint(0, 100, (k, 2))  # guess k random centers

"""
guess_centers = np.array([[150, 200], [300, 230], [425, 193], [250, 250], [375, 280], [225, 250]])

which_cluster = []  # store which cluster each point belongs to

cluster_x = np.zeros((6, 0))
cluster_y = np.zeros((6, 0))

num_of_points = 100     # number of points for each circle data
center_x = [150, 300, 425, 250, 375, 225]   # center for generating data
center_y = [200, 230, 193, 250, 280, 250]
radius = 50

all_x_values = []  # create empty array to store all x and y values
all_y_values = []
all_colour =[]

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
        all_x_values.append(x_values[i])   # return all data points in one x and y array
        all_y_values.append(y_values[i]) 
    
  
    
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


def assign_to_cluster(guess_centers, x, y):
    distances = []
    for i in range(len(x)):
        distances = []
        for center in guess_centers:
            distance = np.sqrt((center[0] - x[i])**2 + (center[1] - y[i])**2)
            distances.append(distance)
        closest_index = np.argmin(distances)
        which_cluster.append(closest_index)  # store which cluster each point belongs to
        cluster_x[closest_index] += x[i]
        cluster_y[closest_index] += y[i]
        distances = []
    new_guess_center_x = cluster_x / len(x)
    new_guess_center_y = cluster_y / len(y)
    all_colour = [color[cluster] for cluster in which_cluster]
    return new_guess_center_x, new_guess_center_y, all_colour





for i in range(6):
    generate_data(num_of_points, center_x[i], center_y[i], radius, color[i])


'''
for x, y in zip(all_x_values, all_y_values):
    print(f"x: {x:.2f}, y: {y:.2f}")
'''

fig.show(config={'displayModeBar': False})

print('showing the first time, random data')






fig.data = []  # Clear the figure
which_cluster = []

new_x, new_y, all_colour = assign_to_cluster(guess_centers, all_x_values, all_y_values)

print(all_colour)
 # Update the colors of all data points
fig.add_trace(go.Scatter(x=all_x_values, y=all_y_values, mode='markers', marker=dict(color=all_colour, size=5)))

fig.show(config={'displayModeBar': False})
'''
for i in range (times):
    fig.data = []  # Clear the figure
    which_cluster = []

    assign_to_cluster(guess_centers, all_x_values, all_y_values)

    # Update the colors of all data points
    fig.add_trace(go.Scatter(x=all_x_values, y=all_y_values, mode='markers', marker=dict(color=all_colour, size=5)))

    for i in range(k):
        fig.add_trace(go.Scatter(x=guess_centers[i][0], y=guess_centers[i][0], mode='markers', marker=dict(color=color[i], size=20)))

    fig.show(config={'displayModeBar': False})
    print('showing the ', i+1, 'time, k-mean data')

    for i in range(k):
        guess_centers[i][0] = cluster_x[i] / len(all_x_values)
        guess_centers[i][1] = cluster_y[i] / len(all_y_values)


'''