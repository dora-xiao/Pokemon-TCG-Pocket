import json

cardfile = open("data/inventory.csv", "r", encoding='utf-8')
lines = cardfile.readlines()

result = {}

for line in lines:
    vals = line.replace("\n", "").split(",")
    result[f"{vals[0]}:{vals[1]}"] = vals[2];

with open('data/inventory.json', 'w') as f:
    json.dump(result, f)