# Inizializzazione della variabile somma
somma = 0

# Ciclo di input
while True:
    # Chiedo all'utente di inserire un numero intero
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    
    # Controllo se il numero è 0
    if numero == 0:
        # Se il numero è 0, esci dal ciclo
        break
    
    # Aggiungo il numero alla somma
    somma += numero

# Stampo la somma dei numeri inseriti
print("La somma dei numeri inseriti è:", somma)
