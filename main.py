import json

f = open('C:\Users\joshr\Documents\GitHub\StockBot\sample-stocks-data.json')

data = json.load(f)

# Iterating through the json

for i in data['results']:
    print(i)

# Closing file
f.close()