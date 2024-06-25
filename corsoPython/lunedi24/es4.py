#Scrivete un programma che chiede un numero all’utente e restituisce un dizionario con il quadrato del numero,
#se è pari o dispari e quante cifre contiene. Esempio: Numero 12. 
#Risultato {‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }

# Chiedi all'utente di inserire un numero
numero = int(input("Inserisci un numero: "))

# Calcola il quadrato del numero
quadrato = numero ** 2

# Determina se il numero è pari o dispari
if numero % 2 == 0:
    pari_dispari = "pari"
else:
    pari_dispari = "dispari"

# Conta il numero di cifre del numero
num_cifre = len(str(abs(numero)))

# Crea il dizionario con le informazioni richieste
risultato = {
    'quadrato': quadrato,
    'pari o dispari': pari_dispari,
    'n. cifre': num_cifre
}

# Stampa il dizionario
print(risultato)
