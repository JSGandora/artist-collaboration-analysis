import requests
import json

f = open('rappers.txt', 'r')
rappers = [x.strip('\n') for x in f.readlines()]
rapper_data = {}

count = 0
rapper_popularities = {}
for rapper in rappers:
    count +=1
    if True:
        print rapper
        parameters = {'q': rapper, 'type': 'artist'}

        search = requests.get('https://api.spotify.com/v1/search', params=parameters)
        if len(search.json()['artists']['items'][0]) == 0:
            print rapper + 'has a problem'
        id = search.json()['artists']['items'][0]['id']
        name = search.json()['artists']['items'][0]['name']
        popularity = search.json()['artists']['items'][0]['popularity']
        # The following extracts the popularity of the artists
        rapper_popularities[rapper] = popularity
        print popularity

        # The following extracts all tracks of the artists
        # artist_albums = requests.get('https://api.spotify.com/v1/artists/' + id + '/albums')
        # tracks = []
        #
        # # code to go through all the songs of an artist at current_page
        # current_page = artist_albums
        # while not current_page == 'none':
        #     for album in current_page.json()['items']:
        #         # operations on each album
        #         albumID = album['id']
        #         album_request = requests.get('https://api.spotify.com/v1/albums/' + albumID + '/tracks')
        #         current_album_page = album_request
        #         while not current_album_page == 'none':
        #             for item in current_album_page.json()['items']:
        #                 print item['name'], item['href']
        #                 # operations on each track in the album
        #                 appearsOn = False
        #                 for artist in item['artists']:
        #                     if artist['id'] == id:
        #                         appearsOn = True
        #                 if appearsOn:
        #                     tracks.append(item)
        #             next_album_page = current_album_page.json()['next']
        #             if next_album_page is not None:
        #                 current_album_page = requests.get(next_album_page)
        #             else:
        #                 current_album_page = 'none'
        #     next = current_page.json()['next']
        #     if next is not None:
        #         current_page = requests.get(next)
        #     else:
        #         current_page = 'none'
        #
        # rapper_data[rapper] = tracks
        # with open('rapper_stats'+str(count)+'.json', 'w') as fp:
        #     json.dump(rapper_data, fp)
        # rapper_data = {}

    with open('popularities.json', 'w') as fp:
        json.dump(rapper_popularities, fp)

f.close()
