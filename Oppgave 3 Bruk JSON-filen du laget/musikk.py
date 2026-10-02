import json

with open("musikk.json", encoding="utf-8") as fil:
    data = json.load(fil)


print()
print(data["artister"][2]["navn"])
print()
print(data["artister"][0]["navn"]), print(data["artister"][1]["navn"]), print(data["artister"][2]["navn"])
print()
print(data["artister"][0]["sjanger"])
print(data["artister"][2]["album"][0])
print()