import json

# Opening JSON file
filename = input('Filename?')

f = open(filename, 'r')
data = json.load(f)

for i in data['translator']:
    print(i)

f.close()