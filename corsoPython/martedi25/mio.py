#stampa la lunghezza della stringa inserita dall'utente
 
stringa = input("inserisci parola: ")
token = True

while token:
#menu
    decisione = input("Vuoi stampare la lunghezza della stringa?")
    if decisione == "si":
    # Stampa la lunghezza della stringa
        print("La lunghezza della stringa è:", len(stringa))
    elif decisione == "no":
        print("Arrivederci")
        token = False  # Esce dal ciclo impostando il token a False
    else:
        print("Risposta non valida, per favore rispondi 'si' o 'no'.")

    


