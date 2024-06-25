# Chiedi all'utente di inserire una lista di parole separate da spazi
lista = input("Inserisci una lista di parole: ")

# Dividi la stringa inserita in una lista di parole
parole = lista.split()

# Inizializza una lista vuota per memorizzare le lunghezze delle parole
lunghezze = []

# Itera attraverso ogni parola nella lista e calcola la lunghezza
for parola in parole:
    lunghezze.append(len(parola))

# Stampa la lunghezza di ciascuna parola
for parola, lunghezza in zip(parole, lunghezze):
    print(f"La parola '{parola}' ha {lunghezza} caratteri.")

#ALTRA VERSIONE 
parole =[]

while True:
parola = input("Inserisci una parola: ")
parole.append(parola)

scelta = input("Vuoi inserire un altra parola?")
if scelta.lower() == "no":
break

lunghezze = []
for parola in parole:
lunghezza = len(parola)
lunghezze.append(lunghezza)

print("Le lungezze delle parole inserite sono: " , lunghezze)