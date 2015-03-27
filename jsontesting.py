import json
data = [10, 15]
with open('data.txt', 'w') as outfile:	json.dump(data, outfile)

