# Idrottshallen! En svår nöt att knäcka!

TENNIS = 1
BOWLING = 2
BADMINTON = 3
SPORTS = {1: "Tennis",
          2: "Bowling",
          3: "Badminton"}

BANA_1 = 1
BANA_2 = 2
BANA_3 = 3
BANA_4 = 4
BANA_5 = 5


idrottshall = {TENNIS: None,
               BOWLING: None,
               BADMINTON: None}

# flera banor (olika antal) som sedan ska ha olika tider som ska kunna bokas!

def skapa_tidsbokning():
    tidsbokning = {}
    for tid in range(9,22):
        tidsbokning[tid] = None

    return tidsbokning

def skapa_banor(antal):
    banor = {}
    totalt_antal_banor = antal + 1
    for bannummer in range(1, totalt_antal_banor):
        banor[bannummer] = skapa_tidsbokning()

    return banor


idrottshall[TENNIS] = skapa_banor(4)
idrottshall[BOWLING] = skapa_banor(3)
idrottshall[BADMINTON] = skapa_banor(5)


print("Välkommen till Bengans idrottshall")
while True:
    print("1. Boka")
    print("2. Avboka")
    print("3. Lediga tider")
    print("4. Skriv ut allt")
    print("0. Avsluta")

    choice = input("Gör ett val: ")

    if choice == "1":
        while True:
            print("Vad vill du boka för sport")
            print("1. Tennis")
            print("2. Bowling")
            print("3. Badminton")
            sport = input("Välj önskad sport: ")

            if sport.isdigit() and 1 <= int(sport) <= 3:
                sport = int(sport)

                banor = idrottshall[sport]

                print("Välj bana: ")                
                for bana in banor:
                    print(f"Bana {bana}")

                önskad_bana = input(">>>")

                if önskad_bana.isdigit() and int(önskad_bana) in banor:
                    önskad_bana = int(önskad_bana)
                    tidsbokning = banor[önskad_bana]
                    
                    # ett set()
                    lediga_tider = set()

                    for tid, bokad in tidsbokning.items():
                        if not bokad:
                            lediga_tider.add(tid)

                    if lediga_tider:
                        while True:
                            for ledig_tid in lediga_tider:
                                print(f"Ledig tid kl {ledig_tid}")

                            boka_tid = input("Ange önskad tid:")

                            if boka_tid.isdigit() and int(boka_tid) in lediga_tider:
                                boka_tid = int(boka_tid)
                                tidsbokning[boka_tid] = "Bokad"
                                break
                        break
                    else:
                        print("Alla tider bokade tyvärr!")

            else:
                print("Felaktigt val!")
            


    elif choice == "2":
        ...

    elif choice == "3":
        ...

    elif choice == "4":
        for sport, banor in idrottshall.items():
            print(f"{SPORTS[sport]}:")
            for bana, tidsbokning in banor.items():
                print(f"\tBana {bana}")
                for tid, bokning in tidsbokning.items():
                    print(f"\t\t{tid}-{bokning}")

    elif choice == "0":
        break

    else:
        print("Ogiltligt val!")
    
