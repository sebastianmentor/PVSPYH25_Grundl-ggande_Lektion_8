# Skapar en lista med [0,1,...8,9]!!!
list_of_numbers =  []
for i in range(10):
    list_of_numbers.append(i)

# Vi kan skriva kod som tex loopar igenom något och 
# vi kan då skriva varje objekt för sig till filen
with open('my_file2.txt', 'w') as f:
    for number in list_of_numbers:
        f.write(f'{number}->{number**2}->{number**3}->{number**4}\n')
            

with open('my_file2.txt', 'r') as f:
    dict_kvadrat = {}
    dict_kub = {}
    dict_upphöjt_i_fyra = {}
    for line in f.readlines():
        # 2->4->8->16\n
        line = line.strip()
        # 2->4->8->16
        list_line = line.split("->")
        # ['2', '4', '8', '16']
        int_lista = []
        for tal in list_line:
            int_lista.append(int(tal))

        list_line = int_lista
        dict_kvadrat[list_line[0]] = list_line[1]
        dict_kub[list_line[0]] = list_line[2]
        dict_upphöjt_i_fyra[list_line[0]] = list_line[3]



print(dict_kvadrat)
print(dict_kub)
print(dict_upphöjt_i_fyra)