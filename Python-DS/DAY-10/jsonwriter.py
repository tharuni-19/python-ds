import json #in json the value should be in dictionary
data={
    "Name":"Tharunika",
    "Age":"Nineteen"
}
with open("jsonData.json","w")as f:
    json.dump(data,f,indent=4)
