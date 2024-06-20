# Variabili iniziali
controllo = True
selezione = input("Ciao! Vuoi iniziare? (si/no): ")
lista_prodotti = ['papera di gomma', 'anello', 'borraccia blu']
acquisti_cliente = []

# Controllo per iniziare il processo
if selezione.lower() == "si":
    while controllo:
        selezione2 = input("Vuoi vedere i prodotti? (si/no): ")
        if selezione2.lower() == "si":
            print("Prodotti disponibili:")
            for prodotto in lista_prodotti:
                print(prodotto)

        # Chiedere se il cliente vuole fare un acquisto
        selezione3 = input("Vuoi acquistare un prodotto? (si/no): ")
        if selezione3.lower() == "si":
            prodotto_acquistato = input("Quale prodotto vuoi acquistare? ")
            if prodotto_acquistato in lista_prodotti:
                acquisti_cliente.append(prodotto_acquistato)
                print(f"Hai acquistato: {prodotto_acquistato}")
            else:
                print("Prodotto non disponibile")

        selezione4 = input("Vuoi vedere i tuoi acquisti? (si/no): ")
        if selezione4.lower() == "si":
            print("I tuoi acquisti: ")
            for acquisto in acquisti_cliente:
                print(acquisto)

        # Chiedere al cliente se vuole continuare
        selezioneFinale = input("Vuoi continuare a vedere i prodotti? (si/no): ")
        if selezioneFinale.lower() != "si":
            controllo = False
    print("Grazie per aver utilizzato il servizio! Arrivederci")

# Aggiunta di alcuni articoli
inventario = []

# Aggiunta di alcuni articoli iniziali
inventario.append(["Papera di gomma", 5, 100])
inventario.append(["Anello", 200, 50])
inventario.append(["Borraccia blu", 15, 30])

# Ciclo per gestire le operazioni dell'inventario
while True:
    print("\nCosa desideri fare?")
    print("1. Mostra l'inventario")
    print("2. Aggiungi un nuovo articolo")
    print("3. Rimuovi un articolo")
    print("4. Aggiorna un articolo")
    print("5. Esci")

    # Scelgo le opzioni elencate, ogni scelta avrà un'azione associata
    scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")
    if scelta == "1":
        print("Inventario:")
        for articolo in inventario:
            print(f"Nome: {articolo[0]}, Prezzo: {articolo[1]}€, Quantità: {articolo[2]}")

    elif scelta == "2":
        nome_articolo = input("Inserisci il nome del nuovo articolo: ")
        esiste = False
        for articolo in inventario:
            if articolo[0].lower() == nome_articolo.lower():
                esiste = True
                break

        if esiste:
            print(f"L'articolo '{nome_articolo}' è già presente nell'inventario.")
        else:
            prezzo_articolo = float(input("Inserisci il prezzo dell'articolo: "))
            quantita_articolo = int(input("Inserisci la quantità disponibile: "))
            inventario.append([nome_articolo, prezzo_articolo, quantita_articolo])
            print(f"Articolo '{nome_articolo}' aggiunto all'inventario.")

    elif scelta == "3":
        nome_articolo = input("Inserisci il nome dell'articolo da rimuovere: ")
        trovato = False
        for articolo in inventario:
            if articolo[0].lower() == nome_articolo.lower():
                inventario.remove(articolo)
                trovato = True
                print(f"Articolo '{nome_articolo}' rimosso dall'inventario.")
                break

        if not trovato:
            print(f"L'articolo '{nome_articolo}' non è presente nell'inventario.")

    elif scelta == "4":
        nome_articolo = input("Inserisci il nome dell'articolo da aggiornare: ")
        trovato = False
        for articolo in inventario:
            if articolo[0].lower() == nome_articolo.lower():
                nuovo_prezzo = float(input("Inserisci il nuovo prezzo dell'articolo: "))
                nuova_quantita = int(input("Inserisci la nuova quantità disponibile: "))
                articolo[1] = nuovo_prezzo
                articolo[2] = nuova_quantita
                trovato = True
                print(f"Articolo '{nome_articolo}' aggiornato.")
                break

        if not trovato:
            print(f"L'articolo '{nome_articolo}' non è presente nell'inventario.")

    elif scelta == "5":
        print("Grazie per aver utilizzato il sistema di gestione dell'inventario.")
        break

    else:
        print("Scelta non valida. Per favore, inserisci un numero da 1 a 5 corrispondente all'azione desiderata.")

