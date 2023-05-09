
#OPENAI_API_KEY = "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"

import json

filename = "output.txt"

dict1 = {}

with open(filename) as f:
    for line in f:
        command, descrition = line.strip().split(None, 1)
        dict1[command] = descrition

output_file = open("test-1.json" , "w")
json.dump(dict1, output_file, indent= 4, sort_keys= False)
output_file.close()

