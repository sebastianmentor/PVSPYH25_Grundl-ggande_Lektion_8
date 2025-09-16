# Här öppnar vi filen med "permision" att skriva till filen!
# <as f> gör ett alias av våran koppling till filen!! Tänk variabelnamn
with open("my_file.txt", "w", encoding='utf-8') as f:
    # Här använder vi f som en variabel och anropar funtionen write
    # med strängen som argument
    f.write('Den här texten kommer att skrivas till filen!\n')

# # Här gör vi som ovan fast enda skillnaden är att vi encodar 
# # våran text på ett speciellt sätt , utf-8, för att möjliggöra att
# # vi kan ha tex. å,ä och ö.
# with open("my_file.txt","w", encoding="utf-8") as f:
#     f.write('Nu skriver vi över filen igen\n\t!!!')

# # gör vi såhär rensar vi hela filen fast vi inte gjort något med den!
# with open("my_file.txt","w", encoding="utf-8") as f:
#     pass
