#primo esercizio
numero_scelto = int(input ("Scegli un numero: ")) #specifica che è intero perche è stringa di default
numero_definito = 90
if numero_scelto > numero_definito:
    print("Il numero scelto è maggiore di quello definito")
elif numero_scelto < numero_definito:
    print("Il numero scelto è minore di quello definito")
else:
    print("Hai indovinato!")