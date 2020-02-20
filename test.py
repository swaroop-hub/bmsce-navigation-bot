import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for i in data["people"]:
        print("name:"+ i["name"])