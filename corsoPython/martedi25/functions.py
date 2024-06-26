numeri = [1,2,3,4,5,6,7,8,]

def numeri_pari(a):
    return a%2 == 0

numeri_true = []
for numero in numeri:
    numeri_true.append(numeri_pari(numero))

numeri_true = list(map(numeri_pari,numeri))
print(numeri_true)

#nuova lista con soli elementi PARI
lista_numeri_pari = []
for numero in numeri:
    if numeri_pari(numero):
        lista_numeri_pari.append(numero)

lista_numeri_pari = list(filter(numeri_pari,numeri))
print(lista_numeri_pari)