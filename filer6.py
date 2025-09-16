# Exempel på hur vi kontrollerar om filer existerar innan vi 
# försöker koppla upp oss till dem!
import os


data = []
# Returnerar True om filen finns
if os.path.exists('my_file4.txt'):
    with open('my_file2.txt', 'r') as f:
        for line in f:
            data.append(line)
# Annars finns filen inte och vi vill 
else:
    print('file not found!')
    
print(data)