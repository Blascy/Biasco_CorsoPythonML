#secondo esercizio

numeri_definiti = [1, 30, 50, 90, 21]
print("Che operazione vuoi fare?")
numero_scelto = input("Scegli tra Aggiungere,Rimuovere,Eliminare")

if numero_scelto == "Aggiungere":
    aggiunta = int(input("inserisci un numero: "))
    
while True:
    print("\menu")
    print("1.Aggiungi")
    print("2.Rimuovi")
    print("3.Visualizza")
    print("4.Esci")

    numero_scelto = int(input("Scegli numero: "))

if numero_scelto > numeri_definiti:
    print("Il numero scelto è maggiore di quello definito,ritenta")
numero_scelto = int(input ("Scegli un numero: "))
if numero_scelto < numeri_definiti:
 print("Il numero scelto è minore di quello definito,ritenta")
numero_scelto = int(input ("Scegli un numero: "))
    elif numero_scelto == numeri_definti:
    print("Non è uguale")
    else:
        print("opzione non valida, ritenta!")
