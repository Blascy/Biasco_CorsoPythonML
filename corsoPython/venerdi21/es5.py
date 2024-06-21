import random

# Funzione per determinare se un numero è primo
def è_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Chiedi all'utente di inserire un numero intero positivo
while True:
    n = int(input("Inserisci un numero intero positivo: "))
    if n > 0:
        break
    else:
        print("Il numero deve essere positivo. Riprova.")

# Genera una lista di numeri interi casuali tra 1 e n
numeri = [random.randint(1, n) for _ in range(n)]
print("Lista dei numeri generati:", numeri)

# Calcolare e stampare la somma dei numeri pari nella lista
somma_pari = 0
for num in numeri:
    if num % 2 == 0:
        somma_pari += num
print("La somma dei numeri pari nella lista è:", somma_pari)


# Stampare tutti i numeri dispari nella lista
print("I numeri dispari nella lista sono:")
for num in numeri:
    if num % 2 != 0:
        print(num, end=' ')
print()

# Stampare tutti i numeri primi nella lista utilizzando la funzione è_primo
print("I numeri primi nella lista sono:")
for num in numeri:
    if è_primo(num):
        print(num, end=' ')
print()

# Calcolare la somma di tutti i numeri nella lista
somma_totale = sum(numeri)

# Determinare se la somma di tutti i numeri nella lista è un numero primo
if è_primo(somma_totale):
    print(f"La somma di tutti i numeri nella lista ({somma_totale}) è un numero primo.")
else:
    print(f"La somma di tutti i numeri nella lista ({somma_totale}) non è un numero primo.")

