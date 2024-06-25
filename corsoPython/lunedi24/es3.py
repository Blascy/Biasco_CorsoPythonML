# Chiedi all'utente di inserire una stringa
stringa = input("Inserisci una stringa: ")

# Inizializza un dizionario vuoto per memorizzare le frequenze
frequenze = {}

# Itera attraverso ciascun carattere nella stringa
for carattere in stringa:
    # Se il carattere è già nel dizionario, incrementa il conteggio
    if carattere in frequenze:
        frequenze[carattere] += 1
    # Altrimenti, aggiungi il carattere al dizionario con conteggio 1
    else:
        frequenze[carattere] = 1

# Stampa il dizionario delle frequenze
print(frequenze)
