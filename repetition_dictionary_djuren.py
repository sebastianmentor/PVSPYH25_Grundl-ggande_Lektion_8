animals = {}


while True:
    animal = input("Skriv in ett djur eller q för att avsluta: ")

    if animal.lower() == "q":
        break

    animal = animal.capitalize()

    if animal in animals:
        number_of_times = animals[animal]
        animals[animal] = number_of_times + 1
        # animals[animal] += 1
    else:
        animals[animal] = 1

    print(animals)

# Djur | antal
# -----------
# djur | antal

print("Djur      |Antal")
print("----------------")
for animal, count in animals.items():
    print(f"{animal:<10}|{count}")