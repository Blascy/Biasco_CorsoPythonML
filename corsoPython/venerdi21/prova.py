# Calcolare e stampare la somma dei numeri pari nella lista
somma_pari = 0
for num in numeri:
    if num % 2 == 0:
        somma_pari += num
print("La somma dei numeri pari nella lista è:", somma_pari)