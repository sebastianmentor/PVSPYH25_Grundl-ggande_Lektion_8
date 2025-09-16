def funktions_namn():
    print("-"*20)
    print("Vi kör innuti vår funktion!")
    print("Vi beräknar något")
    x = 5 + 10
    print(f"{x=}")
    print("Vi avslutar vår funktion nu och går tillbaka där vi var!")
    en_annan_funktion()
    print("-"*20)

def en_annan_funktion():
    print("*"*20)
    print("Vi kör den andra funktionen nu!")
    print("*"*20)

print(funktions_namn)
print(funktions_namn())
print("Vi fortsätter på rad 11 i vårat program!")

def func_A():
    print("Function A")
    print("Anropar function B")
    func_B()
    print("EXIT A")


def func_B():
    print("Function B")
    print("Anropar function A")
    func_A()
    print("EXIT B")

# func_A()

print("-"*20)
meny_1_counter = 0
meny_2_counter = 0
def meny1():
    global meny_1_counter
    meny_1_counter += 1
    print(f"Meny1 har anropats {meny_1_counter} ggr")
    print("Välj något och går till meny2")
    input("")
    meny2()
    print("Vi är tillbaka från meny 2")
    

def meny2():
    global meny_2_counter
    meny_2_counter += 1
    print(f"Meny2 har anropats {meny_2_counter} ggr")
    print("Vi gör något")
    print("Okej, vi går tillbaka till meny1")
    input("")
    meny1()
    

meny1()