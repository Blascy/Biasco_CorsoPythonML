lista = ["ciao", "a", "tutti"]
frutta = ["mela","banana","pera","ciliegia"]
frutta_e = [frutto for frutto in frutta if "e" in frutto]

for frutto in frutta:
    if "e" in frutto:
        frutta_e.append(frutto)



print(frutta_e)

stringa = "ciao-a-tutti" #elenco di caratteri
stringa2=stringa[:4]
lista3=list(range(12,1,-2))

print(lista3)
for parola in lista:
    print("")
    print(parola)#stampa parola per parola con spazi
print(stringa2) #stampa ciao
print("ciao" in lista) #stampa true