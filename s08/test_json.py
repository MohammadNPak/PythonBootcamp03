import json

# with open("data.json","r") as f:
#     data = json.load(f)
#     print(data)
# print(data[0]["name"])
    
data = [{"name":"mohamamd","lastname":"dorri"},
        {"name":"sadra","sl":"dorri"}]
with open("data.json","w") as f:
    json.dump(data,f)
