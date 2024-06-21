#Chieda all'utente di inserire un numero intero positivo n.
#Se il numero inserito non è positivo, chieda nuovamente l'inserimento fino a quando non viene inserito un numero positivo.
#Una volta ottenuto un numero positivo n, il programma dovrà:
#Stampare tutti i numeri pari da 0 a n inclusi.
#Calcolare e stampare la somma di tutti i numeri dispari da 0 a n inclusi.
#terminare solo dopo tre tentativi ("hai finito i tentativi") o dopo che una soma totale supera 250 ("hai vinto")

tentativi_rimasti = 3
somma_dispari = 0

while tentativi_rimasti > 0:
    n = int(input("Inserisci un numero intero positivo: "))
    
    if n <= 0:
        print("Devi inserire un numero intero positivo.")
        tentativi_rimasti -= 1
        if tentativi_rimasti == 0:
            print("Hai finito i tentativi.")
            break
        else:
            continue
    
    print(f"Numeri pari da 0 a {n}:")
    for i in range(0, n + 1, 2):
        print(i, end=' ')
    print()  # Stampa una riga vuota
    
    for i in range(1, n + 1, 2):
        somma_dispari += i
    
    print(f"Somma dei numeri dispari da 0 a {n}: {somma_dispari}")
    
    if somma_dispari > 250:
        print("Hai vinto!")
        break
    
    tentativi_rimasti -= 1

if tentativi_rimasti == 0 and somma_dispari <= 250:
    print("Hai finito i tentativi.")

