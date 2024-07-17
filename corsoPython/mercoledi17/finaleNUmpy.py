"""giovedi11\Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 

Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sulla matrice. Le operazioni disponibili includono:

Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma.


Parte DUE: Andare a specializzare per aggiungere nuove operazioni:

Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare il risultato.
Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi della matrice.
"""
import numpy as np

def stampa_menu():
    print("\nMenu:")
    print("1. Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.")
    print("2. Estrarre e stampare la sotto-matrice centrale.")
    print("3. Trasporre la matrice e stamparla.")
    print("4. Calcolare e stampare la somma di tutti gli elementi della matrice.")
    print("5. Moltiplicazione elemento per elemento con un'altra matrice.")
    print("6. Calcolo della media degli elementi della matrice.")
    print("7. Calcolare la matrice inversa.")
    print("8. Applicare una funzione matematica a tutti gli elementi della matrice.")
    print("9. Filtrare e visualizzare solo gli elementi della matrice che soddisfano una determinata condizione.")
    print("10. Uscire dal programma.")

def crea_matrice():
    righe = int(input("Inserisci il numero di righe: "))
    colonne = int(input("Inserisci il numero di colonne: "))
    matrice = np.random.randint(1, 10, size=(righe, colonne))
    print("Matrice creata:\n", matrice)
    return matrice

def estrai_sottomatrice_centrale(matrice):
    righe, colonne = matrice.shape # matrice.shape restituisce una tupla contenente il numero di righe e colonne della matrice
    if righe < 3 or colonne < 3:
        print("La matrice è troppo piccola per avere una sotto-matrice centrale.")
        return
    start_riga = (righe - 3) // 2 # ottengo indice di inizio per le colonne
    start_colonna = (colonne - 3) // 2 #o ttengo indice di inizio per le colonne
    # utilizzo slicing per estrarre 3 righe e 3 colonne
    sottomatrice_centrale = matrice[start_riga:start_riga + 3, start_colonna:start_colonna + 3]
    print("Sotto-matrice centrale:\n", sottomatrice_centrale)

def trasponi_matrice(matrice):
    trasposta = np.transpose(matrice)
    print("Matrice trasposta:\n", trasposta)

def somma_elementi(matrice):
    somma_totale = np.sum(matrice)
    print("Somma di tutti gli elementi della matrice:", somma_totale)

def moltiplicazione_elementwise(matrice):
    righe, colonne = matrice.shape
    seconda_matrice = np.random.randint(1, 10, size=(righe, colonne))
    print("Seconda matrice:\n", seconda_matrice)
    risultato = np.multiply(matrice, seconda_matrice) # esegue la moltiplicazione elemento per elemento tra la matrice originale e la seconda matrice.
    print("Risultato della moltiplicazione elemento per elemento:\n", risultato)

def calcola_media(matrice):
    media = np.mean(matrice)
    print("Media di tutti gli elementi della matrice:", media)

def calcola_inversa(matrice):
    if matrice.shape[0] != matrice.shape[1]: # per essere quadrata numero righe == numero colonne
        print("La matrice non è quadrata, quindi non è invertibile.")
        return
    try: # provo a calcolare l'inversa
        inversa = np.linalg.inv(matrice)
        print("Matrice inversa:\n", inversa)
    except np.linalg.LinAlgError: # se la matrice è singolare non è invertibile
        print("La matrice non è invertibile.")

def applica_funzione(matrice):
    funzioni = {
        'sin': np.sin,
        'cos': np.cos,
        'exp': np.exp
    }
    print("Funzioni disponibili: sin, cos, exp")
    scelta_funzione = input("Scegli una funzione da applicare: ").strip().lower()
    if scelta_funzione in funzioni:
        risultato = funzioni[scelta_funzione](matrice)
        print(f"Matrice con {scelta_funzione} applicato a tutti gli elementi:\n", risultato)
    else:
        print("Funzione non valida.")

def filtra_elementi(matrice):
    condizione = input("Inserisci una condizione: ").strip()
    try:
        elementi_filtrati = matrice[eval(f"matrice {condizione}")]
        print(f"Elementi che soddisfano la condizione {condizione}:\n", elementi_filtrati)
    except:
        print("Condizione non valida.")

def main():
    matrice = None
    
    while True:
        stampa_menu()
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            matrice = crea_matrice()
        elif scelta == '2':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                estrai_sottomatrice_centrale(matrice)
        elif scelta == '3':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                trasponi_matrice(matrice)
        elif scelta == '4':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                somma_elementi(matrice)
        elif scelta == '5':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                moltiplicazione_elementwise(matrice)
        elif scelta == '6':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                calcola_media(matrice)
        elif scelta == '7':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                calcola_inversa(matrice)
        elif scelta == '8':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                applica_funzione(matrice)
        elif scelta == '9':
            if matrice is None:
                print("Prima crea una matrice.")
            else:
                filtra_elementi(matrice)
        elif scelta == '10':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main() # main da eseguire solo se script viene eseguito direttamente
