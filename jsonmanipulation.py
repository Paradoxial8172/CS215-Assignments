import json

def overwrite(item, value):

    with open("data.json", "r") as f:
        data = json.load(f)
        
        data[item] = value

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

        """
        data = name of dict
        item = key in dict
        value = value in dict
        """
with open("data.json", "r+") as f:
    data = json.load(f)

overwrite("Name", "James")