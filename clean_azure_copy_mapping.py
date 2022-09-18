import json
import re

# Opening JSON file
filename = input('Filename?')

characterToCheck = [",", ";", "{", "}", "(", ")", "\n", "\t", "=", " "]
#characterToCheck = ",;{()}\n\t= "

def replace(str, characterList):
    x = str
    for ch in characterList:
        x = x.replace(ch,"_")
    return x

f = open(filename, 'r')
data = json.load(f)

for i in data['translator']['mappings']:
    if any(char in i['source'] for char in characterToCheck):
        test = i['sink']
        print(test)
        test = replace(test, characterToCheck)
        print(test)
f.close()