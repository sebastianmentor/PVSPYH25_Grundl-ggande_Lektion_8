# Exempel vid användandet av append till en fil!
# Vi har at 'a' gör att vi hamnar sist och kan lägga
# till längst "ner" i filen
# with open('my_file4.txt','a') as f:
#     i = 10
#     f.write(f'{i}->{i**2}->{i**3}->{i**4}\n')

# Vi kan utöka detta och lägga till och sedan läsa i filen#
with open('my_file2.txt','a+') as f:
    # i = 11
    # f.write(f'{i}->{i**2}->{i**3}->{i**4}\n') 
    # Går till början av filen
    f.seek(0)
    # Läser in all data
    data = f.read()

print(data)
