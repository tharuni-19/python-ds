import json #in json the value should be in dictionary
with open("jsonData.json",'r') as file:
    data=json.load(file)
    print(data)                       

