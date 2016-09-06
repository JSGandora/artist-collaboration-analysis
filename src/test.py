
# import networkx as nx
# import matplotlib.pyplot as plt
# G=nx.Graph()#  G is an empty Graph
# Nodes=['$2$', 'a', '2']
# G.add_nodes_from(Nodes)
# Edges=[('$2$', 'a')]
# G.add_edges_from(Edges)
#
# pos = nx.spring_layout(G)
# # nodes
# nx.draw_networkx_nodes(G,pos,node_size=700)
#
# # edges
# nx.draw_networkx_edges(G,pos,width=3)
#
# # labels
# nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
#
# print 'WE HAVE FINISHED PARSING DATA'
#
# plt.axis('off')
# plt.savefig("weighted_graph.png") # save as png
# plt.show() # display

# how to read json file

# import json
#
# with open('all_stats.json') as data_file:
#     data = json.load(data_file)

import plotly.graph_objs as go
import plotly.plotly as py

import numpy as np

trace1 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size='16',
        color = np.random.randn(500), #set color equal to a variable
        colorscale='Viridis',
        showscale=True
    )
)
data = [trace1]

plot_url = py.plot(data, filename='basic-line')