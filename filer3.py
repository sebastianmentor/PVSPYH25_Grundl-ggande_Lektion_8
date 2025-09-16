# Vi kan läsa in all data från en fil!
# Varning, är filen stor kan detta va dåligt att göra
with open("my_file2.txt","r") as f:
    data = f.read()
    print(data)

# Vi kan läsa in rad för rad i en fil
with open("my_file2.txt","r") as f:
    lista_med_data = []
    for line in f.readlines():
        # här använder vi strip för att ta bort \n och mellanslag
        # sedan avänder vi split för att dela upp till en lista med strängar
        print(line.strip().split('->'))

# Lite mer anvancerat exempel för hur vi läser in data
# och mappar det till en tupel med texter!
with open("my_file2.txt","r") as f:
    my_dict = {}
    exponet = ("kvadrat", "kuben", "hyperkuben")
    for line in f:
        numbers = line.strip().split('->')
        numbers = [int(num) for num in numbers]
        my_dict[numbers[0]] = {
            key:value for key,value in zip(exponet, numbers[1:])
        }

# loopar igenom våran dictionary
for key, value in my_dict.items():
    print(key, "ger", value)