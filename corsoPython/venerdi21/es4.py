#Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:
# Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
# Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1an.
# Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
# Utilizzare una struttura if per determinare sen è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.

# Chiedi all'utente di inserire un numero intero positivo
while True:
    n = int(input("Inserisci un numero intero positivo: "))
    if n > 0:
        break
    else:
        print("Il numero deve essere positivo. Riprova.")

# Calcolare e stampare la somma dei numeri pari da 1 a n
somma_pari = 0
for i in range(2, n + 1, 2):
    somma_pari += i
print("La somma dei numeri pari da 1 a", n, "è:", somma_pari)

# Stampare tutti i numeri dispari da 1 a n
print("I numeri dispari da 1 a", n, "sono:")
for i in range(1, n + 1, 2):
    print(i, end=' ')
print()

# Determinare se n è un numero primo
if n < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

if primo:
    print(n, "è un numero primo.")
else:
    print(n, "non è un numero primo.")
