import json
import re

# Opening JSON file
filename = input('Filename?')

characterToCheck = [",", ";", "{", "}", "(", ")", "\n", "\t", "=", " "]
#characterToCheck = ",;{()}\n\t= "

def clean(str, characterList):
    x = str.strip()
    for ch in characterList:
        x = x.replace(ch,"_")
    return x

with open(filename, 'r') as f:
    data = json.load(f)

for i in data['translator']['mappings']:
    if any(char in i['source'] for char in characterToCheck):
        i['sink'] = clean(i['sink'], characterToCheck)
f.close()

filename_mod = str(filename) + '.New'
with open(filename_mod, 'w') as f_mod:
    json.dump(data, f_mod, indent=4)
f_mod.close()