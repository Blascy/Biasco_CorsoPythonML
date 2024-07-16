import numpy as np

token = True

while token:
    # Creare una matrice 2D di dimensioni 6x6 con numeri interi casuali compresi tra 1 e 100
    matrice_casuale = np.random.randint(1, 101, size=(6, 6))

    # Estrarre la sotto-matrice centrale 4x4
    sotto_matrice_centrale = matrice_casuale[1:5, 1:5]

    # Invertire le righe della sotto-matrice centrale
    sotto_matrice_invertita = sotto_matrice_centrale[::-1, :]

    # Estrarre la diagonale principale della matrice invertita
    diagonale_principale = np.diag(sotto_matrice_invertita)

    # Sostituire tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1
    sotto_matrice_modificata = np.where(sotto_matrice_invertita % 3 == 0, -1, sotto_matrice_invertita)

    # Stampare i risultati
    print("Matrice originale 6x6:")
    print(matrice_casuale)
    print("\nSotto-matrice centrale 4x4:")
    print(sotto_matrice_centrale)
    print("\nSotto-matrice centrale con righe invertite:")
    print(sotto_matrice_invertita)
    print("\nDiagonale principale della matrice invertita:")
    print(diagonale_principale)
    print("\nSotto-matrice invertita modificata (multipli di 3 sostituiti da -1):")
    print(sotto_matrice_modificata)

    # Chiedere all'utente se vuole ripetere
    scelta = input("\nVuoi ripetere? (si/no): ").strip().lower()
    if scelta != "si":
        token = False
