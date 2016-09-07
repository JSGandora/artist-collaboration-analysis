'''
This code generates two scatter plots of collaboration vs popularity of the rappers in our list. One, using
collaboration rate of songs as a metric, and the other using the degree of each rapper in the collaboration grapha
as a metric.
'''

import json

# initialize the rappers_data dictionary that will hold the information needed to plot the graphs
rappers_data = {}

# initialize the arrays needed to store data for plotting the graphs
percentage_collabs = []
total_songs = []
popularity = []
degrees = []

# load data from the json files
with open('degrees.json') as data_file:
    degree_data = json.load(data_file)
with open('popularities.json') as data_file:
    popularity_data = json.load(data_file)

# iterate through the rapper list and fill in the necessary data in our data structures
for x in range(1, 197):
    with open('rapper_stats' + str(x) + '.json') as data_file:
        data = json.load(data_file)

    name = data.keys()[0]
    num_collabs = 0
    num_songs = 0
    collaborators = {}

    # count the number of songs and number of collaborative songs for the artist
    for track in data[name]:
        if len(track['artists']) > 1:
            num_collabs += 1
        num_songs += 1
        for artist in track['artists']:
            collaborators[artist['name']] = 1

    # fill in the rapper_data dictionary
    rappers_data[x] = {'num_songs': num_songs,
                       'num_collabs': num_collabs,
                       'collaborators': collaborators}

    # calculate collaboration rate and commented out lines to test the code
    num_collaborators = len(collaborators)
    # print num_collaborators, name
    # print num_collabs / float(num_songs)
    percentage_collabs.append(num_collabs / float(num_songs))
    popularity.append(popularity_data[name])
    total_songs.append(num_songs)
    # print collaborators

    # update degree of the artist
    degrees.append(degree_data[name])



import plotly.plotly as py
import plotly.graph_objs as go

# plot the scatter plot of percentage collabs vs artist popularity

# Create a trace
trace = go.Scatter(
    x=percentage_collabs,
    y=popularity,
    mode='markers',
    marker=dict(
        size='16',
        color=total_songs,
        colorscale='Viridis',
        showscale=True
    )
)

data = [trace]

# set layout
layout = go.Layout(
    title='Collaboration Rate vs. Artist Popularity',
    xaxis=dict(
        title='Collaboration Rate',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Artist Spotify Popularity',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Percentage Collabs vs Popularity')

# plot the scatter plot of degree of artist vs artist popularity

# create a trace
trace = go.Scatter(
    x=degrees,
    y=popularity,
    mode='markers',
    marker=dict(
        size='16',
        color=total_songs,
        colorscale='Viridis',
        showscale=True
    )
)

data = [trace]

# set layout
layout = go.Layout(
    title='Degree of Artist vs. Artist Popularity',
    xaxis=dict(
        title='Number of Collaborators in Top 200',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Artist Spotify Popularity',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Degree of Artist vs Popularity')
