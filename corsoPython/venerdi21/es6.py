import random

# Genera un numero casuale compreso tra 1 e 100
numero_casuale = random.randint(1, 100)
scelta = int(input("Scegli un numero: "))


if scelta == numero_casuale:
    print("Complimenti hai trovato il numero")
elif scelta > numero_casuale:
    print("Scegli un numero piu basso")
elif scelta < numero_casuale:
    print("Scegli un numero piu alto")
else:
    scelta = int(input("Ritenta, inserisci numero: "))


def indovina():
    numero_da_indovinare = 50
    controllo = True
    numero = 0

    while controllo:
        print("Indovina il numero compreso tra 0 e 50: ")
        scelta = int(input("Scegli un numero: "))

        if scelta == 50:
            print("Complimenti! Numero trovato")
            break # cosi quando lo trovi si ferma
        elif scelta < 50:
            ("Sbagliato! Il numero è piu alto")
        elif scelta > 50:
            print("Sbagliato! Il numero è più basso.")

indovina()
        


