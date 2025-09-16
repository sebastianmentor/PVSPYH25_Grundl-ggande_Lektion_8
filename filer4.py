# Exempel på hur vi kan arbeta med JSON i python!
import json

# Skapar en komplex data-struktur
my_nest = [
    {1:'2',2:'3',3:'4', 4:'5', 6:6}, 
    {'key': {'key1':'value1','key2':'value2', 'key3':[1,2,3]}}
    ]


# Vi öppnar en kanal till våran fil och därefter 
# använder vi JSON för att skriva ner våran data-struktur
# till json format! Vi ger den vår data, länken f till vår fil
# och en indentering för att det ska se snyggare ut!
with open('my_file3.json','w') as f:
    json.dump(my_nest,f, indent=2)


# Här läser vi in vår data!
with open('my_file3.json', 'r') as f:
    data = json.loads(f.read())

print(data)
print(type(data))
print(data[0]['2'])