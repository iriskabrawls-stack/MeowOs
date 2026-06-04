import json

with open("version.json", "r") as f:
    data = json.load(f)

print("Meow OS", data["version"])