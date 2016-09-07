import json

rappers_data = {}

num_collaborators = 0

percentage_collabs = []
total_songs = []
popularity = []
degrees = []
with open('degrees.json') as data_file:
    degree_data = json.load(data_file)
with open('popularities.json') as data_file:
    popularity_data = json.load(data_file)

for x in range(1, 197):
    with open('rapper_stats'+str(x)+'.json') as data_file:
        data = json.load(data_file)

    name = data.keys()[0]

    num_collabs = 0
    num_songs = 0
    collaborators = {}

    for track in data[name]:
        if len(track['artists']) > 1:
            num_collabs += 1
        num_songs += 1
        for artist in track['artists']:
            collaborators[artist['name']] = 1

    rappers_data[x] = {'num_songs': num_songs,
                       'num_collabs': num_collabs,
                       'collaborators': collaborators}

    # print len(collaborators), name
    # print collaborators

    num_collaborators = len(collaborators)
    print num_collaborators, name
    print num_collabs / float(num_songs)
    percentage_collabs.append(num_collabs / float(num_songs))
    popularity.append(popularity_data[name])
    total_songs.append(num_songs)
    print collaborators
    degrees.append(degree_data[name])

# Plot the scatter plot of Percentage Collabs vs Spotify Popularity

import plotly.plotly as py
import plotly.graph_objs as go

'''
# Create a trace
trace = go.Scatter(
    x = percentage_collabs,
    y = popularity,
    mode = 'markers',
    marker=dict(
        size='16',
        color=total_songs,
        colorscale='Viridis',
        showscale=True
    )
)

data = [trace]

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
'''

# Create a trace
trace = go.Scatter(
    x = degrees,
    y = popularity,
    mode = 'markers',
    marker=dict(
        size='16',
        color=total_songs,
        colorscale='Viridis',
        showscale=True
    )
)

data = [trace]

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
#plot_url = py.plot(fig, filename='Degree of Artist vs Popularity')