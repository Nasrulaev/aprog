import json
with open("data.json","rt",encoding = "utf-8") as f:
	js = f.read()
dictionary = json.loads(js)
print(dictionary["virus"]["name"] = "Руслан")
js2 =