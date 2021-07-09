import json

with open('variable.json')as file_object:
    data=json.load(file_object)

print(data)

