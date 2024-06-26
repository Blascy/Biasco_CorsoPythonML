#Scrivete un programma che utilizza il cifrario di Cesare per criptare una parola o decriptarla.
#Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare ciascuna lettera di 
# una certa quantità di posti nell'alfabeto. Per utilizzarlo, si sceglie una chiave (scelta dall’utente) 
# che rappresenta il numero di posti di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, 
# se si sceglie una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via. Per decifrare
#  un messaggio cifrato con il cifrario di Cesare bisogna conoscere la chiave utilizzata e 
# spostare ogni lettera indietro di un numero di posti corrispondente alla chiave.

def cifrario_cesare(testo, chiave, metodo):
    risultato = ""
    # Itera su ciascun carattere nella stringa
    for char in testo:
        if char.isalpha():  # Verifica se il carattere è una lettera
            # Determina il punto di partenza (A o a)
            punto_di_partenza = ord('A') if char.isupper() else ord('a')
            # Calcola la nuova posizione del carattere
            if metodo == "cripta":
                nuova_posizione = (ord(char) - punto_di_partenza + chiave) % 26
            elif metodo == "decripta":
                nuova_posizione = (ord(char) - punto_di_partenza - chiave) % 26
            nuovo_char = chr(punto_di_partenza + nuova_posizione)
            risultato += nuovo_char
        else:
            risultato += char  # Mantiene i caratteri non alfabetici invariati
    return risultato

# Chiede all'utente di inserire una stringa
testo = input("Inserisci una parola o frase: ")
# Chiede all'utente di inserire la chiave
chiave = int(input("Inserisci la chiave (numero di posizioni): "))
# Chiede all'utente di scegliere se criptare o decriptare
metodo = input("Vuoi 'cripta' o 'decripta' il messaggio?: ").strip().lower()

# Verifica che l'input del metodo sia corretto
if metodo not in ["cripta", "decripta"]:
    print("Metodo non valido. Scegli 'cripta' o 'decripta'.")
else:
    # Esegue il cifrario di Cesare
    risultato = cifrario_cesare(testo, chiave, metodo)
    print("Risultato:", risultato)
