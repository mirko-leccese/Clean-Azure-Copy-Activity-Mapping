import json
import re

# Opening JSON file
filename = input('Filename?')

characterToCheck = [",", ";", "{", "}", "(", ")", "\n", "\t", "=", " "]
#characterToCheck = ",;{()}\n\t= "

def replace(str, characterList):
    for ch in characterList:
        x = str.replace(ch,"_")
    return x

f = open(filename, 'r')
data = json.load(f)

for i in data['translator']['mappings']:
    if any(char in i['source'] for char in characterToCheck):
        i['sink'] = replace(i['sink'], characterToCheck)
    print(i)
f.close()