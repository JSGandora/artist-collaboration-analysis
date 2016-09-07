'''
This code generates the collaboration graph centered at a single artist and includes all other artists that contributed
to common albums or songs that the artist in question appears on.
'''

import requests
import networkx as nx
import matplotlib.pyplot as plt

# use the Spotify API to retrieve all the albums of the artist in question
parameters = {'q': 'Starrah', 'type': 'artist'}
search = requests.get('https://api.spotify.com/v1/search', params=parameters)
id = search.json()['artists']['items'][0]['id']
name = search.json()['artists']['items'][0]['name']
artist_albums = requests.get('https://api.spotify.com/v1/artists/' + id + '/albums')

# initialize the collaboration graph
G = nx.Graph()
Edges = []

# set the minimum popularity (as defined by Spotify's popularity metric) for artists to be included in the graph
min_popularity = search.json()['artists']['items'][0]['popularity'] - 10

# code to iterate through the songs of the artist in question
current_page = artist_albums
while not current_page == 'none':
    for album in current_page.json()['items']:
        albumID = album['id']
        album_request = requests.get('https://api.spotify.com/v1/albums/' + albumID + '/tracks')
        current_album_page = album_request
        while not current_album_page == 'none':
            for item in current_album_page.json()['items']:
                print item['name'], item['href']
                for x in range(0, len(item['artists'])):
                    candidate_artist = requests.get('https://api.spotify.com/v1/artists/' + item['artists'][x]['id'])
                    if candidate_artist.json()['popularity'] >= min_popularity:
                        for y in range(x+1, len(item['artists'])):
                            candidate_artist_prime = requests.get('https://api.spotify.com/v1/artists/' + item['artists'][y]['id'])
                            if candidate_artist_prime.json()['popularity'] >= min_popularity:
                                G.add_edge(item['artists'][x]['name'].replace('$', '\$'), item['artists'][y]['name'].replace('$', '\$'))
            next_album_page = current_album_page.json()['next']
            if next_album_page is not None:
                current_album_page = requests.get(next_album_page)
            else:
                current_album_page = 'none'
    next = current_page.json()['next']
    if next is not None:
        current_page = requests.get(next)
    else:
        current_page = 'none'

# draw the Graph
pos = nx.spring_layout(G)
# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,width=3)

# labels
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph2.png") # save as png
plt.show() # display