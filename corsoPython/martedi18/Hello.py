# variabili 
eta = 23
nome = "Andrea"
animale = "zebra"
eta_animale = 16.0
nomignolo = input("Inserisci il tuo nome: ") #esempio di input
print("Ciao", nomignolo ,"benvenuto in python!") #stampa di input
print("Mi chiamo", nome ,"e ho", eta, "anni") #stampa di output

# operazioni 
print(1 + 5)
print(6/2)
print(3 ** 3) # potenza

# commentare è fondamentale, a quel codice lavoreranno anche altri dipendenti che devono capire il codice
# le variabili sono contenitori per i valori, che possono essere di diversi tipi
# i nomi delle variabili devono essere descrittivi
# variabili non possono avere spazi
# possono includere solo lettere,...
# = per assegnare un valore

# variabile
print("Ho una animale di" )

# virgola non si usa, si usa il punto
# stringhe: si parte da 0
s = "Python"
print(s[0]) #stampa p
print(s[1]) #stampa y

# posso concatenare le stringhe col +
saluto = "Ciao!"
messaggio = saluto + " " + nome
print(messaggio)

# stringhe: metodi len(); upper(); lower(); split(); replace();
s = "Ciao Mondo!"
print(len(s))
print(s.upper())
print(s.lower())
print(s.replace('mondo', 'universo')) #output:Ciao universo!

#booleani lettera maiuscola e minuscola True e False
x = 5
y = 10
z = 7

print(x < y and y > z) #stamperà true
print(x < y or z > y) #stampa true
print(not(x < y)) #stampa false

# operatori == (uguale a); != (diverso da); < ; > ; >= ; <= .
print(x == 5)
print(x != y)
print(x < y)

# liste [] contengono valori di diversi tipi, come stringhe, interi, tipi, booleani,rappresentate dal tipo di dato List

# Controllo del flusso:if, elif, else, for, while
numero = 10
if numero > 0:
    print("Il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("Il numero è negativo")
else:
    print("Il numero è negativo")

#primo esercizio
numero_scelto = int(input ("Scegli un numero: ")) #specifica che è intero perche è stringa di default
numero_definito = 90
if numero_scelto > numero_definito:
    print("Il numero scelto è maggiore di quello definito")
elif numero_scelto < numero_definito:
    print("Il numero scelto è minore di quello definito")
else:
    print("Hai indovinato!")


#secondo esercizio
if numero_scelto > numero_definito:
    print("Il numero scelto è maggiore di quello definito,ritenta")
    numero_scelto = int(input ("Scegli un numero: "))
elif numero_scelto < numero_definito:
 print("Il numero scelto è minore di quello definito,ritenta")
 numero_scelto = int(input ("Scegli un numero: "))
elif numero_scelto < 0:
    print("E' negativo")
elif:
    print

