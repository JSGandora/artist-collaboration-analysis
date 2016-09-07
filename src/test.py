import json

with open('degrees.json') as data_file:
    degree = json.load(data_file)

for name in degree.keys():
    if degree[name] == {}:
        degree[name] = 0

import operator
degree = sorted(degree.items(), key = operator.itemgetter(1))

for pair in degree:
    print pair[0]

for pair in degree:
    print pair[1]
