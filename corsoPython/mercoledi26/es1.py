#Scrivete un programma che genera 5 numeri casuali e li salva su un file, l’utente dovrà
#cercare di indovinarne almeno 2 oppure avrà perso
import random

# Funzione per generare 5 numeri casuali e salvarli su un file
def genera_numeri_casuali(filename):
    numeri = [random.randint(1, 100) for _ in range(5)]
    with open(filename, 'w') as file:
        for numero in numeri:
            file.write(f"{numero}\n")
    return numeri

# Funzione per far indovinare i numeri all'utente
def indovina_numeri(filename):
    with open(filename, 'r') as file:
        numeri_corretti = [int(line.strip()) for line in file]

    tentativi = 0
    numeri_indovinati = 0
    print("Prova a indovinare 5 numeri compresi tra 1 e 100.")

    while tentativi < 5:
        try:
            guess = int(input(f"Tentativo {tentativi + 1}: "))
            if guess in numeri_corretti:
                numeri_indovinati += 1
                print("Hai indovinato un numero!")
            else:
                print("Numero sbagliato.")
            tentativi += 1
        except ValueError:
            print("Per favore, inserisci un numero valido.")

    if numeri_indovinati >= 2:
        print(f"Complimenti! Hai indovinato {numeri_indovinati} numeri e hai vinto!")
    else:
        print(f"Mi dispiace, hai indovinato solo {numeri_indovinati} numeri e hai perso.")

# Nome del file dove verranno salvati i numeri
filename = "numeri_casuali.txt"

# Genera i numeri casuali e salvali su un file
numeri = genera_numeri_casuali(filename)
print(f"I numeri casuali generati sono: {numeri}")

# Inizia il gioco di indovinare i numeri
indovina_numeri(filename)
