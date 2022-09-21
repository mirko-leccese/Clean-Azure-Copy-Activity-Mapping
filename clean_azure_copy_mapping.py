import json
import sys

# Defining list of character to check in the JSON file:
characterToCheck = [",", ";", "{", "}", "(", ")", "\n", "\t", "=", " "]

# Defining the cleaning function:
def clean(str, characterList):
    """
    This function trims trailing and leading whitespaces from a string and replace
    any character of the string matching an element of a passed list with a "_"

    Args:
        str (str): a string to clean
        characterList (list): a list of the character to replace

    Returns:
        x (str): a cleaned string
    """
    # Trimming the string
    x = str.strip()

    # Looping over characterList and replace matching elements:
    for ch in characterList:
        x = x.replace(ch,"_")
    print(f"Source field to clean: {str:30s} Sink field cleaned: {x:s}")
    return x

# Asking for JSON filename
filename = input('JSON Filename?\n')

# Opening JSON file and loading data:
try:
    with open(filename, 'r') as f:
        data = json.load(f)
        f.close()
# Exit from the script if file not found:
except FileNotFoundError:
    print('File not found!')
    sys.exit()

# Checking if 'source' field of any 'mappings' array element contains any undesired characters and 
# calling the clean() function to clean it:
for i in data['translator']['mappings']:
    if any(char in i['source'] for char in characterToCheck):
        i['sink'] = clean(i['sink'], characterToCheck)

# Creating a new name for the modified file:
filename_mod = str(filename)[:-5] + '_Cleaned.json'

# Loading the clean JSON code into the new file:
with open(filename_mod, 'w') as f_mod:
    json.dump(data, f_mod, indent=4)
f_mod.close()