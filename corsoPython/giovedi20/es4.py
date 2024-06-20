# Richiedi una lista di numeri all'utente
input_utente = input("Inserisci una lista di numeri separati da virgole: ")

# Dividi la stringa di input in una lista di stringhe
lista_str = input_utente.split(",")

# Crea una lista vuota per i numeri
lista_numeri = []

# Itera su ciascun elemento della lista di stringhe
for i in lista_str:  # i è il contatore
    # Rimuovi eventuali spazi, converti la stringa in un intero e aggiungilo alla lista dei numeri
    numero = int(i.strip())
    lista_numeri.append(numero)

# Itera su ciascun numero nella lista dei numeri e stampa il quadrato
for numero in lista_numeri:
    # Calcola il quadrato del numero
    quadrato = numero ** 2
    print(f"Il quadrato di {numero} è {quadrato}")
