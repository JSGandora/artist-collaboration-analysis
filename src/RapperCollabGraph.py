import networkx as nx
import matplotlib.pyplot as plt

import json

with open('rapper_names.json') as data_file:
    rapper_names = json.load(data_file)

with open('rapper_names.json', 'w') as df:
    json.dump(rapper_names, df)

G = nx.Graph()
Edges = []

max_nodes = 197

for x in range(1, max_nodes):
    with open('rapper_stats'+str(x)+'.json') as data_file:
        tracks = json.load(data_file)
    tracks_info = tracks[tracks.keys()[0]]
    for track in tracks_info:
        for x in range(len(track['artists'])):
            for y in range(x+1, len(track['artists'])):
                if(track['artists'][x]['name'] in rapper_names[:max_nodes] and track['artists'][y]['name'] in rapper_names[:max_nodes]):
                    G.add_edge(track['artists'][x]['name'], track['artists'][y]['name'])

pos = nx.spring_layout(G)
# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,width=3)

# labels
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

print 'WE HAVE FINISHED PARSING DATA'

'''
plt.axis('off')
plt.savefig("weighted_graph2.png") # save as png
plt.show() # display
'''

print nx.connected_components(G)
print sorted(nx.degree(G).values())

# The following code plots the histogram of degrees
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
x = nx.degree(G).values()

trace = go.Histogram(
    x=x,
    histnorm='count',
    name='control',
    autobinx=False,
    xbins=dict(
        start=0,
        end=70,
        size=2
    ),
    marker=dict(
        color='fuchsia',
        line=dict(
            color='grey',
            width=0
        )
    ),
    opacity=0.75
)
data = [trace]

layout = go.Layout(
    title='Degree Distribution of Nodes in Collaboration Graph',
    xaxis=dict(
        title='Node Degree',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
#plot_url = py.plot(fig, filename='Degree Distribution')

degrees = {}
for name in rapper_names:
    degrees[name] = G.degree(name)

with open('degrees.json', 'w') as df:
    json.dump(degrees, df)

