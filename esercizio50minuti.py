#variabili iniziali
controllo = True
selezione = input("Ciao! Vuoi iniziare? (si/no): ")
lista_prodotti = ['papera di gomma', 'anello', 'borraccia blu']
acquisti_cliente = []

#controllo per iniziare il processo
if selezione.lower() == "si":
    while controllo:
        selezione2 = input("Vuoi vedere i prodotti? (si/no): ")
        if selezione2.lower() == "si":
            print("Prodotti disponibili:")
            for prodotto in lista_prodotti:
                print(prodotto)

        #chiedere se il cliente vuole fare un acquisto

        selezione3 = input("Vuoi acquistare un prodotto? (si/no): ")
        if selezione3.lower() == "si":
            prodotto_acquistato = input("Quale prodotto vuoi acquistare? ")
            if prodotto_acquistato in lista_prodotti:
                acquisti_cliente.append(prodotto_acquistato)
                print(f"Hai acquistato: {prodotto_acquistato}")
            else:
                    print("Prodotto non disponibile")
            

        selezione4 = input("Vuoi vedere i tuoi acquisti? ")
        if selezione4.lower() == "si":
            print("I tuoi acquisti: ")
            for acquisto in acquisti_cliente:
                print(prodotto_acquistato)

        #Chiedere a cliente se vuole continuare
        selezioneFinale = input("Vuoi continuare a vedere i prodotti? (si/no)")
        if selezioneFinale.lower() != "si":
            controllo = False
        print("Grazie per aver utilizzato il servizio! Arrivederci")
           

inventario = {}
#Aggiunta di alcuni articoli
inventario["papera di gomma"] = {"prezzo": 5, "quantita": 100}
inventario["anello"] = {"prezzo": 200, "quantita": 50}
inventario["borraccia blu"] = {"prezzo": 15, "quantita": 30}

controllo2 = True

aggiunta = input("Vuoi aggiungere nuovi acquisti all'inventario? (si/no): ")
if aggiunta.lower() == "si":
    while controllo2:
        aggiunta2.lower() == "si"
        print("Articoli aggiunti: ")



