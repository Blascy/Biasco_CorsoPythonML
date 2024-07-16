import numpy as np

# Crea un array di numeri equidistanti tra inizio e fine con dimensione_matrice elementi
inizio = float(input("Inserisci il numero da cui vuoi far partire la matrice: "))
fine = float(input("Inserisci il numero a cui vuoi far finire la matrice: "))
dimensione_matrice = int(input("Inserisci la dimensione della matrice: "))
array_linspace = np.linspace(inizio, fine, dimensione_matrice)

# Crea un array di numeri casuali tra 0 e 1 con array2 elementi
array2 = int(input("Quanti numeri tra 0 e 1 vuoi inserire nell'array?: "))
array_random = np.random.random(array2)

# Somma i due array elemento per elemento
scelta = input("Vuoi sommare i due array elemento per elemento? (si/no): ").strip().lower()
if scelta == 'si':
    array_somma = array_linspace + array_random
    somma_totale = np.sum(array_somma)
else:
    array_somma = None
    somma_totale = None
    print("Nessuna somma eseguita.")

# Calcola la somma degli elementi del nuovo array che sono maggiori di un numero scelto
scelta3 = float(input("Scegli un numero per calcolare la somma degli elementi maggiori di questo valore: "))
if array_somma is not None:
    somma_maggiori_di_x = np.sum(array_somma[array_somma > scelta3])
else:
    somma_maggiori_di_x = None
    print("Array di somma non disponibile.")

# Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate
print("\nArray di numeri equidistanti tra", inizio, "e", fine, ":")
print(array_linspace)
print("\nArray di", array2, "numeri casuali tra 0 e 1:")
print(array_random)
if array_somma is not None:
    print("\nArray risultante dalla somma:")
    print(array_somma)
    print("\nSomma totale degli elementi del nuovo array:", somma_totale)
    print("Somma degli elementi del nuovo array che sono maggiori di", scelta3, ":", somma_maggiori_di_x)
