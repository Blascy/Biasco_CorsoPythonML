"""Numpy fondamentalmente è una libreria di python che fornisce supporto per array multidimensionali e matrici, 
inoltre implementa funzioni matematiche per operare su questi array in modo efficiente. Le operazioni aritmetiche 
sui vettori di NumPy vengono effettuate in modo vettoriale. 
Le operazioni aritmetiche su array di NumPy, come `np.add()`, `np.subtract()`, `np.multiply()`, e `np.divide()`, 
sono eseguite in modo vettoriale, il che significa che possono essere applicate a interi array senza la necessità di 
loop espliciti. NumPy offre anche funzioni matematiche come `np.sin()`, `np.cos()`, `np.exp()`, e `np.log()`, e 
funzioni statistiche come `np.mean()`, `np.median()`, `np.std()`, e `np.var()`.
"""
#Operazioni matematiche: 

f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
print(np.add(f, g))
# Output [5 7 9]
print(np.subtract(f, g))
# Output [-3 -3 -3]
print(np.multiply(f, g))
# Output [ 4 10 18]
print(np.divide(f, g))
# Output [0.25 0.4  0.5 ]

#Manipolazione di array:

h = np.arange(6)
i = h.reshape((2, 3))
print(i)
# Output [[0 1 2]
# [3 4 5]]

#Indicizzazione e slicing:

o = np.array([1, 2, 3, 4, 5])
print(o[0])
# Output 1
print(o[1:3])
# Output [2 3]

#Creazione di array

import numpy as np
a = np.array([1, 2, 3])
print(a)
# Output: [1 2 3]

d = np.arange(0, 10, 2)
print(d)
# Output: [0 2 4 6 8]
