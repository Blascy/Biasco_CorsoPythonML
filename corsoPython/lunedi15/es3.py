import numpy as np

token = True

while token:
    arr = np.arange(10, 50)  # Stampa da 10 a 49
    arr1 = np.arange(10.0, 50.0)
    print(arr)
    print("Tipo di dati: ", arr.dtype)
    print("Tipo di dati: ", arr1.dtype)
    print("Forma dell'array: ", arr.shape)

    scelta = input("Vuoi ripetere? (si/no): ")
    if scelta == "no":
        token = False
    elif scelta == "si":
        token = True
    else:
        print("Risposta non valida, per favore rispondi 'si' o 'no'.")

