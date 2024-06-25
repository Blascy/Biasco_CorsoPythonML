# Scrivete una programma che richiede una lista di numeri all’utente e 
# fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], il programma dovrà produrre questa sequenza: ***
#***
#*******
#*********
#*****
def crea_istogramma():
    try:
        # Chiedi all'utente di inserire una lista di numeri separati da spazi
        numeri_input = input("Inserisci una lista di numeri separati da spazi: ")

        # Dividi la stringa inserita in una lista di stringhe e convertile in interi
        numeri = list(map(int, numeri_input.split()))

        # Itera attraverso ogni numero nella lista e stampa l'istogramma
        for numero in numeri:
            print('*' * numero)
    except ValueError:
        print("Per favore, inserisci solo numeri interi separati da spazi.")

crea_istogramma()
