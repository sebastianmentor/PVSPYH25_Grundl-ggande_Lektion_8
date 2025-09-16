# Vad var en dictionary? (hemska svenska ordet ordbok)

# En datastruktur som har keys och values länkade, nyckel-värdepar!
# dvs en unik nyckel kan hämta ett unikt värde!!!!

my_dict = {"id": 666}

my_dict[4] = "sträng"

print(my_dict.get(4))
print(my_dict[4])

# print(my_dict[3])
print(my_dict.get(3, "Nyckeln finns inte!"))

if 3 not in my_dict:
    print("Nyckeln fanns inte i vår dict!")


new_dict = {"id": 1234}
print(new_dict.update(my_dict))
print(new_dict)

for key, val in my_dict:
    new_dict[key] = val

