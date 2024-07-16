import numpy as np

token = True

while token:
    
    # Crea un array di 12 numeri equidistanti tra 0 e 1
    array_linspace = np.linspace(0, 1, 12)

    # Cambia la forma dell'array a una matrice 3x4
    matrice_3x4_linspace = array_linspace.reshape(3, 4)

    # Genera una matrice 3x4 di numeri casuali tra 0 e 1
    matrice_casuale_3x4 = np.random.rand(3, 4)

    # Calcola la somma degli elementi di entrambe le matrici
    somma_matrice_linspace = np.sum(matrice_3x4_linspace)
    somma_matrice_casuale = np.sum(matrice_casuale_3x4)

    # Stampa le matrici e le loro somme
    print("Matrice 3x4 creata con linspace:")
    print(matrice_3x4_linspace)
    print("\nSomma degli elementi della matrice linspace:", somma_matrice_linspace)

    print("\nMatrice 3x4 di numeri casuali:")
    print(matrice_casuale_3x4)
    print("\nSomma degli elementi della matrice casuale:", somma_matrice_casuale)

    # Chiedi all'utente se vuole ripetere
    scelta = input("Vuoi ripetere? (si/no): ").strip().lower()
    if scelta != 'si':
        token = False
