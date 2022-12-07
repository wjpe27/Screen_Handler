
import json

filename = "your_file.json"
lst = [{"ID": 1}, {"miguel"}, {"edad:": 15}]
entry = [{"ID:": 2}, {"pedro"}, {"edad:": 17}]



with open(filename, "w") as file:
    json.dump(lst, filename)



with open(filename, "w") as file:
    lst.append(entry)
    json.dump(lst, file)