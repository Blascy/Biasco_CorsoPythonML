with open("file.csv","r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")
print(righe)

elementi = []
for element in righe:
    elementi.append(element.split(","))
    
print(elementi[1][1])