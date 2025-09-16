def my_func(a,b,c,d):
    print(f"{a=}, {b=}, {c=}, {d=}")

my_func(3, d=4.4, b="hejsan", c=True)


def my_func2(first, second, third=None):
    if  third:
        print(f"Third argument is here, {third}")
    else:
        print(first, second) 

my_func2("Hejsan", "Hopsan", "Sopsan")

def dont_do_this(a, lista=[]):
    lista.append(a)
    print(lista)

dont_do_this(5)
dont_do_this(7)

def append_to_list(a, lista=None):
    if lista == None:
        return [a]
    else:
        lista.append(a)

def append_to_list_v2(a):
    lista = []
    lista.append(a)
    return lista

animals = {}
last_animal = "finns inte"

def add_animal_to_list(animal):
    if animal not in animals:
        animals[animal] = 1
    else:
        animals[animal] += 1
    global last_animal
    last_animal = animal
    print(last_animal)

add_animal_to_list("ko")
add_animal_to_list("ko")
add_animal_to_list("häst")
print(animals)
print(last_animal)