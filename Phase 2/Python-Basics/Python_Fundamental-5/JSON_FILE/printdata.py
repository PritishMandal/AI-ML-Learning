import json

data = {
    "name": "Pritish Mandal",
    "age": 21,
}

with open("data2.json", "w") as f:
    json.dump(data, f)