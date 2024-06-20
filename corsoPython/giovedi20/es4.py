controllo = True

while controllo:
    lista = []
    scelta = int(input("Inserisci una lista di numeri: "))

    #divido stringa di input in una lista di stringhe
    lista_str = scelta.split(",")

    #lista vuota
    lista_numeri = []

    #itero su ciascun elemento
    for i in lista: #i è il contatore
        numero = int(i) #converto in intero 
        quadrato = i ** 2
        quadrati.append(quadrato)
    print(quadrato)
controllo = False

    
