
def create_car(märke, modell, år, pris):
    ny_bil = {"märke": märke,
              "modell":modell,
              "år":år,
              "pris":pris}
    
    return ny_bil

def print_list_of_cars(list_of_cars):
    for bil in list_of_cars:
        print("--------------")
        print("Märke", bil["märke"])
        print("Modell", bil["modell"])
        print("Årsmodell", bil["år"])
        print("Pris", bil["pris"])
    print("--------------")



def main():
    lista_med_bilar = []
    bil1 = create_car("BMW", "M3", 2020, 200_000)
    bil2 = create_car("Volvo", "V90", 2023, 250_000)
    lista_med_bilar.extend([bil1, bil2])

    print("Välkommen till Nisses bilhandel!")
    while True:
        print("1. Lägg till bil")
        print("2. Kolla pris")
        print("3. Skriv ut alla bilar!")
        print("0. Avsluta")
        val = input("Gör ett val: ")

        if val == "1":
            märke = input("Ange märke: ")
            modell = input("Ange modell: ")
            ålder = input("Ange ålder: ")
            pris = input("Ange pris: ")

            ny_bil = create_car(märke, modell, ålder, pris)

            lista_med_bilar.append(ny_bil)

        elif val == "2":
            märke = input("Ange märke för att kolla pris: ")
            bilar_av_intresse = []

            for car in lista_med_bilar:
                if car["märke"] == märke:
                    bilar_av_intresse.append(car)
            
            print_list_of_cars(bilar_av_intresse)

        elif val == "3":
            print_list_of_cars(lista_med_bilar)

        elif val == "0":
            break
        else:
            print("Felaktig input!")


if __name__ == "__main__":
    main()