import requests
import networkx as nx
import matplotlib.pyplot as plt
import json

import json

with open('all_stats.json') as data_file:
    rapper_names = json.load(data_file).keys()

with open('rapper_names.json', 'w') as df:
    json.dump(rapper_names, df)

G = nx.Graph()
Edges = []

for x in range(1, 197):
    with open('rapper_stats'+str(x)+'.json') as data_file:
        tracks = json.load(data_file)
    tracks_info = tracks[tracks.keys()[0]]
    for track in tracks_info:
        for x in range(len(track['artists'])):
            for y in range(x+1, len(track['artists'])):
                if(track['artists'][x]['name'] in rapper_names and track['artists'][y]['name'] in rapper_names):
                    G.add_edge(track['artists'][x]['name'], track['artists'][y]['name'])

pos = nx.spring_layout(G)
# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,width=3)

# labels
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

print 'WE HAVE FINISHED PARSING DATA'

plt.axis('off')
plt.savefig("weighted_graph2.png") # save as png
plt.show() # display