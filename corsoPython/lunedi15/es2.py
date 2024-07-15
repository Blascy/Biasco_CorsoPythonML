import numpy as np

#creazione di un array unidimensionale
arr = np.array([1,2,3,4,5])

#utilizzo di alcuni metodi
print("Forma dell'array: ",arr.shape)
print("Dimensione dell'array: ",arr.ndim)
print("Tipo di dati: ",arr.dtype)
print("Numero di elementi: ",arr.size)
print("Somma degli elementi: ",arr.sum())
print("Media degli elementi: ",arr.mean())
print("Valore massimo: ",arr.max())
print("Indice del valore massimo: ",arr.argmax())