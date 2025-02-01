import json
x = open("myjson.json")
y = x.read()
x.close()

z = json.loads(y)

print(z["name"])