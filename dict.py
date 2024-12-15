newDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(newDict)
print(newDict["brand"])
print(newDict.get("model"))
print(newDict.keys())
print(newDict.values())
print(newDict.items())

print("brand" in newDict)
newDict["year"] = 2020
newDict.update({"color": "red"})

print(newDict)

newDict.update({"color": "blue", "year": 2021})

print(newDict)

print(newDict.pop("model"))

print(newDict)

print(newDict.popitem())

print(newDict)
