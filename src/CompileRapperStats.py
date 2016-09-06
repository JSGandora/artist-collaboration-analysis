# The code to extract Spotify data saves data for each rapper in different files for the sake of efficiency in case of
# unreliable internet connection.

import json

total_rappers = 196 # There are 196 rappers in total

all_data = {}

for x in range(1, total_rappers+1):
    with open('rapper_stats'+str(x)+'.json') as df:
        data = json.load(df)
        all_data.update(data)

with open('all_stats.json', 'w') as df:
    json.dump(all_data, df)