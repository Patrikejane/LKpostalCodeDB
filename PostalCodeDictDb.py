import json

PostalCodeMap = dict()
with open('postalCodeDB.json', 'r') as f:
    data = json.load(f)
    print(data)
    for i in data:
        print(data[i])
        PostalCodeMap[i] = data[i]


with open('postalCodeMapDB.json', 'w') as f:
    json.dump(PostalCodeMap, f,indent=4)
