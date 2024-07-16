import numpy as np

# Creare un array 1D di 20 numeri interi casuali compresi tra 10 e 50
array_casuale = np.random.randint(10, 51, size=20)

# Estrarre i primi 10 elementi dell'array
primi_10_elementi = array_casuale[:10]

# Estrarre gli ultimi 5 elementi dell'array
ultimi_5_elementi = array_casuale[-5:]

# Estrarre gli elementi dall'indice 5 all'indice 15 (escluso)
primi_5_fino_15 = array_casuale[5:15]

# Estrarre ogni terzo elemento dell'array
ogni_terzo_elemento = array_casuale[::3]

# Modificare gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99
array_casuale[5:10] = 99


print("Array casuale: ", array_casuale)
print("Primi 10 elementi: ", primi_10_elementi)
print("Ultimi 5 elementi: ", ultimi_5_elementi)
print("Dal 5^ elemento fino al 15^ elemento: ",primi_5_fino_15)
print("Ogni terzo elemento:", ogni_terzo_elemento)
print("Array modificato:", array_casuale)